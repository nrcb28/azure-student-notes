# Laboratorios avanzados

[←](README.md) · [Núcleo común de estudio](16-common-core.md)

Tres prácticas con el mismo procedimiento en los ocho idiomas. La simulación es local; las otras necesitan una suscripción de pruebas, Azure CLI y permisos adecuados. No se han ejecutado aquí contra Azure. Los recursos y datos retenidos pueden generar costes. Ejecuta desde la raíz y lee primero la limpieza.

<a id="advanced-lab-1"></a>

## 1. Recuperar un archivo y comparar bytes

Crea exclusivamente el grupo y cuenta dedicados de abajo. La plantilla desactiva versionado y namespace jerárquico para que el ejercicio use undelete sin promoción de versiones. Activa siete días de eliminación temporal para blobs y contenedores; prohíbe claves compartidas y blobs públicos, pero mantiene endpoint público autenticado.

Necesitas gestión para desplegar y un rol de datos apropiado para tu identidad, por ejemplo Storage Blob Data Contributor en esta cuenta. La plantilla no concede roles. Espera propagación si procede; no amplíes a Owner de toda la suscripción.

El script crea un contenedor nuevo, carga texto sintético, elimina solo ese blob, restaura y compara contenido. Esperado: RECOVERY_OK. Después elimina su contenedor; pueden quedar datos retenidos. Si falla, registra fase y error sin secretos. No cambies la protección de una cuenta de producción.

[Bicep](../labs/protected-storage.bicep) · [Script](../labs/blob-recovery.sh)

```bash
az login
export LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account show --subscription "$LAB_SUBSCRIPTION" --query '{name:name,id:id}' -o table
export LAB_RG="rg-notes-recovery-$(date -u +%Y%m%d%H%M%S)"
export LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$RANDOM"
az group create --name "$LAB_RG" --location westeurope \
  --subscription "$LAB_SUBSCRIPTION" --tags environment=lab project=notes-recovery

az deployment group what-if --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Review proposed changes before running create.
az deployment group create --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Run after the required data permissions have been provided.
bash labs/blob-recovery.sh
```

<a id="advanced-lab-2"></a>

## 2. Inspeccionar asignaciones sin conceder roles

Obtén el ID del recurso y proporciona el object ID del principal, no su client ID. El script solo lee y filtra asignaciones directas para ese principal, incluyendo ámbitos heredados. No es un cálculo completo de acceso efectivo: membresías de grupos, condiciones, denegaciones, activación temporal y controles de datos o red necesitan análisis separado.

Entrega rol, ámbito, condición y la acción que quieres autorizar. Una tabla vacía no demuestra ausencia de todo acceso. No crees una asignación para hacer aparecer resultados.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Simular una respuesta perdida

Sin red, credenciales ni recursos cloud. SQLite guarda el documento y el primer intento pierde su respuesta. El cliente repite. Esperado con tres intentos: naive guarda dos documentos, idempotent uno y permanent no escribe ni reintenta. Las esperas se calculan, no se ejecutan.

Con un solo intento, no hay confirmación de éxito pero puede existir una escritura. Explica por qué excepción no equivale a operación no realizada. Las siete pruebas locales comprueban comportamiento y bloqueos de los scripts, no disponibilidad de Azure.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Limpieza y entrega

Lista el grupo dedicado y confirma su eliminación cuando CLI pregunte. Debe terminar en false. La eliminación del contenedor del script no garantiza que todos los datos hayan dejado de estar retenidos. Verifica errores o bloqueos; no purgues recursos compartidos.

Entrega resultado esperado, observado, permiso usado, comparación de contenido, interpretación de roles y salida del simulador. Mantén separadas las verificaciones locales y las pruebas cloud.



```bash
case "$LAB_RG" in
  rg-notes-recovery-*) ;;
  *) echo "Not a dedicated recovery lab group"; exit 2 ;;
esac
az resource list --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" -o table
az group delete --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
az group exists --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
```

[Microsoft Learn: Blob soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable) · [Restore](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-manage) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)
