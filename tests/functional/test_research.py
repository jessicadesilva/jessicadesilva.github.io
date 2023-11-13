"""
Functional tests for the research blueprint routes.
"""

from website.research.research import project_names


def test_get_current_ugrad_projects_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/undergrad/current.html").status_code == 200


def test_get_current_ugrad_projects_abstracts_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current/abstracts.html' page is requested (GET)
    THEN check the response is valid
    """
    assert (
        test_client.get("/research/undergrad/current/abstracts.html").status_code == 200
    )


def test_get_former_ugrad_projects_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/former.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/undergrad/former.html").status_code == 200


def test_get_other_research_projects_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/other.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/other.html").status_code == 200


def test_get_project_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/projects/<project_name>.html' page is requested (GET)
    THEN check the response is valid
    """
    for project_name in project_names:
        assert (
            test_client.get(f"/research/projects/{project_name}.html").status_code
            == 200
        )
