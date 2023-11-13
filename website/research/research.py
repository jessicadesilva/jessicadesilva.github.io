"""
The `research` blueprint handles dipsplaying research pages.
"""
from flask import Blueprint, render_template, abort

research_blueprint = Blueprint("research", __name__, template_folder="templates")


# List of all projects that have their own page
project_names = ["ev_charging_poster", "walking_time_poster"]


@research_blueprint.route("/undergrad/current.html")
def current_undergrad_projects():
    return render_template("current_ugrad_projects.j2")


@research_blueprint.route("/undergrad/current/abstracts.html")
def current_undergrad_abstracts():
    return render_template("current_ugrad_projects_abstracts.j2")


@research_blueprint.route("/undergrad/former.html")
def former_undergrad_projects():
    return render_template("former_ugrad_projects.j2")


@research_blueprint.route("/other.html")
def other_research_projects():
    return render_template("other_research_projects.j2")


@research_blueprint.route("/projects/<project_name>.html")
def project(project_name):
    if project_name not in project_names:
        abort(404)

    return render_template(f"{project_name}.j2")
