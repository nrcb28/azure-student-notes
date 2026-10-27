# Messages et événements

[Sommaire](README.md) · [Certifications](../certifications/fr/README.md)

Une file découple envoi et traitement. Storage Queues sert les tâches simples ; Service Bus propose files et topics ; Event Grid distribue des événements ; Event Hubs ingère de grands flux. Ils ne sont pas interchangeables.

Un message peut revenir après un travail terminé si l'accusé de réception manque. Le consommateur doit tolérer les répétitions grâce à des identifiants stables et des mises à jour cohérentes.

**Miniatures :** le message identifie le document ; le traitement vérifie le résultat, le crée puis confirme. Considérer concurrence et opérations atomiques.

Surveiller âge et nombre des messages. Ajouter des consommateurs ne résout pas une base saturée. Ordre et traitement des échecs dépendent du service.

**Exercice :** prépare le rejeu de messages échoués sans documents en double ni perte d'historique des erreurs.

---

[Précédent](10-architecture.md) · [Suivant](12-devops.md) · [English](../en/11-messaging.md)
