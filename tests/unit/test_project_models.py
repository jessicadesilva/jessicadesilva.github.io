# -*- coding: utf-8 -*-
"""Unit tests for the research `Project`, `ProjectType`, and `UndergradStatus` models."""
import pytest

from tests.factories import ProjectFactory
from website.research.models import Project, ProjectType, UndergradStatus


@pytest.mark.usefixtures("database")
class TestProjectType:
    def test_get_id_returns_id(self):
        type = ProjectType(type="Testing")
        type.save()
        assert ProjectType.get_id("Testing") == type.id

    def test_get_by_id_returns_type(self):
        type = ProjectType(type="Testing")
        type.save()
        assert ProjectType.get_by_id(type.id) == type

    def test_get_id_returns_none_if_no_type(self):
        assert ProjectType.get_id("not a type") is None

    def test_get_id_returns_none_if_invalid_type(self):
        assert ProjectType.get_id(0) is None

    def test_type_must_be_unique(self):
        type = ProjectType(type="Testing")
        type.save()
        with pytest.raises(Exception):
            ProjectType(type="Testing").save()


@pytest.mark.usefixtures("database")
class TestUndergradStatus:
    def test_get_id_returns_id(self):
        status = UndergradStatus(status="Testing")
        status.save()
        assert UndergradStatus.get_id("Testing") == status.id

    def test_get_by_id_returns_status(self):
        status = UndergradStatus(status="Testing")
        status.save()
        assert UndergradStatus.get_by_id(status.id) == status

    def test_get_id_returns_none_if_no_status(self):
        assert UndergradStatus.get_id("not a status") is None

    def test_get_id_returns_none_if_invalid_status(self):
        assert UndergradStatus.get_id(0) is None

    def test_status_must_be_unique(self):
        status = UndergradStatus(status="Testing")
        status.save()
        with pytest.raises(Exception):
            UndergradStatus(status="Testing").save()


@pytest.mark.usefixtures("database")
class TestProjectModel:
    def test_get_by_id_returns_project(self):
        project = Project(
            type_id=ProjectType.get_id("project"),
            status_id=UndergradStatus.get_id("current"),
            image="test.png",
            students="Test Student",
            title="Test Project",
            description="Test Description",
        )
        project.save()
        retrieved = Project.get_by_id(project.id)
        assert retrieved == project

    def test_get_by_id_returns_none_if_no_project(self):
        assert Project.get_by_id(0) is None

    def test_get_by_id_returns_none_if_invalid_id(self):
        assert Project.get_by_id("not an id") is None

    def test_factory(self):
        project = ProjectFactory()
        assert project.id is not None
        assert isinstance(project, Project)

    def test_search_for_project_returns_project(self):
        project = ProjectFactory()
        assert Project.search_for_project(project) == project
