# -*- coding: utf-8 -*-
"""Integration tests for the `research` blueprint."""
from http import HTTPStatus

from flask import url_for

from website.research.models import Project


class TestResearchPagesCRUDOperations:
    _data = {
        "type_id": 1,  # 1 = "project", 2 = "abstract"
        "status_id": 1,  # 1 = "current", 2 = "former"
        "image": "default.jpg",
        "advisors": "Test Advisor",
        "students": "Test Student",
        "majors": "Test Major",
        "title": "Test Project",
        "description": "Test Description",
        "link": "https://www.csustan.edu/",
    }

    def test_add_project_returns_201_project_title_and_added_to_database(self, testapp):
        old_project_count = len(Project.query.all())
        # Go to the Add Project page
        response = testapp.get(url_for("research.add_project"))
        # Fill out and submit the form
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Test Project successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        assert len(Project.query.all()) == old_project_count + 1

    def test_edit_project_returns_200_project_title_and_updates_database(
        self, testapp, project
    ):
        response = testapp.get(url_for("research.edit_project", project_id=project.id))
        # Fill out and submit the form
        form = response.forms["project_form"]
        form["type_id"] = 2
        form["status_id"] = 2
        form["image"] = "default.jpg"
        form["advisors"] = "Edited Advisor"
        form["students"] = "Edited Student"
        form["majors"] = "Edited Major"
        form["title"] = "Edited Project"
        form["description"] = "Edited Description"
        form["link"] = "https://www.csustan.edu/"
        response = form.submit()

        assert b"Edited Project successfully updated." in response.body
        assert response.status_code == HTTPStatus.OK
        assert project.title == "Edited Project"
        assert project.description == "Edited Description"

    def test_delete_project_returns_200_project_title_and_removed_from_database(
        self, testapp, project
    ):
        response = testapp.get(
            url_for("research.delete_project", project_id=project.id)
        )
        form = response.forms["project_form"]
        response = form.submit().follow()

        assert b"Test Title successfully deleted." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == 0

    def test_receive_error_when_adding_duplicate_project(self, testapp):
        old_project_count = len(Project.query.all())
        # Create and submit a project
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Test Project successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        assert len(Project.query.all()) == old_project_count + 1
        # Create and submit a duplicate project
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Project already exists." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == old_project_count + 1

    def test_recieve_error_when_adding_project_with_empty_required_text_fields(
        self, testapp
    ):
        old_project_count = len(Project.query.all())
        # Create and submit a project
        response = testapp.get(url_for("research.add_project"))
        form = response.forms["project_form"]
        for key, value in self._data.items():
            form[key] = value
        # Set required fields to empty strings
        form["students"] = ""
        form["title"] = ""
        form["description"] = ""
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Project.query.all()) == old_project_count
