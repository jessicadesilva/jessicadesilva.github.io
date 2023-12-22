# -*- coding: utf-8 -*-
"""Integration tests for the `events` blueprint."""
from http import HTTPStatus

from flask import url_for

from website.events.models import Event


class TestEventsPagesCRUDOperations:
    _data = {
        "start_date": "2024-01-01",
        "end_date": "2024-01-01",
        "name": "Test Event",
        "description": "Test Description",
    }

    def test_add_event_returns_201_event_name_and_added_to_database(self, testapp):
        old_event_count = len(Event.query.all())
        # Go to the Add Event page
        response = testapp.get(url_for("events.add_event"))
        # Fill out and submit the form
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Test Event successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        assert len(Event.query.all()) == old_event_count + 1

    def test_edit_event_returns_200_event_name_and_updates_database(
        self, testapp, event
    ):
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        # Fill out and submit the form
        form = response.forms["event_form"]
        form["start_date"] = "2024-01-10"
        form["end_date"] = "2024-01-10"
        form["name"] = "Edited Event"
        form["description"] = "Edited Description"
        response = form.submit()

        assert b"Edited Event successfully updated." in response.body
        assert response.status_code == HTTPStatus.OK
        assert event.name == "Edited Event"
        assert event.description == "Edited Description"

    def test_delete_event_returns_200_event_name_and_removed_from_database(
        self, testapp, event
    ):
        response = testapp.get(url_for("events.delete_event", event_id=event.id))
        form = response.forms["event_form"]
        response = form.submit().follow()

        assert b"Test Event successfully deleted." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == 0

    def test_recieve_error_when_adding_duplicate_event(self, testapp):
        old_event_count = len(Event.query.all())
        # Create and submit an event
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Test Event successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        # Check that the event was added to the database
        assert len(Event.query.all()) == old_event_count + 1

        # Duplicate and submit the event
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Event already exists." in response.body
        assert response.status_code == HTTPStatus.OK
        # Check that the event was not added to the database
        assert len(Event.query.all()) == old_event_count + 1
        assert len(Event.query.all()) < old_event_count + 2

    def test_receive_error_when_adding_event_with_invalid_end_date(self, testapp):
        self._data["end_date"] = "2023-01-01"
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Start date must be before or equal to end date." in response.body
        assert response.status_code == HTTPStatus.OK
        # Check that the event was not added to the database
        assert len(Event.query.all()) == 0

    def test_receive_error_when_adding_event_with_empty_fields(self, testapp):
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            value = ""
            form[key] = value
            response = form.submit()

            assert b"This field is required." in response.body
            assert response.status_code == HTTPStatus.OK
            assert len(Event.query.all()) == 0

    def test_recieve_error_when_updating_event_with_duplicate_event_data(
        self, testapp, event
    ):
        old_event_count = len(Event.query.all())
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["name"] = event.name
        form["description"] = event.description
        form["start_date"] = event.start_date
        form["end_date"] = event.end_date
        response = form.submit()

        assert b"Event already exists." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == old_event_count

    def test_recieve_error_when_updating_event_with_invalid_end_date(
        self, testapp, event
    ):
        old_event_count = len(Event.query.all())
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["start_date"] = "2024-01-10"
        form["end_date"] = "2023-01-10"
        response = form.submit()

        assert b"Start date must be before or equal to end date." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == old_event_count

    def test_receive_error_when_updating_event_with_with_empty_fields(
        self, testapp, event
    ):
        old_event_count = len(Event.query.all())
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = ""
            response = form.submit()

            assert b"This field is required." in response.body
            assert response.status_code == HTTPStatus.OK
            assert len(Event.query.all()) == old_event_count
