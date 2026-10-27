# Supervision et diagnostic

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

Métriques, journaux et traces éclairent des aspects différents. Azure Monitor fournit des capacités de supervision ; Application Insights observe les applications ; Log Analytics interroge les journaux disponibles avec KQL.

Une faible CPU ne prouve pas une réponse rapide : l'application peut attendre sa base. Une moyenne masque parfois des requêtes très lentes. Considérer distribution, percentiles et volume.

Une alerte utile a un signal, un seuil, une fenêtre et une action. Service Health concerne les services utilisés ; Resource Health une ressource précise.

**Méthode :** délimiter impact et début, examiner le dernier changement, suivre une requête et ses dépendances, tester l'hypothèse, corriger et confirmer.

Ne pas journaliser tokens ou documents entiers. Rétention et détail influencent coût et confidentialité. Adapter OpenTelemetry au runtime.

**Exercice :** mesurer réussite des téléversements, latence et durée de traitement.

---

[Précédent](07-governance.md) · [Suivant](09-costs.md) · [English](../en/08-observability.md)
