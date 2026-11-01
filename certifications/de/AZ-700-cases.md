# AZ-700 · 10 Fälle mit begründeten Antworten

[Leitfaden](AZ-700.md) · [Arbeitsbuch](AZ-700-workbook.md) · [Inhalt](README.md)

Eigene Lernszenarien, keine offiziellen oder geleakten Prüfungsfragen. Nenne die Anforderung, verwirf eine Alternative und bestimme die Nachweise, bevor du aufklappst. Eine Azure-Ausführung wird nicht behauptet.

## 1. Campus und neues Azure-VNet nutzen beide 10.70.0.0/16. Machen gewöhnliches Peering oder VPN ihre Adressen eindeutig?

<details>
<summary>Begründung</summary>

Überlappende Bereiche sind ein Entwurfsproblem, keine fehlende Freigaberegel. Erfasse die tatsächlichen Netze und wähle vor gewöhnlichem Peering oder hybrider Verbindung nicht überlappende Bereiche. Für manche Szenarien gibt es unterstützte Übersetzungsentwürfe; sie bringen eigene Einschränkungen mit und müssen ausdrücklich geplant werden. Ein Paket an denselben privaten Bereich kann den gemeinten Ort nicht durch seine Adresse allein ausdrücken. Nachweise wären Bereichsinventar, überarbeiteter Adressplan und erwartete Routen zu jedem Ziel.

</details>

## 2. A ist mit B und B mit C gekoppelt. A erreicht C nicht. Sollte die Quell-VM Owner erhalten?

<details>
<summary>Begründung</summary>

Nein. VNet-Peering ist nicht automatisch transitiv, und eine Azure-Verwaltungsrolle ersetzt keinen Netzwerkpfad. Entscheide, ob eine direkte Verbindung oder ein unterstützter Transitentwurf gebraucht wird. Prüfe Routen, Weiterleitung und Sicherheit in beiden Richtungen. Bei einem gemeinsamen Gateway sind die konkreten Transiteinstellungen wichtig, statt sämtliche Spoke-Weiterleitung vorauszusetzen. Der nützliche Nachweis ist ein vollständiger Paketweg mit effektiven nächsten Hops, nicht eine breitere Verwaltungsrolle.

</details>

## 3. Eine neue Standardroute zeigt auf die Firewall, Verkehr zu einem spezifischeren Präfix aber anderswohin. Sind alle benutzerdefinierten Routen defekt?

<details>
<summary>Begründung</summary>

Nicht zwingend. Prüfe alle geltenden Routen und das tatsächliche Ziel. Eine breite Standardroute verdrängt nicht automatisch jede spezifischere Route. Vergleiche Präfixe, Routenursprung und effektiven nächsten Hop anhand der Azure-Auswahlregeln. Bestätige auch die Zuordnung der gewünschten Routingtabelle zum Quellsubnetz. Der Nachweis soll konkurrierende Präfixe und beobachteten nächsten Hop zeigen. Änderungen an Sicherheitsregeln erklären nicht, welche Route gewählt wurde.

</details>

## 4. Anfragen passieren eine zustandsbehaftete Appliance, Antworten laufen anders zurück. Warum kann eine erlaubte Verbindung scheitern?

<details>
<summary>Begründung</summary>

Ein zustandsbehaftetes Gerät muss unter Umständen beide Seiten einer Verbindung sehen. Bei asymmetrischem Routing verfehlt der Rückverkehr das Gerät mit dem ursprünglichen Verbindungszustand oder trifft auf ein anderes ohne passenden Zustand. Prüfe Hin- und Rückrouten, Applianceweiterleitung und Adressübersetzung. Füge nicht wahllos eingehende Freigaben hinzu, bevor diese Hypothese geprüft wurde. Sinnvoll sind ein Diagramm beider Pfade und Beobachtungen von Endpunkten oder unterstützten Diagnosewerkzeugen.

</details>

## 5. Öffentlicher Speicherzugriff ist deaktiviert. Die API kann einen privaten Endpunkt nutzen, löst aber die öffentliche Adresse auf. Was zuerst?

<details>
<summary>Begründung</summary>

Untersuche den tatsächlichen DNS-Pfad des API-Clients: Servereinstellungen, private Zone, VNet-Verknüpfung und hybride Weiterleitung. Behalte den Dienstnamen bei und sorge für die passende Auflösung zum privaten Ziel. Storage Blob Data Reader korrigiert keine öffentliche DNS-Antwort. Sind Namensauflösung und Routing in Ordnung, prüfe die Datenautorisierung getrennt. Dokumentiere Hostname, aufgelöste Adresse, verwendeten Resolver, Endpunkt-Unterressource und eine spätere authentifizierte Operation als unterschiedliche Nachweise.

