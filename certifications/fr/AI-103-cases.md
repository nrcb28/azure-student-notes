# AI-103 · 10 cas de développement avec réponses argumentées

[Guide](AI-103.md) · [Cahier d’exercices](AI-103-workbook.md) · [Sommaire](README.md)

Scénarios originaux d’application universitaire de notes, sans questions d’examen. Toutes les sorties et durées proposées sont hypothétiques. Expliquez la décision d’implémentation et les preuves nécessaires avant d’ouvrir chaque réponse. Vérification des références : **1 novembre 2026**.

## 1. Un exemple Python s’importe correctement, mais sa réponse ne possède pas la propriété attendue. L’équipe doit-elle changer le déploiement jusqu’à ce que cela fonctionne ?

<details>
<summary>Réponse</summary>

Examinez d’abord la version du SDK installé, la génération d’API, l’opération, le point de terminaison et la structure de réponse documentée. Une importation réussie prouve peu de choses sur la compatibilité avec un exemple copié. Figez un ensemble cohérent de dépendances et convertissez un exemple de réponse expurgé dans le contrat propre à l’application. Distinguez une propriété manquante d’un échec d’authentification ou d’un déploiement inconnu. Changer de modèle ne répare pas un client qui lit le mauvais objet. Consignez l’URL de documentation et les versions de packages, puis ne vérifiez un appel réel que dans un laboratoire autorisé séparément.

</details>

## 2. Un modèle plus grand améliore les résumés, mais double la latence hypothétique pendant la semaine de révision. Quel modèle faut-il livrer ?

<details>
<summary>Réponse</summary>

Utilisez le même jeu d’évaluation représentatif et les mêmes hypothèses de charge pour les deux candidats. Mesurez l’appui sur les sources, l’exactitude des citations, l’abstention, la sortie structurée, la distribution de latence, le débit et l’utilisation des ressources. Déterminez les exigences obligatoires avant de comparer des moyennes. Un modèle plus petit pourrait traiter les questions courantes tandis qu’une escalade limitée prend en charge les plus difficiles, mais ce routage doit également être évalué. Incluez le temps de recherche documentaire et les nouvelles tentatives dans le budget. Ni la taille du modèle ni un résumé séduisant ne permettent d’établir le meilleur déploiement ; consignez un compromis justifié entre qualité, capacité, latence et coût, sans inventer de prix.

</details>

## 3. Un étudiant perd l’accès à un carnet partagé, mais des fragments en cache répondent encore à sa question. Le filtre de l’index suffit-il ?

<details>
<summary>Réponse</summary>

L’ensemble du chemin de recherche documentaire doit appliquer les droits actuels avant que le contexte n’atteigne le modèle. Examinez la propagation des autorisations aux fragments enfants, les mises à jour d’index, la mémoire de conversation et les caches. Les clés de cache doivent inclure un contexte approprié d’identité et d’autorisation, et la révocation exige une invalidation ou un autre contrôle de fraîcheur. Une requête d’index correcte ne peut pas protéger une réponse servie depuis un ancien cache sans restriction. Écrivez une politique de fraîcheur acceptable des autorisations et refusez l’accès par défaut lorsqu’elle ne peut pas être respectée. Démontrez le refus avec deux identités synthétiques et une trace avant et après révocation.

</details>

## 4. Une réponse cite le bon PDF de cours, mais attribue une échéance à un paragraphe qui ne fait que définir un algorithme. La présence d’une citation satisfait-elle l’évaluation ?

<details>
<summary>Réponse</summary>

Non. Vérifiez que le passage cité et sa version appuient effectivement l’affirmation. L’existence de la source, sa pertinence et l’appui sur l’affirmation sont des vérifications distinctes. Examinez si la recherche a omis la page du devoir, si le découpage a perdu le contexte ou si la génération a inventé une date malgré des preuves suffisantes. L’application doit s’abstenir lorsque ses passages autorisés ne contiennent pas l’échéance. Conservez l’exemple en échec dans l’évaluation de régression et notez l’exactitude des citations indépendamment de la lisibilité. Un lien de source qui s’ouvre correctement aide à la navigation, mais ne peut pas établir que la réponse est fondée sur cette source.

</details>

## 5. Un agent dépasse son délai après avoir demandé un outil de partage ; le backend a déjà créé le partage. Le client doit-il réessayer immédiatement ?

<details>
<summary>Réponse</summary>

Considérez le résultat comme inconnu jusqu’à sa réconciliation. Attribuez à l’opération applicative approuvée une clé d’idempotence stable et consignez son état indépendamment de la réponse du modèle. Interrogez ou récupérez cet état avant de renvoyer la demande ; les nouvelles tentatives ne doivent pas créer un autre partage. Liez l’approbation aux documents, destinataires et versions exacts, puis revérifiez l’autorisation à l’exécution. Distinguez le délai d’un outil du budget global de l’agent. Capturez des identifiants de corrélation expurgés afin que la trace relie requête, approbation, achèvement du backend et réponse perdue sans exposer de contenu étudiant.

