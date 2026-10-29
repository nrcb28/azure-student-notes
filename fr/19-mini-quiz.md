# Mini simulation : choisir et comprendre pourquoi

[←](README.md) · [CLI](../QUIZ.md) · [Lire les questions sur GitHub](20-quiz-cases.md)

Cette mini simulation propose huit scénarios originaux, deux pour chaque parcours : AZ-900, AZ-104, AZ-305 et AZ-400. Elle permet de travailler des décisions concrètes sur Azure, sans compte ni connexion. Les scénarios sont originaux ; les explications renvoient à Microsoft Learn et les sources restent en anglais.

## Commencer

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang fr
python tools/quiz.py run --lang fr --exam AZ-104 --count 2
```

## Pratique avec correction

En mode practice, la correction suit chaque réponse : vous voyez le raisonnement, le problème de votre autre choix et un chapitre à revoir. Les questions et les options changent d’ordre. Répondez avec A–D, appuyez sur S ou Entrée pour passer, et sur Q pour terminer ; vous pouvez filtrer par examen.

```bash
python tools/quiz.py run --lang fr --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## Simulation avec minuteur facultatif

Le mode exam réserve les explications à la fin de la session. Le minuteur est facultatif et se vérifie lorsque vous appuyez sur Entrée : il n’interrompt pas seul l’attente du terminal et refuse une réponse envoyée trop tard. Les questions sans réponse restent dans le total, même si vous terminez plus tôt.

```bash
python tools/quiz.py run --lang fr --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## Revoir les erreurs

review affiche de nouveau les réponses incorrectes et les questions sans réponse ; --all ajoute les réponses correctes. Le rapport conserve une copie des énoncés, options et explications : une mise à jour de la banque ne change donc pas votre révision. Les questions gardent la langue de la session enregistrée ; vous pouvez changer la langue de l’interface.

```bash
python tools/quiz.py review --lang fr --report .study-reports/first-quiz.json
python tools/quiz.py review --lang fr --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang fr --report .study-reports/first-quiz.json --json
```

## Rapports personnels

À la fin, un rapport JSON local est enregistré dans .study-reports/, dossier exclu de Git. Il contient les questions, vos choix, les durées et l’état de la session. Rien n’est envoyé à un service et aucun appel à Azure n’est effectué. Vous pouvez choisir un autre chemin ; un fichier existant n’est jamais remplacé.

## Ce que mesure le résultat

Huit scénarios ne couvrent qu’une petite partie du programme et ne constituent pas un examen officiel ou complet. Le résultat indique seulement les bonnes réponses de cette session et ne prédit pas votre réussite. Utilisez les explications et les sources pour revoir les sujets difficiles, puis consultez les objectifs officiels à jour avant de préparer une certification.

```bash
python tools/quiz.py doctor --lang fr
```

[CLI](../QUIZ.md) · [Lire les questions sur GitHub](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
