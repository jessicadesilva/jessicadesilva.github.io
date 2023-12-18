# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `mentor_groups` pages.

See: http://webtest.readthedocs.org/
"""
from flask import url_for


class TestMentorGroupsPages:
    """Mentor Groups page tests."""

    def test_mentor_groups_math_page_returns_200(self, testapp):
        """Mentor Groups Math page should respond with a success 200."""
        response = testapp.get(url_for("mentor_groups.math"))
        assert response.status_code == 200

    def test_mentor_groupts_stan_page_returns_200(self, testapp):
        """Mentor Groups Stan page should respond with a success 200."""
        response = testapp.get(url_for("mentor_groups.stan"))
        assert response.status_code == 200
