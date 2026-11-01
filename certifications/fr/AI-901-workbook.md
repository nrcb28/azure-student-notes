# AI-901 · Cahier avancé commun

[Guide](AI-901.md) · [Dix cas](AI-901-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes dans les langues d’étude. Travaillez hors ligne avec des notes universitaires, invites, transcriptions et réponses candidates inventées. Étiquetez chaque sortie candidate comme **synthétique** et chaque résultat attendu comme une **prédiction**. Ne téléversez pas de véritables documents d’étudiants. Ce cahier ne déploie rien et n’établit pas une couverture complète de l’examen. Vérification des références : **1 novembre 2026** ; [objectifs applicables depuis le 15 avril 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).

<a id="ai-901-unit-1"></a>

## 1. Définir cinq contrats d’IA

Rédigez un contrat pour chacune des tâches suivantes : répondre à une question de cours, extraire l’échéance d’un devoir, analyser le texte d’un retour, accepter une question orale et décrire un schéma. Précisez la modalité d’entrée, les données autorisées, la forme de sortie, les erreurs inacceptables et une solution de repli. Comparez les réponses génératives, l’analyse de texte, la parole, la vision et Content Understanding selon leurs productions. Incluez une demande de génération d’image pour distinguer création et interprétation.

**Scénario :** un coéquipier propose un seul modèle d’image pour toutes les fonctions. **Éléments probants :** une matrice de décision de cinq lignes avec un choix de capacité justifié et une solution écartée pour chaque ligne. Ajoutez des questions de sélection du modèle sur les modalités, les options de déploiement, la langue et les paramètres pris en charge. Marquez les détails inconnus du service comme étant à vérifier dans la documentation actuelle plutôt que d’inventer des limites.

<a id="ai-901-unit-2"></a>

## 2. Rédiger des invites ancrées et des règles d’accès

Inventez trois passages courts : une note de cours autorisée, un carnet privé et une page autorisée contenant une instruction d’exportation de documents. Attribuez des identifiants de source stables et créez deux étudiants avec des listes d’accès différentes. Rédigez des invites système et utilisateur demandant une réponse étayée par les sources, préservant les délimitations de celles-ci et permettant l’abstention. La recherche doit filtrer selon l’accès de l’appelant avant de construire le contexte ; l’invite ne peut pas fournir cette limite de sécurité.

**Scénario :** une question n’a pas de réponse dans les passages autorisés. **Éléments probants :** une abstention attendue, un refus d’accès interdit et une réponse synthétique résistant à l’injection. Annotez les affirmations étayées par chaque source. Expliquez pourquoi une citation ou un détecteur d’attaque ne suffit pas à établir la vérité, la confidentialité ou une permission.

<a id="ai-901-unit-3"></a>

## 3. Suivre un client léger sans appels au cloud

Dessinez une requête d’un client Python vers le point de terminaison Foundry voulu et le déploiement configuré, suivie d’une réponse ou d’une erreur. Distinguez identité, autorisation, destination et sélection du déploiement. Esquissez un pseudocode qui lit une configuration protégée, obtient un moyen d’identification adapté, envoie une entrée autorisée, vérifie les erreurs et la sortie, puis affiche un résultat sûr. Étiquetez l’esquisse **pseudocode**, pas code SDK exécutable. Expliquez où peuvent apparaître les dictionnaires, l’itération, les exceptions et les appels asynchrones.

**Scénario :** l’authentification réussit, mais la ressource choisie refuse l’opération. **Éléments probants :** une liste de dépannage expurgée et le comportement attendu du client en cas d’accès refusé, de délai expiré, de sortie vide et de configuration invalide. Comparez la manière dont REST, le SDK et la CLI expriment la même tâche. Identifiez le [démarrage rapide actuel du SDK](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) que vous suivriez lors d’une pratique ultérieure dans le cloud.

<a id="ai-901-unit-4"></a>

## 4. Valider l’extraction multimodale

Inventez une fiche de devoir avec une échéance finale, une deuxième sans date, un schéma avec une unité illisible et une question orale bruitée. Définissez un schéma d’échéance avec types de champs, politique de valeurs manquantes et références aux sources. Produisez des sorties synthétiques délibérément erronées : une date devinée, une mauvaise unité et un terme technique mal entendu. Situez l’échec dans l’extraction, l’interprétation visuelle, la reconnaissance ou le raisonnement en aval. Décrivez un pipeline de reconnaissance vocale et une autre approche multimodale directe prise en charge.

**Scénario :** une sortie est un JSON valide, mais contredit la fiche. **Éléments probants :** des résultats distincts de validation du schéma et de la source, des règles de révision en cas d’ambiguïté et une solution textuelle d’accessibilité. Incluez la manière dont [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) pourrait traiter des documents, images, fichiers audio et vidéos. Ne considérez pas la confiance comme un substitut aux éléments probants.

<a id="ai-901-unit-5"></a>

## 5. Évaluer un agent unique aux outils limités

Concevez un agent de recherche de notes avec des instructions, un choix de modèle, une recherche limitée aux droits de l’appelant et aucun outil de modification. Définissez la requête et le résultat de son outil de recherche ainsi que la manière dont un client identifie l’agent et maintient le contexte de conversation. Créez une matrice d’échec d’au moins six lignes : réponse étayée, éléments manquants, document interdit, injection, échéance contradictoire et délai d’outil expiré. Ajoutez les résultats attendus avant d’écrire deux réponses synthétiques concurrentes pour chaque ligne.

**Éléments probants finaux :** remettez les contrats, invites, listes d’accès, esquisse du client, vérifications d’extraction et matrice notée. Évaluez séparément l’appui factuel, les citations, l’abstention ou le refus, la confidentialité, la validité du schéma et les permissions des outils. Expliquez une révision d’invite et son compromis. Énumérez le travail pratique restant : déploiement du modèle et interaction avec le portail, véritable client de conversation SDK, agent unique testé dans le portail et son client. La notation hors ligne prépare à ce travail.
