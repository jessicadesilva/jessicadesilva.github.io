"""
Functional tests for the general blueprint routes.
"""
import pytest


@pytest.mark.route
def test_get_page_home(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/index.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/index.html").status_code == 200


@pytest.mark.route
def test_get_page_about(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/about.html").status_code == 200


@pytest.mark.route
def test_get_page_cv(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/cv.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/about/cv.html").status_code == 200


@pytest.mark.route
def test_get_page_student_news(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/student_news.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/news.html").status_code == 200
