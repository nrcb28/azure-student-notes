# Réseaux et connectivité

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

Un VNet est un réseau virtuel, divisé en sous-réseaux. Les NSG filtrent avec état. DNS résout les noms. Autoriser un port ne prouve pas qu'un processus écoute.

Le peering n'est pas automatiquement transitif. VPN Gateway fournit des tunnels chiffrés. ExpressRoute apporte une connexion privée, pas automatiquement un chiffrement de bout en bout.

Un private endpoint donne un accès par adresse privée à un service compatible. Vérifier séparément DNS, routage et accès public.

Load Balancer traite TCP/UDP ; Application Gateway le web régional ; Front Door l'entrée web globale ; Traffic Manager sélectionne via DNS.

**Diagnostic :** nom, adresse résolue, route, filtres, port, authentification puis autorisation. Ouvrir tous les ports masque le problème.

**Question :** pourquoi le private endpoint ne suffit-il pas ? Chaque client doit résoudre et joindre son adresse privée.

---

[Précédent](04-storage.md) · [Suivant](06-identity.md) · [English](../en/05-networking.md)
