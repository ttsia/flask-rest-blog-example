import datetime
import os

DEFAULT_SECRET_KEY = "Pikachu"


class Config(object):
    DEBUG = False

    SECRET_KEY = os.environ.get("SECRET_KEY", DEFAULT_SECRET_KEY)

    JWT_SECRET_KEY = os.environ.get(SECRET_KEY)
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_HOST = os.environ.get("POSTGRES_HOST")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    print(SQLALCHEMY_DATABASE_URI)
