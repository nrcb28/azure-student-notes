# DP-900 · 10 cas avec réponses argumentées

[Guide](DP-900.md) · [Cahier](DP-900-workbook.md) · [Sommaire](README.md)

Scénarios d’entraînement originaux, pas de vraies questions d’examen. Commencer par formuler l’exigence, puis écarter une autre solution et décrire les preuves à recueillir. Aucun déploiement cloud n’est revendiqué.

## 1. L’application stocke des PDF et des métadonnées de propriété interrogeables. Tout doit-il aller dans une même table SQL ?

<details>
<summary>Raisonnement</summary>

Non. Une conception possible stocke les PDF dans Blob Storage et leurs relations de propriété et de cours dans une base. L’essentiel est d’expliquer la frontière des accès et de la cohérence : le téléversement peut réussir alors que la mise à jour des métadonnées échoue. Prévoir un processus récupérable et la détection des fichiers orphelins. Une représentation entièrement en base reste possible si les exigences la justifient, mais « toute donnée doit être une ligne SQL » n’est pas une hypothèse de départ utile.

</details>

## 2. Un fichier JSON contient des attributs imbriqués facultatifs. Est-il non structuré parce que certains champs manquent ?

<details>
<summary>Raisonnement</summary>

JSON peut représenter des données semi-structurées : les clés et l’imbrication donnent une organisation même lorsque les enregistrements diffèrent. Des champs absents ne suppriment pas cette structure. Séparer la représentation de la qualité et du choix du stockage. Demander si un champ absent est valide, inconnu ou dû à une erreur d’ingestion, puis préciser la réaction attendue du consommateur. Une base documentaire peut convenir au mode d’accès, mais la seule présence de JSON ne tranche pas la conception.

</details>

## 3. Chaque inscription répète le titre du cours et son enseignant. Quel problème la normalisation pourrait-elle éviter ?

<details>
<summary>Raisonnement</summary>

Un changement de titre pourrait être appliqué à certaines inscriptions et laisser les autres avec l’ancienne valeur. Conserver un enregistrement Courses identifié par une clé stable, puis le référencer depuis Enrolments, réduit cette anomalie de mise à jour. Expliquer les contraintes nécessaires et les jointures qui reconstruisent le résultat utile. La duplication n’est pas interdite partout : un instantané analytique peut volontairement conserver des descriptions historiques. Préciser si l’on cherche la vérité transactionnelle actuelle ou un modèle de rapport historique.

</details>

## 4. Une requête de rapport ralentit les inscriptions. Déplacer le graphique dans Power BI supprime-t-il automatiquement la charge sur la base ?

<details>
<summary>Raisonnement</summary>

Non. L’effet dépend du mode d’obtention et d’actualisation des données du modèle. Un rapport peut toujours interroger la source opérationnelle ou provoquer des actualisations coûteuses. Préciser la fraîcheur, les requêtes et la capacité de la source avant de choisir. Une copie analytique préparée peut isoler une partie du travail, mais ajoute un délai et des responsabilités de pipeline. Mesurer la charge source et définir « à jour », plutôt que supposer qu’un autre outil visuel change les accès sous-jacents.

</details>

## 5. Une application SQL Server existante dépend de composants système. Azure SQL Database est-il toujours un remplacement sans modification ?

<details>
<summary>Raisonnement</summary>

Non. Inventorier ces composants et les autres dépendances avant de sélectionner la cible. Azure SQL Database, Managed Instance et SQL Server sur VM Azure ont des limites différentes de gestion et de compatibilité. Une VM donne accès au système, mais laisse davantage de maintenance à l’équipe. Managed Instance peut répondre à certaines exigences d’instance sans satisfaire chaque dépendance externe. Établir une liste de compatibilité et un plan de migration testé ; un moteur familier ne prouve pas que toute l’application fonctionnera sans changement.

</details>

## 6. Un étudiant pense qu’Azure Table Storage impose des clés étrangères parce que son nom contient Table. Comment corriger la conception ?

<details>
<summary>Raisonnement</summary>

Table Storage est un stockage d’entités non relationnel, pas un service SQL relationnel managé. Son nom ne garantit ni jointures relationnelles ni clés étrangères. Identifier les lectures, mises à jour, relations et exigences de cohérence réelles, puis comparer un modèle d’entités adapté à une conception relationnelle. La preuve utile est un exemple travaillé : montrer comment une inscription retrouve son cours et comment les références invalides sont empêchées ou détectées. Le nom d’un produit invite à vérifier ses capacités, il ne les remplace pas.

</details>

## 7. Un traitement nocturne respecte l’échéance du rapport du matin. Faut-il le remplacer par du streaming pour paraître moderne ?

<details>
<summary>Raisonnement</summary>

Partir du délai métier exigé. Si un lot nocturne fiable fournit le résultat à temps, le streaming peut ajouter du travail d’exploitation sans modifier les décisions possibles des utilisateurs. Si le personnel doit réagir à une surcharge en quelques minutes, étudier un chemin à plus faible latence pour ce besoin. Dans les deux cas, traiter doublons, entrées incomplètes et nouvelles tentatives. Comparer la fraîcheur de bout en bout et la reprise après panne, pas seulement la fréquence d’exécution d’un composant.

</details>

## 8. Les données brutes sont chargées dans un entrepôt puis nettoyées sur place. Est-ce de l’ETL, et l’entrepôt dispense-t-il de validation ?

<details>
<summary>Raisonnement</summary>

Cet ordre correspond à ELT : charger d’abord, puis transformer avec les capacités de la cible. ETL transforme avant le chargement dans la destination prévue. Aucun des deux ne supprime contrats et contrôles de données. Définir où vont les rejets, quelles transformations peuvent être rejouées et comment les totaux acceptés se rapprochent de la source. Contrôler l’accès aux données brutes sensibles même si les analystes ne voient qu’un modèle nettoyé ; une interface de requête simple ne garantit pas des enregistrements sûrs ou corrects.

</details>

## 9. Un tableau de bord compte des événements de téléchargement. Les nouvelles tentatives dupliquent leurs identifiants. COUNT(*) donne-t-il forcément le nombre de téléchargements terminés ?

<details>
<summary>Raisonnement</summary>

Seulement si chaque ligne comptée correspond, selon la définition retenue, à un téléchargement terminé. Des livraisons en double peuvent gonfler COUNT(*). Définir l’événement métier, son identifiant stable, sa condition de fin et sa période de rapport, puis dédupliquer ou agréger selon cette définition. Conserver le nombre de rejets et de doublons pour expliquer les changements. Tester un petit ensemble avec un identifiant répété et un téléchargement incomplet. Un graphique plausible ne prouve pas que sa mesure répond à la question souhaitée.

</details>

## 10. Six cours tiennent dans un modèle documentaire. Cela prouve-t-il que Cosmos DB est le seul stockage raisonnable ?

<details>
<summary>Raisonnement</summary>

Non. Beaucoup de services peuvent conserver six enregistrements ; l’exemple montre uniquement qu’on peut les représenter. Comparer les requêtes prévues, les relations, les mises à jour, la cohérence, l’exploitation et les compétences de l’équipe. Une base relationnelle peut être plus simple lorsque contraintes et entités liées dominent ; un modèle documentaire peut convenir à d’autres accès. Donner un motif du choix et une condition qui le modifierait. Les fondamentaux doivent développer ce raisonnement plutôt qu’associer automatiquement une base à chaque exemple en JSON.

</details>

Sources : [objectifs officiels](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900), [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction), [ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl), [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview).
