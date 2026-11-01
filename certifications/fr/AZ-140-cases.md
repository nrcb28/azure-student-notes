# AZ-140 · 10 cas avec réponses argumentées

[Guide](AZ-140.md) · [Cahier d'exercices](AZ-140-workbook.md) · [Sommaire](README.md)

Scénarios originaux de salle informatique universitaire, et non questions d'examen officielles. Expliquez le besoin et les éléments qui permettraient de le confirmer avant de révéler chaque réponse. Tous les résultats ci-dessous relèvent d'un raisonnement de conception ; aucun déploiement cloud n'est revendiqué.

## 1. Quarante étudiants ont besoin de bureaux interchangeables, tandis qu'un chercheur a besoin de la même machine dédiée. Faut-il attribuer un pool personnel à chacun ?

<details>
<summary>Réponse</summary>

Évaluez un pool d'hôtes mutualisé avec un système d'exploitation multisession pris en charge pour les étudiants, et une affectation personnelle pour le chercheur. Des machines dédiées pour tous pourraient consommer une capacité inutile, tandis qu'imposer au chercheur un pool interchangeable pourrait enfreindre le besoin. L'affectation personnelle exige toujours le droit d'accès approprié à la ressource publiée. Consignez les mesures de charge, les vérifications de licences, les hypothèses de densité par hôte et le besoin de persistance du chercheur. Un ensemble d'éléments probants adapté comprend le modèle d'affectation et le calcul de capacité, plutôt que le seul nombre de machines virtuelles.

</details>

## 2. Un étudiant possède le rôle Azure Contributor et voit les machines virtuelles dans le portail, mais son flux AVD est vide. Que faut-il examiner ?

<details>
<summary>Réponse</summary>

Examinez l'identité de l'étudiant et son affectation au groupe d'applications, l'association du groupe au pool d'hôtes prévu et son inscription dans l'espace de travail. Un accès de gestion aux ressources de machines virtuelles ne publie pas de bureau pour cet utilisateur. Vérifiez également que le client s'abonne au bon espace de travail avec le compte attendu. Consignez l'appartenance aux groupes, les droits effectifs d'accès aux ressources et les diagnostics du flux avec leurs horodatages. Ouvrir un port entrant sur une machine virtuelle ou attribuer le rôle Owner de l'abonnement n'expliquerait ni ne corrigerait la relation de publication manquante.

</details>

## 3. Le projet souhaite des hôtes joints à Entra, mais une ancienne application exige des services de domaine. Entra ID remplace-t-il automatiquement AD DS ?

<details>
<summary>Réponse</summary>

Non. Séparez les exigences précises de l'application en matière d'authentification et d'annuaire de l'authentification au flux AVD. Microsoft Entra ID, AD DS et Microsoft Entra Domain Services offrent des capacités différentes, et le choix d'une jonction pour les hôtes ne supprime pas les dépendances de l'application. Vérifiez les combinaisons d'identités prises en charge, l'authentification du stockage des profils, la gestion des stratégies et les exigences de SSO avant de choisir une conception. Les éléments probants doivent inclure un inventaire des dépendances applicatives et un flux d'authentification pris en charge. Une stratégie d'accès conditionnel ne peut pas à elle seule fournir un protocole de domaine manquant ou l'accessibilité d'un contrôleur de domaine.

</details>

## 4. Une équipe pare-feu propose d'exposer TCP 3389 au public pour réparer toutes les connexions AVD. La connexion inversée exige-t-elle ce changement ?

<details>
<summary>Réponse</summary>

Non. La connexion inversée AVD de base repose sur une connectivité sortante du client et de l'hôte de session vers le service via HTTPS/TCP. Examinez les destinations requises, le DNS, TLS, le comportement du proxy, l'état de l'agent et l'étape de connexion en échec. Shortpath est un choix distinct de transport UDP, avec des prérequis propres à chaque option, et non une raison d'exposer RDP au public. Pour une conception avec écouteur sur réseau managé, documentez l'accessibilité privée et le port d'écoute UDP choisi. Les éléments probants doivent identifier la dépendance réellement bloquée et proposer une correction précisément délimitée.

</details>

## 5. Les clients du campus utilisent UDP, mais ceux du domicile se replient sur TCP. Cela prouve-t-il que l'hôte de session est en panne ?

<details>
<summary>Réponse</summary>

Non. Comparez les clients, les réseaux et les options Shortpath sélectionnées. Un VPN du campus peut offrir une accessibilité privée directe, tandis qu'un NAT ou un pare-feu domestique empêche un chemin UDP particulier. Vérifiez les versions de client prises en charge, la stratégie UDP, l'accessibilité STUN/TURN, la disponibilité dans le cloud et le transport négocié. Le repli sur la connexion inversée peut préserver la session tout en modifiant ses performances. Consignez les horodatages, le délai aller-retour, la perte de paquets et les observations des chemins réussis comme des chemins échoués. Ne supposez pas que l'écouteur managé UDP 3390 est requis pour chaque connexion Shortpath sur réseau public.

</details>

## 6. Les étudiants s'authentifient correctement, mais obtiennent des profils temporaires après un changement d'identité SMB. Reconstruire toutes les machines virtuelles corrigerait-il la cause ?

<details>
<summary>Réponse</summary>

Examinez d'abord les journaux de rattachement FSLogix et le chemin d'authentification du stockage. Vérifiez l'emplacement attendu du conteneur, la résolution DNS, les autorisations au niveau du partage, les autorisations NTFS, la configuration Kerberos prise en charge et la compatibilité du chiffrement. L'authentification au flux et l'accès aux fichiers du profil sont des étapes distinctes. Reconstruire les hôtes sans corriger une dépendance de stockage partagée pourrait reproduire le même échec partout. Préservez les conteneurs concernés et examinez les sessions ou verrous existants avant les actions de reprise. Les éléments probants doivent montrer l'erreur exacte de rattachement et une opération de profil autorisée avec l'identité utilisateur prévue.

</details>

## 7. Le même étudiant ouvre deux sessions indépendantes et la seconde ne peut pas rattacher le conteneur de profil. Un opérateur doit-il supprimer immédiatement le verrou ?

<details>
<summary>Réponse</summary>

Ne considérez pas le verrou comme un élément que l'on peut supprimer sans examen. La configuration standard des profils FSLogix prend en charge une seule connexion à un conteneur ; les configurations simultanées imposent des exigences supplémentaires et des limites applicatives. Identifiez les sessions actives et déconnectées, l'hôte propriétaire et l'état réel du verrou avant de décider si une ressource obsolète nécessite une récupération. Coordonnez une fermeture de session contrôlée et protégez le travail non enregistré. Consignez les horodatages et les journaux de rattachement. Une conception exigeant des sessions simultanées nécessite une configuration explicitement prise en charge et une validation, plutôt que des écritures simultanées sans restriction dans le même conteneur.

</details>

## 8. L'éditeur de notes apparaît dans un groupe RemoteApp, mais échoue sur la moitié des hôtes. Publier l'icône installe-t-il l'application ?

<details>
<summary>Réponse</summary>

Publier une RemoteApp contrôle l'accès et la présentation ; cela ne prouve pas que chaque hôte de session éligible peut exécuter l'application. Comparez les versions d'image, les dépendances installées et la méthode de distribution choisie. Pour App Attach, examinez la compatibilité du package, l'accès au stockage, les affectations au pool d'hôtes et aux utilisateurs, ainsi que les preuves d'inscription. Testez le même utilisateur sur un hôte dont le bon fonctionnement est connu et sur un hôte affecté, sans modifier les affectations de production. Le livrable doit expliquer la différence et proposer une correction progressive du package ou de l'image avec une solution de repli fonctionnelle.

</details>

## 9. Quarante-huit étudiants arrivent en même temps. Les hôtes prennent en charge douze sessions chacun et il faut tolérer la panne d'un hôte. Quatre hôtes avec Start VM on Connect suffisent-ils ?

<details>
<summary>Réponse</summary>

Quatre hôtes sains fournissent exactement 48 sessions selon l'hypothèse mesurée, sans marge pour la panne d'un hôte. Cinq hôtes disponibles fournissent encore 48 sessions après la perte de l'un d'eux. Start VM on Connect ne garantit pas que les hôtes de réserve sont sains et prêts avant l'arrivée simultanée d'une classe. Modélisez le temps de démarrage, le nombre maximal de sessions, la répartition de charge, les calendriers de mise à l'échelle, les exclusions de drainage et la capacité du stockage des profils. Les éléments probants sont un tableau de capacité en fonctionnement normal et dégradé, ainsi que des prévisions de délais de démarrage. Validez l'hypothèse de densité avec des charges représentatives avant de l'utiliser en exploitation.

</details>

## 10. Une région de remplacement dispose de machines virtuelles, mais les étudiants ne peuvent pas retrouver leur environnement de travail. Que manque-t-il à l'affirmation de reprise ?

<details>
<summary>Réponse</summary>

Un inventaire de machines virtuelles ne suffit pas à établir la reprise des bureaux. Suivez la disponibilité de l'identité et du DNS, la publication des ressources, la distribution des applications, les chemins réseau, l'accès au stockage des profils et sa cohérence, ainsi que l'API de notes. Précisez séparément les objectifs de reprise des profils et des données applicatives. Utilisez un identifiant de corrélation de connexion, les diagnostics, les événements de l'hôte et les journaux FSLogix pour localiser la première étape en échec. L'exercice sur table doit attribuer des opérateurs, préciser les hypothèses de capacité et les étapes de retour à la région principale, et retenir un parcours étudiant réussi comme preuve d'acceptation. Présentez ces éléments comme des vérifications planifiées tant qu'un exercice de reprise autorisé n'a pas produit d'observations réelles.

</details>

Les références techniques, les dates des objectifs et les limites du périmètre figurent dans le [guide](AZ-140.md). Transformez le raisonnement en schémas et en éléments probants grâce au [cahier d'exercices](AZ-140-workbook.md).
