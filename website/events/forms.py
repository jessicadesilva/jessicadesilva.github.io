# -*- coding: utf-8 -*-
"""Event forms."""
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import InputRequired

from website.events.models import Event, EventStatus
from website.events.utils import determine_event_status
from website.events.validator import EventValidator
from website.utils import clean_input


class EventForm(FlaskForm):
    """Multi-purpose event form."""

    start_date = DateField("Start Date", validators=[InputRequired()])
    end_date = DateField("End Date", validators=[InputRequired()])
    title = CKEditorField("Event title", validators=[InputRequired()])
    description = CKEditorField("Event Description", validators=[InputRequired()])

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    def is_unique(self, event: Event) -> bool:
        return Event.search_for_event(event) is None

    def validate(self, **kwargs):
        initial_validation = super(EventForm, self).validate()

        if not initial_validation:
            return False

        if self.start_date.data > self.end_date.data:
            self.start_date.errors.append(
                "Start date must be before or equal to end date."
            )
            return False

        event = EventValidator(
            status=determine_event_status(self.end_date.data),
            start_date=self.start_date.data,
            end_date=self.end_date.data,
            title=clean_input(self.title.data),
            description=clean_input(self.description.data),
        )

        try:
            EventValidator.model_validate(event)
        except ValueError as error:
            self.title.errors.append(f"{error}")
            return False

        new_event = Event(
            status_id=EventStatus.get_id(event.status),
            start_date=event.start_date,
            end_date=event.end_date,
            title=event.title,
            description=event.description,
        )

        if Event.search_for_event(new_event) is not None:
            self.title.errors.append("Event already exists.")
            return False

        return True
