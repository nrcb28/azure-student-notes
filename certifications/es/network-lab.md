# Práctica de redes: predecir reglas y comprobar configuración

[Certificaciones](README.md) · [English](../en/network-lab.md)

## Objetivo y límites

La plantilla crea una VNet, dos subredes y un NSG. No crea VM, IP pública, gateway ni conectividad híbrida. Sirve para interpretar configuración, no para demostrar una conexión de aplicación completa.

No se ha desplegado desde estos apuntes. Se necesitan Azure CLI, Bicep y permiso en una suscripción de pruebas. Las políticas y la disponibilidad pueden impedir operaciones. Revisa siempre recursos y posibles costes.

## Antes de ejecutar

Lee [network.bicep](../../labs/network.bicep) y predice estas situaciones:

| Origen | Destino | Puerto | Resultado esperado del NSG de datos |
|---|---|---|---|
| 10.30.1.5 | 10.30.2.5 | TCP 443 | Allow por prioridad 100 |
| 10.30.1.5 | 10.30.2.5 | TCP 22 | Deny por prioridad 110 |
| 10.30.2.6 | 10.30.2.5 | TCP 443 | Deny por prioridad 110 |

Son predicciones de reglas, suponiendo tráfico nuevo sujeto a ese NSG y sin otros cambios. No prueban ruta, resolución, proceso escuchando ni autorización de aplicación.

La denegación de prioridad 110 bloquea el tráfico entrante restante del service tag VirtualNetwork antes de la regla predeterminada que lo permitiría. Es una decisión didáctica; no copiarla a producción sin analizar todas las dependencias.

## Desplegar desde la raíz

```bash
az login
AZURE_NET_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_NET_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

NET_RG="rg-notes-network-$(date -u +%Y%m%d%H%M%S)"
NET_LOCATION='westeurope'
az group create --name "$NET_RG" --location "$NET_LOCATION" \
  --tags project=notes-app environment=lab

az bicep build --file labs/network.bicep --stdout > /dev/null

az deployment group validate --resource-group "$NET_RG" \
  --template-file labs/network.bicep

az deployment group what-if --resource-group "$NET_RG" \
  --template-file labs/network.bicep

# Después de revisar las operaciones previstas:
az deployment group create --resource-group "$NET_RG" \
  --template-file labs/network.bicep
```

## Verificación

```bash
az network vnet subnet list --resource-group "$NET_RG" \
  --vnet-name vnet-notes-lab \
  --query '[].{name:name,prefix:addressPrefix,nsg:networkSecurityGroup.id}' \
  --output table

az network nsg rule list --resource-group "$NET_RG" \
  --nsg-name nsg-notes-lab \
  --query '[].{name:name,priority:priority,access:access,port:destinationPortRange}' \
  --output table
```

Debe haber dos subredes. La de datos referencia el NSG y las reglas personalizadas muestran prioridades 100 y 110. No confundir listar reglas personalizadas con ver todas las reglas predeterminadas o efectivas de una interfaz.

**Qué no se ha probado:** no hay VM ni listener, por lo que no existe una prueba real de HTTPS entre las IP del ejemplo. Para una prueba de extremo a extremo harían falta cargas, rutas y comprobaciones adicionales.

## Variantes sin desplegar

1. Cambia el puerto permitido en una copia local y predice la tabla.
2. Añade en papel un NSG a la interfaz del destino. Explica por qué permitir en subred no basta si el otro filtro deniega.
3. Supón un DNS que apunta a IP pública. Explica qué parte no resuelve el NSG.
4. Explica qué cambia para conexiones ya establecidas al modificar filtros con estado.

## Limpieza

Solo para el grupo dedicado recién creado:

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Confirma cuando CLI lo solicite. Tras terminar debe devolver false. Revisa errores o bloqueos si no ocurre.

## Entrega

Tabla de predicciones, resultados observados de configuración y un párrafo explicando la diferencia entre permitir un puerto y demostrar una aplicación operativa.
