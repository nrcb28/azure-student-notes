# SC-300 · 10 cas avec réponses argumentées

[Guide](SC-300.md) · [Cahier d’exercices](SC-300-workbook.md) · [Sommaire](README.md)

Questions originales sur une application universitaire de notes fictive, pas des questions d’examen officielles. Expliquez la limite d’accès, écartez un raccourci inadapté et identifiez les éléments probants. Tous les résultats sont hypothétiques ; aucune modification d’un locataire réel ni exécution dans le cloud n’a été effectuée.

## 1. Un administrateur des utilisateurs d’un département ne peut pas lire un conteneur de notes privé. Faut-il élargir son rôle d’annuaire ?

<details>
<summary>Réponse</summary>

Commencez par identifier si l’action en échec concerne l’administration de l’annuaire, la gestion des ressources Azure, les données de stockage ou les permissions applicatives. Un rôle d’annuaire dont la portée est limitée par une unité administrative n’accorde pas tous les droits sur les ressources de ce département. L’élargir viserait la mauvaise limite. Pour cette conception, cartographiez l’identité connectée, l’opération demandée, la portée de la ressource et le rôle de données ou le droit applicatif applicable. Les éléments doivent expliquer pourquoi cette lecture précise est autorisée ou refusée sans transformer un administrateur de département en administrateur de tout le locataire.

</details>

## 2. Nous avons supprimé l’affectation directe d’un étudiant à l’application, mais son accès persiste. La suppression a-t-elle échoué ?

<details>
<summary>Réponse</summary>

Une suppression ne prouve pas que tous les octrois ont disparu. Examinez les affectations d’application par groupe, les sources d’appartenance aux groupes, les rôles applicatifs, les partages propres à l’application ainsi que l’identité et le locataire réellement utilisés. Selon la ressource, les affectations héritées et les sessions existantes peuvent aussi compter. Ne supprimez pas le compte comme première étape de diagnostic. Produisez un schéma des chemins d’octroi et distinguez l’état d’affectation de la décision observée dans l’application. Une explication utile identifie le chemin restant, son propriétaire et les éléments nécessaires pour confirmer la suppression à cette limite.

</details>

## 3. Une université partenaire signale une MFA réussie. Tous ses enseignants peuvent-ils désormais ouvrir des corrigés non publiés ?

<details>
<summary>Réponse</summary>

Non. Faire confiance à une revendication MFA prise en charge par les paramètres inter-locataires entrants peut aider à satisfaire une exigence d’authentification à portée définie ; cela n’accorde pas l’accès à toutes les ressources universitaires. Examinez les paramètres d’accès applicables des deux organisations, l’identité de l’enseignant dans le locataire de ressource, l’application cible et son droit d’accès. Les restrictions d’invitation et le cycle de vie de l’invité comptent également. Je consignerais un cours autorisé et un corrigé non publié refusé dans la matrice. Les éléments doivent distinguer la garantie d’authentification acceptée de la décision d’autorisation séparée concernant un document précis.

</details>

## 4. Les nouveaux éditeurs ne peuvent pas inscrire de clés d’accès. Le support doit-il recueillir leurs mots de passe dans une feuille de calcul ?

<details>
<summary>Réponse</summary>

Non. Concevez un processus approuvé d’amorçage et de récupération utilisant des méthodes prises en charge, éventuellement un Temporary Access Pass pour les utilisateurs éligibles. Vérifiez la portée de la stratégie des méthodes d’authentification, la prise en charge des appareils, la vérification d’identité, la durée de vie et les usages autorisés, ainsi que la remise sécurisée. Un TAP est sensible et temporaire ; il ne doit pas figurer dans le cahier ni devenir un moyen d’authentification permanent partagé. Le livrable décrit les résultats attendus d’inscription et d’expiration, ainsi que le responsable de la récupération. Une inscription réussie de clé d’accès nécessite encore une vérification séparée de l’application de la stratégie de force d’authentification voulue lors de l’accès.

</details>

## 5. Une stratégie d’accès conditionnel en mode rapport seul consigne des échecs. A-t-elle protégé l’application en bloquant ces requêtes ?

<details>
<summary>Réponse</summary>

L’évaluation en mode rapport seul n’applique pas les contrôles proposés. Ses résultats servent à planifier, mais ne prouvent pas que cette stratégie a bloqué une requête. Vérifiez les identités et ressources ciblées, les conditions, les exclusions, les autres stratégies applicables et les détails de stratégie de l’événement. Documentez le résultat attendu en mode appliqué séparément du résultat observé en mode rapport seul. Avant tout déploiement autorisé ailleurs, la conception devrait inclure un pilote, un accès de récupération, un responsable du retour arrière et des vérifications de licence. Ici, nous créons uniquement ce plan et une matrice des accès autorisés et refusés.

