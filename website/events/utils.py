# -*- coding: utf-8 -*-
"""Event utilities."""
from datetime import datetime

from website.utils import format_display_date


def determine_event_status(end_date: datetime.date or str) -> str:
    if type(end_date) is str:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    if end_date < datetime.today().date():
        return "completed"
    else:
        return "scheduled"


def output_dict(event) -> dict:
    return {
        "ID": event.id,
        "Date": format_display_date(event.end_date)
        if event.start_date == event.end_date
        else format_display_date(event.start_date)
        + " - "
        + format_display_date(event.end_date),
        "Title": event.title,
        "Description": event.description,
    }
