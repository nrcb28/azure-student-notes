# AZ-900 · Révision

[Lire](AZ-900.md) · [Sommaire](README.md)

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
