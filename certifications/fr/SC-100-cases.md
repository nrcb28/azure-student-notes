# SC-100 · Dix cas d’architecture

[Guide](SC-100.md) · [Cahier d’exercices](SC-100-workbook.md) · [Sommaire](README.md) · [Español](../es/SC-100-cases.md)

Questions hypothétiques originales pour l’application universitaire de notes. Expliquez l’exigence métier, la frontière du contrôle, le responsable et les preuves d’acceptation avant d’ouvrir une réponse. Ce sont des exercices de conception hors connexion, sans questions d’examen officielles ni affirmation de contrôles exécutés.

## 1. Un doyen veut le score de sécurité le plus élevé avant de protéger les réponses non publiées. Comment fixer les priorités ?

<details>
<summary>Réponse</summary>

Commencez par l’impact de la divulgation des réponses et les chemins qui pourraient les exposer. Identifiez le propriétaire des données, les accès actuels, les identités privilégiées, les voies de partage et les preuves disponibles. Un score peut mettre en évidence des lacunes de posture, mais ne peut pas attribuer les priorités métier de l’université. Proposez des contrôles qui réduisent l’exposition critique, puis définissez l’acceptation par des tests d’accès limités au périmètre et des preuves de configuration examinables. Consignez les coûts, les risques résiduels et la décision de risque autorisée du doyen. Améliorer d’abord une recommandation sans rapport et à faible impact exigerait une raison défendable, pas simplement une hausse de score plus facile.

</details>

## 2. L’API utilise un point de terminaison privé. L’architecture peut-elle déclarer Zero Trust achevé ?

<details>
<summary>Réponse</summary>

La connectivité privée limite un chemin réseau ; elle n’établit ni identité, ni autorisation applicative, ni isolation complète. Vérifiez si l’accès public reste activé, comment le campus et les environnements de récupération résolvent le DNS et quels appelants peuvent atteindre le point de terminaison. Définissez ensuite l’authentification utilisateur, les autorisations de charge de travail, les exigences d’appareil lorsqu’elles s’appliquent et les décisions d’accès par cours. Incluez les chemins d’administration et de sortie. L’acceptation doit comprendre les requêtes autorisées et refusées attendues ainsi que les preuves nécessaires pour distinguer une panne réseau d’un refus d’autorisation. L’architecture doit consigner les frontières restantes plutôt que de qualifier une fonctionnalité de stratégie complète.

</details>

## 3. L’indexeur et l’agent IA partagent un compte administrateur. Que faut-il changer dans la conception ?

<details>
<summary>Réponse</summary>

Donnez à chaque charge de travail une identité distincte, un responsable, un cycle de vie et une frontière d’autorisation. L’indexeur doit accéder aux documents publiés autorisés ; l’agent n’a besoin que de la recherche documentaire et des outils nécessaires à sa tâche. Évaluez les identités managées, la fédération et les contrôles d’identité d’agent pris en charge au regard de ces exigences. Supprimez la dépendance à un administrateur humain et définissez comment l’accès expirerait ou serait révoqué. Une authentification réussie ne doit pas impliquer un accès étendu aux données ou des droits de déploiement. Les preuves d’acceptation doivent montrer les opérations autorisées, les accès inter-cours refusés, l’attribution de l’activité et la récupération si l’une des identités devient indisponible.

</details>

## 4. Sentinel reçoit des alertes cloud, mais aucun événement de l’annuaire du campus. L’architecture SOC est-elle adéquate ?

<details>
<summary>Réponse</summary>

L’adéquation dépend des menaces prioritaires et de la couverture documentée. Si un annuaire de campus compromis peut affecter le service de notes, l’absence de télémétrie d’annuaire constitue une lacune importante de détection. Reliez cette menace aux signaux attendus, dépendances d’ingestion, rétention, détection, triage et autorité de confinement. Expliquez les contributions de Defender XDR et Sentinel sans supposer que l’un ou l’autre voit automatiquement chaque actif. Proposez une phase d’intégration ou une surveillance compensatoire avec un responsable et une échéance. L’acceptation exige des événements représentatifs exploitables et une simulation de réponse, pas simplement le statut activé d’un connecteur ou un tableau de bord rempli.

</details>

## 5. Une étiquette de confidentialité et des disques chiffrés sont proposés comme stratégie complète de données étudiantes. Que manque-t-il ?

<details>
<summary>Réponse</summary>

Clarifiez les emplacements de données, leur classification, les destinataires et les obligations. Vérifiez ce que l’étiquette configure réellement et quels clients et dépôts respectent ses protections. Le chiffrement des disques protège une frontière de stockage, mais n’empêche pas un service autorisé de lire ou d’exporter du texte en clair. Considérez les accès limités au périmètre, les restrictions de partage, la couverture DLP, l’audit, la rétention, la suppression et l’administration des clés. Attribuez des preuves et des responsables à chaque exigence, y compris aux voies non prises en charge. Les parties prenantes juridiques et de protection des données doivent évaluer les obligations ; ni une étiquette ni un score de conformité ne prouvent que l’établissement respecte chaque exigence juridique.

