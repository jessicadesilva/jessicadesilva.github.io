# -*- coding: utf-8 -*-
"""Functional tests for Event related endpoints."""
from http import HTTPStatus

from flask import url_for


class TestEventsPageRoutes:
    def test_future_events_page_returns_200(self, testapp):
        response = testapp.get(url_for("events.future_events"))
        assert response.status_code == HTTPStatus.OK

    def test_past_events_page_returns_200(self, testapp):
        response = testapp.get(url_for("events.past_events"))
        assert response.status_code == HTTPStatus.OK

    def test_add_event_page_returns_200(self, testapp):
        response = testapp.get(url_for("events.add_event"))
        assert response.status_code == HTTPStatus.OK

    def test_edit_event_page_returns_200_with_valid_event_id(self, testapp, event):
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        assert response.status_code == HTTPStatus.OK

    def test_delete_event_page_returns_200_with_valid_event_id(self, testapp, event):
        response = testapp.get(url_for("events.delete_event", event_id=event.id))
        assert response.status_code == HTTPStatus.OK

    def test_edit_event_page_returns_404_with_invalid_event_id(self, testapp):
        response = testapp.get(
            url_for("events.edit_event", event_id=0), expect_errors=True
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_delete_event_page_returns_404_with_invalid_event_id(self, testapp):
        response = testapp.get(
            url_for("events.delete_event", event_id=0), expect_errors=True
        )
        assert response.status_code == HTTPStatus.NOT_FOUND
