# SC-900 · 10 Fälle mit begründeten Antworten

[Leitfaden](SC-900.md) · [Arbeitsbuch](SC-900-workbook.md) · [Inhalt](README.md)

Eigene Lernszenarien, keine offiziellen Prüfungsfragen. Benenne Anforderung, verworfene Alternative und benötigten Nachweis. Alle Beispiele sind hypothetisch; es gab keine Mandantenänderungen oder Cloudtests.

## 1. Die App wurde in einen verwalteten Dienst verlagert. Kann das Team Dokumentberechtigungen nun ungeprüft lassen?

<details>
<summary>Begründung</summary>

Nein. Der Anbieter betreibt Teile der Plattform; unsere Organisation bestimmt weiterhin den angemessenen Datenzugriff. Ich würde das Dienstmodell abbilden und Plattformbetrieb von Identität, Freigaben und Anwendungseinstellungen trennen. Eine Complianceaussage des Anbieters beweist nicht, dass unsere unveröffentlichten Dokumente privat sind. Nützliche Nachweise wären der konfigurierte Freigabebereich und Tests der vorgesehenen erlaubten und verweigerten Aktionen, ausschließlich in einer dafür autorisierten Testumgebung.

</details>

## 2. Eine Studentin meldet sich erfolgreich an, kann aber einen privaten Kursordner nicht öffnen. Ist die Authentifizierung defekt?

<details>
<summary>Begründung</summary>

Nicht zwingend. Die Authentifizierung kann funktionieren, während die Autorisierung den Zugriff korrekt verweigert. Prüfe die tatsächlich angemeldete Identität, Gruppenmitgliedschaften, die erforderliche Ordnerberechtigung und geltende Richtlinien. Eine administrative Rolle würde die Diagnose umgehen und den Bedarf überschreiten. Halte in der Entwurfsübung die erwartete Zugriffsentscheidung und den Nachweis fest, der einen Authentifizierungsfehler von einer Ablehnung durch Anwendung oder Ressourcenberechtigung unterscheiden würde.

</details>

## 3. Ein Team schlägt Passwort plus zweites Passwort als MFA vor. Was fehlt?

<details>
<summary>Begründung</summary>

Beide Geheimnisse gehören zur Wissenskategorie. Zwei davon ergeben keine unterschiedlichen Authentifizierungsfaktoren. Wähle ein unterstütztes Verfahren und eine Richtlinie für die benötigten Faktor- oder Authentifizierungsstärkeanforderungen. Berücksichtige Phishingresistenz, Registrierung, Gerätekompatibilität und Wiederherstellung. Ein Screenshot der Registrierung beweist keine Durchsetzung. Beschreibe eine erwartete Anmeldung, die das konfigurierte Verfahren verlangt, und einen Negativfall, bei dem ein unzureichendes Verfahren die Anforderung nicht erfüllt.

</details>

## 4. Eine heruntergeladene Datei hat den erwarteten Hash. Beweist das die hochladende Person oder schützt es die Vertraulichkeit?

<details>
<summary>Begründung</summary>

Nein. Ein geeigneter Vergleichswert hilft, Inhalt mit einer Referenz abzugleichen. Er verschlüsselt die Datei nicht und belegt nicht die vertrauenswürdige Herkunft der Referenz. Vertraulichkeit benötigt passende Zugriffe und gegebenenfalls Verschlüsselung; Herkunftssicherheit ein geeignetes vertrauenswürdiges Verfahren, etwa eine geprüfte Signatur. Erkläre zuerst, woher der erwartete Hash stammt. Kann ein Angreifer Datei und Referenz ersetzen, ist die Übereinstimmung deutlich weniger aussagekräftig als angenommen.

</details>

## 5. Eine Conditional-Access-Richtlinie verlangt MFA für die Finanzanwendung. Sind alle Hochschulanwendungen abgedeckt?

<details>
<summary>Begründung</summary>

Die Schlussfolgerung geht über den Richtlinienumfang hinaus. Prüfe Zielidentitäten, Anwendungen, Bedingungen, Ausnahmen und Gewährungskontrollen. Die Finanzregel kann korrekt sein, während andere Anwendungen außerhalb liegen. Nach der Zugriffsentscheidung gelten weiterhin Anwendungsberechtigungen. Vor einer autorisierten Einführung würde ich eine Matrix erwarteter Ergebnisse für verschiedene Personen und Anwendungen einschließlich Administratorwiederherstellung und Abhängigkeiten erstellen. Der Berichtsmodus kann die Prüfung unterstützen; seine Beobachtungen sind keine durchgesetzten Sperren.

