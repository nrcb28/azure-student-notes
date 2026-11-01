# DP-300 · Cahier opérationnel commun

[Guide](DP-300.md) · [Dix cas](DP-300-cases.md) · [Sommaire](README.md)

Cinq unités avec objectifs et preuves correspondants dans les huit éditions. Réaliser les exercices de conception sans Azure si nécessaire. Distinguer comportement attendu et observations réelles. Aucune exécution Azure ni couverture complète de l’examen n’est revendiquée.

<a id="dp-300-unit-1"></a>

## 1. Justifier le choix de plateforme et de migration

Rédiger les exigences de l’application : fonctionnalités, accès système, dépendances d’instance, interruption acceptable des écritures, maintenance et récupération. Comparer SQL Database, Managed Instance et SQL Server sur VM sur ces exigences, plutôt qu’accorder des points aux noms connus.

**Cas :** une tâche planifiée dépend d’un outil système. **Preuves :** nécessité actuelle de la dépendance, cible compatible ou refonte, et contrôle de compatibilité. **Livrable :** séquence avec transfert initial, gel des écritures, validation, bascule, responsable du retour arrière et traitement des écritures après bascule. Une copie terminée n’est pas le test d’acceptation.

<a id="dp-300-unit-2"></a>

## 2. Séparer frontières d’accès et de confidentialité

Dessiner le trajet de l’identité applicative vers une opération autorisée sur une table. Marquer résolution, réseau, authentification, principal de base et permissions d’objet. Séparer application, déploiement et administration d’urgence. Définir les données visibles dans requêtes, journaux, exports et sauvegardes.

**Cas :** la connexion privée fonctionne, mais l’application ne lit pas sa table. **Preuves :** identité, base, objet et opération refusée ; ne pas ouvrir le réseau public à la place du diagnostic. **Livrable :** permissions minimales et comparaison transport chiffré, TDE, Always Encrypted et masquage face à une exigence de confidentialité précise. Inclure responsabilité et récupération des clés.

<a id="dp-300-unit-3"></a>

## 3. Diagnostiquer une régression mesurée

Inventer deux périodes de charge comparables pour une requête de permission, avec durée, lectures, CPU, concurrence et plan. Relier une hypothèse aux preuves et nommer l’observation qui la réfuterait. Inclure blocages et durée des transactions avec l’historique Query Store disponible ; ni une métrique normale ni un opérateur de plan apparemment coûteux ne suffit à déterminer la cause.

**Cas :** un nouvel index améliore les lectures et ralentit les imports. **Preuves :** résultats avant/après pour les deux opérations sous charge représentative. **Livrable :** expérience réversible, seuils d’acceptation, étapes de retour arrière et limites des preuves. Ne pas proposer réduction systématique des fichiers ou interruption de toutes les sessions comme maintenance ordinaire.

<a id="dp-300-unit-4"></a>

## 4. Rendre l’automatisation observable et répétable

Classer une tâche nocturne selon son travail et sa plateforme. Comparer SQL Agent pour SQL Server ou Managed Instance compatibles avec Elastic Jobs pour du T-SQL dans SQL Database. Préciser identité, cibles, calendrier, délai maximal, budget de tentatives et notification d’échec. Les dépendances externes peuvent demander un orchestrateur plus large.

**Cas :** la tâche valide son résultat mais perd la réponse de réussite. **Preuves :** expliquer comment une reprise évite un doublon et comment l’opérateur confirme l’achèvement. **Livrable :** tableau des états en attente, en cours, terminé et incertain, avec plan de test synthétique. L’appel réussi du planificateur n’équivaut pas à un résultat métier vérifié.

<a id="dp-300-unit-5"></a>

## 5. Récupérer les données et le service complet

Définir deux incidents : suppression accidentelle et panne régionale. Choisir états conservés et mécanismes de disponibilité selon leurs problèmes respectifs. Exprimer RPO et RTO du point de vue de l’application, puis identifier permissions, capacité cible, point de connexion, DNS, authentification et dépendances nécessaires. La réplication peut transmettre une modification validée indésirable.

**Cas :** le nouveau principal est sain, mais les utilisateurs ne téléchargent rien. **Preuves :** vérification fonctionnelle et chronologie incluant reconnexion. **Livrable :** plan isolé de validation de restauration, choix de copie faisant autorité avant le retour et responsable du nettoyage des données conservées. Marquer les délais proposés ATTENDUS tant qu’ils ne sont pas observés ; un exercice sur table ne mesure pas la récupération Azure.

[Objectifs officiels](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Guide et sources techniques](DP-300.md)