</details>

## 6. Un document importé par un enseignant demande à l’assistant IA d’envoyer tous les fichiers du cours par courriel. Quelle frontière compte ?

<details>
<summary>Réponse</summary>

Le document est un contenu récupéré non fiable et ne peut pas accorder d’autorité au modèle ou à ses outils. Gardez la recherche documentaire limitée aux documents autorisés de l’utilisateur, restreignez l’identité de l’agent et imposez l’autorisation des outils en dehors des instructions générées par le modèle. Un outil d’envoi exige une politique délibérée de destinataires et d’accès aux données, ainsi qu’une approbation des divulgations à conséquences lorsque la conception l’exige. Évaluez la détection d’attaques par prompt comme contrôle supplémentaire avec des hypothèses d’intégration et de langues prises en charge. Utilisez des documents synthétiques dans l’exercice sur table. L’acceptation doit démontrer qu’une instruction dans un document ne peut pas étendre les autorisations de recherche documentaire ou d’outils.

</details>

## 7. Des sauvegardes nocturnes restaurent des fichiers individuels, mais le service exige un RPO de quinze minutes. La conception peut-elle être approuvée ?

<details>
<summary>Réponse</summary>

Pas à partir de ces preuves. Des points de récupération nocturnes seuls ne satisfont pas une exigence de perte maximale de données de quinze minutes. Identifiez chaque source de données et le mécanisme de récupération proposé, y compris la cohérence entre documents et métadonnées. Évaluez aussi l’administration des sauvegardes résistante aux rançongiciels, la rétention et la récupération des clés. Le RTO applicatif de deux heures exige identité, DNS, configuration et accès au plan de contrôle, pas seulement récupération de fichiers. Le responsable doit financer et valider une conception qui respecte les objectifs ou approuver des exigences révisées avec un impact explicite. Consignez les mesures attendues ; cet exercice hors connexion ne prouve aucune performance de restauration.

</details>

## 8. L’équipe plateforme cloud applique une stratégie à Azure. Comment traiter une exception SaaS départementale ?

<details>
<summary>Réponse</summary>

Établissez d’abord si le périmètre de cette stratégie peut régir le service SaaS ; ne déduisez pas la couverture d’un résultat de conformité Azure. Reliez le service départemental aux exigences de contrôle de l’université et évaluez ses contrôles natifs, son intégration d’identité, sa gestion des données, ses preuves d’audit et ses responsabilités contractuelles. Utilisez le modèle de responsabilité des zones d’atterrissage pour clarifier la propriété de plateforme et de charge de travail sans prétendre que chaque service relève du même mécanisme d’application. Si une lacune subsiste, consignez contrôles compensatoires, responsable du risque, date de révision et expiration. La décision d’architecture doit montrer comment l’exception affecte le service dans son ensemble.

</details>

## 9. Un artefact de build signé provient d’un agent doté de larges autorisations en production. La chaîne d’approvisionnement est-elle protégée ?

<details>
<summary>Réponse</summary>

La signature soutient l’intégrité et la provenance des artefacts selon des hypothèses de confiance définies, mais elle ne peut pas rendre à elle seule un build autorisé compromis digne de confiance. Examinez l’approbation des sources, les contrôles de dépendances, l’isolation de l’agent de build, l’accès aux clés de signature, la promotion d’artefacts et les autorisations de déploiement. Séparez la confiance de test de celle de production et limitez, lorsque cela s’applique, les revendications de fédération et le périmètre des ressources. Définissez qui enquête sur une version suspecte et comment rétablir une version reconnue comme fonctionnelle. Les preuves d’acceptation doivent relier une révision source approuvée à l’artefact promu et au déploiement autorisé, tout en montrant qu’un pipeline non approuvé ne peut pas modifier la production ou la politique de signature.

</details>

## 10. Le financement ne couvre qu’un semestre. Comment un architecte peut-il justifier un programme de sécurité par phases ?

<details>
<summary>Réponse</summary>

Classez les travaux selon l’exposition critique pour l’activité, les dépendances, la capacité pratique de livraison et la réduction des risques attendue. Protéger la récupération et l’administration privilégiée peut permettre des améliorations ultérieures de migration et de réponse, mais justifiez cette séquence au regard des menaces de l’université. Comparez les options réalisables, les licences, la charge opérationnelle et les perturbations de l’enseignement. Pour chaque phase, attribuez un responsable, des critères d’acceptation limités au périmètre, des preuves, des conditions de retour arrière et une révision datée du risque résiduel. Documentez une autre solution et la raison de son rejet dans une ADR. Un achat financé est un jalon ; l’efficacité validée des contrôles et l’acceptation autorisée du risque déterminent l’aptitude opérationnelle.

</details>

[Guide d’étude officiel SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)
