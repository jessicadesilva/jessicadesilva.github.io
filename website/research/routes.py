# -*- coding: utf-8 -*-
"""Research section, including current and former undergraduate projects."""
import os

from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from werkzeug.utils import secure_filename


from website.extensions import database
from website.utils import clean_input, dev_utils
from website.research.forms import ProjectForm
from website.research.models import Project, ProjectType, UndergradStatus
from website.research.utils import image_folder, set_select_options


blueprint = Blueprint(
    "research", __name__, url_prefix="/research", static_folder="../static"
)

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


@blueprint.route("/undergrad/current.html")
@dev_utils
def current_undergrad_projects(*args, **kwargs):
    """Display current undergraduate projects."""

    data = []

    for project in database.session.execute(database.select(Project)).scalars().all():
        if project.status_rel.status == "current":
            output_data = {
                "id": project.id,
                "type": project.type_rel.type,
                "status": project.status_rel.status,
                "image": url_for("static", filename=f"images/projects/{project.image}"),
                "advisors": project.advisors if project.advisors != "" else None,
                "students": project.students,
                "majors": project.majors if project.majors != "" else None,
                "title": project.title,
                "description": project.description,
                "link": project.link if project.link != "" else None,
            }
            data.append(output_data)

    return render_template(
        "research/current_ugrad_projects.j2", data=data, *args, **kwargs
    )


@blueprint.route("/undergrad/current/abstracts.html")
def current_undergrad_abstracts():
    return render_template("research/current_ugrad_abstracts.j2")


@blueprint.route("/undergrad/former.html")
def former_undergrad_projects():
    return render_template("research/former_ugrad_projects.j2")


@blueprint.route("/other.html")
def other_projects():
    return render_template("research/other_projects.j2")


@blueprint.route("/projects/<project_name>.html")
def project(project_name):
    if project_name not in project_pages:
        abort(404)

    return render_template(f"{project_name}.j2")


@blueprint.route("/add_project.html", methods=["GET", "POST"])
def add_project(*args, **kwargs):
    """Add a project."""

    form = ProjectForm()
    set_select_options(form)

    if request.method == "POST":
        if form.validate_on_submit():
            if not form.image.data and not form.upload.data:
                default_image = "default.jpg"

            if form.image.data:
                filename = form.image.data

            if form.upload.data:
                file = form.upload.data
                filename = secure_filename(file.filename)
                try:
                    file.save(os.path.join(image_folder(), filename))
                    flash("File successfully uploaded.", "success")
                except Exception as e:
                    flash(f"500: {e}", "error")
                    abort(500)

            Project.create(
                type_id=form.type_id.data,
                status_id=form.status_id.data,
                image=filename if filename else default_image,
                advisors=clean_input(form.advisors.data),
                students=clean_input(form.students.data),
                majors=clean_input(form.majors.data, allow_tags=None),
                title=clean_input(form.title.data, allow_tags=None),
                description=clean_input(form.description.data),
                link=clean_input(form.link.data, allow_tags="a"),
            )
            flash(f"{clean_input(form.title.data)} successfully added.", "success")
            return redirect(request.url)

    return render_template("research/add_project.j2", form=form)


@blueprint.route("/edit_project/<int:project_id>.html", methods=["GET", "POST"])
def edit_project(project_id: int):
    """Edit a project."""

    form = ProjectForm()
    project = Project.get_by_id(project_id)

    set_select_options(form)

    if not project:
        flash(f"Project with ID {project_id} does not exist.", "error")
        abort(404)

    if request.method == "POST":
        if form.validate_on_submit():
            filename = None
            if form.upload.data:
                file = form.upload.data
                filename = secure_filename(file.filename)
                try:
                    file.save(os.path.join(image_folder(), filename))
                    flash("File successfully uploaded.", "success")
                except OSError as e:
                    flash(f"500: {e}", "error")
                    abort(500)
            project.update(
                commit=True,
                type_id=form.type_id.data,
                status_id=form.status_id.data,
                image=filename if filename else form.image.data,
                advisors=clean_input(form.advisors.data),
                students=clean_input(form.students.data),
                majors=clean_input(form.majors.data, allow_tags=None),
                title=clean_input(form.title.data, allow_tags=None),
                description=clean_input(form.description.data),
                link=clean_input(form.link.data, allow_tags="a"),
            )
            flash(f"{clean_input(form.title.data)} successfully updated.", "success")
            return redirect(request.url)

    form.type_id.data = project.type_id
    form.status_id.data = project.status_id
    form.image.data = project.image
    form.advisors.data = project.advisors
    form.students.data = project.students
    form.majors.data = project.majors
    form.title.data = project.title
    form.description.data = project.description
    form.link.data = project.link

    return render_template("research/edit_project.j2", project=project, form=form)


@blueprint.route("/delete_project/<int:project_id>.html", methods=["GET", "POST"])
def delete_project(project_id: int):
    """Delete a project."""

    project = Project.get_by_id(project_id)

    if not project:
        flash(f"Project with ID {project_id} does not exist.", "error")
        abort(404)

    if request.method == "POST":
        project.delete()
        flash(f"{project.title} successfully deleted.", "success")
        return redirect(url_for("research.current_undergrad_projects"))

    form = ProjectForm()
    flash(f"Are you sure you want to delete {project.title}?", "warning")

    return render_template("research/delete_project.j2", project=project, form=form)
