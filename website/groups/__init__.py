"""
The `groups` blueprint handles dipsplaying mentor group pages.
"""
from flask import Blueprint

groups_blueprint = Blueprint("groups", __name__, template_folder="templates")

from . import controllers
