# SC-300 · Cahier de décisions d’accès et de gouvernance

[Guide](SC-300.md) · [Dix cas](SC-300-cases.md) · [Sommaire](README.md)

Cinq unités originales hors ligne pour une application universitaire de notes fictive. Utilisez des identités et des documents synthétiques. Ne modifiez pas les stratégies d’un locataire, ne créez pas de moyens d’authentification, n’activez pas de rôles et ne connectez pas de véritable télémétrie. Les livrables décrivent les décisions attendues ; aucune exécution dans le cloud n’est revendiquée.

<a id="sc-300-unit-1"></a>

## 1. Suivre l’accès effectif et les sources d’identité

Cartographiez le locataire, l’abonnement, l’application et le magasin de documents. Séparez les rôles d’annuaire, la portée des unités administratives, les rôles Azure de ressource et de données, et les droits applicatifs. Incluez les chemins d’octroi directs et par groupe et identifiez qui contrôle les appartenances. Pour une identité hybride, consignez la source faisant autorité et les hypothèses de synchronisation et d’authentification choisies ; ne considérez pas la synchronisation comme un octroi d’accès.

**Scénario :** un étudiant perd une affectation directe, mais peut encore lire un dossier de cours. **Éléments probants :** un schéma identifiant deux chemins d’octroi possibles et les relevés nécessaires pour les départager. **Livrable :** une matrice de décision d’accès de six lignes couvrant étudiant, invité, éditeur, administrateur, indexeur et ancien membre, avec une portée minimale et un refus attendu pour chacun.

<a id="sc-300-unit-2"></a>

## 2. Concevoir l’authentification et l’accès conditionnel

Précisez une méthode d’authentification prise en charge, un parcours d’inscription et un responsable de la récupération. Expliquez la résistance à l’hameçonnage et où un Temporary Access Pass pourrait amorcer un utilisateur éligible sans stocker de véritable code secret. Décrivez les cibles de stratégie, les conditions, les contrôles d’octroi et de session, les exclusions, les hypothèses de licence et la récupération d’urgence. Séparez les évaluations en mode rapport seul des résultats en mode appliqué.

**Scénario :** un enseignant visiteur utilise un appareil personnel, tandis qu’un éditeur manipule des corrigés non publiés. **Éléments probants :** trois requêtes attendues avec des identités, méthodes, appareils ou ressources différents ; expliquez séparément la confiance dans les revendications inter-locataires et le droit applicatif. **Livrable :** une matrice de stratégie proposée et une note de déploiement contenant des critères de pilote, de révision, de récupération et de retour arrière. Rien n’est activé dans un locataire réel.

<a id="sc-300-unit-3"></a>

## 3. Choisir et limiter les identités de charge de travail

Comparez une inscription d’application, son principal de service et une identité managée pour l’indexeur. Expliquez les permissions déléguées et d’application, le consentement et la portée des ressources. Pour une génération externe fictive, documentez l’émetteur, le sujet et l’audience de fédération attendus à l’aide de valeurs de revendication inventées. Indiquez pourquoi l’émission réussie d’un jeton n’établit pas l’autorisation de déployer.

**Scénario :** l’indexeur lit uniquement les notes publiées, tandis que la génération met à jour uniquement son application de test. **Éléments probants :** une opération autorisée et une refusée par charge de travail, ainsi qu’un propriétaire de permission et une date de révision. **Livrable :** un tableau de choix d’identité et une esquisse de confiance fédérée sans mots de passe, secrets clients, jetons réels ni commandes de déploiement. Notez les hypothèses non étayées sous forme de questions à poser au propriétaire.

<a id="sc-300-unit-4"></a>

## 4. Construire le cycle de vie des droits et des privilèges

Séparez l’éligibilité PIM, l’activation et la durée active des révisions d’accès périodiques. Proposez un package d’accès pour les enseignants visiteurs et une automatisation du cycle de vie prise en charge pour les arrivées, mobilités et départs. Distinguez la fédération d’authentification unique du provisionnement SCIM et expliquez comment la suppression en aval serait confirmée. Énumérez les hypothèses de licence propres à chaque fonctionnalité et les responsables des échecs d’automatisation.

**Scénario :** le semestre d’un enseignant se termine alors qu’un administrateur a besoin d’un accès de maintenance temporaire. **Éléments probants :** une décision d’expiration, une révision par le propriétaire de ressource, une proposition d’activation à portée définie et un relevé d’achèvement du provisionnement en aval. **Livrable :** un tableau de gouvernance indiquant déclencheur, approbateur, droit, durée, révision, suppression attendue, éléments probants et gestion des exceptions. Une révision terminée ne prouve pas qu’un rôle est activé.

<a id="sc-300-unit-5"></a>

## 5. Expliquer un échec avec des éléments délimités

Séparez risque utilisateur, risque de connexion, évaluation des stratégies, changements d’annuaire et échecs de provisionnement. Choisissez les journaux pertinents et décrivez les hypothèses de routage des diagnostics, de conservation, d’accès et de schéma. Annotez la requête KQL hypothétique du guide pour préciser ce que son agrégat peut et ne peut pas établir. N’ajoutez Private Access, Internet Access ou le profil de trafic Microsoft que lorsque le chemin de la ressource rend cet objectif pertinent.

**Scénario :** un invité ne peut pas ouvrir un cours, mais un tableau de bord n’affiche aucun échec correspondant. **Éléments probants :** une chronologie hypothétique, les lacunes de couverture, les champs de corrélation et deux explications concurrentes. **Livrable :** un diagnostic d’une page et une liste de vérification des éléments reliant identité, chemin réseau, stratégie, droit applicatif et provisionnement. Étiquetez chaque résultat comme attendu ; aucune requête ni aucun test de locataire n’est exécuté.

[Guide d’étude Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Fondements de l’identité](../../fr/06-identity.md)
