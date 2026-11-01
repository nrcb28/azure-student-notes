# AI-103 · Cahier avancé de développement

[Guide](AI-103.md) · [Dix cas](AI-103-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes utilisent des notes universitaires inventées et des jeux de requêtes et réponses hors connexion. Étiquetez les sorties candidates **synthétiques** et le comportement attendu **prévision**. Aucune ressource cloud, aucun identifiant d’accès, aucune donnée étudiante réelle et aucune mesure de service ne sont nécessaires. Ces exercices développent certaines compétences d’implémentation sans prétendre à une couverture complète. Vérification le **1 novembre 2026** par rapport aux [objectifs applicables à compter du 16 avril 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).

<a id="ai-103-unit-1"></a>

## 1. Figer un contrat client et une décision de déploiement

**Scénario :** l’application de notes doit renvoyer une réponse fondée sur les sources depuis un backend Python pendant un pic de révision. Définissez des exemples de requête et de réponse comportant contexte d’identité, identifiant de requête, cours, résultat, réponse, citations et catégories d’erreur. Incluez JSON invalide, accès refusé, dépassement de délai et sortie partielle. Créez un manifeste de compatibilité pour la ressource/le projet, le type de point de terminaison, le nom de déploiement, la génération d’API, les versions de packages et la méthode d’authentification, en suivant les [recommandations actuelles sur les SDK](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview).

**Preuves :** comparez deux modèles candidats hypothétiques sur la qualité, les fonctionnalités prises en charge, la capacité, la latence et l’utilisation des ressources ; signalez les inconnues à vérifier plus tard. **Livrable :** une ébauche de contrat typé, quatre exemples d’échec et une décision de déploiement justifiée sans limites ni prix inventés.

<a id="ai-103-unit-2"></a>

## 2. Concevoir la recherche documentaire à travers une révocation d’accès

**Scénario :** deux étudiants partagent un carnet jusqu’à la révocation de l’accès de l’un d’eux. Inventez six passages, dont une précision de devoir séparée par une limite de fragment proposée. Définissez les identifiants de documents et de fragments, les versions, les emplacements de source, les métadonnées d’ACL et une version d’index/embedding. Comparez les prévisions de recherche par mots-clés, vectorielle et hybride. Représentez dans leur ordre réel l’authentification de l’appelant, le filtrage des autorisations, la recherche documentaire, la consultation du cache et le contexte du modèle.

**Preuves :** une table d’accès avant et après couvrant la propagation dans l’index, les fragments en cache et la mémoire de conversation, plus une citation sans appui et une réponse d’insuffisance de preuves. **Livrable :** une conception de recherche documentaire avec une politique de fraîcheur des autorisations, une règle d’invalidation et quatre cas de régression. Expliquez comment les [modèles d’accès Search](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) influencent le choix d’implémentation.

<a id="ai-103-unit-3"></a>

## 3. Tracer un outil approuvé au résultat incertain

**Scénario :** un agent de notes propose de partager un document autorisé avec un groupe d’étude. Définissez le schéma de l’outil, le périmètre de l’appelant, la charge utile exacte d’approbation, la clé d’opération, le stockage de statut, le budget de délai et la propriété de la conversation. Esquissez du **pseudocode** pour valider → autoriser → approuver → exécuter → réconcilier → rendre compte ; il s’agit d’une conception applicative, pas de code SDK exécutable. Ajoutez un transfert planificateur/agent de recherche qui préserve les mêmes autorisations.

**Preuves :** traces de refus, d’exécution réussie, de remise en double, d’approbation expirée et de réponse perdue après réussite du backend. **Livrable :** une table de transitions d’état et une trace expurgée montrant pourquoi une nouvelle tentative ne peut pas dupliquer le partage. Reliez la conception à la [frontière actuelle d’appel de fonctions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling).

<a id="ai-103-unit-4"></a>

## 4. Valider les champs multimodaux et le sens

**Scénario :** une feuille de devoir comporte des échéances de brouillon et de remise finale, un graphique possède un axe illisible et une question orale contient « mutex ». Définissez des contrats distincts pour texte, parole, compréhension visuelle, génération de médias et extraction. Écrivez un schéma de champs Content Understanding avec descriptions précises, types, gestion des valeurs nulles et références aux sources. Construisez des sorties synthétiques erronées : échéances inversées, unité inventée et terme technique mal entendu.

**Preuves :** vérifications séparées du schéma, des sources, de la sémantique et de l’accessibilité, comprenant un champ incorrect avec une confiance élevée et une solution de correction textuelle. **Livrable :** cinq exemples annotés et une politique de révision calibrée sur des exemples étiquetés. Consultez la [conception d’analyseur](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices) et la [disponibilité de l’ancrage documentaire](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement), en explicitant les limites de modalité et d’API.

<a id="ai-103-unit-5"></a>

## 5. Évaluer et répéter un retour arrière

**Scénario :** une version candidate change les prompts, les schémas d’outils et un modèle d’embedding. Notez huit cas fixes : réponse appuyée sur les sources, source manquante, accès révoqué, injection, citation incorrecte, échéance ambiguë, dépassement de délai d’outil et action en double. Séparez qualité de recherche documentaire, appui des affirmations, sécurité, respect des autorisations et prévisions de latence. Décrivez un déploiement progressif limité et les mesures qui déclencheraient un rétablissement.

**Preuves :** une feuille de comparaison, un manifeste de version compatible, un schéma de télémétrie expurgée et une séquence de retour arrière restaurant ensemble client, index, prompt et outils. **Livrable :** un dossier de livraison examinable et une liste des mesures qui exigent encore un laboratoire cloud autorisé. Utilisez les [recommandations d’évaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation) pour distinguer les prévisions hors connexion des preuves de déploiement observées ; ne présentez pas les scores synthétiques comme des résultats Azure.
