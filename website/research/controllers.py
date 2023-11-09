from . import research_blueprint
from flask import render_template, abort

# List of all projects that have their own page
project_names = ["ev_charging_poster", "walking_time_poster"]


@research_blueprint.route("/")
def research():
    # This is a placeholder for the research page
    pass


@research_blueprint.route("/undergrad/current")
def current_undergrad_projects():
    return render_template("research/current_ugrad_projects.j2")


@research_blueprint.route("/undergrad/current/abstracts")
def current_undergrad_abstracts():
    return render_template("research/current_ugrad_projects_abstracts.j2")


@research_blueprint.route("/undergrad/former")
def former_undergrad_projects():
    return render_template("research/former_ugrad_projects.j2")


@research_blueprint.route("/other")
def other_research_projects():
    return render_template("research/other_research_projects.j2")


@research_blueprint.route("/projects/<project_name>")
def project(project_name):
    if project_name not in project_names:
        abort(404)

    return render_template(f"research/{project_name}.j2")
