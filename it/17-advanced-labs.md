# Laboratori avanzati

[←](README.md) · [Nucleo comune di studio](16-common-core.md)

Tre pratiche equivalenti nelle otto lingue. Simulazione locale; le altre richiedono sottoscrizione di prova, Azure CLI e permessi. Non eseguite qui su Azure. Risorse e dati trattenuti possono costare. Parti dalla radice e leggi prima la pulizia.

<a id="advanced-lab-1"></a>

## 1. Recuperare e confrontare i byte

Crea solo gruppo e account dedicati. La configurazione disattiva versioning e namespace gerarchico per usare undelete senza promozione. Soft delete di blob e contenitori dura sette giorni; chiavi condivise e blob pubblici sono disattivati, endpoint pubblico autenticato resta.

Servono gestione e un ruolo dati appropriato, come Storage Blob Data Contributor sull'account. La configurazione non assegna ruoli. Attendi propagazione senza concedere Owner globale.

Lo script crea un contenitore nuovo, carica testo sintetico, elimina solo quel blob, ripristina e confronta. Atteso RECOVERY_OK. Elimina poi il contenitore, ma possono restare dati trattenuti. Registra fase ed errore senza segreti; non modificare produzione.

[Bicep](../labs/protected-storage.bicep) · [Script](../labs/blob-recovery.sh)

```bash
az login
export LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account show --subscription "$LAB_SUBSCRIPTION" --query '{name:name,id:id}' -o table
export LAB_RG="rg-notes-recovery-$(date -u +%Y%m%d%H%M%S)"
export LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$RANDOM"
az group create --name "$LAB_RG" --location westeurope \
  --subscription "$LAB_SUBSCRIPTION" --tags environment=lab project=notes-recovery

az deployment group what-if --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Review proposed changes before running create.
az deployment group create --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Run after the required data permissions have been provided.
bash labs/blob-recovery.sh
```

<a id="advanced-lab-2"></a>

## 2. Ispezionare senza assegnare

Usa ID risorsa e object ID del principal, non client ID. Lo script legge assegnazioni al principal, includendo ambiti ereditati. Non calcola tutto l'accesso effettivo: gruppi, condizioni, negazioni, attivazione temporanea e controlli dati/rete richiedono analisi.

Consegna ruolo, ambito, condizione e azione richiesta. Output vuoto non dimostra assenza di ogni accesso. Non creare assegnazioni per ottenere righe.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Simulare risposta persa

Nessuna rete, credenziale o risorsa cloud. SQLite salva, la prima risposta si perde e il client ripete. Con tre tentativi: naive salva due documenti, idempotent uno, permanent non scrive né ripete. Le attese sono calcolate senza dormire.

Un tentativo può lasciare una scrittura senza successo confermato. Spiega perché eccezione non significa nessuna operazione. Sette test locali verificano comportamento e protezioni, non disponibilità Azure.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Pulizia e consegna

Elenca il gruppo dedicato, conferma eliminazione e verifica false. Il contenitore eliminato non dimostra scadenza di tutta la retention. Controlla errori e lock, senza purge di risorse condivise.

Consegna previsto, osservato, permessi, confronto, interpretazione ruoli e simulatore. Separa test locali e cloud.



```bash
case "$LAB_RG" in
  rg-notes-recovery-*) ;;
  *) echo "Not a dedicated recovery lab group"; exit 2 ;;
esac
az resource list --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" -o table
az group delete --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
az group exists --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
```

[Microsoft Learn: Blob soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable) · [Restore](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-manage) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)
