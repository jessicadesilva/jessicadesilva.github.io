# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `error` pages."""
from http import HTTPStatus

import pytest


class TestErrorPageRoutes:
    def test_invalid_route_returns_404(self, testapp):
        response = testapp.get("/not/a/valid/route", expect_errors=True)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(reason="TODO: Figure out how to force a 500 error")
    def test_internal_server_error_returns_500(self, testapp):
        pass