</details>

## 6. Un agent planificateur délègue à un agent de recherche documentaire qui peut lire tous les cours. Le prompt restreint du planificateur préserve-t-il les autorisations de l’étudiant ?

<details>
<summary>Réponse</summary>

Le transfert doit porter un contexte d’appelant fiable et l’outil de recherche documentaire doit faire respecter les autorisations de cet appelant. Un prompt de planification ne peut pas contraindre de façon fiable un service privilégié en aval. Définissez le rôle de chaque agent, le périmètre de ses outils, les champs de transfert autorisés, la propriété de la mémoire et le budget d’arrêt. Ne renvoyez au planificateur que des preuves autorisées et empêchez la conversation d’un étudiant de réutiliser la mémoire d’un autre. Testez une demande de cours refusée et un transfert contenant une injection. La délégation peut répartir les responsabilités, mais elle ne doit jamais élargir silencieusement l’accès de l’utilisateur final.

</details>

## 7. L’application doit décrire un graphique et créer une affiche de révision. Les deux demandes peuvent-elles utiliser le même contrat visuel ?

<details>
<summary>Réponse</summary>

Définissez des contrats distincts pour la compréhension de preuves existantes et la création de nouveaux médias, même si une plateforme prend en charge les deux. La réponse sur le graphique doit s’appuyer sur les étiquettes, unités et relations visibles, avec abstention pour les régions illisibles. L’affiche exige des contrôles de génération, des droits appropriés sur les sources, des vérifications de sécurité et une révision du texte et des schémas générés. Les variantes vidéo exigent également une sémantique de segment ou de modification. Vérifiez l’utilité du texte alternatif et évitez de déduire des détails invisibles. Une illustration générée convaincante ne peut pas valider une affirmation sur le graphique original du cours.

</details>

## 8. La reconnaissance vocale transforme « mutex » en « music », puis la traduction produit un non-sens fluide. Faut-il modifier uniquement le prompt de traduction ?

<details>
<summary>Réponse</summary>

Examinez les étapes au regard de leurs contrats respectifs. Une erreur de reconnaissance en amont peut devenir un texte traduit fluide mais incorrect, puis une mauvaise réponse. Construisez des exemples avec vocabulaire technique, bruit, négation et interruptions ; conservez une voie de correction textuelle et vérifiez la personnalisation de domaine prise en charge par le service choisi. Si une conception directement multimodale n’expose pas de transcription, évaluez la même préservation du sens de bout en bout. Consignez les échecs propres à chaque langue au lieu de les masquer dans une moyenne. Une modification de prompt ne se justifie qu’après avoir identifié l’étape et mesuré son effet.

</details>

## 9. Content Understanding renvoie avec une confiance élevée une échéance de brouillon dans `final_due_date`. La proposition d’ajout au calendrier peut-elle se poursuivre ?

<details>
<summary>Réponse</summary>

La valeur enfreint la sémantique prévue du champ malgré sa confiance. Définissez clairement le champ de remise finale, examinez son ancrage dans le document et comparez-le à des exemples annotés de brouillon et de version finale. Validez le format, les valeurs manquantes et la cohérence avec les autres jalons. Orientez les ambiguïtés non résolues vers une révision ; la confiance est une estimation et non une décision de règle métier. Vérifiez que l’API et la configuration sélectionnées exposent les preuves nécessaires. Une action en aval sur le calendrier ou le partage exige aussi sa propre autorisation et son approbation, indépendamment de la qualité de l’extraction ou de la validité du JSON.

</details>

## 10. Une version change le prompt, le modèle d’embedding et le schéma de réponse d’un outil ; les échecs de citation augmentent. Rétablir le prompt suffit-il ?

<details>
<summary>Réponse</summary>

Utilisez le manifeste de version pour identifier tous les composants modifiés et leur compatibilité. Une nouvelle représentation d’embedding peut nécessiter une réindexation, tandis qu’un ancien client peut mal interpréter un nouveau résultat d’outil. Comparez les traces et les cas de régression pour localiser l’échec, puis restaurez un ensemble compatible reconnu comme fonctionnel ou appliquez la migration documentée. Définissez avant le déploiement progressif des déclencheurs de retour arrière pour l’appui sur les sources, l’accès, les erreurs d’outils et la latence. Conservez les identifiants de version dans une télémétrie expurgée. Revenir sur un seul prompt visible ne peut pas réparer de façon fiable les changements de représentations de recherche documentaire ou de contrats de réponse applicative.

</details>

Sources : [objectifs actuels](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SDK et points de terminaison](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview), [évaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), [accès aux documents](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [appel de fonctions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [conception d’analyseur](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices), [confiance et ancrage dans les sources](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement).
