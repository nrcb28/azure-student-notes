# AZ-802 · 10 cas avec réponses argumentées

[Guide](AZ-802.md) · [Cahier en cinq unités](AZ-802-workbook.md) · [Sommaire](README.md)

Ces scénarios originaux se déroulent dans un laboratoire universitaire ; ce ne sont pas des questions officielles d'examen. Formuler une hypothèse, une explication alternative et les preuves nécessaires avant d'ouvrir une réponse. Les commandes citées sont des vérifications proposées pour un laboratoire Windows autorisé ; aucune exécution ni récupération de production n'est revendiquée. Chaque question contient le scénario complet pour que l'entraîneur et l'export Anki en conservent le contexte.

## 1. Après une modification du réseau de la salle de cours, un client de domaine résout les sites publics, mais ne trouve pas son contrôleur de domaine. Son résolveur est un service DNS public ; le serveur DNS AD configuré est joignable et ses enregistrements SRV sont réputés sains. L'heure du client est correcte. La première réparation doit-elle réinitialiser tous les mots de passe étudiants ?

<details>
<summary>Raisonnement</summary>

Non. Les éléments fournis orientent d'abord vers le chemin de résolution du client. La réussite du DNS public ne démontre pas la découverte des enregistrements privés de service AD. Consigner le résolveur du client, la requête SRV pertinente et son résultat, puis comparer ce chemin à la configuration DNS approuvée du laboratoire. Une correction adaptée rétablit le chemin prévu vers un résolveur connaissant AD, puis vérifie découverte, joignabilité du contrôleur et connexion affectée avant d'élargir la modification.

Les hypothèses de serveur sain et d'heure correcte réduisent le périmètre de cette investigation ; elles ne signifient pas que toute panne réelle de connexion vient du DNS. Si la découverte réussit mais que l'authentification échoue encore, poursuivre avec l'erreur exacte, l'état du compte et les preuves de protocole et de canal sécurisé. Préserver un relevé avant/après avec horodatages et contrôleur réellement sélectionné. Réinitialiser tous les mots de passe changerait un état sans rapport sans corriger l'écart de résolveur identifié, et pourrait masquer des éléments utiles. Le retour arrière consiste à restaurer la configuration client enregistrée si le changement approuvé perturbe d'autres résolutions nécessaires, plutôt que laisser un assemblage de résolveurs public et privé dont le comportement reste incompris.

</details>

## 2. Une modification d'appartenance au groupe de recherche est visible sur LAB-DC1, mais pas sur le contrôleur du bâtiment distant. Les clients y utilisent ce second contrôleur, la réplication signale des échecs liés au DNS et un nouveau partage reste inaccessible. Ajouter l'utilisateur à un autre groupe privilégié est-il une correction adaptée ?

<details>
<summary>Raisonnement</summary>

Non. Les versions observées de l'annuaire et l'échec de réplication fournissent une explication concrète à examiner avant d'élargir les privilèges. Consigner l'heure du changement, le contrôleur qui l'a accepté, celui sélectionné par le client et les erreurs de réplication. Vérifier les enregistrements DNS des partenaires, leurs résolveurs configurés, la connectivité et les prérequis d'authentification. Vérifier que le sous-réseau distant correspond au site prévu, sans supposer qu'un changement de calendrier de site répare un échec DNS.

Après une réparation prise en charge, confirmer que cette modification précise d'appartenance a atteint le contrôleur concerné. Obtenir ensuite un nouveau jeton adapté de connexion ou de session utilisateur et tester le partage prévu sous cette identité ; convergence de l'annuaire et renouvellement du contexte d'autorisation sont distincts. Examiner aussi les permissions du partage et du système de fichiers si l'accès échoue encore. Garder un groupe limité et consigner un test autorisé et un test refusé. Un groupe privilégié sans rapport pourrait masquer le symptôme en laissant la réplication défaillante et en élargissant l'accès étudiant. Le livrable est une chronologie de convergence et d'accès, avec les observations prévues étiquetées comme telles tant qu'un test de laboratoire ne les a pas réellement fournies.

</details>

## 3. Une salle de cours isolée en agence utilisera un RODC. Une proposition y autorise la mise en cache des mots de passe des administrateurs privilégiés de l'université pour leur connexion pendant les pannes WAN. La protection physique de la salle est plus faible que celle du centre de données principal. Que doit exiger la revue de conception ?

