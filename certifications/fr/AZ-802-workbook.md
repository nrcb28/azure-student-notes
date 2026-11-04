# AZ-802 · Cahier Windows Server fondé sur les preuves

[Guide](AZ-802.md) · [10 cas argumentés](AZ-802-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes réunissent les sept domaines d'étude AZ-802. Utiliser le laboratoire universitaire fictif et isolé `lab.example.test`. Produire une décision et un dossier de preuves vérifiables, pas une liste de paramètres copiés d'une vidéo. Ce sont des exercices Windows proposés ; aucune exécution sur AD, Hyper-V ou Azure, aucune restauration ni application de contrôle de sécurité n'est revendiquée. Sans laboratoire Windows compatible, remettre une conception étiquetée et des observations prévues plutôt qu'inventer des résultats.

Tenir un registre pour chaque unité : état initial, hypothèse, explication concurrente, vérification en lecture seule choisie, changement proposé, observation attendue, observation réelle si exécutée et condition d'arrêt ou de retour arrière. Consigner l'édition et la version du système, les modules installés, les droits requis et l'identité cible. Masquer secrets et données personnelles. La matrice de prérequis du guide s'applique à ses exemples ; aucune commande ne donne l'autorité d'inspecter un système sans rapport.

<a id="az-802-unit-1"></a>

## 1. Suivre une modification d'identité de l'annuaire jusqu'à l'accès

**Scénario :** LAB-DC1 accepte un changement d'appartenance au groupe de recherche, mais un client du bâtiment distant n'accède toujours pas à `\\LAB-FS1\LabNotes`. Le client sélectionne LAB-DC2. Un projet d'agence distinct utilise un RODC, car la salle dispose d'une protection physique limitée.

**Investigation :** dessiner la forêt et le domaine, les deux contrôleurs accessibles en écriture, le RODC d'agence, les résolveurs DNS, les sites et les associations de sous-réseaux IP. Marquer le contrôleur ayant accepté le changement et celui utilisé par le client. Identifier le chemin de réplication, les SRV pertinents, la hiérarchie de temps, le jeton utilisateur et le périmètre partage/NTFS. Choisir une séquence ordonnée de vérifications distinguant un état d'annuaire périmé d'un problème d'accès effectif. Inclure une observation attendue qui réfuterait la première hypothèse.

Utiliser les requêtes d'inventaire AD, de résolveur/temps et de réplication du guide uniquement dans un contexte d'administration Windows approprié. Pour la stratégie de groupe, expliquer séparément périmètre, traitement client et paramètres effectifs. Pour le RODC, définir les comptes ordinaires admissibles à l'accès déconnecté, ceux qui doivent rester refusés, l'administration déléguée d'agence et la réponse à une perte d'appareil. Vérifier la stratégie effective de réplication des mots de passe plutôt que la déduire du nom d'un groupe.

**Preuves :** topologie avec périmètres d'identité ; contextes de requête et horodatages expurgés ; chronologie de modification d'objet ; sélection prévue et observée du contrôleur ; paire de tests d'accès aux fichiers autorisé/refusé ; décision de cache RODC sans mot de passe.

**Livrable et conditions de décision :** rédiger un diagnostic d'une page avec une réparation limitée proposée. Préserver les paramètres initiaux de résolveur, de site et de stratégie avant toute modification autorisée du laboratoire. Arrêter si le contrôleur défaillant ou l'espace de noms sort du laboratoire jetable. Ne pas élargir les privilèges, prendre de force les rôles FSMO ni réinitialiser tous les comptes pour faire disparaître le symptôme. La réussite signifie que la modification d'annuaire requise converge et que l'utilisateur prévu reçoit seulement l'accès prévu, tandis que l'utilisateur interdit reste refusé.

<a id="az-802-unit-2"></a>

## 2. Examiner les périmètres d'administration distante et de récupération des VM

**Scénario :** un opérateur atteint à distance un serveur membre, mais pas une seconde ressource. Une proposition active la délégation d'identifiants réutilisables et exécute un point JEA sur un DC. En parallèle, l'étape de cohérence de production d'une VM échoue, mais un point standard est créé. Le laboratoire possède deux hôtes de 64 Gio, une réserve synthétique de 12 Gio par hôte et douze invités à mémoire fixe de 4 Gio attribués à chaque hôte.

**Investigation :** dessiner chaque saut d'authentification, le protocole, l'identité effective et l'opération requise. Comparer une conception de deuxième saut prise en charge aux risques de CredSSP et aux limites de délégation propres aux protocoles. Examiner commandes et paramètres autorisés JEA, groupes d'exécution, audit et emplacement ; expliquer pourquoi les privilèges par défaut d'un compte virtuel sur DC sont excessifs pour une tâche limitée de service membre. Pour une machine gérée par Arc, identifier séparément l'autorité d'extension Azure et les permissions locales.

Utiliser l'inventaire des VM, commutateurs, mémoires et points de contrôle pour expliquer le réseau invité et l'état de récupération. Comparer points de contrôle, Replica, clustering et sauvegarde protégée selon la panne traitée par chacun. Expliquer Production et ProductionOnly ainsi que l'importance du type réel de point. Dans le dimensionnement synthétique, la mémoire normalement attribuée vaut 48 + 12 = 60 Gio par hôte ; déplacer les 24 invités sur un seul demanderait 96 + 12 = 108 Gio. Préciser les hypothèses et montrer pourquoi tenir en fonctionnement normal ne démontre pas la capacité après panne d'un hôte.

**Preuves :** schéma des permissions et des sauts ; revue du point restreint ; chemin commutateur/invité ; feuille de calcul mémoire ; métadonnées réelles du point de contrôle si disponibles ; plan de copie indépendante de restauration.

**Livrable et conditions de décision :** proposer une conception d'administration prise en charge et au périmètre limité, ainsi que des mécanismes de récupération séparés. Arrêter si la délégation expose une identité réellement privilégiée ou si les exigences de cohérence prises en charge de la VM sont inconnues. Consigner les paramètres du point avant changement et l'accès de récupération. Ne pas supprimer d'AVHDX, affirmer que Replica corrige la corruption logique ni qualifier de sauvegarde indépendante un point sur le même stockage. Une commande réussie et un service récupérable en sécurité demandent des validations différentes.

<a id="az-802-unit-3"></a>

## 3. Diagnostiquer le chemin du client au fichier à travers réseau et stockage

**Scénario :** de nouveaux clients de salle de cours n'obtiennent pas d'adresse, tandis que les anciens baux continuent. Après une correction réseau approuvée, un utilisateur de recherche atteint un partage, mais reçoit un refus sur un dossier. Le serveur est enregistré dans Azure File Sync et certains fichiers sont hiérarchisés. Le schéma comprend aussi un redirecteur conditionnel DNS hybride et un second serveur DHCP non configuré.

**Investigation :** suivre le VLAN et le relais client, l'étendue DHCP autorisée, exclusions et réservations, options et capacité libre. Définir ce qu'un véritable test de nouvelle attribution apporte par rapport à un test de client existant. Distinguer un second serveur d'une relation de basculement configurée et prise en charge. Suivre le résolveur prévu, l'espace de noms, la cible de redirection conditionnelle, le retour et le port applicatif ; une réponse DNS correcte ne démontre pas une connexion SMB utilisable.

Consigner ensuite l'utilisateur réel, l'autorisation de partage, l'héritage NTFS et le contexte du jeton de groupes. Tester une identité autorisée et une identité qui doit rester refusée. Pour Azure Files, séparer la configuration d'identité prise en charge, l'autorisation de partage et les permissions de répertoire/fichier. Inventorier les points File Sync, les hypothèses de cache local, les sauvegardes indépendantes conservées et une procédure de récupération prise en charge. Rejeter explicitement la restauration, le clonage ou le retour arrière du système ou de la VM d'un serveur enregistré comme méthode générique de récupération File Sync.

**Preuves :** fiche d'attribution des adresses ; schémas de résolveur et de routes ; observations de partage/ACL sans secrets ; critères de tests autorisé/refusé ; carte des points cloud et serveur ; point historique de récupération choisi avec ses dépendances.

**Livrable et conditions de décision :** expliquer la panne réseau et la panne de permissions comme deux constats distincts. Capturer l'étendue et l'ACL existantes avant toute modification autorisée. Arrêter face à une plage d'attribution qui chevauche une autre, un élargissement involontaire des permissions ou une dépendance de récupération non protégée. Réussir exige que le nouveau client prévu obtienne des paramètres valides, que l'utilisateur prévu accède au dossier, que l'utilisateur interdit reste bloqué et que le plan de récupération identifie une copie protégée plutôt qu'un simple autre point synchronisé.

<a id="az-802-unit-4"></a>

## 4. Concevoir un renforcement par rôle sans perdre l'accès de récupération

**Scénario :** le parc comprend Windows Server 2022 et 2025, des serveurs membres, un DC et un serveur de fichiers. Une proposition déploie la même base OSConfig partout, expose SMB sur QUIC sans vérifier les certificats et partage un mot de passe LAPS dans un rapport. Retirer la base est présenté comme un retour arrière complet.

**Investigation :** construire une matrice rôle/version avant de choisir les contrôles. Les recommandations OSConfig examinées ciblent Windows Server 2025 ; noter version du module, scénario, différences de réglages attendues, besoin de redémarrage et conflits avec GPO ou autre gestion existante. Tester le rôle approprié. Expliquer pourquoi retirer la gestion ne peut pas être supposé reconstruire l'état antérieur. Conserver un relevé protégé de cet état et un autre chemin d'administration autorisé.

Pour LAPS, séparer rotation, destination de sauvegarde, récupération autorisée, audit et accès de reprise. Documenter les conditions de récupération DSRM pertinentes, sans récupérer ni publier de mot de passe. Pour SMB sur QUIC, vérifier précisément la prise en charge serveur/client : les recommandations examinées citent Windows Server 2022 Datacenter: Azure Edition ou les éditions Windows Server 2025, avec des clients Windows 11. Examiner confiance, noms et utilisation de clé privée du certificat ainsi que le chemin UDP permis, puis préserver l'autorisation partage/fichiers. Ne pas considérer QUIC comme son remplacement.

**Preuves :** matrice rôle/version ; contrôles choisis avec références de prise en charge ; différence des réglages et condition de retour arrière ; rôles de récupération permis et refusés ; liste de vérification de certificat expurgée ; plan isolé de tests d'accès autorisé/refusé.

**Livrable et conditions de décision :** rédiger une proposition de changement progressif avec responsabilités de récupération nommées. Arrêter si la base n'est pas prise en charge, si l'unique chemin de gestion serait supprimé, si une exigence de certificat reste non résolue ou si un véritable secret apparaît dans les preuves. Traiter toute divulgation existante d'identifiants selon le processus de réponse de l'organisation. Résultat de conformité, fonction installée et application démontrée sont des observations distinctes.

<a id="az-802-unit-5"></a>

## 5. Suivre un événement absent et répéter la récupération d'annuaire

**Scénario :** un serveur géré par Arc indique Connecté et AMA envoie Heartbeat, mais un événement System requis existe seulement localement. Dans un exercice sur table distinct, un objet AD est supprimé alors que la Corbeille n'était pas activée auparavant. Une sauvegarde d'annuaire prise en charge existe. L'équipe vise une restauration en deux heures et veut des preuves plus solides que « la VM démarre ».

**Investigation :** suivre un événement local expurgé par l'extension et le service AMA prévus, la DCR, l'association, la sélection de source, la destination et la période de requête. Consigner séparément identité de machine, heure d'événement et heure d'arrivée. Définir un test distinguant événements sources absents, configuration de collecte manquante et requête vers une mauvaise table ou un mauvais espace de travail. Expliquer ce que démontrent respectivement connexion Arc et Heartbeat, ainsi que leurs incertitudes.

Pour la récupération d'annuaire, identifier objets et dépendances affectés, sauvegarde prise en charge disponible, responsable, identifiants DSRM protégés et périmètre de restauration approprié. Distinguer récupération d'objet par la Corbeille, restauration d'annuaire faisant autorité ou non, récupération SYSVOL et récupération de toute la forêt. Choisir une procédure prise en charge pour la panne réelle ; ne pas transformer une erreur sur un seul objet en retour arrière automatique du contrôleur ou en prise forcée FSMO. Répéter l'ordre des dépendances, les implications de réplication, la validation et le retour sûr des services récupérés.

**Preuves :** suivi de l'événement de sa source à sa destination ; journal d'hypothèses horodaté ; inventaire des points de récupération ; durées prévues clairement présentées comme estimations ; vérifications d'acceptation couvrant l'objet requis, l'authentification, la réplication, la stratégie et l'application affectée.

**Livrable et conditions de décision :** produire des runbooks distincts de supervision et de récupération. Préserver les preuves initiales de DCR et d'association avant les modifications. Arrêter si le périmètre de récupération ou la copie de référence n'est pas clair. Tenir une chronologie de l'interruption métier et des données récupérées utilisables pour ne pas confondre RTO et RPO. Enregistrer une opération comme terminée seulement après son exécution par un laboratoire autorisé fournissant les observations indiquées. Le dépôt lui-même ne revendique aucune restauration Windows/AD ni résultat mesuré de deux heures.

Terminer en répondant aux [dix cas](AZ-802-cases.md) sans ouvrir leurs explications. Pour chaque réponse faible, identifier la preuve manquante ou le périmètre confondu et revenir à cette partie du [guide](AZ-802.md). Ce cahier fournit une pratique choisie, pas une couverture exhaustive des objectifs ni une prédiction de réussite.
