# Huit scénarios pour s’entraîner

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
