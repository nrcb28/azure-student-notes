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

## Récupérer les blobs selon le niveau

La suppression réversible conserve les objets pendant la rétention configurée. Elle ne protège pas seule la suppression du conteneur ou du compte. Séparer ces risques.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Récupérer les blobs selon le niveau](15-microsoft-learn.md#learn-blob-recovery)

## Retries bornés et idempotence

Les retries aident les pannes transitoires, pas des identifiants invalides ou une requête incorrecte. Borner tentatives et durée totale, vérifier les retries déjà intégrés aux SDK.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Retries bornés et idempotence](15-microsoft-learn.md#learn-retry)

## Récupérer Key Vault et ses intégrations

La suppression réversible permet de récupérer pendant la rétention. Restaurer le vault ne recrée pas automatiquement certaines intégrations, notamment attributions RBAC et abonnements Event Grid.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Récupérer Key Vault et ses intégrations](15-microsoft-learn.md#learn-vault-recovery)
