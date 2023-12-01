"""
Functional tests for the groups blueprint routes.
"""
import pytest


@pytest.mark.route
def test_get_page_mentor_groups_math(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/mentor-groups/math.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/mentor-groups/math.html").status_code == 200


@pytest.mark.route
def test_get_page_mentor_groups_stan(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/mentor-groups/stan.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/mentor-groups/stan.html").status_code == 200
