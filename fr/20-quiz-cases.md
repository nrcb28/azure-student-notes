# 32 scénarios pour s’entraîner

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

C’est un exercice court : ce n’est pas un examen officiel ou complet et le résultat ne prédit pas votre réussite à l’examen.

<a id="quiz-q01"></a>

## AZ-900 · Contrôle du système d’exploitation

Une application de laboratoire doit installer son propre pilote du noyau Linux. Quel hébergement répond le mieux à ce besoin ?

- **A.** Exécuter l’application dans Microsoft 365.
- **B.** Utiliser une machine virtuelle Azure avec une image Linux compatible.
- **C.** La déployer dans un environnement d’exécution géré d’App Service.
- **D.** Placer le pilote dans une Azure Function standard.

<details>
<summary>Pourquoi :</summary>

**B. Utiliser une machine virtuelle Azure avec une image Linux compatible.**

Le besoin décisif est de contrôler le système d’exploitation invité. Une VM Azure compatible permet à l’équipe de gérer cet environnement et ses pilotes, mais lui laisse aussi la maintenance du système. Une plateforme applicative gérée ne convient pas si elle ne donne pas le contrôle du noyau nécessaire.

- **A.** Microsoft 365 fournit des logiciels prêts à l’emploi, pas un hébergement pour des pilotes de noyau arbitraires.
- **C.** L’environnement géré d’App Service ne permet pas l’administration nécessaire du noyau invité.
- **D.** Une Function standard ne donne pas le contrôle nécessaire pour installer ce pilote.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [À revoir :](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · Mise à l’échelle horizontale et sessions

Une API de partage de notes ajoute des instances derrière un équilibreur de charge. Toute instance peut être remplacée, mais les utilisateurs doivent conserver leur session. Les sessions existent uniquement dans la mémoire de chaque instance. Que faut-il changer ?

- **A.** Augmenter le processeur de toutes les instances.
- **B.** Garder les sessions en mémoire et activer seulement l’affinité de session.
- **C.** Déplacer l’état des sessions vers un stockage externe partagé adapté.
- **D.** Attribuer une adresse IP publique à chaque instance.

<details>
<summary>Pourquoi :</summary>

**C. Déplacer l’état des sessions vers un stockage externe partagé adapté.**

La mise à l’échelle horizontale répartit les requêtes entre plusieurs instances. L’état important d’une session ne peut donc pas dépendre uniquement de la mémoire d’une instance. Un stockage externe adapté permet aux instances de remplacement de le retrouver. L’affinité seule ne préserve pas la mémoire d’une instance qui disparaît. L’application doit aussi gérer les accès et les pannes éventuelles de ce stockage.

- **A.** Plus de processeur ne préserve pas la mémoire lorsque l’instance est remplacée.
- **B.** Même avec l’affinité, la session est perdue si l’instance choisie disparaît.
- **D.** Une IP publique ne fournit pas un état de session partagé ou durable.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [À revoir :](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · Accès aux données de stockage

Un utilisateur possède Contributor sur un compte de stockage. Une requête Blob avec son identité Entra atteint le service, mais elle est refusée faute d’autorisation sur les données. Il doit seulement lire les blobs d’un conteneur. Quelle réponse respecte le moindre privilège ?

- **A.** Attribuer Storage Blob Data Reader à l’étendue de ce conteneur.
- **B.** Attribuer Owner sur toute la souscription.
- **C.** Ouvrir tous les ports réseau entrants.
- **D.** Transmettre à l’utilisateur la clé du compte de stockage.

<details>
<summary>Pourquoi :</summary>

**A. Attribuer Storage Blob Data Reader à l’étendue de ce conteneur.**

Les autorisations de gestion et celles sur les données Blob sont distinctes. Storage Blob Data Reader permet la lecture demandée, et l’étendue du conteneur limite l’accès au besoin indiqué. Le scénario identifie déjà un problème d’autorisation sur les données : des droits administratifs étendus ou des changements réseau sans rapport ne seraient pas une réponse proportionnée.

- **B.** Owner sur la souscription dépasse le besoin de lecture d’un seul conteneur.
- **C.** Ouvrir des ports ne donne pas l’autorisation manquante sur les données.
- **D.** Une clé de compte donne un accès bien plus large que nécessaire.

[Source :](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [À revoir :](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · Héritage des autorisations RBAC

Un utilisateur possède Reader directement sur une VM et appartient aussi à un groupe ayant Reader à l’étendue de la souscription. Vous supprimez uniquement l’attribution directe sur la VM. Il peut toujours lire la VM. Pourquoi ?

- **A.** Azure donne automatiquement Reader sur toutes les VM à chaque utilisateur.
- **B.** Une étiquette du groupe de ressources rétablit l’attribution supprimée.
- **C.** Retirer un rôle exige toujours de supprimer la VM.
- **D.** L’attribution du groupe continue de donner un accès hérité.

<details>
<summary>Pourquoi :</summary>

**D. L’attribution du groupe continue de donner un accès hérité.**

Supprimer une attribution ne retire pas les autorisations obtenues par une autre. Le groupe possède Reader sur la souscription : ses membres peuvent donc hériter de cet accès à la VM. Vérifiez les attributions directes, l’appartenance aux groupes et les étendues parentes avant de considérer l’accès restant comme une erreur du service ou d’ajouter des autorisations.

- **A.** Il n’existe pas d’attribution universelle de Reader à tous les utilisateurs.
- **B.** Les étiquettes classent les ressources et ne recréent pas les attributions de rôles.
- **C.** Retirer un rôle n’exige pas de supprimer la ressource protégée.

[Source :](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [À revoir :](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · Objectifs de récupération

Une architecture ne conserve des points de récupération valides de la base de données qu’une fois toutes les 24 heures. L’entreprise exige maintenant de perdre au maximum une heure de données récentes après un sinistre. Quel changement répond directement à cet écart ?

- **A.** Augmenter le processeur du serveur de l’API.
- **B.** Prévoir des points de protection des données récupérables espacés d’au plus une heure et valider la restauration.
- **C.** Ajouter un budget avec des alertes de coûts.
- **D.** Renommer le groupe de ressources en production.

<details>
<summary>Pourquoi :</summary>

**B. Prévoir des points de protection des données récupérables espacés d’au plus une heure et valider la restauration.**

Le RPO exprime en temps la quantité de données récentes que l’on accepte de perdre. Des points quotidiens seuls ne suffisent pas pour un objectif d’une heure. La protection doit produire des états récupérables assez souvent, et leur restauration doit être vérifiée. Plus de puissance applicative ou des étiquettes de coûts ne changent pas l’âge des données disponibles pour la récupération.

- **A.** Le processeur de l’API n’augmente pas la fréquence de protection des données.
- **C.** Un budget signale des dépenses, pas une perte de données.
- **D.** Le nom du groupe de ressources ne change pas la fréquence des points de récupération.

[Source :](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [À revoir :](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · DNS pour les connexions privées

L’accès public à un service de stockage est désactivé et un point de terminaison privé existe. Le client résout encore le nom du service vers son IP publique. Le chemin réseau privé est par ailleurs disponible. Que faut-il examiner en premier ?

- **A.** Donner au client Owner sur la souscription.
- **B.** Inscrire définitivement l’IP publique dans la configuration.
- **C.** Les zones DNS privées, leurs liens et le transfert DNS utilisés par ce client.
- **D.** Augmenter sans limite les nouvelles tentatives de l’application.

<details>
<summary>Pourquoi :</summary>

**C. Les zones DNS privées, leurs liens et le transfert DNS utilisés par ce client.**

Le client résout une mauvaise destination pour la connexion privée prévue. Vérifiez la configuration DNS privée recommandée pour le service et la manière dont ce client y accède, y compris les liens et le transfert DNS. Continuez à utiliser le nom du service. Corriger le DNS ne donne pas à lui seul des autorisations sur les données, mais des privilèges supplémentaires ou des tentatives infinies ne corrigent pas cet écart.

- **A.** Owner ne change pas la résolution de noms du client.
- **B.** L’adresse publique est la mauvaise destination lorsque l’accès public est désactivé.
- **D.** Répéter une requête ne corrige pas une mauvaise configuration DNS.

[Source :](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [À revoir :](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · Promotion de l’artefact testé

Un pipeline teste une image de conteneur, puis reconstruit depuis le code source pour la production avec des dépendances qui peuvent changer. Comment garantir que la production reçoit l’image qui a réussi les tests ?

- **A.** Tester à nouveau uniquement les commentaires du code.
- **B.** Utiliser l’étiquette latest sans enregistrer l’image qu’elle désigne.
- **C.** Omettre les tests puisque le commit du code source n’a pas changé.
- **D.** Promouvoir la même image testée, identifiée par un digest immuable.

<details>
<summary>Pourquoi :</summary>

**D. Promouvoir la même image testée, identifiée par un digest immuable.**

Un même commit peut produire des résultats différents si les outils, les dépendances ou les images de base changent. Promouvoir l’image déjà testée évite cette différence liée à la reconstruction. Un digest immuable identifie l’artefact précis, tandis qu’une étiquette peut changer de cible. La configuration des environnements demande toujours sa propre validation et une gestion contrôlée.

- **A.** Les commentaires du code n’identifient pas l’artefact construit.
- **B.** Une étiquette modifiable peut désigner une autre image plus tard.
- **C.** Un commit inchangé ne prouve pas que la reconstruction produit un résultat identique.

[Source :](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [À revoir :](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · Signaux d’un déploiement canary

Une version canary affiche une utilisation normale du processeur et de la mémoire, mais ses téléchargements de documents renvoient de mauvais fichiers. Sur quoi doit reposer la décision de poursuivre le déploiement ?

- **A.** Sur des signaux de justesse fonctionnelle et un critère défini d’arrêt ou de retour arrière.
- **B.** Sur le processeur seul, car une infrastructure saine prouve que les résultats sont corrects.
- **C.** Sur une VM plus puissante avant de vérifier les fichiers renvoyés.
- **D.** Sur la suppression des anciens journaux pour rendre le tableau de bord plus propre.

<details>
<summary>Pourquoi :</summary>

**A. Sur des signaux de justesse fonctionnelle et un critère défini d’arrêt ou de retour arrière.**

Une version peut consommer peu de ressources et produire tout de même des résultats incorrects. Sa promotion demande des signaux liés à l’opération de l’utilisateur, en plus des métriques d’infrastructure. Un critère défini d’arrêt ou de retour arrière permet d’agir sur ces éléments. Vérifiez aussi la compatibilité des données : revenir au code précédent n’annule pas automatiquement les changements nuisibles apportés aux données par la version.

- **B.** Le processeur et la mémoire ne prouvent pas que les utilisateurs reçoivent les bons documents.
- **C.** Plus de puissance de calcul ne corrige pas automatiquement une sortie erronée de l’application.
- **D.** Supprimer les preuves complique l’enquête et ne corrige pas les résultats.

[Source :](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [À revoir :](12-devops.md)

</details>

<a id="quiz-q09"></a>

## DP-900 · Charges transactionnelles

Un service d'inscription universitaire doit réserver la dernière place d'un TP et créer l'inscription de l'étudiant en une seule opération cohérente. Quelle description de charge de travail correspond le mieux à ce besoin ?

- **A.** Une charge analytique qui regroupe les inscriptions par semestre.
- **B.** Une charge par lots qui rapproche chaque nuit des mises à jour indépendantes du nombre de places.
- **C.** Une charge transactionnelle qui valide ensemble les modifications liées.
- **D.** Une charge de traitement en continu qui publie séparément les événements de place et d'inscription, sans coordonner leur validation.

<details>
<summary>Pourquoi :</summary>

**C. Une charge transactionnelle qui valide ensemble les modifications liées.**

Le besoin porte sur une opération précise dont les modifications liées doivent réussir ou échouer ensemble. C'est un comportement transactionnel : une autre demande ne doit pas réserver la même dernière place alors que les enregistrements d'inscription et de capacité se contredisent. Les rapports historiques relèvent de l'analyse, avec d'autres modes d'accès. Des événements et un rapprochement ultérieur peuvent compléter l'architecture, mais des mises à jour indépendantes ne suffisent pas à garantir la cohérence demandée.

- **A.** Le regroupement par semestre répond à des questions historiques ; il ne coordonne pas la réservation et l'inscription requises pour cette demande en cours.
- **B.** Un rapprochement nocturne laisse une période où le nombre de places et les inscriptions peuvent diverger, contrairement à l'exigence de cohérence immédiate.
- **D.** Des événements peuvent informer d'autres systèmes, mais leur validation séparée ne rend pas, à elle seule, les deux modifications sources atomiques.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing) · [À revoir :](../certifications/fr/DP-900.md)

</details>

<a id="quiz-q10"></a>

## DP-900 · Ordre ETL et ELT

Une équipe de recherche extrait les enregistrements de téléchargement de la veille, supprime les identifiants invalides dans un service de traitement, puis charge les données nettoyées dans son entrepôt de reporting. Quelle description correspond à cet ordre ?

- **A.** ETL, car la transformation précède le chargement dans la cible de reporting.
- **B.** ELT, car tout flux aboutissant à un entrepôt effectue sa transformation dans cet entrepôt.
- **C.** Traitement en continu, car les téléchargements proviennent initialement d'événements applicatifs.
- **D.** Orchestration seule, car coordonner les étapes supprime le besoin de transformation.

<details>
<summary>Pourquoi :</summary>

**A. ETL, car la transformation précède le chargement dans la cible de reporting.**

ETL signifie extraire, transformer, puis charger dans la cible prévue. Ici, les identifiants invalides sont traités avant que l'entrepôt de reporting reçoive les enregistrements nettoyés. Avec ELT, les données seraient d'abord chargées, puis transformées grâce aux capacités de la cible. La collection délimitée des données de la veille constitue une entrée par lots. Un orchestrateur peut coordonner ces activités, mais orchestration et transformation désignent des responsabilités différentes dans le même pipeline.

- **B.** ELT suppose un chargement avant la transformation dans la cible ; choisir un entrepôt comme destination ne détermine pas, à lui seul, cet ordre.
- **C.** L'origine événementielle ne rend pas ce traitement continu : le travail porte sur une collection quotidienne délimitée, pas sur des données qui arrivent en permanence.
- **D.** L'orchestration coordonne les dépendances et la reprise ; supprimer des identifiants invalides modifie les données et reste une responsabilité de transformation distincte.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) · [À revoir :](../certifications/fr/DP-900.md)

</details>

<a id="quiz-q11"></a>

## SC-900 · Catégories de facteurs MFA

Un étudiant compare des modes de connexion. Quel exemple associe un facteur de connaissance à un facteur de possession, en supposant que l'appareil d'authentification est enregistré et que son approbation est obligatoire ?

- **A.** Un mot de passe, puis une réponse mémorisée à une question de sécurité.
- **B.** Un mot de passe universitaire, puis un autre mot de passe de service mémorisé.
- **C.** Un mot de passe, puis un code PIN mémorisé saisi sur le même site, sans authentificateur lié à un appareil.
- **D.** Un mot de passe, puis une approbation sur l'appareil d'authentification enregistré de l'étudiant.

<details>
<summary>Pourquoi :</summary>

**D. Un mot de passe, puis une approbation sur l'appareil d'authentification enregistré de l'étudiant.**

Un mot de passe représente une information que l'étudiant connaît, tandis que le contrôle d'un appareil d'authentification enregistré apporte un facteur de possession. Exiger les deux associe donc des catégories de facteurs différentes. Deux secrets mémorisés restent des facteurs de connaissance, même s'ils diffèrent. Cela ne rend pas toutes les méthodes MFA aussi résistantes à l'hameçonnage : le choix de la méthode, l'enregistrement, la récupération et l'application effective doivent aussi être pris en compte dans la politique universitaire.

- **A.** Le mot de passe et la réponse mémorisée sont tous deux des facteurs de connaissance ; une vérification supplémentaire de connaissance n'ajoute pas le facteur de possession demandé.
- **B.** Des mots de passe distincts peuvent séparer des identifiants, mais restent deux secrets mémorisés appartenant à la même catégorie de facteurs.
- **C.** L'énoncé exclut un authentificateur lié à un appareil : un PIN saisi comme autre secret du site apporte de la connaissance, pas une preuve de possession.

[Source :](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [À revoir :](../certifications/fr/SC-900.md)

</details>

<a id="quiz-q12"></a>

## SC-900 · Gestion des données avec Purview

Une université doit détecter les identifiants étudiants lors d'activités prises en charge de partage documentaire, puis avertir ou limiter le partage externe lorsqu'une règle configurée correspond. Quelle fonctionnalité Purview répond le plus directement à ce besoin ?

- **A.** Audit, utilisé uniquement pour enregistrer qu'un partage a eu lieu.
- **B.** La prévention contre la perte de données (DLP), avec une stratégie au périmètre adapté et testée.
- **C.** La conservation, configurée pour garder les documents sept ans.
- **D.** Une étiquette de confidentialité nommée Confidentiel, sans configuration de protection ni de DLP.

<details>
<summary>Pourquoi :</summary>

**B. La prévention contre la perte de données (DLP), avec une stratégie au périmètre adapté et testée.**

La DLP évalue les informations sensibles et les activités correspondantes selon des stratégies configurées, et peut avertir ou limiter les actions prises en charge. La conception doit préciser les emplacements, les conditions de détection, les destinataires, les exceptions et la réponse attendue. Audit fournit des traces d'activité, la conservation gère le cycle de vie et une étiquette indique une classification ou applique une protection configurée. Son nom seul n'établit pas la restriction de partage externe décrite.

- **A.** Audit aide à enquêter en enregistrant l'activité ; enregistrer un partage ne produit pas, à lui seul, l'avertissement ou la restriction demandés.
- **C.** Conserver un document pendant une durée définie régit son cycle de vie, mais ne décide pas si cette activité de partage externe doit être autorisée.
- **D.** Le nom d'une étiquette ne configure aucune restriction de partage ; une protection ou une stratégie DLP adaptée doit mettre en œuvre le comportement attendu.

[Source :](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [À revoir :](../certifications/fr/SC-900.md)

</details>

<a id="quiz-q13"></a>

## AZ-700 · Routage au préfixe le plus long

Une VM de TP possède deux routes effectives actives : une route définie par l'utilisateur 0.0.0.0/0 vers une appliance réseau et une route système 10.20.0.0/16 par peering de réseaux virtuels. Aucune route plus précise n'existe. Quel prochain saut est choisi pour 10.20.7.5 ?

- **A.** Le peering de réseaux virtuels, car le préfixe /16 correspondant est plus précis.
- **B.** L'appliance réseau, car les routes définies par l'utilisateur priment toujours sur toutes les routes système.
- **C.** Les deux prochains sauts, car Azure duplique les paquets sur toutes les routes correspondantes.
- **D.** Aucun prochain saut, car des préfixes correspondants qui se chevauchent invalident la table de routage.

<details>
<summary>Pourquoi :</summary>

**A. Le peering de réseaux virtuels, car le préfixe /16 correspondant est plus précis.**

Azure choisit d'abord la route correspondante dont le préfixe est le plus long. La destination appartient à 10.20.0.0/16, plus précis que 0.0.0.0/0 : ce paquet suit donc la route de peering active. La préférence entre sources de routes intervient lorsque les routes applicables ont la même longueur de préfixe ; elle ne donne pas une priorité universelle à une route par défaut définie par l'utilisateur. Choisir un prochain saut ne garantit encore ni autorisation du pare-feu ni accès applicatif.

- **B.** La préférence entre sources ne remplace pas ici le choix du préfixe le plus long ; la route par défaut définie par l'utilisateur est moins précise que la route de peering active.
- **C.** Le routage ordinaire par destination choisit la route correspondante préférée ; il ne copie pas le paquet vers chaque prochain saut dont le préfixe correspond.
- **D.** Le chevauchement des préfixes est normal dans une table de routage ; une route par défaut peut coexister avec des routes plus précises sans l'invalider.

[Source :](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) · [À revoir :](../certifications/fr/AZ-700.md)

</details>

<a id="quiz-q14"></a>

## AZ-700 · Chiffrement ExpressRoute

Une université utilise ExpressRoute et exige un chiffrement entre son équipement VPN sur le campus et une passerelle VPN Azure. ExpressRoute doit rester le réseau de transport sous-jacent. Quelle conception respecte le plus directement ce périmètre ?

- **A.** Activer MACsec sur les liaisons ExpressRoute Direct prises en charge et considérer cette protection physique comme couvrant tout le trajet campus-passerelle.
- **B.** Utiliser le peering privé ExpressRoute sans autre mécanisme de chiffrement, car le routage privé chiffre toutes les données utiles.
- **C.** Utiliser un tunnel IPsec pris en charge sur ExpressRoute, en validant le routage, la compatibilité des passerelles et le débit nécessaire.
- **D.** Activer TLS uniquement entre l'application Azure et sa base de données, en laissant le trajet campus-passerelle non chiffré.

<details>
<summary>Pourquoi :</summary>

**C. Utiliser un tunnel IPsec pris en charge sur ExpressRoute, en validant le routage, la compatibilité des passerelles et le débit nécessaire.**

ExpressRoute fournit une connectivité privée, mais ne chiffre pas automatiquement les données utiles. Une surcouche IPsec prise en charge peut protéger la connexion demandée, de l'équipement VPN du campus à la passerelle VPN Azure, en utilisant ExpressRoute comme transport. MACsec protège les liaisons physiques ExpressRoute Direct compatibles, soit un autre périmètre. La proposition doit aussi valider le routage, les configurations de passerelles prises en charge, la capacité et le comportement en panne : le chiffrement seul ne suffit pas à finaliser la conception.

- **A.** MACsec protège les liaisons physiques Direct compatibles ; ce segment ne couvre pas, à lui seul, tout le périmètre demandé entre l'équipement du campus et la passerelle Azure.
- **B.** Le peering privé modifie la connectivité et le routage, mais ne chiffre pas automatiquement les données sur la connexion campus-passerelle exigée.
- **D.** TLS entre l'application et la base protège un autre segment ; il ne traite pas le périmètre explicitement demandé entre l'équipement VPN du campus et la passerelle Azure.

[Source :](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption) · [À revoir :](../certifications/fr/AZ-700.md)

</details>

<a id="quiz-q15"></a>

## DP-300 · Restauration SQL à un instant donné

À 14 h 20, une université découvre une mise à jour destructrice d'Azure SQL Database, validée à 13 h et déjà répliquée. La rétention des sauvegardes automatiques couvre 12 h 59. L'objectif est de retrouver cet état antérieur avec le moins de perte évitable. Quel plan de récupération convient le mieux ?

- **A.** Promouvoir le réplica synchronisé actuel et supposer que la mise à jour validée disparaît.
- **B.** Restaurer l'état de 12 h 59 dans une nouvelle base, le valider et prévoir la reconnexion contrôlée de l'application ainsi que le rapprochement éventuel des données ultérieures.
- **C.** Restaurer une sauvegarde conservée datant de deux jours alors que le point de 12 h 59 est disponible.
- **D.** Lancer une restauration à un instant donné et supposer qu'Azure écrase la base de production et redirige automatiquement tous les clients.

<details>
<summary>Pourquoi :</summary>

**B. Restaurer l'état de 12 h 59 dans une nouvelle base, le valider et prévoir la reconnexion contrôlée de l'application ainsi que le rapprochement éventuel des données ultérieures.**

La restauration à un instant donné permet de retrouver un état conservé antérieur à la transaction destructrice. Pour Azure SQL Database, elle crée une base : sa validation et la reconnexion contrôlée de l'application font donc partie du plan de récupération. Le traitement des activités légitimes survenues ensuite doit également faire l'objet d'une décision explicite. Le réplica synchronisé contient déjà la mauvaise mise à jour ; le promouvoir ne rétablit ni l'exactitude historique ni l'état à l'instant demandé.

- **A.** Le réplica a déjà reçu la modification destructrice validée ; promouvoir cette copie actuelle ne retrouve pas l'état correct antérieur de la base.
- **C.** La sauvegarde plus ancienne abandonne inutilement davantage d'historique alors que la rétention permet le point requis avant la mise à jour et une perte évitable minimale.
- **D.** La restauration à un instant donné de SQL Database crée une base ; l'équipe doit la valider et gérer les connexions applicatives sans supposer un remplacement automatique.

[Source :](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups) · [À revoir :](../certifications/fr/DP-300.md)

</details>

<a id="quiz-q16"></a>

## DP-300 · Périmètres de chiffrement SQL

Une application de recherche doit rendre certaines valeurs de participants illisibles aux administrateurs de base qui interrogent les tables. Seul son client de confiance peut les déchiffrer, et les administrateurs ne doivent pas disposer des clés du client. Quelle approche correspond le mieux à ce périmètre ?

- **A.** Activer TDE et laisser aux administrateurs leurs droits habituels de requête.
- **B.** Exiger TLS entre le client et la base, sans chiffrer les valeurs sélectionnées côté client.
- **C.** Appliquer le masquage dynamique des données tout en conservant les droits de requête étendus des administrateurs.
- **D.** Utiliser Always Encrypted correctement configuré, avec un client compatible et des clés gérées séparément.

<details>
<summary>Pourquoi :</summary>

**D. Utiliser Always Encrypted correctement configuré, avec un client compatible et des clés gérées séparément.**

Always Encrypted vise un périmètre où des clients compatibles chiffrent et déchiffrent les valeurs sensibles, tandis que les clés peuvent rester hors de portée du moteur de base de données. L'université doit valider les pilotes, les opérations permises et la gestion séparée des clés. TDE protège les fichiers au repos, TLS protège la connexion et le masquage modifie la présentation des résultats. Ces contrôles ne satisfont pas, à eux seuls, l'exigence d'exclusion des administrateurs.

- **A.** TDE protège les fichiers au repos ; des administrateurs disposant de droits de requête normaux peuvent encore obtenir les valeurs en clair par le moteur de base de données.
- **B.** TLS protège les données en transit sur la connexion, mais n'empêche pas, à lui seul, un administrateur autorisé d'interroger les valeurs stockées.
- **C.** Le masquage modifie la présentation des résultats pour les utilisateurs concernés ; il ne crée pas de séparation cryptographique face à des administrateurs gardant des privilèges étendus.

[Source :](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview) · [À revoir :](../certifications/fr/DP-300.md)

</details>

<a id="quiz-q17"></a>

## AI-901 · Identité du client Foundry

Le client Foundry d'un étudiant utilise le point de terminaison et le nom de déploiement documentés, mais aucun identifiant d'authentification n'est configuré pour la charge appelante. Que faut-il ajouter pour établir l'identité d'un appelant autorisé ?

- **A.** Remplacer le nom de déploiement par le nom du modèle du catalogue, toujours sans identifiant d'authentification.
- **B.** Configurer un identifiant d'authentification pris en charge pour la charge et accorder à cette identité l'accès minimal requis.
- **C.** Passer de REST à un SDK tout en laissant l'appelant non authentifié.
- **D.** Copier dans le client l'URL de portail d'un administrateur connecté comme preuve de l'autorisation de la charge.

<details>
<summary>Pourquoi :</summary>

**B. Configurer un identifiant d'authentification pris en charge pour la charge et accorder à cette identité l'accès minimal requis.**

Un point de terminaison indique où envoyer la demande et un déploiement identifie le modèle configuré ; aucun des deux n'établit qui appelle. Le client a besoin d'un mécanisme d'authentification pris en charge, et l'identité obtenue doit posséder les autorisations minimales adaptées. Le SDK et la génération d'API choisis doivent aussi être compatibles. Les secrets doivent rester hors des notebooks et du code source ; l'accès au portail d'un administrateur humain n'est pas automatiquement transmis à l'application.

- **A.** Le nom du modèle au catalogue et le nom du déploiement ont des rôles différents ; modifier cette chaîne n'authentifie pas la charge et n'accorde aucun accès.
- **C.** Un SDK encapsule des contrats de requête pris en charge, mais changer de bibliothèque ne supprime pas les exigences d'authentification et d'autorisation du service.
- **D.** Une URL de portail indique un emplacement ; la session authentifiée de l'administrateur dans son navigateur n'établit ni l'identité ni les autorisations de la charge distincte.

[Source :](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [À revoir :](../certifications/fr/AI-901.md)

</details>

<a id="quiz-q18"></a>

## AI-901 · Ancrage et justification des affirmations

Un assistant de notes donne une date de remise et cite le bon PDF de cours, mais le passage récupéré définit seulement un algorithme. L'application doit répondre aux questions de dates uniquement à partir de passages autorisés qui les étayent. Quelle est la meilleure réponse ?

- **A.** Récupérer un passage qui étaye la date, ou indiquer que les éléments disponibles sont insuffisants.
- **B.** Accepter la date, car citer le bon document prouve toutes les affirmations de la réponse.
- **C.** Régler la température de génération à zéro et accepter la même date sans vérifier un autre passage.
- **D.** Accepter la date si le modèle indique une forte confiance, même si le passage ne l'étaye pas.

<details>
<summary>Pourquoi :</summary>

**A. Récupérer un passage qui étaye la date, ou indiquer que les éléments disponibles sont insuffisants.**

L'ancrage exige une preuve soutenant l'affirmation précise, pas simplement une citation d'un document lié au sujet. La définition d'algorithme fournie n'établit aucune date de remise. La recherche doit trouver un passage autorisé contenant la date pertinente et ses conditions ; sinon, l'assistant doit s'abstenir. Une génération déterministe et la confiance déclarée par le modèle ne créent pas les preuves manquantes. L'évaluation doit comparer chaque affirmation ayant des conséquences au texte réellement cité.

- **B.** Une citation du bon document peut pointer vers un passage sans rapport ; l'identité du document ne suffit pas à justifier la date annoncée.
- **C.** Une température plus basse change la variabilité de génération, mais ne transforme pas une définition d'algorithme en preuve d'une date de remise absente.
- **D.** La confiance du modèle peut être erronée ; la règle explicite de l'application exige toujours un passage autorisé qui étaye précisément cette date.

[Source :](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [À revoir :](../certifications/fr/AI-901.md)

</details>

<a id="quiz-q19"></a>

## SC-200 · Preuves temporelles du SOC

Des données synthétiques du même compte vérifié montrent une activité de messagerie à 10 h 02 UTC, ingérée à 10 h 20, et une connexion à 10 h 08 UTC, ingérée à 10 h 09. Les deux horloges d'événement sont fiables. Quelle conclusion ces seuls enregistrements permettent-ils ?

- **A.** La connexion a eu lieu d'abord, car son enregistrement est arrivé en premier dans l'espace de travail.
- **B.** Le courriel a causé la connexion et prouve la compromission du compte.
- **C.** L'heure de l'événement de messagerie doit être écartée, car son ingestion a été retardée.
- **D.** L'activité de messagerie a précédé la connexion ; la causalité et la compromission nécessitent encore d'autres éléments.

<details>
<summary>Pourquoi :</summary>

**D. L'activité de messagerie a précédé la connexion ; la causalité et la compromission nécessitent encore d'autres éléments.**

Les horodatages fiables des événements placent l'activité de messagerie avant la connexion. Les horodatages d'ingestion indiquent l'arrivée des enregistrements ; des retards de collecte différents peuvent inverser cet ordre d'arrivée. Associer le même compte vérifié aide à corréler les données, mais ne prouve ni que le courriel a causé la connexion ni que l'un des événements était malveillant. L'analyste doit préserver les deux champs temporels, examiner l'activité environnante et préciser les limites des éléments disponibles.

- **A.** L'ordre d'ingestion décrit l'arrivée de la collecte, pas l'ordre des activités ; les horodatages fiables placent ici la messagerie avant la connexion.
- **B.** Un compte commun et une séquence temporelle justifient une enquête, mais n'établissent seuls ni causalité, ni activité malveillante, ni compromission confirmée.
- **C.** Une ingestion retardée n'invalide pas nécessairement un horodatage d'événement fiable ; il faut conserver les deux champs et examiner le retard plutôt qu'écarter la preuve.

[Source :](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · [À revoir :](../certifications/fr/SC-200.md)

</details>

<a id="quiz-q20"></a>

## SC-200 · Idempotence des actions de réponse

Un playbook Sentinel crée un ticket d'incident universitaire, mais la réponse de réussite est perdue. Une nouvelle tentative pourrait créer un autre ticket pour la même action approuvée. Quel contrôle du flux traite le mieux cette défaillance ?

- **A.** Allonger le délai d'attente et supposer qu'une réponse absente signifie toujours qu'aucun ticket n'existe.
- **B.** Générer un nouvel identifiant d'action à chaque tentative pour que chaque demande paraisse indépendante.
- **C.** Conserver durablement une clé incident/action et l'état du ticket, puis rapprocher ou réutiliser le résultat existant lors d'une nouvelle tentative de cette action.
- **D.** Dédupliquer uniquement les alertes entrantes, tout en laissant la création de ticket se répéter sans vérifier l'état.

<details>
<summary>Pourquoi :</summary>

**C. Conserver durablement une clé incident/action et l'état du ticket, puis rapprocher ou réutiliser le résultat existant lors d'une nouvelle tentative de cette action.**

L'idempotence signifie que répéter une même action logique préserve son résultat prévu au lieu de produire un effet supplémentaire. Une clé incident/action durable, un état enregistré et une référence de ticket externe permettent de retrouver ou rapprocher le travail existant lors des reprises. Une réponse absente laisse le résultat inconnu jusqu'à vérification. Le flux doit aussi prévoir des tentatives limitées, un responsable identifié et des droits adaptés à la création de tickets ; dédupliquer les alertes ne contrôle pas l'exécution des actions.

- **A.** Un délai plus long peut réduire certaines défaillances, mais une réponse perdue laisse toujours un doute sur la création effective du ticket externe.
- **B.** Un nouvel identifiant fait passer la reprise pour un nouveau travail et empêche le flux de reconnaître l'action logique déjà tentée.
- **D.** La déduplication des alertes contrôle les entrées ; une étape ultérieure rejouée peut encore créer des doublons sans ses propres vérifications d'état d'exécution.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) · [À revoir :](../certifications/fr/SC-200.md)

</details>

<a id="quiz-q21"></a>

## SC-300 · Accès conditionnel : rapport uniquement

Une université teste une stratégie d'accès conditionnel en mode Rapport uniquement. L'évaluation indique qu'une connexion ne satisferait pas la condition d'octroi proposée, mais la connexion réussit. Aucune autre stratégie n'exige ce contrôle. Quelle explication convient le mieux ?

- **A.** Les autorisations applicatives priment toujours sur un refus d'accès conditionnel appliqué.
- **B.** Le contrôle proposé est déjà appliqué, puisque le mode Rapport uniquement l'évalue.
- **C.** Le mode Rapport uniquement enregistre l'évaluation de la stratégie sans imposer sa condition d'octroi.
- **D.** Le mode Rapport uniquement autorise le premier échec, puis bloque automatiquement la connexion suivante.

<details>
<summary>Pourquoi :</summary>

**C. Le mode Rapport uniquement enregistre l'évaluation de la stratégie sans imposer sa condition d'octroi.**

Le mode Rapport uniquement évalue la stratégie et enregistre le résultat prévu sans appliquer ses contrôles. Une connexion réussie peut donc coexister avec un résultat indiquant que la condition d'octroi échouerait si elle était imposée. Avant un déploiement approuvé, l'équipe doit examiner les cas attendus d'autorisation et de refus, les identités concernées, les exclusions et les possibilités de récupération pour les administrateurs. Les autorisations applicatives constituent un périmètre distinct et n'annulent pas un refus d'accès conditionnel effectivement appliqué.

- **A.** Le droit d'utiliser une application ne prime pas automatiquement sur un refus d'accès conditionnel applicable et imposé ; le mode de la stratégie explique ici la connexion réussie.
- **B.** L'évaluation et l'application sont distinctes : Rapport uniquement enregistre ce qui se passerait ; son résultat ne prouve pas que la condition d'octroi a été imposée.
- **D.** Rapport uniquement n'autorise pas un premier essai avant une application automatique ; imposer le contrôle nécessite de modifier la configuration de la stratégie concernée.

[Source :](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · [À revoir :](../certifications/fr/SC-300.md)

</details>

<a id="quiz-q22"></a>

## SC-300 · Revendications de fédération de charge

Un travail de build universitaire utilise la fédération d'identité de charge de travail. L'échange de jetons échoue : le subject du jeton externe diffère par la casse de celui configuré dans l'identifiant fédéré. L'issuer et l'audience correspondent. Quelle modification corrige cet écart identifié ?

- **A.** Accorder à la charge le rôle Propriétaire de l'abonnement sans modifier le subject fédéré.
- **B.** Aligner exactement le subject configuré sur la revendication entrante prévue, puis vérifier séparément les autorisations minimales de l'identité sur les ressources.
- **C.** Ajouter des correspondances de provisionnement utilisateur SCIM pour le nom du dépôt au lieu de corriger l'identifiant fédéré.
- **D.** Augmenter la durée de vie du jeton externe sans modifier le subject qui ne correspond pas.

<details>
<summary>Pourquoi :</summary>

**B. Aligner exactement le subject configuré sur la revendication entrante prévue, puis vérifier séparément les autorisations minimales de l'identité sur les ressources.**

Les identifiants fédérés comparent l'émetteur approuvé, le subject et l'audience à l'assertion entrante ; ces valeurs doivent correspondre, y compris la casse. Corriger la relation de subject prévue résout l'écart indiqué lors de l'échange sans introduire de secret client stocké. Un échange réussi authentifie ensuite la charge, mais n'accorde pas un accès arbitraire aux ressources. L'identité obtenue doit toujours recevoir séparément des autorisations au périmètre adapté aux opérations réelles du build.

- **A.** Les autorisations de ressource déterminent les actions d'une identité authentifiée ; un rôle étendu ne corrige pas une revendication incorrecte qui empêche l'échange de jetons.
- **C.** SCIM concerne le provisionnement des comptes et leurs attributs ; il ne remplace pas les vérifications d'issuer, de subject et d'audience dans cet échange de jetons de charge.
- **D.** Modifier la durée de vie change la période de validité du jeton, mais ne fait pas correspondre le subject sensible à la casse à l'identifiant fédéré configuré.

[Source :](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · [À revoir :](../certifications/fr/SC-300.md)

</details>

<a id="quiz-q23"></a>

## AZ-140 · Autorisations des profils AVD

Un étudiant peut lancer sa session Azure Virtual Desktop mutualisée, mais FSLogix reçoit un refus d'accès à son dossier de profil SMB. L'accès au niveau du partage existe, mais les autorisations NTFS du dossier refusent l'étudiant. Quelle correction répond le mieux aux éléments observés ?

- **A.** Corriger les autorisations NTFS du dossier en isolant correctement les utilisateurs, puis vérifier l'attachement du profil avec l'identité de cet étudiant.
- **B.** Accorder à l'étudiant un rôle Contributeur Azure plus étendu sur le plan de contrôle, sans changer les autorisations du dossier.
- **C.** Réattribuer le groupe d'applications de bureau et supposer que cette attribution accorde aussi l'accès NTFS au profil.
- **D.** Réinstaller l'hôte de session en conservant le même chemin de profil et les autorisations NTFS qui refusent l'accès.

<details>
<summary>Pourquoi :</summary>

**A. Corriger les autorisations NTFS du dossier en isolant correctement les utilisateurs, puis vérifier l'attachement du profil avec l'identité de cet étudiant.**

L'accès au profil SMB dépend à la fois des droits sur le partage et des autorisations du système de fichiers. Les éléments fournis identifient un refus NTFS : corriger l'accès prévu au dossier tout en préservant l'isolation des autres étudiants traite donc la panne immédiate. Il faut tester avec l'identité concernée et examiner les traces d'attachement FSLogix. L'accès au bureau et l'administration des ressources Azure sont des périmètres différents ; lancer une session ne prouve pas le droit de lire et d'écrire le profil persistant.

- **B.** Un rôle de gestion du plan de contrôle ne corrige pas, à lui seul, le refus NTFS identifié sur le dossier SMB du profil étudiant.
- **C.** L'attribution du groupe d'applications rend le bureau accessible, mais n'accorde pas à elle seule les droits de système de fichiers requis sur le stockage du profil.
- **D.** Remplacer l'hôte en conservant le refus d'accès au même dossier laisse le problème de permissions de stockage dans le parcours de la nouvelle session.

[Source :](https://learn.microsoft.com/en-us/fslogix/how-to-configure-storage-permissions) · [À revoir :](../certifications/fr/AZ-140.md)

</details>

<a id="quiz-q24"></a>

## AZ-140 · Réserve AVD en cas de panne

Un TP AVD synthétique nécessite 60 sessions étudiantes simultanées. Les tests autorisent au plus 10 sessions par hôte sain. Tous les hôtes doivent être prêts avant le cours, et il faut encore pouvoir assurer 60 sessions après la panne de n'importe quel hôte. Quel est le nombre minimal d'hôtes prêts ?

- **A.** Six hôtes.
- **B.** Cinq hôtes.
- **C.** Huit hôtes.
- **D.** Sept hôtes.

<details>
<summary>Pourquoi :</summary>

**D. Sept hôtes.**

Six hôtes sains couvrent la demande normale mesurée : 60 divisées par 10 sessions par hôte. Un hôte supplémentaire déjà prêt fournit la réserve demandée pour une panne unique, en laissant six hôtes après celle-ci. Sept est donc le minimum selon ces hypothèses explicites. Le plan réel doit aussi considérer le temps de démarrage, le drainage, la capacité défaillante, la charge de stockage à la connexion et les autorisations ; démarrer plus tard un hôte arrêté ne satisfait pas l'exigence de disponibilité avant le cours.

- **A.** Six hôtes ne couvrent la demande que s'ils restent tous sains ; en perdre un limite la capacité à 50 sessions selon la limite mesurée.
- **B.** Cinq hôtes ne fournissent que 50 sessions avant même une panne ; ils ne peuvent pas accueillir les 60 étudiants simultanés selon ces hypothèses.
- **C.** Huit hôtes conviennent, mais sept laissent déjà six hôtes sains après une panne ; huit dépasse donc le minimum requis.

[Source :](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan) · [À revoir :](../certifications/fr/AZ-140.md)

</details>

<a id="quiz-q25"></a>

## AI-103 · Révocation d'accès lors de la recherche

Un étudiant perd l'autorisation d'accéder à un notebook de recherche, mais un assistant en conserve des passages en cache. La politique exige un accès actuel avant tout envoi d'un passage au modèle. L'application ne peut pas établir que les autorisations sont à jour. Quel comportement respecte la politique ?

- **A.** Envoyer le passage en cache en retirant sa citation pour ne pas nommer le notebook.
- **B.** Continuer à servir le passage en cache jusqu'à la prochaine actualisation planifiée de l'index.
- **C.** Envoyer le passage avec une instruction demandant au modèle de ne pas révéler les contenus interdits à l'étudiant.
- **D.** Retenir le passage jusqu'à la vérification de l'accès et appliquer des contrôles d'autorisation actuels aux résultats de recherche et du cache.

<details>
<summary>Pourquoi :</summary>

**D. Retenir le passage jusqu'à la vérification de l'accès et appliquer des contrôles d'autorisation actuels aux résultats de recherche et du cache.**

La politique place l'autorisation avant l'accès du modèle, y compris pour le contenu en cache. Si l'actualité des permissions ne peut pas être établie, retenir le passage préserve ce périmètre. L'application doit valider sa conception de recherche et de cache face aux révocations, changements de groupe et index périmés. Une instruction ou l'absence de citation n'annule pas la divulgation d'un passage non autorisé au modèle. Les fonctions natives de permissions et les filtres personnalisés nécessitent leurs propres vérifications de capacités et d'application.

- **A.** Retirer la citation modifie la présentation, mais le contenu non autorisé du notebook atteindrait toujours le modèle et resterait disponible pour générer la réponse.
- **B.** Une actualisation planifiée laisse une fenêtre d'accès contraire à l'exigence d'autorisation actuelle, surtout si des passages en cache survivent aux changements d'index.
- **C.** Une instruction délègue la décision d'accès à la génération après divulgation ; elle ne peut pas imposer le contrôle requis avant que le passage atteigne le modèle.

[Source :](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · [À revoir :](../certifications/fr/AI-103.md)

</details>

<a id="quiz-q26"></a>

## AI-103 · Résultats inconnus des outils

Un outil d'agent approuvé demande la création d'un seul partage de notes de recherche. Le backend accepte une clé d'opération stable, mais la réponse expire et le partage existe peut-être déjà. Une consultation de statut est disponible. Que doit faire l'application ensuite ?

- **A.** Enregistrer un résultat inconnu, rapprocher le statut à l'aide de la clé d'opération et réutiliser cette clé si une nouvelle tentative prise en charge est nécessaire.
- **B.** Réessayer immédiatement avec une nouvelle clé d'opération pour que le backend traite la demande comme une nouvelle action.
- **C.** Marquer l'opération comme définitivement échouée et abandonner sa clé, puisqu'aucune réponse n'est arrivée.
- **D.** Demander au modèle de déduire la réussite de son appel d'outil antérieur et annoncer la fin sans vérifier le backend.

<details>
<summary>Pourquoi :</summary>

**A. Enregistrer un résultat inconnu, rapprocher le statut à l'aide de la clé d'opération et réutiliser cette clé si une nouvelle tentative prise en charge est nécessaire.**

Un dépassement de délai après l'envoi ne permet pas de savoir si l'effet a eu lieu. Conserver un état explicitement inconnu et une clé d'opération stable permet d'interroger le backend et de rapprocher le résultat avant toute autre écriture. Si une nouvelle tentative est prise en charge, la même clé logique préserve le périmètre d'idempotence prévu. L'approbation et la validation des arguments restent nécessaires ; l'appel proposé par le modèle ne prouve pas que le backend a réalisé le partage autorisé.

- **B.** Une nouvelle clé fait de la reprise une opération distincte, susceptible de créer un autre partage si la première demande a déjà été validée.
- **C.** L'absence de réponse rend le résultat incertain, pas définitivement échoué ; abandonner la clé supprime aussi la référence disponible pour le rapprochement.
- **D.** L'appel d'outil généré décrit le travail prévu ; seuls des éléments du backend peuvent confirmer que le partage demandé a effectivement été créé.

[Source :](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply) · [À revoir :](../certifications/fr/AI-103.md)

</details>

<a id="quiz-q27"></a>

## DP-700 · Ordre des suppressions incrémentielles

Un chargement Fabric des inscriptions traite la modification source de séquence 98, qui supprime l'inscription E. Une mise à jour retardée de E, de séquence 94, arrive ensuite. Les séquences sources définissent l'ordre de référence, et une réinscription légitime ultérieure est possible. Quelle règle de fusion préserve l'état correct ?

- **A.** Appliquer la mise à jour 94, car elle est arrivée le plus récemment dans le pipeline.
- **B.** Ignorer définitivement toute modification future de E dès qu'une suppression est observée.
- **C.** Conserver les informations de suppression et de version de la séquence 98, refuser la mise à jour 94 comme ancienne et autoriser une modification plus récente valide.
- **D.** Abandonner le point de contrôle et rejouer les modifications strictement dans l'ordre d'arrivée, sans comparer les versions.

<details>
<summary>Pourquoi :</summary>

**C. Conserver les informations de suppression et de version de la séquence 98, refuser la mise à jour 94 comme ancienne et autoriser une modification plus récente valide.**

La séquence source détermine l'ordre métier : la mise à jour 94 ne doit donc pas recréer une inscription supprimée à la séquence 98. Conserver la suppression et sa version permet à une fusion idempotente de refuser les changements périmés tout en acceptant une version ultérieure valide. L'heure d'arrivée ne fait pas référence ici. Des clés stables, des comparaisons déterministes de versions et une progression durable sont nécessaires ensemble ; rejouer les entrées sans ces règles ne corrige pas le problème d'ordre.

- **A.** L'ordre d'arrivée peut différer de celui des changements sources ; appliquer l'ancienne mise à jour recréerait à tort une inscription supprimée par une modification plus récente.
- **B.** Une interdiction définitive refuserait aussi une réinscription ultérieure valide ; la fusion doit comparer les versions plutôt que bloquer tout futur changement pour cette clé.
- **D.** Rejouer le même ordre d'arrivée sans contrôler les versions peut reproduire la réapparition ; supprimer le point de contrôle n'établit pas, à lui seul, l'ordre métier de référence.

[Source :](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-lake-change-data-feed) · [À revoir :](../certifications/fr/DP-700.md)

</details>

<a id="quiz-q28"></a>

## DP-700 · Chemins d'accès Fabric

Un rapport universitaire applique correctement des restrictions au niveau des lignes et possède une étiquette de confidentialité. Le même analyste peut lire directement les fichiers sous-jacents détaillés par étudiant via un chemin OneLake autorisé. La politique n'autorise que les totaux par module. Que doit modifier et vérifier l'ingénieur ?

- **A.** Renommer l'étiquette Hautement confidentiel et supposer que son nom applique les restrictions de lignes du rapport aux lectures directes des fichiers.
- **B.** Limiter le chemin d'accès sous-jacent aux autorisations minimales nécessaires et tester, avec l'identité de l'analyste, les totaux permis et les détails refusés.
- **C.** Masquer la table détaillée dans le rapport en laissant les autorisations directes de fichiers de l'analyste inchangées.
- **D.** Accorder un rôle d'espace de travail plus étendu pour que les restrictions de lignes actuelles du rapport régissent automatiquement tous les accès.

<details>
<summary>Pourquoi :</summary>

**B. Limiter le chemin d'accès sous-jacent aux autorisations minimales nécessaires et tester, avec l'identité de l'analyste, les totaux permis et les détails refusés.**

Une restriction appliquée par un rapport ou un moteur de requêtes ne régit pas automatiquement un accès direct distinct aux fichiers. L'ingénieur doit aligner les permissions d'espace de travail, d'élément, de moteur et de fichier sur la politique, puis tester chaque chemin prévu avec l'identité de l'analyste. Une étiquette de confidentialité apporte un contexte de gouvernance ou une protection configurée, mais son nom seul n'impose pas partout la même autorisation. Des droits plus étendus peuvent ouvrir d'autres voies au lieu de fermer cette faille.

- **A.** Changer un nom de classification ne configure pas la limite d'accès aux fichiers et n'applique pas automatiquement les restrictions de lignes du moteur de rapport via OneLake.
- **C.** Masquer du contenu dans le rapport ne change que sa présentation ; l'analyste conserve l'accès direct indiqué aux fichiers détaillés par étudiant.
- **D.** Un rôle d'espace de travail plus étendu augmente les accès et ne transforme pas les restrictions du rapport en règle universelle pour chaque moteur et chemin de fichier.

[Source :](https://learn.microsoft.com/en-us/fabric/security/permission-model) · [À revoir :](../certifications/fr/DP-700.md)

</details>

<a id="quiz-q29"></a>

## SC-100 · Responsabilité du risque résiduel

Un architecte documente qu'une future plateforme universitaire de notes conserve un risque important d'interruption après les contrôles réalisables. L'équipe sécurité recommande d'avancer, mais la gouvernance exige une acceptation métier du risque. Qui doit autoriser l'acceptation de ce risque résiduel ?

- **A.** L'analyste SOC qui peut fermer le ticket de sécurité associé.
- **B.** Le responsable métier du risque, disposant de l'autorité décisionnelle requise, en consignant l'exposition et les conditions de réexamen.
- **C.** Le fournisseur du produit, car son score de conformité remplace la décision métier de l'université.
- **D.** L'administrateur cloud, uniquement parce qu'il peut déployer les ressources.

<details>
<summary>Pourquoi :</summary>

**B. Le responsable métier du risque, disposant de l'autorité décisionnelle requise, en consignant l'exposition et les conditions de réexamen.**

Le risque résiduel reste une exposition métier après le choix des contrôles techniques. Son responsable habilité et redevable doit décider si elle est acceptable, à partir des éléments de l'architecte sur l'impact, les hypothèses de probabilité, les alternatives et les lacunes restantes. La décision doit préciser le périmètre, les conditions de réexamen et la responsabilité. Les recommandations de sécurité, les droits de déploiement et les évaluations fournisseur éclairent la décision, mais ne confèrent pas automatiquement l'autorité d'acceptation exigée par l'université.

- **A.** Fermer un ticket opérationnel est une permission de workflow ; cela n'établit pas l'autorité d'accepter une exposition métier importante pour l'université.
- **C.** Une évaluation fournisseur peut guider le choix des contrôles, mais ne remplace pas la décision responsable de l'université sur son propre risque opérationnel restant.
- **D.** La capacité de déployer des ressources est une autorité technique ; le scénario exige séparément un responsable métier habilité à accepter le risque résiduel d'interruption.

[Source :](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/assess-cloud-risks) · [À revoir :](../certifications/fr/SC-100.md)

</details>

<a id="quiz-q30"></a>

## SC-100 · Validation des objectifs de reprise

Un exercice de reprise fixe un RTO de deux heures et un RPO de 15 minutes. Une panne commence à 11 h UTC. Les lectures documentaires autorisées reprennent à 12 h 30, avec des données restaurées seulement jusqu'à 10 h 40. Ces limites de mesure sont celles convenues. Quelle évaluation est correcte ?

- **A.** Les deux objectifs sont atteints, car le service a repris en moins de deux heures.
- **B.** Le RPO est atteint, mais le RTO est dépassé.
- **C.** Les deux objectifs sont manqués, car toute perte de données enfreint le RTO.
- **D.** Le RTO est atteint, mais le RPO est manqué, car le point de récupération précède la panne de 20 minutes.

<details>
<summary>Pourquoi :</summary>

**D. Le RTO est atteint, mais le RPO est manqué, car le point de récupération précède la panne de 20 minutes.**

Le RTO mesure l'interruption acceptable : les lectures autorisées reprennent après 90 minutes, dans la cible de deux heures. Le RPO mesure la perte récente de données acceptable : récupérer jusqu'à 10 h 40 pour une panne à 11 h laisse un écart de 20 minutes, supérieur aux 15 minutes prévues. Ces contrôles sont indépendants : satisfaire l'un ne satisfait pas l'autre. L'exercice doit consigner les deux mesures et les dépendances ayant permis la reprise de l'opération métier définie.

- **A.** Rétablir le service dans le délai cible satisfait seulement le RTO ; l'écart distinct de 20 minutes jusqu'au point de récupération dépasse toujours le RPO indiqué.
- **B.** L'interruption dure 90 minutes, dans les deux heures, tandis que l'écart de données de 20 minutes dépasse 15 minutes ; cette option inverse les résultats.
- **C.** Le RTO concerne la durée d'interruption, pas l'existence d'une perte de données ; la reprise mesurée en 90 minutes l'atteint malgré le RPO manqué.

[Source :](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview) · [À revoir :](../certifications/fr/SC-100.md)

</details>

<a id="quiz-q31"></a>

## AZ-120 · Fencing SAP et nœud unique en écriture

Lors d'un exercice sur table d'un cluster SAP HANA, la communication avec le primaire est perdue et le secondaire ne peut pas l'isoler par fencing. L'équipe ne peut pas confirmer que le primaire a cessé d'accepter des écritures. Quelle réponse préserve le mieux l'intégrité avant la reprise de rôle ?

- **A.** Désactiver le fencing et promouvoir le secondaire pour que le tableau de bord affiche immédiatement des ressources actives.
- **B.** Promouvoir le secondaire, car le dernier état de réplication réussi prouve que l'ancien primaire ne peut plus écrire.
- **C.** Suivre la procédure d'incident prise en charge pour rétablir ou vérifier le fencing et confirmer l'isolation de l'ancien nœud d'écriture avant d'autoriser les écritures après reprise de rôle.
- **D.** Déplacer l'adresse virtuelle du service vers le secondaire sans changer la capacité d'écriture incertaine du primaire.

<details>
<summary>Pourquoi :</summary>

**C. Suivre la procédure d'incident prise en charge pour rétablir ou vérifier le fencing et confirmer l'isolation de l'ancien nœud d'écriture avant d'autoriser les écritures après reprise de rôle.**

La perte de communication ne prouve pas l'arrêt du primaire. Le fencing isole un nœud qui ne peut pas continuer en sécurité, préservant l'exigence d'un seul nœud en écriture et réduisant le risque de split-brain. L'équipe doit examiner la configuration prise en charge du fencing et du quorum, conserver les preuves d'état et établir l'isolation de l'ancien nœud d'écriture avant d'autoriser les écritures de reprise. La santé de réplication et le déplacement d'une adresse ne fournissent pas cette isolation ; désactiver le fencing retire un mécanisme de sécurité essentiel.

- **A.** Désactiver le fencing retire le mécanisme nécessaire pour isoler un nœud d'écriture à l'état incertain ; une disponibilité apparente peut alors se payer par des primaires concurrents.
- **B.** Un résultat de réplication antérieur décrit les transferts à cet instant ; il ne prouve pas que le primaire injoignable a maintenant cessé d'accepter des écritures.
- **D.** Déplacer une adresse virtuelle change un chemin client, mais n'empêche pas, à lui seul, l'ancien primaire d'écrire via d'autres sessions ou chemins.

[Source :](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-hana-high-availability) · [À revoir :](../certifications/fr/AZ-120.md)

</details>

<a id="quiz-q32"></a>

## AZ-120 · Écritures SAP après la bascule

Une migration SAP universitaire ouvre la cible aux achats, et les utilisateurs créent de nouvelles commandes. La source inchangée reste isolée. Un problème de validation ultérieur conduit à envisager un retour arrière. Quel plan protège le mieux les nouvelles transactions métier ?

- **A.** Geler les écritures, établir l'état de données de référence, préserver les transactions de la cible et convenir d'un rapprochement ou d'une migration inverse pris en charge avant de rouvrir un système en écriture.
- **B.** Faire repointer DNS vers la source inchangée et supposer que les nouvelles commandes de la cible s'y trouvent.
- **C.** Écraser la cible à partir de l'ancienne source, puis rouvrir les achats sans identifier les transactions créées après la bascule.
- **D.** Rouvrir la source et la cible en écriture, en laissant les utilisateurs métier décider plus tard des commandes à conserver.

<details>
<summary>Pourquoi :</summary>

**A. Geler les écritures, établir l'état de données de référence, préserver les transactions de la cible et convenir d'un rapprochement ou d'une migration inverse pris en charge avant de rouvrir un système en écriture.**

Dès que la cible accepte de nouvelles écritures, le retour arrière devient une décision de traitement des données autant qu'un changement d'infrastructure. Revenir à une source inchangée peut abandonner de nouvelles commandes ; rouvrir les deux côtés peut faire diverger les transactions. Le runbook doit geler les écritures, préserver les preuves et les nouvelles données métier, choisir un état de référence et prévoir un rapprochement ou un transfert inverse pris en charge avec les responsables métier. La validation et le contrôle d'un seul nœud en écriture précèdent la réouverture des achats.

- **B.** DNS redirige les clients, mais ne copie pas les commandes créées après la bascule vers la source inchangée ; revenir en arrière seul peut abandonner ces transactions.
- **C.** Écraser depuis la source périmée peut détruire des commandes légitimes de la cible ; il faut d'abord identifier et préserver les changements métier réalisés après la bascule.
- **D.** Autoriser les deux environnements à écrire crée des historiques de transactions divergents, complique le rapprochement et rompt le contrôle requis d'un nœud d'écriture de référence.

[Source :](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/execute-migration) · [À revoir :](../certifications/fr/AZ-120.md)

</details>
