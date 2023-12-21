# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `research` pages.

See: http://webtest.readthedocs.org/
"""
from http import HTTPStatus

from flask import url_for


class TestResearchPages:
    """Test 'research' pages return a success 200."""

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
