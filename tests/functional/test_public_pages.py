# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `public` pages.

See: http://webtest.readthedocs.org/
"""
from http import HTTPStatus

from flask import url_for


class TestPublicPages:
    """Test 'public' pages return a success 200."""

    def test_home_page_returns_200(self, testapp):
        response = testapp.get(url_for("public.home"))
        assert response.status_code == HTTPStatus.OK

    def test_about_page_returns_200(self, testapp):
        response = testapp.get(url_for("public.about"))
        assert response.status_code == HTTPStatus.OK

    def test_cv_page_returns_200(self, testapp):
        response = testapp.get(url_for("public.cv"))
        assert response.status_code == HTTPStatus.OK

    def test_student_news_page_returns_200(self, testapp):
        response = testapp.get(url_for("public.student_news"))
        assert response.status_code == HTTPStatus.OK
