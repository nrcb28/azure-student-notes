# Laboratorios: entender antes de desplegar

Estas prácticas usan Azure CLI desde Bash. No se han ejecutado en una suscripción real como parte de estos apuntes. Crean recursos que pueden generar costes. No utilizan contraseñas ni conceden permisos automáticamente.

## Requisitos

- Azure CLI y una cuenta autorizada en una suscripción de pruebas.
- Permiso para crear el grupo y la cuenta de almacenamiento.
- Para la práctica de datos, permiso Storage Blob Data Contributor en el ámbito adecuado. Contributor de administración no garantiza ese acceso.
- Revisar políticas, cuotas y regiones permitidas de la suscripción.
- Para Bicep, tener disponible el compilador integrado en Azure CLI.

## 1. Revisar la suscripción y crear un grupo

Ejecuta desde la raíz del repositorio:

```bash
az login
az account list --output table

# Sustituye el valor antes de continuar.
AZURE_LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_LAB_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

LAB_RG="rg-notes-lab-$(date -u +%Y%m%d%H%M%S)"
LAB_LOCATION='westeurope'
az group create --name "$LAB_RG" --location "$LAB_LOCATION" \
  --tags project=notes-app environment=lab

# Confirma que es un grupo recién creado y vacío.
az resource list --resource-group "$LAB_RG" --output table
```

Elige otra región si tu suscripción lo exige. Conserva el valor de LAB_RG en esta sesión para la limpieza.

**Comprueba:** el grupo existe, está etiquetado y todavía no contiene recursos.

## 2. Revisar y desplegar almacenamiento con Bicep

El archivo [storage.bicep](../labs/storage.bicep) crea una cuenta Standard_LRS, desactiva acceso anónimo a blobs y desactiva autenticación mediante claves compartidas. Mantiene un endpoint público de red: la autenticación sigue siendo obligatoria. No configura red privada, backup ni RBAC.

```bash
# 22 caracteres alfanuméricos en minúscula; debe ser único globalmente.
LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$(printf '%05d' "$RANDOM")"

az bicep build --file labs/storage.bicep --stdout > /dev/null

az deployment group validate --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az deployment group what-if --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Continúa después de revisar los cambios previstos.
az deployment group create --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az storage account show --resource-group "$LAB_RG" --name "$LAB_STORAGE" \
  --query '{name:name,publicBlobs:allowBlobPublicAccess,sharedKey:allowSharedKeyAccess}' \
  --output table
```

**Resultado esperado:** publicBlobs y sharedKey en false. La unicidad del nombre, las políticas y la disponibilidad regional todavía pueden provocar un error.

Compilar valida la sintaxis; validate y what-if requieren Azure y no demuestran que todas las operaciones posteriores tendrán éxito.

## 3. Crear un contenedor privado con tu identidad

Si falta el rol de datos, pide a un administrador que asigne Storage Blob Data Contributor al ámbito de esta cuenta. No amplíes permisos de toda la suscripción para resolver la práctica. La propagación del rol puede tardar.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

**Comprueba:** aparece notes. Un error de autorización no se arregla necesariamente cambiando la red: distingue conectividad de permisos de datos.

**Pregunta:** ¿por qué usamos --auth-mode login? Para utilizar la identidad de Azure CLI, sin pedir una clave de la cuenta.

## 4. Diagnóstico guiado, sin crear más recursos

Para una API que tarda demasiado, escribe una hipótesis para cada caso:

| Síntoma | Qué revisaría |
|---|---|
| El nombre no resuelve | DNS y zonas privadas |
| Hay timeout de conexión | Rutas, NSG, firewall y endpoint |
| Responde 401 | Autenticación y token |
| Responde 403 | Autorización y controles del servicio |
| Responde 500 | Logs, dependencias y último cambio |
| La cola crece | Capacidad del consumidor, errores y antigüedad |

Los códigos son pistas, no diagnósticos definitivos. El servicio concreto puede usar respuestas distintas.

## 5. Limpieza

Hazlo solo sobre el grupo dedicado que acabas de crear. El siguiente comando elimina el grupo y todos sus recursos:

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

Confirma la eliminación cuando Azure CLI lo solicite. Cuando termine:

```bash
az group exists --name "$LAB_RG"
```

Debe devolver false. Si hay bloqueos, errores de permisos o recursos retenidos, revisa el resultado; no asumas que todo se ha borrado.

## Entrega sugerida

Una captura de los resultados sin datos sensibles y un párrafo explicando: qué desplegaste, qué permiso necesitaste, cómo verificaste la configuración y cómo hiciste la limpieza.
