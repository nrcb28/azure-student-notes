# AZ-900 · Quaderno avanzato comune

[←](README.md) · [Nucleo comune di studio](../../it/16-common-core.md) · [Laboratori avanzati](../../it/17-advanced-labs.md)

Obiettivi, scenari e consegne corrispondono nelle otto lingue. L'equivalenza si controlla per unità ed evidenze, non contando parole. Le guide precedenti restano spiegazioni complementari.

<a id="az-900-unit-1"></a>

## 1. Distribuire responsabilità

Confronta VM, piattaforma gestita e software già sottoscritto per lo stesso bisogno. Elenca sistema operativo, dipendenze, dati, accesso e recupero. Nessuna opzione elimina ogni responsabilità: decidono controllo necessario e capacità operativa.

**Caso:** una libreria richiede un driver di sistema. Quale opzione non è più adatta? **Evidenza:** matrice delle responsabilità e alternativa scartata per un requisito preciso.

<a id="az-900-unit-2"></a>

## 2. Disponibilità e confini

Distingui guasti di processo, istanza, zona e regione. Più istanze possono condividere dipendenze critiche. Spiega sessioni e file quando cambia l'istanza. Lo SLA di un componente non descrive tutta l'app.

**Caso:** quattro API dipendono da una base senza recupero definito. **Evidenza:** percorso completo, dipendenza debole e prova proposta.

<a id="az-900-unit-3"></a>

## 3. Dati e connettività

Separa oggetti, metadati relazionali e file condivisi. Definisci lettura, scrittura, autorizzazione e recupero. Pubblico non significa anonimo; DNS privato non concede diritti.

**Caso:** il docente apre un documento, un altro utente riceve 403. **Evidenza:** ipotesi distinte per rete, identità e autorizzazione, con osservazione che confermerebbe ciascuna.

<a id="az-900-unit-4"></a>

## 4. Governo e stime

RBAC autorizza azioni, Policy impone condizioni e tag classificano. I budget avvisano senza arrestare universalmente la spesa. Stima capacità, operazioni, trasferimenti, log e copie con ipotesi esplicite.

**Caso:** regioni approvate e costi per facoltà. **Evidenza:** regola, ruolo minimo e tabella di unità di costo senza inventare prezzi.

<a id="az-900-unit-5"></a>

## 5. Spiegare e verificare

Distingui deploy, funzionamento e recupero. Creare risorse non prova il download; creare una copia non prova un ripristino tempestivo. Usa segnali applicativi oltre alla CPU.

**Consegna:** diagramma, cinque decisioni motivate, guasto tollerato, responsabilità rimaste e pulizia. Ripeti cambiando un requisito: se la risposta non cambia mai, controlla il ragionamento.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [AZ-900](AZ-900.md)
