# Ripasso · 24

[Indice](README.md)

Prova a rispondere prima di aprire la soluzione. Sono domande di studio originali, non domande ufficiali. Per ogni caso indica requisito, scelta e metodo di verifica.

## 1. Serve controllo del kernel. VM o piattaforma web?

<details>
<summary>Risposta</summary>

VM, se offre il controllo richiesto. La scelta dipende dai requisiti del sistema.

</details>

## 2. MFA concede lettura ai documenti?

<details>
<summary>Risposta</summary>

No. Autenticazione e autorizzazione sono diverse.

</details>

## 3. Un endpoint pubblico significa anonimo?

<details>
<summary>Risposta</summary>

No. Può richiedere identità e permessi.

</details>

## 4. Aggiungiamo istanze: quale scalabilità?

<details>
<summary>Risposta</summary>

Orizzontale. Più capacità nella stessa istanza è verticale.

</details>

## 5. Una replica recupera ogni cancellazione?

<details>
<summary>Risposta</summary>

No. Occorre conservare uno stato precedente con strumenti adatti.

</details>

## 6. Una regola deve bloccare regioni non ammesse.

<details>
<summary>Risposta</summary>

Usare Policy con ambito ed effetto appropriati.

</details>

## 7. Il budget interrompe tutta la spesa?

<details>
<summary>Risposta</summary>

No. Serve a monitorare e avvisare.

</details>

## 8. CPU bassa ma API lenta.

<details>
<summary>Risposta</summary>

Controllare dipendenze, rete, query e attese.

</details>

## 9. Come trasferire grandi volumi con rete insufficiente?

<details>
<summary>Risposta</summary>

Confrontare trasferimento online e Data Box secondo supporto, tempi e sicurezza.

</details>

## 10. Il deploy è riuscito: abbiamo finito?

<details>
<summary>Risposta</summary>

No. Verificare comportamento e dipendenze dell'app.

</details>

## 11. Tolto Reader, accesso ancora presente.

<details>
<summary>Risposta</summary>

Controllare gruppi e assegnazioni ereditate.

</details>

## 12. Contributor crea Storage, ma non legge blob.

<details>
<summary>Risposta</summary>

Controllare ruoli dati e autenticazione.

</details>

## 13. VNet integration ma web ancora pubblica.

<details>
<summary>Risposta</summary>

L'integrazione riguarda uscita. Verificare controlli di ingresso.

</details>

## 14. Backend unhealthy nel bilanciatore.

<details>
<summary>Risposta</summary>

Controllare porta, risposta del probe, processo e filtri.

</details>

## 15. A-B e B-C in peering, A-C fallisce.

<details>
<summary>Risposta</summary>

Il peering non è automaticamente transitivo.

</details>

## 16. Bicep compila ma deploy negato.

<details>
<summary>Risposta</summary>

Verificare Policy, permessi, quote e disponibilità.

</details>

## 17. Backup corretto: RTO garantito?

<details>
<summary>Risposta</summary>

No. Misurare ripristino e recupero completo.

</details>

## 18. Private endpoint, DNS ancora pubblico.

<details>
<summary>Risposta</summary>

Rivedere zone private, link e risoluzione client.

</details>

## 19. VM spenta ma costo residuo.

<details>
<summary>Risposta</summary>

Distinguere arresto, deallocazione, dischi e altri servizi.

</details>

## 20. Policy non corregge vecchie risorse.

<details>
<summary>Risposta</summary>

Verificare effetto e remediation necessaria.

</details>

## 21. RPO zero implica RTO zero?

<details>
<summary>Risposta</summary>

No. Perdita di dati e tempo di recupero sono distinti.

</details>

## 22. API usa JSON e transazioni complesse.

<details>
<summary>Risposta</summary>

Scegliere dai requisiti, non dal formato di trasporto.

</details>

## 23. Piccolo team vuole AKS per una API.

<details>
<summary>Risposta</summary>

Valutare necessità Kubernetes, competenze, alternative e costi.

</details>

## 24. Replica esterna ma dati vincolati al paese.

<details>
<summary>Risposta</summary>

Controllare residenza di repliche, backup, log e dipendenze.

</details>
