# Welkom bij OpenGarden

OpenGarden is een **open-source leerframework** voor scholen en onderwijsinstellingen. Het doel is simpel: docenten moeten hun eigen lesinhoud kunnen maken, beheren en delen — zonder afhankelijk te zijn van commerciële platforms.

## Hoe werkt het?

1. **Content schrijf je in Markdown** — gewone tekst met opmaak.
2. **Metadata zet je in YAML** — titel, volgorde, niveau, leerdoelen.
3. **Vragen definieer je in YAML** — multiple choice, waar/niet waar, of open.
4. **De app leest alles automatisch** — geen database-migraties nodig voor nieuwe lessen.

## De mapstructuur

```
content/
├── _sources.yaml          ← welke bronnen zijn actief?
└── local/                 ← jouw eigen lessen
    └── welkom/
        └── intro/
            ├── meta.yaml
            ├── lesson.md
            └── questions.yaml
```

## Meerdere bronnen

Je kunt lessen uit meerdere bronnen combineren:
- **Lokaal** — je eigen lessen
- **Git** — een gedeelde lesbibliotheek van collega-scholen
- **Officieel** — gecontroleerde lessen van een centrale repo

Elke bron krijgt een eigen *namespace*, zodat twee modules met dezelfde naam nooit met elkaar botsen.

## Volgende stap

Beantwoord de vragen hieronder om te oefenen met het systeem. Daarna ben je klaar om je eerste eigen module te maken!
