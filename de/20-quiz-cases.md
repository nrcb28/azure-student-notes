# 32 Szenarien zum Üben

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

Dies ist eine kleine Übung mit eigenen Fragen, keine offizielle oder vollständige Prüfung und keine Vorhersage deines Prüfungsergebnisses.

<a id="quiz-q01"></a>

## AZ-900 · Kontrolle über die Rechenumgebung

Eine Laboranwendung muss einen eigenen Linux-Kerneltreiber installieren. Welche Hostingoption erfüllt diese Anforderung am besten?

- **A.** Die Anwendung in Microsoft 365 ausführen.
- **B.** Eine Azure-VM mit einem kompatiblen Linux-Image verwenden.
- **C.** Die Anwendung in einer verwalteten App-Service-Laufzeit bereitstellen.
- **D.** Den Treiber in eine gewöhnliche Azure Function aufnehmen.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Eine Azure-VM mit einem kompatiblen Linux-Image verwenden.**

Entscheidend ist die Kontrolle über das Gastbetriebssystem. Mit einer passenden Azure-VM kann das Team dieses System und seine Treiber verwalten. Dafür bleibt auch die Betriebssystemwartung beim Team. Eine verwaltete Anwendungsplattform passt hier nicht, wenn sie den erforderlichen Zugriff auf den Kernel nicht bietet.

