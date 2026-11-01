# SC-300 · 10 Fälle mit begründeten Antworten

[Leitfaden](SC-300.md) · [Arbeitsbuch](SC-300-workbook.md) · [Inhalt](README.md)

Eigene Fragen zu einer fiktiven universitären Notizen-App, keine offiziellen Prüfungsfragen. Erklären Sie die Zugriffsgrenze, verwerfen Sie eine ungeeignete Abkürzung und benennen Sie Belege. Alle Ergebnisse sind hypothetisch; es wurden weder Änderungen an einem echten Mandanten noch Cloud-Ausführungen vorgenommen.

## 1. Ein Benutzeradministrator der Abteilung kann einen privaten Notizencontainer nicht lesen. Sollten wir die Verzeichnisrolle erweitern?

<details>
<summary>Antwort</summary>

Identifizieren Sie zuerst, ob die fehlgeschlagene Aktion Verzeichnisverwaltung, Azure-Ressourcenverwaltung, Speicherdaten oder Anwendungsberechtigungen betrifft. Eine über eine administrative Einheit begrenzte Verzeichnisrolle gewährt nicht jede Ressourcenberechtigung dieser Abteilung. Ihre Erweiterung würde die falsche Grenze betreffen. Bilden Sie für diesen Entwurf angemeldete Identität, angeforderte Operation, Ressourcenumfang und zutreffende Datenrolle oder Anwendungsberechtigung ab. Die Belege sollten erklären, warum genau dieser Lesezugriff erlaubt oder verweigert ist, ohne aus einem Abteilungsadministrator einen mandantenweiten Administrator zu machen.

</details>

## 2. Wir haben die direkte App-Zuweisung eines Studierenden entfernt, aber der Zugriff bleibt bestehen. Schlägt das Entfernen fehl?

<details>
<summary>Antwort</summary>

Eine einzelne Entfernung belegt nicht, dass jede Gewährung verschwunden ist. Prüfen Sie gruppenbasierte App-Zuweisungen, Quellen der Gruppenmitgliedschaft, App-Rollen, anwendungseigene Freigaben sowie die tatsächlich verwendete Identität und den Mandanten. Je nach Ressource können auch geerbte Zuweisungen und bestehende Sitzungen wichtig sein. Löschen Sie das Konto nicht als ersten Diagnoseschritt. Erstellen Sie ein Diagramm der Gewährungspfade und unterscheiden Sie Zuweisungszustand von der beobachteten Entscheidung der Anwendung. Eine nützliche Erklärung benennt den verbleibenden Pfad, seinen Eigentümer und die Belege, die zur Bestätigung der Entfernung an dieser Grenze nötig sind.

</details>

## 3. Eine Partneruniversität meldet erfolgreiche MFA. Dürfen nun alle ihre Lehrenden unveröffentlichte Lösungen öffnen?

<details>
<summary>Antwort</summary>

Nein. Das Vertrauen in einen unterstützten MFA-Claim über eingehende mandantenübergreifende Einstellungen kann helfen, eine eingegrenzte Authentifizierungsanforderung zu erfüllen; es gewährt keinen Zugriff auf alle Universitätsressourcen. Untersuchen Sie die geltenden Zugriffseinstellungen beider Organisationen, die Identität des Lehrenden im Ressourcenmandanten, die Zielanwendung und ihre Berechtigung. Einladungsbeschränkungen und Gastlebenszyklus sind ebenfalls wichtig. Ich würde einen erlaubten Kurs und eine verweigerte unveröffentlichte Lösung in der Matrix erfassen. Die Belege müssen akzeptierte Authentifizierungssicherheit von der separaten Autorisierungsentscheidung für ein bestimmtes Dokument unterscheiden.

</details>

## 4. Neue Redakteure können keine Passkeys registrieren. Sollte der Helpdesk ihre Kennwörter in einer Tabelle sammeln?

