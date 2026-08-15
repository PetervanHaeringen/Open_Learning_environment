# 🌱 OpenGarden

Een open-source leerframework voor onderwijsinstellingen.
Lessen in YAML + Markdown, voortgang in SQLite, blauwdrukken in Flask.

## Snel starten (lokaal)

```bash
# 1. Virtual environment aanmaken
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Installeren
pip install -r requirements.txt

# 3. Database aanmaken
python init_db.py

# 4. Starten
python run.py
```

Ga naar http://localhost:5000 en registreer een account.
Maak daarna een admin aan via het register-formulier,
en pas de rol aan in de database (of via een klein script).

## Structuur

- `opengarden/` — Het framework (Python package)
- `content/` — Lesinhoud (YAML + Markdown)
- `instance/` — SQLite database (wordt automatisch aangemaakt)

## Content toevoegen

1. Maak een map in `content/local/<track>/<module>/`
2. Voeg `meta.yaml`, `lesson.md` en `questions.yaml` toe
3. Herstart de app (of wacht op cache-verversing)

## PythonAnywhere

1. Upload de bestanden
2. Zet `wsgi.py` als WSGI-configuratie
3. Zet `SECRET_KEY` als environment variable
4. Run `python init_db.py` in een console

## Licentie

Creative Commons — vrij te gebruiken voor onderwijs.
