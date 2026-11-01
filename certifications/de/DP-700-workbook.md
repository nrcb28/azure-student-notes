# DP-700 · Offline-Arbeitsbuch für Data Engineering

[Leitfaden](DP-700.md) · [Zehn Fälle](DP-700-cases.md) · [Inhalt](README.md) · [English](../en/DP-700-workbook.md)

Fünf Einheiten verwenden synthetische Universitätsdaten. Sie erfordern weder Konto noch bezahlte Kapazität oder Fabric-Ausführung. Behalte in allen Sprachausgaben dieselben Abgaben bei. Kennzeichne hergeleitete Ausgaben als **ERWARTET**, lokale Beobachtungen als **BEOBACHTET** und nicht durchgeführte Plattformprüfungen als **NICHT AUSGEFÜHRT**. Quellenumfang und Grenzen der Referenzprüfung stehen im [Leitfaden](DP-700.md).

<a id="dp-700-unit-1"></a>

## 1. Plattform und Verantwortlichkeiten kartieren

Erkläre Unterschiede zwischen Mandant, Kapazität, Arbeitsbereich, Element, OneLake-Speicherort und Ausführungsmotor. Zeichne Einschreibungsquelle, rohe Downloaddateien, aufbereitete Tabellen, Bibliothekskatalog-Verknüpfung und analytischen Verbraucher. Entscheide mit je einem konkreten Grund, wo Lakehouse und Warehouse passen könnten. Nenne die Granularität jeder Tabelle.

**Szenario:** Die Bibliothek kontrolliert das Verknüpfungsziel und ändert ihre Zugriffsrichtlinie. **Belege:** Dokumentiere Zielverantwortung, interne oder externe Authentifizierungsannahmen, notwendige Rechte, Schemavertrag und Folgen einer Ziellöschung. **Abgabe:** Abhängigkeitsdiagramm und Zugriffsmatrix. Ergänze eine getrennte historische Aufbewahrungsanforderung; die Verknüpfung allein erfüllt keine Sicherungs- oder Wiederherstellungsanforderung.

<a id="dp-700-unit-2"></a>

## 2. Ein inkrementelles Änderungsprotokoll abgleichen

Nutze dieses vollständige synthetische Protokoll; `version` bestimmt die verbindliche Quellreihenfolge und `key` identifiziert eine Einschreibung. Beginne mit leerem Ziel. Bewahre für Löschungen eine versionierte Löschmarke auf. Reduziere jeden Schlüssel auf die größte Version, fasse identische Duplikate zusammen und übernimm nur neuere Versionen. Widersprüchliche Inhalte derselben Version erfordern Quarantäne.

| key | version | operation | module |
|---|---:|---|---|
| E1 | 1 | upsert | CS101 |
| E2 | 1 | upsert | DB201 |
| E1 | 2 | upsert | AI301 |
| E1 | 2 | upsert | AI301 |
| E2 | 2 | delete | DB201 |
| E2 | 1 | upsert | DB201 |

**Szenario:** Wiederhole das Protokoll nach Verlust der Erfolgsantwort. **Erwartete Belege:** E1 bleibt in AI301 mit Version 2 aktiv; E2 ist mit Version 2 gelöscht. Die aktive Anzahl ist nach beiden Läufen 1. **Abgabe:** Zwischenzustände und Regeln für Fortschrittsbestätigung; erkläre, warum die späte E2-Version 1 keine Wiederbelebung auslöst.

<a id="dp-700-unit-3"></a>

## 3. Qualitäts- und Ereigniszeitregeln festlegen

Entwirf einen Downloaddatensatz mit Ereigniskennung, Modul, Ereigniszeit, Ankunftszeit und Schemaversion. Definiere Null-, Typ-, Werte- und Duplikatregeln. Erkläre den Unterschied zwischen der Freigabe eines optionalen Felds und der Annahme ungültiger Datensätze. Quarantäne muss eine reparierbare Kennung und Ursache bewahren und sensible Inhalte beschränken.

**Szenario:** Ein Ereignis erfolgt um 23:59 UTC und kommt am nächsten Tag um 00:07 UTC an; die erklärte Verspätungstoleranz beträgt zehn Minuten. **Erwartete Belege:** Sein Ereigniszeittag ist der frühere Tag. Ob es akzeptiert wird, erfordert auch das Wasserzeichen des Motors bei Ankunft; acht Minuten Zeitverzug allein beweisen keine Annahme. **Abgabe:** Annahme- und Korrekturregeln, Abgleich, Fenstergrenzen, Prüfpunktzweck und Verhalten außerhalb der Toleranz.

<a id="dp-700-unit-4"></a>

## 4. Eine kontrollierte Bereitstellung entwerfen

Beschreibe eine Pipeline, die ein begrenztes Einschreibungsintervall kopiert, Validierung und Transformation aufruft und nur akzeptierte Ergebnisse veröffentlicht. Wähle SQL, PySpark oder KQL für relevante Transformationen und begründe den Motor. Unterscheide Git-Versionierung unterstützter Definitionen von der Bereitstellung unterstützter Inhalte und von Datenbewegung.

**Szenario:** Das Testnotebook verweist noch auf das Produktions-Lakehouse. **Belege:** Prüfe Elementreferenzen, Verbindungsbindung, Laufzeitidentität, Parameter, Umgebungsabhängigkeiten und Zeitpläne vor Ausführung. **Abgabe:** Konfigurationstabelle für Entwicklung/Test/Produktion, erlaubte und verweigerte Lesetests über Bericht und Datei sowie Rücksetzschritte. Erkläre, warum eine Vertraulichkeitsbezeichnung allein nicht den vollständigen Berechtigungsentwurf umsetzt.

<a id="dp-700-unit-5"></a>

## 5. Einen fiktiven langsamen Lauf diagnostizieren

Erstelle eine Basislinie für Dauer, Ein- und Ausgabezahlen, Ablehnungen, Aktualität und Kapazitätsauslastung. Ergänze einen Vorfall, bei dem dieselbe Eingabemenge doppelt so lange braucht. Nenne drei konkurrierende Erklärungen: schiefe Spark-Verknüpfung, viele kleine Dateien und gleichzeitiger Kapazitätsbedarf. Nenne Belege für oder gegen jede Erklärung; prüfe bei Bedarf Partitionsausschluss und Abfrageverhalten.

**Szenario:** Auf einen Teilschreibvorgang folgt eine Wiederholung. **Belege:** Zeige anhand der Versionsregeln aus Einheit 2, ob sich der fachliche Zustand ändert. **Abgabe:** ein reversibles Optimierungsexperiment mit Abnahmegrenzen und Korrektheitsabgleich. Kennzeichne alle Fabric-Zeiten als NICHT AUSGEFÜHRT; synthetische Herleitung belegt weder echten Durchsatz noch Wiederherstellungsdauer oder erfolgreiche Cloud-Bereitstellung.
