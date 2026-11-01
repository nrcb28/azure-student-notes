# SC-300 · Arbeitsbuch für Zugriffsentscheidungen und Governance

[Leitfaden](SC-300.md) · [Zehn Fälle](SC-300-cases.md) · [Inhalt](README.md)

Fünf eigene Offline-Einheiten für eine fiktive universitäre Notizen-App. Verwenden Sie synthetische Identitäten und Dokumente. Ändern Sie keine Mandantenrichtlinien, erstellen Sie keine Anmeldeinformationen, aktivieren Sie keine Rollen und verbinden Sie keine echte Telemetrie. Die Ergebnisse beschreiben erwartete Entscheidungen; eine Cloud-Ausführung wird nicht behauptet.

<a id="sc-300-unit-1"></a>

## 1. Wirksamen Zugriff und Identitätsquellen nachverfolgen

Bilden Sie Mandant, Abonnement, App und Dokumentenspeicher ab. Trennen Sie Verzeichnisrollen, Umfang administrativer Einheiten, Azure-Ressourcen- und Datenrollen sowie Anwendungsberechtigungen. Beziehen Sie direkte und gruppenbasierte Gewährungspfade ein und identifizieren Sie, wer die Mitgliedschaft steuert. Notieren Sie für eine hybride Identität die maßgebliche Quelle und die gewählten Annahmen zu Synchronisierung und Authentifizierung; behandeln Sie Synchronisierung nicht als Zugriffsgewährung.

**Szenario:** Ein Studierender verliert eine direkte Zuweisung, kann aber weiterhin einen Kursordner lesen. **Belege:** ein Diagramm mit zwei möglichen Gewährungspfaden und den Datensätzen, die zur Unterscheidung nötig sind. **Ergebnis:** eine Zugriffsentscheidungsmatrix mit sechs Zeilen für Studierenden, Gast, Redakteur, Administrator, Indexierer und ehemaliges Mitglied, jeweils mit minimalem Umfang und einer erwarteten Verweigerung.

<a id="sc-300-unit-2"></a>

## 2. Authentifizierung und bedingten Zugriff entwerfen

Legen Sie eine unterstützte Authentifizierungsmethode, einen Registrierungsweg und einen Wiederherstellungsverantwortlichen fest. Erklären Sie Phishingresistenz und wo ein Temporary Access Pass einem berechtigten Benutzer den Einstieg ermöglichen könnte, ohne einen echten Passcode zu speichern. Beschreiben Sie Richtlinienziele, Bedingungen, Gewährungs- und Sitzungssteuerungen, Ausschlüsse, Lizenzannahmen und Notfallwiederherstellung. Halten Sie Bewertungen im Modus „Nur Bericht“ von erzwungenen Ergebnissen getrennt.

**Szenario:** Ein Gastdozent nutzt ein privates Gerät, während ein Redakteur unveröffentlichte Lösungen bearbeitet. **Belege:** drei erwartete Anfragen mit unterschiedlichen Identitäten, Methoden, Geräten oder Ressourcen; erklären Sie das Vertrauen in mandantenübergreifende Claims getrennt von App-Berechtigungen. **Ergebnis:** eine vorgeschlagene Richtlinienmatrix und eine Einführungsnotiz mit Kriterien für Pilot, Überprüfung, Wiederherstellung und Rollback. In einem echten Mandanten wird nichts aktiviert.

<a id="sc-300-unit-3"></a>

## 3. Workloadidentitäten auswählen und begrenzen

Vergleichen Sie eine App-Registrierung, ihren Dienstprinzipal und eine verwaltete Identität für den Indexierer. Erklären Sie delegierte gegenüber Anwendungsberechtigungen, Zustimmung und Ressourcenumfang. Dokumentieren Sie für einen fiktiven externen Build erwarteten Verbundaussteller, Subjekt und Zielgruppe mit erfundenen Claimwerten. Erläutern Sie, warum erfolgreiche Tokenausgabe keine Bereitstellungsberechtigung belegt.

**Szenario:** Der Indexierer liest nur veröffentlichte Notizen, während der Build nur seine Testanwendung aktualisiert. **Belege:** je eine erlaubte und eine abgelehnte Operation pro Workload sowie ein Berechtigungsverantwortlicher und ein Überprüfungsdatum. **Ergebnis:** eine Tabelle zur Identitätswahl und eine Skizze des Verbundvertrauens ohne Kennwörter, Clientgeheimnisse, echte Tokens oder Bereitstellungsbefehle. Dokumentieren Sie unbelegte Annahmen als Fragen an den Eigentümer.

<a id="sc-300-unit-4"></a>

## 4. Den Lebenszyklus von Berechtigungen und Privilegien aufbauen

Trennen Sie PIM-Aktivierungsberechtigung, Aktivierung und aktive Dauer von regelmäßigen Zugriffsüberprüfungen. Schlagen Sie ein Zugriffspaket für Gastdozenten und unterstützte Lebenszyklusautomatisierung für Eintritte, Wechsel und Austritte vor. Unterscheiden Sie SSO-Verbund von SCIM-Bereitstellung und erklären Sie, wie eine nachgelagerte Entfernung bestätigt würde. Listen Sie funktionsspezifische Lizenzannahmen und Verantwortliche für fehlgeschlagene Automatisierung auf.

**Szenario:** Das Semester eines Dozenten endet, während ein Administrator vorübergehenden Wartungszugriff benötigt. **Belege:** eine Ablaufentscheidung, eine Überprüfung durch den Ressourceneigentümer, ein eingegrenzter Aktivierungsvorschlag und ein Abschlussnachweis der nachgelagerten Bereitstellung. **Ergebnis:** eine Governance-Tabelle mit Auslöser, Genehmiger, Berechtigung, Dauer, Überprüfung, erwarteter Entfernung, Belegen und Ausnahmebehandlung. Eine abgeschlossene Überprüfung ist kein Nachweis einer aktivierten Rolle.

<a id="sc-300-unit-5"></a>

## 5. Einen Fehler anhand begrenzter Belege erklären

Trennen Sie Benutzerrisiko, Anmelderisiko, Richtlinienbewertung, Verzeichnisänderungen und Bereitstellungsfehler. Wählen Sie relevante Protokolle und beschreiben Sie Annahmen zu Diagnoseweiterleitung, Aufbewahrung, Zugriff und Schema. Kommentieren Sie die hypothetische KQL-Abfrage des Leitfadens damit, was ihr Aggregat feststellen kann und was nicht. Ergänzen Sie Private Access, Internet Access oder das Microsoft-Datenverkehrsprofil nur dort, wo der Ressourcenpfad diesen Zweck relevant macht.

**Szenario:** Ein Gast kann einen Kurs nicht öffnen, doch ein Dashboard zeigt keine passenden Fehler. **Belege:** eine hypothetische Zeitleiste, Abdeckungslücken, Korrelationsfelder und zwei konkurrierende Erklärungen. **Ergebnis:** eine einseitige Diagnose und Belegcheckliste, die Identität, Netzwerkpfad, Richtlinie, Anwendungsberechtigung und Bereitstellung verbindet. Kennzeichnen Sie jedes Ergebnis als erwartet; es wird weder eine Abfrage noch ein Mandantentest ausgeführt.

[Microsoft-Learn-Studienleitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Identitätsgrundlagen](../../de/06-identity.md)
