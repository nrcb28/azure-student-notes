# AZ-120 · 10 cas avec réponses argumentées

[Guide](AZ-120.md) · [Cahier d’exercices](AZ-120-workbook.md) · [Sommaire](README.md)

Scénarios originaux d’entreprise universitaire, sans questions d’examen officielles. Expliquez la décision et les preuves avant d’ouvrir chaque réponse. Toutes les vérifications proposées sont du travail de conception hors connexion ; aucune exécution Azure ou SAP n’est revendiquée.

## 1. L’université ajoute deux serveurs d’application, mais garde une seule VM ASCS et une seule VM HANA. A-t-elle supprimé les principaux points uniques de défaillance ?

<details>
<summary>Réponse</summary>

Non. La redondance des serveurs d’application ne protège ni les services centraux ni la base de données. Inventoriez chaque SID et distinguez ASCS, ERS, instances applicatives, HANA, fichiers partagés et dépendances. Proposez des conceptions de haute disponibilité prises en charge pour les services centraux et la base, avec responsabilités explicites et chemins de reconnexion des clients. Les preuves doivent inclure un schéma de dépendances et l’effet prévisionnel de la perte de chaque composant. Confirmez aussi la capacité applicative après une panne. Compter les VM ne démontre pas qu’une transaction d’achat survit à la perte de son service de coordination ou de données.

</details>

## 2. Une VM moins chère possède le même nombre de cœurs que la VM HANA proposée. Est-ce une preuve suffisante pour la remplacer ?

<details>
<summary>Réponse</summary>

Non. Vérifiez la certification SAP HANA pour le type précis de VM, la charge, la version du système d’exploitation, la version de base de données et le modèle de déploiement. Comparez la demande mémoire mesurée, la croissance, les exigences SAPS pertinentes pour les couches applicatives, le débit du stockage, la latence des journaux et les limites réseau. Vérifiez aussi capacité régionale et quotas. La preuve est un relevé de combinaison prise en charge et une feuille de dimensionnement avec marge en cas de panne, plutôt qu’une comparaison de processeurs. Une estimation d’infrastructure plus basse n’est pas une décision de prise en charge, et ces notes d’étude ne peuvent établir ni les droits de licence SAP de l’université ni une capacité de production suffisante.

</details>

## 3. L’équipe réseau du campus affirme qu’ExpressRoute chiffre toutes les connexions SAP. La fiche de décision d’architecture doit-elle accepter cette affirmation ?

<details>
<summary>Réponse</summary>

Non. Connectivité privée et chiffrement sont des propriétés distinctes. Dessinez le chemin campus-Azure, le point de transfert du fournisseur, le routage Azure, les points de terminaison applicatifs et toute frontière de chiffrement choisie. Précisez un chiffrement applicatif pris en charge ou un autre dispositif adapté lorsque la politique l’exige, et vérifiez les capacités exactes du service. Documentez aussi la résolution DNS, les dépendances d’authentification, la résilience des routes et les flux autorisés. Les preuves doivent identifier le trafic chiffré, le début et la fin de la protection et la manière de vérifier la configuration. Un circuit privé seul ne prouve pas la confidentialité de bout en bout pour chaque protocole.

</details>

## 4. Un étudiant place les deux nœuds de haute disponibilité dans un PPG et affirme que cela les protège aussi d’une panne de zone. Que faut-il changer dans le raisonnement ?

<details>
<summary>Réponse</summary>

Séparez la colocalisation pour la latence de l’isolation pour la résilience. Un PPG contraint la proximité physique et ne fournit pas d’isolation des défaillances entre zones. Choisissez un placement de disponibilité pris en charge pour l’exigence de récupération, puis évaluez la latence réelle entre nœuds et le comportement de réplication. Si les PPG se justifient, appliquez-les dans les contraintes de placement appropriées et documentez les limites d’allocation. Les preuves doivent inclure le schéma des domaines de défaillance, la latence mesurée ou explicitement supposée, la capacité restante et la séquence de reprise. Ni un PPG ni les zones de disponibilité ne configurent à eux seuls un cluster SAP sûr ou un basculement de base de données.

</details>

## 5. HANA dispose de beaucoup d’espace disque libre, mais les achats ralentissent pendant les savepoints. L’équipe doit-elle uniquement ajouter de la capacité disque ?

<details>
<summary>Réponse</summary>

Examinez débit, latence et files d’attente des données et journaux, ainsi que le plafond d’E/S cumulé de la VM. Le trafic des savepoints peut concurrencer les écritures de journaux même lorsque la capacité libre est élevée. Examinez l’organisation de stockage prise en charge, le système de fichiers, la configuration des disques, la demande des volumes partagés et le calendrier de charge avant de choisir un changement. Le cache ou Write Accelerator doivent suivre les recommandations exactes du volume et du stockage, pas une recette universelle de performance. Les preuves consistent en une chronologie corrélée de charge et d’E/S et une configuration prise en charge proposée. Étiquetez les mesures comme preuves requises jusqu’à ce qu’un test autorisé les fournisse réellement.

