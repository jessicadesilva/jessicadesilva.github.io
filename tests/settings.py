"""Settings module for test app."""
from environs import Env

env = Env()
env.read_env()

ENV = "development"
TESTING = True
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "sqlite://"
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = "/tmp"
CKEDITOR_ENABLE_CSRF = False
