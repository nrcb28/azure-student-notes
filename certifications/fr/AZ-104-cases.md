# AZ-104 · Révision

[Lire](AZ-104.md) · [Sommaire](README.md)

Réponds avant d'ouvrir la solution. Questions originales d'étude, pas des questions officielles. Pour chaque cas : exigence, choix et méthode de vérification.

## 1. Reader retiré, accès conservé.

<details>
<summary>Réponse</summary>

Vérifier groupes et attributions héritées.

</details>

## 2. Contributor crée Storage mais ne lit pas les blobs.

<details>
<summary>Réponse</summary>

Vérifier rôles de données et authentification.

</details>

## 3. VNet integration mais web toujours public.

<details>
<summary>Réponse</summary>

L'intégration concerne la sortie. Vérifier séparément l'entrée.

</details>

## 4. Backend unhealthy dans l'équilibreur.

<details>
<summary>Réponse</summary>

Vérifier port, réponse de sonde, processus et filtres.

</details>

## 5. Peerings A-B et B-C, A-C échoue.

<details>
<summary>Réponse</summary>

Le peering n'est pas automatiquement transitif.

</details>

## 6. Bicep compile mais déploiement refusé.

<details>
<summary>Réponse</summary>

Vérifier Policy, droits, quotas et disponibilité.

</details>

## 7. Sauvegarde réussie : RTO garanti ?

<details>
<summary>Réponse</summary>

Non. Mesurer restauration et reprise complète.

</details>

## 8. Private endpoint mais DNS public.

<details>
<summary>Réponse</summary>

Vérifier zones privées, liens et résolution cliente.

</details>

## 9. VM arrêtée mais coûts résiduels.

<details>
<summary>Réponse</summary>

Distinguer arrêt, désallocation, disques et services annexes.

</details>

## 10. Policy ne corrige pas l'existant.

<details>
<summary>Réponse</summary>

Vérifier effet et remédiation nécessaire.

</details>
