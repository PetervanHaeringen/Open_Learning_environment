from flask import render_template, session
from opengarden.dashboard import dashboard_bp
from opengarden.auth.utils import login_required
from opengarden.models import User, UserModule
from opengarden.content_loader import load_sources, get_all_tracks, load_track_modules, load_lesson
from opengarden.question_engine import compute_step_status, compute_progress


@dashboard_bp.route("/")
@login_required
def index():
    user_id = session["user_id"]
    user = User.query.get(user_id)

    steps = []
    sources = load_sources()

    for source in sources:
        source_name = source["name"]
        tracks = get_all_tracks(source_name)
        for track in tracks:
            modules = load_track_modules(source_name, track)
            for m in modules:
                slug = m["module_slug"]
                assigned = UserModule.query.filter_by(
                    user_id=user_id, module_slug=slug
                ).first()

                if user.module_visibility == "alleen_toegewezen" and not assigned:
                    continue

                lesson = load_lesson(source_name, track, m["folder"])
                questions = lesson["questions"] if lesson else []

                status = compute_step_status(user_id, slug, {"questions": questions})
                progress = compute_progress(user_id, slug, {"questions": questions})

                locked = (user.module_visibility == "vergrendeld") and not assigned

                steps.append({
                    "name": m["title"],
                    "url": f"/content/{source_name}/{track}/{m['folder']}",
                    "status": status,
                    "pct": progress["percent"],
                    "locked": locked,
                    "source": source_name,
                    "track": track,
                })

    done_count = sum(1 for s in steps if s["status"] == "done")

    return render_template(
        "dashboard/index.html",
        user=user,
        steps=steps,
        done_count=done_count,
        total=len(steps),
    )
