# AZ-140 · 10 Fälle mit begründeten Antworten

[Leitfaden](AZ-140.md) · [Arbeitsbuch](AZ-140-workbook.md) · [Inhalt](README.md)

Eigene Szenarien für ein Universitätslabor, keine offiziellen Prüfungsfragen. Erklären Sie Anforderung und bestätigende Belege, bevor Sie jede Antwort aufdecken. Alle folgenden Ergebnisse sind Entwurfsüberlegungen; eine Cloud-Bereitstellung wird nicht behauptet.

## 1. Vierzig Studierende benötigen austauschbare Desktops, während ein Forscher dieselbe dedizierte Maschine braucht. Sollte jeder einen persönlichen Pool erhalten?

<details>
<summary>Antwort</summary>

Bewerten Sie einen gepoolten Hostpool mit unterstütztem Betriebssystem für mehrere Sitzungen für die Studierenden und persönliche Zuweisung für den Forscher. Dedizierte Maschinen für alle könnten unnötige Kapazität verbrauchen, während ein erzwungener austauschbarer Pool die Anforderung des Forschers verletzen könnte. Persönliche Zuweisung benötigt weiterhin die passende Berechtigung für die veröffentlichte Ressource. Erfassen Sie Workloadmessungen, Lizenzprüfungen, Annahmen zur Hostdichte und die Persistenzanforderung des Forschers. Ein geeigneter Belegsatz enthält Zuweisungsmodell und Kapazitätsberechnung statt nur die VM-Anzahl.

</details>

## 2. Ein Studierender besitzt Azure Contributor und sieht die VMs im Portal, aber sein AVD-Feed ist leer. Was sollten Sie untersuchen?

<details>
<summary>Antwort</summary>

Prüfen Sie Identität und Anwendungsgruppenzuweisung des Studierenden, die Zuordnung der Gruppe zum vorgesehenen Hostpool und ihre Registrierung beim Arbeitsbereich. Verwaltungszugriff auf VM-Ressourcen veröffentlicht keinen Desktop für diesen Benutzer. Prüfen Sie außerdem, ob der Client mit dem erwarteten Konto den richtigen Arbeitsbereich abonniert. Erfassen Sie Gruppenmitgliedschaft, wirksame Ressourcenberechtigung und Feeddiagnose mit Zeitstempeln. Das Öffnen eines eingehenden VM-Ports oder die Vergabe von Owner auf Abonnementebene würde die fehlende Veröffentlichungsbeziehung weder erklären noch korrigieren.

</details>

## 3. Das Projekt möchte Entra-verbundene Hosts, aber eine ältere App benötigt Domänendienste. Ist Entra ID automatisch ein Ersatz für AD DS?

<details>
<summary>Antwort</summary>

Nein. Trennen Sie die genauen Authentifizierungs- und Verzeichnisanforderungen der Anwendung von der AVD-Feed-Authentifizierung. Microsoft Entra ID, AD DS und Microsoft Entra Domain Services bieten unterschiedliche Fähigkeiten, und die Wahl eines Hostbeitritts beseitigt keine Anwendungsabhängigkeiten. Prüfen Sie unterstützte Identitätskombinationen, Profilspeicherauthentifizierung, Richtlinienverwaltung und SSO-Anforderungen, bevor Sie einen Entwurf wählen. Belege sollten ein Inventar der Anwendungsabhängigkeiten und einen unterstützten Authentifizierungsablauf enthalten. Eine Richtlinie für bedingten Zugriff allein kann kein fehlendes Domänenprotokoll oder fehlende Erreichbarkeit eines Domänencontrollers bereitstellen.

</details>

## 4. Ein Firewall-Team schlägt öffentliches TCP 3389 vor, um jede AVD-Verbindung zu reparieren. Benötigt die umgekehrte Verbindung diese Änderung?

<details>
<summary>Antwort</summary>

