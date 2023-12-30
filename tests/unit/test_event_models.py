# -*- coding: utf-8 -*-
"""Unit tests for the `Event` and `EventStatus` models."""
from datetime import datetime

import pytest

from tests.factories import EventFactory
from website.events.models import Event, EventStatus


@pytest.mark.usefixtures("database")
class TestEventStatus:
    def test_get_id_returns_id(self):
        status = EventStatus(status="Testing")
        status.save()
        assert EventStatus.get_id("Testing") == status.id

    def test_get_by_id_returns_status(self):
        status = EventStatus(status="Testing")
        status.save()
        assert EventStatus.get_by_id(status.id) == status

    def test_get_id_returns_none_if_no_status(self):
        assert EventStatus.get_id("not a status") is None

    def test_get_id_returns_none_if_invalid_status(self):
        assert EventStatus.get_id(0) is None

    def test_status_must_be_unique(self):
        status = EventStatus(status="Testing")
        status.save()
        with pytest.raises(Exception):
            EventStatus(status="Testing").save()


@pytest.mark.usefixtures("database")
class TestEvent:
    def test_get_by_id_returns_event(self):
        event = Event(
            status_id=EventStatus.get_id("scheduled"),
            title="Test Event",
            description="Test Description",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 1),
        )
        event.save()
        retrieved = Event.get_by_id(event.id)
        assert retrieved == event

    def test_get_by_id_returns_none_if_no_event(self):
        assert Event.get_by_id(0) is None

    def test_get_by_id_returns_none_if_invalid_id(self):
        assert Event.get_by_id("not an id") is None

    def test_factory(self):
        event = EventFactory()
        assert event.id is not None
        assert isinstance(event, Event)

    def test_search_for_event_returns_event(self):
        event = EventFactory()
        assert Event.search_for_event(event) == event
