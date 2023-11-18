"""
The `research` blueprint handles dipsplaying research pages.
"""
from flask import Blueprint, render_template, abort

research_blueprint = Blueprint("research", __name__, template_folder="templates")

# Add current undergraduate projects here
# NOTE: the project must be located in the `projects` directory
# NOTE: the project name must match the name of the jinja2 file
#       and should exclude the file extension
#       (i.e. <project_name>.j2)
# NOTE: projects are displayed in the order they are listed
current_ugrad_project_names = [
    "ev_charging_desert",
    "cnn_medical_imaging",
]

# Add former undergraduate projects here
# NOTE: the project must be located in the `projects` directory
# NOTE: the project name must match the name of the jinja2 file
#       and should exclude the file extension
#       (i.e. <project_name>.j2)
# NOTE: projects are displayed in the order they are listed
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

# Add current undergraduate abstracts here
# NOTE: the project must be located in the `abstracts` directory
# NOTE: the project name must match the name of the jinja2 file
#       and should exclude the file extension
#       (i.e. abstract_<project_name>.j2)
# NOTE: projects are displayed in the order they they are listed
current_ugrad_abstract_names = [
    "abstract_hypergraph_image_segmentation",
    "abstract_mean_shift_clustering",
    "abstract_pokemon_go_optimization",
    "abstract_embryo_cell_migration",
    "abstract_math_course_success",
    "abstract_track_performances",
]

# Add projects that have their own page here.
# (i.e. pages that have an embedded pdf)
#
# NOTE: These pages are located in the `research/templates` folder.
project_pages = [
    "ev_charging_poster",
    "walking_time_poster",
]


@research_blueprint.route("/undergrad/current.html")
def current_undergrad_projects():
    return render_template(
        "current_ugrad_projects.j2",
        project_names=current_ugrad_project_names,
    )


@research_blueprint.route("/undergrad/current/abstracts.html")
def current_undergrad_abstracts():
    return render_template(
        "current_ugrad_projects_abstracts.j2",
        project_names=current_ugrad_abstract_names,
    )


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