<details>
<summary>Raisonnement</summary>

Rejeter l'hypothèse selon laquelle un RODC sécurise n'importe quel identifiant mis en cache. Examiner sa stratégie de réplication des mots de passe, les appartenances effectivement autorisées et refusées, l'administration déléguée et la procédure de perte physique. Les comptes privilégiés doivent rester hors de ce cache d'agence. Si un compte est à la fois autorisé et refusé par la stratégie effective, le refus prévaut. Identifier les comptes ordinaires limités qui ont réellement besoin d'un accès déconnecté et vérifier la stratégie résultante plutôt que se fier au seul nom d'un groupe.

Le plan doit distinguer l'authentification des utilisateurs en cache des opérations nécessitant un contrôleur accessible en écriture, notamment les états nouveaux ou modifiés de l'annuaire. Définir les services restant utilisables pendant l'interruption WAN et la façon dont les opérateurs obtiendront un chemin administratif approuvé sans affaiblir le périmètre du domaine. Les preuves incluent les hypothèses de menace de l'agence, les comptes choisis, les décisions effectives de cache, la connectivité des contrôleurs et la réponse à la perte d'appareil. Ne publier ni mots de passe ni contenu du cache. Le plan de récupération doit traiter les identifiants en cache concernés et le serveur compromis, pas seulement remplacer le matériel en supposant tous les secrets d'annuaire restés protégés.

</details>

## 4. Un serveur connecté à Azure Arc échoue encore sur une tâche distante du serveur B vers le serveur de fichiers C. Quelqu'un propose une large délégation d'identifiants et un compte virtuel JEA par défaut sur un contrôleur de domaine. La tâche nécessite seulement une opération de service limitée. La connexion Arc justifie-t-elle cette conception ?

<details>
<summary>Raisonnement</summary>

Non. La connexion Arc crée une relation d'administration Azure ; elle ne joint pas le serveur à AD, ne crée pas d'approbation de forêt et ne délègue pas automatiquement les identifiants de l'opérateur interactif vers C. Dessiner le premier et le deuxième saut, le protocole de chacun, l'identité effective et l'opération exacte nécessaire. Diagnostiquer le périmètre d'autorisation et d'authentification en échec. Une première session réussie ne prouve pas que la seconde ressource acceptera l'identité prévue.

Examiner les options prises en charge pour le deuxième saut et leurs limites avant de choisir. CredSSP expose davantage les identifiants ; les méthodes de délégation contrainte ne résolvent pas de façon générique un deuxième saut WinRM vers WinRM. Pour JEA, examiner ensemble identité d'exécution, utilisateurs autorisés, commandes, paramètres et piste d'audit. Un compte virtuel par défaut sur un DC peut posséder les privilèges Administrateurs du domaine, disproportionnés pour une tâche de service étroite. Préférer un emplacement de gestion adapté et des droits d'exécution explicitement restreints. La preuve est un schéma des permissions et des sauts avec opérations permises et refusées, pas une commande réussie grâce à des identifiants administrateur réutilisables. Les droits d'extension sur un contrôleur géré par Arc doivent aussi être revus séparément.

</details>

## 5. Une VM de laboratoire utilise des points de contrôle de production, mais le traitement de cohérence invité échoue et l'hôte crée un point standard. Un étudiant le qualifie de sauvegarde indépendante cohérente avec l'application. Le point et les disques de la VM partagent le même stockage. Que faut-il corriger ?

<details>
<summary>Raisonnement</summary>

Corriger à la fois l'affirmation de cohérence et le périmètre de protection. Le mode Production peut autoriser le repli vers un point standard ; le paramètre demandé est donc une preuve plus faible que le type réel du point et le résultat du traitement invité. Si l'exercice exige un point de production sans repli, évaluer ProductionOnly et corriger les prérequis d'intégration invitée, de VSS ou de gel du système de fichiers concerné. Le refus de créer le point requis est une preuve d'échec utile ; accepter silencieusement un autre type n'est pas équivalent.

Même un point de production réussi ne démontre pas l'existence d'une sauvegarde indépendante conservée. Sa chaîne de disques peut disparaître avec le stockage de la VM, et la récupération applicative nécessite encore une méthode de cohérence et de restauration prise en charge. Prévoir une sauvegarde protégée avec rétention adaptée et plan de validation de restauration lorsque l'exigence le demande. Inspecter métadonnées du point et réserve de stockage par les outils pris en charge ; ne pas supprimer les fichiers AVHDX manuellement. Expliquer séparément si l'objectif est d'annuler une modification de laboratoire jetable, de survivre à une perte d'hôte ou de stockage ou de récupérer un état applicatif antérieur valide. Chaque objectif demande des preuves différentes et parfois un autre mécanisme.

