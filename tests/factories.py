# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from website.database import database
from website.events.models import Event, EventStatus


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = database.session


class EventFactory(BaseFactory):
    """Event factory."""

    class Meta:
        """Factory configuration."""

        model = Event

    id = Sequence(lambda n: n)
    status_id = EventStatus.return_status_id("scheduled")
    start_date = "2024-01-01"
    end_date = "2024-01-01"
    name = "Test Event"
    description = "Test Description"
