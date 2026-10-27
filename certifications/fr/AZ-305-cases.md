# AZ-305 · Révision

[Lire](AZ-305.md) · [Sommaire](README.md)

Réponds avant d'ouvrir la solution. Questions originales d'étude, pas des questions officielles. Pour chaque cas : exigence, choix et méthode de vérification.

## 1. RPO zéro implique RTO zéro ?

<details>
<summary>Réponse</summary>

Non. Perte de données et délai de reprise diffèrent.

</details>

## 2. API avec JSON et transactions complexes.

<details>
<summary>Réponse</summary>

Choisir selon les exigences, pas le format d'échange.

</details>

## 3. Petite équipe souhaitant AKS pour une API.

<details>
<summary>Réponse</summary>

Évaluer besoin Kubernetes, compétences, alternatives et coûts.

</details>

## 4. Réplique externe et résidence nationale obligatoire.

<details>
<summary>Réponse</summary>

Vérifier résidence des répliques, sauvegardes, logs et dépendances.

</details>

## 5. VM répliquées, DNS et secrets absents.

<details>
<summary>Réponse</summary>

Le service n'est pas complètement rétabli.

</details>

## 6. Ajouter un cache.

<details>
<summary>Réponse</summary>

Prévoir invalidation, expiration et données anciennes.

</details>

## 7. Migration avec écritures continues.

<details>
<summary>Réponse</summary>

Définir transfert initial, synchronisation, bascule et retour.

</details>

## 8. Rapports historiques ralentissant les inscriptions.

<details>
<summary>Réponse</summary>

Évaluer séparation analytique et requêtes avant de dimensionner.

</details>

## 9. Schéma composé seulement de services.

<details>
<summary>Réponse</summary>

Ajouter exigences, frontières, pannes, exploitation et validation.

</details>

## 10. Budget réduit, objectifs inchangés.

<details>
<summary>Réponse</summary>

Réévaluer les options et valider avant de promettre.

</details>
