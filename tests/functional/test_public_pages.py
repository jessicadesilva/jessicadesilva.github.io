# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `public` pages.

See: http://webtest.readthedocs.org/
"""
from flask import url_for


class TestPublicPages:
    """Public page tests."""

    def test_home_page_returns_200(self, testapp):
        """Home page should respond with a success 200."""
        response = testapp.get(url_for("public.home"))
        assert response.status_code == 200

    def test_about_page_returns_200(self, testapp):
        """About page should respond with a success 200."""
        response = testapp.get(url_for("public.about"))
        assert response.status_code == 200

    def test_cv_page_returns_200(self, testapp):
        """CV page should respond with a success 200."""
        response = testapp.get(url_for("public.cv"))
        assert response.status_code == 200

    def test_student_news_page_returns_200(self, testapp):
        """Student news page should respond with a success 200."""
        response = testapp.get(url_for("public.student_news"))
        assert response.status_code == 200
