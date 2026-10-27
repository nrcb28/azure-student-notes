# Calcul et conteneurs

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

Une VM convient au contrôle du système ; App Service aux applications web compatibles ; Functions au code déclenché par événement. Container Instances et Container Apps exécutent des conteneurs sans administrer directement un cluster Kubernetes. AKS se justifie lorsque les besoins compensent sa complexité opérationnelle.

Un conteneur n'est pas une VM complète. Le serverless conserve des limites de démarrage, durée, réseau et facturation selon le plan.

**Diagnostic :** le conteneur démarre mais ne répond pas. Vérifions port, processus, configuration, journaux et sondes, puis une requête complète avec ses dépendances.

Séparons image et configuration. Les secrets ne doivent pas entrer dans les couches de l'image. Une version identifiable est plus reproductible qu'une étiquette latest modifiable.

**Exercice :** défends le choix d'AKS ou d'une plateforme plus simple pour une petite API.

---

[Précédent](02-resources.md) · [Suivant](04-storage.md) · [English](../en/03-compute.md)
