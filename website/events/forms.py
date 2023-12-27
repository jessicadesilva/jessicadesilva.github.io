# -*- coding: utf-8 -*-
"""Event forms."""
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import DateField
from wtforms.validators import DataRequired

from .models import Event, EventStatus
from .validator import EventValidator
from .utils import determine_event_status
from website.utils import clean_input


class EventForm(FlaskForm):
    """Multi-purpose event form."""

    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    name = CKEditorField("Event Name", validators=[DataRequired()])
    description = CKEditorField("Event Description", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

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
            name=clean_input(self.name.data),
            description=clean_input(self.description.data),
        )

        try:
            EventValidator.model_validate(event)
        except ValueError as error:
            self.name.errors.append(f"{error}")
            return False

        new_event = Event(
            status_id=EventStatus.return_status_id(event.status),
            start_date=event.start_date,
            end_date=event.end_date,
            name=event.name,
            description=event.description,
        )

        if Event.search_for_event(new_event) is not None:
            self.name.errors.append("Event already exists.")
            return False

        return True
