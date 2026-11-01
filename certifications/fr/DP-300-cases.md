# DP-300 · 10 cas avec réponses argumentées

[Guide](DP-300.md) · [Cahier](DP-300-workbook.md) · [Sommaire](README.md)

Exercices originaux, pas de questions officielles. Avant de révéler une réponse, identifier la contrainte, proposer une décision et décrire les preuves à recueillir. Ces cas ne revendiquent ni exécution Azure ni couverture complète de l’examen.

## 1. L’application exige une extension au niveau du système. Peut-on choisir SQL Database parce qu’il exécute du T-SQL ?

<details>
<summary>Raisonnement</summary>

Non. Le besoin système modifie la frontière d’hébergement. Vérifier si l’extension est indispensable et si une solution managée compatible peut la remplacer. Si le contrôle direct du système reste nécessaire, examiner SQL Server sur VM en incluant correctifs, sauvegardes, surveillance et disponibilité. L’évaluation doit couvrir les dépendances extérieures aux objets de la base, pas seulement T-SQL. Vérifier l’exigence applicative réelle avant le choix ; connaître une syntaxe SQL ne démontre pas la compatibilité du déploiement.

</details>

## 2. La migration des données se termine avec succès. Peut-on immédiatement rouvrir les écritures ?

<details>
<summary>Raisonnement</summary>

Un transfert terminé n’est qu’une étape. Valider état final prévu, totaux métier importants, permissions, chemins applicatifs et tâches planifiées. Établir quand les écritures sources se sont arrêtées et si les derniers changements ont été appliqués. Désigner la destination comme source faisant autorité avant de rouvrir. Le retour arrière doit traiter les écritures de destination après bascule ; revenir simplement à la source peut les perdre. Utiliser une liste explicite d’acceptation ou de refus et distinguer vérifications observées et supposées.

</details>

## 3. L’application résout l’adresse SQL privée et se connecte, mais SELECT est refusé. Faut-il ouvrir davantage le réseau ?

<details>
<summary>Raisonnement</summary>

La connexion réussie et le refus de l’instruction pointent vers l’autorisation dans la base plutôt qu’une panne réseau générale. Confirmer principal authentifié, base, objet et opération. Vérifier les permissions applicables et accorder le minimum nécessaire selon le modèle choisi. Un rôle Azure Contributor ne donne pas automatiquement accès aux tables. Ouvrir le point public changerait l’exposition sans apporter la permission manquante. Refaire la même opération applicative avec la même identité pour vérifier le diagnostic.

</details>

## 4. Les administrateurs de base ne doivent pas voir certaines valeurs en clair. TDE seul suffit-il ?

<details>
<summary>Raisonnement</summary>

TDE protège les fichiers au repos ; il n’empêche pas à lui seul une requête autorisée de renvoyer des valeurs en clair. Examiner une conception telle qu’Always Encrypted avec clients compatibles et clés hors de la frontière d’accès de l’administrateur. Vérifier opérations de requête, compatibilité applicative, récupération des clés et responsabilités. Le masquage dynamique ne constitue pas une frontière équivalente de confidentialité. Valider le modèle de menace par un test autorisé sur données synthétiques au lieu de confondre toutes les fonctions contenant le mot chiffrement.

</details>

## 5. Une requête ralentit après une version alors que le CPU global reste normal. Quelles preuves chercher d’abord ?

<details>
<summary>Raisonnement</summary>

Identifier la requête et comparer plans et exécutions sur des périodes comparables avec l’historique Query Store disponible. Examiner paramètres applicatifs, lectures, attentes, blocages et changements de schéma ou de statistiques. Un CPU agrégé normal ne prouve pas la santé d’une transaction particulière. Formuler une hypothèse avant de changer la taille du service. Si on teste un ancien plan, définir succès et retour arrière puis suivre un trafic représentatif ; une seule exécution rapide prouve peu une amélioration durable.

</details>

## 6. Un index accélère les lectures mais ralentit fortement les imports. Est-ce nécessairement un succès ?

<details>
<summary>Raisonnement</summary>

Non. Un index doit être maintenu lors des modifications, donc son avantage doit être évalué sur toute la charge. Comparer latence de lecture et d’écriture, débit, stockage et plans avant et après dans des conditions représentatives. Vérifier les doublons avec les index existants et si une définition plus étroite ou ordonnée autrement répondrait au besoin. Fixer un seuil d’acceptation pour les imports comme pour les recherches. Ne pas garder la modification uniquement parce que la requête de démonstration est plus rapide.

</details>

## 7. Une longue transaction bloque de petites recherches. Faut-il tuer toutes les sessions bloquées ?

<details>
<summary>Raisonnement</summary>

Trouver la chaîne de blocage et la transaction qui détient les verrous pertinents avant d’interrompre quoi que ce soit. La session bloquée est souvent un symptôme. Identifier travail, ancienneté, responsable et conséquences de l’annulation. Tuer une transaction peut imposer un retour arrière long et affecter la correction applicative. Dans une investigation contrôlée, envisager transactions plus courtes ou isolation adaptée après compréhension de la cohérence exigée. Consigner preuves et décision d’incident plutôt qu’exécuter un script de terminaison indiscriminé.

</details>

## 8. Un travail SQL Agent doit migrer vers Azure SQL Database. Peut-on simplement recopier son calendrier ?

<details>
<summary>Raisonnement</summary>

SQL Agent n’est pas disponible dans Azure SQL Database. Classer la tâche : du T-SQL compatible entre bases peut convenir à Elastic Jobs, tandis qu’un flux avec services externes peut demander une orchestration. Évaluer dépendances, identité, découverte des cibles, reprises et notifications, pas seulement l’heure d’exécution. Une répétition ne doit pas dupliquer le résultat métier après une réponse incertaine. Tester le remplacement sur données synthétiques isolées et comparer à la fois les traces d’exécution et l’état métier obtenu.

</details>

## 9. Un DELETE accidentel atteint la base secondaire. La réplication a-t-elle échoué ?

<details>
<summary>Raisonnement</summary>

La réplication peut faire exactement son travail : transmettre une modification valide et validée vers une autre copie. Disponibilité et récupération historique répondent à des problèmes différents. Déterminer heure d’incident et points conservés, puis prévoir une restauration isolée antérieure à la modification. Valider enregistrements manquants et ajouts légitimes ultérieurs avant de décider la remise en service. Remplacer tout par un ancien état n’est pas forcément acceptable ; la décision doit tenir compte des écritures valides effectuées entre-temps.

</details>

## 10. La base a basculé, mais l’application échoue encore. Le RTO est-il respecté ?

<details>
<summary>Raisonnement</summary>

Non si l’objectif porte sur le service visible par l’utilisateur. Vérifier point de connexion compatible, DNS client, reconnexion, identités, dépendances et opérations planifiées sur le principal actuel. Effectuer une vérification fonctionnelle synthétique et mesurer le délai depuis l’événement de départ défini. Noter séparément la perte de données par rapport au RPO. Avant le retour, établir copie faisant autorité et synchronisation. Un statut de base sain ne démontre pas la récupération de l’application ni le respect de ses objectifs.

</details>

## Autoévaluation et sources

Pour chaque cas : identifier l’exigence, justifier une décision et nommer une vérification. Cette méthode de révision indépendante ne fournit ni note officielle ni prédiction de réussite.

[Guide officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Références techniques et explications](DP-300.md)
