# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import os

import pytest
from webtest import TestApp

from website import create_app
from website import database as _database

from .factories import EventFactory


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app("tests.settings")
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """Create Webtest app."""
    return TestApp(app)


@pytest.fixture
def database(app):
    """Create database for the tests."""
    _database.app = app

    with app.app_context():
        _database.create_all()

    yield _database

    # Explicitly close database connection
    _database.session.close()
    _database.drop_all()


@pytest.fixture
def event(database):
    """Create event for the tests."""
    event = EventFactory()
    database.session.commit()
    return event