</details>

## 6. Les PC existants de la salle fonctionnent, mais les nouveaux clients n'obtiennent pas d'adresse. Le serveur DHCP autorisé est joignable par un relais fonctionnel ; son étendue concernée n'a plus de baux libres. Un second serveur est installé, sans relation de basculement. Que doit conclure l'investigation ?

<details>
<summary>Raisonnement</summary>

Les éléments fournis identifient l'épuisement de l'étendue comme problème immédiat des nouvelles attributions. Les clients existants peuvent continuer selon leur état de bail ; leur réussite ne prouve donc pas que le serveur peut attribuer une adresse supplémentaire. Examiner les plages, exclusions, réservations, baux actifs et le sous-réseau réel avant de proposer une correction de capacité approuvée. Rechercher des allocations périmées ou inattendues, sans supprimer les baux sans discernement ni étendre vers une plage qui chevauche une autre.

Un second serveur installé ne coordonne pas automatiquement les baux. Si la disponibilité est requise, concevoir une relation de basculement DHCP prise en charge pour les étendues prévues, en comprenant mode, état du partenaire, comportement des baux et responsabilités de récupération. Ne pas activer de copies concurrentes non gérées de la même plage. Les preuves comprennent l'inventaire d'étendue, le nombre d'adresses disponibles, le chemin de relais et un test avec un véritable nouveau client ainsi qu'un client existant. Capacité et basculement répondent à des pannes différentes : un partenariat sain ne permet pas d'ignorer un pool sous-dimensionné. Consigner l'étendue avant changement et arrêter si la plage proposée entre en conflit avec le routage ou une autre autorité d'attribution.

</details>

## 7. Un étudiant possède l'autorisation prévue sur un partage SMB, mais NTFS refuse l'accès à un dossier de projet. Azure File Sync est sain et son point serveur contient des fichiers hiérarchisés. Accorder le rôle Contributeur Azure et qualifier la copie synchronisée de sauvegarde résoudrait-il les deux problèmes ?

<details>
<summary>Raisonnement</summary>

Non. Suivre le chemin de fichiers Windows et l'identité réels. Le refus NTFS identifié reste pertinent même quand les permissions du partage sont présentes. Corriger l'autorisation prévue du dossier avec des groupes et une isolation adaptés, puis tester l'étudiant concerné et un autre qui doit rester refusé. Un rôle de gestion des ressources Azure ne répare pas automatiquement l'ACL du système de fichiers et n'établit pas d'accès SMB aux données. Inspecter l'accès effectif plutôt que le déduire d'une entrée configurée isolée.

Traiter la récupération séparément. Une synchronisation saine peut propager une suppression et des fichiers serveur hiérarchisés peuvent ne pas constituer une copie locale indépendante complète. Identifier le point cloud, les sauvegardes conservées utilisables, les dépendances de restauration et la procédure prise en charge. Restaurer ou cloner un serveur File Sync enregistré depuis une image système ou un point de contrôle de VM n'est pas une méthode générique de récupération prise en charge. Les preuves doivent inclure la décision partage/NTFS, l'état du point de terminaison et de la hiérarchisation ainsi qu'un plan de point de récupération historique. Rétablir l'accès aujourd'hui et pouvoir récupérer les données après une erreur ultérieure sont deux résultats distincts ; aucun ne doit être revendiqué sans son test ou des éléments de conception explicitement étiquetés.

</details>

## 8. Un parc mixte contient Windows Server 2022 et 2025. Une proposition de renforcement applique partout une base OSConfig Windows Server 2025, puis promet que retirer la gestion restaure tous les anciens paramètres. Elle stocke aussi un mot de passe LAPS récupéré dans un rapport partagé. Que faut-il changer ?

<details>
<summary>Raisonnement</summary>

