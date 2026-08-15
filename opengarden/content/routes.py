from flask import render_template, request, redirect, url_for, abort, session
from opengarden.content import content_bp
from opengarden.auth.utils import login_required
from opengarden.content_loader import (
    load_lesson, load_track_modules, available_translations,
    load_sources, get_all_tracks,
)
from opengarden.question_engine import get_answer_map, check_answer, upsert_answer
import markdown


@content_bp.route("/")
@login_required
def index():
    sources = load_sources()
    overview = []
    for source in sources:
        tracks = get_all_tracks(source["name"])
        track_data = []
        for track in tracks:
            modules = load_track_modules(source["name"], track)
            track_data.append({"name": track, "modules": modules})
        overview.append({
            "source": source,
            "tracks": track_data,
        })
    return render_template("content/index.html", overview=overview)


@content_bp.route("/<source_name>/<track>/overview")
@login_required
def overview(source_name, track):
    modules = load_track_modules(source_name, track)
    if not modules:
        abort(404)
    return render_template(
        "content/overview.html",
        source=source_name, track=track, modules=modules
    )


@content_bp.route("/<source_name>/<track>/<module>")
@login_required
def lesson(source_name, track, module):
    lang = request.args.get("lang")
    lesson_data = load_lesson(source_name, track, module, lang=lang)
    if not lesson_data:
        abort(404)

    vertalingen = available_translations(source_name, track, module)
    html_content = markdown.markdown(lesson_data["content"], extensions=["extra"])

    user_id = session["user_id"]
    answer_map = get_answer_map(user_id, lesson_data["module_slug"])

    total = len(lesson_data["questions"])
    correct = sum(
        1 for q in lesson_data["questions"]
        if answer_map.get(q["id"]) and answer_map[q["id"]].is_correct
    )

    return render_template(
        "content/lesson.html",
        lesson=lesson_data,
        html_content=html_content,
        answer_map=answer_map,
        total_questions=total,
        correct_count=correct,
        beschikbare_vertalingen=vertalingen,
        huidige_taal=lesson_data["content_lang"],
        source=source_name,
        track=track,
        module_name=module,
    )


@content_bp.route("/submit-answer", methods=["POST"])
@login_required
def submit_answer():
    module_slug = request.form.get("module_slug")
    question_id = request.form.get("question_id")
    user_answer = request.form.get(question_id)
    source = request.form.get("source")
    track = request.form.get("track")
    module = request.form.get("module")

    lesson_data = load_lesson(source, track, module)
    if not lesson_data:
        abort(404)

    question = next(
        (q for q in lesson_data["questions"] if q["id"] == question_id), None
    )
    if not question:
        abort(404)

    user_id = session["user_id"]

    if question.get("type") == "open":
        upsert_answer(
            user_id, module_slug, question_id, user_answer,
            is_correct=False, totaal_vragen=len(lesson_data["questions"])
        )
    else:
        is_correct = check_answer(question, user_answer)
        upsert_answer(
            user_id, module_slug, question_id, user_answer,
            is_correct=is_correct, totaal_vragen=len(lesson_data["questions"])
        )

    return redirect(
        url_for("content.lesson", source_name=source, track=track, module=module)
        + f"#{question_id}"
    )
