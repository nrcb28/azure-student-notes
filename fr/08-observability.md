# Supervision et diagnostic

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

Métriques, journaux et traces éclairent des aspects différents. Azure Monitor fournit des capacités de supervision ; Application Insights observe les applications ; Log Analytics interroge les journaux disponibles avec KQL.

Une faible CPU ne prouve pas une réponse rapide : l'application peut attendre sa base. Une moyenne masque parfois des requêtes très lentes. Considérer distribution, percentiles et volume.

Une alerte utile a un signal, un seuil, une fenêtre et une action. Service Health concerne les services utilisés ; Resource Health une ressource précise.

**Méthode :** délimiter impact et début, examiner le dernier changement, suivre une requête et ses dépendances, tester l'hypothèse, corriger et confirmer.

Ne pas journaliser tokens ou documents entiers. Rétention et détail influencent coût et confidentialité. Adapter OpenTelemetry au runtime.

**Exercice :** mesurer réussite des téléversements, latence et durée de traitement.

---

[Précédent](07-governance.md) · [Suivant](09-costs.md) · [English](../en/08-observability.md)

## Approfondissement Microsoft Learn · dcr

Les data collection rules décrivent collecte et routage dans les scénarios compatibles. Des transformations peuvent filtrer ou modifier les données avant destination. Elles ne remplacent pas universellement diagnostic settings.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-dcr)