Séparer la prise en charge, le retour arrière et le traitement des secrets. Les recommandations OSConfig examinées ciblent Windows Server 2025 ; il ne faut donc pas présenter la même configuration comme prise en charge sur les machines 2022. Consigner les versions système et module, les paramètres par rôle et un groupe pilote. Identifier les GPO ou autres gestions existantes susceptibles de conflits, inspecter les réglages effectifs et prévoir le redémarrage nécessaire et la validation d'accès. Retirer une base ne garantit pas la reconstruction de chaque valeur antérieure à la gestion ; conserver un état initial revu et une procédure de récupération.

LAPS permet rotation contrôlée, sauvegarde et récupération autorisée des mots de passe. Copier un mot de passe récupéré dans un rapport largement lisible détruit ce périmètre d'accès. Le retirer par le processus d'incident ou de changement approprié, traiter l'exposition selon la politique et effectuer une rotation si nécessaire ; ne publier que des preuves expurgées de stratégie et d'autorisation. Les identifiants de récupération exigent un accès protégé restant utilisable pendant la panne anticipée. Les preuves doivent montrer déploiement pris en charge, rôles de récupération permis et refusés, accès audité et plan de récupération, plutôt qu'un identifiant en clair ou une capture de conformité supposée prouver toutes les protections.

</details>

## 9. Un serveur Arc affiche Connecté et son espace de travail contient des lignes Heartbeat récentes de l'agent, mais les événements Windows System requis sont absents alors qu'ils existent localement. La requête vide prouve-t-elle que Windows n'a généré aucune erreur ?

<details>
<summary>Raisonnement</summary>

Non. Le scénario précise déjà que les événements pertinents existent localement. Connectivité Arc et Heartbeat de l'agent sont des observations différentes de la livraison réussie de la source d'événements sélectionnée. Confirmer la machine prévue, la fenêtre temporelle, l'espace de travail et la table de destination, puis inspecter l'état de l'extension et du service AMA, la DCR associée, sa sélection d'événements, sa destination et la configuration effectivement reçue par l'agent. Créer une DCR ne suffit pas : elle doit être associée à cette machine pour y collecter les données.

Utiliser un identifiant local d'événement expurgé et son horodatage pour suivre un événement dans le pipeline prévu. Distinguer absence à la source, échec de collecte, problème de transport ou configuration et requête vers une mauvaise destination. Séparer l'heure de l'événement de l'arrivée de la collecte, et tenir compte du délai d'ingestion documenté sans juger tout retard acceptable. Les preuves incluent le relevé local, l'identité de machine, l'association et le contexte de requête, suivis d'un test d'arrivée attendue. Éviter de réinstaller tous les agents en premier : cela modifie l'état et peut effacer un contexte utile sans traiter la sélection ou l'association manquante.

</details>

## 10. Un étudiant supprime un objet AD important et découvre que la Corbeille n'était pas activée avant la suppression. Il propose de ramener un contrôleur de domaine de production à un point de contrôle VM ordinaire et de prendre de force tous les rôles FSMO. L'organisation dispose d'une sauvegarde d'annuaire prise en charge et d'un responsable de récupération. Quel processus de décision est plus sûr ?

<details>
<summary>Raisonnement</summary>

Transmettre le cas à la procédure documentée de récupération d'annuaire et préserver les éléments de suppression, réplication et sauvegarde. Activer la Corbeille après l'événement ne crée pas magiquement l'état antérieur récupérable manquant. Déterminer l'objet et les dépendances affectés, la sauvegarde prise en charge disponible et le périmètre de restauration avant de choisir une méthode. Une erreur sur un seul objet ne justifie pas, à elle seule, la récupération d'une forêt entière ou la prise de rôles FSMO sans rapport.

Le responsable doit choisir les étapes prises en charge de restauration faisant autorité ou non adaptées à la panne réelle, avec un contexte DSRM si requis, des identifiants de récupération protégés et les considérations SYSVOL. Un retour générique à un point de contrôle VM ne remplace pas ce plan. Documenter l'état de référence, les implications de réplication, la validation et les conditions de retour d'un ancien détenteur de rôle si une prise forcée est réellement nécessaire. Valider objets d'annuaire, authentification, réplication et service affecté, sans s'arrêter à « la VM démarre ». Dans ce dépôt, le livrable est un exercice sur table avec des étapes de décision explicites ; aucune restauration d'annuaire, prise de rôle ou récupération mesurée n'a été exécutée.

</details>

Utiliser les références techniques et les conditions de version du [guide](AZ-802.md). Développer les preuves et les décisions de changement contrôlé dans le [cahier](AZ-802-workbook.md).
