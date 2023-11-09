"""
The `events` blueprint handles dipsplaying events pages.
"""
from . import controllers
from flask import Blueprint

events_blueprint = Blueprint("events", __name__, template_folder="templates")
