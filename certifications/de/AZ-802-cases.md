# AZ-802 · 10 Fälle mit begründeten Antworten

[Leitfaden](AZ-802.md) · [Arbeitsbuch mit fünf Einheiten](AZ-802-workbook.md) · [Inhalt](README.md)

Dies sind eigene Szenarien aus einem Universitätslabor, keine offiziellen Prüfungsfragen. Formuliere eine Hypothese, eine alternative Erklärung und die benötigten Nachweise, bevor du eine Antwort öffnest. Die hier erwähnten Befehle sind vorgeschlagene Prüfungen für ein autorisiertes Windows-Labor; es wird keine Ausführung oder Wiederherstellung einer Produktionsumgebung behauptet. Jede Frage enthält das vollständige Szenario, damit Trainer und Anki-Export seinen Kontext erhalten.

## 1. Nach einer Änderung am Unterrichtsnetz kann ein Domänenclient öffentliche Websites auflösen, seinen Domänencontroller aber nicht finden. Sein Resolver ist ein öffentlicher DNS-Dienst; der konfigurierte AD-DNS-Server ist erreichbar und seine SRV-Einträge sind nachweislich in Ordnung. Die Clientzeit stimmt. Sollte die erste Reparatur alle Studierendenkennwörter zurücksetzen?

<details>
<summary>Begründung</summary>

Nein. Die vorliegenden Nachweise deuten zuerst auf den Namensauflösungspfad des Clients. Erfolgreiches öffentliches DNS belegt nicht, dass private AD-Diensteinträge gefunden werden. Erfasse den Clientresolver, die relevante SRV-Abfrage und ihr Ergebnis und vergleiche diesen Pfad mit der genehmigten Labor-DNS-Konfiguration. Eine passende Korrektur stellt den vorgesehenen AD-fähigen Resolverpfad wieder her und prüft Dienstsuche, Controllererreichbarkeit und eine betroffene Anmeldung, bevor die Änderung ausgeweitet wird.

Die Annahmen eines gesunden Servers und korrekter Zeit grenzen diese konkrete Untersuchung ein. Sie bedeuten nicht, dass jeder echte Anmeldefehler ein DNS-Problem ist. Wenn die Dienstsuche gelingt, die Authentifizierung aber weiter scheitert, fahre mit genauer Fehlermeldung, Kontostatus, Protokoll- und Sicherheitskanalnachweisen fort. Bewahre einen Vorher-nachher-Nachweis mit Zeitstempeln und tatsächlich ausgewähltem Controller auf. Alle Kennwörter zurückzusetzen würde unbeteiligten Zustand verändern, ohne die erkannte Resolverabweichung zu beheben, und könnte hilfreiche Belege verdecken. Rücknahme bedeutet, die aufgezeichnete Clientkonfiguration wiederherzustellen, falls die genehmigte Änderung andere benötigte Namensauflösung stört. Es bedeutet nicht, eine unverstandene Anordnung aus öffentlichen und privaten Resolvern zu hinterlassen.

</details>

## 2. Eine Änderung der Forschungsgruppenmitgliedschaft ist auf LAB-DC1 sichtbar, auf dem Controller des entfernten Gebäudes aber nicht. Die dortigen Clients verwenden diesen zweiten Controller, die Replikation meldet DNS-bezogene Fehler und eine neue Freigabe bleibt unzugänglich. Ist es sinnvoll, den Benutzer einer weiteren privilegierten Gruppe hinzuzufügen?

<details>
<summary>Begründung</summary>

Nein. Die beobachteten Verzeichnisversionen und der Replikationsfehler liefern eine konkrete Erklärung, die vor einer Rechteausweitung untersucht werden sollte. Erfasse Änderungszeit, annehmenden Controller, vom Client ausgewählten Controller und Replikationsfehler. Prüfe DNS-Einträge, konfigurierte Resolver, Konnektivität und Authentifizierungsvoraussetzungen der Replikationspartner. Prüfe, ob das entfernte Subnetz dem vorgesehenen Standort zugeordnet ist. Nimm aber nicht an, dass ein geänderter Standortzeitplan einen DNS-Fehler behebt.

