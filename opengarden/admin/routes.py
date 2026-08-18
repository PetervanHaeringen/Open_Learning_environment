from flask import render_template, redirect, url_for, flash, session, request
from functools import wraps
from opengarden.admin import admin_bp
from opengarden.auth.utils import login_required
from opengarden.extensions import db
from opengarden.models import User, UserModule
from opengarden.content_loader import load_sources, get_all_tracks, load_track_modules
from opengarden.sync_manager import sync_source, get_sync_status
from opengarden.content_loader import load_sources

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Alleen admins mogen dit.", "danger")
            return redirect(url_for("dashboard.index"))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route("/")
@login_required
@admin_required
def index():
    users = User.query.order_by(User.username.asc()).all()
    return render_template("admin/index.html", users=users)


@admin_bp.route("/set-role/<username>/<role>")
@login_required
@admin_required
def set_role(username, role):
    if role not in ("student", "teacher", "admin"):
        flash("Ongeldige rol.", "warning")
        return redirect(url_for("admin.index"))

    user = User.query.filter_by(username=username).first()
    if not user:
        flash("Gebruiker niet gevonden.", "warning")
        return redirect(url_for("admin.index"))

    user.role = role
    db.session.commit()
    flash(f"{username} is nu {role}.", "success")
    return redirect(url_for("admin.index"))


def _get_all_modules():
    """Haal alle modules op uit alle bronnen, gegroepeerd per bron/track."""
    result = []
    for source in load_sources():
        source_name = source["name"]
        tracks = get_all_tracks(source_name)
        for track in tracks:
            modules = load_track_modules(source_name, track)
            result.append({
                "source": source_name,
                "track": track,
                "modules": modules,
            })
    return result


@admin_bp.route("/assign/<username>")
@login_required
@admin_required
def assign_form(username):
    """Toon een overzicht van alle modules met vinkjes voor deze gebruiker."""
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("Gebruiker niet gevonden.", "warning")
        return redirect(url_for("admin.index"))

    assigned = {
        um.module_slug for um in UserModule.query.filter_by(user_id=user.id).all()
    }

    all_modules = _get_all_modules()

    return render_template(
        "admin/assign.html",
        user=user,
        all_modules=all_modules,
        assigned=assigned,
    )


@admin_bp.route("/assign/<username>", methods=["POST"])
@login_required
@admin_required
def assign_save(username):
    """Sla de toegewezen modules op voor deze gebruiker."""
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("Gebruiker niet gevonden.", "warning")
        return redirect(url_for("admin.index"))

    UserModule.query.filter_by(user_id=user.id).delete()

    selected = request.form.getlist("module_slug")
    admin_id = session["user_id"]

    for slug in selected:
        um = UserModule(
            user_id=user.id,
            module_slug=slug,
            assigned_by=admin_id,
        )
        db.session.add(um)

    db.session.commit()
    flash(f"Toewijzingen voor {username} bijgewerkt.", "success")
    return redirect(url_for("admin.assign_form", username=username))


@admin_bp.route("/sources")
@login_required
@admin_required
def sources_overview():
    """Toon alle bronnen met sync-status."""
    all_sources = []
    for source in load_sources():
        info = dict(source)
        status, detail = get_sync_status(source["name"])
        info["sync_status"] = status
        info["sync_detail"] = detail
        all_sources.append(info)
    return render_template("admin/sources.html", sources=all_sources)


@admin_bp.route("/sync/<source_name>")
@login_required
@admin_required
def sync_git_source(source_name):
    success, message = sync_source(source_name)
    flash(message, "success" if success else "danger")
    return redirect(url_for("admin.sources_overview"))