Nein. Die grundlegende umgekehrte AVD-Verbindung beruht auf ausgehender Dienstkonnektivität von Client und Sitzungshost über HTTPS/TCP. Prüfen Sie erforderliche Ziele, DNS, TLS, Proxyverhalten, Agentzustand und die fehlschlagende Verbindungsphase. Shortpath ist eine separate UDP-Transportwahl mit optionsspezifischen Voraussetzungen und kein Grund, RDP öffentlich freizugeben. Dokumentieren Sie für einen Entwurf mit verwaltetem Listener private Erreichbarkeit und den ausgewählten UDP-Listenerport. Die Belege sollten die tatsächlich blockierte Abhängigkeit und einen eng begrenzten Korrekturvorschlag identifizieren.

</details>

## 5. Campus-Clients verwenden UDP, aber Heim-Clients fallen auf TCP zurück. Beweist das einen Ausfall des Sitzungshosts?

<details>
<summary>Antwort</summary>

Nein. Vergleichen Sie Clients, Netzwerke und ausgewählte Shortpath-Optionen. Ein Campus-VPN könnte direkte private Erreichbarkeit bieten, während ein Heim-NAT oder eine Firewall einen bestimmten UDP-Pfad verhindert. Prüfen Sie unterstützte Clientversionen, UDP-Richtlinie, STUN/TURN-Erreichbarkeit, Cloudverfügbarkeit und ausgehandelten Transport. Der Rückfall auf die umgekehrte Verbindung kann die Sitzung erhalten, während sich die Leistung unterscheidet. Erfassen Sie Zeitstempel, Umlaufzeit, Paketverlust sowie Beobachtungen erfolgreicher und fehlgeschlagener Pfade. Nehmen Sie nicht an, der verwaltete UDP-3390-Listener sei für jede Shortpath-Verbindung über öffentliche Netzwerke nötig.

</details>

## 6. Studierende authentifizieren sich erfolgreich, erhalten aber nach einer SMB-Identitätsänderung temporäre Profile. Würde das Neuerstellen jeder VM die Ursache beheben?

<details>
<summary>Antwort</summary>

Prüfen Sie zuerst FSLogix-Einbindungsprotokolle und den Speicherauthentifizierungspfad. Verifizieren Sie erwarteten Containerort, DNS-Auflösung, Freigabeberechtigungen, NTFS-Berechtigungen, unterstützte Kerberos-Konfiguration und Verschlüsselungskompatibilität. Feed-Authentifizierung und Zugriff auf Profildateien sind getrennte Phasen. Das Neuerstellen von Hosts ohne Korrektur einer gemeinsamen Speicherabhängigkeit könnte denselben Fehler überall reproduzieren. Bewahren Sie betroffene Container auf und untersuchen Sie bestehende Sitzungen oder Sperren vor Wiederherstellungsaktionen. Die Belege sollten den genauen Einbindungsfehler und eine erlaubte Profiloperation mit der vorgesehenen Benutzeridentität zeigen.

</details>

## 7. Derselbe Studierende öffnet zwei unabhängige Sitzungen, und die zweite kann den Profilcontainer nicht einbinden. Sollte ein Operator die Sperre sofort löschen?

<details>
<summary>Antwort</summary>

Behandeln Sie die Sperre nicht als entbehrlichen Hinweis. Die standardmäßige FSLogix-Profilkonfiguration unterstützt eine einzelne Verbindung zu einem Container; gleichzeitige Konfigurationen haben zusätzliche Anforderungen und Anwendungseinschränkungen. Identifizieren Sie aktive und getrennte Sitzungen, den zugehörigen Host und den tatsächlichen Sperrzustand, bevor Sie entscheiden, ob eine verwaiste Ressource wiederhergestellt werden muss. Koordinieren Sie eine kontrollierte Abmeldung und schützen Sie ungespeicherte Arbeit. Erfassen Sie Zeitstempel und Einbindungsprotokolle. Ein Entwurf mit gleichzeitigen Sitzungen benötigt ausdrücklich unterstützte Konfiguration und Validierung statt unbeschränkter gleichzeitiger Schreibzugriffe auf denselben Container.