</details>

## 6. Un cluster ne peut pas isoler son pair par fencing après une panne de communication. Désactiver le fencing rétablirait-il un service sûr ?

<details>
<summary>Réponse</summary>

Non. Supprimer le fencing peut autoriser des primaires en conflit et endommager l’intégrité des données. Préservez les preuves et suivez la procédure d’incident en examinant quorum, communication entre nœuds, autorisations et connectivité de l’agent de fencing ou configuration SBD prise en charge choisie. Confirmez que le nœud supposé défaillant ne peut pas continuer comme auteur d’écritures indépendant avant la reprise. Les preuves doivent inclure état du cluster, horodatages, résultats de fencing, état de réplication et primaire faisant autorité identifié. La conception corrective rétablit une isolation et des décisions prises en charge. Faire apparaître les ressources du cluster comme démarrées ne suffit pas à prouver que le service SAP peut accepter des écritures sans danger.

</details>

## 7. Une mise à jour financière erronée a atteint les deux réplicas HANA. Pourquoi la sauvegarde protégée d’hier peut-elle encore être utile ?

<details>
<summary>Réponse</summary>

La réplication préserve la disponibilité, mais peut copier les erreurs logiques. Une sauvegarde protégée et une chaîne de journaux utilisable peuvent permettre une récupération à un point acceptable avant l’erreur, sous réserve du processus de restauration pris en charge choisi. Établissez le RPO approuvé par le métier, les dépendances de restauration, la rétention et toute transaction légitime ultérieure à réconcilier. Confirmez la cohérence applicative ; un instantané générique de VM n’est pas automatiquement suffisant. Les preuves doivent inclure choix du point de récupération, disponibilité des sauvegardes et journaux, plan de restauration isolée, vérifications de base de données et validation métier. Une réplication réussie seule ne peut pas récupérer l’exactitude historique après réception du même mauvais changement par les deux copies.

</details>

## 8. La bascule réussit les vérifications de base, puis les utilisateurs saisissent de nouvelles commandes d’achat. Le retour arrière peut-il simplement rediriger le DNS vers la source inchangée ?

<details>
<summary>Réponse</summary>

Cela abandonnerait les nouvelles transactions ou créerait des historiques divergents. La procédure exige une décision distincte dès le début des écritures sur la cible : geler à nouveau les écritures, identifier le jeu de données faisant autorité, préserver les nouvelles transactions et évaluer une réconciliation ou migration inverse prise en charge. Incluez approbation métier, files d’attente d’interfaces, synchronisation finale, isolation de la source et validation avant de rouvrir l’un ou l’autre côté. Les preuves sont une chronologie de propriété des écritures et une décision documentée de traitement des données, pas seulement des instructions DNS. La répétition doit distinguer retour arrière avant réouverture des écritures et récupération ultérieure, avec des échéances claires et des opérateurs responsables de chaque point de décision.

</details>

## 9. Le portail de recherche ne peut pas atteindre SAP RISE. Son opérateur doit-il modifier les NSG dans l’abonnement de SAP avec le rôle Azure de l’université ?

<details>
<summary>Réponse</summary>

Respectez d’abord la matrice contractuelle des responsabilités. SAP gère le paysage RISE dans son propre environnement Azure ; un rôle dans l’abonnement de l’université n’accorde pas le contrôle de ces ressources. Retracez DNS, routes, peering ou connectivité, règles de pare-feu, identité et interface SAP convenue du portail, en attribuant chaque vérification au bon responsable. Coordonnez les changements côté SAP et l’escalade par l’intermédiaire de SAP. Les preuves doivent inclure le point de transfert défaillant et les responsabilités des deux parties. RISE ne supprime pas la responsabilité du client pour ses propres services d’intégration, sa configuration de sécurité ou son chemin réseau vers une interface disponible.

</details>

## 10. La région de reprise dispose d’une copie actuelle de la base et de VM en cours d’exécution, mais les achats restent indisponibles. Que doit encore valider l’exercice sur table ?

<details>
<summary>Réponse</summary>

Validez services centraux, ordre de démarrage applicatif, identité, DNS, noms virtuels, routes, secrets, fichiers partagés, points de terminaison d’intégration et capacité suffisante prise en charge. Comparez le point de récupération utilisable et le temps de restauration prévisionnel aux RPO et RTO métier. Empêchez le primaire initial d’accepter des écritures indépendantes. Définissez un processus d’achat et un échange d’interface réussis comme vérifications d’acceptation, suivis d’un plan de retour au primaire contrôlé. Les preuves doivent inclure responsables, ordre des dépendances, état de réplication, durées prévisionnelles et critères de validation. Une infrastructure en fonctionnement n’est qu’une partie du rétablissement d’un service SAP universitaire complet.

</details>

Les dates des objectifs et six références techniques principales figurent dans le [guide](AZ-120.md). Développez des schémas et des procédures d’exploitation examinables dans le [cahier d’exercices](AZ-120-workbook.md).