<details>
<summary>Antwort</summary>

Nein. Entwerfen Sie einen genehmigten Erstregistrierungs- und Wiederherstellungsprozess mit unterstützten Methoden, möglicherweise einem Temporary Access Pass für berechtigte Nutzende. Prüfen Sie den Umfang der Authentifizierungsmethodenrichtlinie, Geräteunterstützung, Identitätsprüfung, zulässige Gültigkeitsdauer und Nutzung sowie sichere Zustellung. Ein TAP ist vertraulich und vorübergehend; er gehört weder ins Arbeitsbuch noch darf er zu einer geteilten dauerhaften Anmeldeinformation werden. Das Ergebnis beschreibt erwartete Registrierungs- und Ablaufergebnisse sowie Wiederherstellungsverantwortung. Auch erfolgreiche Passkey-Registrierung erfordert eine getrennte Prüfung, ob die vorgesehene Richtlinie zur Authentifizierungsstärke beim Zugriff gilt.

</details>

## 5. Eine Richtlinie für bedingten Zugriff im Modus „Nur Bericht“ protokolliert Fehler. Hat sie die App geschützt, indem sie diese Anfragen blockierte?

<details>
<summary>Antwort</summary>

Die Bewertung im Modus „Nur Bericht“ setzt die vorgeschlagenen Steuerungen nicht durch. Ihre Erkenntnisse unterstützen die Planung, belegen aber nicht, dass diese Richtlinie eine Anfrage blockierte. Prüfen Sie Zielidentitäten und -ressourcen, Bedingungen, Ausschlüsse, weitere zutreffende Richtlinien und die Richtliniendetails des Ereignisses. Dokumentieren Sie das erwartete erzwungene Ergebnis getrennt vom beobachteten Berichtsergebnis. Vor einer autorisierten Einführung anderswo sollte der Entwurf Pilotgruppe, Wiederherstellungszugriff, Rollback-Verantwortlichen und Lizenzprüfungen enthalten. Hier erstellen wir nur diesen Plan und eine Matrix erlaubter und verweigerter Zugriffe.

</details>

## 6. Eine ungewöhnliche Anmeldung erscheint, während ein ehemaliger Dozent noch eine Kursberechtigung besitzt. Reicht eine Risikorichtlinie?

<details>
<summary>Antwort</summary>

Dies sind unterschiedliche Entscheidungen. Anmelderisiko betrifft die Authentifizierungsanfrage; Benutzerrisiko betrifft die mögliche Kompromittierung der Identität. Untersuchen Sie Erkennungen und Kontext, bevor Sie eine ungewöhnliche Anmeldung als bösartig einstufen. Ob der Dozent weiterhin Kurszugriff benötigt, gehört zur Verantwortung für Berechtigungen und zum Austritts- oder Zugriffsüberprüfungsprozess. Eine Risikorichtlinie kann diesen geschäftlichen Bedarf nicht entscheiden. Führen Sie eine Untersuchungszeitleiste und eine getrennte Berechtigungsentscheidung mit Verantwortlichen und erwarteten Belegen zur Behebung. Das Entfernen veralteten Zugriffs bereinigt für sich genommen keine möglicherweise kompromittierte Identität.

</details>

## 7. Unser nächtlicher Indexierer hat eine Anforderung für delegierte Berechtigungen. Kann er ohne Benutzer alle Studierendennotizen lesen?

<details>
<summary>Antwort</summary>

Eine delegierte Berechtigung hängt von einem angemeldeten Benutzerkontext und dem Berechtigungsmodell der betreffenden API ab. Ein unbeaufsichtigter Workload benötigt eine geeignete Anwendungsidentität und unterstützte Anwendungsberechtigungen oder Ressourcenberechtigungen über eine verwaltete Identität. Das Anfordern von Berechtigungen unterscheidet sich außerdem vom Erteilen der Zustimmung. Vergleichen Sie Anwendungsobjekt, lokalen Dienstprinzipal, API, erteilte Zustimmungen und Ressourcenumfang. Verwenden Sie nicht ersatzweise das Kennwort eines Lehrenden. Der Offline-Entwurf sollte den minimalen Dokumentbestand des Indexierers erklären, warum er Zugriff benötigt, wer ihn genehmigt und wie sein Zugriff überprüft wird.

