# -*- coding: utf-8 -*-
"""Research module utility and helper functions."""
import os

from website.extensions import database
from website.research.models import Project, ProjectType, UndergradStatus

HERE = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(HERE, os.pardir)
PROJECT_IMAGES = os.path.join(APP_DIR, "static", "images", "projects")
PROJECT_POSTERS = os.path.join(APP_DIR, "static", "images", "posters")
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}
POSTER_PAGES = os.path.join(APP_DIR, "templates", "research", "posters")


def allowed_file(filename):
    # Check if file extension is allowed
    # https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def image_folder():
    return PROJECT_IMAGES


def poster_image_folder():
    return PROJECT_POSTERS


def poster_pages():
    poster_pages = []
    for file in os.listdir(POSTER_PAGES):
        if file.endswith(".j2"):
            poster_pages.append(file[:-3])
    return poster_pages


def set_type_id_select_options(form) -> None:
    form.type_id.choices = [(0, "Select a project type...")] + [
        (project_type.id, project_type.type)
        for project_type in database.session.query(ProjectType).all()
    ]


def set_status_id_select_options(form) -> None:
    form.status_id.choices = [(0, "Select a project status...")] + [
        (project_status.id, project_status.status)
        for project_status in database.session.query(UndergradStatus).all()
    ]


def set_image_select_options(form) -> None:
    form.image.choices = [("default.jpg", "Select a project image...")] + [
        (image, image) for image in os.listdir(image_folder())
    ]


def create_output_dict(project: Project) -> dict:
    return {
        "id": project.id,
        "type": project.type_rel.type,
        "status": project.status_rel.status,
        "image": project.image,
        "advisors": project.advisors if project.advisors != "" else None,
        "students": project.students,
        "majors": project.majors if project.majors != "" else None,
        "title": project.title,
        "description": project.description,
        "link": project.link if project.link != "" else None,
    }
