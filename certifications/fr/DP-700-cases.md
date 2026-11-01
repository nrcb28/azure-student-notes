# DP-700 · Dix cas avec réponses argumentées

[Guide](DP-700.md) · [Cahier d’exercices](DP-700-workbook.md) · [Sommaire](README.md) · [Español](../es/DP-700-cases.md)

Exercices originaux de données universitaires, sans questions d’examen officielles. Énoncez votre décision et vos preuves avant d’ouvrir chaque réponse. Le [guide](DP-700.md) consigne le périmètre officiel et la vérification des sources ; ces cas ne revendiquent ni couverture complète ni exécution de Fabric.

## 1. L’équipe connaît Synapse Spark. Peut-elle supposer des valeurs par défaut et un comportement de déploiement identiques dans Fabric ?

<details>
<summary>Réponse</summary>

Non. Les concepts Spark familiers sont utiles, mais Fabric est une plateforme SaaS avec ses propres frontières d’espace de travail, capacité, élément, runtime et cycle de vie. Inventoriez dépendances, bibliothèques, chemins de stockage, identités et configurations prises en charge avant d’adapter le notebook. Définissez une petite charge synthétique d’inscriptions et comparez sa sortie attendue à celle d’une future exécution Fabric contrôlée. Vérifiez les comportements de déploiement et de connexion séparément de la syntaxe de transformation. Un code similaire est un point de départ utile, mais ne prouve pas l’équivalence des autorisations, des valeurs par défaut du runtime ou des responsabilités opérationnelles.

</details>

## 2. Une équipe de reporting relationnel et une équipe de traitement de fichiers proposent le même stockage. Qu’est-ce qui détermine le choix ?

<details>
<summary>Réponse</summary>

Comparez la charge réelle : formats de fichiers, moteurs de transformation, besoins d’écriture relationnelle, consommation SQL, gouvernance et propriété. Un lakehouse est un candidat raisonnable pour la préparation de fichiers de téléchargement pilotée par Spark ; un entrepôt peut convenir à un modèle analytique centré sur T-SQL. Ils peuvent coopérer lorsque les exigences le justifient. Définissez la granularité des tables et la fraîcheur acceptable avant de comparer les performances. Ne considérez pas le point de terminaison analytique SQL du lakehouse comme une interface générale d’écriture d’entrepôt. Consignez les opérations prises en charge et un plan de validation représentatif plutôt que de choisir uniquement selon la familiarité de l’équipe.

</details>

## 3. Un raccourci expose le catalogue de la bibliothèque. Fournit-il une sauvegarde et un accès à chaque analyste ?

<details>
<summary>Réponse</summary>

Non. Le raccourci référence les données sources ; une cible manquante ou une autorisation source modifiée peut donc affecter l’accès. Ce n’est pas une copie de récupération conservée indépendamment. Examinez si le raccourci est interne ou externe, quelle identité ou connexion est utilisée et quelles autorisations s’appliquent au véritable chemin de lecture. Testez un analyste autorisé et un analyste refusé avec des données synthétiques. Convenez des changements de schéma et de la disponibilité avec le propriétaire du catalogue. Une conception distincte de conservation et de récupération est nécessaire si une restauration historique est requise.

</details>

## 4. Un rapport doit contenir uniquement les inscriptions d’hier. La copie est indiquée comme réussie, mais le rapport contient des inscriptions d’aujourd’hui. Le flux complet a-t-il réussi ?

<details>
<summary>Réponse</summary>

L’activité s’est terminée techniquement, mais la condition d’acceptation métier a échoué. Examinez les paramètres de fenêtre de traitement, les expressions dynamiques, les filtres sources, les fuseaux horaires et les liaisons de destination. Réconciliez les nombres de la fenêtre source et les clés métier sélectionnées avec la sortie publiée avant d’autoriser l’actualisation en aval. Un pipeline doit coordonner validation et publication, tandis qu’un notebook ou une transformation SQL peut implémenter les règles de données. Consignez l’identifiant d’exécution et l’intervalle prévu pour permettre de retracer l’erreur. Corrigez la sortie affectée par un rejeu idempotent plutôt que de supposer qu’un statut vert prouve l’exactitude.

</details>

## 5. Un lot a été validé durablement, mais sa réponse de réussite a été perdue. Comment une nouvelle tentative peut-elle éviter les inscriptions dupliquées ?

<details>
<summary>Réponse</summary>

Utilisez une clé d’inscription stable et une version source déterministe, dédupliquez le lot entrant et fusionnez-le dans l’état cible prévu. Ne persistez la progression qu’après validation de la sortie et engagement réussi. Une nouvelle tentative sur le même intervalle source borné doit trouver les versions équivalentes déjà appliquées et laisser les totaux métier inchangés. Consignez un identifiant de lot et les décomptes de réconciliation pour le diagnostic opérationnel. Ajouter chaque arrivée sans règle d’unicité dupliquerait les lignes. Considérez aussi les anciennes mises à jour retardées et les suppressions : une stratégie de nouvelle tentative doit préserver l’ordre des versions, pas seulement reconnaître des charges utiles identiques.

