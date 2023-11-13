"""
Functional tests for the general blueprint routes.
"""


def test_get_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/index.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/index.html").status_code == 200


def test_get_about_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/about.html").status_code == 200


def test_get_cv_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/cv.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/about/cv.html").status_code == 200


def test_get_student_news_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/student_news.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/news.html").status_code == 200
