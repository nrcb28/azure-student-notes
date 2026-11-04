# AZ-802 · Windows-Server-Arbeitsbuch mit beleggestützten Entscheidungen

[Leitfaden](AZ-802.md) · [10 Fälle mit Begründungen](AZ-802-cases.md) · [Inhalt](README.md)

Fünf entsprechende Einheiten verbinden die sieben AZ-802-Lernbereiche. Verwende das erfundene isolierte Universitätslabor `lab.example.test`. Erstelle eine überprüfbare Entscheidung samt Nachweispaket, keine Liste von Einstellungen aus einem Video. Dies sind vorgeschlagene Windows-Übungen; es wird keine Ausführung von AD, Hyper-V, Azure, Wiederherstellung oder Sicherheitsmaßnahmen behauptet. Reiche ohne kompatibles Windows-Labor einen gekennzeichneten Entwurf und vorhergesagte Beobachtungen ein, statt Ergebnisse zu erfinden.

Führe für jede Einheit ein Protokoll: Ausgangszustand, Hypothese, konkurrierende Erklärung, ausgewählte rein lesende Prüfung, vorgeschlagene Änderung, erwartete Beobachtung, tatsächliche Beobachtung bei Ausführung und Abbruch-/Rücknahmebedingung. Erfasse Betriebssystemedition und -version, installierte Module, benötigte Rechte und Zielidentität. Schwärze Geheimnisse und personenbezogene Daten. Die Voraussetzungsmatrix des Leitfadens gilt für seine Befehlsbeispiele. Kein Befehl verleiht die Befugnis, ein unbeteiligtes System zu untersuchen.

<a id="az-802-unit-1"></a>

## 1. Eine Identitätsänderung vom Verzeichnis bis zum Zugriff verfolgen

**Szenario:** LAB-DC1 nimmt eine Änderung der Forschungsgruppenmitgliedschaft an. Ein Client im entfernten Gebäude kann aber weiterhin nicht auf `\\LAB-FS1\LabNotes` zugreifen. Er wählt LAB-DC2 aus. Ein gesonderter Außenstellenentwurf verwendet einen RODC, weil der Raum nur begrenzten physischen Schutz besitzt.

**Untersuchung:** Zeichne Gesamtstruktur und Domäne, zwei beschreibbare Controller, Außenstellen-RODC, DNS-Resolver, Standorte und IP-Subnetzzuordnungen. Markiere den Controller, der die Änderung angenommen hat, und den vom Client verwendeten. Bestimme Replikationspfad, relevante SRV-Einträge, Zeithierarchie, Benutzertoken und Freigabe-/NTFS-Grenze. Wähle eine geordnete Prüffolge, die veralteten Verzeichniszustand von einem Problem effektiven Zugriffs unterscheiden kann. Ergänze eine erwartete Beobachtung, die deine erste Hypothese widerlegen würde.

Verwende AD-Inventar-, Resolver-/Zeit- und Replikationsabfragen des Leitfadens nur aus einem passenden Windows-Verwaltungskontext. Erkläre bei Gruppenrichtlinien Geltungsbereich, Clientverarbeitung und effektive Einstellungen getrennt. Definiere für den RODC gewöhnliche Konten für Zugriff ohne WAN, weiter auszuschließende Konten, delegierte Außenstellenverwaltung und Reaktion auf Geräteverlust. Prüfe die effektive Kennwortreplikationsrichtlinie, statt ihren Inhalt aus einem Gruppennamen abzuleiten.

**Nachweise:** Topologie mit Identitätsgrenzen; bereinigte Abfragekontexte und Zeitstempel; Zeitlinie einer Objektänderung; beabsichtigte und beobachtete Controllerauswahl; ein Paar aus erlaubtem und verweigertem Dateizugriff; RODC-Cacheentscheidung ohne Kennwörter.

**Abgabe und Entscheidungspunkte:** Schreibe eine einseitige Diagnose mit einer eng begrenzten Reparatur. Sichere vor einer autorisierten Laboränderung die ursprünglichen Resolver-, Standort- und Richtlinieneinstellungen. Stoppe, wenn der fehlerhafte Controller oder Namespace außerhalb des verwerfbaren Labors liegt. Weite keine Rechte aus, übernimm keine FSMO-Rollen zwangsweise und setze nicht alle Konten zurück, um das Symptom zu beseitigen. Erfolg bedeutet, dass die benötigte Verzeichnisänderung konvergiert, der vorgesehene Benutzer nur den beabsichtigten Zugriff erhält und der ausgeschlossene Benutzer ausgeschlossen bleibt.

