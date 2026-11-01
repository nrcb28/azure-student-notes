# SC-100 · Zehn Architekturfälle

[Leitfaden](SC-100.md) · [Arbeitsbuch](SC-100-workbook.md) · [Inhalt](README.md) · [English](../en/SC-100-cases.md)

Eigene hypothetische Fragen zur universitären Notizen-App. Erkläre fachliche Anforderung, Kontrollgrenze, Verantwortung und Abnahmebelege vor dem Öffnen der Antwort. Dies sind Offline-Entwurfsübungen, keine offiziellen Prüfungsfragen oder Behauptungen ausgeführter Kontrollen.

## 1. Ein Dekan will zuerst den höchsten Sicherheitswert statt unveröffentlichte Antworten zu schützen. Wie setzt man Prioritäten?

<details>
<summary>Antwort</summary>

Beginne mit den Auswirkungen offengelegter Antworten und möglichen Offenlegungswegen. Ermittle Datenverantwortung, aktuellen Zugriff, privilegierte Identitäten, Freigabewege und vorhandene Belege. Ein Wert kann Sicherheitslücken anzeigen, aber keine fachlichen Prioritäten der Universität festlegen. Schlage Kontrollen zur Verringerung der kritischen Gefährdung vor und definiere Abnahme durch begrenzte Zugriffstests und prüfbare Konfiguration. Dokumentiere Kosten, Restrisiken und die befugte Risikoentscheidung des Dekans. Eine sachfremde Empfehlung mit geringer Wirkung vorzuziehen braucht eine belastbare Begründung, nicht nur einen leichter erreichbaren höheren Wert.

</details>

## 2. Die API nutzt einen privaten Endpunkt. Darf die Architektur Zero Trust für abgeschlossen erklären?

<details>
<summary>Antwort</summary>

Private Verbindung begrenzt einen Netzwerkweg; sie schafft keine Identität, Anwendungsautorisierung oder umfassende Isolation. Prüfe verbleibenden öffentlichen Zugriff, DNS-Auflösung auf Campus und in Wiederherstellungsumgebungen sowie erreichende Aufrufer. Definiere danach Nutzerauthentifizierung, Workload-Rechte, gegebenenfalls Geräteanforderungen und kursbezogene Zugriffsentscheidungen. Beziehe Verwaltungs- und Ausgangswege ein. Die Abnahme soll erwartete erlaubte und verweigerte Anfragen sowie Belege zur Unterscheidung zwischen Netzfehler und Rechteverweigerung enthalten. Dokumentiere verbleibende Grenzen, statt eine einzelne Funktion zur vollständigen Strategie zu erklären.

</details>

## 3. Indexer und KI-Agent teilen ein Administratorkonto. Was muss sich am Entwurf ändern?

<details>
<summary>Antwort</summary>

Gib jedem Workload eine unterscheidbare Identität, Verantwortung, Lebenszyklus und Berechtigungsgrenze. Der Indexer braucht erlaubte veröffentlichte Dokumente; der Agent nur Retrieval und aufgabenbezogene Werkzeuge. Bewerte verwaltete Identitäten, Föderation und unterstützte Agent-Identitätskontrollen anhand dieser Anforderungen. Entferne die Abhängigkeit von einem menschlichen Administrator und definiere Ablauf oder Entzug des Zugriffs. Erfolgreiche Authentifizierung darf weder breiten Datenzugriff noch Bereitstellungsrechte bedeuten. Abnahmebelege sollen erlaubte Operationen, verweigerten kursübergreifenden Zugriff, zurechenbare Aktivität und Wiederherstellung beim Ausfall einer Identität zeigen.

</details>

## 4. Sentinel erhält Cloud-Warnungen, aber keine Campusverzeichnisereignisse. Ist die SOC-Architektur ausreichend?

<details>
<summary>Antwort</summary>

Das hängt von priorisierten Bedrohungen und dokumentierter Abdeckung ab. Kann ein kompromittiertes Campusverzeichnis den Notizendienst betreffen, ist fehlende Verzeichnistelemetrie eine erhebliche Erkennungslücke. Ordne die Bedrohung erwarteten Signalen, Aufnahmeabhängigkeiten, Aufbewahrung, Erkennung, Ersteinschätzung und Eindämmungsbefugnis zu. Erkläre Beiträge von Defender XDR und Sentinel, ohne automatische Sicht auf jede Anlage anzunehmen. Schlage eine Aufnahmephase oder Ersatzüberwachung mit Verantwortung und Frist vor. Abnahme verlangt nutzbare repräsentative Ereignisse und einen Reaktionsdurchlauf, nicht nur einen aktivierten Connector oder gefüllten Dashboardbildschirm.

</details>

## 5. Vertraulichkeitsbezeichnung und verschlüsselte Datenträger sollen die gesamte Studierendendatenstrategie bilden. Was fehlt?

<details>
<summary>Antwort</summary>

Kläre Datenorte, Klassifizierung, Empfänger und Pflichten. Prüfe die tatsächliche Konfiguration der Bezeichnung sowie Clients und Speicher, die deren Schutz beachten. Datenträgerverschlüsselung schützt eine Speichergrenze, hindert autorisierte Dienste aber nicht am Klartextlesen oder -export. Berücksichtige begrenzten Zugriff, Freigaberegeln, DLP-Abdeckung, Überwachung, Aufbewahrung, Löschung und Schlüsselverwaltung. Weise jeder Anforderung Belege und Verantwortung zu, auch bei nicht unterstützten Wegen. Datenschutz- und Rechtsverantwortliche müssen Pflichten bewerten; weder eine Bezeichnung noch ein Compliance-Wert beweist die Erfüllung aller gesetzlichen Anforderungen.

