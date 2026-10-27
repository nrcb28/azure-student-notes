# Révision · 24

[Sommaire](README.md)

Réponds avant d'ouvrir la solution. Questions originales d'étude, pas des questions officielles. Pour chaque cas : exigence, choix et méthode de vérification.

## 1. Contrôle du noyau nécessaire : VM ou plateforme web ?

<details>
<summary>Réponse</summary>

VM si elle fournit le contrôle requis. Le besoin système décide.

</details>

## 2. MFA accorde-t-il la lecture ?

<details>
<summary>Réponse</summary>

Non. Authentification et autorisation sont distinctes.

</details>

## 3. Public signifie-t-il anonyme ?

<details>
<summary>Réponse</summary>

Non. Une identité et des droits peuvent être requis.

</details>

## 4. Ajouter des instances : quelle mise à l'échelle ?

<details>
<summary>Réponse</summary>

Horizontale. Renforcer une instance est vertical.

</details>

## 5. Une réplique récupère-t-elle toute suppression ?

<details>
<summary>Réponse</summary>

Non. Il faut conserver un état antérieur approprié.

</details>

## 6. Bloquer les régions interdites.

<details>
<summary>Réponse</summary>

Utiliser Policy avec effet et étendue adaptés.

</details>

## 7. Un budget arrête-t-il toute dépense ?

<details>
<summary>Réponse</summary>

Non. Il suit les dépenses et alerte.

</details>

## 8. CPU faible mais API lente.

<details>
<summary>Réponse</summary>

Vérifier dépendances, réseau, requêtes et attentes.

</details>

## 9. Gros volume et réseau insuffisant ?

<details>
<summary>Réponse</summary>

Comparer transfert en ligne et Data Box selon prise en charge, délai et sécurité.

</details>

## 10. Déploiement réussi : terminé ?

<details>
<summary>Réponse</summary>

Non. Valider le comportement et les dépendances.

</details>

## 11. Reader retiré, accès conservé.

<details>
<summary>Réponse</summary>

Vérifier groupes et attributions héritées.

</details>

## 12. Contributor crée Storage mais ne lit pas les blobs.

<details>
<summary>Réponse</summary>

Vérifier rôles de données et authentification.

</details>

## 13. VNet integration mais web toujours public.

<details>
<summary>Réponse</summary>

L'intégration concerne la sortie. Vérifier séparément l'entrée.

</details>

## 14. Backend unhealthy dans l'équilibreur.

<details>
<summary>Réponse</summary>

Vérifier port, réponse de sonde, processus et filtres.

</details>

## 15. Peerings A-B et B-C, A-C échoue.

<details>
<summary>Réponse</summary>

Le peering n'est pas automatiquement transitif.

</details>

## 16. Bicep compile mais déploiement refusé.

<details>
<summary>Réponse</summary>

Vérifier Policy, droits, quotas et disponibilité.

</details>

## 17. Sauvegarde réussie : RTO garanti ?

<details>
<summary>Réponse</summary>

Non. Mesurer restauration et reprise complète.

</details>

## 18. Private endpoint mais DNS public.

<details>
<summary>Réponse</summary>

Vérifier zones privées, liens et résolution cliente.

</details>

## 19. VM arrêtée mais coûts résiduels.

<details>
<summary>Réponse</summary>

Distinguer arrêt, désallocation, disques et services annexes.

</details>

## 20. Policy ne corrige pas l'existant.

<details>
<summary>Réponse</summary>

Vérifier effet et remédiation nécessaire.

</details>

## 21. RPO zéro implique RTO zéro ?

<details>
<summary>Réponse</summary>

Non. Perte de données et délai de reprise diffèrent.

</details>

## 22. API avec JSON et transactions complexes.

<details>
<summary>Réponse</summary>

Choisir selon les exigences, pas le format d'échange.

</details>

## 23. Petite équipe souhaitant AKS pour une API.

<details>
<summary>Réponse</summary>

Évaluer besoin Kubernetes, compétences, alternatives et coûts.

</details>

## 24. Réplique externe et résidence nationale obligatoire.

<details>
<summary>Réponse</summary>

Vérifier résidence des répliques, sauvegardes, logs et dépendances.

</details>