<a id="az-802-unit-2"></a>

## 2. Grenzen von Remoteverwaltung und VM-Wiederherstellung prüfen

**Szenario:** Eine Bedienperson erreicht einen Mitgliedsserver remote, aber keine zweite Ressource. Ein Vorschlag aktiviert Delegierung wiederverwendbarer Anmeldeinformationen und betreibt einen JEA-Endpunkt auf einem DC. Gleichzeitig scheitert die Produktionskonsistenzprüfung einer VM, aber ein Standardprüfpunkt wird erstellt. Das Labor besitzt zwei Hosts mit je 64 GiB, eine synthetische Hostreserve von 12 GiB und zwölf Gäste mit jeweils festen 4 GiB pro Host.

**Untersuchung:** Zeichne jeden Authentifizierungshop mit Protokoll, effektiver Identität und benötigter Operation. Vergleiche einen unterstützten Second-Hop-Entwurf mit CredSSP-Risiken und protokollspezifischen Delegierungsgrenzen. Prüfe erlaubte JEA-Befehle und -Parameter, Ausführungsgruppen, Überwachung und Platzierung. Erkläre, warum die Standardprivilegien eines virtuellen Kontos auf einem DC für eine eng begrenzte Dienstaufgabe auf einem Mitgliedsserver überzogen sind. Bestimme bei einem Arc-verwalteten Computer Azure-Erweiterungsbefugnisse und lokale Berechtigungen getrennt.

Erkläre Gastnetzwerk und Wiederherstellungszustand anhand von VM-, Switch-, Speicher- und Prüfpunktinventar. Vergleiche Prüfpunkte, Replica, Clustering und geschützte Sicherung nach dem jeweils abgedeckten Fehler. Erkläre Production gegenüber ProductionOnly und die Bedeutung des tatsächlichen Prüfpunktstyps. Bei der synthetischen Dimensionierung beträgt der normal zugewiesene Speicher 48 + 12 = 60 GiB pro Host. Alle 24 Gäste auf einem Host würden 96 + 12 = 108 GiB verlangen. Benenne die Annahmen und zeige, warum passende Normalbelegung keine Kapazität für den Ausfall eines Hosts belegt.

**Nachweise:** Berechtigungs- und Hopdiagramm; Prüfung des eingeschränkten Endpunkts; Switch-/Gastpfad; Speicherberechnung; tatsächliche Prüfpunktmetadaten, falls verfügbar; Plan einer unabhängigen Wiederherstellungskopie.

**Abgabe und Entscheidungspunkte:** Schlage einen unterstützten, eng begrenzten Verwaltungsentwurf und getrennte Wiederherstellungsmechanismen vor. Stoppe, wenn Delegierung eine echte privilegierte Identität offenlegen würde oder die unterstützten Konsistenzanforderungen einer VM unbekannt sind. Erfasse Endpunkteinstellungen vor der Änderung und Wiederherstellungszugriff. Lösche keine AVHDX-Dateien, behaupte nicht, Replica behebe logische Beschädigung, und bezeichne einen Prüfpunkt auf demselben Speicher nicht als unabhängige Sicherung. Ein erfolgreicher Befehl und ein sicher wiederherstellbarer Dienst benötigen unterschiedliche Validierung.

<a id="az-802-unit-3"></a>

## 3. Einen Client-Datei-Pfad durch Netzwerk und Speicher diagnostizieren

**Szenario:** Neue Unterrichtsclients erhalten keine Adresse, während alte Leases weiterlaufen. Nach einer genehmigten Netzwerkkorrektur erreicht ein Forschungsbenutzer eine Freigabe, erhält aber eine Ordnerverweigerung. Der Server ist bei Azure File Sync registriert und einige Dateien sind ausgelagert. Ein Diagramm enthält außerdem eine hybride bedingte DNS-Weiterleitung und einen unkonfigurierten zweiten DHCP-Server.

**Untersuchung:** Verfolge Client-VLAN und Relay, autorisierten DHCP-Bereich, Ausschlüsse und Reservierungen, Optionen und freie Kapazität. Definiere, was ein Test einer tatsächlich neuen Zuteilung gegenüber einem Test mit bestehendem Client ergänzt. Unterscheide einen zweiten Server von einer konfigurierten unterstützten Failoverbeziehung. Verfolge vorgesehenen Resolver, Namespace, Ziel der bedingten Weiterleitung, Rückweg und Anwendungsport. Eine korrekte DNS-Antwort belegt noch keine nutzbare SMB-Verbindung.