Bestätige nach einer unterstützten Reparatur, dass genau diese Mitgliedschaftsänderung den relevanten Controller erreicht hat. Erzeuge danach einen passenden neuen Anmelde- oder Sitzungstoken für den Benutzer und teste die vorgesehene Freigabe als dieser Benutzer. Verzeichniskonvergenz und erneuerter Autorisierungskontext sind getrennte Prüfungen. Untersuche auch Freigabe- und Dateisystemberechtigungen, falls der Zugriff weiter scheitert. Halte die Gruppe eng begrenzt und protokolliere einen erlaubten und einen verweigerten Test. Eine unbeteiligte privilegierte Gruppe hinzuzufügen könnte das Symptom verdecken, während Replikation defekt bleibt und der Studierende mehr Zugriff erhält. Die Abgabe ist eine Zeitlinie der Änderungskonvergenz und des Zugriffs. Vorhergesagte Beobachtungen bleiben als solche gekennzeichnet, bis ein Labortest sie tatsächlich liefert.

</details>

## 3. Ein isolierter Unterrichtsraum in einer Außenstelle soll einen RODC nutzen. Ein Vorschlag erlaubt, dort Kennwörter privilegierter Universitätsadministratoren zwischenzuspeichern, damit diese bei WAN-Ausfällen arbeiten können. Der Raum ist physisch schlechter geschützt als das zentrale Rechenzentrum. Was muss die Entwurfsprüfung verlangen?

<details>
<summary>Begründung</summary>

Verwirf die Annahme, dass ein RODC beliebige zwischengespeicherte Anmeldeinformationen sicher macht. Prüfe seine Kennwortreplikationsrichtlinie, effektiv zugelassene und ausgeschlossene Mitgliedschaften, delegierte Verwaltung und das Verfahren bei physischem Verlust. Privilegierte Konten gehören nicht in diesen Anmeldeinformationscache der Außenstelle. Ist ein Konto nach der effektiven Richtlinie sowohl zugelassen als auch ausgeschlossen, hat die Verweigerung Vorrang. Bestimme die begrenzten gewöhnlichen Konten, die tatsächlich Zugriff ohne WAN benötigen, und prüfe die wirksame Richtlinie, statt dich allein auf einen Gruppennamen zu verlassen.

Der Plan sollte Authentifizierung zwischengespeicherter Benutzer von Operationen unterscheiden, die einen beschreibbaren Controller benötigen, darunter neue oder geänderte Verzeichniszustände. Lege fest, welche Dienste während der WAN-Unterbrechung nutzbar bleiben und wie Bedienpersonen einen genehmigten Verwaltungspfad erhalten, ohne die Domänengrenze aufzuweichen. Nachweise umfassen Bedrohungsannahmen der Außenstelle, ausgewählte Konten, effektive Cacheentscheidungen, Controllerkonnektivität und eine Reaktion auf Geräteverlust. Veröffentliche weder Kennwörter noch Cacheinhalte als Belege. Ein Wiederherstellungsplan muss betroffene zwischengespeicherte Anmeldeinformationen und den kompromittierten Server berücksichtigen, statt nur Hardware zu ersetzen und den Schutz aller Verzeichnisgeheimnisse anzunehmen.

</details>

## 4. Ein mit Azure Arc verbundener Server scheitert weiterhin an einem Remotingauftrag von Server B zu Dateiserver C. Jemand schlägt umfassende Delegierung von Anmeldeinformationen und ein standardmäßiges virtuelles JEA-Konto auf einem Domänencontroller vor. Die Aufgabe benötigt nur eine eng begrenzte Dienstoperation. Rechtfertigt die Arc-Verbindung diesen Entwurf?

<details>
<summary>Begründung</summary>

Nein. Eine Arc-Verbindung erstellt eine Azure-Verwaltungsbeziehung. Sie fügt den Server keiner AD-Domäne hinzu, erzeugt keine Gesamtstrukturvertrauensstellung und delegiert nicht automatisch die Anmeldeinformationen der interaktiven Bedienperson an C. Zeichne ersten und zweiten Hop, jeweiliges Protokoll, effektive Identität und exakt benötigte Operation. Diagnostiziere die scheiternde Autorisierungs- und Authentifizierungsgrenze. Eine erfolgreiche erste Sitzung beweist nicht, dass die zweite Ressource die vorgesehene Identität akzeptiert.

Prüfe vor der Auswahl unterstützte Second-Hop-Optionen und ihre Grenzen. CredSSP legt Anmeldeinformationen zusätzlich offen; Verfahren eingeschränkter Delegierung lösen einen zweiten WinRM-zu-WinRM-Hop nicht allgemein. Untersuche bei JEA Ausführungsidentität der Sitzung, zugelassene Benutzer, Befehle, Parameter und Prüfspur gemeinsam. Ein standardmäßiges virtuelles Konto auf einem DC kann Domänenadministratorrechte besitzen. Das ist für eine eng begrenzte Dienstaufgabe unverhältnismäßig. Bevorzuge einen passenden Verwaltungsstandort und ausdrücklich eingeschränkte Ausführungsrechte. Der Nachweis ist ein Berechtigungs- und Hopdiagramm mit erlaubten und verweigerten Operationen, kein erfolgreicher Befehl mit wiederverwendbaren Administratoranmeldeinformationen. Erweiterungsberechtigungen auf einem Arc-verwalteten Controller benötigen ebenfalls eine eigene Prüfung.

