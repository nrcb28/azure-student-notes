# Entrenador de estudio sin Azure

[←](README.md) · [Anki](../flashcards/es.tsv)

Practica con los 160 casos de tu idioma: diez por certificación. Funciona con Python 3.9 o posterior y solo su biblioteca estándar. No necesita cuenta cloud, paquetes externos ni conexión durante el uso.

```bash
python tools/study.py demo --lang es --exam AZ-104
python tools/study.py study --lang es --exam AZ-104 --limit 5
```

La zona de visualización predeterminada, Europe/Madrid, necesita los datos horarios IANA del sistema operativo. Si no están disponibles, añade --timezone UTC al comando demo o study; no requiere paquetes adicionales.

## 1. Ponte a prueba

Muestra una pregunta, piensa la respuesta y pulsa Intro. Después compara la explicación y valórate: 0 olvidada, 1 difícil, 2 bien, 3 fácil. q sale; cada valoración ya completada se guarda. Es autoevaluación, no corrección automática ni nota de certificación.

## 2. Repasa lo que cuesta

Por defecto aparecen tarjetas pendientes y nuevas, priorizando las vencidas. weak recupera casos valorados como difíciles o con historial de olvido; random permite mezclar. El progreso se separa por idioma. No se guardan tus respuestas escritas.

## 3. Progreso y plan

stats muestra nuevas, pendientes, consolidadas y olvidos por examen. Consolidada significa dos valoraciones consecutivas de al menos 2; no demuestra preparación para aprobar. plan propone sesiones de aproximadamente cuatro minutos por caso, sin prometer vencimientos futuros.

## 4. Cómo funciona la repetición

0 vuelve en diez minutos y reinicia la racha; 1 vuelve al día siguiente y la reinicia. Las valoraciones 2 y 3 comparten una racha de repasos consecutivos acertados. Con 2, el primer acierto programa un día, el segundo tres y los siguientes duplican el intervalo anterior. Con 3, el primer acierto programa cuatro días; los siguientes multiplican el intervalo anterior por 2,5, redondean a días enteros y usan al menos cuatro días. Ambos tienen un máximo de 365 días. Cambiar de valoración no reinicia la racha: 3 seguido de 2 programa cuatro y luego tres días. Es una regla sencilla propia, no FSRS ni una garantía de memoria.

## 5. Llévatelo a Anki

Puedes descargar los mazos preparados o exportar una selección. El archivo usa UTF-8 y tres columnas: pregunta, explicación y etiquetas. El progreso de Anki es independiente del entrenador. Revisa la vista previa y las columnas al importar.

## 6. Tus datos

El progreso predeterminado está en .study-progress.json, excluido de Git. Puedes elegir otro archivo con --progress. Las escrituras son atómicas y rechazan una sesión concurrente que haya modificado el archivo. Un JSON dañado no se reemplaza. Conserva copias si quieres trasladar tu historial.

```bash
python tools/study.py study --lang es --mode weak --limit 5
python tools/study.py stats --lang es
python tools/study.py plan --lang es --days 7 --minutes 20
python tools/study.py export --lang es --exam AZ-104 --output exports/es-az104.tsv
python tools/study.py doctor --lang es
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)

## Mini simulacro: decide y entiende el porqué

[Mini simulacro: decide y entiende el porqué](19-mini-quiz.md) · [Preguntas para leer en GitHub](20-quiz-cases.md)
