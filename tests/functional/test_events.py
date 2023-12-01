"""
Functional tests for the events blueprint routes.
"""
import pytest


@pytest.mark.route
def test_get_page_scheduled_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/scheduled.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/events/scheduled.html").status_code == 200
    assert b"Upcoming Events" in test_client.get("/events/scheduled.html").data


@pytest.mark.route
def test_get_page_past_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/past.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/events/past.html").status_code == 200
    assert b"Past Events" in test_client.get("/events/past.html").data


@pytest.mark.route
def test_get_page_add_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/add.html' page is requested (GET)
    THEN check the response is valid
    """
    # NOTE: This page is only interactive when the development server is running.
    assert test_client.get("/events/add.html").status_code == 200
    assert b"Add Event" in test_client.get("/events/add.html").data


@pytest.mark.route
def test_get_page_content_scheduled_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/scheduled.html' page is requested (GET)
    THEN check the response contains the expected content
    """
    assert b"Upcoming Events" in test_client.get("/events/scheduled.html").data
    assert b"Add Event" in test_client.get("/events/scheduled.html").data
    assert b"Past Events" in test_client.get("/events/scheduled.html").data


@pytest.mark.route
def test_get_page_content_past_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/past.html' page is requested (GET)
    THEN check the response contains the expected content
    """
    assert b"Past Events" in test_client.get("/events/past.html").data
    assert b"Upcoming Events" in test_client.get("/events/past.html").data
    assert b"<tr id=" in test_client.get("/events/past.html").data
    assert b"Date" in test_client.get("/events/past.html").data
    assert b"Name" in test_client.get("/events/past.html").data
    assert b"Description" in test_client.get("/events/past.html").data


@pytest.mark.route
def test_get_page_content_add_events(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/add.html' page is requested (GET)
    THEN check the response contains the expected content
    """
    # NOTE: This page is only interactive when the development server is running.
    assert b"Add Event" in test_client.get("/events/add.html").data
    assert b"Start Date" in test_client.get("/events/add.html").data
    assert b"End Date" in test_client.get("/events/add.html").data
    assert b"Event Name" in test_client.get("/events/add.html").data
    assert b"Event Description" in test_client.get("/events/add.html").data