- **A.** Microsoft 365 bietet fertige Software und keinen Host für beliebige Kerneltreiber.
- **C.** Eine verwaltete App-Service-Laufzeit bietet nicht die erforderliche Administration des Gastkernels.
- **D.** Eine gewöhnliche Function gewährt nicht die benötigte Kontrolle über Kerneltreiber.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [Zum Nachlesen](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · Horizontale Skalierung und Sitzungen

Eine API für Lernnotizen erhält weitere Instanzen hinter einem Lastenausgleich. Jede Instanz kann ersetzt werden, die Benutzersitzungen müssen aber erhalten bleiben. Bisher liegen die Sitzungen nur im Arbeitsspeicher der jeweiligen Instanz. Was sollte sich ändern?

- **A.** Die CPU-Leistung jeder Instanz erhöhen.
- **B.** Die Sitzungen im Arbeitsspeicher behalten und nur Sitzungsaffinität aktivieren.
- **C.** Den Sitzungszustand in einen geeigneten gemeinsamen externen Speicher verlagern.
- **D.** Jeder Instanz eine öffentliche IP-Adresse geben.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Den Sitzungszustand in einen geeigneten gemeinsamen externen Speicher verlagern.**

Bei horizontaler Skalierung werden Anfragen auf mehrere Instanzen verteilt. Wichtiger Sitzungszustand darf deshalb nicht allein vom Arbeitsspeicher einer Instanz abhängen. Ein geeigneter externer Speicher ermöglicht auch Ersatzinstanzen den Zugriff. Sitzungsaffinität allein rettet keine Daten aus einer verschwundenen Instanz. Die Anwendung muss außerdem Zugriffe und Ausfälle des externen Zustandsdienstes behandeln.

- **A.** Mehr CPU erhält den Arbeitsspeicher einer ersetzten Instanz nicht.
- **B.** Auch mit Sitzungsaffinität geht die Sitzung verloren, wenn die zugeordnete Instanz verschwindet.
- **D.** Öffentliche IP-Adressen stellen keinen gemeinsamen oder dauerhaften Sitzungsspeicher bereit.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [Zum Nachlesen](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · Zugriff auf Speicherdaten

Ein Benutzer hat Contributor für ein Speicherkonto. Eine Blob-Anfrage mit seiner Entra-Identität erreicht den Dienst, wird aber wegen einer fehlenden Datenberechtigung abgelehnt. Der Benutzer muss nur Blobs in einem Container lesen. Welche Maßnahme erfüllt das Prinzip der geringsten Rechte?

- **A.** Storage Blob Data Reader im Gültigkeitsbereich dieses Containers zuweisen.
- **B.** Owner für das gesamte Abonnement zuweisen.
- **C.** Alle eingehenden Netzwerkports öffnen.
- **D.** Dem Benutzer den Schlüssel des Speicherkontos geben.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Storage Blob Data Reader im Gültigkeitsbereich dieses Containers zuweisen.**

Verwaltungsberechtigungen und Berechtigungen für Blob-Daten sind getrennt. Storage Blob Data Reader erlaubt das benötigte Lesen; der Container als Gültigkeitsbereich begrenzt die Freigabe auf den konkreten Bedarf. Im Szenario ist eine fehlende Datenberechtigung bereits als Ursache benannt. Weitreichende Verwaltungsrechte oder unpassende Netzwerkänderungen lösen das Problem nicht angemessen.

- **B.** Owner auf Abonnementebene geht weit über das Lesen eines Containers hinaus.
- **C.** Offene Ports erteilen keine fehlende Datenberechtigung.
- **D.** Ein Kontoschlüssel ermöglicht einen viel breiteren Zugriff als erforderlich.

[Quelle](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [Zum Nachlesen](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · Vererbte RBAC-Berechtigungen

Ein Benutzer hat Reader direkt für eine VM und zusätzlich über eine Gruppe, der Reader auf Abonnementebene zugewiesen ist. Du entfernst nur die direkte VM-Zuweisung. Der Benutzer kann die VM weiterhin lesen. Warum?

- **A.** Azure gibt automatisch allen Benutzern Reader für sämtliche VMs.
- **B.** Ein Tag der Ressourcengruppe stellt die gelöschte Zuweisung wieder her.
- **C.** Zum Entfernen einer Rolle muss immer die VM gelöscht werden.
- **D.** Die Gruppenzuweisung gewährt weiterhin geerbten Zugriff.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Die Gruppenzuweisung gewährt weiterhin geerbten Zugriff.**

Das Entfernen einer Zuweisung entfernt keine Berechtigungen aus anderen Zuweisungen. Die Gruppe besitzt Reader auf Abonnementebene; ihre Mitglieder können diesen Zugriff auf die VM erben. Prüfe direkte Zuweisungen, Gruppenmitgliedschaften und übergeordnete Gültigkeitsbereiche, bevor du einen Dienstfehler annimmst oder weitere Rechte vergibst.

- **A.** Es gibt keine allgemeine Reader-Zuweisung für alle Benutzer.
- **B.** Tags ordnen Ressourcen ein und legen keine Rollenzuweisungen erneut an.
- **C.** Eine Rolle lässt sich entfernen, ohne die geschützte Ressource zu löschen.

[Quelle](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [Zum Nachlesen](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · Wiederherstellungsziele

Ein Entwurf erzeugt nur einmal alle 24 Stunden einen erfolgreich wiederherstellbaren Datenbankstand. Nach einer Katastrophe darf das Unternehmen künftig höchstens die Daten der letzten Stunde verlieren. Welche Änderung schließt diese Lücke unmittelbar?

- **A.** Die CPU-Leistung des API-Servers erhöhen.
- **B.** Wiederherstellbare Sicherungsstände mit höchstens einer Stunde Abstand vorsehen und die Wiederherstellung prüfen.
- **C.** Ein Budget mit Kostenwarnung hinzufügen.
- **D.** Die Ressourcengruppe in production umbenennen.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Wiederherstellbare Sicherungsstände mit höchstens einer Stunde Abstand vorsehen und die Wiederherstellung prüfen.**

Das RPO beschreibt den zulässigen Verlust aktueller Daten als Zeitspanne. Tägliche Wiederherstellungspunkte allein erfüllen kein Ziel von einer Stunde. Der Datensicherungsentwurf muss ausreichend häufig wiederherstellbare Zustände erzeugen, und die Wiederherstellung muss überprüft werden. Schnellere Anwendungsserver oder Kostenbezeichnungen ändern das Alter der verfügbaren Wiederherstellungsdaten nicht.

- **A.** Mehr API-CPU erzeugt keine häufigeren geschützten Datenstände.
- **C.** Ein Budget warnt vor Ausgaben und nicht vor Datenverlust.
- **D.** Der Name der Ressourcengruppe verändert die Häufigkeit der Wiederherstellungspunkte nicht.

[Quelle](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [Zum Nachlesen](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · Privates DNS

Der öffentliche Zugriff auf einen Speicherdienst ist deaktiviert und ein privater Endpunkt vorhanden. Der Client löst den Dienstnamen weiterhin zur öffentlichen IP-Adresse auf. Der private Netzwerkpfad ist ansonsten verfügbar. Was solltest du zuerst untersuchen?

- **A.** Dem Client Owner auf Abonnementebene geben.
- **B.** Die öffentliche IP-Adresse dauerhaft fest eintragen.
- **C.** Die privaten DNS-Zonen, Verknüpfungen und Weiterleitungen, die dieser Client nutzt.
- **D.** Die Anzahl der Anwendungswiederholungen unbegrenzt erhöhen.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Die privaten DNS-Zonen, Verknüpfungen und Weiterleitungen, die dieser Client nutzt.**

Der Client ermittelt das falsche Ziel für die gewünschte private Verbindung. Prüfe die für den Dienst empfohlene private DNS-Konfiguration und wie der Client sie erreicht, einschließlich Verknüpfungen und Weiterleitungen. Verwende weiterhin den Dienstnamen. Eine DNS-Korrektur erteilt noch keine Datenberechtigung; zusätzliche Rechte oder endlose Wiederholungen beheben diese falsche Namensauflösung jedoch nicht.

- **A.** Owner ändert die Namensauflösung des Clients nicht.
- **B.** Nach dem Abschalten des öffentlichen Zugriffs ist die öffentliche Adresse das falsche Ziel.
- **D.** Wiederholte Anfragen korrigieren keine beständig falsche DNS-Konfiguration.

[Quelle](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Zum Nachlesen](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · Getestete Artefakte weitergeben

Eine Pipeline testet ein Container-Image und baut für die Produktion anschließend erneut aus dem Quellcode, wobei sich Abhängigkeiten ändern können. Wie stellt das Team sicher, dass die Produktion genau das getestete Image erhält?

- **A.** Nur die Kommentare im Quellcode erneut prüfen.
- **B.** Das Tag latest verwenden, ohne das zugehörige Image festzuhalten.
- **C.** Tests auslassen, weil der Quellcode-Commit unverändert ist.
- **D.** Dasselbe getestete Image weitergeben und es über einen unveränderlichen Digest identifizieren.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Dasselbe getestete Image weitergeben und es über einen unveränderlichen Digest identifizieren.**

Derselbe Quellcode-Commit kann bei geänderten Werkzeugen, Abhängigkeiten oder Basis-Images unterschiedliche Ergebnisse liefern. Wer das bereits getestete Image weitergibt, vermeidet diese Abweichung durch einen Neubau. Ein unveränderlicher Digest identifiziert das tatsächliche Artefakt, während ein Tag verschoben werden kann. Die Umgebungskonfiguration muss trotzdem gesondert geprüft und kontrolliert verwaltet werden.

- **A.** Quellcodekommentare identifizieren das gebaute Artefakt nicht.
- **B.** Ein veränderliches Tag kann später auf ein anderes Image zeigen.
- **C.** Ein unveränderter Commit belegt kein identisches Ergebnis eines erneuten Builds.

[Quelle](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [Zum Nachlesen](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · Signale für Canary-Bereitstellungen

Eine Canary-Version zeigt normale CPU- und Speicherauslastung, liefert beim Herunterladen von Dokumenten aber falsche Dateien. Worauf sollte die Entscheidung über die weitere Bereitstellung beruhen?

- **A.** Auf Signalen zur fachlichen Korrektheit und einem festgelegten Abbruch- oder Rollback-Kriterium.
- **B.** Nur auf der CPU, denn gesunde Infrastruktur beweist korrekte Ergebnisse.
- **C.** Auf einer größeren VM, bevor die gelieferten Dateien geprüft werden.
- **D.** Auf dem Löschen alter Protokolle, damit das Dashboard aufgeräumter aussieht.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Auf Signalen zur fachlichen Korrektheit und einem festgelegten Abbruch- oder Rollback-Kriterium.**

Eine Version kann ressourcenschonend laufen und trotzdem fachlich falsche Ergebnisse liefern. Die Freigabe braucht Signale zum tatsächlichen Benutzervorgang und nicht allein zur Infrastrukturauslastung. Eine festgelegte Abbruch- oder Rollback-Regel macht diese Beobachtungen handlungsfähig. Prüfe auch die Datenkompatibilität: Ein Code-Rollback macht schädliche Datenänderungen der Version nicht automatisch rückgängig.

- **B.** CPU und Arbeitsspeicher beweisen nicht, dass Benutzer die richtigen Dokumente erhalten.
- **C.** Mehr Rechenleistung korrigiert falsche Anwendungsergebnisse nicht automatisch.
- **D.** Das Löschen von Belegen erschwert die Untersuchung und korrigiert keine Ergebnisse.

[Quelle](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [Zum Nachlesen](12-devops.md)

</details>

<a id="quiz-q09"></a>

## DP-900 · Transaktionale Workloads

Ein Anmeldedienst der Universität muss den letzten freien Laborplatz reservieren und die Anmeldung der studierenden Person als einen konsistenten Vorgang anlegen. Welche Art von Arbeitslast passt am besten zu dieser Anforderung?

- **A.** Eine analytische Arbeitslast, die Anmeldungen nach Semester zusammenfasst.
- **B.** Eine Batcharbeitslast, die unabhängige Änderungen der Platzzahlen jede Nacht abgleicht.
- **C.** Eine transaktionale Arbeitslast, die die zusammengehörigen Änderungen gemeinsam bestätigt.
- **D.** Eine Streamingarbeitslast, die getrennte Ereignisse für Platz und Anmeldung veröffentlicht, ohne deren Bestätigung zu koordinieren.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Eine transaktionale Arbeitslast, die die zusammengehörigen Änderungen gemeinsam bestätigt.**

Gefordert ist ein kleiner, gezielter Vorgang, dessen zusammengehörige Änderungen gemeinsam erfolgreich sein oder scheitern müssen. Das ist transaktionales Verhalten: Eine andere Anfrage darf nicht denselben letzten Platz reservieren, während Anmeldung und Kapazitätsdaten widersprüchlich sind. Historische Berichte gehören zu analytischen Aufgaben mit anderen Zugriffsmustern. Ereignisse und spätere Abgleiche können Teil einer umfassenderen Architektur sein; unabhängige Änderungen allein erfüllen aber nicht die geforderte Konsistenz.

- **A.** Die Zusammenfassung nach Semester beantwortet historische Fragen. Sie koordiniert nicht die Reservierung und Anmeldung für diese laufende Anfrage.
- **B.** Ein nächtlicher Abgleich lässt einen Zeitraum zu, in dem Platzzahl und Anmeldung nicht übereinstimmen. Das widerspricht der geforderten sofortigen Konsistenz.
- **D.** Ereignisse können andere Systeme informieren. Getrennt bestätigte Ereignisse machen die beiden ursprünglichen Änderungen aber nicht von selbst atomar.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing) · [Zum Nachlesen](../certifications/de/DP-900.md)

</details>

<a id="quiz-q10"></a>

## DP-900 · Reihenfolge von ETL und ELT

Ein Forschungsteam extrahiert die Download-Datensätze von gestern, entfernt ungültige Kennungen in einem Verarbeitungsdienst und lädt anschließend die bereinigten Datensätze in sein Reporting-Data-Warehouse. Welche Beschreibung passt zu dieser Reihenfolge?

- **A.** ETL, weil die Transformation vor dem Laden in das Berichtsziel erfolgt.
- **B.** ELT, weil jeder Ablauf mit einem Data Warehouse als Ziel innerhalb dieses Warehouses transformiert.
- **C.** Streaming, weil die Download-Datensätze ursprünglich aus Anwendungsereignissen stammen.
- **D.** Nur Orchestrierung, weil das Koordinieren der Schritte eine Transformation überflüssig macht.

<details>
<summary>Warum diese Antwort passt</summary>

**A. ETL, weil die Transformation vor dem Laden in das Berichtsziel erfolgt.**

ETL bedeutet: extrahieren, transformieren und dann in das vorgesehene Ziel laden. Hier werden ungültige Kennungen behandelt, bevor das Reporting-Data-Warehouse die bereinigten Datensätze erhält. Bei ELT würden die Daten zuerst geladen und anschließend mit den Verarbeitungsmöglichkeiten des Ziels transformiert. Die abgegrenzte Sammlung der gestrigen Datensätze ist eine Batcheingabe. Ein Orchestrator kann diese Aktivitäten koordinieren; Orchestrierung und Transformation bezeichnen aber unterschiedliche Aufgaben innerhalb derselben Pipeline.

- **B.** Bei ELT wird vor der Transformation im Ziel geladen. Allein die Wahl eines Data Warehouses als Ziel legt diese Reihenfolge nicht fest.
- **C.** Die Herkunft aus Ereignissen macht eine spätere Verarbeitung nicht zu Streaming. Dieser Auftrag verarbeitet eine abgegrenzte Tagessammlung statt kontinuierlich eintreffender Datensätze.
- **D.** Orchestrierung koordiniert Abhängigkeiten und Wiederherstellung. Das Entfernen ungültiger Kennungen verändert die Daten und bleibt eine eigene Transformationsaufgabe.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) · [Zum Nachlesen](../certifications/de/DP-900.md)

</details>

<a id="quiz-q11"></a>

## SC-900 · MFA-Faktorkategorien

Eine Studentin vergleicht Anmeldeverfahren. Welches Beispiel verbindet einen Wissensfaktor mit einem Besitzfaktor, wenn das Authentifizierungsgerät registriert ist und seine Bestätigung verlangt wird?

- **A.** Ein Kennwort, gefolgt von einer auswendig gewussten Antwort auf eine Sicherheitsfrage.
- **B.** Ein Universitätskennwort, gefolgt von einem anderen auswendig gewussten Dienstkennwort.
- **C.** Ein Kennwort, gefolgt von einer auswendig gewussten PIN auf derselben Website, ohne gerätegebundenen Authentifikator.
- **D.** Ein Kennwort, gefolgt von einer Bestätigung über das registrierte Authentifizierungsgerät der Studentin.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Ein Kennwort, gefolgt von einer Bestätigung über das registrierte Authentifizierungsgerät der Studentin.**

Ein Kennwort steht für etwas, das die Studentin weiß. Die Kontrolle über ein registriertes Authentifizierungsgerät liefert dagegen einen Besitzfaktor. Werden beide verlangt, verbindet das Verfahren unterschiedliche Faktorkategorien. Zwei auswendig gewusste Geheimnisse bleiben Wissensfaktoren, auch wenn ihre Zeichenfolgen unterschiedlich sind. Diese Einordnung bedeutet nicht, dass jede MFA-Methode gleich gut gegen Phishing schützt: Für die Zugriffsrichtlinie der Universität müssen auch Methodenwahl, Registrierung, Wiederherstellung und tatsächliche Durchsetzung berücksichtigt werden.

- **A.** Kennwort und auswendig gewusste Antwort sind beide Wissensfaktoren. Eine weitere Wissensabfrage fügt keinen Besitzfaktor hinzu.
- **B.** Unterschiedliche Kennwörter können Zugangsdaten trennen, bleiben aber auswendig gewusste Geheimnisse derselben Faktorkategorie.
- **C.** Die Frage schließt einen gerätegebundenen Authentifikator aus. Eine PIN als weiteres Websitegeheimnis belegt Wissen und keinen Gerätebesitz.

[Quelle](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [Zum Nachlesen](../certifications/de/SC-900.md)

</details>

<a id="quiz-q12"></a>

## SC-900 · Datenbehandlung mit Purview

Eine Universität muss Studierendenkennungen bei unterstützten Aktivitäten zum Teilen von Dokumenten erkennen und beim Zutreffen einer konfigurierten Regel vor externer Freigabe warnen oder sie einschränken. Welche Purview-Funktion erfüllt diese Anforderung am direktesten?

- **A.** Audit, das ausschließlich aufzeichnet, dass eine Freigabe stattgefunden hat.
- **B.** Data Loss Prevention mit einer passend eingegrenzten und getesteten Richtlinie.
- **C.** Aufbewahrung, die Dokumente sieben Jahre lang erhält.
- **D.** Eine Vertraulichkeitsbezeichnung namens Vertraulich ohne Schutz- oder DLP-Konfiguration.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Data Loss Prevention mit einer passend eingegrenzten und getesteten Richtlinie.**

DLP bewertet vertrauliche Informationen und passende Aktivitäten anhand konfigurierter Richtlinien und kann bei unterstützten Aktionen warnen oder sie einschränken. Die Planung muss weiterhin Speicherorte, Erkennungsbedingungen, Empfänger, Ausnahmen und die gewünschte Reaktion festlegen. Audit liefert Aktivitätsnachweise, Aufbewahrung steuert den Lebenszyklus von Inhalten, und eine Bezeichnung vermittelt eine Klassifizierung oder setzt konfigurierten Schutz um. Der Name einer Bezeichnung allein richtet die in diesem Szenario beschriebene Einschränkung externer Freigaben nicht ein.

- **A.** Audit unterstützt Untersuchungen durch das Aufzeichnen von Aktivitäten. Eine Freigabe aufzuzeichnen liefert allein noch keine verlangte Richtlinienwarnung oder Einschränkung.
- **C.** Eine festgelegte Aufbewahrungsdauer steuert den Lebenszyklus eines Dokuments, entscheidet aber nicht, ob diese externe Freigabe erfolgen darf.
- **D.** Der Name einer Bezeichnung allein konfiguriert keine Freigabeeinschränkung. Schutzfunktionen oder eine passende DLP-Richtlinie müssen das gewünschte Verhalten umsetzen.

[Quelle](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [Zum Nachlesen](../certifications/de/SC-900.md)

</details>

<a id="quiz-q13"></a>

## AZ-700 · Routing nach längstem Präfix

Eine Labor-VM hat zwei aktive effektive Routen: eine benutzerdefinierte Route 0.0.0.0/0 zu einer Netzwerkappliance und eine Systemroute 10.20.0.0/16 über VNet-Peering. Es gibt keine spezifischere Route. Welcher nächste Hop wird für 10.20.7.5 gewählt?

- **A.** VNet-Peering, weil das passende /16-Präfix spezifischer ist.
- **B.** Die Netzwerkappliance, weil benutzerdefinierte Routen immer Vorrang vor jeder Systemroute haben.
- **C.** Beide nächsten Hops, weil Azure Pakete über alle passenden Routen dupliziert.
- **D.** Kein nächster Hop, weil überlappende passende Präfixe die Routingtabelle ungültig machen.

<details>
<summary>Warum diese Antwort passt</summary>

**A. VNet-Peering, weil das passende /16-Präfix spezifischer ist.**

Azure wählt zuerst die passende Route mit dem längsten Präfix. Das Ziel gehört zu 10.20.0.0/16. Dieses Präfix ist spezifischer als 0.0.0.0/0, daher nutzt das Paket die aktive Peeringroute. Die Priorität der Routenquelle ist relevant, wenn passende Routen dieselbe Präfixlänge haben. Sie gibt einer benutzerdefinierten Standardroute keinen allgemeinen Vorrang. Die Auswahl eines nächsten Hops belegt außerdem noch keine Firewallfreigabe oder Anwendungsberechtigung.

- **B.** Die Priorität der Routenquelle setzt hier die Auswahl nach längstem Präfix nicht außer Kraft. Die benutzerdefinierte Standardroute ist weniger spezifisch als die aktive Peeringroute.
- **C.** Normales zielbasiertes Routing wählt die bevorzugte passende Route. Es kopiert ein Paket nicht an jeden nächsten Hop mit passendem Präfix.
- **D.** Überlappende Präfixe sind in Routingtabellen normal. Eine Standardroute kann neben spezifischeren Routen bestehen, ohne die Tabelle ungültig zu machen.

[Quelle](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) · [Zum Nachlesen](../certifications/de/AZ-700.md)

</details>

<a id="quiz-q14"></a>

## AZ-700 · ExpressRoute-Verschlüsselung

Eine Universität nutzt ExpressRoute und verlangt Verschlüsselung von ihrem VPN-Gerät auf dem Campus bis zu einem Azure-VPN-Gateway. Der zugrunde liegende Übertragungsweg muss weiterhin ExpressRoute sein. Welcher Entwurf erfüllt diese Grenze am direktesten?

- **A.** MACsec auf unterstützten ExpressRoute-Direct-Verbindungen aktivieren und diesen Schutz der physischen Verbindung als die gesamte Grenze vom Campus bis zum Gateway behandeln.
- **B.** Privates ExpressRoute-Peering ohne weitere Verschlüsselung nutzen, weil privates Routing alle Nutzdaten verschlüsselt.
- **C.** Einen unterstützten IPsec-Tunnel über ExpressRoute nutzen und Routing, Gatewayunterstützung und erforderlichen Durchsatz prüfen.
- **D.** TLS nur zwischen Azure-Anwendung und Datenbank aktivieren und den Weg vom Campus zum Gateway unverschlüsselt lassen.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Einen unterstützten IPsec-Tunnel über ExpressRoute nutzen und Routing, Gatewayunterstützung und erforderlichen Durchsatz prüfen.**

ExpressRoute bietet private Konnektivität, verschlüsselt Nutzdaten aber nicht automatisch. Ein unterstütztes IPsec-Overlay kann die verlangte Verbindung vom Campus-VPN-Gerät zum Azure-VPN-Gateway schützen und dabei ExpressRoute als zugrunde liegenden Weg nutzen. MACsec schützt unterstützte physische ExpressRoute-Direct-Verbindungen; das ist eine andere Schutzgrenze. Der Vorschlag muss auch Routing, unterstützte Gatewayanordnungen, Kapazität und Verhalten bei Ausfällen prüfen. Verschlüsselung allein schließt den Entwurf nicht ab.

- **A.** MACsec schützt unterstützte physische Direct-Verbindungen. Dieser Abschnitt deckt für sich nicht die gesamte verlangte Grenze vom Campusgerät bis zum Azure-Gateway ab.
- **B.** Privates Peering verändert Konnektivität und Routing, verschlüsselt die Nutzdaten auf der verlangten Verbindung vom Campus zum Gateway aber nicht automatisch.
- **D.** TLS zwischen Anwendung und Datenbank schützt einen anderen Abschnitt. Die ausdrücklich verlangte Grenze vom Campus-VPN-Gerät zum Azure-Gateway bleibt offen.

[Quelle](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption) · [Zum Nachlesen](../certifications/de/AZ-700.md)

</details>

<a id="quiz-q15"></a>

## DP-300 · SQL-Zeitpunktwiederherstellung

Um 14:20 Uhr entdeckt eine Universität ein schädliches Update in Azure SQL Database, das um 13:00 Uhr bestätigt wurde. Die Änderung hat auch das Replikat erreicht. Die automatische Sicherungsaufbewahrung umfasst 12:59 Uhr. Ziel ist dieser Zustand vor dem Update mit möglichst wenig vermeidbarem Datenverlust. Welcher Wiederherstellungsplan passt am besten?

- **A.** Das aktuelle synchronisierte Replikat zum primären System machen und annehmen, dass das bestätigte Update verschwindet.
- **B.** Den Zustand von 12:59 Uhr als neue Datenbank wiederherstellen, prüfen und die kontrollierte Neuverbindung der Anwendung sowie einen nötigen Abgleich späterer Daten planen.
- **C.** Eine zwei Tage alte aufbewahrte Sicherung wiederherstellen, obwohl der benötigte Wiederherstellungspunkt um 12:59 Uhr verfügbar ist.
- **D.** Eine Zeitpunktwiederherstellung ausführen und annehmen, dass Azure die Produktionsdatenbank überschreibt und alle Clients automatisch umleitet.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Den Zustand von 12:59 Uhr als neue Datenbank wiederherstellen, prüfen und die kontrollierte Neuverbindung der Anwendung sowie einen nötigen Abgleich späterer Daten planen.**

Die Zeitpunktwiederherstellung kann einen aufbewahrten Zustand vor der schädlichen Transaktion wiederherstellen. Bei Azure SQL Database entsteht dabei eine Datenbank. Prüfung und kontrollierte Neuverbindung der Anwendung gehören deshalb zum Wiederherstellungsplan. Auch für berechtigte spätere Aktivitäten muss ausdrücklich entschieden werden, wie sie behandelt werden. Das synchronisierte Replikat enthält das fehlerhafte Update bereits. Seine Hochstufung stellt weder den historisch korrekten Zustand noch den gewünschten Zeitpunkt wieder her.

- **A.** Das Replikat hat die bestätigte schädliche Änderung bereits erhalten. Diese aktuelle Kopie hochzustufen stellt den früheren korrekten Datenbankzustand nicht wieder her.
- **C.** Die ältere Sicherung verwirft unnötig mehr Daten, obwohl die angegebene Aufbewahrung den benötigten Zustand direkt vor dem Update mit weniger vermeidbarem Verlust ermöglicht.
- **D.** Die Zeitpunktwiederherstellung von SQL Database erstellt eine Datenbank. Das Team muss sie prüfen und die Anwendungsverbindungen steuern, statt einen automatischen Austausch anzunehmen.

[Quelle](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups) · [Zum Nachlesen](../certifications/de/DP-300.md)

</details>

<a id="quiz-q16"></a>

## DP-300 · SQL-Verschlüsselungsgrenzen

Eine Forschungsanwendung muss ausgewählte Teilnehmerwerte vor Datenbankadministratoren verbergen, die Tabellen abfragen. Nur ihr vertrauenswürdiger Client darf die Werte entschlüsseln; die Administratoren dürfen die Clientschlüssel nicht besitzen. Welcher Ansatz passt am besten zu dieser Schutzgrenze?

- **A.** TDE aktivieren und den Administratoren ihren üblichen Datenbankabfragezugriff geben.
- **B.** TLS zwischen Client und Datenbank verlangen, ohne die ausgewählten Werte an der Clientgrenze zu verschlüsseln.
- **C.** Dynamic Data Masking einsetzen und die umfassenden Abfragerechte der Administratoren beibehalten.
- **D.** Passend konfiguriertes Always Encrypted mit einem kompatiblen Client und getrennt verwalteten Schlüsseln nutzen.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Passend konfiguriertes Always Encrypted mit einem kompatiblen Client und getrennt verwalteten Schlüsseln nutzen.**

Always Encrypted ist für eine Grenze ausgelegt, bei der kompatible Clients vertrauliche Werte ver- und entschlüsseln und Schlüssel außerhalb des Zugriffs der Datenbank-Engine bleiben können. Die Universität muss Treiberunterstützung, erlaubte Operationen und getrennte Schlüsselverwaltung prüfen. TDE schützt Datenbankdateien im Ruhezustand, TLS schützt die Verbindung, und Maskierung verändert die Darstellung von Abfrageergebnissen. Diese Maßnahmen allein erfüllen die verlangte Abgrenzung gegenüber Administratoren nicht.

- **A.** TDE schützt Datenbankdateien im Ruhezustand. Administratoren mit normalen Abfragerechten können über die Datenbank-Engine weiterhin Klartextwerte erhalten.
- **B.** TLS schützt Daten während der Übertragung. Es hindert einen berechtigten Datenbankadministrator allein aber nicht daran, gespeicherte Werte abzufragen.
- **C.** Maskierung verändert die Ergebnisdarstellung für bestimmte Benutzer. Sie schafft keine kryptografische Grenze gegenüber Administratoren mit umfassenden Datenbankrechten.

[Quelle](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview) · [Zum Nachlesen](../certifications/de/DP-300.md)

</details>

<a id="quiz-q17"></a>

## AI-901 · Foundry-Clientidentität

Der Foundry-Client eines Studenten verwendet den dokumentierten Endpunkt und Bereitstellungsnamen. Für die aufrufende Workload sind aber keine Anmeldeinformationen konfiguriert. Was muss der Entwurf ergänzen, um einen berechtigten Aufrufer herzustellen?

- **A.** Den Bereitstellungsnamen durch den Modellnamen aus dem Katalog ersetzen und weiterhin keine Anmeldeinformationen verwenden.
- **B.** Unterstützte Anmeldeinformationen für die Workload konfigurieren und dieser Identität den mindestens erforderlichen Zugriff gewähren.
- **C.** Von REST auf ein SDK wechseln und den Aufrufer weiterhin nicht authentifizieren.
- **D.** Die Portal-URL eines erfolgreichen Administratorzugriffs als Berechtigungsnachweis für die Workload in den Client kopieren.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Unterstützte Anmeldeinformationen für die Workload konfigurieren und dieser Identität den mindestens erforderlichen Zugriff gewähren.**

Ein Endpunkt bestimmt, wohin eine Anfrage geht; eine Bereitstellung bestimmt das konfigurierte Modell. Beides legt nicht fest, wer aufruft. Der Client benötigt einen unterstützten Authentifizierungsmechanismus, und die daraus entstehende Identität braucht passende minimale Berechtigungen. Auch das gewählte SDK und die API-Generation müssen zusammenpassen. Geheimnisse gehören außerhalb von Notebooks und Quellcode. Der Portalzugriff eines menschlichen Administrators wird nicht automatisch auf die Anwendung übertragen.

- **A.** Katalogmodellname und Bereitstellungsname erfüllen unterschiedliche Zwecke. Diese Zeichenfolge zu ändern authentifiziert die Workload nicht und gewährt keinen Zugriff.
- **C.** Ein SDK kapselt unterstützte Anfrageverträge. Ein Wechsel der Clientbibliothek beseitigt die Authentifizierungs- und Autorisierungsanforderungen des Dienstes nicht.
- **D.** Eine Portal-URL bezeichnet einen Ort. Die authentifizierte Browsersitzung des Administrators begründet weder Identität noch Berechtigungen der getrennten Workload.

[Quelle](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [Zum Nachlesen](../certifications/de/AI-901.md)

</details>

<a id="quiz-q18"></a>

## AI-901 · Grounding und Aussagebelege

Ein Notizassistent nennt ein Abgabedatum und zitiert die richtige Vorlesungs-PDF. Der abgerufene Abschnitt definiert aber nur einen Algorithmus. Die Anwendung darf Datumsangaben nur aus zugelassenen, belegenden Textstellen beantworten. Wie sollte sie reagieren?

- **A.** Eine Textstelle abrufen, die das Datum belegt, oder erklären, dass die verfügbaren Belege nicht ausreichen.
- **B.** Das Datum akzeptieren, weil ein Zitat aus dem richtigen Dokument jede Aussage der Antwort beweist.
- **C.** Die Generierungstemperatur auf null setzen und dasselbe Datum ohne Prüfung einer weiteren Textstelle akzeptieren.
- **D.** Das Datum akzeptieren, wenn das Modell hohe Sicherheit meldet, obwohl die Textstelle es nicht belegt.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Eine Textstelle abrufen, die das Datum belegt, oder erklären, dass die verfügbaren Belege nicht ausreichen.**

Grounding verlangt Belege für die konkrete Aussage, nicht nur einen Verweis auf ein verwandtes Dokument. Die vorliegende Algorithmusdefinition belegt kein Abgabedatum. Der Abruf sollte eine zugelassene Textstelle mit dem relevanten Datum und seinen Bedingungen suchen. Andernfalls sollte der Assistent auf eine Datumsantwort verzichten. Deterministische Generierung und selbst gemeldete Sicherheit können fehlende Belege nicht erzeugen. Bei der Bewertung sollte jede folgenreiche Aussage mit dem tatsächlich zitierten Text verglichen werden.

- **B.** Ein Verweis auf das richtige Dokument kann trotzdem auf eine unpassende Textstelle zeigen. Der Dokumentname allein belegt das genannte Datum nicht.
- **C.** Eine niedrigere Temperatur verändert die Schwankungen der Generierung. Sie macht aus einer Algorithmusdefinition keinen Beleg für ein fehlendes Abgabedatum.
- **D.** Die Sicherheit des Modells kann falsch sein. Die ausdrückliche Belegregel der Anwendung verlangt weiterhin eine zugelassene Textstelle für diese konkrete Datumsangabe.

[Quelle](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [Zum Nachlesen](../certifications/de/AI-901.md)

</details>

<a id="quiz-q19"></a>

## SC-200 · Belege für SOC-Zeitlinien

Synthetische Datensätze desselben verifizierten Kontos zeigen eine E-Mail-Aktivität um 10:02 UTC, erfasst um 10:20 Uhr, und eine Anmeldung um 10:08 UTC, erfasst um 10:09 Uhr. Beide Ereignisuhren gelten als zuverlässig. Welche Aussage tragen diese Datensätze allein?

- **A.** Die Anmeldung erfolgte zuerst, weil ihr Datensatz zuerst im Arbeitsbereich ankam.
- **B.** Die E-Mail verursachte die Anmeldung und beweist eine Kompromittierung des Kontos.
- **C.** Die Ereigniszeit der E-Mail muss verworfen werden, weil ihre Erfassung verzögert war.
- **D.** Die E-Mail-Aktivität lag vor der Anmeldung. Für Kausalität und Kompromittierung sind weitere Belege nötig.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Die E-Mail-Aktivität lag vor der Anmeldung. Für Kausalität und Kompromittierung sind weitere Belege nötig.**

Die zuverlässigen Ereigniszeitstempel ordnen die E-Mail-Aktivität vor der Anmeldung ein. Erfassungszeitstempel zeigen, wann Datensätze ankamen. Unterschiedliche Sammelverzögerungen können ihre Ankunftsreihenfolge umkehren. Dass beide Datensätze zu demselben verifizierten Konto gehören, hilft bei der Korrelation. Es beweist aber weder, dass die E-Mail die Anmeldung verursachte, noch, dass eines der Ereignisse bösartig war. Die Analyse sollte beide Zeitfelder erhalten, die umliegenden Aktivitäten untersuchen und die Grenzen der Belege benennen.

- **A.** Die Erfassungsreihenfolge beschreibt die Ankunft der Daten statt die Reihenfolge der Aktivitäten. Die zuverlässigen Ereigniszeiten setzen in diesen Daten die E-Mail vor die Anmeldung.
- **B.** Ein gemeinsames Konto und eine zeitliche Abfolge rechtfertigen Untersuchungen, belegen allein aber weder Kausalität noch bösartige Aktivität oder eine bestätigte Kompromittierung.
- **C.** Eine verzögerte Erfassung macht einen zuverlässigen Ereigniszeitstempel nicht automatisch ungültig. Beide Felder sollten erhalten und die Verzögerung untersucht werden.

[Quelle](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · [Zum Nachlesen](../certifications/de/SC-200.md)

</details>

<a id="quiz-q20"></a>

## SC-200 · Idempotenz von Reaktionsaktionen

Ein Sentinel-Playbook erstellt ein Vorfallticket für die Universität, aber die Erfolgsantwort geht verloren. Eine Wiederholung könnte für dieselbe genehmigte Aktion ein weiteres Ticket erzeugen. Welche Ablaufsteuerung behandelt diesen Fehler am besten?

- **A.** Ein längeres Zeitlimit verwenden und annehmen, dass eine fehlende Antwort immer bedeutet, dass kein Ticket existiert.
- **B.** Für jede Wiederholung eine neue Aktionskennung erzeugen, damit jede Anfrage unabhängig erscheint.
- **C.** Einen Vorfall-/Aktionsschlüssel und den Ticketzustand dauerhaft speichern und bei einer Wiederholung das bestehende Ergebnis abgleichen oder wiederverwenden.
- **D.** Nur eingehende Warnungsdatensätze deduplizieren und den Schritt zur Ticketerstellung ohne Zustandsprüfung wiederholen lassen.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Einen Vorfall-/Aktionsschlüssel und den Ticketzustand dauerhaft speichern und bei einer Wiederholung das bestehende Ergebnis abgleichen oder wiederverwenden.**

Idempotenz bedeutet, dass eine Wiederholung derselben logischen Aktion das beabsichtigte Ergebnis erhält, statt eine weitere Nebenwirkung zu erzeugen. Ein dauerhafter Vorfall-/Aktionsschlüssel, gespeicherter Zustand und eine externe Ticketreferenz ermöglichen es, bestehende Arbeit bei Wiederholungen zu finden oder abzugleichen. Eine fehlende Antwort bedeutet bis zur Prüfung ein unbekanntes Ergebnis. Der Ablauf benötigt außerdem begrenzte Wiederholungen, eine verantwortliche Person und passende Rechte zur Ticketerstellung. Die Deduplizierung von Warnungen allein steuert die Aktionsausführung nicht.

- **A.** Ein längeres Zeitlimit kann manche Fehler verringern. Eine verlorene Antwort lässt aber weiterhin offen, ob das externe Ticket bereits erstellt wurde.
- **B.** Eine neue Kennung lässt die Wiederholung als neue Arbeit erscheinen. Der Ablauf kann dann die bereits versuchte logische Aktion nicht wiedererkennen.
- **D.** Warnungsdeduplizierung steuert Eingabedatensätze. Ein wiederholter nachgelagerter Schritt kann weiterhin doppelte Tickets erzeugen, wenn der Aktionsausführung eigene Zustandsprüfungen fehlen.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) · [Zum Nachlesen](../certifications/de/SC-200.md)

</details>

<a id="quiz-q21"></a>

## SC-300 · Bedingter Zugriff: Nur Bericht

Eine Universität testet eine Richtlinie für bedingten Zugriff im Modus „Nur Bericht“. Die Auswertung zeigt, dass eine Anmeldung die vorgeschlagene Gewährungsanforderung nicht erfüllen würde. Trotzdem gelingt die Anmeldung. Keine andere Richtlinie verlangt diese Maßnahme. Was erklärt das Ergebnis am besten?

- **A.** Anwendungsberechtigungen setzen eine erzwungene Ablehnung durch bedingten Zugriff immer außer Kraft.
- **B.** Die vorgeschlagene Maßnahme wurde bereits erzwungen, weil „Nur Bericht“ sie auswertet.
- **C.** „Nur Bericht“ protokolliert die Auswertung der Richtlinie, ohne ihre Gewährungsanforderung durchzusetzen.
- **D.** „Nur Bericht“ lässt den ersten fehlgeschlagenen Versuch zu und blockiert automatisch den nächsten.

<details>
<summary>Warum diese Antwort passt</summary>

**C. „Nur Bericht“ protokolliert die Auswertung der Richtlinie, ohne ihre Gewährungsanforderung durchzusetzen.**

Der Modus „Nur Bericht“ wertet die Richtlinie aus und protokolliert das vorhergesagte Ergebnis, ohne ihre Maßnahmen anzuwenden. Eine erfolgreiche Anmeldung kann deshalb neben dem Befund stehen, dass die vorgeschlagene Gewährungsanforderung bei Durchsetzung nicht erfüllt wäre. Vor einer genehmigten Einführung sollte das Team erwartete Zulassungen und Ablehnungen, betroffene Identitäten, Ausschlüsse und den Wiederherstellungszugriff für Administratoren prüfen. Anwendungsberechtigungen bilden eine eigene Autorisierungsgrenze und erklären keine tatsächlich erzwungene Ablehnung durch bedingten Zugriff.

- **A.** Eine Anwendungsberechtigung setzt eine anwendbare, erzwungene Ablehnung durch bedingten Zugriff nicht automatisch außer Kraft. Hier erklärt der Richtlinienmodus die erfolgreiche Anmeldung.
- **B.** Auswertung und Durchsetzung sind getrennt: „Nur Bericht“ zeichnet auf, was geschehen würde. Das Ergebnis beweist daher nicht, dass die Gewährungsanforderung angewendet wurde.
- **D.** „Nur Bericht“ gewährt nicht erst einen Versuch und erzwingt dann automatisch die Richtlinie. Für die Durchsetzung muss die betreffende Richtlinienkonfiguration geändert werden.

[Quelle](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · [Zum Nachlesen](../certifications/de/SC-300.md)

</details>

<a id="quiz-q22"></a>

## SC-300 · Ansprüche beim Workloadverbund

Ein Buildauftrag einer Universität nutzt Workloadidentitätsverbund. Der Tokenaustausch schlägt fehl, und der subject-Wert des externen Tokens unterscheidet sich in der Groß-/Kleinschreibung vom konfigurierten Verbund-subject. issuer und audience stimmen überein. Welche Änderung behebt diese erkannte Abweichung?

- **A.** Der Workload die Rolle „Besitzer“ für das Abonnement zuweisen und den Verbund-subject unverändert lassen.
- **B.** Den konfigurierten subject-Wert exakt an den vorgesehenen eingehenden Anspruch anpassen und anschließend die minimal nötigen Ressourcenberechtigungen der Identität gesondert prüfen.
- **C.** SCIM-Zuordnungen zur Benutzerbereitstellung für den Repositorynamen ergänzen, statt die Verbundanmeldeinformationen zu korrigieren.
- **D.** Die Lebensdauer des externen Tokens verlängern und den abweichenden subject-Wert unverändert lassen.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Den konfigurierten subject-Wert exakt an den vorgesehenen eingehenden Anspruch anpassen und anschließend die minimal nötigen Ressourcenberechtigungen der Identität gesondert prüfen.**

Verbundanmeldeinformationen vergleichen vertrauenswürdigen Aussteller, subject und audience mit der eingehenden Assertion. Diese Werte müssen einschließlich Groß-/Kleinschreibung übereinstimmen. Die beabsichtigte subject-Zuordnung zu korrigieren behebt die genannte Abweichung beim Tokenaustausch, ohne ein gespeichertes Clientgeheimnis einzuführen. Ein erfolgreicher Austausch authentifiziert die Workload, gewährt aber keinen beliebigen Ressourcenzugriff. Die entstandene Identität benötigt weiterhin separat zugewiesene, passend eingeschränkte Berechtigungen für die tatsächlichen Operationen des Builds.

- **A.** Ressourcenberechtigungen bestimmen, was eine authentifizierte Identität tun darf. Eine umfassende Rolle korrigiert keinen abweichenden Anspruch, der schon den Tokenaustausch verhindert.
- **C.** SCIM betrifft Kontobereitstellung und Attribute. Es ersetzt nicht die Prüfungen von issuer, subject und audience beim Tokenaustausch dieser Workload.
- **D.** Eine längere Lebensdauer verändert den Gültigkeitszeitraum des Tokens. Sie lässt den nach Groß-/Kleinschreibung geprüften subject-Anspruch nicht mit den Verbundanmeldeinformationen übereinstimmen.

[Quelle](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · [Zum Nachlesen](../certifications/de/SC-300.md)

</details>

<a id="quiz-q23"></a>

## AZ-140 · AVD-Profilberechtigungen

Ein Student kann seine zugewiesene gepoolte Azure-Virtual-Desktop-Sitzung starten. FSLogix erhält jedoch „Zugriff verweigert“ für seinen SMB-Profilordner. Der Zugriff auf Freigabeebene ist vorhanden, die NTFS-Berechtigungen des Ordners verweigern ihm aber den Zugriff. Welche Korrektur passt am besten zu diesen Befunden?

- **A.** Die NTFS-Berechtigungen des Ordners bei angemessener Benutzertrennung korrigieren und anschließend die Profileinbindung als dieser Student prüfen.
- **B.** Dem Studenten eine umfassendere Azure-Rolle „Mitwirkender“ für die Steuerungsebene geben, ohne die Ordnerberechtigungen zu ändern.
- **C.** Die Desktopanwendungsgruppe neu zuweisen und annehmen, dass dies auch NTFS-Profilzugriff gewährt.
- **D.** Den Sitzungshost neu bereitstellen und dabei denselben Profilpfad sowie die verweigernden NTFS-Berechtigungen beibehalten.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Die NTFS-Berechtigungen des Ordners bei angemessener Benutzertrennung korrigieren und anschließend die Profileinbindung als dieser Student prüfen.**

Der SMB-Profilzugriff hängt sowohl vom Zugriff auf Freigabeebene als auch von Dateisystemberechtigungen ab. Der Befund nennt eine NTFS-Verweigerung. Den vorgesehenen Ordnerzugriff zu korrigieren und dabei die Trennung anderer Studierender zu erhalten behebt daher den unmittelbaren Fehler. Mit der betroffenen Identität testen und die FSLogix-Nachweise zur Profileinbindung prüfen. Desktopzuweisung und Azure-Ressourcenverwaltung sind andere Berechtigungsgrenzen: Ein erfolgreicher Sitzungsstart belegt kein Lese- und Schreibrecht für das dauerhafte Profil.

- **B.** Eine Verwaltungsrolle der Steuerungsebene korrigiert für sich nicht die festgestellte NTFS-Verweigerung auf dem SMB-Ordner für das Studentenprofil.
- **C.** Die Anwendungsgruppenzuweisung stellt dem Benutzer den Desktop bereit. Sie gewährt allein keinen erforderlichen Dateisystemzugriff auf den Profilspeicher.
- **D.** Wenn derselbe verweigerte Ordnerzugriff bestehen bleibt, lässt auch ein neuer Host den festgestellten Speicherberechtigungsfehler im Sitzungspfad bestehen.

[Quelle](https://learn.microsoft.com/en-us/fslogix/how-to-configure-storage-permissions) · [Zum Nachlesen](../certifications/de/AZ-140.md)

</details>

<a id="quiz-q24"></a>

## AZ-140 · AVD-Reserve bei Ausfällen

Ein synthetisches AVD-Labor benötigt 60 gleichzeitige Studentensitzungen. Tests erlauben höchstens 10 Sitzungen je gesundem Host. Alle Hosts müssen vor Unterrichtsbeginn bereit sein, und auch nach dem Ausfall eines beliebigen Hosts müssen 60 Sitzungen möglich bleiben. Wie viele bereite Hosts sind mindestens nötig?

- **A.** Sechs Hosts.
- **B.** Fünf Hosts.
- **C.** Acht Hosts.
- **D.** Sieben Hosts.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Sieben Hosts.**

Für die gemessene normale Nachfrage sind sechs gesunde Hosts nötig: 60 geteilt durch 10 Sitzungen pro Host. Ein zusätzlicher bereiter Host liefert die verlangte Reserve für einen Hostausfall; danach bleiben sechs Hosts übrig. Unter diesen ausdrücklichen Annahmen sind sieben daher das Minimum. Der reale Skalierungsplan muss außerdem Startzeit, Entleerungsstatus, fehlerhafte Kapazität, Speicherlast bei Anmeldungen und Berechtigungen berücksichtigen. Einen angehaltenen Host erst später zu starten erfüllt „vor Unterrichtsbeginn bereit“ nicht.

- **A.** Sechs Hosts decken die Nachfrage nur, solange alle gesund bleiben. Nach einem Ausfall reichen sie bei der gemessenen Grenze nur für 50 Sitzungen.
- **B.** Fünf Hosts bieten bereits vor einem Ausfall nur 50 Sitzungen. Sie können unter den genannten Annahmen keine 60 gleichzeitigen Studierenden unterstützen.
- **C.** Acht Hosts erfüllen die Anforderung, aber schon sieben lassen nach einem Ausfall sechs gesunde Hosts übrig. Acht liegt deshalb über dem Minimum.

[Quelle](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan) · [Zum Nachlesen](../certifications/de/AZ-140.md)

</details>

<a id="quiz-q25"></a>

## AI-103 · Berechtigungsentzug beim Abruf

Ein Student verliert den Zugriff auf ein Forschungsnotizbuch. Ein Assistent hat daraus aber noch zwischengespeicherte Textstellen. Die Richtlinie verlangt aktuellen Zugriff, bevor irgendeine Textstelle das Modell erreicht. Die Anwendung kann nicht feststellen, ob die Berechtigungsprüfung aktuell ist. Welches Verhalten erfüllt die Richtlinie?

- **A.** Die zwischengespeicherte Textstelle senden, aber den Quellenverweis entfernen, damit das Notizbuch ungenannt bleibt.
- **B.** Die zwischengespeicherte Textstelle bis zur nächsten geplanten Indexaktualisierung weiter ausliefern.
- **C.** Die Textstelle mit einer Anweisung senden, dass das Modell keine für den Studenten gesperrten Inhalte preisgeben darf.
- **D.** Die Textstelle zurückhalten, bis der Zugriff geprüft werden kann, und aktuelle Autorisierungsprüfungen auf Abruf- und Cacheergebnisse anwenden.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Die Textstelle zurückhalten, bis der Zugriff geprüft werden kann, und aktuelle Autorisierungsprüfungen auf Abruf- und Cacheergebnisse anwenden.**

Die Richtlinie verlangt Autorisierung vor dem Modellzugriff, auch für zwischengespeicherte Inhalte. Wenn die Aktualität der Berechtigung nicht festgestellt werden kann, erhält das Zurückhalten der Textstelle diese Grenze. Die Anwendung muss den gewählten Abruf- und Cacheentwurf gegen Berechtigungsentzug, Gruppenänderungen und veraltete Indizes prüfen. Eine Anweisung oder ein fehlender Quellenverweis kann die Offenlegung einer unzulässigen Textstelle gegenüber dem Modell nicht rückgängig machen. Native Berechtigungsfunktionen und benutzerdefinierte Filter benötigen eigene Funktions- und Durchsetzungsprüfungen.

- **A.** Das Entfernen des Quellenverweises verändert die Darstellung. Der unzulässige Notizbuchinhalt würde trotzdem das Modell erreichen und für die Antwortgenerierung verfügbar bleiben.
- **B.** Eine geplante Aktualisierung lässt eine Zugriffslücke, die der verlangten aktuellen Berechtigung widerspricht, besonders wenn zwischengespeicherte Textstellen Indexänderungen überdauern.
- **C.** Eine Anweisung delegiert die Zugriffsentscheidung nach der Offenlegung an die Generierung. Sie kann die verlangte Grenze vor dem Modellzugriff nicht durchsetzen.

[Quelle](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · [Zum Nachlesen](../certifications/de/AI-103.md)

</details>

<a id="quiz-q26"></a>

## AI-103 · Unbekannte Toolergebnisse

Ein genehmigtes Agententool fordert die Erstellung genau einer Freigabe für Forschungsnotizen an. Das Backend akzeptiert einen stabilen Vorgangsschlüssel. Die Antwort läuft jedoch in ein Zeitlimit, und die Freigabe könnte bereits existieren. Eine Statusabfrage ist verfügbar. Was sollte die Anwendung als Nächstes tun?

- **A.** Ein unbekanntes Ergebnis festhalten, den Status anhand des Vorgangsschlüssels abgleichen und denselben Schlüssel für eine gegebenenfalls unterstützte Wiederholung verwenden.
- **B.** Sofort mit einem neuen Vorgangsschlüssel wiederholen, damit das Backend die Anfrage als neue Aktion behandelt.
- **C.** Den Vorgang eindeutig als fehlgeschlagen markieren und seinen Schlüssel verwerfen, weil keine Antwort eintraf.
- **D.** Das Modell den Erfolg aus seinem früheren Toolaufruf ableiten lassen und ohne Backendprüfung den Abschluss melden.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Ein unbekanntes Ergebnis festhalten, den Status anhand des Vorgangsschlüssels abgleichen und denselben Schlüssel für eine gegebenenfalls unterstützte Wiederholung verwenden.**

Ein Zeitlimit nach dem Absenden belegt nicht, ob die Nebenwirkung eingetreten ist. Ein ausdrücklich unbekannter Zustand und ein stabiler Vorgangsschlüssel erlauben der Anwendung, das Backend abzufragen und das Ergebnis vor einem weiteren Schreibzugriff abzugleichen. Wird eine Wiederholung unterstützt, erhält derselbe logische Schlüssel die beabsichtigte Idempotenzgrenze. Genehmigung und Argumentprüfung gelten weiterhin. Der vom Modell vorgeschlagene Aufruf ist kein Beleg dafür, dass das Backend die genehmigte Freigabe tatsächlich erstellt hat.

- **B.** Ein neuer Schlüssel macht die Wiederholung zu einem eigenständigen Vorgang. Das kann eine weitere Freigabe erzeugen, wenn die erste Anfrage bereits erfolgreich bestätigt wurde.
- **C.** Keine Antwort bedeutet ein unsicheres Ergebnis und keinen sicheren Fehlschlag. Den Schlüssel zu verwerfen entfernt außerdem die verfügbare Referenz für den Abgleich.
- **D.** Der generierte Toolaufruf beschreibt die beabsichtigte Arbeit. Nur Nachweise des Backends können bestätigen, ob die verlangte Freigabe tatsächlich erstellt wurde.

[Quelle](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply) · [Zum Nachlesen](../certifications/de/AI-103.md)

</details>

<a id="quiz-q27"></a>

## DP-700 · Reihenfolge inkrementeller Löschungen

Ein Fabric-Ladeprozess für Einschreibungen verarbeitet die Quelländerungssequenz 98, die Einschreibung E löscht. Danach trifft eine verzögerte Aktualisierung für E mit Sequenz 94 ein. Die Quellsequenzen bestimmen die verbindliche Reihenfolge, und eine spätere berechtigte Neueinschreibung ist möglich. Welche Zusammenführungsregel erhält den richtigen Zustand?

- **A.** Aktualisierung 94 anwenden, weil sie zuletzt in der Pipeline angekommen ist.
- **B.** Nach einer beliebigen Löschung alle künftigen Änderungen für E dauerhaft ignorieren.
- **C.** Lösch- und Versionsinformationen für Sequenz 98 behalten, Aktualisierung 94 als älter ablehnen und eine gültige neuere Änderung zulassen.
- **D.** Den Prüfpunkt verwerfen und Änderungen strikt nach Ankunft ohne Versionsvergleich erneut abspielen.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Lösch- und Versionsinformationen für Sequenz 98 behalten, Aktualisierung 94 als älter ablehnen und eine gültige neuere Änderung zulassen.**

Die Quellsequenz bestimmt die fachliche Reihenfolge. Aktualisierung 94 darf daher keine Einschreibung wiederherstellen, die bei Sequenz 98 gelöscht wurde. Die Löschung mit ihrer Version aufzubewahren erlaubt einer idempotenten Zusammenführung, veraltete Änderungen abzulehnen und eine gültige spätere Version trotzdem anzunehmen. Die Ankunftszeit ist hier nicht maßgeblich. Stabile Schlüssel, deterministische Versionsvergleiche und dauerhaft gespeicherter Fortschritt werden gemeinsam benötigt. Eingaben ohne diese Regeln erneut auszuführen behebt das Reihenfolgeproblem nicht.

- **A.** Die Ankunftsreihenfolge kann von der Reihenfolge der Quelländerungen abweichen. Die ältere Aktualisierung würde eine durch die neuere Änderung gelöschte Einschreibung fälschlich wiederherstellen.
- **B.** Ein dauerhaftes Verbot würde auch eine gültige spätere Neueinschreibung ablehnen. Die Zusammenführung muss Versionen vergleichen, statt jede künftige Änderung für den Schlüssel zu verbieten.
- **D.** Ein erneutes Abspielen derselben Ankunftsreihenfolge ohne Versionsprüfung kann die Wiederherstellung wiederholen. Den Prüfpunkt zu entfernen schafft allein keine verbindliche fachliche Reihenfolge.

[Quelle](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-lake-change-data-feed) · [Zum Nachlesen](../certifications/de/DP-700.md)

</details>

<a id="quiz-q28"></a>

## DP-700 · Fabric-Zugriffspfade

Ein Universitätsbericht setzt Zeileneinschränkungen korrekt um und trägt eine Vertraulichkeitsbezeichnung. Derselbe Analyst kann über einen berechtigten OneLake-Pfad direkt die zugrunde liegenden Dateien mit Studentendetails lesen. Die Richtlinie erlaubt nur Modulsummen. Was sollte die verantwortliche Fachkraft ändern und prüfen?

- **A.** Die Bezeichnung in „Streng vertraulich“ umbenennen und annehmen, dass ihr Name die Zeileneinschränkungen des Berichts auch bei direkten Dateizugriffen durchsetzt.
- **B.** Den zugrunde liegenden Zugriffspfad auf die minimal erforderlichen Berechtigungen beschränken und als Analyst erlaubte Summen sowie verweigerte Details testen.
- **C.** Die Detailtabelle im Bericht ausblenden und die direkten Dateiberechtigungen des Analysten unverändert lassen.
- **D.** Eine umfassendere Arbeitsbereichsrolle vergeben, damit die bestehenden Zeileneinschränkungen des Berichts automatisch jeden Zugriffspfad regeln.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Den zugrunde liegenden Zugriffspfad auf die minimal erforderlichen Berechtigungen beschränken und als Analyst erlaubte Summen sowie verweigerte Details testen.**

Eine Einschränkung eines Berichts oder einer Abfrage-Engine gilt nicht automatisch für einen getrennten direkten Dateizugriff. Die verantwortliche Fachkraft muss Arbeitsbereichs-, Element-, Engine- und Dateiberechtigungen an die Richtlinie anpassen und jeden vorgesehenen Zugriffspfad mit der Identität des Analysten testen. Eine Vertraulichkeitsbezeichnung liefert Governancekontext oder konfigurierten Schutz. Ihr Name allein setzt aber nicht überall dieselbe Autorisierung um. Umfassendere Berechtigungen können zusätzliche Wege öffnen, statt diese Lücke zu schließen.

- **A.** Ein anderer Klassifizierungsname konfiguriert die getrennte Dateizugriffsgrenze nicht und überträgt Zeileneinschränkungen der Berichts-Engine nicht automatisch auf OneLake.
- **C.** Das Ausblenden von Berichtsinhalten ändert nur deren Darstellung. Der genannte direkte Zugriff auf die zugrunde liegenden Dateien mit Studentendetails bleibt erhalten.
- **D.** Eine umfassendere Arbeitsbereichsrolle erweitert Zugriff. Sie macht die Zeileneinschränkungen des Berichts nicht zu einer universellen Regel für jede Engine und jeden Dateipfad.

[Quelle](https://learn.microsoft.com/en-us/fabric/security/permission-model) · [Zum Nachlesen](../certifications/de/DP-700.md)

</details>

<a id="quiz-q29"></a>

## SC-100 · Verantwortung für Restrisiken

Ein Architekt dokumentiert, dass für eine geplante Notizplattform der Universität trotz umsetzbarer Maßnahmen ein erhebliches Ausfallrisiko bleibt. Das Sicherheitsteam empfiehlt die Einführung. Die Governance verlangt aber eine geschäftliche Risikoakzeptanz. Wer sollte die Annahme dieses Restrisikos genehmigen?

- **A.** Der SOC-Analyst, der das zugehörige Sicherheitsticket schließen kann.
- **B.** Die verantwortliche Person aus dem Fachbereich mit der nötigen Befugnis zur Risikoannahme; sie dokumentiert die verbleibende Gefährdung und die Bedingungen für eine erneute Prüfung.
- **C.** Der Produktanbieter, weil seine Konformitätsbewertung die Geschäftsentscheidung der Universität ersetzt.
- **D.** Der Cloudadministrator allein deshalb, weil er die Ressourcen bereitstellen kann.

<details>
<summary>Warum diese Antwort passt</summary>

**B. Die verantwortliche Person aus dem Fachbereich mit der nötigen Befugnis zur Risikoannahme; sie dokumentiert die verbleibende Gefährdung und die Bedingungen für eine erneute Prüfung.**

Auch nach Auswahl technischer Maßnahmen bleibt das Restrisiko eine geschäftliche Gefährdung. Die dafür verantwortliche und befugte Person aus dem Fachbereich sollte anhand der Architekturbelege zu Auswirkungen, Wahrscheinlichkeitsannahmen, Alternativen und verbleibenden Lücken entscheiden, ob diese akzeptabel ist. Die Entscheidung sollte Geltungsbereich, Bedingungen für eine erneute Prüfung und Verantwortung festhalten. Sicherheitsempfehlungen, Ressourcenbereitstellungsrechte und Anbieterbewertungen informieren die Entscheidung, verleihen aber nicht automatisch die von der Universität verlangte Befugnis zur Risikoannahme.

- **A.** Ein operatives Ticket schließen zu dürfen ist eine Ablaufberechtigung. Daraus folgt keine Befugnis, erhebliche geschäftliche Risiken für die Universität zu akzeptieren.
- **C.** Eine Anbieterbewertung kann die Auswahl von Maßnahmen unterstützen. Sie ersetzt nicht die rechenschaftspflichtige Entscheidung der Universität über ihr verbleibendes Betriebsrisiko.
- **D.** Ressourcen bereitstellen zu können ist eine technische Befugnis. Das Szenario verlangt zusätzlich einen befugten geschäftlichen Verantwortlichen, der das verbleibende Ausfallrisiko akzeptiert.

[Quelle](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/assess-cloud-risks) · [Zum Nachlesen](../certifications/de/SC-100.md)

</details>

<a id="quiz-q30"></a>

## SC-100 · Wiederherstellungsziele prüfen

Eine Wiederherstellungsübung setzt zwei Stunden RTO und 15 Minuten RPO fest. Ein Ausfall beginnt um 11:00 UTC. Berechtigte Dokumentlesezugriffe sind ab 12:30 Uhr wieder möglich; die Daten wurden nur bis 10:40 Uhr wiederhergestellt. Dies seien die vereinbarten Messgrenzen. Welche Bewertung stimmt?

- **A.** Beide Ziele sind erfüllt, weil der Dienst innerhalb von zwei Stunden wieder verfügbar war.
- **B.** Das RPO ist erfüllt, das RTO wurde verfehlt.
- **C.** Beide Ziele wurden verfehlt, weil jeder Datenverlust das RTO verletzt.
- **D.** Das RTO ist erfüllt, das RPO wurde verfehlt, weil der Wiederherstellungspunkt 20 Minuten vor dem Ausfall liegt.

<details>
<summary>Warum diese Antwort passt</summary>

**D. Das RTO ist erfüllt, das RPO wurde verfehlt, weil der Wiederherstellungspunkt 20 Minuten vor dem Ausfall liegt.**

Das RTO misst die zulässige Unterbrechung: Berechtigte Lesezugriffe sind nach 90 Minuten wieder möglich und liegen damit innerhalb des Zweistundenziels. Das RPO misst den zulässigen Verlust neuer Daten: Der Zustand von 10:40 Uhr bei einem Ausfall um 11:00 Uhr lässt eine Lücke von 20 Minuten, mehr als die erlaubten 15 Minuten. Beide Prüfungen sind unabhängig. Ein erfülltes Ziel erfüllt nicht automatisch das andere. Die Übung sollte beide Messwerte und die Abhängigkeiten dokumentieren, die die definierte Geschäftsoperation wieder ermöglichten.

- **A.** Die Wiederherstellung innerhalb des Zeitziels erfüllt nur das RTO. Die gesonderte Lücke von 20 Minuten bis zum Wiederherstellungspunkt überschreitet weiterhin das angegebene RPO.
- **B.** Die Unterbrechung dauert 90 Minuten und liegt innerhalb von zwei Stunden; die Datenlücke von 20 Minuten überschreitet 15 Minuten. Diese Option vertauscht die Ergebnisse.
- **C.** Das RTO betrifft die Unterbrechungsdauer, nicht die Frage, ob Daten verloren gehen. Die gemessenen 90 Minuten erfüllen es trotz verfehltem RPO.

[Quelle](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview) · [Zum Nachlesen](../certifications/de/SC-100.md)

</details>

<a id="quiz-q31"></a>

## AZ-120 · SAP-Fencing und einzelner Schreiber

Bei einer Planspielübung für einen SAP-HANA-Cluster geht die Kommunikation mit dem primären Knoten verloren. Der sekundäre Knoten kann ihn nicht isolieren (Fencing). Das Team kann nicht bestätigen, dass der primäre Knoten keine Schreibzugriffe mehr annimmt. Welche Reaktion schützt vor einer Übernahme die Datenintegrität am besten?

- **A.** Fencing deaktivieren und den sekundären Knoten hochstufen, damit das Clusterdashboard sofort laufende Ressourcen zeigt.
- **B.** Den sekundären Knoten hochstufen, weil der letzte erfolgreiche Replikationsstatus beweist, dass der alte primäre Knoten nicht mehr schreiben kann.
- **C.** Nach dem unterstützten Vorfallverfahren Fencing wiederherstellen oder prüfen und vor Schreibzugriffen nach der Übernahme die Isolation des bisherigen schreibenden Knotens bestätigen.
- **D.** Die virtuelle Dienstadresse auf den sekundären Knoten verschieben und die unklare Schreibfähigkeit des primären Knotens unverändert lassen.

<details>
<summary>Warum diese Antwort passt</summary>

**C. Nach dem unterstützten Vorfallverfahren Fencing wiederherstellen oder prüfen und vor Schreibzugriffen nach der Übernahme die Isolation des bisherigen schreibenden Knotens bestätigen.**

Ein Kommunikationsverlust beweist nicht, dass der primäre Knoten angehalten wurde. Fencing isoliert einen Knoten, der nicht sicher weiterarbeiten kann. Das schützt die Anforderung eines einzigen schreibenden Knotens und verringert Split-Brain-Risiken. Das Team muss die unterstützte Fencing- und Quorumkonfiguration untersuchen, Zustandsnachweise sichern und vor Schreibzugriffen nach der Übernahme die Isolation des bisherigen Schreibers feststellen. Replikationszustand und Adressverschiebung liefern diese Isolation nicht. Fencing zu deaktivieren entfernt einen wesentlichen Schutzmechanismus.

- **A.** Fencing zu deaktivieren entfernt den Mechanismus zur Isolation eines unklaren schreibenden Knotens. Scheinbare Verfügbarkeit kann dann konkurrierende primäre Knoten ermöglichen.
- **B.** Ein früheres Replikationsergebnis beschreibt die damalige Datenübertragung. Es beweist nicht, dass der jetzt unerreichbare primäre Knoten keine Schreibzugriffe mehr annimmt.
- **D.** Eine virtuelle Adresse zu verschieben ändert einen Clientpfad. Das hindert den alten primären Knoten allein nicht am Schreiben über andere Sitzungen oder Pfade.

[Quelle](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-hana-high-availability) · [Zum Nachlesen](../certifications/de/AZ-120.md)

</details>

<a id="quiz-q32"></a>

## AZ-120 · SAP-Schreibzugriffe nach der Umstellung

Bei einer SAP-Migration der Universität wird das Ziel für den Einkauf geöffnet, und Benutzer erstellen neue Bestellungen. Die unveränderte Quelle bleibt isoliert. Ein späteres Validierungsproblem lässt das Team einen Rollback erwägen. Welcher Plan schützt die neuen Geschäftstransaktionen am besten?

- **A.** Schreibzugriffe einfrieren, den maßgeblichen Datenzustand feststellen, Zieltransaktionen sichern und vor Wiederöffnung eines Schreibsystems einen unterstützten Abgleich oder Rückmigrationsplan vereinbaren.
- **B.** DNS auf die unveränderte Quelle zurückstellen und annehmen, dass die neuen Bestellungen des Ziels dort vorhanden sind.
- **C.** Das Ziel aus der alten Quelle überschreiben und den Einkauf wieder öffnen, ohne die nach der Umstellung erstellten Transaktionen zu identifizieren.
- **D.** Quelle und Ziel für Schreibzugriffe öffnen, während die Fachbenutzer später entscheiden, welche Bestellungen sie behalten.

<details>
<summary>Warum diese Antwort passt</summary>

**A. Schreibzugriffe einfrieren, den maßgeblichen Datenzustand feststellen, Zieltransaktionen sichern und vor Wiederöffnung eines Schreibsystems einen unterstützten Abgleich oder Rückmigrationsplan vereinbaren.**

Sobald das Ziel neue Schreibzugriffe annimmt, wird der Rollback neben einer Infrastrukturänderung auch zu einer Entscheidung über den Umgang mit Daten. Die Rückkehr zur unveränderten Quelle kann neue Bestellungen verlieren lassen; beide Seiten zu öffnen kann Transaktionen auseinanderlaufen lassen. Das Betriebshandbuch sollte Schreibzugriffe einfrieren, Nachweise und neue Geschäftsdaten sichern, einen maßgeblichen Zustand bestimmen und mit den verantwortlichen Fachbereichen einen unterstützten Abgleich oder Rücktransfer nutzen. Prüfung und Kontrolle eines einzigen Schreibsystems müssen der Wiederöffnung des Einkaufs vorausgehen.

- **B.** DNS leitet Clients um, kopiert aber keine Bestellungen nach der Umstellung in die unveränderte Quelle. Die reine Rückschaltung kann diese neuen Transaktionen verlieren lassen.
- **C.** Das Überschreiben aus der veralteten Quelle kann berechtigte Zielbestellungen zerstören. Zuerst müssen die geschäftlichen Änderungen nach der Umstellung identifiziert und gesichert werden.
- **D.** Wenn beide Landschaften Schreibzugriffe annehmen, entstehen abweichende Transaktionsverläufe. Das erschwert den Abgleich und verletzt die nötige Kontrolle eines maßgeblichen Schreibsystems.

[Quelle](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/execute-migration) · [Zum Nachlesen](../certifications/de/AZ-120.md)

</details>
