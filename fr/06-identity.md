# Identité et sécurité

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

Entra ID gère les identités. L'authentification vérifie qui nous sommes ; l'autorisation détermine nos actions. MFA renforce la connexion, sans attribuer de droits sur les documents.

Azure RBAC associe identité, rôle et étendue. Reader consulte ; Contributor administre sans attribuer des rôles RBAC ; Owner peut aussi accorder l'accès. Les rôles d'annuaire et de ressources sont distincts.

Une identité managée évite des identifiants applicatifs stockés par nous, mais exige des droits. Key Vault gère secrets, clés et certificats.

**Cas :** supprimer Reader d'une ressource ne retire pas un accès hérité ou obtenu par un groupe. Vérifier l'identité effective et les autres attributions.

L'application doit contrôler l'accès à chaque document, même pour un étudiant connecté.

**Exercice :** sépare les permissions de l'étudiant, de l'API et du traitement des miniatures.

---

[Précédent](05-networking.md) · [Suivant](07-governance.md) · [English](../en/06-identity.md)
