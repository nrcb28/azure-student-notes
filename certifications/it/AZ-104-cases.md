# AZ-104 · Ripasso

[Leggi](AZ-104.md) · [Indice](README.md)

Prova a rispondere prima di aprire la soluzione. Sono domande di studio originali, non domande ufficiali. Per ogni caso indica requisito, scelta e metodo di verifica.

## 1. Tolto Reader, accesso ancora presente.

<details>
<summary>Risposta</summary>

Controllare gruppi e assegnazioni ereditate.

</details>

## 2. Contributor crea Storage, ma non legge blob.

<details>
<summary>Risposta</summary>

Controllare ruoli dati e autenticazione.

</details>

## 3. VNet integration ma web ancora pubblica.

<details>
<summary>Risposta</summary>

L'integrazione riguarda uscita. Verificare controlli di ingresso.

</details>

## 4. Backend unhealthy nel bilanciatore.

<details>
<summary>Risposta</summary>

Controllare porta, risposta del probe, processo e filtri.

</details>

## 5. A-B e B-C in peering, A-C fallisce.

<details>
<summary>Risposta</summary>

Il peering non è automaticamente transitivo.

</details>

## 6. Bicep compila ma deploy negato.

<details>
<summary>Risposta</summary>

Verificare Policy, permessi, quote e disponibilità.

</details>

## 7. Backup corretto: RTO garantito?

<details>
<summary>Risposta</summary>

No. Misurare ripristino e recupero completo.

</details>

## 8. Private endpoint, DNS ancora pubblico.

<details>
<summary>Risposta</summary>

Rivedere zone private, link e risoluzione client.

</details>

## 9. VM spenta ma costo residuo.

<details>
<summary>Risposta</summary>

Distinguere arresto, deallocazione, dischi e altri servizi.

</details>

## 10. Policy non corregge vecchie risorse.

<details>
<summary>Risposta</summary>

Verificare effetto e remediation necessaria.

</details>
