# -*- coding: utf-8 -*-
"""Unit tests for the `events` module."""
from datetime import datetime

import pytest
from pydantic import ValidationError

from website.events.models import Event, EventStatus
from website.events.validator import EventValidator
from tests.factories import EventFactory


class TestEventModel:
    def test_method_get_by_id_returns_event(self, event):
        assert Event.get_by_id(event.id) == event

    def test_method_get_by_id_returns_none(self):
        assert Event.get_by_id(0) is None


class TestEventValidator:
    def test_class_event_validator_accepts_valid_data(self):
        event = EventValidator(
            status="scheduled",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 1),
            name="Test Event",
            description="Test Description",
        )
        assert isinstance(event, EventValidator)

    def test_method_status_must_be_scheduled_or_completed_method_returns_status(self):
        assert (
            EventValidator.status_must_be_scheduled_or_completed("scheduled")
            == "scheduled"
        )
        assert (
            EventValidator.status_must_be_scheduled_or_completed("completed")
            == "completed"
        )

    def test_method_dates_must_use_iso_format_method_returns_date(self):
        assert (
            EventValidator.dates_must_use_iso_format(datetime(2024, 1, 1).date())
            == datetime(2024, 1, 1).date()
        )

    def test_class_event_validator_with_invalid_data_raises_validation_error(self):
        with pytest.raises(ValidationError):
            EventValidator(
                status="not an option",
                start_date="01-01-2024",
                end_date="01-01-2024",
                name="Test Event",
                description="Test Description",
            )

    def test_method_status_must_be_scheduled_or_completed_raises_value_error(self):
        with pytest.raises(ValueError):
            EventValidator(
                status="invalid",
                start_date=datetime(2024, 1, 1),
                end_date=datetime(2024, 1, 1),
                name="Test Event",
                description="Test Description",
            )

    def test_method_dates_must_use_iso_format_raises_value_error(self):
        with pytest.raises(ValueError):
            EventValidator(
                status="scheduled",
                start_date="01-01-2024",  # Invalid date format
                end_date="01-01-2024",  # Invalid date format
                name="Test Event",
                description="Test Description",
            )
