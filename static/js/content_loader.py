"""
Generieke content-loader voor OpenGarden.
Leest lesinhoud uit meerdere bronnen, gedefinieerd in content/_sources.yaml.
"""
from pathlib import Path
from functools import lru_cache
import re
import yaml

# FIX: __file__ is opengarden/content_loader.py
# .parent = opengarden/
# .parent.parent = project root (where content/ lives)
BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"


def load_sources():
    """Laad het manifest met alle content-bronnen."""
    sources_path = CONTENT_DIR / "_sources.yaml"
    if not sources_path.exists():
        return []
    with open(sources_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("sources", [])


def _get_source_namespace(source_name):
    """
    Haal de namespace op voor een bron uit _sources.yaml.
    Fallback naar source_name zelf als geen namespace is geconfigureerd.
    """
    for source in load_sources():
        if source["name"] == source_name:
            return source.get("namespace", source_name)
    return source_name


def _resolve_slug(source_name, track, module, meta=None):
    """
    Bepaal de canonieke module slug.

    Volgorde van prioriteit:
      1. meta["id"]           → bijv. "developer.m01"  (TestGarden-stijl)
      2. meta["legacy_slug"]  → nooduitgang voor oude yaml
      3. namespace.track.module → bijv. "local.getallenstelsels.00_tientallig"

    De namespace komt uit _sources.yaml (veld 'namespace'), met fallback
    naar de bronnaam zelf. Zo blijven bestaande lokale modules werken
    zonder expliciete id, en krijgen geïmporteerde repo's hun eigen
    prefix als de auteur dat niet expliciet in meta.yaml heeft gezet.
    """
    if meta:
        if meta.get("id"):
            return meta["id"]
        if meta.get("legacy_slug"):
            return meta["legacy_slug"]

    namespace = _get_source_namespace(source_name)
    return f"{namespace}.{track}.{module}"


def get_source_dir(source_name):
    """Bepaal het pad op schijf voor een bron."""
    for source in load_sources():
        if source["name"] == source_name:
            if source["type"] == "local":
                raw_path = source["path"]
                # Strip leading ./ or .\ (Windows)
                if raw_path.startswith("./") or raw_path.startswith(".\\"):
                    raw_path = raw_path[2:]
                return CONTENT_DIR / raw_path
            elif source["type"] == "git":
                return CONTENT_DIR / source.get("local_path", source["name"])
    return None


def get_all_sources():
    """Lijst van alle geconfigureerde bron-namen."""
    return [s["name"] for s in load_sources()]


def get_all_tracks(source_name):
    """Alle tracks binnen een bron."""
    source_dir = get_source_dir(source_name)
    if not source_dir or not source_dir.exists():
        return []
    tracks = []
    for d in source_dir.iterdir():
        if d.is_dir() and not d.name.startswith(("_", ".")):
            has_modules = any(
                sub.is_dir() and (sub / "meta.yaml").exists()
                for sub in d.iterdir()
            )
            if has_modules:
                tracks.append(d.name)
    return sorted(tracks)


def _strip_leading_h1(markdown_content):
    return re.sub(r"^# .+\n+", "", markdown_content, count=1)


@lru_cache(maxsize=None)
def load_lesson(source_name, track, module, lang=None):
    """
    Laadt een module: metadata, lesinhoud en vragen.
    De module_slug wordt bepaald door _resolve_slug() op basis van
    meta.id, meta.legacy_slug, of namespace.track.module als fallback.
    """
    source_dir = get_source_dir(source_name)
    if not source_dir:
        return None

    module_dir = source_dir / track / module
    meta_path = module_dir / "meta.yaml"
    lesson_path = module_dir / "lesson.md"
    questions_path = module_dir / "questions.yaml"

    if not meta_path.exists() or not lesson_path.exists():
        return None

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f)

    content_lang = "nl"
    chosen_lesson_path = lesson_path

    if lang and lang != "nl":
        translated_path = module_dir / f"lesson.{lang}.md"
        if translated_path.exists():
            chosen_lesson_path = translated_path
            content_lang = lang

    with open(chosen_lesson_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    if content_lang == "nl":
        markdown_content = _strip_leading_h1(markdown_content)

    questions = []
    if questions_path.exists():
        with open(questions_path, "r", encoding="utf-8") as f:
            qdata = yaml.safe_load(f) or {}
            questions = qdata.get("questions", [])

    # === GEWIJZIGD: gebruik _resolve_slug voor canonieke identiteit ===
    module_slug = _resolve_slug(source_name, track, module, meta)

    return {
        "meta": meta,
        "content": markdown_content,
        "questions": questions,
        "module_slug": module_slug,
        "content_lang": content_lang,
    }


@lru_cache(maxsize=None)
def load_track_modules(source_name, track):
    """Laadt alle modules in een track."""
    source_dir = get_source_dir(source_name)
    if not source_dir:
        return []

    track_dir = source_dir / track
    if not track_dir.exists():
        return []

    modules = []
    for module_dir in track_dir.iterdir():
        if not module_dir.is_dir():
            continue
        meta_path = module_dir / "meta.yaml"
        if not meta_path.exists():
            continue
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = yaml.safe_load(f) or {}

        # === GEWIJZIGD: gebruik _resolve_slug voor canonieke identiteit ===
        module_slug = _resolve_slug(source_name, track, module_dir.name, meta)

        modules.append({
            "folder": module_dir.name,
            "title": meta.get("title", module_dir.name),
            "order": meta.get("order", 999),
            "level": meta.get("level", ""),
            "status": meta.get("status", "active"),
            "module_slug": module_slug,
        })

    return sorted(modules, key=lambda m: m["order"])


def available_translations(source_name, track, module):
    """Geeft beschikbare taalcodes voor een module."""
    source_dir = get_source_dir(source_name)
    if not source_dir:
        return []
    module_dir = source_dir / track / module
    if not module_dir.exists():
        return []
    talen = []
    for pad in module_dir.glob("lesson.*.md"):
        stam = pad.name[len("lesson."):-len(".md")]
        if stam and stam != "nl":
            talen.append(stam)
    return sorted(talen)
