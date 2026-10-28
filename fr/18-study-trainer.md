# Entraîneur de révision sans Azure

[←](README.md) · [Anki](../flashcards/fr.tsv)

Travaille les 40 cas de ta langue, dix par certification. Python 3.9 ou supérieur et sa bibliothèque standard suffisent. Aucun compte cloud, paquet externe ou connexion pendant l'utilisation.

```bash
python tools/study.py demo --lang fr --exam AZ-104
python tools/study.py study --lang fr --exam AZ-104 --limit 5
```

## 1. Se tester

Lis, réfléchis et appuie sur Entrée. Compare l'explication puis évalue : 0 oubliée, 1 difficile, 2 bien, 3 facile. q quitte ; chaque évaluation terminée est sauvegardée. Autoévaluation, pas correction automatique ou note d'examen.

## 2. Revoir les difficultés

Le mode normal privilégie les cartes échues, puis les nouvelles. weak sélectionne les cas difficiles ou avec des oublis passés ; random mélange. Progression séparée par langue. Les réponses écrites ne sont pas conservées.

## 3. Progression et plan

stats montre nouvelles, échues, consolidées et oublis par examen. Consolidée signifie deux évaluations successives au moins 2, pas préparation garantie. plan suggère environ quatre minutes par cas sans prédire les échéances.

## 4. Intervalles

0 revient dans dix minutes et réinitialise la série ; 1 demain et réinitialise. 2 programme un jour, puis trois, puis double. 3 commence à quatre jours puis multiplie par 2,5, maximum365. Règle simple propre, pas FSRS ni garantie de mémoire.

## 5. Emporter dans Anki

Télécharge les paquets prêts ou exporte une sélection. UTF-8, trois colonnes : question, explication, tags. Anki garde sa propre progression. Vérifie aperçu et correspondance des colonnes.

## 6. Tes données

Le fichier .study-progress.json est exclu de Git. --progress permet un autre chemin. Écritures atomiques et protection contre les sessions concurrentes. Un JSON endommagé n'est pas remplacé. Conserve des copies pour déplacer ton historique.

```bash
python tools/study.py study --lang fr --mode weak --limit 5
python tools/study.py stats --lang fr
python tools/study.py plan --lang fr --days 7 --minutes 20
python tools/study.py export --lang fr --exam AZ-104 --output exports/fr-az104.tsv
python tools/study.py doctor --lang fr
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)
