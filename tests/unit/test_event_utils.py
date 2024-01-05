# -*- coding: utf-8 -*-
"""Unit tests for event utilities."""
from datetime import datetime, timedelta


from website.events.utils import determine_event_status, output_dict


TODAY = datetime.today().date()
TOMMOROW = TODAY + timedelta(days=1)
YESTERDAY = TODAY - timedelta(days=1)


class TestEventUtils:
    def test_determine_event_status_returns_completed_when_end_date_has_passed(
        self,
    ):
        assert determine_event_status(YESTERDAY) == "completed"
        assert determine_event_status(YESTERDAY.strftime("%Y-%m-%d")) == "completed"

    def test_determine_event_status_returns_scheduled_when_end_date_has_not_passed(
        self,
    ):
        assert determine_event_status(TODAY) == "scheduled"
        assert determine_event_status(TOMMOROW) == "scheduled"
        assert determine_event_status(TODAY.strftime("%Y-%m-%d")) == "scheduled"
        assert determine_event_status(TOMMOROW.strftime("%Y-%m-%d")) == "scheduled"

    def test_output_dict_returns_dict_with_correct_keys(self, event):
        assert output_dict(event).keys() == {"ID", "Date", "Title", "Description"}

    def test_output_dict_returns_correct_date_when_start_date_is_equal_to_end_date(
        self, event
    ):
        event.start_date = TODAY.strftime("%Y-%m-%d")
        event.end_date = TODAY.strftime("%Y-%m-%d")
        assert output_dict(event)["Date"] == TODAY.strftime("%m/%d/%Y")

    def test_output_dict_returns_correct_date_when_start_date_is_not_equal_to_end_date(
        self, event
    ):
        event.start_date = TODAY.strftime("%Y-%m-%d")
        event.end_date = TOMMOROW.strftime("%Y-%m-%d")
        assert output_dict(event)["Date"] == (
            TODAY.strftime("%m/%d/%Y") + " - " + TOMMOROW.strftime("%m/%d/%Y")
        )
