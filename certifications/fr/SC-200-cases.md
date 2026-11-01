# SC-200 · 10 cas avec réponses argumentées

[Guide](SC-200.md) · [Cahier d’exercices](SC-200-workbook.md) · [Sommaire](README.md)

Scénarios d’étude originaux, et non questions officielles de l’examen. Utilisez l’application universitaire fictive de notes et des enregistrements synthétiques. Énoncez le besoin, rejetez une solution tentante et identifiez les preuves manquantes. Il s’agit d’exercices sur table hors ligne ; aucune requête dans un locataire, aucun message ni aucune action de réponse n’est exécuté.

## 1. Les alertes Microsoft 365 apparaissent dans Defender XDR, mais le pare-feu du campus est absent. XDR le couvre-t-il déjà ?

<details>
<summary>Réponse</summary>

Non. Les preuves Microsoft 365 existantes n’établissent pas la couverture du pare-feu. Inventoriez le chemin d’export pris en charge par le pare-feu et l’analyse requise, puis évaluez un connecteur Sentinel adapté et ses prérequis. La corrélation Defender XDR et la collecte Sentinel ont des objectifs liés, mais aucune n’invente la télémétrie manquante. Je demanderais la table attendue, le schéma, les identifiants sources, le périmètre de collecte et des exemples d’heures d’arrivée. Le livrable sur table est une carte de couverture montrant les sources présentes et manquantes, en distinguant l’ingestion attendue des observations effectivement fournies.

</details>

## 2. Un connecteur indique Connected, mais une requête ne renvoie aucune ligne d’appareil. L’analyste doit-il clore l’investigation ?

<details>
<summary>Réponse</summary>

Non. Vérifiez l’intégration des appareils, les exigences de licence et de service, les types d’événements sélectionnés dans le connecteur, la table de destination, les autorisations de l’analyste, la fenêtre UTC, le délai d’ingestion et la rétention. Une table peut utiliser des champs différents du schéma supposé par la requête. Connected est un signal de configuration, pas la preuve que chaque événement requis est arrivé. Clore le dossier confondrait le manque de visibilité avec un comportement bénin. Consignez les preuves absentes et demandez au responsable de la source un échantillon borné d’événements synthétiques et des preuves du bon fonctionnement de la collecte avant de conclure.

</details>

## 3. Trois alertes partagent une adresse IP du campus. Cela suffit-il à les fusionner en une attaque confirmée ?

<details>
<summary>Réponse</summary>

Une IP partagée est une piste, surtout derrière la traduction d’adresses réseau du campus, mais elle n’identifie pas une personne ou un attaquant unique. Comparez les identifiants stables des comptes et des appareils, les preuves liées aux messages ou fichiers, les types d’activité et les horaires UTC. Les alertes sont des détections ; un incident regroupe des preuves liées et une entité est un objet impliqué. Je ne proposerais une corrélation qu’avec des relations à l’appui, en documentant l’incertitude. Les preuves requises sont une chronologie et une carte des entités qui envisagent aussi le cas d’étudiants sans lien partageant la même adresse publique.

</details>

## 4. Une alerte de point de terminaison concerne le serveur de diffusion des cours. L’étudiant analyste peut-il l’isoler immédiatement ?

<details>
<summary>Réponse</summary>

L’alerte seule n’accorde pas le pouvoir de confiner. Préservez les preuves, évaluez l’activité en cours et le périmètre probable, et consultez la procédure d’incident ainsi que le décideur autorisé. L’isolement pourrait interrompre l’enseignement ; documentez donc l’impact sur le service, la limite proposée, les alternatives et les conditions de rétablissement. Attendre sans escalade est également insuffisant si les preuves suggèrent une menace en cours. Dans cet exercice sur table, consignez l’escalade et l’action proposée ; ne l’exécutez pas. L’achèvement exigerait un enregistrement d’action approuvée et des preuves distinctes confirmant le résultat visé.

</details>

## 5. La requête synthétique du guide contient trois lignes Denied. Pourquoi le décompte attendu est-il de deux ?

<details>
<summary>Réponse</summary>

Le jeu de données répète la même paire `EventId` et compte pour `e1`. Après le filtre temporel UTC, `distinct EventId, Account` conserve une copie de cette paire plus `e2` ; l’agrégation attend donc deux événements pour `student-a`. Cette conclusion dépend de l’hypothèse énoncée d’un identifiant stable. Dédupliquer uniquement par compte fusionnerait des événements distincts et les sous-estimerait. L’événement Allowed se trouve aussi à la borne temporelle supérieure exclue. Il s’agit d’un résultat prédit par la lecture de lignes synthétiques, pas de la preuve d’une requête exécutée dans un locataire.

