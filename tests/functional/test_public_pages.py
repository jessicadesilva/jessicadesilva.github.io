# -*- coding: utf-8 -*-
"""Functional tests for Public related endpoints."""
from http import HTTPStatus

from flask import url_for


class TestPublicPageRoutes:
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
