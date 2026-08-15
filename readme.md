# 🌱 OpenGarden

Een open-source leerframework voor onderwijsinstellingen.
Lesinhoud in YAML en Markdown. Voortgang in SQLite. Vrijheid voor elke school.

---

## Inhoudsopgave

1. [Wat is OpenGarden?](#wat-is-opengarden)
2. [Snel starten](#snel-starten)
3. [Je eerste module maken](#je-eerste-module-maken)
4. [Markdown & YAML: de basis](#markdown--yaml-de-basis)
5. [Veelgemaakte fouten](#veelgemaakte-fouten)
6. [Vragen toevoegen](#vragen-toevoegen)
7. [Modules toewijzen aan leerlingen](#modules-toewijzen-aan-leerlingen)
8. [Bestandsstructuur](#bestandsstructuur)

---

## Wat is OpenGarden?

OpenGarden is een lichtgewicht leeromgeving waarin docenten hun eigen lesinhoud schrijven in leesbare bestanden (YAML en Markdown). De app leest deze bestanden automatisch in — geen database-migraties, geen complexe CMS, geen commerciële afhankelijkheid.

**Kernprincipes:**
- **Content = bestanden** — lesinhoud leeft in YAML + Markdown, niet in een database
- **Lokaal draaien** — SQLite-database, geen externe server nodig
- **Meertalig** — vertaal je les voor wie het nodig heeft
- **Deelbaar** — lesbibliotheek via Git
- **Vrij** — open source, geen licentiekosten

---

## Snel starten

### Vereisten

- Python 3.10 of hoger
- pip (Python package installer)

### Installatie

```bash
# 1. Pak het OpenGarden-archief uit
cd opengarden

# 2. Maak een virtuele omgeving (aanbevolen)
python -m venv venv

# 3. Activeer de virtuele omgeving
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Installeer afhankelijkheden
pip install -r requirements.txt

# 5. Maak de database aan
python init_db.py

# 6. Start de app
python run.py"# Open_Learning_environment" 
