from flask import render_template, redirect, url_for, request, flash, session
from sqlalchemy.exc import IntegrityError
from opengarden.auth import auth_bp
from opengarden.extensions import db
from opengarden.models import User


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not username or not email or not password:
            flash("Vul alle velden in.", "error")
            return redirect(url_for("auth.register"))

        if User.query.filter_by(username=username).first():
            flash("Gebruikersnaam bestaat al.", "error")
            return redirect(url_for("auth.register"))

        if User.query.filter_by(email=email).first():
            flash("E-mailadres is al geregistreerd.", "error")
            return redirect(url_for("auth.register"))

        user = User(username=username, email=email)
        user.set_password(password)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Deze gebruiker bestaat al.", "error")
            return redirect(url_for("auth.register"))

        flash("Registratie succesvol! Log nu in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash("Ongeldige inloggegevens.", "error")
            return redirect(url_for("auth.login"))

        session["user_id"] = user.id
        session["username"] = user.username
        session["role"] = user.role

        flash(f"Welkom terug, {user.username}!", "success")

        next_url = request.args.get("next")
        return redirect(next_url or url_for("dashboard.index"))

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Je bent uitgelogd.", "success")
    return redirect(url_for("auth.login"))
