"""
Git-synchronisatie voor OpenGarden-contentbronnen.
Houdt de content-loader dom: die ziet alleen mappen, niet hoe ze er kwamen.
"""
import shutil
import subprocess
from pathlib import Path
from opengarden.content_loader import CONTENT_DIR, load_sources, load_lesson, load_track_modules


def _run_git(args, cwd=None):
    """Voer een git-commando uit. Retourneert (succes, stdout, stderr)."""
    if not shutil.which("git"):
        return False, "", "Git is niet geïnstalleerd op dit systeem."
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def sync_source(source_name):
    """
    Sync één Git-bron. Clone als deze nog niet bestaat, anders pull.
    Retourneert (succes, bericht).
    """
    for source in load_sources():
        if source["name"] != source_name:
            continue

        if source["type"] != "git":
            return False, f"'{source_name}' is geen Git-bron."

        url = source.get("url")
        if not url:
            return False, f"Geen URL geconfigureerd voor '{source_name}'."

        local_path = CONTENT_DIR / source.get("local_path", source["name"])

        # CASE 1: Bestaat al en is een git repo → pull
        if local_path.exists() and (local_path / ".git").is_dir():
            success, stdout, stderr = _run_git(["pull"], cwd=str(local_path))
            if success:
                load_lesson.cache_clear()
                load_track_modules.cache_clear()
                return True, f"Updates binnengehaald voor '{source_name}'."
            return False, f"Pull mislukt: {stderr}"

        # CASE 2: Bestaat niet → clone
        local_path.parent.mkdir(parents=True, exist_ok=True)
        success, stdout, stderr = _run_git(
            ["clone", "--depth", "1", url, str(local_path)],
            cwd=str(CONTENT_DIR),
        )
        if success:
            load_lesson.cache_clear()
            load_track_modules.cache_clear()
            return True, f"'{source_name}' gekloond van {url}."
        return False, f"Clone mislukt: {stderr}"

    return False, f"Bron '{source_name}' niet gevonden in _sources.yaml."


def get_sync_status(source_name):
    """Geeft status terug: 'not_cloned', 'synced', 'error', 'local'."""
    for source in load_sources():
        if source["name"] != source_name:
            continue

        if source["type"] != "git":
            return "local", "Lokale map"

        local_path = CONTENT_DIR / source.get("local_path", source["name"])

        if not local_path.exists():
            return "not_cloned", "Nog niet gekloond"
        if not (local_path / ".git").is_dir():
            return "error", "Map bestaat maar is geen Git-repo"

        success, stdout, _ = _run_git(
            ["log", "-1", "--format=%cd (%h)"],
            cwd=str(local_path),
        )
        if success:
            return "synced", f"Laatste update: {stdout.strip()}"
        return "error", "Kan status niet uitlezen"

    return "unknown", "Onbekende bron"
