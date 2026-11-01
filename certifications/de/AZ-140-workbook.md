# AZ-140 · Gemeinsames Arbeitsbuch für Fortgeschrittene

[Leitfaden](AZ-140.md) · [10 Fälle](AZ-140-cases.md) · [Inhalt](README.md)

Fünf übereinstimmende Einheiten in allen Sprachen. Arbeiten Sie offline mit der universitären Notizen-App und einem virtuellen Computerlabor. Dokumentieren Sie Vorhersagen als Vorhersagen; diese Einheiten stellen nichts bereit, ändern keinen Mandanten und belegen keine Produktionsreife.

<a id="az-140-unit-1"></a>

## 1. Ressourcen, Benutzer und Verantwortung abbilden

Zeichnen Sie ein gepooltes Labor für 48 Studierende und einen persönlichen Desktop für einen Forscher. Identifizieren Sie Hostpools, Sitzungshosts, Anwendungsgruppen, Arbeitsbereichsregistrierung und Benutzerzuweisungen. Trennen Sie Microsofts Broker- und Gateway-Verantwortung von kundenseitigen Images, VMs, Netzwerk, Identitätsintegration und Speicher. Erklären Sie, warum unterstützter Mehrsitzungsbetrieb etwas anderes als persönliche Zuweisung ist.

**Szenario:** Ein Studierender sieht Azure-VMs, hat aber einen leeren Desktopfeed. **Belege:** ein Diagramm der Ressourcenbeziehungen, wirksame Anwendungsgruppenberechtigung, vorgesehenes Clientkonto und Lizenzannahmen. **Ergebnis:** die ersten drei Prüfungen, eine abgelehnte ungeeignete Rollenerweiterung und ein Verantwortlicher für jede kundenseitig verwaltete Abhängigkeit. Verknüpfen Sie den Entwurf mit den [Compute-Grundlagen](../../de/03-compute.md).

<a id="az-140-unit-2"></a>

## 2. Identität und Transport getrennt verfolgen

Vergleichen Sie Entra-Beitritt, AD-DS-Beitritt und Entra-Domain-Services-Beitritt mit den Anforderungen einer älteren App und der gewählten Profilspeicherauthentifizierung. Zeichnen Sie Feed-Authentifizierung, Berechtigung, Sitzungsanmeldung und Dateizugriff als getrennte Phasen. Ergänzen Sie ausgehende umgekehrte HTTPS-Verbindung und einen optionsspezifischen UDP-Shortpath-Pfad. Erklären Sie die private Erreichbarkeit des verwalteten Listeners und wie ICE/STUN oder TURN die Transportanforderungen verändern.

**Szenario:** Campusnutzer verbinden sich problemlos; Heimnutzer erhalten eine weitere Anmeldeaufforderung und langsamere Sitzungen. **Belege:** benötigte Beobachtungen zu Clientversion, Beitrittstyp, SSO- und Conditional-Access-Annahmen, ausgehandeltem Transport, DNS-Pfad und Latenz. **Ergebnis:** zwei unabhängige Hypothesen und ihre bestätigenden Tests ohne öffentliche Freigabe von TCP 3389. Wiederholen Sie die [Netzwerkgrundlagen](../../de/05-networking.md).

<a id="az-140-unit-3"></a>

## 3. Profile schützen und eine nutzbare App veröffentlichen

Entwerfen Sie dauerhafte FSLogix-Container außerhalb austauschbarer gepoolter Hosts. Dokumentieren Sie Kompatibilität von Speicheridentität und Kerberos, Freigabe- und NTFS-Berechtigungen, Kapazität, Annahmen zu Anmeldespitzen, Einzelverbindungsverhalten und Sicherungs-/Wiederherstellungsziele. Unterscheiden Sie Profilpräferenzen von maßgeblichen Notizendaten. Vergleichen Sie die Installation des Editors im Image mit einem unterstützten App-Attach-Paket und erklären Sie die RemoteApp-Veröffentlichung getrennt.

**Szenario:** Ein Studierender erreicht den Desktop, erhält aber ein temporäres Profil und kann den Editor nicht starten. **Belege:** Containereinbindungsfehler, Eigentümerschaft aktiver Sitzungen, erwartete Berechtigungen, Host-Image-Version, Paketzugriff und Zuweisungen. **Ergebnis:** ein geordneter Fehlerbaum mit getrennten Profil- und Anwendungszweigen, ein sicherer Wiederherstellungsvorschlag und Kriterien zum Schutz bestehender Benutzerarbeit.

<a id="az-140-unit-4"></a>

## 4. Images veröffentlichen und Unterrichtskapazität berechnen

Schreiben Sie einen versionierten Golden-Image-Releaseplan mit unterstütztem Betriebssystem, Agenten, Sicherheitsrichtlinie, Anwendungen, Validierungsnutzern, Entleerungsverhalten und Rollback. Berechnen Sie bei einer gemessenen Grenze von 12 Sitzungen pro Host die Kapazität für 48 Studierende bei einem Hostausfall. Unterscheiden Sie die gewählte Methode eines Skalierungsplans von Start VM on Connect; beziehen Sie Startzeit, Zustand, maximale Sitzungen und Speichergrenzen ein.

**Szenario:** Vor dem Unterricht erscheint ein Patch, während ein Host bereits nicht verfügbar ist. **Belege:** eine Kapazitätstabelle mit fünf Hosts, Image-Versionen, Validierungscheckliste, aktive Sitzungen und Wartungsausschlüsse. **Ergebnis:** eine schrittweise Einführung, die ausreichende nutzbare Kapazität erhält, mit Rollback-Auslösern und einer ausdrücklichen Richtlinie für beim Herunterfahren noch verbundene Benutzer.

<a id="az-140-unit-5"></a>

## 5. Ein Planspiel für Anmeldefehler und Wiederherstellung durchführen

Verfolgen Sie eine synthetische Verbindung anhand von UTC-Zeitstempeln, pseudonymem Benutzer, Ressource, Host und Korrelations-ID. Legen Sie Diagnoseeinstellungen, Erfassung der Hostleistung, FSLogix-Protokolle und erforderliche Beobachtungen zum Nutzungserlebnis fest. Erklären Sie, warum ein Versuch, der AVD nie erreicht, keinen Verbindungsdatensatz hinterlassen muss. Ergänzen Sie einen Wiederherstellungsplan für eine Ausweichregion um Identität, DNS, App-Pakete, Profile und Abhängigkeiten der Notizen-API.

**Szenario:** Der Kurs um 09:00 kann nach einem Speicherausfall keine Profile wiederherstellen. **Belege:** vorhergesagte Prüfpunkte, Vergleich mit einer normalen Sitzung, Profilwiederherstellungsziele, verfügbare Kapazität und Verantwortliche für laufende VM-, Datenträger-, Speicher-, Netzwerk-, Überwachungs- und Lizenzkosten. **Ergebnis:** eine Vorfallzeitleiste, eine Hypothese zur ersten Fehlerstelle, Kriterien für Wiederherstellung und Rückkehr in die primäre Region sowie eine klare Grenze zwischen Planspielvorhersagen und beobachteten Tests.

Nutzen Sie die sechs technischen Referenzen im [Leitfaden](AZ-140.md), um Annahmen zu hinterfragen. Diese Übungen sind eigenes Lernmaterial, decken nicht jedes offizielle Lernziel ab und garantieren kein Prüfungsergebnis.
