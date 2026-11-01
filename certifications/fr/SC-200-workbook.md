# SC-200 · Cahier de décisions et de preuves

[Guide](SC-200.md) · [Dix cas](SC-200-cases.md) · [Sommaire](README.md)

Cinq unités originales pour une application universitaire fictive de notes. Travaillez hors ligne avec des enregistrements et des identifiants inventés. Distinguez les résultats attendus des observations fournies dans l’exercice. Aucun accès à un locataire, déploiement cloud, requête réelle, envoi de message ou confinement n’est requis ni revendiqué.

<a id="sc-200-unit-1"></a>

## 1. Cartographier les limites de collecte et d’accès

Dessinez Microsoft 365, une application Azure, un serveur local et un pare-feu de campus. Attribuez, selon le cas, l’investigation à Defender XDR ou la collecte et l’analyse à Sentinel. Pour chaque source, précisez l’intégration, les prérequis du connecteur, la table et la colonne temporelle attendues, les identifiants stables, le délai, la rétention et un responsable. Distinguez les autorisations de lecture, de gestion des incidents, de création de règles et d’automatisation.

**Scénario :** le connecteur du pare-feu semble connecté, mais l’événement requis est absent. **Preuves :** un tableau de couverture des quatre sources, une question sur le bon fonctionnement de la collecte et un événement synthétique avec le schéma attendu. **Livrable :** un diagramme et une liste des lacunes expliquant ce que l’analyste peut conclure. Incluez des règles de traitement des données personnelles et des exports ; ne collectez aucune information réelle sur les étudiants.

<a id="sc-200-unit-2"></a>

## 2. Construire une chronologie d’incident étayée

Inventez six enregistrements couvrant un courriel, l’identité, un point de terminaison, l’application et une charge de travail cloud. Donnez à chacun une heure d’événement UTC, une heure d’ingestion, un ID source, des identifiants d’entité et une observation. Regroupez les alertes liées dans un incident proposé sans supposer qu’une IP partagée sur le campus prouve la relation. Distinguez le périmètre connu, le périmètre suspecté et la télémétrie indisponible.

**Scénario :** un message suspect précède un apparent accès à un document privé. **Preuves :** la chronologie, la carte des entités, une explication concurrente et un enregistrement manquant demandé. **Livrable :** une note de triage précisant le responsable, la justification de la priorité, le confinement proposé, l’autorisation requise, l’impact sur le service et une condition de rétablissement. Marquez chaque action proposée comme non exécutée ; une confirmation attendue n’est pas une réponse observée.

<a id="sc-200-unit-3"></a>

## 3. Expliquer les résultats d’une requête avant de se fier aux décomptes

Lisez le jeu de données KQL synthétique et fixe du guide. Suivez les lignes à travers la fenêtre UTC semi-ouverte, le filtre Denied, la déduplication et l’agrégation. Expliquez pourquoi la réponse attendue est de deux événements pour `student-a`. Ajoutez une seconde table inventée avec deux lignes pour ce compte et dessinez les paires produites par une jointure interne explicite. Comparez cela à la déduplication du côté gauche par le type par défaut `innerunique`.

**Scénario :** un rapport confond des lignes jointes avec des attaques distinctes. **Preuves :** les décomptes intermédiaires, les clés de jointure, les hypothèses sur les identifiants et un exemple à la borne temporelle. **Livrable :** une interprétation corrigée avec la sortie attendue et les limites. Aucune exécution de requête n’est revendiquée ; les éventuels calculs locaux restent distincts des observations dans un locataire.

<a id="sc-200-unit-4"></a>

## 4. Transformer une hypothèse de chasse en revue d’ajustement

Rédigez une hypothèse reliant la réception d’un message suspect à un accès inhabituel à des fichiers privés. Définissez la population, la fenêtre UTC, les sources requises et une explication alternative. Créez quatre exemples synthétiques étiquetés comme bénins et quatre comme préoccupants. Proposez une détection et une exception étroite, puis identifiez les exemples qui déclencheraient une alerte, seraient manqués ou exigeraient plus de contexte. Expliquez comment ASIM pourrait normaliser les sources compatibles et où les mappages des parseurs doivent être validés.

**Scénario :** un import autorisé ressemble à un usage abusif. **Preuves :** un tableau de décision versionné, les lacunes des sources, l’analyse des faux positifs et faux négatifs, et une vérification de mappage de parseur. **Livrable :** une recommandation d’ajustement. Une chasse vide et moins d’alertes ne prouvent ni l’absence de compromission ni une couverture complète.

<a id="sc-200-unit-5"></a>

## 5. Examiner un workflow de réponse assistée

Schématisez une règle d’automatisation qui appelle un playbook d’enrichissement et demande une approbation avant un confinement perturbateur. Identifiez séparément l’opérateur, l’autorisation d’appel de Sentinel, l’identité du workflow et le périmètre en aval. Simulez un déclenchement en double et un dépassement de délai ; documentez les identifiants et les vérifications d’état qui empêchent les tickets en double ou les restrictions répétées inutilement. Incluez un responsable et des conditions de rétablissement.

**Scénario :** un résumé d’IA relie une alerte cloud au téléchargement d’un étudiant sans journal applicatif. **Preuves :** un tableau reliant chaque affirmation à sa source, la conclusion corrigée, la limite d’approbation et le comportement attendu lors d’une nouvelle tentative. **Livrable :** une procédure sur table revue. Vérifiez les suggestions de Copilot à partir des enregistrements fournis et de la sémantique des requêtes. Aucune notification, demande d’approbation ou réponse réelle n’est envoyée.

[Guide d’étude officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Fondements de l’observabilité](../../fr/08-observability.md)
