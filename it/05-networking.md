# Reti e connettività

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Una VNet è una rete virtuale; le subnet ne dividono gli indirizzi. Gli NSG filtrano traffico con stato. DNS risolve nomi. Una porta consentita non dimostra che un processo stia ascoltando.

Il peering non è automaticamente transitivo. VPN Gateway offre tunnel cifrati; ExpressRoute offre connettività privata, non automaticamente cifratura end-to-end.

Un private endpoint fornisce accesso tramite IP privato a un servizio compatibile. Occorre verificare DNS, instradamento e accesso pubblico separatamente.

Load Balancer lavora con TCP/UDP; Application Gateway con traffico web regionale; Front Door offre ingresso web globale; Traffic Manager seleziona destinazioni tramite DNS.

**Diagnosi:** prima nome e indirizzo risolto, poi route, filtri, porta, autenticazione e autorizzazione. Aprire tutte le porte nasconde il problema.

**Domanda:** perché creare il private endpoint non configura ogni client? Ogni client deve risolvere e raggiungere l'indirizzo privato.

---

[Precedente](04-storage.md) · [Successivo](06-identity.md) · [English](../en/05-networking.md)

## Approfondimento Microsoft Learn · dns

Il client deve risolvere il nome del servizio verso l'IP del private endpoint. Creare l'interfaccia non configura ogni resolver; le zone dipendono dal servizio.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-dns)
