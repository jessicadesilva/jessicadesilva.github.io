from . import groups_blueprint
from flask import render_template


@groups_blueprint.route("/")
def mentor_group():
    # This is a placeholder for the mentor group page
    pass


@groups_blueprint.route("/math")
def mentor_groups_math():
    return render_template("mentor_groups_math.j2")


@groups_blueprint.route("/stan")
def mentor_groups_stan():
    return render_template("mentor_groups_stan.j2")