</details>

## 5. Eine Labor-VM verwendet Produktionsprüfpunkte. Die Konsistenzverarbeitung im Gast scheitert aber, und der Host erstellt einen Standardprüfpunkt. Ein Student nennt das eine unabhängige anwendungskonsistente Sicherung. Prüfpunkt und VM-Datenträger liegen auf demselben Speicher. Was muss korrigiert werden?

<details>
<summary>Begründung</summary>

Korrigiere sowohl die Konsistenzaussage als auch die Schutzgrenze. Der Produktionsmodus kann den Rückfall auf einen Standardprüfpunkt erlauben. Die gewünschte Einstellung ist deshalb ein schwächerer Beleg als tatsächlicher Prüfpunktstyp und Ergebnis der Gastverarbeitung. Wenn die Übung einen Produktionsprüfpunkt verlangt und keinen Rückfall erlaubt, prüfe ProductionOnly und behebe die Voraussetzungen der Gastintegration, von VSS oder des jeweiligen Einfrierens des Dateisystems. Dass der benötigte Prüfpunkt nicht erstellt wird, ist ein hilfreicher Fehlernachweis. Einen anderen Typ stillschweigend zu akzeptieren ist nicht gleichwertig.

Selbst ein erfolgreicher Produktionsprüfpunkt belegt keine unabhängige aufbewahrte Sicherung. Seine Datenträgerkette kann mit dem VM-Speicher verloren gehen, und Anwendungswiederherstellung benötigt weiter ein unterstütztes Konsistenz- und Wiederherstellungsverfahren. Halte eine geschützte Sicherung mit passender Aufbewahrung und einem Plan zur Wiederherstellungsprüfung vor, wenn die Anforderung dies verlangt. Untersuche Prüfpunktmetadaten und Speicherreserve mit unterstützten Werkzeugen; lösche AVHDX-Dateien nicht manuell. Erkläre getrennt, ob das Ziel die Rücknahme einer verwerfbaren Laboränderung, das Überstehen eines Host-/Speicherverlusts oder die Wiederherstellung eines früheren gültigen Anwendungszustands ist. Jedes Ziel benötigt andere Nachweise und möglicherweise einen anderen Mechanismus.

</details>

## 6. Bestehende Unterrichts-PCs arbeiten weiter, aber neue Clients erhalten keine Adressen. Der autorisierte DHCP-Server ist über ein funktionierendes Relay erreichbar; sein betroffener Bereich hat keine freien Leases. Ein zweiter Server wurde installiert, aber es besteht keine Failoverbeziehung. Welche Schlussfolgerung sollte die Untersuchung ziehen?

<details>
<summary>Begründung</summary>

Die vorliegenden Belege identifizieren einen ausgeschöpften Bereich als unmittelbares Problem für neue Zuteilungen. Bestehende Clients können gemäß ihrem Leasestatus weiterarbeiten. Ihr Erfolg beweist deshalb nicht, dass der Server eine weitere Adresse vergeben kann. Untersuche Bereichsgrenzen, Ausschlüsse, Reservierungen, aktive Leases und das tatsächliche Clientsubnetz, bevor du eine genehmigte Kapazitätskorrektur vorschlägst. Suche nach veralteten oder unerwarteten Zuteilungsmustern, lösche aber keine Leases wahllos und erweitere nicht in einen überlappenden Adressbereich.

Ein zweiter installierter Server koordiniert Leases nicht automatisch. Falls Verfügbarkeit verlangt wird, entwirf eine unterstützte DHCP-Failoverbeziehung für die vorgesehenen Bereiche und kläre Modus, Partnerstatus, Leaseverhalten und Wiederherstellungsverantwortung. Aktiviere keine konkurrierenden unverwalteten Kopien desselben Bereichs. Nachweise umfassen Bereichsinventar, Anzahl verfügbarer Adressen, Relaypfad und einen Test mit einem tatsächlich neuen sowie einem bestehenden Client. Kapazität und Failover lösen unterschiedliche Fehlerbedingungen. Eine gesunde Partnerschaft erlaubt nicht, einen zu kleinen Pool zu ignorieren. Erfasse den Bereich vor der Änderung und stoppe, wenn der vorgeschlagene Bereich mit Routing oder einer anderen Vergabestelle kollidiert.

