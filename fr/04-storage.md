# Stockage et données

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

Blob Storage conserve des objets comme les PDF ; Azure Files fournit des partages ; Managed Disks sert aux VM. Une base relationnelle gère relations et transactions. Échanger du JSON ne force pas le choix d'une base documentaire.

LRS réplique localement, ZRS entre zones. GRS et GZRS ajoutent une réplication géographique asynchrone : les dernières écritures ne sont pas nécessairement déjà dans la région secondaire.

Versions, suppression réversible et sauvegardes répondent à d'autres risques que la redondance. Archive peut nécessiter une réhydratation et ne convient pas à une lecture immédiate.

**Application :** PDF dans Blob, métadonnées dans la base. Restaurer uniquement le fichier peut créer une incohérence.

Les SAS sont des informations d'accès sensibles : limiter droits et durée. Distinguer administration et accès aux données.

**Exercice :** prépare la récupération d'un document supprimé dix jours auparavant.

---

[Précédent](03-compute.md) · [Suivant](05-networking.md) · [English](../en/04-storage.md)

## Approfondissement Microsoft Learn · sas

Une user delegation SAS pour Blob utilise une clé de délégation obtenue avec Entra ID. Son émission exige des droits ; connaître l'URL ne suffit pas.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-sas)

## Récupérer les blobs selon le niveau

La suppression réversible conserve les objets pendant la rétention configurée. Elle ne protège pas seule la suppression du conteneur ou du compte. Séparer ces risques.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Récupérer les blobs selon le niveau](15-microsoft-learn.md#learn-blob-recovery)
