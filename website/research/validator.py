# -*- coding: utf-8 -*-
"""Validator utilities."""
from pydantic import (
    BaseModel,
    ConfigDict,
    field_validator,
)


class ProjectValidator(BaseModel):
    """Project schema validator."""

    model_config: ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        extra="forbid",
    )

    type_id: int
    status_id: int
    image: str = "default.jpg"
    advisors: str = None
    students: str
    majors: str = None
    title: str
    description: str
    link: str = None

    @field_validator("type_id")
    @classmethod
    def type_id_must_be_greater_than_0(cls, id: int) -> int:
        """Validate `type_id`."""
        if id <= 0:
            raise ValueError("type_id must be greater than 0")
        return id

    @field_validator("status_id")
    @classmethod
    def status_id_must_be_greater_than_0(cls, id: int) -> int:
        """Validate `status_id`."""
        if id <= 0:
            raise ValueError("status_id must be greater than 0")
        return id

    @field_validator("link")
    @classmethod
    def link_must_contain_a_url(cls, link: str) -> str:
        """Validate `link`."""
        if link != "" and not link.startswith("http") or "href=" not in link:
            raise ValueError("link must contain a link")
        return link