</details>

## 8. Eine föderierte Buildidentität erhält ein Token, aber die Bereitstellung scheitert. Sollten wir ein dauerhaftes Clientgeheimnis erstellen?

<details>
<summary>Antwort</summary>

Trennen Sie zuerst die Validierung der externen Assertion, die Entra-Tokenausgabe und die Ressourcenautorisierung. Prüfen Sie konfigurierten Aussteller, Subjekt und Zielgruppe gegen die erwarteten Claims, einschließlich Groß-/Kleinschreibung, ohne echte Tokens zu protokollieren. Untersuchen Sie anschließend die minimale Rolle und den Bereitstellungsumfang des resultierenden Prinzipals. Tokenausgabe beweist keine Berechtigung zum Ändern der Zielressource. Ein dauerhaftes Geheimnis würde Pflegeaufwand für Anmeldeinformationen einführen, ohne den Fehler zu erklären. Liefern Sie eine hypothetische Claim- und Berechtigungstabelle mit einem vorgesehenen und einem abgelehnten Buildkontext sowie den an jeder Grenze benötigten Belegen.

</details>

## 9. SAML-SSO funktioniert, aber ein abgelaufenes Gastkonto bleibt auf der Lernplattform. Ist SSO der Mechanismus zur Aufhebung der Bereitstellung?

<details>
<summary>Antwort</summary>

SSO-Verbund und Kontobereitstellung haben unterschiedliche Aufgaben. SAML kann die Authentifizierung unterstützen, während ein SCIM-Connector Anwendungskonten separat erstellt, aktualisiert oder deaktiviert. Prüfen Sie Zuweisungsumfang, Zuordnungen, Quellenänderungen, Bereitstellungsprotokolle und das unterstützte Entfernungsverhalten der Zielanwendung. Leiten Sie eine Kontolöschung nicht allein aus dem Ablauf eines Zugriffspakets oder einer erfolgreichen Anmeldung ab. Das Governance-Protokoll sollte den Verantwortlichen jedes Schritts nennen und die Entfernung einer Entra-Berechtigung vom nachgelagerten Kontozustand unterscheiden. Eine fehlgeschlagene Bereitstellungsaktion benötigt Nachverfolgung und beobachtbare Abschlussbelege.

</details>

## 10. Ein überprüfter Administrator ist für PIM aktivierungsberechtigt, und ein Dashboard zeigt keine Fehler. Ist der Wartungszugriff bewiesen?

<details>
<summary>Antwort</summary>

Eine Zugriffsüberprüfung kann die Beibehaltung der Aktivierungsberechtigung rechtfertigen, aber Aktivierung und aktive Zuweisung bleiben getrennt. Prüfen Sie genaue Rolle, Umfang, Aktivierungsanforderungen, Genehmigung, Dauer und relevante Lizenzierung. Ein leeres Dashboard hängt außerdem von Protokollabdeckung, Erfassung, Aufbewahrung, Filtern und Berechtigungen ab; es beweist weder erfolgreiche Wartung noch Fehlerfreiheit. Dokumentieren Sie eine erwartete Aktivierung und eine eingegrenzte erlaubte Operation zusammen mit einer Verweigerung außerhalb des Umfangs. Halten Sie Überprüfungsentscheidung, Aktivierungsbelege und hypothetische Protokollanalyse als getrennte Ergebnisse fest, statt zu behaupten, eine Operation sei ausgeführt worden.

</details>

[Offizieller Leitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Technische Quellen und Erklärungen](SC-300.md)
