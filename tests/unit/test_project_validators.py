# -*- coding: utf-8 -*-
"""Unit tests for the reasearch `ProjectValidator`."""
import pytest
from pydantic import ValidationError

from website.research.validator import ProjectValidator


class TestProjectValidator:
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

    def setup_validator_with_all_fields(self, **kwargs):
        _validator = self.setup_validator_with_required_fields(**kwargs)
        type_id = _validator.type_id
        status_id = _validator.status_id
        students = _validator.students
        title = _validator.title
        description = _validator.description
        image = "default.jpg"
        advisors = "Test Advisor"
        majors = "Test Major"
        link = "https://www.csustan.edu/"

        if kwargs:
            image = kwargs.get("image")
            advisors = kwargs.get("advisors")
            majors = kwargs.get("majors")
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

    def test_project_validator_accepts_valid_data_with_required_fields(self):
        project = self.setup_validator_with_required_fields()
        assert isinstance(project, ProjectValidator)

    def test_project_validator_accepts_valid_data_with_all_fields(self):
        project = self.setup_validator_with_all_fields()
        assert isinstance(project, ProjectValidator)

    def test_id_must_be_greater_than_0_returns_id(self):
        assert ProjectValidator.id_must_be_greater_than_0(1) == 1

    def test_project_validator_raises_validation_error_with_invalid_id(
        self,
    ):
        test_fields = [
            {"type_id": 0},
            {"status_id": 0},
        ]

        for field in test_fields:
            with pytest.raises(ValidationError) as error:
                self.setup_validator_with_all_fields(**field)
            assert "ID must be greater than 0" in str(error.value)
