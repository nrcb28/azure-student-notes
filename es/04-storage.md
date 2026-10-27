# Almacenamiento y datos

Primero pensaría cómo se van a leer y escribir los datos. Después elegiría un producto.

| Necesidad | Opción a estudiar |
|---|---|
| PDFs, imágenes y objetos | Blob Storage |
| Archivos compartidos | Azure Files |
| Disco de una VM | Managed Disks |
| Relaciones, restricciones y transacciones SQL | Azure SQL Database o PostgreSQL administrado |
| Modelos distribuidos que encajen con sus APIs | Azure Cosmos DB |

## Blob Storage

Los blobs se organizan en contenedores dentro de una cuenta de almacenamiento. Un contenedor de blobs no es un contenedor Docker.

Los niveles de acceso intercambian costes de almacenamiento y lectura. Los datos archivados pueden necesitar rehidratación antes de leerse; no elegiría Archive para documentos que el usuario espera abrir al instante.

## Redundancia

- **LRS:** varias copias dentro de una ubicación física de la región principal.
- **ZRS:** copias entre zonas de la región principal.
- **GRS:** replicación geográfica hacia una región secundaria.
- **GZRS:** combina redundancia por zonas en la principal y replicación geográfica.

La replicación geográfica es asíncrona: puede existir pérdida de escrituras recientes durante un fallo. El acceso de lectura a la secundaria depende de la opción elegida y del estado del servicio.

## Bases de datos

Una base administrada no arregla índices ausentes, consultas caras ni conexiones mal gestionadas. Antes de aumentar capacidad, mediría consultas y tiempos.

En nuestra app, guardaría los PDFs en Blob Storage y en la base de datos el título, asignatura, autor y referencia al objeto. Así no confundimos almacenamiento de archivos con consulta de metadatos.

## Protección

Preferir identidades y permisos de datos adecuados. Si se utilizan SAS, limitar permisos y duración y tratarlas como credenciales. Añadir borrado temporal, versionado o backup cuando el servicio lo permita y el requisito lo justifique.

**Repaso:** redundancia y backup cubren riesgos distintos. Una eliminación puede propagarse entre réplicas.

---

[Índice](README.md) · [Otro idioma](../en/04-storage.md) · [Anterior](03-compute.md) · [Siguiente](05-networking.md)
