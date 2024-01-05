# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import pytest
from webtest import TestApp

from tests.factories import EventFactory, ProjectFactory
from website import create_app
from website import database as _database


@pytest.fixture
def app():
    _app = create_app("tests.settings")
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    return TestApp(app)


@pytest.fixture
def database(app):
    _database.app = app

    with app.app_context():
        _database.create_all()

    yield _database

    # Explicitly close database connection
    _database.session.close()
    _database.drop_all()


@pytest.fixture
def event(database):
    event = EventFactory()
    database.session.commit()
    return event


@pytest.fixture
def project(database):
    project = ProjectFactory()
    database.session.commit()
    return project
