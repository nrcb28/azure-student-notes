# DevOps et infrastructure comme code

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

DevOps rapproche développement et exploitation pour livrer des changements fiables. CI intègre avec compilation et contrôles. La livraison continue maintient prêt à publier ; le déploiement continu publie automatiquement selon critères.

Promouvoir le même artefact testé. Versions et digests permettent d'identifier ce qui s'exécutait.

Bicep décrit les ressources Azure. Terraform maintient un état à protéger. Plan et what-if aident sans garantir toute opération future. OIDC évite un secret durable mais exige confiance fédérée et autorisation.

**Rollback :** l'ancien code ne recrée pas une colonne supprimée. Prévoir migrations compatibles et récupération testée.

Un runner privilégié ne doit pas exécuter indistinctement du code non fiable.

**Exercice :** relie issue, PR, tests, artefact et publication. Définis critères de promotion et de retour arrière. Exécute localement python tools/check_docs.py.

---

[Précédent](11-messaging.md) · [Suivant](13-laboratorios.md) · [English](../en/12-devops.md)
