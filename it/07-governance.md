# Governo e conformità

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

RBAC stabilisce chi può agire; Policy stabilisce condizioni delle risorse. Una persona autorizzata a creare VM può essere bloccata da una regola sulle regioni.

Audit segnala, Deny blocca richieste incompatibili. Modify e DeployIfNotExists richiedono configurazione appropriata; le risorse esistenti possono richiedere remediation. Non tutto viene corretto immediatamente.

Tag come project, environment e owner aiutano a classificare. Non sono confini di sicurezza e non si ereditano sempre automaticamente. I lock amministrativi non sostituiscono backup o permessi sui dati.

Defender for Cloud e Sentinel rispondono a esigenze diverse. Una certificazione del provider non certifica automaticamente la nostra applicazione.

**Esercizio:** introduci una regola prima in audit, identifica impatto e responsabili, poi valuta il blocco. Ogni eccezione deve avere motivo e revisione.

---

[Precedente](06-identity.md) · [Successivo](08-observability.md) · [English](../en/07-governance.md)

## Approfondimento Microsoft Learn · policy

La remediation applica modify o deployIfNotExists alle risorse esistenti utilizzando identità e permessi dell'assegnazione. Una modifica della definizione non aggiorna automaticamente ogni autorizzazione.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-policy)
