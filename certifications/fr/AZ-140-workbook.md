# AZ-140 · Cahier d'exercices avancés commun

[Guide](AZ-140.md) · [10 cas](AZ-140-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes dans toutes les langues. Travaillez hors ligne avec l'application universitaire de notes et la salle informatique virtuelle. Consignez les prévisions comme telles ; ces unités ne déploient rien, ne modifient aucun tenant et n'établissent pas une aptitude à la production.

<a id="az-140-unit-1"></a>

## 1. Cartographier les ressources, les utilisateurs et les responsabilités

Dessinez une salle mutualisée pour 48 étudiants et un bureau personnel pour un chercheur. Identifiez les pools d'hôtes, les hôtes de session, les groupes d'applications, l'inscription dans l'espace de travail et les affectations aux utilisateurs. Séparez les responsabilités de Microsoft concernant le répartiteur de connexions et la passerelle de celles du client concernant les images, les machines virtuelles, le réseau, l'intégration des identités et le stockage. Expliquez pourquoi le fonctionnement multisession pris en charge diffère de l'affectation personnelle.

**Scénario :** un étudiant voit les machines virtuelles Azure, mais son flux de bureaux est vide. **Éléments probants :** un schéma des relations entre ressources, le droit effectif d'accès au groupe d'applications, le compte client prévu et les hypothèses de licences. **Livrable :** les trois premières vérifications, une élévation de rôle inadaptée que vous écartez et un responsable pour chaque dépendance gérée par le client. Reliez la conception aux [bases du calcul](../../fr/03-compute.md).

<a id="az-140-unit-2"></a>

## 2. Suivre séparément l'identité et le transport

Comparez la jonction Entra, la jonction AD DS et la jonction Entra Domain Services au regard d'une application ancienne et de l'authentification choisie pour le stockage des profils. Représentez l'authentification au flux, les droits d'accès, l'ouverture de session et l'accès aux fichiers comme des étapes distinctes. Ajoutez la connexion inversée HTTPS sortante et un chemin UDP Shortpath propre à une option donnée. Expliquez l'accessibilité privée de l'écouteur managé et la manière dont ICE/STUN ou TURN modifie les exigences de transport.

**Scénario :** les utilisateurs du campus se connectent sans difficulté ; ceux du domicile reçoivent une nouvelle demande d'authentification et disposent de sessions plus lentes. **Éléments probants :** la version du client, le type de jonction, les hypothèses de SSO et d'accès conditionnel, le transport négocié, le chemin DNS et les observations de latence nécessaires. **Livrable :** deux hypothèses indépendantes et les tests permettant de les confirmer, sans exposer TCP 3389 au public. Revoyez les [bases des réseaux](../../fr/05-networking.md).

<a id="az-140-unit-3"></a>

## 3. Protéger les profils et publier une application utilisable

Concevez des conteneurs FSLogix persistants hors des hôtes mutualisés remplaçables. Documentez la compatibilité identité/Kerberos du stockage, les autorisations de partage et NTFS, la capacité, les hypothèses de pointe de connexions, le comportement à connexion unique et les objectifs de sauvegarde et de restauration. Distinguez les préférences de profil des données de référence de l'application de notes. Comparez l'installation de l'éditeur dans l'image avec un package App Attach pris en charge et expliquez séparément la publication RemoteApp.

**Scénario :** un étudiant atteint le bureau, mais reçoit un profil temporaire et ne peut pas lancer l'éditeur. **Éléments probants :** l'erreur de rattachement du conteneur, le propriétaire de la session active, les autorisations attendues, la version d'image de l'hôte, l'accès au package et les affectations. **Livrable :** un arbre de défaillances ordonné, avec des branches distinctes pour le profil et l'application, une proposition de reprise sûre et des critères de préservation du travail utilisateur existant.

<a id="az-140-unit-4"></a>

## 4. Publier les images et calculer la capacité de la salle

Rédigez un plan de publication d'image de référence versionnée couvrant le système d'exploitation pris en charge, les agents, la stratégie de sécurité, les applications, les utilisateurs de validation, le comportement de drainage et le retour arrière. Avec une limite mesurée de 12 sessions par hôte, calculez la capacité pour 48 étudiants pendant la panne d'un hôte. Distinguez la méthode choisie dans un plan de mise à l'échelle de Start VM on Connect ; incluez le temps de démarrage, l'état de santé, le nombre maximal de sessions et les contraintes de stockage.

**Scénario :** un correctif arrive avant le cours alors qu'un hôte est déjà indisponible. **Éléments probants :** un tableau de capacité à cinq hôtes, les versions d'image, la liste des vérifications de validation, les sessions actives et les exclusions de maintenance. **Livrable :** un déploiement progressif qui préserve une capacité utilisable suffisante, avec des déclencheurs de retour arrière et une politique explicite pour les utilisateurs encore connectés lors de la réduction de capacité.

<a id="az-140-unit-5"></a>

## 5. Mener un exercice sur table d'échec de connexion et de reprise

Suivez une connexion synthétique à l'aide d'horodatages UTC, d'un utilisateur pseudonymisé, d'une ressource, d'un hôte et d'un identifiant de corrélation. Précisez les paramètres de diagnostic, la collecte des performances des hôtes, les journaux FSLogix et les observations de l'expérience utilisateur nécessaires. Expliquez pourquoi une tentative qui n'atteint jamais AVD peut ne laisser aucun enregistrement de connexion. Ajoutez les dépendances d'identité, de DNS, de packages applicatifs, de profils et d'API de notes à un plan de reprise dans une autre région.

**Scénario :** la classe de 09:00 ne peut pas restaurer les profils après une panne de stockage. **Éléments probants :** les points de contrôle prévus, la comparaison avec une session normale, les objectifs de reprise des profils, la capacité disponible et les responsables des coûts récurrents de machines virtuelles, de disques, de stockage, de réseau, de supervision et de licences. **Livrable :** une chronologie d'incident, une hypothèse sur la première défaillance, des critères de reprise et de retour à la région principale, ainsi qu'une distinction claire entre les prévisions de l'exercice sur table et les tests observés.

Utilisez les six références techniques du [guide](AZ-140.md) pour remettre les hypothèses à l'épreuve. Ces exercices sont des supports d'étude originaux ; ils ne couvrent pas tous les objectifs officiels et ne garantissent aucun résultat à l'examen.