Erfasse danach tatsächlichen Benutzer, Freigabeautorisierung, NTFS-Vererbung und Gruppentokenkontext. Teste eine erlaubte Identität und eine, die weiter ausgeschlossen bleiben muss. Trenne bei Azure Files unterstützte Identitätseinrichtung, Freigabeautorisierung und Verzeichnis-/Dateiberechtigungen. Inventarisiere File-Sync-Endpunkte, Annahmen zum lokalen Cache, unabhängige aufbewahrte Sicherungen und ein unterstütztes Wiederherstellungsverfahren. Schließe das Wiederherstellen, Klonen oder Zurücksetzen des Betriebssystems bzw. der VM eines registrierten Servers als allgemeines File-Sync-Wiederherstellungsverfahren ausdrücklich aus.

**Nachweise:** Arbeitsblatt zur Adresszuteilung; Resolver- und Routendiagramme; Freigabe-/ACL-Beobachtungen ohne Geheimnisse; Kriterien für erlaubte und verweigerte Tests; Übersicht der Cloud-/Serverendpunkte; ausgewählter historischer Wiederherstellungspunkt mit seinen Abhängigkeiten.

**Abgabe und Entscheidungspunkte:** Erkläre Netzwerk- und Berechtigungsfehler als getrennte Befunde. Erfasse bestehenden Bereich und ACL vor jeder autorisierten Änderung. Stoppe bei überlappenden Zuteilungsbereichen, unbeabsichtigter Rechteausweitung oder ungeschützter Wiederherstellungsabhängigkeit. Erfolg verlangt, dass der vorgesehene neue Client gültige Einstellungen erhält, der vorgesehene Benutzer auf den Ordner zugreifen kann, der ausgeschlossene Benutzer blockiert bleibt und der Wiederherstellungsplan eine geschützte Kopie statt bloß eines weiteren synchronisierten Endpunkts benennt.

<a id="az-802-unit-4"></a>

## 4. Rollenspezifische Härtung ohne Verlust des Wiederherstellungszugriffs entwerfen

**Szenario:** Die Serverflotte umfasst Windows Server 2022 und 2025, Mitgliedsserver, einen DC und einen Dateiserver. Ein Vorschlag verteilt überall dieselbe OSConfig-Baseline, legt SMB über QUIC ohne Zertifikatsprüfung offen und teilt ein LAPS-Kennwort in einem Bericht. Die Entfernung der Baseline wird als vollständige Rücknahme beschrieben.

**Untersuchung:** Erstelle vor der Maßnahmenwahl eine Rollen-/Versionsmatrix. Die geprüften OSConfig-Sicherheitsbaselinehinweise richten sich an Windows Server 2025. Erfasse Modulversion, Szenario, erwartete Einstellungsunterschiede, Neustartbedarf und Konflikte mit bestehender GPO oder anderer Verwaltung. Teste die passende Rolle. Erkläre, warum das Entfernen der Verwaltung nicht als Rekonstruktion des früheren Zustands angenommen werden darf. Halte einen geschützten Ausgangszustand und einen alternativen autorisierten Verwaltungspfad vor.

Trenne bei LAPS Rotation, Sicherungsziel, erlaubten Abruf, Überwachung und Wiederherstellungszugriff. Dokumentiere gegebenenfalls DSRM-Wiederherstellungsbedingungen, ohne ein Kennwort abzurufen oder zu veröffentlichen. Prüfe für SMB über QUIC die genaue Server-/Clientunterstützung: Die geprüften Hinweise nennen Windows Server 2022 Datacenter: Azure Edition oder Windows-Server-2025-Editionen mit Windows-11-Clients. Prüfe Zertifikatsvertrauen, Namen, Nutzung des privaten Schlüssels und den erlaubten UDP-Pfad und erhalte dabei Freigabe-/Dateiautorisierung. Behandle QUIC nicht als ihren Ersatz.

**Nachweise:** Rollen-/Versionsmatrix; gewählte Maßnahmen mit Unterstützungsreferenzen; Einstellungsunterschiede und Rücknahmebedingung; erlaubte und ausgeschlossene Abrufrollen; bereinigte Zertifikatscheckliste; isolierter Plan für Tests erlaubten und verweigerten Zugriffs.