</details>

## 6. Une connexion inhabituelle apparaît, tandis qu’un ancien enseignant conserve un droit sur un cours. Une seule stratégie de risque suffit-elle ?

<details>
<summary>Réponse</summary>

Il s’agit de décisions différentes. Le risque de connexion concerne la demande d’authentification ; le risque utilisateur concerne une possible compromission de l’identité. Examinez les détections et le contexte avant de conclure qu’une connexion inhabituelle est malveillante. Le besoin de conserver l’accès au cours relève du propriétaire du droit d’accès et du processus de départ ou de révision d’accès. Une stratégie de risque ne peut pas décider de ce besoin métier. Conservez une chronologie d’investigation et une décision de droit d’accès séparée, avec leurs responsables et les éléments de correction attendus. Supprimer un accès obsolète ne résout pas en soi une identité potentiellement compromise.

</details>

## 7. Notre indexeur nocturne demande une permission déléguée. Peut-il lire les notes de tous les étudiants sans utilisateur ?

<details>
<summary>Réponse</summary>

Une permission déléguée dépend d’un contexte utilisateur connecté et du modèle de permissions de l’API concernée. Une charge de travail sans interface a besoin d’une identité applicative appropriée et de permissions d’application prises en charge, ou de permissions sur les ressources par une identité managée. Demander des permissions reste aussi distinct de l’octroi du consentement. Comparez l’objet d’application, le principal de service local, l’API, les consentements accordés et la portée des ressources. Ne substituez pas le mot de passe d’un enseignant. La conception hors ligne doit expliquer le corpus minimal de l’indexeur, la raison de cet accès, qui l’approuve et comment il est révisé.

</details>

## 8. Une identité de génération fédérée reçoit un jeton, mais le déploiement échoue. Faut-il créer un secret client permanent ?

<details>
<summary>Réponse</summary>

Commencez par distinguer validation de l’assertion externe, émission du jeton Entra et autorisation sur les ressources. Vérifiez l’émetteur, le sujet et l’audience configurés par rapport aux revendications attendues, y compris la casse, sans consigner de jetons réels. Examinez ensuite le rôle minimal et la portée de déploiement du principal obtenu. L’émission du jeton ne prouve pas l’autorisation de modifier la ressource cible. Un secret permanent introduirait une maintenance des moyens d’authentification sans expliquer l’échec. Remettez un tableau hypothétique des revendications et permissions contenant un contexte de génération prévu et un contexte refusé, ainsi que les éléments nécessaires à chaque limite.

</details>

## 9. L’authentification unique SAML fonctionne, mais un compte invité expiré reste dans la plateforme pédagogique. L’authentification unique est-elle le mécanisme de déprovisionnement ?

<details>
<summary>Réponse</summary>

La fédération d’authentification unique et le provisionnement des comptes ont des rôles différents. SAML peut prendre en charge l’authentification tandis qu’un connecteur SCIM crée, met à jour ou désactive séparément les comptes applicatifs. Examinez la portée des affectations, les mappages, les changements à la source, les journaux de provisionnement et le comportement de suppression pris en charge par l’application de destination. Ne déduisez pas la suppression d’un compte de la seule expiration d’un package d’accès ou d’une connexion réussie. Le relevé de gouvernance doit nommer le propriétaire de chaque étape et distinguer la suppression d’un droit Entra de l’état du compte en aval. Une action de provisionnement échouée exige un suivi et des éléments observables de son achèvement.

</details>

## 10. Un administrateur ayant fait l’objet d’une révision est éligible PIM et un tableau de bord n’affiche aucun échec. L’accès de maintenance est-il prouvé ?

<details>
<summary>Réponse</summary>

Une révision d’accès peut justifier le maintien de l’éligibilité, mais l’activation et une affectation active restent distinctes. Vérifiez le rôle exact, la portée, les exigences d’activation, l’approbation, la durée et les licences pertinentes. Un tableau de bord vide dépend aussi de la couverture des journaux, de l’ingestion, de la conservation, des filtres et des permissions ; il ne prouve ni une maintenance réussie ni l’absence d’échecs. Consignez une activation attendue et une opération autorisée à portée définie, ainsi qu’un refus hors de cette portée. Conservez la décision de révision, les éléments d’activation et l’analyse hypothétique des journaux comme des livrables distincts plutôt que de prétendre qu’une opération a été exécutée.

</details>

[Guide officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Sources techniques et explications](SC-300.md)
