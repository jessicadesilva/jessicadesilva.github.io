from . import groups_blueprint
from flask import render_template


@groups_blueprint.route("/mentor-groups/math")
def mentor_groups_math():
    return render_template("mentor_groups_math.html")


@groups_blueprint.route("/mentor-groups/stan")
def mentor_groups_stan():
    return render_template("mentor_groups_stan.html")
