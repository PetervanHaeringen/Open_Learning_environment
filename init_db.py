from opengarden import create_app
from opengarden.extensions import db


def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tabellen aangemaakt.")


if __name__ == "__main__":
    init_db()
