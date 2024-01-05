# -*- coding: utf-8 -*-
"""Integration tests for the `research` blueprint."""
from http import HTTPStatus

from flask import url_for

from website.research.models import Project

# ProjectType
PROJECT = 1
ABSTRACT = 2
# UndergradStatus
CURRENT = 1
FORMER = 2


class TestResearchPagesCRUDOperations:
    _data = {
        "type_id": PROJECT,
        "status_id": CURRENT,
        "image": "default.jpg",
        "advisors": "Test Advisor",
        "students": "Test Student",
        "majors": "Test Major",
        "title": "Test Project",
        "description": "Test Description",
        "link": "https://www.csustan.edu/",
    }

    def assertProjectCreated(self, response, count):
        assert b"Test Project successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        assert len(Project.query.all()) == count

    def assertDuplicateProjectError(self, response, count):
        assert b"Project already exists." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == count

    def assertRequiredFieldError(self, response, count):
        assert b"This field is required." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == count

    def test_add_project_returns_201_success_message_and_added_to_database(
        self, testapp
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Add Project' page
        # Fill out and submit the 'Add Project' form
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()
        # Check for a success message
        # Check that the project was added to the database
        self.assertProjectCreated(response, (PROJECT_COUNT + 1))

    def test_edit_project_returns_200_success_message_and_updated_in_database(
        self, testapp, project
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Edit Project' page
        # Fill out and submit the 'Edit Project' form
        response = testapp.get(url_for("research.edit_project", project_id=project.id))
        form = response.forms["project_form"]
        form["type_id"] = ABSTRACT
        form["status_id"] = FORMER
        form["image"] = "default.jpg"
        form["advisors"] = "Edited Advisor"
        form["students"] = "Edited Student"
        form["majors"] = "Edited Major"
        form["title"] = "Edited Project"
        form["description"] = "Edited Description"
        form["link"] = "https://www.csustan.edu/"
        response = form.submit()
        # Check for a success message
        # Check that a new project was not added to the database
        assert b"Edited Project successfully updated." in response.body
        assert response.status_code == HTTPStatus.OK
        assert project.title == "Edited Project"
        assert project.description == "Edited Description"
        assert len(Project.query.all()) == PROJECT_COUNT

    def test_delete_project_returns_200_success_message_and_removed_from_database(
        self, testapp, project
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Delete Project' page
        # Confirm deletion of the project
        response = testapp.get(
            url_for("research.delete_project", project_id=project.id)
        )
        form = response.forms["project_form"]
        response = form.submit().follow()
        # Check for a success message
        # Check that the project was removed from the database
        assert b"Test Title successfully deleted." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == PROJECT_COUNT - 1

    def test_receive_error_when_adding_duplicate_project(self, testapp):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Add Project' page
        # Fill out and submit the 'Add Project' form
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()
        # Check for a success message
        # Check that the project was added to the database
        self.assertProjectCreated(response, (PROJECT_COUNT + 1))
        # Duplicate and submit the project form
        response = form.submit()
        # Check for an error message
        # Check that the project was not added to the database
        self.assertDuplicateProjectError(response, (PROJECT_COUNT + 1))

    def test_recieve_error_when_adding_project_with_missing_required_fields(
        self, testapp
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Add Project' page
        # Fill out and submit the 'Add Project' form
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            value = "" if key in ["students", "title", "description"] else value
            form[key] = value
        response = form.submit()
        # Check for an error message
        # Check that the project was not added to the database
        self.assertRequiredFieldError(response, PROJECT_COUNT)

    def test_recieve_error_when_updating_project_with_duplicate_data(
        self, testapp, project
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Edit Project' page
        # Fill out and submit the 'Edit Project' form
        response = testapp.get(url_for("research.edit_project", project_id=project.id))
        form = response.forms["project_form"]
        for key in form.fields.keys():
            if key in ["csrf_token", "upload", "edit_project"]:
                continue
            form[key] = getattr(project, key)
        response = form.submit()
        # Check for an error message
        # Check that the project was not updated in the database
        self.assertDuplicateProjectError(response, PROJECT_COUNT)

    def test_recieve_error_when_updating_project_with_missing_required_fields(
        self, testapp, project
    ):
        PROJECT_COUNT = len(Project.query.all())
        # Navigate to the 'Edit Project' page
        # Fill out and submit the 'Edit Project' form
        response = testapp.get(url_for("research.edit_project", project_id=project.id))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            value = "" if key in ["students", "title", "description"] else value
            form[key] = value
        response = form.submit()
        # Check for an error message
        # Check that the project was not updated in the database
        self.assertRequiredFieldError(response, PROJECT_COUNT)
