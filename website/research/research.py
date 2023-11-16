"""
The `research` blueprint handles dipsplaying research pages.
"""
from flask import Blueprint, render_template, abort

research_blueprint = Blueprint("research", __name__, template_folder="templates")

# Add projects by current undergraduate students here.
# The project should be a `.j2` file in the `projects` folder.
# The name of the file should be the same as,
# or a shortened version of the name of the project.
# The `.j2` extension should be omitted.
#
# NOTE: Projects are displayed in the order they are listed here.
# NOTE: The `projects` directory shares projects from current and former students.
current_ugrad_project_names = ["ev_charging_desert", "cnn_medical_imaging"]

# Add projects by former undergraduate students here.
# See instructions and notes from `current_ugrad_project_names`.
former_ugrad_project_names = [
    "analysis_campus_walk_times",
    "mathematical_fairness_districting",
    "turan_vertex_cliques",
    "anti_ramsey_multiplicities",
    "hypergraph_image_segmentation",
    "mean_shift_clustering",
    "pokemon_go_optimization",
    "embryo_cell_migration",
    "predictive_math_course_success",
    "predictive_track_performances",
]

# Add projects that have their own page here.
# (i.e. pages that have an embedded pdf)
#
# NOTE: These pages are located in the `research/templates` folder.
project_pages = ["ev_charging_poster", "walking_time_poster"]


# This page will display the projects listed in `current_ugrad_projects`
# from the `research/templates/projects` directory.
@research_blueprint.route("/undergrad/current.html")
def current_undergrad_projects():
    return render_template(
        "current_ugrad_projects.j2",
        project_names=current_ugrad_project_names,
    )


@research_blueprint.route("/undergrad/current/abstracts.html")
def current_undergrad_abstracts():
    return render_template("current_ugrad_projects_abstracts.j2")


# This page will display the projects listed in `former_ugrad_projects`
# from the `research/templates/projects` directory.
@research_blueprint.route("/undergrad/former.html")
def former_undergrad_projects():
    return render_template(
        "former_ugrad_projects.j2",
        project_names=former_ugrad_project_names,
    )


@research_blueprint.route("/other.html")
def other_research_projects():
    return render_template("other_research_projects.j2")


@research_blueprint.route("/projects/<project_name>.html")
def project(project_name):
    if project_name not in project_pages:
        abort(404)

    return render_template(f"{project_name}.j2")
