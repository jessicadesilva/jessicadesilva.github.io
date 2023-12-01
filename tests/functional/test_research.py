"""
Functional tests for the research blueprint routes.
"""
import pytest

from website.research.research import (
    project_pages,
    current_ugrad_project_names,
    former_ugrad_project_names,
    current_ugrad_abstract_names,
)


@pytest.mark.route
def test_get_page_current_ugrad_projects(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/undergrad/current.html").status_code == 200


@pytest.mark.route
def test_get_page_current_ugrad_projects_abstracts(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current/abstracts.html' page is requested (GET)
    THEN check the response is valid
    """
    assert (
        test_client.get("/research/undergrad/current/abstracts.html").status_code == 200
    )


@pytest.mark.route
def test_get_page_former_ugrad_projects(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/former.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/undergrad/former.html").status_code == 200


@pytest.mark.route
def test_get_page_other_research_projects(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/other.html' page is requested (GET)
    THEN check the response is valid
    """
    assert test_client.get("/research/other.html").status_code == 200


@pytest.mark.route
def test_get_page_project_name(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/projects/<project_name>.html' page is requested (GET)
    THEN check the response is valid
    """
    for project_name in project_pages:
        assert (
            test_client.get(f"/research/projects/{project_name}.html").status_code
            == 200
        )


@pytest.mark.route
def test_get_page_content_current_ugrad_projects(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current.html' page is requested (GET)
    THEN check the response contains the correct content
    """
    response = test_client.get("/research/undergrad/current.html")
    assert b"Current Undergraduate Projects" in response.data
    for project_name in current_ugrad_project_names:
        assert bytes(project_name, "utf-8") in response.data


@pytest.mark.route
def test_get_page_content_former_ugrad_projects(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/former.html' page is requested (GET)
    THEN check the response contains the correct content
    """
    response = test_client.get("/research/undergrad/former.html")
    assert b"Former Undergraduate Projects" in response.data
    for project_name in former_ugrad_project_names:
        assert bytes(project_name, "utf-8") in response.data


@pytest.mark.route
def test_get_page_content_current_ugrad_abstracts(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/research/undergraduate/current/abstracts.html' page is requested (GET)
    THEN check the response contains the correct content
    """
    response = test_client.get("/research/undergrad/current/abstracts.html")
    assert b"Current Undergraduate Abstracts" in response.data
    for project_name in current_ugrad_abstract_names:
        assert bytes(project_name, "utf-8") in response.data
