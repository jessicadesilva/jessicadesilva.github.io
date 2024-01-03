# -*- coding: utf-8 -*-
"""Integration tests for the `events` blueprint."""
from datetime import datetime, timedelta
from http import HTTPStatus

from flask import url_for

from website.events.models import Event

TODAY = datetime.today().date()
TOMMOROW = TODAY + timedelta(days=1)
YESTERDAY = TODAY - timedelta(days=1)


class TestEventsPagesCRUDOperations:
    _data = {
        "start_date": TODAY,
        "end_date": TOMMOROW,
        "title": "Test Event",
        "description": "Test Description",
    }

    def assertEventCreated(self, response, count):
        assert b"Test Event successfully added." in response.body
        assert response.status_code == HTTPStatus.CREATED
        assert len(Event.query.all()) == count

    def assertDuplicateEventError(self, response, count):
        assert b"Event already exists." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == count

    def assertInvalidDateError(self, response, count):
        assert b"Start Date must be before or equal to End Date." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == count

    def assertRequiredFieldError(self, response, count):
        assert b"This field is required." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == count

    def test_add_event_returns_201_success_message_and_added_to_database(self, testapp):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Add Event' page
        # Fill out and submit the 'Add Event' form
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()
        # Check for a success message
        # Check that the event was added to the database
        self.assertEventCreated(response, (EVENT_COUNT + 1))

    def test_edit_event_returns_200_success_message_and_updates_database(
        self, testapp, event
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Edit Event' page
        # Fill out and submit the 'Edit Event' form
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["start_date"] = YESTERDAY
        form["end_date"] = TODAY
        form["title"] = "Edited Event"
        form["description"] = "Edited Description"
        response = form.submit()
        # Check for a success message
        # Check that a new event was not added to the database
        assert b"Edited Event successfully updated." in response.body
        assert response.status_code == HTTPStatus.OK
        assert event.title == "Edited Event"
        assert event.description == "Edited Description"
        assert len(Event.query.all()) == EVENT_COUNT

    def test_delete_event_returns_200_success_message_and_removed_from_database(
        self, testapp, event
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Delete Event' page
        # Comfirm deletion of the event
        response = testapp.get(url_for("events.delete_event", event_id=event.id))
        form = response.forms["event_form"]
        response = form.submit().follow()
        # Check for a success message
        # Check that the event was removed from the database
        assert b"Test Event successfully deleted." in response.body
        assert response.status_code == HTTPStatus.OK
        assert len(Event.query.all()) == EVENT_COUNT - 1

    def test_recieve_error_when_adding_duplicate_event(self, testapp):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Add Event' page
        # Fill out and submit the 'Add Event' form
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()
        # Check for a success message
        # Check that the event was added to the database
        self.assertEventCreated(response, (EVENT_COUNT + 1))
        # Duplicate and submit the event form
        response = form.submit()
        # Check for an error message
        # Check that the event was not added to the database
        self.assertDuplicateEventError(response, (EVENT_COUNT + 1))

    def test_receive_error_when_adding_event_with_end_date_before_start_date(
        self, testapp
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Add Event' page
        # Fill out and submit the 'Add Event' form
        self._data["start_date"] = TOMMOROW
        self._data["end_date"] = YESTERDAY
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()
        # Check for an error message
        # Check that the event was not added to the database
        self.assertInvalidDateError(response, EVENT_COUNT)

    def test_receive_error_when_adding_event_with_missing_required_fields(
        self, testapp
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Add Event' page
        # Fill out and submit the 'Add Event' form
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            value = ""
            form[key] = value
            response = form.submit()
            # Check for an error message
            # Check that the event was not added to the database
            self.assertRequiredFieldError(response, EVENT_COUNT)

    def test_recieve_error_when_updating_event_with_duplicate_event_data(
        self, testapp, event
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Edit Event' page
        # Fill out and submit the 'Edit Event' form
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["title"] = event.title
        form["description"] = event.description
        form["start_date"] = event.start_date
        form["end_date"] = event.end_date
        response = form.submit()
        # Check for an error message
        # Check that the event was not added to the database
        self.assertDuplicateEventError(response, EVENT_COUNT)

    def test_recieve_error_when_updating_event_with_end_date_before_start_date(
        self, testapp, event
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Edit Event' page
        # Fill out and submit the 'Edit Event' form
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["start_date"] = TOMMOROW
        form["end_date"] = YESTERDAY
        response = form.submit()
        # Check for an error message
        # Check that the event was not added to the database
        self.assertInvalidDateError(response, EVENT_COUNT)

    def test_receive_error_when_updating_event_with_with_missing_required_fields(
        self, testapp, event
    ):
        EVENT_COUNT = len(Event.query.all())
        # Navigate to the 'Edit Event' page
        # Fill out and submit the 'Edit Event' form
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = ""
            response = form.submit()
            # Check for an error message
            # Check that the event was not added to the database
            self.assertRequiredFieldError(response, EVENT_COUNT)