</details>

## 6. Ein Administrator darf eine privilegierte Rolle aktivieren, kann die Aktion aber noch nicht ausführen. Versagt PIM?

<details>
<summary>Begründung</summary>

Eine Aktivierungsberechtigung kann eine tatsächliche Aktivierung voraussetzen, bevor privilegierte Rechte nutzbar werden. Prüfe Rolle und Umfang, Aktivierungsanforderungen, Dauer, Genehmigungsstatus und aktive Zuweisung. Vergib keine dauerhaft breitere Rolle, nur um den Fehler zu beseitigen. PIM beeinflusst die zeitliche Verfügbarkeit von Privilegien, macht eine unpassende Rolle aber nicht minimal. Der nützliche Nachweis ist eine genehmigte Aktivierung mit eingegrenzter Aktion unter der erwarteten Identität, nicht nur ein Eintrag als aktivierungsberechtigt.

</details>

## 7. Ein ehemaliges Projektmitglied hat noch Zugriff. Passt eine Zugriffsüberprüfung oder ein ID-Protection-Fund?

<details>
<summary>Begründung</summary>

Die unmittelbare Frage lautet, ob eine bestehende Berechtigung fachlich noch gerechtfertigt ist. Dazu passen eine Zugriffsüberprüfung und der Prozess für Eintritt, Wechsel und Austritt. ID Protection untersucht Identitätsrisikosignale und entscheidet nicht jeden fachlichen Bedarf für Projektordner. Verdächtiges Verhalten wird bei vorhandenen Hinweisen getrennt untersucht. Ermittle Ressourcenverantwortliche und Vergabepfad sowie mögliche Auswirkungen auf andere Projekte. Dokumentiere Entscheidung und erforderlichen Nachweis, dass die veraltete Berechtigung entfernt wurde.

</details>

## 8. Eine schädliche E-Mail und eine Endpunktwarnung könnten zusammenhängen, doch vom Endpunkt kommt keine Sicherheitstelemetrie. Was fehlt zuerst?

<details>
<summary>Begründung</summary>

Korrelation braucht relevante Quelldaten. Prüfe unterstütztes Produkt, Lizenz, Anbindungsstatus, Identitätszuordnung und den Ereigniseingang in der Untersuchungsplattform. Defender XDR kann nicht alle fehlenden Endpunktnachweise aus einer anderen Warnung rekonstruieren. Sentinel ermöglicht zusätzliche Analysen verbundener Quellen, benötigt aber ebenfalls Datenaufnahme und sinnvolle Regeln. Dokumentiere vorhandene und fehlende Ereignisse sowie eine eng gefasste prüfbare Hypothese, bevor du dem Dashboard eine vollständige Angriffsdarstellung zuschreibst.

</details>

## 9. Ein Dokument trägt „Vertraulich“, lässt sich aber extern teilen. Beweist das einen Produktfehler?

<details>
<summary>Begründung</summary>

Der Bezeichnungsname legt weder konfigurierten Schutz noch die Regel für diesen Freigabepfad fest. Prüfe Einstellungen, unterstützten Workload, Veröffentlichung und Umfang der Bezeichnung sowie DLP-Bedingungen und Aktionen. Eine rein klassifizierende Bezeichnung kann ohne Freigabesperre korrekt funktionieren. Definiere vor der Untersuchung erlaubte und blockierte Fälle. Verwende synthetischen Inhalt in einem genehmigten Test; verteile keine echten vertraulichen Daten, um eine Richtlinie vorzuführen.

</details>

## 10. Für eine Untersuchung werden Aktivitäten des Vormonats und erhaltene Nachrichten benötigt. Entspricht Audit einer Aufbewahrung oder einem Backup?

<details>
<summary>Begründung</summary>

Die Fähigkeiten haben verschiedene Zwecke. Audit liefert Aktivitätsnachweise innerhalb der konfigurierten Verfügbarkeit und Aufbewahrung. Inhaltsaufbewahrung regelt Behalten oder Löschen; eDiscovery hilft, relevantes Material für eine Untersuchung zu finden und zu bewahren. Ein Backup deckt Wiederherstellung ab und entsteht nicht automatisch durch Untersuchungswerkzeuge. Kläre Quellen, Zeitraum, Berechtigungen, Aufbewahrungs- und Sicherungsanforderungen für die Untersuchung sowie Zuständigkeit. Versprich keine nie erfassten Nachweise oder Inhalte außerhalb der geltenden Aufbewahrungsdauer.

</details>

[Offizieller Leitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · [Technische Quellen und Erklärungen](SC-900.md)