</details>

## 6. La jointure des messages et des connexions par compte double le nombre de résultats. Y a-t-il eu deux fois plus d’attaques ?

<details>
<summary>Réponse</summary>

Pas nécessairement. Plusieurs messages et plusieurs connexions pour un même compte peuvent produire plusieurs paires correspondantes. Précisez le type de jointure, l’unicité des clés et la relation que l’analyse cherche à établir. Le type par défaut `innerunique` modifie aussi l’entrée gauche en dédupliquant les clés de jointure, ce qui peut supprimer des distinctions utiles à l’analyste. Examinez la cardinalité de chaque entrée et ajoutez une relation temporelle adaptée avant d’interpréter la sortie. Je conserverais les ID des événements sources et comparerais les paires attendues sur un petit jeu de données synthétique, plutôt que d’assimiler des lignes jointes à des attaques.

</details>

## 7. Une chasse ne trouve aucun accès à des fichiers privés après un courriel suspect. Le rapport peut-il affirmer que le compte n’a jamais été compromis ?

<details>
<summary>Réponse</summary>

Cette affirmation dépasse les preuves. Indiquez que la requête définie n’a trouvé aucun enregistrement disponible correspondant à sa population et à son intervalle UTC. Vérifiez si l’audit applicatif était activé, si les appareils concernés étaient intégrés, si les enregistrements sont encore conservés et si l’analyste peut les lire. Examinez aussi les filtres et le sens des événements d’accès. Un remplacement d’appareil autorisé est une explication concurrente à l’activité d’un appareil inhabituel. Conservez l’hypothèse, la version de la requête, les lacunes de couverture et une question de suivi au lieu de traiter l’absence de correspondances comme une preuve de sécurité.

</details>

## 8. Un import de cours en masse crée des alertes répétées. Faut-il exclure tous les comptes enseignants de la règle ?

<details>
<summary>Réponse</summary>

Une exclusion large fondée sur le rôle pourrait masquer l’activité d’un enseignant compromis. Identifiez d’abord le compte précis autorisé pour l’import, la charge de travail, le profil temporel et les preuves d’audit. Comparez les événements synthétiques d’import étiquetés avec les accès préoccupants à des corrigés non publiés. Proposez une exception étroitement délimitée ou un ajustement de la règle et évaluez à la fois les faux positifs et les faux négatifs. Examinez aussi le chevauchement de la planification, la période rétrospective, le regroupement et la suppression avant de mettre en cause le seuil. Conservez les résultats attendus et la version de la règle dans un dossier d’ajustement ; une baisse du volume d’alertes ne démontre pas à elle seule une meilleure qualité de détection.

</details>

## 9. Une nouvelle tentative de playbook ouvrirait un autre ticket et restreindrait à nouveau le même compte. Que manque-t-il ?

<details>
<summary>Réponse</summary>

La conception exige l’idempotence et un modèle clair des états des actions. Associez le workflow à des identifiants stables d’incident et d’action, vérifiez si l’étape visée est déjà terminée et gérez les échecs partiels sans la répéter aveuglément. Vérifiez séparément les rôles de l’opérateur, l’autorisation de Sentinel d’appeler le playbook et le périmètre en aval de l’identité du workflow. Les restrictions perturbatrices nécessitent l’approbation et le chemin de rétablissement prévus par la procédure. Dans cette revue hors ligne, simulez sur papier un déclenchement en double et un dépassement de délai ; ne déployez pas le playbook et ne l’exécutez pas.

</details>

## 10. Copilot affirme qu’une alerte de charge de travail cloud prouve que student-a a téléchargé des corrigés. Son résumé suffit-il comme preuve ?

<details>
<summary>Réponse</summary>

Non. Remontez de l’affirmation aux enregistrements d’accès applicatif, à l’ID de ressource cloud, aux identifiants d’identité et à la chronologie UTC. Une alerte de charge de travail ou une recommandation de posture ne prouve pas à elle seule le téléchargement d’un document précis. Examinez les sources citées par Copilot, les intégrations disponibles ainsi que le schéma, les filtres, les jointures et les décomptes de toute requête générée. Signalez les affirmations non étayées et conservez la conclusion corrigée de l’analyste. Le dossier doit distinguer les preuves synthétiques observées, une relation déduite et les enregistrements manquants. Un résumé fluide ne peut ni fournir une télémétrie indisponible ni autoriser une réponse.

</details>

[Guide d’étude officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Sources techniques et explications](SC-200.md)
