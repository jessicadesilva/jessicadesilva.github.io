# -*- coding: utf-8 -*-
"""Validator utilities."""
import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    field_validator,
)


class EventValidator(BaseModel):
    model_config: ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        extra="forbid",
    )

    status: str
    start_date: datetime.date
    end_date: datetime.date
    name: str
    description: str

    @field_validator("status")
    @classmethod
    def status_must_be_scheduled_or_completed(cls, status: str) -> str:
        if status not in ("scheduled", "completed"):
            raise ValueError(
                "Invalid status. Status must be either 'scheduled' or 'completed'."
            )
        return status

    @field_validator("start_date", "end_date")
    @classmethod
    def dates_must_use_iso_format(cls, date: datetime.date) -> datetime.date:
        try:
            datetime.date.fromisoformat(str(date))
        except ValueError:
            raise ValueError(
                "Invalid date format. Date must be in the format 'YYYY-MM-DD'."
            )
        return date