</details>

## 8. Der Notizeneditor erscheint in einer RemoteApp-Gruppe, schlägt aber auf der Hälfte der Hosts fehl. Installiert das Veröffentlichen des Symbols die Anwendung?

<details>
<summary>Antwort</summary>

Die Veröffentlichung einer RemoteApp steuert Zugriff und Darstellung; sie beweist nicht, dass jeder berechtigte Sitzungshost die Anwendung ausführen kann. Vergleichen Sie Image-Versionen, installierte Abhängigkeiten und die gewählte Bereitstellungsmethode. Prüfen Sie bei App Attach Paketkompatibilität, Speicherzugriff, Hostpool- und Benutzerzuweisungen sowie Registrierungsbelege. Testen Sie denselben Benutzer auf einem nachweislich funktionierenden und einem betroffenen Host, ohne Produktionszuweisungen zu ändern. Das Ergebnis sollte den Unterschied erklären und eine schrittweise Paket- oder Image-Korrektur mit funktionierender Rückfalllösung vorschlagen.

</details>

## 9. Achtundvierzig Studierende treffen gleichzeitig ein. Hosts unterstützen je zwölf Sitzungen, und ein Host darf ausfallen. Reichen vier Hosts plus Start VM on Connect?

<details>
<summary>Antwort</summary>

Vier fehlerfreie Hosts liefern unter der gemessenen Annahme genau 48 Sitzungen und lassen keine Reserve für einen Hostausfall. Fünf verfügbare Hosts liefern nach Verlust eines Hosts 48 Sitzungen. Start VM on Connect garantiert nicht, dass Reservehosts vor dem gleichzeitigen Kursbeginn fehlerfrei und bereit sind. Modellieren Sie Startzeit, maximale Sitzungen, Lastverteilung, Skalierungszeitpläne, Entleerungsausschlüsse und Profilspeicherkapazität. Belege sind eine Kapazitätstabelle für Normalbetrieb und eingeschränkten Betrieb sowie vorhergesagte Startzeiten. Validieren Sie die Dichteannahme mit repräsentativen Workloads, bevor Sie sie betrieblich verwenden.

</details>

## 10. Eine Ersatzregion besitzt VMs, trotzdem können Studierende ihre Arbeitsumgebung nicht wiederherstellen. Was fehlt der Wiederherstellungsbehauptung?

<details>
<summary>Antwort</summary>

Ein VM-Inventar allein belegt keine Desktopwiederherstellung. Verfolgen Sie Identitäts- und DNS-Verfügbarkeit, Ressourcenveröffentlichung, Anwendungsbereitstellung, Netzwerkpfade, Zugriff und Konsistenz des Profilspeichers sowie die Notizen-API. Legen Sie Wiederherstellungsziele für Profile und Anwendungsdaten getrennt fest. Verwenden Sie Verbindungskorrelations-ID, Diagnose, Hostereignisse und FSLogix-Protokolle, um die erste fehlgeschlagene Phase zu finden. Das Planspiel sollte Operatoren, Kapazitätsannahmen, Rückkehrschritte zur primären Region und einen erfolgreichen Studierendenworkflow als Abnahmebeleg festlegen. Kennzeichnen Sie diese als geplante Prüfungen, bis eine autorisierte Wiederherstellungsübung tatsächliche Beobachtungen liefert.

</details>

Technische Referenzen, Gültigkeitsdaten der Lernziele und Umfangsgrenzen stehen im [Leitfaden](AZ-140.md). Überführen Sie die Überlegungen mithilfe des [Arbeitsbuchs](AZ-140-workbook.md) in Diagramme und Belege.
