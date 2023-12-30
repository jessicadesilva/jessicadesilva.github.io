# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set environment variables.
"""
import os

from environs import Env

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)

env = Env()
env.read_env()


ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.join(PROJECT_ROOT, 'instance', 'app.db')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = env.str("UPLOAD_FOLDER")
CKEDITOR_ENABLE_CSRF = True
