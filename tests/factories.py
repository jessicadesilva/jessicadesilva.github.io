# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from website.events.models import Event
from website.extensions import database
from website.research.models import Project


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = database.session


class EventFactory(BaseFactory):
    class Meta:
        model = Event

    id = Sequence(lambda n: n)
    status_id = 1
    start_date = "2024-01-01"
    end_date = "2024-01-01"
    title = "Test Event"
    description = "Test Description"


class ProjectFactory(BaseFactory):
    class Meta:
        model = Project

    id = Sequence(lambda n: n)
    type_id = 1
    status_id = 1
    image = "default.jpg"
    advisors = "Test Advisor"
    students = "Test Student"
    majors = "Test Major"
    title = "Test Title"
    description = "Test Description"
    link = "https://www.csustan.edu/"
