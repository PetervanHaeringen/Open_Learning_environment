from datetime import datetime
from sqlalchemy import UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from opengarden.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="student")
    dashboard_theme = db.Column(db.String(20), nullable=False, default="plant")
    module_visibility = db.Column(db.String(20), nullable=False, default="alles")
    last_seen = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserModule(db.Model):
    __tablename__ = "user_module"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    module_slug = db.Column(db.String(120), nullable=False)
    assigned_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    volgorde = db.Column(db.Integer, nullable=True)
    __table_args__ = (UniqueConstraint("user_id", "module_slug", name="uq_user_module"),)


class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    module_slug = db.Column(db.String(120), nullable=False)
    question_id = db.Column(db.String(120), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)
    attempts = db.Column(db.Integer, nullable=False, default=1)
    last_answer = db.Column(db.Text, nullable=True)
    answer_text = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    __table_args__ = (
        UniqueConstraint("user_id", "module_slug", "question_id", name="uq_user_module_question"),
    )


class ModuleVoortgang(db.Model):
    __tablename__ = "module_voortgang"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    module_slug = db.Column(db.String(120), nullable=False)
    gestart_op = db.Column(db.DateTime, nullable=True)
    afgerond_op = db.Column(db.DateTime, nullable=True)
    __table_args__ = (UniqueConstraint("user_id", "module_slug", name="uq_user_module_voortgang"),)
