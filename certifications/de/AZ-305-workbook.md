# AZ-305 · Gemeinsames Vertiefungsheft

[←](README.md) · [Gemeinsamer Lernkern](../../de/16-common-core.md) · [Vertiefende Übungen](../../de/17-advanced-labs.md)

Ziele, Fälle und Abgaben entsprechen sich in allen acht Sprachen. Gleichwertigkeit wird anhand von Lerneinheiten und Nachweisen geprüft, nicht anhand der Wortzahl. Frühere Leitfäden bleiben ergänzende Erklärungen.

<a id="az-305-unit-1"></a>

## 1. Bedarf in Grenzen übersetzen

Definiere Nutzer, Wachstum, Residenz, Datenschutz, Leistung, RTO, RPO, Budget und Kompetenzen. Trenne bestätigte Anforderungen und Annahmen. Immer verfügbar braucht Operationen und Messfenster.

**Fall:** Fünf Fakultäten teilen Netze, nicht private Daten. **Nachweis:** Verwaltungs- und Datengrenzen, Eigentümer und trennende Anforderung. Architektur nicht wegen ihrer Größe wählen.

<a id="az-305-unit-2"></a>

## 2. Daten und Zustand entwerfen

Vergleiche Abfragen, Transaktionen, Kompatibilität, Konsistenz und Wiederherstellung. JSON bestimmt keinen Motor. Leseskalierung erhöht nicht zwingend Schreibkapazität. Unterscheide Anwendungs-, Sitzungs- und Dokumentzustand.

**Fall:** Schneller Cache liefert alte Rechte. **Nachweis:** Invalidierung, Ablauf, Ausfallverhalten und Informationen, die keiner veralteten Kopie vertrauen dürfen.

<a id="az-305-unit-3"></a>

## 3. Vollständige Wiederherstellung planen

Weise Dienste und Daten RTO/RPO zu. Berücksichtige Kapazität, Zugangsdaten, Rechte, DNS und Konfiguration. Replikation kann logische Schäden verteilen. Vergleiche aktiv-aktiv und aktiv-passiv nach Kosten und Komplexität.

**Fall:** Key Vault ohne notwendige Integrationen zurück. **Nachweis:** Reihenfolge, autorisierter Verbrauchertest, nicht automatisch restaurierte Abhängigkeiten und isolierte Probe.

<a id="az-305-unit-4"></a>

## 4. Ausführung und Kommunikation

Vergleiche VM, PaaS, Container und Batch nach Kontrolle, Dauer und Betrieb. Queues schaffen Zustände und Duplikate. Plane Timeouts, begrenzte Retries und Idempotenz vor mehr Verbrauchern.

**Fall:** Speicherantwort verloren, Nachricht wiederholt. **Nachweis:** stabile Kennung, Versuchslimit und Teilverarbeitung. Begründe Cluster oder einfachere Plattform.

<a id="az-305-unit-5"></a>

## 5. Migration dokumentieren

Inventarisiere Abhängigkeiten und Nutzung; prüfe Kompatibilität, Pilot, Ersttransfer, Änderungen, Umschaltung und Rückfall. Definiere Integritätsnachweis und Abschaltung der Quelle. Eine VM ohne benötigte Dateien ist unvollständig migriert.

**Abgabe:** zwei ADRs, Netzwerk und Wiederherstellung, Risikotabelle. Je Entscheidung Alternative, Konsequenz, Test und Review-Anlass. Budget- oder Residenzänderung neu bewerten.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [AZ-305](AZ-305.md)