</details>

## 6. Une requête sur la date de modification manque les retraits et les corrections tardives. Que faut-il changer dans le chargement ?

<details>
<summary>Réponse</summary>

Déterminez si les retraits suppriment physiquement les lignes ou produisent un changement de statut. Une simple requête sur les lignes restantes ne peut pas découvrir des suppressions physiques. Évaluez une CDC prise en charge avec enregistrements de suppression, un contrat de suppression logique ou une réconciliation périodique. Pour les corrections tardives, utilisez un ordre source fiable et une fenêtre de chevauchement avec déduplication déterministe, ou un autre mécanisme pris en charge de suivi des changements. Gardez assez d’informations de version pour refuser les mises à jour obsolètes après une suppression. Testez horodatages égaux, enregistrements retardés et rejeu. Documentez la fenêtre de rétention source pour qu’une panne prolongée ne crée pas silencieusement un intervalle impossible à récupérer.

</details>

## 7. Un téléchargement a lieu à 23:59 et arrive à 00:07. Le compte de quel jour doit-il modifier ?

<details>
<summary>Réponse</summary>

La réponse suit la règle temporelle métier déclarée. Si les rapports comptent les téléchargements selon le temps d’événement, l’enregistrement appartient à la fenêtre du jour précédent. Définissez le fuseau horaire, la limite de fenêtre, le retard toléré et la possibilité de corriger un résultat publié. Un regroupement selon le temps de traitement le placerait le jour d’arrivée et répondrait à une autre question. Un watermark de streaming contrôle le traitement des retards et l’état conservé ; un point de contrôle soutient la progression de récupération. Aucun des deux ne remplace une politique explicite de correction ni ne prouve que la destination ne peut pas dupliquer la sortie après rejeu.

</details>

## 8. Une colonne facultative arrive avec des dates mal formées et des clés de module inconnues. L’évolution de schéma doit-elle accepter toutes les lignes ?

<details>
<summary>Réponse</summary>

Évaluez la colonne facultative comme un changement de compatibilité, séparément de la validité des enregistrements. Un champ additionnel approuvé ne rend pas acceptables les dates mal formées ou les références manquantes. Appliquez des règles explicites de type et de clé, conservez les entrées invalides dans une quarantaine contrôlée avec des codes de motif et réconciliez les enregistrements acceptés et rejetés. Un module inconnu peut exiger une résolution différée des références plutôt qu’un rejet permanent. Préservez les identifiants sources pour permettre réparation et rejeu sans danger. Vérifiez les contrats en aval avant de publier le nouveau schéma et évitez d’inscrire des détails étudiants dans des journaux de diagnostic sans restriction.

</details>

## 9. Un rapport applique une sécurité au niveau des lignes et possède une étiquette de confidentialité. L’accès direct aux fichiers est-il automatiquement sûr ?

<details>
<summary>Réponse</summary>

Non. Identifiez la frontière qui applique la restriction des lignes et examinez les chemins alternatifs tels que les requêtes SQL et l’accès direct OneLake. Les rôles d’espace de travail, les autorisations d’éléments, les règles propres au moteur et les autorisations de fichiers doivent correspondre aux capacités de lecture requises. Une étiquette de confidentialité fournit un contexte de gouvernance et les protections prises en charge ; sa seule présence ne prouve pas l’application de chaque exigence d’autorisation. Testez les agrégats de modules autorisés et le refus des détails étudiants avec des identités représentatives. Examinez aussi les autorisations d’export et les accès étendus hérités, qui peuvent compromettre une interface de rapport soigneusement restreinte.

</details>

## 10. Un notebook déployé est plus lent et lit la production depuis le test. Faut-il d’abord augmenter la capacité ?

<details>
<summary>Réponse</summary>

Corrigez d’abord la liaison d’environnement et empêchez toute publication involontaire. Examinez les références de connexion, les paramètres, l’identité d’exécution et la prise en charge du déploiement pour l’élément et ses dépendances. L’historique Git ou une promotion réussie ne prouvent pas que ces valeurs sont correctes. Comparez ensuite la même charge à une référence : concurrence de capacité, déséquilibre des étapes Spark, shuffle, tailles de fichiers, élimination de partitions et comportement de la source. Testez un changement appuyé sur des preuves avec des vérifications d’exactitude. Augmentez la capacité lorsque la pression mesurée le justifie, plutôt que d’utiliser le dimensionnement pour masquer une erreur de configuration ou une organisation inefficace des données.

</details>
