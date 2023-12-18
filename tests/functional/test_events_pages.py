# -*- coding: utf-8 -*-
"""Functional tests using WebTest for `events` pages."""
from flask import url_for

from website.events.models import Event


class TestEventsPages:
    """Events page tests."""

    _data = {
        "start_date": "2024-01-01",
        "end_date": "2024-01-01",
        "name": "Test Event",
        "description": "Test Description",
    }

    def test_future_events_page_returns_200(self, testapp):
        """Future events page should respond with a success 200."""
        response = testapp.get(url_for("events.future_events"))
        assert response.status_code == 200

    def test_past_events_page_returns_200(self, testapp):
        """Past events page should respond with a success 200."""
        response = testapp.get(url_for("events.past_events"))
        assert response.status_code == 200

    def test_add_event_page_returns_200(self, testapp):
        """Add event page should respond with a success 200."""
        response = testapp.get(url_for("events.add_event"))
        assert response.status_code == 200

    def test_can_create_event_successfully(self, testapp):
        """Add event page should display a success message when adding an event."""
        old_event_count = len(Event.query.all())
        # Go to the Add Event page
        response = testapp.get(url_for("events.add_event"))
        # Fill out and submit the form
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit().follow()

        assert b"Test Event" in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == old_event_count + 1

    def test_recieve_error_when_adding_duplicate_event(self, testapp):
        """Add event page should display an error when trying to add a duplicate event."""
        old_event_count = len(Event.query.all())
        # Create and submit an event
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit().follow()

        # Check that the event was added to the database
        assert len(Event.query.all()) == old_event_count + 1

        # Duplicate and submit the event
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Event already exists." in response.body
        assert response.status_code == 200
        # Check that the event was not added to the database
        assert len(Event.query.all()) == old_event_count + 1

    def test_receive_error_when_adding_event_with_end_date_before_start_date(
        self, testapp
    ):
        """Add event page should display an error when adding an event with an end date before the start date."""
        self._data["end_date"] = "2023-01-01"
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"Start date must be before or equal to end date." in response.body
        assert response.status_code == 200
        # Check that the event was not added to the database
        assert len(Event.query.all()) == 0

    def test_receive_error_when_adding_event_with_no_start_date(self, testapp):
        """Add event page should display an error when adding an event with no start date."""
        self._data["start_date"] = ""
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == 0

    def test_receive_error_when_adding_event_with_no_end_date(self, testapp):
        """Add event page should display an error when adding an event with no end date."""
        self._data["end_date"] = ""
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == 0

    def test_receive_error_when_adding_event_with_no_name(self, testapp):
        """Add event page should display an error when adding an event with no name."""
        self._data["name"] = ""
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == 0

    def test_receive_error_when_adding_event_with_no_description(self, testapp):
        """Add event page should display an error when adding an event with no description."""
        self._data["description"] = ""
        response = testapp.get(url_for("events.add_event"))
        form = response.forms["event_form"]
        for key, value in self._data.items():
            form[key] = value
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == 0

    def test_edit_event_page_returns_200(self, testapp, event):
        """Edit event page should respond with a success 200."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        assert response.status_code == 200

    def test_edit_event_page_returns_404(self, testapp):
        """Edit event page should respond with a success 404."""
        response = testapp.get(
            url_for("events.edit_event", event_id=0), expect_errors=True
        )
        assert response.status_code == 404

    def test_can_edit_all_event_fields_successfully(self, testapp, event):
        """Edit event page should display a success message when editing an event."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        # Fill out and submit the form
        form = response.forms["event_form"]
        form["start_date"] = "2024-01-10"
        form["end_date"] = "2024-01-10"
        form["name"] = "Edited Event"
        form["description"] = "Edited Description"
        response = form.submit().follow()

        assert b"Edited Event" in response.body
        assert response.status_code == 200

    def test_recieve_error_when_editing_event_with_duplicate_event_data(
        self, testapp, event
    ):
        """Edit event page should display an error when editing an event with a duplicate event data."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["name"] = event.name
        form["description"] = event.description
        form["start_date"] = event.start_date
        form["end_date"] = event.end_date
        response = form.submit()

        assert b"Event already exists." in response.body
        assert response.status_code == 200

    def test_recieve_error_when_editing_event_with_end_date_before_start_date(
        self, testapp, event
    ):
        """Edit event page should display an error when editing an event with an end date before the start date."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["start_date"] = "2024-01-10"
        form["end_date"] = "2023-01-10"
        response = form.submit()

        assert b"Start date must be before or equal to end date." in response.body
        assert response.status_code == 200

    def test_receive_error_when_editing_event_with_no_start_date(self, testapp, event):
        """Edit event page should display an error when editing an event with no start date."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["start_date"] = ""
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200

    def test_receive_error_when_editing_event_with_no_end_date(self, testapp, event):
        """Edit event page should display an error when editing an event with no end date."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["end_date"] = ""
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200

    def test_receive_error_when_editing_event_with_no_name(self, testapp, event):
        """Edit event page should display an error when editing an event with no name."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["name"] = ""
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200

    def test_receive_error_when_editing_event_with_no_description(self, testapp, event):
        """Edit event page should display an error when editing an event with no description."""
        response = testapp.get(url_for("events.edit_event", event_id=event.id))
        form = response.forms["event_form"]
        form["description"] = ""
        response = form.submit()

        assert b"This field is required." in response.body
        assert response.status_code == 200

    def test_delete_event_page_returns_200(self, testapp, event):
        """Delete event page should respond with a success 200."""
        response = testapp.get(url_for("events.delete_event", event_id=event.id))
        assert response.status_code == 200

    def test_delete_event_page_returns_404(self, testapp):
        """Delete event page should respond with a success 404."""
        response = testapp.get(
            url_for("events.delete_event", event_id=0), expect_errors=True
        )
        assert response.status_code == 404

    def test_can_delete_event_successfully(self, testapp, event):
        """Delete event page should display a success message when deleting an event."""
        response = testapp.get(url_for("events.delete_event", event_id=event.id))
        form = response.forms["event_form"]
        response = form.submit().follow()

        assert b"successfully deleted." in response.body
        assert response.status_code == 200
        assert len(Event.query.all()) == 0
