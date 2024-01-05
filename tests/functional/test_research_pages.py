# -*- coding: utf-8 -*-
"""Functional tests for Research Project related endpoints."""
from http import HTTPStatus

from flask import url_for

from website.research.routes import poster_pages


class TestResearchPageRoutes:
    def test_current_undergrad_projects_page_returns_200(self, testapp):
        response = testapp.get(url_for("research.current_undergrad_projects"))
        assert response.status_code == HTTPStatus.OK

    def test_current_undergrad_abstracts_page_returns_200(self, testapp):
        response = testapp.get(url_for("research.current_undergrad_abstracts"))
        assert response.status_code == HTTPStatus.OK

    def test_former_undergrad_projects_page_returns_200(self, testapp):
        response = testapp.get(url_for("research.former_undergrad_projects"))
        assert response.status_code == HTTPStatus.OK

    def test_other_projects_page_returns_200(self, testapp):
        response = testapp.get(url_for("research.other_projects"))
        assert response.status_code == HTTPStatus.OK

    def test_projects_pages_returns_200_with_valid_poster(self, testapp):
        for poster in poster_pages:
            response = testapp.get(url_for("research.project", poster=poster))
            assert response.status_code == HTTPStatus.OK

    def test_add_project_page_returns_200(self, testapp):
        response = testapp.get(url_for("research.add_project"))
        assert response.status_code == HTTPStatus.OK

    def test_edit_project_page_returns_200_with_valid_project_id(
        self, testapp, project
    ):
        response = testapp.get(url_for("research.edit_project", project_id=project.id))
        assert response.status_code == HTTPStatus.OK

    def test_delete_project_page_returns_200_with_valid_project_id(
        self, testapp, project
    ):
        response = testapp.get(
            url_for("research.delete_project", project_id=project.id)
        )
        assert response.status_code == HTTPStatus.OK

    def test_projects_page_returns_404_with_invalid_poster(self, testapp):
        response = testapp.get(
            url_for("research.project", poster="invalid"), expect_errors=True
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_edit_project_page_returns_404_with_invalid_project_id(self, testapp):
        response = testapp.get(
            url_for("research.edit_project", project_id=0), expect_errors=True
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_delete_project_page_returns_404_with_invalid_project_id(self, testapp):
        response = testapp.get(
            url_for("research.delete_project", project_id=0), expect_errors=True
        )
        assert response.status_code == HTTPStatus.NOT_FOUND
