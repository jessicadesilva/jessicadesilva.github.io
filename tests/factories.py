# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from website.extensions import database
from website.events.models import Event, EventStatus
from website.research.models import Project, ProjectType, UndergradStatus


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = database.session


class EventFactory(BaseFactory):
    class Meta:
        model = Event

    id = Sequence(lambda n: n)
    status_id = EventStatus.return_status_id("scheduled")
    start_date = "2024-01-01"
    end_date = "2024-01-01"
    name = "Test Event"
    description = "Test Description"


class ProjectFactory(BaseFactory):
    class Meta:
        model = Project

    id = Sequence(lambda n: n)
    type_id = ProjectType.return_type_id("project")
    status_id = UndergradStatus.return_status_id("current")
    image = "default.jpg"
    advisors = "Test Advisor"
    students = "Test Student"
    majors = "Test Major"
    title = "Test Title"
    description = "Test Description"
    link = "https://www.google.com"
