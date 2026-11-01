# AZ-700 · Gemeinsames vertiefendes Arbeitsbuch

[Leitfaden](AZ-700.md) · [10 Fälle](AZ-700-cases.md) · [Inhalt](README.md) · [Netzwerklabor](network-lab.md)

Fünf Einheiten mit entsprechenden Zielen, Szenarien und Abgaben in acht Sprachen. Es sind Entwurfs- und Diagnoseübungen. Vorhersagen sind keine Azure-Beobachtungen; kein neues Deployment wird behauptet.

<a id="az-700-unit-1"></a>

## 1. Einen Adress- und Abhängigkeitsplan erstellen

Entwirf Campus-, Hub-, Web- und Datennetze für die App. Erfasse bestehende Bereiche vor der Wahl neuer CIDRs und reserviere Platz für Wachstum und dienstspezifische Subnetze. Erkläre, warum ein gewöhnliches /24 in Azure weniger zuweisbare IPv4-Adressen als seine rohe Adresszahl besitzt. Ein delegierter Dienst passt nicht automatisch in jedes leere Subnetz.

**Szenario:** Ein Partner nutzt einen Bereich, der den geplanten Hub überlappt. **Nachweis:** Tabelle mit Eigentümer, Präfix, Zweck, Grenzen und Wachstumsreserve. **Abgabe:** überarbeiteter nicht überlappender Entwurf, beseitigter Konflikt und eine noch anhand aktueller Dienstdokumentation zu prüfende Bedingung.

<a id="az-700-unit-2"></a>

## 2. Eine Anfrage und ihre Antwort verfolgen

Zeichne einen API-Aufruf vom Web-Spoke durch eine Prüfappliance zu einem anderen Netz. Notiere je Schritt Zielpräfix, nächsten Hop und relevante Weiterleitungseinstellung. Zeichne die Antwort getrennt. Zustandsbehaftete Prüfung und Adressübersetzung können eine oberflächlich plausible asymmetrische Route scheitern lassen. Peering allein macht einen Hub nicht zum Transitrouter.

**Szenario:** Nach einer UDR-Änderung sendet die Quelle Anfragen, erhält aber keine Antwort. **Nachweis:** konkurrierende Routen und effektiver nächster Hop beider Richtungen. **Abgabe:** eine überprüfbare Hypothese, eine bestätigende Beobachtung und eine Rücknahmebedingung für die vorgeschlagene Änderung.

<a id="az-700-unit-3"></a>

## 3. Privaten Zugriff schichtweise diagnostizieren

Beschreibe, wie ein Campusclient den Speichernamen mit dem gewählten DNS- und Weiterleitungsentwurf auflöst. Benenne Dienst-Unterressource, private Adresse, Genehmigungsstatus und vorgesehene Netzwerkeinschränkungen des privaten Endpunkts. Trenne Namensauflösung, Erreichbarkeit, TLS und Datenrechte: Der Nachweis einer Schicht bestätigt nicht die übrigen.

**Szenario:** Öffentlicher Zugriff ist deaktiviert, der Client löst aber weiterhin öffentlich auf. **Nachweis:** Hostname, Resolverpfad, zurückgelieferte Adresse und erwartetes privates Ziel. **Abgabe:** DNS-Korrekturvorschlag und anschließende Prüfungen von Routing und authentifiziertem Datenzugriff. Begründe, warum eine dauerhafte öffentliche IP-Überschreibung ungeeignet ist.

<a id="az-700-unit-4"></a>

## 4. Bereitstellungs- und Schutzkontrollen wählen

Vergleiche einen TCP-Dienst, eine regionale und eine globale Webanwendung. Wähle Kandidaten nach Protokoll, Reichweite, Routingbedarf und Ausfallverhalten statt nach einem gemerkten Produktetikett. Ergänze Sondenverhalten und Zertifikatsbehandlung. Unterscheide DNS-Auswahl vom Anfrageproxy sowie WAF-Prüfung von Netzwerkfilterung und DDoS-Verfügbarkeitsschutz.

**Szenario:** Das Backend besteht seine Gesundheitssonde, liefert aber falsche Dokumente. **Nachweis:** Was prüft die Sonde, was validiert eine echte Operation? **Abgabe:** kurze Entscheidungsnotiz mit verworfener Alternative und einem funktionalen Signal, das die weitere Ausrollung einer fehlerhaften Version stoppen würde.

<a id="az-700-unit-5"></a>

## 5. Hybride Wiederherstellung entwerfen und prüfen

Plane primäre und alternative Campusverbindungen. Erfasse gekoppelte Ausfälle, Routenänderungen, Verschlüsselung, Kapazität und Anwendungsabhängigkeiten. Private ExpressRoute-Anbindung belegt keine standardmäßige Verschlüsselung. Lege Schutzgrenze und kompatiblen Verschlüsselungsentwurf fest; nicht jeder Leitungstyp unterstützt dieselben Optionen.

**Szenario:** Die Hauptverbindung fällt während vieler Mitschriftendownloads aus. **Nachweis:** erwartete Hin- und Rückwege, Annahmen zur Ersatzkapazität und messbare Kriterien der Anwendungswiederherstellung. **Abgabe:** isolierter Testplan, Rückkehrschritte und Spalten für erwartet und beobachtet. Ohne autorisierte Umgebung gibst du den Entwurf ab und kennzeichnest Beobachtungen ausdrücklich als ungeprüft.

[Offizieller Leitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) · [Technische Erklärungen](AZ-700.md)
