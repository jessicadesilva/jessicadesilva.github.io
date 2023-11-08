"""
The 'core' blueprint handles displaying the home page and other static pages.
"""
from flask import Blueprint

core_blueprint = Blueprint("core", __name__, template_folder="templates")

from . import routes
