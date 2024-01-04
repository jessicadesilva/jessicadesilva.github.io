# -*- coding: utf-8 -*-
"""Validator utilities."""
from pydantic import BaseModel, ConfigDict, field_validator


class ProjectValidator(BaseModel):
    model_config: ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        extra="forbid",
    )

    type_id: int
    status_id: int
    image: str = "default.jpg"
    students: str
    advisors: str = None
    majors: str = None
    title: str
    description: str
    link: str = None

    @field_validator("type_id", "status_id")
    @classmethod
    def id_must_be_greater_than_0(cls, id: int) -> int:
        if id <= 0:
            raise ValueError("ID must be greater than 0")
        return id
