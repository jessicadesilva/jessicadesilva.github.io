from . import research_blueprint
from flask import render_template


@research_blueprint.route("/research")
def research():
    # This is a placeholder for the research page
    pass


@research_blueprint.route("/research/undergrad/current")
def current_undergrad_projects():
    return render_template("current_undergrad_projects.html")


@research_blueprint.route("/research/undergrad/current/abstracts")
def current_undergrad_abstracts():
    return render_template("current_undergrad_projects_abstracts.html")


@research_blueprint.route("/research/undergrad/former")
def former_undergrad_projects():
    return render_template("former_undergrad_projects.html")


@research_blueprint.route("/research/other")
def other_research_projects():
    return render_template("other_research_projects.html")
