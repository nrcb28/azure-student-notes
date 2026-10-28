# AZ-104 · Cahier avancé commun

[←](README.md) · [Socle commun d'étude](../../fr/16-common-core.md) · [Travaux pratiques avancés](../../fr/17-advanced-labs.md)

Objectifs, cas et livrables correspondent dans les huit langues. L'équivalence se vérifie par unités et preuves, pas par nombre de mots. Les guides antérieurs restent des explications complémentaires.

<a id="az-104-unit-1"></a>

## 1. Retracer l'accès effectif

Note identité, tenant, abonnement, ressource, action et étendue. Examine groupes, attributions directes et héritées, conditions et propagation. Sépare gestion et données. Attribuer des rôles exige ses propres droits.

**Cas :** création de Storage mais impossible de lister les blobs. **Preuve :** permission nécessaire et contrôle minimal avec la même identité. Ni Owner comme test universel ni changement réseau sans hypothèse.

<a id="az-104-unit-2"></a>

## 2. Protéger et restaurer

Choisis protection d'objet, conteneur et compte. Note ce qui était activé avant l'incident. Avec versioning, une version peut devoir être sélectionnée ou promue ; pas de procédure unique.

**Cas :** récupérer un fichier identique. **Preuve :** configuration antérieure, hachages avant/après, droits vérifiés et données encore retenues après nettoyage.

<a id="az-104-unit-3"></a>

## 3. Lire avant de modifier

Interprète paramètres, ressources, dépendances, sorties et différences. Sépare compilation, validation, what-if et application. Les exports peuvent nécessiter une révision ; quotas, régions et Policy bloquent parfois une syntaxe valide.

**Cas :** module non analysé. **Preuve :** diagnostic, étendue exclue et résolution avant application. Examiner disques, réseau et paramètres lors des changements de VM.

<a id="az-104-unit-4"></a>

## 4. Diagnostiquer tout le trajet

Suis DNS, IP, route, NSG, pare-feu système, processus et autorisation. Plusieurs filtres avec état peuvent agir. Vérifie frontend, backend, règle et sonde. Sépare entrée privée App Service et intégration sortante.

**Cas :** sonde saine, requête réelle en échec. **Preuve :** ports, réponses, règles et hypothèse testable. La sonde ne prouve pas la correction métier.

<a id="az-104-unit-5"></a>

## 5. Exploiter avec des preuves

Définis métrique, log, alerte, action et responsable. Contrôle source, association et destination avant la requête. Mesure la reprise complète avec identité, DNS et dépendances.

**Livrable :** pratiques Storage et inspection des rôles, attendu face à observé, runbook. Sépare tests locaux et Azure ; vérifie suppression ou rétention résiduelle.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) · [AZ-104](AZ-104.md)
