from . import research_blueprint
from flask import render_template


@research_blueprint.route("/current-undergrad-projects")
def current_undergrad_projects():
    return render_template("current_undergrad_projects.html")


@research_blueprint.route("/current-undergrad-projects/abstracts")
def current_undergrad_projects_abstracts():
    return render_template("current_undergrad_projects_abstracts.html")


@research_blueprint.route("/former-undergrad-projects")
def former_undergrad_projects():
    return render_template("former_undergrad_projects.html")


@research_blueprint.route("/other-research-projects")
def other_research_projects():
    return render_template("other_research_projects.html")