</details>

## 6. Ein hochgeladenes Lehrdokument fordert den KI-Assistenten auf, alle Kursdateien zu mailen. Welche Grenze zählt?

<details>
<summary>Antwort</summary>

Das Dokument ist nicht vertrauenswürdiger abgerufener Inhalt und kann Modell oder Werkzeugen keine Befugnisse erteilen. Begrenze Retrieval auf erlaubte Inhalte, beschränke die Agent-Identität und erzwinge Werkzeugautorisierung außerhalb generierter Anweisungen. Ein Versandwerkzeug braucht eine ausdrückliche Empfänger- und Datenzugriffsrichtlinie sowie die im Entwurf verlangte Zustimmung zu folgenreicher Offenlegung. Bewerte Promptangriffserkennung als Zusatzkontrolle mit unterstützten Integrations- und Sprachannahmen. Nutze synthetische Dokumente im Planspiel. Die Abnahme soll zeigen, dass eine Dokumentanweisung weder Retrieval- noch Werkzeugrechte erweitern kann.

</details>

## 7. Nächtliche Sicherungen stellen Dateien wieder her, aber der Dienst braucht fünfzehn Minuten RPO. Besteht der Entwurf die Prüfung?

<details>
<summary>Antwort</summary>

Nicht anhand dieser Belege. Nur nächtliche Wiederherstellungspunkte erfüllen keinen maximalen Datenverlust von fünfzehn Minuten. Ermittle alle Datenquellen und ihre Wiederherstellungsverfahren einschließlich Konsistenz zwischen Dokumenten und Metadaten. Prüfe außerdem ransomwarefeste Sicherungsverwaltung, Aufbewahrung und Schlüsselwiederherstellung. Das zweistündige Anwendungs-RTO braucht Identität, DNS, Konfiguration und Steuerungszugang, nicht nur Dateien. Die Verantwortung muss einen passenden Entwurf finanzieren und validieren oder geänderte Anforderungen mit ausdrücklichen Auswirkungen genehmigen. Dokumentiere erwartete Messungen; diese Offline-Übung beweist keine Wiederherstellungsleistung.

</details>

## 8. Das Cloud-Plattformteam wendet Azure-Richtlinien an. Wie behandelt man eine SaaS-Ausnahme eines Fachbereichs?

<details>
<summary>Antwort</summary>

Kläre zuerst, ob der Richtlinienumfang den SaaS-Dienst überhaupt steuern kann; leite keine Abdeckung aus einem Azure-Compliance-Ergebnis ab. Ordne den Fachbereichsdienst den Universitätsanforderungen zu und prüfe native Kontrollen, Identitätsintegration, Datenverarbeitung, Prüfbelege und vertragliche Verantwortung. Nutze das Verantwortungsmodell der Landezone zur Klärung von Plattform- und Workload-Aufgaben, ohne identische Durchsetzung für alle Dienste vorzutäuschen. Dokumentiere bei verbleibender Lücke Ersatzkontrollen, Risikoverantwortung, Prüftermin und Ablaufdatum. Die Architekturentscheidung soll Auswirkungen der Ausnahme auf den gesamten Dienst zeigen.

</details>

## 9. Ein signiertes Build-Artefakt stammt von einem Runner mit breiten Produktionsrechten. Ist die Lieferkette geschützt?

<details>
<summary>Antwort</summary>

Signieren unterstützt Integrität und Herkunft unter definierten Vertrauensannahmen; es macht einen kompromittierten autorisierten Build allein nicht vertrauenswürdig. Prüfe Quellfreigabe, Abhängigkeitskontrollen, Runner-Isolation, Zugriff auf Signaturschlüssel, Artefaktübernahme und Bereitstellungsrechte. Trenne Test- und Produktionsvertrauen und begrenze gegebenenfalls Föderationsansprüche und Ressourcenumfang. Definiere, wer verdächtige Releases untersucht und einen bekannten guten Stand wiederherstellt. Abnahmebelege sollen genehmigte Quellrevision, übernommenes Artefakt und autorisierte Bereitstellung verbinden und zeigen, dass eine nicht freigegebene Pipeline weder Produktion noch Signaturrichtlinie ändern kann.

</details>

## 10. Die Finanzierung reicht für ein Semester. Wie lässt sich ein gestuftes Sicherheitsprogramm begründen?

<details>
<summary>Antwort</summary>

Ordne Arbeiten nach fachlich kritischer Gefährdung, Abhängigkeiten, praktischer Umsetzungskapazität und erwarteter Risikominderung. Schutz von Wiederherstellung und privilegierter Verwaltung kann spätere Migration und Reaktion ermöglichen; begründe diese Reihenfolge anhand der Universitätsbedrohungen. Vergleiche machbare Optionen, Lizenzen, Betriebsaufwand und Lehrunterbrechung. Weise jeder Phase Verantwortung, begrenzte Abnahmekriterien, Belege, Rücksetzbedingungen und datierte Restrisikoprüfung zu. Dokumentiere eine Alternative und ihre Ablehnung in einem ADR. Ein finanzierter Kauf ist ein Meilenstein; validierte Wirksamkeit und befugte Risikoannahme bestimmen die Einsatzbereitschaft.

</details>

[Offizieller SC-100-Studienleitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)