**Abgabe und Entscheidungspunkte:** Schreibe einen gestuften Änderungsvorschlag mit benannten Wiederherstellungsverantwortlichen. Stoppe, wenn die Baseline nicht unterstützt wird, der einzige Verwaltungspfad entfiele, eine Zertifikatsanforderung ungeklärt ist oder ein echtes Geheimnis in Nachweisen auftaucht. Behandle vorhandene Offenlegung von Anmeldeinformationen über das Reaktionsverfahren der Organisation. Konformitätsergebnis, installierte Funktion und nachgewiesene Durchsetzung sind getrennte Beobachtungen.

<a id="az-802-unit-5"></a>

## 5. Ein fehlendes Ereignis verfolgen und Verzeichniswiederherstellung durchspielen

**Szenario:** Ein Arc-verwalteter Server meldet „Verbunden“, AMA sendet Heartbeat, aber ein benötigtes Systemereignis existiert nur lokal. In einem gesonderten Planspiel wird ein AD-Objekt gelöscht, und der Papierkorb war vorher nicht aktiviert. Eine unterstützte Verzeichnissicherung ist vorhanden. Das Team hat ein Wiederherstellungsziel von zwei Stunden und möchte stärkere Belege als „Die VM startet“.

**Untersuchung:** Verfolge ein bereinigtes lokales Ereignis durch vorgesehene AMA-Erweiterung und Dienst, DCR, Zuordnung, Quellauswahl, Ziel und Abfragezeitraum. Erfasse Computeridentität, Ereigniszeit und Ankunftszeit getrennt. Definiere einen Test, der fehlende Quellereignisse von fehlender Sammlungskonfiguration und von einer Abfrage gegen falsche Tabelle oder falschen Arbeitsbereich unterscheidet. Erkläre, was Arc-Verbindung und Heartbeat jeweils belegen und was sie offenlassen.

Bestimme für die Verzeichniswiederherstellung betroffene Objekte und Abhängigkeiten, verfügbare unterstützte Sicherung, verantwortliche Person, geschützte DSRM-Anmeldeinformationen und angemessenen Wiederherstellungsumfang. Unterscheide Objektwiederherstellung aus dem Papierkorb, autoritative oder nicht autoritative Verzeichniswiederherstellung, SYSVOL-Wiederherstellung und Wiederherstellung der ganzen Gesamtstruktur. Wähle ein unterstütztes Verfahren für den tatsächlichen Fehler. Mache aus einem einzelnen Objektfehler keinen automatischen Controllerrollback und keine FSMO-Übernahme. Spiele Abhängigkeitsreihenfolge, Replikationsfolgen, Validierung und sichere Rückkehr wiederhergestellter Dienste durch.

**Nachweise:** Nachverfolgung von Ereignisquelle bis Ziel; Hypothesenprotokoll mit Zeitstempeln; Inventar der Wiederherstellungspunkte; vorhergesagte Wiederherstellungszeiten, klar als Schätzungen markiert; Abnahmeprüfungen für benötigtes Objekt, Authentifizierung, Replikation, Richtlinie und betroffene Anwendung.

**Abgabe und Entscheidungspunkte:** Erstelle getrennte Überwachungs- und Wiederherstellungsrunbooks. Sichere ursprüngliche DCR-/Zuordnungsnachweise vor Änderungen. Stoppe, wenn Wiederherstellungsumfang oder maßgebliche Kopie unklar ist. Halte eine Zeitlinie von Geschäftsunterbrechung und nutzbaren wiederhergestellten Daten fest, damit RTO und RPO nicht verwechselt werden. Vermerke eine Operation erst als abgeschlossen, nachdem ein autorisiertes Labor sie ausgeführt und die genannten Beobachtungen geliefert hat. Das Repository selbst behauptet weder Windows-/AD-Wiederherstellung noch ein gemessenes Zweistundenergebnis.

Beantworte zum Abschluss die [zehn Fälle](AZ-802-cases.md), ohne ihre Erklärungen zu öffnen. Bestimme bei jeder schwachen Antwort den fehlenden Nachweis oder die verwechselte Grenze und kehre zu diesem Teil des [Leitfadens](AZ-802.md) zurück. Dieses Arbeitsbuch bietet ausgewählte Übungen, keine vollständige Abdeckung aller Prüfungsziele und keine Vorhersage des Bestehens.
