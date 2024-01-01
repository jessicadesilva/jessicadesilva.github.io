# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `mentor_groups` pages."""
from flask import url_for


class TestMentorGroupsPageRoutes:
    def test_mentor_groups_math_page_returns_200(self, testapp):
        response = testapp.get(url_for("mentor_groups.math"))
        assert response.status_code == 200

    def test_mentor_groups_stan_page_returns_200(self, testapp):
        response = testapp.get(url_for("mentor_groups.stan"))
        assert response.status_code == 200