</details>

## 6. Campus-Azure-Daten müssen verschlüsselt sein. Belegt der Kauf von ExpressRoute allein diese Eigenschaft?

<details>
<summary>Begründung</summary>

Nein. Private ExpressRoute-Konnektivität unterscheidet sich von Verschlüsselung; Verkehr wird nicht standardmäßig verschlüsselt. Lege fest, was zwischen welchen Punkten geschützt werden soll. MACsec ist für unterstützte ExpressRoute-Direct-Verbindungen eine Option, aber nicht automatisch auf jedem Anbieter-Circuit verfügbar. Ein passender IPsec-Entwurf kann eine Ende-zu-Ende-Anforderung abdecken. Vergleiche Unterstützung und Leistung und dokumentiere die Schlüsselverwaltung. Ein Diagramm des privaten Pfads genügt als Verschlüsselungsnachweis nicht.

</details>

## 7. Ein Team möchte regionale Auswahl per DNS und erwartet jede Anfrage über Traffic Manager. Was muss korrigiert werden?

<details>
<summary>Begründung</summary>

Traffic Manager liefert DNS-basierte Endpunktauswahl und ist kein Anfrageproxy. Der Client verbindet sich mit dem gewählten Ziel; Caches verzögern möglicherweise die Wirkung einer DNS-Änderung. Bei globaler HTTP-Proxy-Bereitstellung ist Azure Front Door anhand der Anforderungen zu prüfen, bei regionalem HTTP-Routing Application Gateway. Zeige DNS-Austausch und Anwendungsverbindung getrennt. Erkläre, wie Gesundheitsinformationen die Auswahl beeinflussen, statt den gesamten Verkehr durch einen DNS-Dienst zu zeichnen.

</details>

## 8. Auf einem Subnetz ist ein Dienstendpunkt aktiviert. Warum beweist das keine private Endpunktadresse des Speicherkontos dort?

<details>
<summary>Begründung</summary>

Dienstendpunkt und privater Endpunkt sind unterschiedliche Entwürfe. Die Aktivierung eines Dienstendpunkts erstellt keine private Netzwerkschnittstelle für das Speicherkonto im Subnetz. Prüfe tatsächliche Dienstendpunktkonfiguration, Dienstnetzwerkregeln und Authentifizierung. Verlangt die Anforderung ausdrücklich eine private Zieladresse, untersuche einen unterstützten privaten Endpunkt samt DNS und Zugriffsregeln. Erfasse aufgelöstes Ziel und relevante Ressourceneinstellungen, statt aus dem gemeinsamen Wort „Endpunkt“ Gleichwertigkeit abzuleiten.

</details>

## 9. Eine neue Ablehnungsregel blockiert frische Verbindungen, aber eine bestehende Sitzung läuft weiter. Ignoriert das NSG seine Regeln?

<details>
<summary>Begründung</summary>

Nicht zwingend. NSGs sind zustandsbehaftet; eine Regeländerung muss einen bestehenden Datenfluss nicht sofort unterbrechen. Trenne eine wirklich neue Verbindung von einer wiederverwendeten Sitzung. Prüfe die effektiven Regeln an Subnetz und Schnittstelle einschließlich Quelle, Ziel, Port, Protokoll und Priorität. Ein Regelname reicht nicht. Die Beobachtung muss festhalten, ob der Test einen neuen Datenfluss erzeugt hat. Breitere Rollen oder das Löschen der VM erklären dieses Verhalten nicht.

</details>

## 10. Ein Diagramm zeigt ExpressRoute und Ersatz-VPN. Welche Nachweise fehlen für ausfallsichere Anwendungskonnektivität?

<details>
<summary>Begründung</summary>

Ermittle gemeinsame Fehlerdomänen und prüfe den kompletten Ersatzpfad: eigene Geräte, Anbieter, Peeringstandorte, Gateways, Routenankündigungen, Rückwege, Tunnelkapazität, DNS-Abhängigkeiten und erneute Anwendungsverbindung. Eine zweite Linie im Bild beweist keine korrekte Verkehrsauswahl beim Ausfall. Plane einen isolierten, genehmigten Test mit Erwartungen, Beobachtungen, Wiederherstellung und Kriterien zur Rückkehr in den Normalbetrieb. Diese Notizen liefern den Entwurf, behaupten aber keinen ausgeführten Failover.

</details>

Technische Quellen und die geprüfte Prüfungsreferenz stehen im [Leitfaden](AZ-700.md). Das [Arbeitsbuch](AZ-700-workbook.md) macht aus Antworten Diagramme und Nachweise.
