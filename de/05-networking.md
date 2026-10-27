# Netzwerke und Verbindungen

[Inhalt](README.md) · [[object Object]](../certifications/de/README.md)

Ein VNet ist ein virtuelles Netzwerk; Subnetze teilen seinen Adressraum. NSGs filtern zustandsbehaftet. DNS löst Namen auf. Ein erlaubter Port beweist keinen lauschenden Prozess.

Peering ist nicht automatisch transitiv. VPN Gateway bietet verschlüsselte Tunnel. ExpressRoute bietet private Verbindungen, aber nicht automatisch Ende-zu-Ende-Verschlüsselung.

Private Endpoints ermöglichen privaten IP-Zugriff auf unterstützte Dienste. DNS, Routen und öffentliche Zugriffseinstellungen sind getrennt zu prüfen.

Load Balancer arbeitet mit TCP/UDP, Application Gateway mit regionalem Webverkehr, Front Door als globaler Webzugang. Traffic Manager wählt Ziele über DNS.

**Diagnose:** Name und aufgelöste IP, Route, Filter, Port, Authentifizierung und Autorisierung nacheinander prüfen. Alle Ports zu öffnen verdeckt das Problem.

**Frage:** Warum reicht der private Endpunkt nicht? Jeder Client muss seine private Adresse auflösen und erreichen können.

---

[Zurück](04-storage.md) · [Weiter](06-identity.md) · [English](../en/05-networking.md)
