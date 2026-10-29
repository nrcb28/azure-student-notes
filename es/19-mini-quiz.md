# Mini simulacro: decide y entiende el porqué

[←](README.md) · [CLI](../QUIZ.md) · [Preguntas para leer en GitHub](20-quiz-cases.md)

Este mini simulacro incluye ocho escenarios originales, dos de cada ruta: AZ-900, AZ-104, AZ-305 y AZ-400. Sirve para practicar decisiones concretas de Azure sin cuenta ni conexión. Los escenarios son propios; las explicaciones enlazan a Microsoft Learn y las fuentes se conservan en inglés.

## Empezar

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang es
python tools/quiz.py run --lang es --exam AZ-104 --count 2
```

## Práctica con corrección

En el modo practice recibes la corrección después de cada respuesta, con el motivo de la solución, el fallo de tu alternativa y un capítulo para repasar. El orden de preguntas y opciones cambia. Responde A–D, pulsa S o Intro para saltar y Q para terminar; puedes filtrar por examen.

```bash
python tools/quiz.py run --lang es --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## Mini simulacro con tiempo opcional

El modo exam reserva las explicaciones para el final de la sesión. El temporizador es opcional y se comprueba al pulsar Intro: no interrumpe por sí solo la espera del terminal y rechaza una respuesta enviada fuera de plazo. Las preguntas sin responder cuentan en el total, incluso si terminas antes.

```bash
python tools/quiz.py run --lang es --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## Revisar errores

review vuelve a mostrar las respuestas incorrectas y las preguntas sin responder; --all incluye también las acertadas. El informe guarda una copia de los enunciados, las opciones y las explicaciones, de modo que una actualización del banco no altera lo que repasas. Las preguntas conservan el idioma de la sesión guardada; puedes cambiar el idioma de la interfaz.

```bash
python tools/quiz.py review --lang es --report .study-reports/first-quiz.json
python tools/quiz.py review --lang es --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang es --report .study-reports/first-quiz.json --json
```

## Informes personales

Al terminar se guarda un informe JSON local en .study-reports/, carpeta excluida de Git. Incluye las preguntas, tus elecciones, los tiempos y el estado de la sesión. No se envía a ningún servicio ni se llama a Azure. Una ruta personalizada permite guardar el informe en otro lugar y nunca se reemplaza un archivo existente.

## Qué mide

Ocho escenarios cubren una parte pequeña del temario y no forman un examen oficial ni completo. El resultado indica únicamente aciertos en esta sesión; no predice si aprobarás. Usa las explicaciones y sus fuentes para revisar los temas que te hayan costado, y consulta los objetivos oficiales actualizados antes de preparar una certificación.

```bash
python tools/quiz.py doctor --lang es
```

[CLI](../QUIZ.md) · [Preguntas para leer en GitHub](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
