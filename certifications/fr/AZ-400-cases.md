# AZ-400 · Révision

[Lire](AZ-400.md) · [Sommaire](README.md)

Réponds avant d'ouvrir la solution. Questions originales d'étude, pas des questions officielles. Pour chaque cas : exigence, choix et méthode de vérification.

## 1. Recompiler pour production après les tests.

<details>
<summary>Réponse</summary>

Risque de différences. Promouvoir l'artefact testé.

</details>

## 2. Retour d'image après suppression de colonne.

<details>
<summary>Réponse</summary>

Ne restaure pas automatiquement schéma et données.

</details>

## 3. Secret publié quelques minutes dans Git.

<details>
<summary>Réponse</summary>

Révoquer ou renouveler, puis analyser l'exposition.

</details>

## 4. PR externe sur runner connecté en interne.

<details>
<summary>Réponse</summary>

Vérifier isolation, confiance, persistance et droits.

</details>

## 5. Canary avec CPU normale et résultats faux.

<details>
<summary>Réponse</summary>

Il faut des signaux fonctionnels et critères d'arrêt.

</details>

## 6. Test réussi au cinquième essai.

<details>
<summary>Réponse</summary>

Examiner l'instabilité au lieu de la masquer.

</details>

## 7. OIDC activé, connexion Azure refusée.

<details>
<summary>Réponse</summary>

Vérifier issuer, subject, audience et confiance fédérée.

</details>

## 8. Plus de releases mais reprise plus lente.

<details>
<summary>Réponse</summary>

Évaluer rapidité et stabilité ensemble.

</details>

## 9. Ancien cache cassant la build.

<details>
<summary>Réponse</summary>

Vérifier clé, dépendances et versions des outils.

</details>

## 10. Postmortem : faire davantage attention.

<details>
<summary>Réponse</summary>

Il faut une action concrète, un responsable et une vérification.

</details>
