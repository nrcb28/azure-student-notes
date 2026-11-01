# DP-700 · Cahier d’ingénierie des données hors connexion

[Guide](DP-700.md) · [Dix cas](DP-700-cases.md) · [Sommaire](README.md) · [Español](../es/DP-700-workbook.md)

Cinq unités utilisent des données universitaires synthétiques. Elles ne nécessitent ni compte, ni capacité payante, ni exécution Fabric. Conservez les mêmes livrables dans toutes les éditions linguistiques. Étiquetez les sorties raisonnées **EXPECTED**, les observations locales **OBSERVED** et les vérifications de plateforme non réalisées **NOT EXECUTED**. Le périmètre des sources et les limites de leur vérification figurent dans le [guide](DP-700.md).

<a id="dp-700-unit-1"></a>

## 1. Dessiner la carte de plateforme et de propriété

Expliquez la différence entre locataire, capacité, espace de travail, élément, emplacement OneLake et moteur d’exécution. Dessinez la source des inscriptions universitaires, les fichiers bruts de téléchargement, les tables préparées, le raccourci du catalogue de bibliothèque et le consommateur analytique. Décidez où un lakehouse et un entrepôt pourraient convenir, avec une raison concrète pour chaque choix. Énoncez la granularité de chaque table.

**Scénario :** la bibliothèque contrôle la cible du raccourci et modifie sa politique d’accès. **Preuves :** consignez la propriété de la cible, les hypothèses d’authentification interne ou externe, les autorisations requises, le contrat de schéma et l’effet d’une suppression de la cible. **Livrable :** un schéma de dépendances et une matrice d’accès. Incluez une exigence distincte de conservation historique ; le raccourci ne satisfait pas lui-même aux besoins de sauvegarde ou de récupération.

<a id="dp-700-unit-2"></a>

## 2. Réconcilier un journal de changements incrémentaux

Utilisez ce journal synthétique complet ; `version` est l’ordre source faisant autorité et `key` identifie une inscription. Commencez avec une cible vide. Conservez un marqueur de suppression versionné pour les suppressions. Réduisez chaque clé à sa version maximale, fusionnez les doublons identiques, puis ne fusionnez que les versions plus récentes dans la cible. Des charges utiles contradictoires à une même version exigent une mise en quarantaine.

| key | version | operation | module |
|---|---:|---|---|
| E1 | 1 | upsert | CS101 |
| E2 | 1 | upsert | DB201 |
| E1 | 2 | upsert | AI301 |
| E1 | 2 | upsert | AI301 |
| E2 | 2 | delete | DB201 |
| E2 | 1 | upsert | DB201 |

**Scénario :** rejouez le journal après la perte de la réponse de réussite. **Preuves attendues :** E1 reste active dans AI301 à la version 2 ; E2 est supprimée à la version 2. Le nombre d’inscriptions actives est 1 après chacune des deux exécutions. **Livrable :** état intermédiaire et règles de validation durable de la progression ; expliquez pourquoi E2 version 1 arrivée tardivement ne peut pas la ressusciter.

<a id="dp-700-unit-3"></a>

## 3. Préciser les règles de qualité et de temps d’événement

Concevez un enregistrement de téléchargement avec identifiant d’événement, module, temps d’événement, heure d’arrivée et version de schéma. Définissez les règles de valeur nulle, de type, de valeurs autorisées et de doublons. Expliquez la différence entre approuver un nouveau champ facultatif et accepter des enregistrements invalides. La quarantaine doit conserver un identifiant réparable et un motif tout en restreignant l’accès au contenu sensible.

**Scénario :** un événement a lieu à 23:59 UTC et arrive à 00:07 UTC le jour suivant ; la tolérance de retard annoncée est de dix minutes. **Preuves attendues :** son jour en temps d’événement est le jour précédent. L’acceptation exige aussi de connaître le watermark du moteur à l’arrivée ; un retard de huit minutes à l’horloge ne prouve pas à lui seul l’acceptation. **Livrable :** règles d’acceptation et de correction, réconciliation, limites des fenêtres, rôle du point de contrôle et comportement au-delà de la tolérance.

<a id="dp-700-unit-4"></a>

## 4. Concevoir un déploiement contrôlé

Décrivez un pipeline qui copie un intervalle borné d’inscriptions, lance validation et transformation, puis ne publie que les résultats acceptés. Choisissez SQL, PySpark ou KQL pour chaque transformation pertinente et justifiez le moteur. Distinguez le versionnement Git des définitions prises en charge, le déploiement du contenu pris en charge et le déplacement des données.

**Scénario :** le notebook de test pointe encore vers le lakehouse de production. **Preuves :** examinez les références d’éléments, la liaison de connexion, l’identité d’exécution, les paramètres, les dépendances d’environnement et les planifications avant l’exécution. **Livrable :** une table de configuration développement/test/production, des tests de lecteurs autorisés et refusés sur les voies rapport et fichier, ainsi que des étapes de retour arrière. Expliquez pourquoi une étiquette de confidentialité seule ne met pas en œuvre toute la conception des autorisations.

<a id="dp-700-unit-5"></a>

## 5. Diagnostiquer une exécution lente fictive

Créez une référence pour la durée d’exécution, les décomptes d’entrée et de sortie, les rejets, la fraîcheur et l’utilisation de capacité. Ajoutez un incident où le même volume d’entrée prend deux fois plus de temps. Incluez trois explications concurrentes : une jointure Spark déséquilibrée, de nombreux petits fichiers et une demande concurrente de capacité. Énoncez les preuves qui confirmeraient ou réfuteraient chaque explication ; examinez l’élimination de partitions et le comportement des requêtes lorsque pertinent.

**Scénario :** une nouvelle tentative suit une écriture partielle. **Preuves :** utilisez les règles de version de l’unité 2 pour montrer si l’état métier change. **Livrable :** une expérience d’optimisation réversible avec des seuils d’acceptation et une réconciliation d’exactitude. Marquez toutes les durées Fabric NOT EXECUTED ; un raisonnement synthétique ne peut pas établir le débit réel, la durée de récupération ou la réussite d’un déploiement cloud.
