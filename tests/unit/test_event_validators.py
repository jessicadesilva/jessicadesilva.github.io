# -*- coding: utf-8 -*-
"""Unit tests for the `EventValidator`."""
from datetime import datetime

import pytest
from pydantic import ValidationError

from website.events.validator import EventValidator


class TestEventValidator:
    def test_event_validator_accepts_valid_data(self):
        event = EventValidator(
            status="scheduled",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 1),
            title="Test Event",
            description="Test Description",
        )
        assert isinstance(event, EventValidator)

    @pytest.mark.parametrize(
        "status, expected",
        [("scheduled", "scheduled"), ("completed", "completed")],
    )
    def test_status_field_validator(self, status, expected):
        assert EventValidator.status_must_be_scheduled_or_completed(status) == expected

    @pytest.mark.parametrize(
        "date, expected",
        [
            (datetime(2024, 1, 1).date(), datetime(2024, 1, 1).date()),
            ("2024-01-01", "2024-01-01"),
        ],
    )
    def test_dates_must_use_iso_format(self, date, expected):
        assert EventValidator.dates_must_use_iso_format(date) == expected

    def test_event_validator_raises_validation_error_with_invalid_data(self):
        with pytest.raises(ValidationError):
            EventValidator(
                status="not a valid option",
                start_date="01-01-2024",  # Invalid date format
                end_date="01-01-2024",  # Invalid date format
                title="Test Event",
                description="Test Description",
            )

    def test_status_must_be_scheduled_or_completed_raises_value_error(self):
        with pytest.raises(ValueError):
            EventValidator(
                status="invalid",
                start_date=datetime(2024, 1, 1),
                end_date=datetime(2024, 1, 1),
                title="Test Event",
                description="Test Description",
            )

    def test_dates_must_use_iso_format_raises_value_error(self):
        with pytest.raises(ValueError):
            EventValidator(
                status="scheduled",
                start_date="01-01-2024",  # Invalid date format
                end_date="01-01-2024",  # Invalid date format
                title="Test Event",
                description="Test Description",
            )