</details>

## 7. Ein Student besitzt die vorgesehenen SMB-Freigaberechte, aber NTFS verweigert den Zugriff auf einen Projektordner. Azure File Sync ist gesund und sein Serverendpunkt enthält ausgelagerte Dateien. Würden die Azure-Rolle „Mitwirkender“ und die Bezeichnung der synchronisierten Kopie als Sicherung beide Probleme lösen?

<details>
<summary>Begründung</summary>

Nein. Folge dem tatsächlichen Windows-Dateipfad und der Identität. Die festgestellte NTFS-Verweigerung bleibt auch bei vorhandenem Freigabezugriff relevant. Korrigiere die vorgesehene Ordnerautorisierung mit passender Gruppenmitgliedschaft und Isolation. Teste dann den betroffenen Studenten und einen Studenten, dem der Zugriff weiterhin verweigert werden muss. Eine Azure-Ressourcenverwaltungsrolle repariert nicht automatisch die Dateisystem-ACL und stellt keinen SMB-Datenzugriff her. Prüfe effektiven Zugriff, statt ihn aus einem einzelnen konfigurierten Eintrag abzuleiten.

Behandle die Wiederherstellungsfrage getrennt. Gesunde Synchronisierung kann eine Löschung weitergeben, und ausgelagerte Serverdateien enthalten möglicherweise keine vollständige unabhängige lokale Kopie. Bestimme Cloudendpunkt, nutzbare aufbewahrte Sicherungen, Wiederherstellungsabhängigkeiten und den unterstützten Ablauf. Einen registrierten File-Sync-Server aus einem Betriebssystemabbild oder VM-Prüfpunkt zurückzusetzen oder zu klonen ist kein allgemein unterstütztes Wiederherstellungsverfahren. Nachweise sollten Freigabe-/NTFS-Entscheidung, Endpunkt- und Auslagerungszustand sowie einen Plan für historische Wiederherstellungspunkte enthalten. Heute wiederhergestellter Zugriff und nach einem späteren Fehler wiederherstellbare Daten sind zwei unterschiedliche Ergebnisse. Behaupte keines ohne entsprechenden Test oder ausdrücklich als Entwurf gekennzeichnete Belege.

</details>

## 8. Eine gemischte Serverflotte enthält Windows Server 2022 und 2025. Ein Härtungsvorschlag wendet überall eine OSConfig-Baseline für Windows Server 2025 an und verspricht, dass das Entfernen der Verwaltung jede alte Einstellung wiederherstellt. Außerdem speichert er ein abgerufenes LAPS-Kennwort in einem gemeinsamen Bericht. Was muss sich ändern?

<details>
<summary>Begründung</summary>

Trenne Unterstützbarkeit, Änderungsrücknahme und den Umgang mit Geheimnissen. Die geprüften OSConfig-Baselinehinweise richten sich an Windows Server 2025. Dieselbe Konfiguration sollte daher nicht als auf den 2022-Systemen unterstützt dargestellt werden. Erfasse Betriebssystem- und Modulversionen, rollenspezifische Einstellungen und eine Pilotgruppe. Bestimme bestehende GPOs oder andere Verwaltung, die Konflikte verursachen könnten, prüfe effektive Einstellungen und plane erforderlichen Neustart sowie Zugriffsprüfung. Eine Baseline zu entfernen garantiert nicht die Rekonstruktion jedes Werts vor der Verwaltung. Halte einen geprüften Ausgangszustand und ein Wiederherstellungsverfahren vor.

LAPS unterstützt kontrollierte Kennwortrotation, Sicherung und autorisierten Abruf. Ein abgerufenes Kennwort in einen breit lesbaren Bericht zu kopieren durchbricht diese Zugriffsgrenze. Entferne es über den passenden Vorfall-/Änderungsprozess, behandle die Offenlegung nach Richtlinie und rotiere es, wo erforderlich. Veröffentliche nur bereinigte Richtlinien- und Autorisierungsnachweise. Wiederherstellungsanmeldeinformationen benötigen geschützten Zugriff, der während des erwarteten Fehlers nutzbar bleibt. Nachweise sollten unterstützte Bereitstellung, zugelassene und ausgeschlossene Abrufrollen, überwachten Zugriff und einen Wiederherstellungsplan zeigen, kein Klartextgeheimnis oder einen Konformitätsscreenshot, der angeblich jeden Schutz beweist.

