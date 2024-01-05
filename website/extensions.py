# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in __init__.py."""
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

ckeditor = CKEditor()
csrf_protect = CSRFProtect()
database = SQLAlchemy()
migrate = Migrate()
