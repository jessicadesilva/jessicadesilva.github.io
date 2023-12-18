# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `error` pages."""
import pytest


class TestErrorPages:
    """Error page tests."""

    def test_404_page(self, testapp):
        """404 page should respond with a success 404."""
        response = testapp.get("/not/a/valid/route", expect_errors=True)
        assert response.status_code == 404

    @pytest.mark.skip(reason="TODO: Figure out how to force a 500 error")
    def test_500_page(self, testapp):
        """500 page should respond with a success 500."""
        # TODO: Figure out how to force a 500 error
        pass
