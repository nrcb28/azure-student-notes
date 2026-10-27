# Gouvernance et conformité

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

RBAC définit qui peut agir ; Policy impose des conditions aux ressources. Une personne autorisée à créer une VM peut être bloquée par une restriction de région.

Audit signale ; Deny bloque des demandes non conformes. Modify et DeployIfNotExists nécessitent configuration et droits adaptés. Les ressources existantes peuvent demander une remédiation.

Les étiquettes project, environment et owner classent les ressources. Ce ne sont pas des frontières de sécurité et leur héritage n'est pas toujours automatique. Les verrous d'administration ne remplacent ni sauvegarde ni permissions sur les données.

Defender for Cloud et Sentinel ont des objectifs différents. Une certification du fournisseur ne rend pas automatiquement l'application conforme.

**Exercice :** commence par auditer une règle, identifie son impact et ses responsables, puis envisage le blocage. Toute exception doit être justifiée et réexaminée.

---

[Précédent](06-identity.md) · [Suivant](08-observability.md) · [English](../en/07-governance.md)
