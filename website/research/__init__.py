"""
The `research` blueprint handles dipsplaying research.
"""
from flask import Blueprint

research_blueprint = Blueprint("research", __name__, template_folder="templates")

from . import routes
