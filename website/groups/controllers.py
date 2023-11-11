"""
The `groups` blueprint handles dipsplaying mentor group pages.
"""
from flask import Blueprint, render_template

groups_blueprint = Blueprint("groups", __name__, template_folder="templates")


@groups_blueprint.route("/math.html")
def mentor_groups_math():
    return render_template("mentor_groups_math.j2")


@groups_blueprint.route("/stan.html")
def mentor_groups_stan():
    return render_template("mentor_groups_stan.j2")
