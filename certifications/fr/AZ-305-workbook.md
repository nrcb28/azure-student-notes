# AZ-305 · Cahier avancé commun

[←](README.md) · [Socle commun d'étude](../../fr/16-common-core.md) · [Travaux pratiques avancés](../../fr/17-advanced-labs.md)

Objectifs, cas et livrables correspondent dans les huit langues. L'équivalence se vérifie par unités et preuves, pas par nombre de mots. Les guides antérieurs restent des explications complémentaires.

<a id="az-305-unit-1"></a>

## 1. Transformer les besoins en contraintes

Définis utilisateurs, croissance, résidence, confidentialité, performance, RTO, RPO, budget et compétences. Sépare exigence vérifiée et hypothèse. Toujours disponible exige opérations et fenêtre.

**Cas :** cinq facultés partagent réseau et gardent des données privées. **Preuve :** frontières, responsables et exigence de séparation. Ne choisis pas une architecture pour sa taille.

<a id="az-305-unit-2"></a>

## 2. Concevoir données et état

Compare requêtes, transactions, compatibilité, cohérence et reprise. JSON ne choisit pas le moteur. La lecture ne dimensionne pas automatiquement l'écriture. Sépare états application, session et document.

**Cas :** cache rapide mais permissions anciennes. **Preuve :** invalidation, expiration, comportement en panne et informations qui ne doivent pas dépendre d'une copie périmée.

<a id="az-305-unit-3"></a>

## 3. Prévoir une reprise complète

Attribue RTO/RPO aux services et données. Inclus capacité, identifiants, droits, DNS et configuration. La réplication propage aussi des dommages logiques. Compare actif-actif et actif-passif avec coût et complexité.

**Cas :** Key Vault revient sans intégrations. **Preuve :** ordre, test du consommateur autorisé, dépendances non restaurées automatiquement et répétition isolée.

<a id="az-305-unit-4"></a>

## 4. Exécution et communication

Compare VM, PaaS, conteneurs et batch selon contrôle, durée et exploitation. Les files ajoutent états et doublons. Prévois timeout, retries bornés et idempotence avant d'ajouter des consommateurs.

**Cas :** réponse perdue et message répété. **Preuve :** identifiant stable, limite d'essais et traitement partiel. Justifie cluster ou plateforme simple.

<a id="az-305-unit-5"></a>

## 5. Documenter la migration

Inventorie dépendances et utilisation, valide compatibilité, pilote, transfert initial, changements, bascule et retour. Définis intégrité et retrait de la source. Une VM privée de fichiers nécessaires reste incomplète.

**Livrable :** deux ADR, réseau, reprise et risques. Pour chaque choix : alternative raisonnable, conséquence, test et révision. Réévalue avec budget ou résidence modifiés.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [AZ-305](AZ-305.md)
