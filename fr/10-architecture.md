# Architecture et reprise

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

Une architecture part des utilisateurs, données, exigences, budget et compétences d'exploitation. Accumuler les services ne garantit pas la qualité.

Notre application combine web/API, base de métadonnées, Blob pour PDF, file et traitement d'analyse. C'est un point de départ conceptuel, pas une configuration de production complète.

Le RTO est le délai de reprise visé. Le RPO exprime en temps la perte récente de données tolérée. Restaurer des données ne suffit pas si API, DNS et droits pointent vers l'ancien environnement.

Prévoir délais d'attente, reprises progressives, idempotence et pannes partielles. Isoler les tests de reprise.

**ADR :** contexte, exigences, alternatives, décision, conséquences, validation et condition de révision.

**Exercice :** défends une solution avec RTO de deux heures et RPO de quinze minutes. Ce sont des exigences à vérifier, pas des garanties attachées au nom d'un produit.

---

[Précédent](09-costs.md) · [Suivant](11-messaging.md) · [English](../en/10-architecture.md)

## Approfondissement Microsoft Learn · landing

Les landing zones organisent identité, connectivité, administration et gouvernance. Plateforme et applications peuvent avoir des responsables distincts. Un accélérateur ne remplace pas les exigences.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Approfondissement Microsoft Learn](15-microsoft-learn.md#learn-landing)
