"""
Maak een bestaande gebruiker admin zonder in de database te hoeven rommelen.
Gebruik: python make_admin.py <gebruikersnaam>
"""
import sys
from opengarden import create_app
from opengarden.extensions import db
from opengarden.models import User

app = create_app()

with app.app_context():
    if len(sys.argv) < 2:
        print("Gebruik: python make_admin.py <gebruikersnaam>")
        sys.exit(1)

    username = sys.argv[1]
    user = User.query.filter_by(username=username).first()

    if not user:
        print(f"Gebruiker '{username}' niet gevonden.")
        sys.exit(1)

    user.role = "admin"
    db.session.commit()
    print(f"✅ {username} is nu admin.")