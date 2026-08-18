import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///instance/opengarden.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    # In ontwikkeling mag een fallback, maar met waarschuwing
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key-niet-gebruiken-in-productie"

class ProductionConfig(Config):
    DEBUG = False
    # In productie: GEEN fallback. Start niet zonder echte SECRET_KEY.
    @property
    def SECRET_KEY(self):
        key = os.environ.get("SECRET_KEY")
        if not key:
            raise RuntimeError(
                "SECRET_KEY environment variable is niet gezet! "
                "Zet een sterke secret key voor productie. "
                "Bijvoorbeeld: export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')"
            )
        return key

config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
