# Identité et sécurité

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

Entra ID gère les identités. L'authentification vérifie qui nous sommes ; l'autorisation détermine nos actions. MFA renforce la connexion, sans attribuer de droits sur les documents.

Azure RBAC associe identité, rôle et étendue. Reader consulte ; Contributor administre sans attribuer des rôles RBAC ; Owner peut aussi accorder l'accès. Les rôles d'annuaire et de ressources sont distincts.

Une identité managée évite des identifiants applicatifs stockés par nous, mais exige des droits. Key Vault gère secrets, clés et certificats.

**Cas :** supprimer Reader d'une ressource ne retire pas un accès hérité ou obtenu par un groupe. Vérifier l'identité effective et les autres attributions.

L'application doit contrôler l'accès à chaque document, même pour un étudiant connecté.

**Exercice :** sépare les permissions de l'étudiant, de l'API et du traitement des miniatures.

---

[Précédent](05-networking.md) · [Suivant](07-governance.md) · [English](../en/06-identity.md)

## Approfondissement Microsoft Learn · sas

Une user delegation SAS pour Blob utilise une clé de délégation obtenue avec Entra ID. Son émission exige des droits ; connaître l'URL ne suffit pas.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-sas)

## Diagnostiquer RBAC avec des preuves

Administrer une ressource ne donne pas automatiquement attribution des rôles ou lecture des données. Action et étendue appropriées sont nécessaires ; des conditions peuvent limiter rôles et destinataires.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting) · [Diagnostiquer RBAC avec des preuves](15-microsoft-learn.md#learn-rbac-diagnosis)

## Récupérer Key Vault et ses intégrations

La suppression réversible permet de récupérer pendant la rétention. Restaurer le vault ne recrée pas automatiquement certaines intégrations, notamment attributions RBAC et abonnements Event Grid.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Récupérer Key Vault et ses intégrations](15-microsoft-learn.md#learn-vault-recovery)
