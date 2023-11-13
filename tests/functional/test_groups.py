def test_get_mentor_groups_math_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/mentor-groups/math.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/mentor-groups/math.html").status_code == 200


def test_get_mentor_groups_stan_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/mentor-groups/stan.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/mentor-groups/stan.html").status_code == 200
