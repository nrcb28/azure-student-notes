# AZ-120 · Cahier avancé commun

[Guide](AZ-120.md) · [10 cas](AZ-120-cases.md) · [Sommaire](README.md)

Cinq unités correspondantes dans toutes les langues. Travaillez hors connexion sur le paysage SAP d’achats et de finance de l’université fictive et sur son intégration au portail de recherche. Aucune licence, aucun déploiement Azure, aucune exécution SAP ni aptitude à la production ne sont fournis ou revendiqués. Distinguez hypothèses et résultats prévisionnels des preuves observées.

<a id="az-120-unit-1"></a>

## 1. Inventorier les responsabilités et la capacité prise en charge

Dessinez les SID de production et hors production, serveurs d’application, ASCS/ERS ou SCS, HANA, fichiers partagés, identité, DNS et interfaces. Attribuez les responsables d’infrastructure, système d’exploitation, Basis, base de données, sécurité et validation métier. Expliquez pourquoi des serveurs d’application redondants laissent d’autres points uniques de défaillance. Construisez une feuille de dimensionnement couvrant SAPS pertinents, mémoire, croissance, débit, latence et marge en cas de panne ; laissez le choix du SKU conditionnel aux vérifications de certification et de compatibilité.

**Scénario :** une VM moins chère correspond au nombre de cœurs, mais aucune preuve de prise en charge HANA n’est consignée. **Preuves :** carte de dépendances, combinaison VM/système d’exploitation/base de données/stockage prise en charge, hypothèses de quotas régionaux et responsable de révision des licences. **Livrable :** une décision d’architecture expliquant les critères d’acceptation et les mesures non résolues. Revoyez les [fondamentaux du calcul](../../fr/03-compute.md).

<a id="az-120-unit-2"></a>

## 2. Concevoir placement, réseau et stockage HANA

Dessinez les chemins pris en charge entre application et base de données, administration, réplication, sauvegarde, connectivité du campus et redirection DNS. Séparez la connectivité privée ExpressRoute des contrôles de chiffrement choisis. Comparez l’isolation des zones aux contraintes de colocalisation PPG avec des hypothèses explicites de latence. Planifiez `/hana/data`, `/hana/log` et `/hana/shared`, les systèmes de fichiers pris en charge, les plafonds d’E/S des disques et VM, ainsi que les décisions de cache ou de Write Accelerator propres à la configuration.

**Scénario :** un savepoint coïncide avec des achats lents et une proposition place une appliance d’inspection entre les couches applicative SAP et de base de données. **Preuves :** chemins de trafic, schéma de placement, budget prévisionnel de latence, table des rôles de volumes et observations d’E/S requises. **Livrable :** une solution de remplacement prise en charge avec compromis de capacité et de domaines de défaillance. Revoyez les [fondamentaux du réseau](../../fr/05-networking.md).

<a id="az-120-unit-3"></a>

## 3. Séparer le basculement sûr de la récupération historique

Expliquez HANA System Replication, le contrôle de cluster pris en charge, la protection ASCS/SCS, ERS, quorum, fencing, noms virtuels et sondes d’équilibreur de charge. Dessinez le seul nœud autorisé à écrire après une partition réseau. Définissez RPO et RTO métier, sauvegardes cohérentes pour la charge, journaux utilisables, rétention et dépendances de restauration. Montrez pourquoi la réplication peut copier une erreur et pourquoi un instantané non coordonné ne prouve pas la cohérence applicative.

**Scénario :** le pair ne peut pas être isolé par fencing et une erreur financière a déjà été répliquée. **Preuves :** décisions de cluster prévisionnelles, dépendances de fencing, règle de copie faisant autorité, disponibilité des sauvegardes/journaux et critères de validation de restauration. **Livrable :** des procédures séparées de haute disponibilité et de restauration, rejetant explicitement la désactivation du fencing comme réparation et incluant la réconciliation métier après récupération historique.

<a id="az-120-unit-4"></a>

## 4. Écrire une procédure de migration et d’intégration

Évaluez prise en charge de la source, versions, interfaces, rythme des changements, durée de transfert, indisponibilité et compatibilité de la cible. Choisissez une approche de migration prise en charge avec ses raisons. Définissez répétition, gel des écritures, synchronisation finale, isolation de la source, changements DNS/interfaces, vérifications techniques, acceptation métier et réouverture des écritures. Pour RISE, attribuez les responsabilités d’intégration client et de gestion SAP selon le contrat plutôt que selon un accès supposé aux abonnements.

**Scénario :** les utilisateurs créent des commandes d’achat après la bascule, puis le portail de recherche tombe en panne. **Preuves :** chronologie de propriété des écritures, état des files d’attente, points de transfert des interfaces, points de validation et décideurs. **Livrable :** retour arrière avant nouvelles écritures et décision distincte de réconciliation ou de migration inverse après écritures, incluant une escalade SAP lorsque la frontière défaillante appartient à RISE.

<a id="az-120-unit-5"></a>

## 5. Examiner l’exploitation et répéter la récupération régionale

Examinez un changement IaC fictif pour la prise en charge des images, le placement, le stockage, les références de secrets, les dépendances et les différences destructrices. Organisez les mises à jour par étapes avec un ordre tenant compte du cluster et des critères de retour arrière. Précisez collecte Azure Monitor, fournisseurs de supervision SAP, preuves de base de données et de cluster, responsables d’alertes et rétention. Récupérez le service complet dans une région secondaire, y compris identité, réseau, services centraux, applications, données, intégrations et synchronisation de retour au primaire.

**Scénario :** une interruption régionale survient pendant les achats alors qu’une proposition de redimensionnement est en attente. **Preuves :** ordre des dépendances, RPO/RTO prévisionnels, capacité en cas de panne, état de réplication, vérifications du processus métier et responsables des coûts récurrents de calcul/stockage/réseau/supervision. **Livrable :** un exercice d’incident sur table et un compte rendu d’examen du changement distinguant vérifications prévues et tests exécutés.

Utilisez les six références techniques du [guide](AZ-120.md) pour remettre les hypothèses à l’épreuve. Ces exercices originaux sélectionnent des concepts utiles ; ils ne couvrent pas tous les objectifs officiels et ne garantissent pas un résultat d’examen.
