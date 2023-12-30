# -*- coding: utf-8 -*-
"""Unit tests for the reasearch `ProjectValidator`."""
import pytest
from pydantic import ValidationError

from website.research.validator import ProjectValidator


class TestProjectValidator:
    def test_project_validator_accepts_valid_data_with_all_fields(self):
        project = ProjectValidator(
            type_id=1,
            status_id=1,
            image="default.jpg",
            advisors="Test Advisor",
            students="Test Student",
            majors="Test Major",
            title="Test Project",
            description="Test Description",
            link="https://www.csustan.edu/",
        )
        assert isinstance(project, ProjectValidator)

    def test_project_validator_accepts_valid_data_with_required_fields(self):
        project = ProjectValidator(
            type_id=1,
            status_id=1,
            students="Test Student",
            title="Test Project",
            description="Test Description",
        )
        assert isinstance(project, ProjectValidator)

    def test_type_id_must_be_greater_than_0_returns_type_id(self):
        assert ProjectValidator.type_id_must_be_greater_than_0(1) == 1

    def test_status_id_must_be_greater_than_0_returns_status_id(self):
        assert ProjectValidator.status_id_must_be_greater_than_0(1) == 1

    def setup_validator_with_all_fields(self, **kwargs):
        type_id = 1
        status_id = 1
        image = "default.jpg"
        advisors = "Test Advisor"
        students = "Test Student"
        majors = "Test Major"
        title = "Test Project"
        description = "Test Description"
        link = "https://www.csustan.edu/"

        if kwargs:
            type_id = kwargs.get("type_id")
            status_id = kwargs.get("status_id")
            image = kwargs.get("image")
            advisors = kwargs.get("advisors")
            students = kwargs.get("students")
            majors = kwargs.get("majors")
            title = kwargs.get("title")
            description = kwargs.get("description")
            link = kwargs.get("link")

        return ProjectValidator(
            type_id=type_id,
            status_id=status_id,
            image=image,
            advisors=advisors,
            students=students,
            majors=majors,
            title=title,
            description=description,
            link=link,
        )

    def setup_validator_with_required_fields(self, **kwargs):
        type_id = 1
        status_id = 1
        students = "Test Student"
        title = "Test Project"
        description = "Test Description"

        if kwargs:
            type_id = kwargs.get("type_id")
            status_id = kwargs.get("status_id")
            students = kwargs.get("students")
            title = kwargs.get("title")
            description = kwargs.get("description")

        return ProjectValidator(
            type_id=type_id,
            status_id=status_id,
            students=students,
            title=title,
            description=description,
        )

    def test_class_project_validator_raises_validation_error_with_invalid_type_id(
        self,
    ):
        with pytest.raises(ValidationError) as error:
            self.setup_validator_with_required_fields(type_id=0)
        assert "type_id must be greater than 0" in str(error.value)

    def test_class_project_validator_raises_validation_error_with_invalid_status_id(
        self,
    ):
        with pytest.raises(ValidationError) as error:
            self.setup_validator_with_required_fields(status_id=0)
        assert "status_id must be greater than 0" in str(error.value)
