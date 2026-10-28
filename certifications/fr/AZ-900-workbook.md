# AZ-900 · Cahier avancé commun

[←](README.md) · [Socle commun d'étude](../../fr/16-common-core.md) · [Travaux pratiques avancés](../../fr/17-advanced-labs.md)

Objectifs, cas et livrables correspondent dans les huit langues. L'équivalence se vérifie par unités et preuves, pas par nombre de mots. Les guides antérieurs restent des explications complémentaires.

<a id="az-900-unit-1"></a>

## 1. Répartir les responsabilités

Compare VM, plateforme administrée et logiciel déjà souscrit pour le même besoin. Liste système, dépendances, données, accès et reprise. Aucune option n'annule toute responsabilité ; contrôle requis et capacité d'exploitation décident.

**Cas :** une bibliothèque impose un pilote système. Quelle option ne convient plus ? **Preuve :** matrice des responsabilités et alternative rejetée pour une exigence précise.

<a id="az-900-unit-2"></a>

## 2. Disponibilité et frontières

Distingue panne de processus, instance, zone et région. Plusieurs instances peuvent partager des dépendances critiques. Explique sessions et documents lorsqu'une requête change d'instance. Un SLA de composant ne décrit pas toute l'application.

**Cas :** quatre API dépendent d'une base sans reprise définie. **Preuve :** trajet complet, faiblesse et test proposé.

<a id="az-900-unit-3"></a>

## 3. Données et connectivité

Sépare objets, métadonnées relationnelles et fichiers partagés. Définis lecture, écriture, autorisation et restauration. Public ne signifie pas anonyme ; DNS privé ne donne pas de droits.

**Cas :** un enseignant ouvre un lien, un autre utilisateur reçoit 403. **Preuve :** hypothèses distinctes réseau, identité et autorisation, chacune associée à une observation.

<a id="az-900-unit-4"></a>

## 4. Gouverner et estimer

RBAC accorde des actions, Policy impose des conditions, les tags classent. Les budgets alertent sans arrêter tous les coûts. Estime capacité, opérations, transfert, logs et sauvegardes avec hypothèses explicites.

**Cas :** régions approuvées et dépenses par faculté. **Preuve :** règle, rôle minimal et unités de coût sans tarifs inventés.

<a id="az-900-unit-5"></a>

## 5. Expliquer et vérifier

Distingue déploiement, fonctionnement et reprise. Créer des ressources ne prouve pas le téléchargement ; une sauvegarde ne prouve pas une restauration rapide. Utilise des signaux métier avec la CPU.

**Livrable :** schéma, cinq décisions justifiées, panne tolérée, responsabilités restantes et nettoyage. Recommence avec une exigence différente ; une réponse immuable peut masquer l'absence de raisonnement.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [AZ-900](AZ-900.md)
