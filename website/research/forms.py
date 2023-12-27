# -*- coding: utf-8 -*-
"""Event forms."""
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import SelectField, StringField, FileField
from wtforms.validators import DataRequired

from website.utils import clean_input
from website.research.models import Project
from website.research.utils import allowed_file
from website.research.validator import ProjectValidator


class ProjectForm(FlaskForm):
    """Multi-purpose project form."""

    # Choices for dynamic select fields are set in the view function.
    # https://wtforms.readthedocs.io/en/3.1.x/fields/#wtforms.fields.SelectField
    type_id = SelectField("Project Type", coerce=int, validators=[DataRequired()])
    status_id = SelectField("Undergrad Status", coerce=int, validators=[DataRequired()])

    image = SelectField("Existing Image")
    upload = FileField("Upload New Image")

    advisors = CKEditorField("Advisors")
    students = CKEditorField("Students", validators=[DataRequired()])
    majors = StringField("Majors")
    title = StringField("Project Title", validators=[DataRequired()])
    description = CKEditorField("Project Description", validators=[DataRequired()])
    link = StringField("Project Link")

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

    def validate(self, **kwargs):
        initial_validation = super(ProjectForm, self).validate()

        if not initial_validation:
            return False

        if (
            not allowed_file(self.upload.data.filename)
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            # https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/
            and self.upload.data.filename != ""
        ):
            self.upload.errors.append("File type not allowed.")
            return False

        project = ProjectValidator(
            type_id=self.type_id.data,
            status_id=self.status_id.data,
            image=self.upload.data.filename if self.upload.data else self.image.data,
            advisors=clean_input(self.advisors.data),
            students=clean_input(self.students.data),
            majors=clean_input(self.majors.data),
            title=clean_input(self.title.data),
            description=clean_input(self.description.data),
            link=clean_input(self.link.data),
        )

        try:
            ProjectValidator.model_validate(project)
        except ValueError as error:
            self.title.errors.append(f"{error}")
            return False

        new_project = Project(
            type_id=project.type_id,
            status_id=project.status_id,
            image=project.image,
            advisors=project.advisors,
            students=project.students,
            majors=project.majors,
            title=project.title,
            description=project.description,
            link=project.link,
        )

        if Project.search_for_project(new_project) is not None:
            self.title.errors.append("Project already exists.")
            return False

        return True
