# AZ-400 · Cahier avancé commun

[←](README.md) · [Socle commun d'étude](../../fr/16-common-core.md) · [Travaux pratiques avancés](../../fr/17-advanced-labs.md)

Objectifs, cas et livrables correspondent dans les huit langues. L'équivalence se vérifie par unités et preuves, pas par nombre de mots. Les guides antérieurs restent des explications complémentaires.

<a id="az-400-unit-1"></a>

## 1. Traçabilité et Git

Relie besoin, issue, PR, commit, build, artefact et déploiement. Définis des métriques cohérentes, sans mesurer les personnes par commits. Choisis les branches selon fréquence et versions maintenues.

**Cas :** annuler une release partagée. **Preuve :** revert contre réécriture et effets sur les données. Révoquer ou renouveler un secret avant de compter sur sa suppression.

<a id="az-400-unit-2"></a>

## 2. Tests et artefacts

Construis une fois et promeus le résultat identifié. Note version, digest et origine. Combine tests selon risques ; la couverture ne prouve pas de bonnes assertions.

**Cas :** cela marchait hier sans changement. **Preuve :** outils, dépendances et images non figés. Examine les tests instables plutôt que répéter jusqu'au vert. Distingue cache et artefacts.

<a id="az-400-unit-3"></a>

## 3. Identité et frontières du runner

Sépare code fiable, entrées PR, permissions workflow et étendue cloud. Les runners propres demandent isolation, mises à jour et nettoyage. OIDC exige encore confiance et autorisation précises.

**Cas :** PR externe modifiant un script interne. **Preuve :** chemin sans accès production, restrictions d'identité et contrôles de ressources. Le code de pipeline n'est pas inoffensif par nature.

<a id="az-400-unit-4"></a>

## 4. Déployer et récupérer

Compare rolling, blue-green, canary, rings et flags. Définis population, signaux fonctionnels, fenêtre et arrêt. Un swap n'isole pas toutes les dépendances. Prévois des migrations compatibles.

**Cas :** CPU normale mais résultats faux. **Preuve :** signal métier et critère rollback. Explique pourquoi l'ancienne image ne recrée pas une colonne supprimée.

<a id="az-400-unit-5"></a>

## 5. Fermer la boucle

Propage contexte et version dans la télémétrie, protège les logs. Définis responsables et fenêtres d'alerte. Les approbations de ressources dépassent les conditions YAML modifiables.

**Livrable :** pipeline complet, test significatif, artefact fixe et promotion. Exécute le simulateur avec une autre règle de retry. Postmortem avec action, responsable et vérification.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
