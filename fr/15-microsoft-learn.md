# Approfondissements pratiques Microsoft Learn

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Sources vérifiées le 27 octobre 2026. Explications reformulées et cas originaux. Les vérifications proposées n'ont pas été exécutées dans Azure.

<a id="learn-sas"></a>

## 1. SAS et Entra ID

Une user delegation SAS pour Blob utilise une clé de délégation obtenue avec Entra ID. Son émission exige des droits ; connaître l'URL ne suffit pas.

**Cas :** téléchargement temporaire d'un PDF. Limiter ressource, lecture et durée, éviter les URL sensibles dans les logs. Distinguer expiration, autorisation et réseau. Prévoir fuite et révocation selon le type de SAS.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. Suivre le DNS privé

Le client doit résoudre le nom du service vers l'IP du private endpoint. L'interface seule ne configure pas tous les résolveurs. La zone recommandée dépend du service.

**Cas :** fonctionnement depuis la VM, échec depuis l'université. Comparer réponses DNS, liens de zones, transfert et routes. Ne pas remplacer aveuglément toute une zone publique ni coder une IP fixe. Résoudre correctement ne donne aucun droit sur les données.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Évaluation et remédiation

La remédiation applique modify ou deployIfNotExists aux ressources existantes avec l'identité et les droits de l'attribution. Modifier la définition ne met pas automatiquement à jour toutes les permissions.

**Cas :** anciennes ressources non conformes. Examiner effet, étendue, identité et rôles, tester sur un groupe pilote et enregistrer les résultats. Deny ne transforme pas automatiquement les anciennes configurations.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR et collecte

Les data collection rules décrivent collecte et routage dans les scénarios compatibles. Des transformations peuvent filtrer ou modifier les données avant destination. Elles ne remplacent pas universellement diagnostic settings.

**Cas :** événements VM absents. Vérifier agent, association, source, flux, destination et schéma. Tout collecter augmente coût et exposition ; trop filtrer supprime des éléments d'enquête.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. Limites de what-if

What-if prévoit des changements sans les appliquer. Droits, dépendances et expressions peuvent limiter l'analyse. Un résultat incomplet ne prouve pas l'absence de changements.

**Cas :** Ignore ou module non évalué. Lire les diagnostics et isoler le module sans conclure NoChange. Séparer compilation, validation, prévision et test après déploiement. La revue tient compte des éléments non analysés.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Des slots réellement actifs

Un slot possède son hostname et exécute une application. Copier les paramètres ne clone ni contenu, ni réseau privé, ni toutes les dépendances. Le swap comprend préparation et préchauffage.

**Cas :** staging envoie de vrais courriels. Vérifier connexions, identité, paramètres spécifiques et tâches de démarrage. Zéro trafic utilisateur n'empêche pas le travail autonome. Le swap inverse n'annule pas une migration destructive.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zones et responsabilités

Les landing zones organisent identité, connectivité, administration et gouvernance. Plateforme et applications peuvent avoir des responsables distincts. Un accélérateur ne remplace pas les exigences.

**Cas :** cinq facultés partagent le réseau et gèrent leurs applications. Définir responsables, frontières, droits, politiques et coûts. Ne pas reproduire une plateforme d'entreprise complète pour un petit laboratoire sans justification.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks et publication

Les responsables des ressources Azure Pipelines administrent approvals et checks hors du YAML. Une étape doit satisfaire les contrôles des ressources qu'elle consomme.

**Cas :** revue indépendante et fenêtre horaire en production. Définir ressource, réviseurs, expiration et refus. Tester délais et changements. Un pipeline vert n'autorise pas toutes les connexions de service.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)
