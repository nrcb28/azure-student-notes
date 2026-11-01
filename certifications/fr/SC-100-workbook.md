# SC-100 · Cahier d’architecture de sécurité

[Guide](SC-100.md) · [Dix cas](SC-100-cases.md) · [Sommaire](README.md) · [Español](../es/SC-100-workbook.md)

Cinq unités originales hors connexion pour le service fictif de notes universitaires. Utilisez des actifs, identités, incidents et preuves inventés. Produisez des propositions d’architecture et des résultats d’exercice sur table ; ne modifiez pas de locataires, ne lancez pas d’attaques, ne déployez pas de ressources et ne connectez pas de télémétrie réelle. Aucune exécution cloud ni efficacité de contrôle n’est revendiquée.

<a id="sc-100-unit-1"></a>

## 1. Établir la criticité et la couverture des contrôles

**Scénario :** l’université ajoute des réponses d’évaluation non publiées à une application qui ne contenait auparavant que des notes publiques. Identifiez les opérations critiques, les propriétaires de données, les menaces probables et les impacts métier. Distinguez la cartographie des capacités MCRA, les exigences de contrôle MCSB, les responsabilités de plateforme CAF et l’examen des charges Well-Architected. Explicitez les hypothèses au lieu d’inventer un inventaire complet.

**Preuves :** un schéma hypothétique d’actifs, trois risques priorisés, les frontières actuelles des contrôles et les informations manquantes. Incluez une exigence qui ne peut pas être évaluée par un seul résultat Azure Policy.

**Livrable :** une table de couverture contenant exigence, contrôle, périmètre, responsable, preuve, lacune et critère d’acceptation. Ajoutez une courte ADR comparant deux options et nommant le responsable autorisé à accepter le risque résiduel.

<a id="sc-100-unit-2"></a>

## 2. Borner identité, réseau et privilèges

**Scénario :** utilisateurs du campus, enseignants invités, administrateurs, pipeline de déploiement et agent IA accèdent à différentes parties du service de notes. Dessinez les frontières d’identité, d’application, de réseau et d’administration entre le campus et les clouds. Précisez les autorisations minimales, l’activation privilégiée, l’accès de récupération et la propriété des identifiants d’accès ou de la fédération. Vérifiez les hypothèses de fonctionnalités et de licences pour les contrôles d’agent proposés.

**Preuves :** six décisions attendues d’autorisation ou de refus, les dépendances DNS privées, les hypothèses d’accès public et une explication du maintien de l’autorisation malgré un chemin réseau accessible.

**Livrable :** un schéma des frontières de confiance et une matrice d’accès avec responsable, périmètre, cycle de vie, journalisation et comportement de défaillance. Incluez une action d’outil d’agent refusée et un chemin d’administrateur de récupération. Gardez toutes les identités et requêtes fictives.

<a id="sc-100-unit-3"></a>

## 3. Relier la détection à une réponse autorisée

**Scénario :** une activité d’identité suspecte sur le campus coïncide avec des téléchargements inhabituels de documents. Définissez les capacités SOC nécessaires sur identité, terminal, application, cloud et SaaS. Reliez deux chemins de menaces prioritaires aux techniques MITRE ATT&CK pertinentes, à la télémétrie attendue, à la corrélation, au triage et au confinement. Expliquez les responsabilités de Sentinel et de Defender XDR sans supposer une visibilité complète.

**Preuves :** une chronologie synthétique montrant les sources d’événements, le délai d’ingestion, les hypothèses de rétention, un signal manquant et des explications concurrentes. Identifiez qui peut désactiver une identité ou interrompre un serveur d’examen.

**Livrable :** une matrice de couverture de détection et une table d’autorité de réponse avec escalade, approbation, retour arrière et préservation des preuves. Marquez chaque détection et réponse comme proposée, avec des preuves d’acceptation requises avant l’usage opérationnel.

<a id="sc-100-unit-4"></a>

## 4. Protéger les données et le cycle de vie logiciel et IA

**Scénario :** un nouvel assistant IA récupère des documents de cours et un pipeline de build déploie son API. Classez les informations et cartographiez les frontières d’étiquetage, de chiffrement, de DLP, de rétention et d’accès applicatif. Indiquez où les contrôles ne sont pas pris en charge. Modélisez les menaces sur les dépendances, les identités de build, la promotion d’artefacts, l’injection de prompt documentaire et l’accès aux outils.

**Preuves :** une recherche synthétique bénigne, un document portant une instruction non fiable et un build fictif non approuvé. Consignez les refus attendus de recherche documentaire et d’outils plutôt que de générer des instructions d’exploitation ou d’exécuter des tests.

**Livrable :** une matrice de contrôles de données et un examen de cycle de vie montrant responsable, périmètre, provenance, autorisations, approbation et preuves d’acceptation. Expliquez pourquoi détection, chiffrement et correspondances de référentiels laissent chacun des risques distincts à évaluer.

<a id="sc-100-unit-5"></a>

## 5. Répéter la récupération et séquencer le programme

**Scénario :** un rançongiciel affecte le stockage documentaire principal et un compte privilégié. Utilisez les exigences d’exercice d’un RTO applicatif de deux heures et d’un RPO de quinze minutes. Retracez les dépendances d’identité, d’accès au plan de contrôle, de DNS, de clés, de configuration, de métadonnées, de fichiers et de déploiement. Comparez les points de récupération protégés à la réplication ; considérez la corruption et la compromission de l’administration des sauvegardes.

**Preuves :** un ordre de restauration sur table, des horodatages hypothétiques de récupération, des vérifications de cohérence et une dépendance qui empêche l’application de servir des lectures autorisées même après le retour des fichiers. Étiquetez les mesures comme supposées.

**Livrable :** un plan d’acceptation de récupération et une feuille de route en trois phases limitée par le financement d’un semestre. Incluez responsables, effort estimé, prérequis, critères de retour arrière, exceptions assorties d’une expiration et approbation métier du risque restant. Aucune restauration réelle ni aucun objectif de récupération n’est validé.

[Guide d’étude officiel SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) · [Modèle d’ADR](ADR-template.md)
