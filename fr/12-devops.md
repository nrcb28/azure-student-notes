# DevOps et infrastructure comme code

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

DevOps rapproche développement et exploitation pour livrer des changements fiables. CI intègre avec compilation et contrôles. La livraison continue maintient prêt à publier ; le déploiement continu publie automatiquement selon critères.

Promouvoir le même artefact testé. Versions et digests permettent d'identifier ce qui s'exécutait.

Bicep décrit les ressources Azure. Terraform maintient un état à protéger. Plan et what-if aident sans garantir toute opération future. OIDC évite un secret durable mais exige confiance fédérée et autorisation.

**Rollback :** l'ancien code ne recrée pas une colonne supprimée. Prévoir migrations compatibles et récupération testée.

Un runner privilégié ne doit pas exécuter indistinctement du code non fiable.

**Exercice :** relie issue, PR, tests, artefact et publication. Définis critères de promotion et de retour arrière. Exécute localement python tools/check_docs.py.

---

[Précédent](11-messaging.md) · [Suivant](13-laboratorios.md) · [English](../en/12-devops.md)

## Approfondissement Microsoft Learn · whatif

What-if prévoit des changements sans les appliquer. Droits, dépendances et expressions peuvent limiter l'analyse. Un résultat incomplet ne prouve pas l'absence de changements.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-whatif)

## Approfondissement Microsoft Learn · slots

Un slot possède son hostname et exécute une application. Copier les paramètres ne clone ni contenu, ni réseau privé, ni toutes les dépendances. Le swap comprend préparation et préchauffage.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-slots)

## Approfondissement Microsoft Learn · checks

Les responsables des ressources Azure Pipelines administrent approvals et checks hors du YAML. Une étape doit satisfaire les contrôles des ressources qu'elle consomme.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-checks)
