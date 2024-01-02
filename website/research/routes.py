# -*- coding: utf-8 -*-
"""Research section, including current and former undergraduate projects."""
import os
from http import HTTPStatus

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from website.research.forms import ProjectForm
from website.research.models import Project
from website.research.utils import (
    create_output_dict,
    get_projects_by_type_and_status,
    image_folder,
    poster_pages,
    set_image_select_options,
    set_status_id_select_options,
    set_type_id_select_options,
)
from website.utils import clean_input, dev_utils

blueprint = Blueprint(
    "research", __name__, url_prefix="/research", static_folder="../static"
)

poster_pages = poster_pages()


@blueprint.route("/undergrad/current.html")
@dev_utils
def current_undergrad_projects(debug=False):
    data = []

    for project in get_projects_by_type_and_status("project", "current"):
        data.append(create_output_dict(project))

    return (
        render_template("research/current_ugrad_projects.j2", data=data, debug=debug),
        HTTPStatus.OK,
    )


@blueprint.route("/undergrad/current/abstracts.html")
@dev_utils
def current_undergrad_abstracts(debug=False):
    data = []

    for project in get_projects_by_type_and_status("abstract", "current"):
        data.append(create_output_dict(project))

    return (
        render_template("research/current_ugrad_abstracts.j2", data=data, debug=debug),
        HTTPStatus.OK,
    )


@blueprint.route("/undergrad/former.html")
@dev_utils
def former_undergrad_projects(debug=False):
    data = []

    for project in get_projects_by_type_and_status("project", "former"):
        data.append(create_output_dict(project))

    return (
        render_template("research/former_ugrad_projects.j2", data=data, debug=debug),
        HTTPStatus.OK,
    )


@blueprint.route("/other.html")
@dev_utils
def other_projects(debug=False):
    return render_template("research/other_projects.j2", debug=debug), HTTPStatus.OK


@blueprint.route("/projects/<poster>.html")
def project(poster: str):
    if poster not in poster_pages:
        abort(HTTPStatus.NOT_FOUND)

    return render_template(f"research/posters/{poster}.j2"), HTTPStatus.OK


@blueprint.route("/add_project.html", methods=["GET", "POST"])
def add_project():
    form = ProjectForm()
    set_type_id_select_options(form)
    set_status_id_select_options(form)
    set_image_select_options(form)

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
                abort(HTTPStatus.INTERNAL_SERVER_ERROR)

        Project.create(
            type_id=form.type_id.data,
            status_id=form.status_id.data,
            image=filename if filename else default_image,
            advisors=clean_input(form.advisors.data),
            students=clean_input(form.students.data),
            majors=clean_input(form.majors.data, allow_tags=None),
            title=clean_input(form.title.data, allow_tags=None),
            description=clean_input(
                form.description.data,
                allow_tags=["a", "b", "em", "i", "strong", "p"],
            ),
            link=clean_input(form.link.data, allow_tags="a"),
        )
        flash(f"{clean_input(form.title.data)} successfully added.", "success")
        return (
            render_template("research/add_project.j2", form=form),
            HTTPStatus.CREATED,
        )

    return render_template("research/add_project.j2", form=form), HTTPStatus.OK


@blueprint.route("/edit_project/<int:project_id>.html", methods=["GET", "POST"])
def edit_project(project_id: int):
    project = Project.get_by_id(project_id)

    if not project:
        flash(f"Project with ID {project_id} does not exist.", "error")
        abort(HTTPStatus.NOT_FOUND)

    form = ProjectForm()
    set_type_id_select_options(form)
    set_status_id_select_options(form)
    set_image_select_options(form)

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
                abort(HTTPStatus.INTERNAL_SERVER_ERROR)
        project.update(
            commit=True,
            type_id=form.type_id.data,
            status_id=form.status_id.data,
            image=filename if filename else form.image.data,
            advisors=clean_input(form.advisors.data),
            students=clean_input(form.students.data),
            majors=clean_input(form.majors.data, allow_tags=None),
            title=clean_input(form.title.data, allow_tags=None),
            description=clean_input(
                form.description.data,
                allow_tags=["a", "b", "em", "i", "strong", "p"],
            ),
            link=clean_input(form.link.data, allow_tags="a"),
        )
        flash(f"{clean_input(form.title.data)} successfully updated.", "success")
        return (
            render_template("research/edit_project.j2", project=project, form=form),
            HTTPStatus.OK,
        )

    form.type_id.data = project.type_id
    form.status_id.data = project.status_id
    form.image.data = project.image
    form.advisors.data = project.advisors
    form.students.data = project.students
    form.majors.data = project.majors
    form.title.data = project.title
    form.description.data = project.description
    form.link.data = project.link

    return (
        render_template("research/edit_project.j2", project=project, form=form),
        HTTPStatus.OK,
    )


@blueprint.route("/delete_project/<int:project_id>.html", methods=["GET", "POST"])
def delete_project(project_id: int):
    project = Project.get_by_id(project_id)

    if not project:
        flash(f"Project with ID {project_id} does not exist.", "error")
        abort(HTTPStatus.NOT_FOUND)

    if request.method == "POST":
        project.delete()
        flash(f"{project.title} successfully deleted.", "success")
        return redirect(url_for("research.current_undergrad_projects"))

    form = ProjectForm()
    flash(f"Are you sure you want to delete {project.title}?", "warning")

    return (
        render_template("research/delete_project.j2", project=project, form=form),
        HTTPStatus.OK,
    )
