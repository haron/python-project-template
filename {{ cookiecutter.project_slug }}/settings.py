import os
from pathlib import Path

import dj_database_url
from decouple import config

SENTRY_DSN = config("SENTRY_DSN", default="")
ENV = os.environ.get("ENV", "dev")
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {"default": dj_database_url.parse(config("DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3"))}
INSTALLED_APPS = ("db", "django_extensions")
