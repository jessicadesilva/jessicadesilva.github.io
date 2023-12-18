# -*- coding: utf-8 -*-
"""Event utilities."""
from datetime import datetime


def determine_event_status(end_date: datetime.date or str) -> str:
    """Determine the status of an event."""

    if type(end_date) == str:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    if end_date < datetime.today().date():
        return "completed"
    else:
        return "scheduled"