</details>

## 9. Ein Arc-Server zeigt „Verbunden“, und sein Arbeitsbereich enthält aktuelle Heartbeatzeilen des Agents. Die benötigten Windows-Systemereignisse fehlen aber, obwohl sie lokal vorhanden sind. Beweist die leere Abfrage, dass Windows keine Fehler erzeugt hat?

<details>
<summary>Begründung</summary>

Nein. Das Szenario sagt bereits, dass relevante Ereignisse lokal existieren. Arc-Konnektivität und Agentheartbeat sind andere Beobachtungen als die erfolgreiche Übermittlung der ausgewählten Ereignisquelle. Bestätige vorgesehenen Computer, Zeitfenster, Arbeitsbereich und Zieltabelle. Prüfe dann den Zustand der AMA-Erweiterung und des Dienstes, die zugeordnete DCR, deren Ereignisauswahl und Ziel sowie die tatsächlich beim Agent angekommene Konfiguration. Ohne passende Zuordnung zur Maschine bewirkt eine erstellte DCR noch keine Datensammlung.

Verfolge ein Ereignis anhand einer bereinigten lokalen Ereigniskennung und eines Zeitstempels durch die geplante Pipeline. Unterscheide fehlende Quelle, Sammlungsfehler, Transport-/Konfigurationsprobleme und eine Abfrage gegen das falsche Ziel. Trenne Ereigniszeit von Sammlungsankunft und berücksichtige dokumentierte Erfassungsverzögerung, ohne jede Verzögerung als akzeptabel zu behandeln. Nachweise umfassen lokalen Datensatz, Computeridentität, Zuordnung und Abfragekontext, gefolgt von einem Test der erwarteten Ankunft. Installiere nicht zuerst alle Agents neu. Das verändert Zustand und kann hilfreichen Diagnosekontext löschen, ohne fehlende Auswahl oder Zuordnung zu beheben.

</details>

## 10. Ein Student löscht ein wichtiges AD-Objekt und entdeckt, dass der Papierkorb vor der Löschung nicht aktiviert war. Er schlägt vor, einen Produktionsdomänencontroller auf einen gewöhnlichen VM-Prüfpunkt zurückzusetzen und alle FSMO-Rollen zwangsweise zu übernehmen. Die Organisation hat eine unterstützte Verzeichnissicherung und eine zuständige Wiederherstellungsperson. Wie sieht der sicherere Entscheidungsprozess aus?

<details>
<summary>Begründung</summary>

Eskaliere an das dokumentierte Verzeichniswiederherstellungsverfahren und sichere Lösch-, Replikations- und Sicherungsnachweise. Den Papierkorb nach dem Ereignis zu aktivieren erzeugt nicht nachträglich den fehlenden früheren wiederherstellbaren Zustand. Bestimme betroffenes Objekt und Abhängigkeiten, verfügbare unterstützte Sicherung und Wiederherstellungsumfang, bevor ein Verfahren gewählt wird. Ein Fehler an einem einzelnen Objekt rechtfertigt allein keine Wiederherstellung der ganzen Gesamtstruktur und keine Übernahme unbeteiligter FSMO-Rollen.

Die wiederherstellungsverantwortliche Person sollte die unterstützten autoritativen oder nicht autoritativen Schritte für den tatsächlichen Fehler wählen, einschließlich DSRM-Kontext, soweit erforderlich, geschützter Wiederherstellungsanmeldeinformationen und SYSVOL-Aspekten. Ein gewöhnlicher VM-Prüfpunktrollback ersetzt diesen Plan nicht. Dokumentiere maßgeblichen Zustand, Replikationsfolgen, Validierung und Bedingungen für die Rückkehr eines früheren Rolleninhabers, falls eine erzwungene Übernahme wirklich erforderlich ist. Prüfe Verzeichnisobjekte, Authentifizierung, Replikation und betroffenen Dienst, statt bei „Die VM startet“ aufzuhören. In diesem Repository besteht die Abgabe aus einem Planspiel mit ausdrücklichen Entscheidungspunkten. Es wurden weder Verzeichniswiederherstellung noch Rollenübernahme oder gemessene Wiederherstellung ausgeführt.

</details>

Nutze die technischen Referenzen und Versionsbedingungen im [Leitfaden](AZ-802.md). Entwickle Nachweise und kontrollierte Änderungsentscheidungen im [Arbeitsbuch](AZ-802-workbook.md).
