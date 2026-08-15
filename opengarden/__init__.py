import os
from flask import Flask, render_template
from opengarden.config import Config
from opengarden.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    @app.context_processor
    def inject_globals():
        from flask import session
        return {
            "current_role": session.get("role", "guest"),
        }

    from opengarden.auth import auth_bp
    from opengarden.content import content_bp
    from opengarden.dashboard import dashboard_bp
    from opengarden.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(content_bp, url_prefix="/content")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
