"""
Functional tests for the events blueprint routes.
"""


def test_get_upcoming_events_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/upcoming.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/events/upcoming.html").status_code == 200


def test_get_past_events_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/events/past.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/events/past.html").status_code == 200
