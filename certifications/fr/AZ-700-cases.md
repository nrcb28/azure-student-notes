# AZ-700 · 10 cas avec réponses argumentées

[Guide](AZ-700.md) · [Cahier](AZ-700-workbook.md) · [Sommaire](README.md)

Scénarios originaux pour apprendre, sans question officielle ou confidentielle. Formuler l’exigence, écarter une alternative et identifier les preuves avant d’afficher la réponse. Aucune exécution dans Azure n’est revendiquée.

## 1. Le campus et un nouveau VNet utilisent tous deux 10.70.0.0/16. Un appairage ordinaire ou un VPN lève-t-il l’ambiguïté ?

<details>
<summary>Raisonnement</summary>

Les plages qui se chevauchent sont un problème de conception, pas une autorisation manquante. Inventorier les réseaux réels et choisir un espace sans chevauchement avant de construire un appairage standard ou une connexion hybride. Certaines architectures de traduction compatibles existent selon le cas, mais ajoutent des contraintes à concevoir explicitement. Un paquet destiné à la même plage privée n’indique pas à lui seul l’emplacement voulu. Les preuves seraient un inventaire, un plan d’adressage révisé et les routes attendues pour chaque destination.

</details>

## 2. A est appairé à B, et B à C. A ne rejoint pas C. Faut-il donner Owner à la VM source ?

<details>
<summary>Raisonnement</summary>

Non. L’appairage VNet n’est pas automatiquement transitif et un rôle d’administration Azure ne crée pas de chemin réseau manquant. Déterminer s’il faut une connexion directe ou un transit pris en charge. Examiner routes, transfert et sécurité dans les deux sens. Si une passerelle partagée intervient, vérifier ses paramètres précis de transit au lieu de supposer qu’elle transmet tout le trafic entre spokes. La preuve utile est un trajet complet et les prochains sauts effectifs, pas un rôle administratif plus large.

</details>

## 3. La nouvelle route par défaut pointe vers un pare-feu, mais un préfixe plus précis passe ailleurs. Toutes les routes utilisateur sont-elles cassées ?

<details>
<summary>Raisonnement</summary>

Pas nécessairement. Examiner toutes les routes applicables et la destination réelle. Une route par défaut large ne remplace pas forcément toutes les routes plus précises. Comparer préfixes, origine et prochain saut effectif selon les règles de sélection Azure. Vérifier aussi que la table attendue est associée au sous-réseau source. Les preuves doivent montrer les préfixes concurrents et le prochain saut observé. Modifier les règles de sécurité ne permet pas d’établir quelle route a été sélectionnée.

</details>

## 4. Les requêtes traversent une appliance à état, mais les réponses passent ailleurs. Pourquoi une connexion autorisée peut-elle échouer ?

<details>
<summary>Raisonnement</summary>

Un équipement à état peut devoir voir les deux sens d’une connexion. Avec un routage asymétrique, le retour peut éviter l’équipement qui a enregistré le flux initial ou atteindre un appareil sans état correspondant. Examiner aller, retour, transfert de l’appliance et éventuelle traduction d’adresses. Ne pas ajouter au hasard des règles entrantes avant de tester l’hypothèse. Un livrable utile contient les deux trajets et les observations des extrémités concernées ou d’outils de diagnostic compatibles.

</details>

## 5. Le stockage public est désactivé. L’API dispose d’un point privé mais résout encore l’adresse publique. Que vérifier d’abord ?

<details>
<summary>Raisonnement</summary>

Examiner le chemin DNS réel du client API : serveurs, zone privée, lien VNet et transfert hybride éventuel. Garder le nom du service et obtenir une résolution adaptée à la connexion privée prévue. Attribuer Storage Blob Data Reader ne corrige pas une réponse DNS publique. Une fois résolution et routage corrects, vérifier séparément l’autorisation sur les données. Noter nom, adresse résolue, résolveur, sous-ressource du point de terminaison et opération authentifiée ultérieure comme preuves distinctes.

</details>

## 6. Les données campus-Azure doivent être chiffrées. Acheter ExpressRoute suffit-il à établir cette propriété ?

<details>
<summary>Raisonnement</summary>

Non. La connectivité privée ExpressRoute est distincte du chiffrement et le trafic n’est pas chiffré par défaut. Définir ce qui doit être protégé et où commence et finit cette protection. MACsec est une option compatible pour les liaisons ExpressRoute Direct, pas une fonction automatiquement présente sur tout circuit fournisseur. Une conception IPsec adaptée peut répondre à une exigence de bout en bout. Comparer compatibilité, performance et gestion des clés. Un simple dessin de liaison privée ne prouve pas le chiffrement.

</details>

## 7. L’équipe veut une sélection régionale par DNS et pense que chaque requête traverse Traffic Manager. Que corriger ?

<details>
<summary>Raisonnement</summary>

Traffic Manager sélectionne les points de terminaison par DNS ; il n’agit pas comme proxy de chaque requête. Le client rejoint la destination choisie et le cache peut retarder l’effet d’un changement DNS. Si le besoin est une livraison HTTP mondiale par proxy, évaluer Azure Front Door selon les exigences. Pour un routage HTTP régional, examiner Application Gateway. Montrer séparément l’échange DNS et la connexion applicative, et expliquer comment la santé des destinations influence leur sélection.

</details>

## 8. Un point de terminaison de service est activé sur le sous-réseau. Pourquoi cela ne prouve-t-il pas une adresse privée du stockage ?

<details>
<summary>Raisonnement</summary>

Un point de terminaison de service et un point privé sont deux conceptions différentes. Activer le premier ne crée pas d’interface réseau privée du compte de stockage dans ce sous-réseau. Vérifier configuration du point de service, règles réseau du service et authentification. Si l’exigence demande précisément une destination privée, évaluer un point privé compatible avec ses réglages DNS et d’accès. Relever l’adresse résolue et la configuration réelle plutôt que prendre le mot commun « terminaison » pour une équivalence.

</details>

## 9. Une nouvelle règle de refus bloque les connexions neuves mais une session établie continue. Le NSG ignore-t-il nécessairement ses règles ?

<details>
<summary>Raisonnement</summary>

Non. Les NSG suivent l’état ; un changement de règle ne coupe donc pas forcément un flux existant immédiatement. Distinguer une connexion réellement nouvelle d’une session réutilisée, puis examiner les règles effectives du sous-réseau et de l’interface. Vérifier source, destination, port, protocole et priorité plutôt que le nom d’une règle. Préciser dans l’observation si le test a créé un nouveau flux. Élargir un rôle ou supprimer la VM n’expliquerait pas ce comportement.

</details>

## 10. Le schéma montre ExpressRoute et un VPN de secours. Quelles preuves manquent pour affirmer la résilience applicative ?

<details>
<summary>Raisonnement</summary>

Identifier les pannes communes et valider tout le chemin de secours. Vérifier équipements du client, fournisseurs, emplacements d’appairage, passerelles, annonces, retours, capacité du tunnel, DNS et reconnexion de l’application. Une seconde ligne dessinée ne prouve pas que le trafic la choisit correctement pendant une panne. Proposer un test isolé et autorisé avec résultats attendus et observés, critères de récupération et retour à la normale. Ces notes proposent la conception ; elles ne prétendent pas avoir exécuté ce basculement.

</details>

Les sources techniques et la référence d’examen consultée sont dans le [guide](AZ-700.md). Le [cahier](AZ-700-workbook.md) transforme les réponses en schémas et en preuves.
