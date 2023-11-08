"""
The `events` blueprint handles dipsplaying events.
"""
from flask import Blueprint

events_blueprint = Blueprint("events", __name__, template_folder="templates")

from . import routes
