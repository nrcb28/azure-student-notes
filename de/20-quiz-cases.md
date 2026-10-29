# Acht Szenarien zum Üben

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
