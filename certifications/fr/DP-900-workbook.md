# DP-900 · Cahier avancé commun

[Guide](DP-900.md) · [Dix cas](DP-900-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes dans les huit langues. Utiliser des données synthétiques et distinguer prévisions et observations. Ces exercices ne déploient pas Azure et ne couvrent pas tout l’examen.

<a id="dp-900-unit-1"></a>

## 1. Décrire les données avant de choisir leur stockage

Inventorier un PDF, une ligne d’inscription, un document JSON à métadonnées facultatives et un événement de téléchargement. Pour chacun, décrire structure, identifiant, producteur, consommateur, rétention et champs sensibles. Écrire ensuite l’opération importante : retrouver un fichier, enregistrer une inscription ou agréger des événements. Distinguer un format d’une exigence de charge.

**Scénario :** quelqu’un propose une base unique parce que les quatre ensembles appartiennent à la même application. **Preuves :** une matrice de décision de quatre lignes, une alternative écartée par ligne et une nouvelle exigence qui pourrait modifier chaque choix. Ne pas inventer de limites de service ni supposer que chaque JSON exige Cosmos DB.

<a id="dp-900-unit-2"></a>

## 2. Rendre visible l’intégrité relationnelle

Dessiner Students, Courses et Enrolments avec des identifiants stables. Créer six lignes synthétiques et expliquer clés primaires, références et règle empêchant une inscription en double. Prévoir le résultat d’une jointure. Modifier ensuite un titre de cours et comparer les changements avec un modèle qui recopie le titre dans chaque inscription. Le but est de montrer une anomalie concrète, pas de réciter un slogan sur la normalisation.

**Scénario :** un étudiant est inscrit à un cours inexistant. **Preuves :** la règle qui devrait le rejeter ou le détecter, un enregistrement invalide et le résultat attendu. Si un exemple SQL local est exécuté, nommer le moteur : le comportement de SQLite local ne teste pas Azure SQL.

<a id="dp-900-unit-3"></a>

## 3. Choisir qui exploite la base

Comparer Azure SQL Database, Managed Instance et SQL Server sur VM pour une nouvelle application et une migration. Lister dépendances de compatibilité, besoins réseau et d’identité, maintenance et récupération. Ajouter un moteur open source si l’application existante l’exige. Séparer une recommandation justifiée d’une affirmation selon laquelle un produit serait toujours meilleur.

**Scénario :** l’inventaire de migration contient un composant exigeant un accès au système invité. **Preuves :** une liste de questions de compatibilité, un tableau des responsabilités d’exploitation et un plan de preuve de concept avec critères de réussite. Aucun déploiement n’est requis ; préciser les hypothèses à tester avant d’accepter une cible.

<a id="dp-900-unit-4"></a>

## 4. Rapprocher les comptes d’un petit pipeline

Créer six événements synthétiques de téléchargement, dont un identifiant en double et un cours absent. Définir l’entrée valide, l’événement unique et la condition de fin. Dessiner un chemin ETL et un chemin ELT en plaçant validation et stockage des rejets. Expliquer quand un lot respecte le délai et quand un flux pourrait être justifié.

**Scénario :** le total du tableau de bord diffère du nombre de lignes sources. **Preuves :** comptes source, doublons, rejets et acceptations avec une explication reproductible. Désigner le responsable et la réaction à une exécution échouée. Un statut de pipeline réussi ne prouve pas que ses totaux métier sont corrects.

<a id="dp-900-unit-5"></a>

## 5. Définir une mesure analytique fiable

Choisir une granularité, par exemple un événement de téléchargement terminé, et définir un fait avec ses contextes de cours et de date. Préciser fuseau, traitement des événements tardifs et fraîcheur. Expliquer ce qui stocke, transforme, fournit le modèle sémantique et affiche le rapport. Comparer lac, entrepôt et lakehouse d’après le travail nécessaire, pas l’étiquette du produit.

**Livrables finaux :** matrice de stockage, schéma relationnel, rapprochement du pipeline et maquette de rapport mensuel avec sa définition de mesure. Expliquer les rôles pertinents de Fabric, Synapse et Power BI. Identifier une question à revoir dans le guide officiel ; une bonne maquette ne démontre ni exploitation cloud ni préparation à l’examen.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) · [Notes sur les données](../../fr/04-storage.md)
