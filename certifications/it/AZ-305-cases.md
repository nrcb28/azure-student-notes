# AZ-305 · Ripasso

[Leggi](AZ-305.md) · [Indice](README.md)

Prova a rispondere prima di aprire la soluzione. Sono domande di studio originali, non domande ufficiali. Per ogni caso indica requisito, scelta e metodo di verifica.

## 1. RPO zero implica RTO zero?

<details>
<summary>Risposta</summary>

No. Perdita di dati e tempo di recupero sono distinti.

</details>

## 2. API usa JSON e transazioni complesse.

<details>
<summary>Risposta</summary>

Scegliere dai requisiti, non dal formato di trasporto.

</details>

## 3. Piccolo team vuole AKS per una API.

<details>
<summary>Risposta</summary>

Valutare necessità Kubernetes, competenze, alternative e costi.

</details>

## 4. Replica esterna ma dati vincolati al paese.

<details>
<summary>Risposta</summary>

Controllare residenza di repliche, backup, log e dipendenze.

</details>

## 5. VM replicate, mancano DNS e segreti.

<details>
<summary>Risposta</summary>

Il servizio non è completamente recuperato.

</details>

## 6. Aggiungiamo cache.

<details>
<summary>Risposta</summary>

Progettare invalidazione, scadenza e tolleranza a dati vecchi.

</details>

## 7. Migrazione con scritture continue.

<details>
<summary>Risposta</summary>

Definire trasferimento iniziale, sincronizzazione, cutover e rollback.

</details>

## 8. Report storici rallentano iscrizioni.

<details>
<summary>Risposta</summary>

Valutare separazione analitica e query prima di scalare.

</details>

## 9. Disegno con soli nomi dei servizi.

<details>
<summary>Risposta</summary>

Aggiungere requisiti, confini, guasti, gestione e validazione.

</details>

## 10. Budget ridotto, stessi obiettivi.

<details>
<summary>Risposta</summary>

Rivalutare alternative e misure; non promettere senza evidenza.

</details>
