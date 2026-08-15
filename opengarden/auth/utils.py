from functools import wraps
from flask import session, redirect, url_for, flash, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Log eerst in.", "warning")
            return redirect(url_for("auth.login", next=request.full_path))
        return f(*args, **kwargs)
    return decorated_function
