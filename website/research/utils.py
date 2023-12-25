# -*- coding: utf-8 -*-
"""Research module utility and helper functions."""
import os

from website.extensions import database
from website.research.models import ProjectType, UndergradStatus

HERE = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(HERE, os.pardir)
PROJECT_IMAGES = os.path.join(APP_DIR, "static", "images", "projects")
PROJECT_POSTERS = os.path.join(APP_DIR, "static", "images", "posters")
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    """Check if the file extension is allowed."""
    # https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def image_folder():
    return PROJECT_IMAGES


def poster_folder():
    return PROJECT_POSTERS


def set_select_options(form):
    """Set select options for dynamic select fields."""
    form.type_id.choices = [(0, "Select a project type...")] + [
        (project_type.id, project_type.type)
        for project_type in database.session.query(ProjectType).all()
    ]
    form.status_id.choices = [(0, "Select a project status...")] + [
        (project_status.id, project_status.status)
        for project_status in database.session.query(UndergradStatus).all()
    ]
    form.image.choices = [("default.jpg", "Select a project image...")] + [
        (image, image) for image in os.listdir(image_folder())
    ]
