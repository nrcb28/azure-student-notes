# Ressources et disponibilité

[Sommaire](README.md) · [[object Object]](../certifications/fr/README.md)

Un abonnement délimite administration, quotas et facturation. Les groupes d'administration appliquent une gouvernance commune à plusieurs abonnements. Les groupes de ressources rassemblent des éléments ayant un cycle de vie lié. Le tenant Entra est un annuaire d'identités, pas un conteneur de ressources ordinaire.

La région du groupe concerne ses métadonnées ; les ressources peuvent se trouver ailleurs. Les zones de disponibilité apportent une séparation physique dans une région. Les capacités varient selon le service.

**Exemple :** séparons développement et production. Un réseau partagé ne doit pas disparaître avec une application.

Avant de déplacer une ressource, vérifions prise en charge, dépendances, droits et identifiants. Changer de groupe n'est pas une migration régionale universelle.

**Exercice :** explique quel type de panne ton architecture tolère réellement.

---

[Précédent](01-fundamentals.md) · [Suivant](03-compute.md) · [English](../en/02-resources.md)
