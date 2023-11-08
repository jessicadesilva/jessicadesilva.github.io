"""
The `groups` blueprint handles dipsplaying groups.
"""
from flask import Blueprint

groups_blueprint = Blueprint("groups", __name__, template_folder="templates")

from . import routes
