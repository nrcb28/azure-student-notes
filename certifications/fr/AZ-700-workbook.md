# AZ-700 · Cahier avancé commun

[Guide](AZ-700.md) · [10 cas](AZ-700-cases.md) · [Sommaire](README.md) · [Laboratoire réseau](network-lab.md)

Cinq unités avec objectifs, scénarios et livrables correspondants dans les huit langues. Ce sont des exercices de conception et de diagnostic. Les prévisions ne sont pas des observations dans Azure et aucun nouveau déploiement n’est revendiqué.

<a id="az-700-unit-1"></a>

## 1. Construire un plan d’adressage et de dépendances

Concevoir les réseaux campus, hub, web et données de l’application. Inventorier les plages existantes avant de choisir des CIDR et réserver de l’espace pour croissance et sous-réseaux spécifiques aux services. Expliquer pourquoi un /24 ordinaire offre moins d’adresses IPv4 attribuables dans Azure que son nombre brut d’adresses. Ne pas supposer qu’un service délégué convient à n’importe quel sous-réseau vide.

**Scénario :** la plage d’un partenaire chevauche le hub prévu. **Preuves :** tableau avec propriétaire, préfixe, but, contraintes et réserve de croissance. **Livrable :** conception révisée sans chevauchement, conflit supprimé et une contrainte restant à vérifier dans la documentation actuelle.

<a id="az-700-unit-2"></a>

## 2. Tracer une requête et sa réponse

Dessiner un appel API depuis un spoke web, à travers une appliance d’inspection, vers un autre réseau. Noter préfixe destination, prochain saut et réglage de transfert à chaque étape. Dessiner séparément la réponse : inspection à état et traduction d’adresses peuvent faire échouer un retour asymétrique apparemment plausible. L’appairage seul ne fait pas du hub un routeur de transit.

**Scénario :** après une modification UDR, la source envoie des requêtes sans recevoir de réponse. **Preuves :** routes concurrentes et prochain saut effectif dans chaque sens. **Livrable :** hypothèse testable, observation de confirmation et condition de retour arrière pour la modification proposée.

<a id="az-700-unit-3"></a>

## 3. Diagnostiquer l’accès privé par couches

Décrire comment un client du campus résout un nom de stockage avec la conception DNS et le transfert choisis. Identifier sous-ressource du service, adresse privée, état d’approbation et restrictions réseau prévues du point privé. Séparer résolution, accessibilité réseau, TLS et permissions de données : prouver l’une ne prouve pas les autres.

**Scénario :** l’accès public est désactivé et l’appelant résout encore une adresse publique. **Preuves :** nom, chemin des résolveurs, adresse renvoyée et destination privée attendue. **Livrable :** correction DNS proposée, puis contrôles de routage et d’accès authentifié. Expliquer pourquoi une substitution permanente par une IP publique est inadaptée.

<a id="az-700-unit-4"></a>

## 4. Choisir les contrôles de livraison et de protection

Comparer un service TCP, une application web régionale et une mondiale. Sélectionner les candidats selon protocole, portée, routage et comportement en panne, pas sur une seule étiquette mémorisée. Inclure sondes et gestion des certificats. Distinguer sélection DNS et proxy des requêtes, inspection WAF, filtrage réseau et protection de disponibilité DDoS.

**Scénario :** un serveur passe sa sonde de santé alors que les téléchargements renvoient les mauvais documents. **Preuves :** ce que teste la sonde et ce que valide une opération réelle. **Livrable :** décision courte avec alternative écartée et signal fonctionnel qui arrêterait la promotion d’une version défectueuse.

<a id="az-700-unit-5"></a>

## 5. Concevoir et vérifier la récupération hybride

Prévoir la connexion principale et son secours. Lister pannes corrélées, changements de routage, exigences de chiffrement, capacité et dépendances applicatives. Le caractère privé d’ExpressRoute ne prouve pas son chiffrement par défaut. Préciser frontière de protection et conception compatible ; ne pas supposer les mêmes options pour tous les circuits.

**Scénario :** la connexion principale tombe pendant de nombreux téléchargements. **Preuves :** trajets aller et retour attendus, hypothèses de capacité du secours et critères mesurables de récupération applicative. **Livrable :** plan de test isolé, étapes de retour à la normale et colonnes attendu/observé. Sans environnement autorisé, rendre la conception et marquer explicitement les observations non testées.

[Guide officiel](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) · [Explications techniques](AZ-700.md)
