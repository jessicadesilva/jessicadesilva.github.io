"""
The `groups` blueprint handles dipsplaying mentor group pages.
"""
from . import controllers
from flask import Blueprint

groups_blueprint = Blueprint("groups", __name__, template_folder="templates")
