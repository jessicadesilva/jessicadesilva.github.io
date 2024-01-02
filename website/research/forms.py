# -*- coding: utf-8 -*-
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, StringField
from wtforms.validators import DataRequired

from website.research.models import Project
from website.research.utils import allowed_file
from website.research.validator import ProjectValidator
from website.utils import clean_input


class ProjectForm(FlaskForm):
    """Multi-purpose project form."""

    # Choices for dynamic select fields are set in the view function.
    # https://wtforms.readthedocs.io/en/3.1.x/fields/#wtforms.fields.SelectField
    type_id = SelectField("Project Type", coerce=int, validators=[DataRequired()])
    status_id = SelectField("Undergrad Status", coerce=int, validators=[DataRequired()])
    image = SelectField("Existing Image")
    upload = FileField("Upload New Image")
    students = CKEditorField("Students", validators=[DataRequired()])
    advisors = CKEditorField("Advisors")
    majors = StringField("Majors")
    title = StringField("Project Title", validators=[DataRequired()])
    description = CKEditorField("Project Description", validators=[DataRequired()])
    link = CKEditorField("Project Link")

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

    def project_validator(self) -> ProjectValidator:
        return ProjectValidator(
            type_id=self.type_id.data,
            status_id=self.status_id.data,
            image=self.upload.data.filename if self.upload.data else self.image.data,
            advisors=clean_input(self.advisors.data),
            students=clean_input(self.students.data),
            majors=clean_input(self.majors.data, allow_tags=None),
            title=clean_input(self.title.data, allow_tags=None),
            description=clean_input(
                self.description.data, allow_tags=["a", "b", "em", "i", "strong", "p"]
            ),
            link=clean_input(self.link.data, allow_tags="a"),
        )

    def project(self, project: ProjectValidator) -> Project:
        return Project(
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

    def is_unique(self, project: Project) -> bool:
        if Project.search_for_project(project) is not None:
            self.title.errors.append("Project already exists.")
            return False
        return True

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

        project = self.project_validator()

        try:
            ProjectValidator.model_validate(project)
        except ValueError as error:
            self.title.errors.append(f"{error}")
            return False

        valid_project = self.project(project)

        if not self.is_unique(valid_project):
            return False

        return True
