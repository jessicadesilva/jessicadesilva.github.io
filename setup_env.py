# -*- coding: utf-8 -*-
"""Initialize Flask environment."""
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

FLASK_ENV = "development"
DEBUG = FLASK_ENV == "development"
SECRET_KEY = os.urandom(24).hex()
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.join(PROJECT_ROOT, 'instance', 'app.db')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, "website", "static", "images", "projects")
CKEDITOR_ENABLE_CSRF = True
ALLOWED_EXTENSION = {"pdf", "png", "jpg", "jpeg", "gif"}


if __name__ == "__main__":
    with open(".env", "w") as f:
        f.write(f"FLASK_ENV={FLASK_ENV}\n")
        f.write(f"DEBUG={DEBUG}\n")
        f.write(f"SECRET_KEY={SECRET_KEY}\n")
        f.write(f"SQLALCHEMY_DATABASE_URI={SQLALCHEMY_DATABASE_URI}\n")
        f.write(f"SQLALCHEMY_TRACK_MODIFICATIONS={SQLALCHEMY_TRACK_MODIFICATIONS}\n")
        f.write(f"UPLOAD_FOLDER={UPLOAD_FOLDER}\n")
        f.write(f"CKEDITOR_ENABLE_CSRF={CKEDITOR_ENABLE_CSRF}\n")
        f.write(f"ALLOWED_EXTENSION={ALLOWED_EXTENSION}\n")
