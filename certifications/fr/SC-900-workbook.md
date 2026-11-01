# SC-900 · Cahier de décisions et de preuves

[Guide](SC-900.md) · [Dix cas](SC-900-cases.md) · [Sommaire](README.md)

Cinq unités originales pour appliquer les mêmes objectifs dans chaque langue. Utiliser une université fictive et des données synthétiques. Ces exercices de conception hors ligne ne revendiquent aucun déploiement de politique, modification de tenant ou exécution dans Azure.

<a id="sc-900-unit-1"></a>

## 1. Cartographier les responsabilités et les frontières de confiance

Dessiner navigateur, fournisseur d’identité, application et stockage des documents. À chaque frontière, expliquer ce qui est vérifié et qui exploite le contrôle. Séparer les tâches de plateforme du fournisseur des décisions de l’organisation sur utilisateurs, partage, configuration et données. Expliquer pourquoi le réseau du campus ne suffit pas à rendre une requête fiable.

**Scénario :** un invité doit lire les notes publiées, jamais les corrigés non publiés. **Preuves :** un schéma et un tableau de deux opérations autorisées et deux refusées, avec responsables et observations nécessaires. **Livrable :** une page distinguant résultats attendus et réellement observés. Aucun test sur un tenant réel n’est demandé.

<a id="sc-900-unit-2"></a>

## 2. Concevoir une décision d’accès

Préciser type d’identité, application cible, action et droit minimal. Proposer une exigence d’authentification et expliquer catégories de facteurs et résistance à l’hameçonnage. Décrire les signaux d’accès conditionnel pertinents et les contrôles applicatifs restant nécessaires. Documenter portée, exclusions, récupération et licences plutôt qu’écrire « activer la MFA pour tous ».

**Scénario :** un enseignant invité accède aux cours depuis un appareil personnel. **Preuves :** décisions attendues pour une requête autorisée, une méthode insuffisante et une opération dépassant ses droits. **Livrable :** une matrice d’accès argumentée. Rester dans l’hypothèse ; ne pas modifier les contrôles du tenant ni confondre rapport seul et application effective.

<a id="sc-900-unit-3"></a>

## 3. Séparer privilège, droit et risque

Écrire trois questions : qui peut activer un rôle privilégié, qui doit conserver un droit sur un projet et quel comportement d’identité mérite investigation ? Les associer respectivement à PIM, aux revues d’accès et aux concepts de risque d’identité. Définir portée et durée d’un rôle sans supposer qu’un privilège large mais bref est automatiquement minimal.

**Scénario :** un ancien membre reste dans un groupe, et un administrateur a besoin d’un accès temporaire de maintenance. **Preuves :** chemins d’attribution, décision du propriétaire, processus d’activation proposé et enregistrements séparés d’éventuels comportements suspects. **Livrable :** une procédure courte indiquant approbateurs et preuves de réalisation. Ne pas créer d’attributions privilégiées.

<a id="sc-900-unit-4"></a>

## 4. Prévoir une détection et une réponse limitée

Choisir une chaîne d’attaque fictive mêlant courriel, identité et charge de travail. Lister les événements nécessaires pour confirmer ou rejeter l’hypothèse. Expliquer l’apport de la corrélation Defender XDR et la pertinence éventuelle des connecteurs, analyses et orchestrations de Sentinel. Marquer les données absentes : un résultat vide ne prouve pas qu’un événement n’a jamais eu lieu.

**Scénario :** une activité de connexion suspecte suit un hameçonnage. **Preuves :** chronologie, couverture des sources, analyste responsable et proposition de notification avant toute action perturbatrice. **Livrable :** un tableau de détection et réponse avec faux positifs et récupération. Pas d’ingestion, d’activation payante ni de blocage automatique de compte.

<a id="sc-900-unit-5"></a>

## 5. Suivre le cycle de vie des données sensibles

Suivre un document synthétique de sa création à son utilisation interne, son partage, son investigation puis sa suppression. Distinguer classification, protection configurée, DLP, rétention, audit et eDiscovery. Noter les hypothèses de charge et de licence pour chaque capacité. Un score de conformité ne remplace pas la détermination des obligations réelles.

**Scénario :** un corrigé fictif doit rester privé jusqu’à publication et des messages pertinents doivent être conservés pour une enquête. **Preuves :** décisions de manipulation attendues, traces nécessaires, hypothèses de rétention et responsable désigné. **Livrable :** un tableau de cycle de vie expliquant pourquoi aucune étiquette, aucun journal ni aucune sauvegarde ne satisfait seul toutes les exigences. Les obligations juridiques sont fournies par un responsable habilité.

[Guide Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
