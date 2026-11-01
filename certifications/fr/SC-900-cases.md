# SC-900 · 10 cas avec réponses argumentées

[Guide](SC-900.md) · [Cahier](SC-900-workbook.md) · [Sommaire](README.md)

Scénarios d’étude originaux, pas de questions officielles. Identifier l’exigence, écarter une alternative et préciser les preuves nécessaires. Tous les exemples sont hypothétiques ; aucun tenant n’a été modifié et aucun test cloud effectué.

## 1. L’application passe à un service managé. L’équipe peut-elle arrêter de revoir les permissions des documents ?

<details>
<summary>Raisonnement</summary>

Non. Le fournisseur exploite certaines parties de la plateforme, tandis que notre organisation détermine toujours les accès adaptés à ses données. Je cartographierais le modèle de service pour séparer l’exploitation de la plateforme des identités, du partage et de la configuration applicative. Une déclaration de conformité du fournisseur ne prouve pas que nos documents non publiés restent privés. Les preuves utiles comprendraient le périmètre de partage configuré et un test des opérations autorisées et refusées prévues, uniquement dans un environnement de test autorisé.

</details>

## 2. Un étudiant se connecte mais ne peut pas ouvrir le dossier privé d’un cours. L’authentification est-elle en panne ?

<details>
<summary>Raisonnement</summary>

Pas forcément. L’authentification peut réussir alors que l’autorisation refuse correctement une ressource précise. Vérifier l’identité réellement connectée, ses groupes, la permission exigée par le dossier et toute politique applicable. Lui donner un rôle administratif contournerait le diagnostic et dépasserait le besoin. Dans l’exercice de conception, noter la décision d’accès attendue et les observations qui distingueraient une erreur d’authentification d’un refus de permission sur la ressource ou dans l’application.

</details>

## 3. Une équipe propose un mot de passe suivi d’un autre comme MFA. Que manque-t-il ?

<details>
<summary>Raisonnement</summary>

Les deux secrets appartiennent à la catégorie de connaissance ; en utiliser deux ne crée pas des facteurs différents. Choisir une méthode et une politique compatibles avec les exigences de facteur ou de force d’authentification. Considérer aussi la résistance à l’hameçonnage, l’inscription, les appareils et la récupération. Une capture de la page d’inscription ne démontre pas l’application effective. Décrire une connexion attendue exigeant la méthode choisie et un cas négatif où une méthode insuffisante ne peut satisfaire l’exigence.

</details>

## 4. Le document téléchargé a l’empreinte attendue. Cela prouve-t-il son auteur et garantit-il son secret ?

<details>
<summary>Raisonnement</summary>

Non. Comparer une empreinte adaptée aide à vérifier la correspondance avec une référence attendue. Cela ne chiffre pas le fichier et ne démontre pas l’origine fiable de la référence. La confidentialité demande des accès adaptés et, si nécessaire, du chiffrement ; l’assurance d’origine demande un mécanisme de confiance approprié, comme une signature vérifiée. Expliquer d’abord d’où vient l’empreinte attendue. Si un attaquant remplace le fichier et sa référence, leur correspondance apporte une assurance bien plus faible que celle supposée.

</details>

## 5. Une politique d’accès conditionnel impose la MFA à l’application financière. Toutes les applications sont-elles couvertes ?

<details>
<summary>Raisonnement</summary>

Cette conclusion dépasse la portée de la politique. Examiner identités, applications, conditions, exclusions et contrôles d’octroi ciblés. La règle financière peut être correcte tandis que d’autres applications restent hors périmètre. Les permissions applicatives continuent de s’appliquer après la décision d’accès. Préparer une matrice des résultats attendus pour plusieurs utilisateurs et applications, avec récupération des administrateurs et dépendances, avant tout déploiement autorisé. L’analyse en rapport seul peut alimenter cette revue ; ses observations ne sont pas des blocages effectifs.

</details>

## 6. Un administrateur éligible à un rôle privilégié ne peut pas encore effectuer l’opération. PIM échoue-t-il ?

<details>
<summary>Raisonnement</summary>

L’éligibilité peut exiger une activation avant que les permissions deviennent utilisables. Vérifier rôle et portée prévus, conditions d’activation, durée, état d’approbation et attribution réellement active. Ne pas attribuer durablement un rôle plus large pour faire disparaître l’erreur. PIM change le moment où les privilèges sont disponibles ; il ne rend pas minimal un rôle inadapté. La preuve utile est une activation approuvée et une opération ciblée utilisant l’identité attendue, pas seulement l’existence d’une attribution éligible.

</details>

## 7. Un ancien membre du projet garde son accès. Faut-il une revue d’accès ou une détection ID Protection ?

<details>
<summary>Raisonnement</summary>

La question immédiate est de savoir si un droit existant reste justifié : elle relève d’une revue d’accès et du processus d’arrivée, de mobilité et de départ. ID Protection traite les signaux de risque d’identité et ne décide pas de tous les besoins métier d’un dossier. Enquêter séparément sur un comportement suspect si des indices existent. Identifier propriétaire, chemin d’attribution et conséquences d’un retrait sur d’autres projets. Noter la décision et les preuves nécessaires pour confirmer la suppression du droit devenu inutile.

</details>

## 8. Un courriel malveillant et une alerte sur un poste semblent liés, mais le poste ne transmet aucune télémétrie. Quelle lacune traiter ?

<details>
<summary>Raisonnement</summary>

La corrélation nécessite les données sources pertinentes. Vérifier produit compatible, licence, intégration, correspondance des identités et arrivée des événements dans la plateforme d’investigation. Defender XDR ne peut pas reconstituer toute la preuve manquante d’un poste parce qu’une autre alerte existe. Sentinel peut ajouter une analyse entre sources connectées, mais exige aussi ingestion et règles utiles. Documenter les événements présents, les absences et une hypothèse ciblée à tester avant d’affirmer que le tableau de bord représente l’ensemble de l’attaque.

</details>

## 9. Un document étiqueté Confidential peut encore être partagé à l’extérieur. Cela prouve-t-il un défaut du produit ?

<details>
<summary>Raisonnement</summary>

Le nom de l’étiquette ne démontre ni sa protection configurée ni la règle de manipulation appliquée à ce chemin de partage. Vérifier paramètres, charge compatible, publication, périmètre et conditions et actions DLP pertinentes. Une étiquette de classification seule peut être valide sans bloquer le partage. Définir les cas autorisés et bloqués attendus avant l’enquête. Utiliser du contenu synthétique dans un test autorisé ; ne pas diffuser de vraies données confidentielles pour démontrer le fonctionnement d’une politique.

</details>

## 10. Une enquête nécessite l’activité du mois dernier et des messages préservés. L’audit équivaut-il à la rétention ou à une sauvegarde ?

<details>
<summary>Raisonnement</summary>

Ces capacités ont des fonctions distinctes. L’audit apporte des preuves d’activité selon la disponibilité et la rétention configurées. La rétention du contenu définit sa conservation ou sa suppression ; eDiscovery aide à retrouver et préserver des éléments pour une enquête. Une sauvegarde répond à des besoins de récupération et n’est pas automatiquement fournie par ces outils. Déterminer sources, dates, permissions, exigences de rétention et de conservation légale, ainsi que le responsable. Ne pas promettre des événements jamais collectés ni un contenu hors délai de rétention.

</details>

[Guide officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · [Sources techniques et explications](SC-900.md)
