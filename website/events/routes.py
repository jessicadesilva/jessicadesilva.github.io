# -*- coding: utf-8 -*-
"""Events module, including scheduled and past events."""
from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from website.events.forms import EventForm
from website.events.models import Event, EventStatus
from website.events.utils import determine_event_status, format_output_data
from website.extensions import database
from website.utils import clean_input, dev_utils

blueprint = Blueprint(
    "events", __name__, url_prefix="/events", static_folder="../static"
)


@blueprint.route("/future.html")
@dev_utils
def future_events(**kwargs):
    data = []

    for event in database.session.execute(database.select(Event)).scalars().all():
        # Update the status of the event if it has changed
        # This is necessary because the status of an event is determined by its end date
        if determine_event_status(event.end_date) == "completed":
            event.update(commit=True, status_id=EventStatus.get_id("completed"))

        if event.status_rel.status == "scheduled":
            data.append(format_output_data(event))

    return (
        render_template("events/future_events.j2", data=data, **kwargs),
        HTTPStatus.OK,
    )


@blueprint.route("/past.html")
@dev_utils
def past_events(**kwargs):
    data = []

    for event in database.session.execute(database.select(Event)).scalars().all():
        # Update the status of the event if it has changed
        # This is necessary because the status of an event is determined by its end date
        if determine_event_status(event.end_date) == "completed":
            event.update(commit=True, status_id=EventStatus.get_id("completed"))

        if event.status_rel.status == "completed":
            data.append(format_output_data(event))

    return (
        render_template("events/past_events.j2", data=data, **kwargs),
        HTTPStatus.OK,
    )


@blueprint.route("/add_event.html", methods=["GET", "POST"])
def add_event():
    form = EventForm()

    if request.method == "POST":
        if form.validate_on_submit():
            Event.create(
                status_id=EventStatus.get_id(
                    determine_event_status(form.end_date.data)
                ),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                title=clean_input(form.title.data),
                description=clean_input(form.description.data),
            )
            flash(f"{clean_input(form.title.data)} successfully added.", "success")
            return (
                render_template("events/add_event.j2", form=form),
                HTTPStatus.CREATED,
            )

    return render_template("events/add_event.j2", form=form), HTTPStatus.OK


@blueprint.route("/edit_event/<int:event_id>.html", methods=["GET", "POST"])
def edit_event(event_id: int):
    form = EventForm()
    event = Event.get_by_id(event_id)

    if not event:
        flash(f"Event with ID {event_id} does not exist.", "error")
        abort(HTTPStatus.NOT_FOUND)

    if request.method == "POST":
        if form.validate_on_submit():
            event.update(
                commit=True,
                id=event_id,
                status_id=EventStatus.get_id(
                    determine_event_status(form.end_date.data)
                ),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                title=clean_input(form.title.data),
                description=clean_input(form.description.data),
            )
            flash(
                f"{clean_input(form.title.data)} successfully updated.",
                "success",
            )
            return (
                render_template("events/edit_event.j2", event=event, form=form),
                HTTPStatus.OK,
            )

    form.start_date.data = datetime.strptime(event.start_date, "%Y-%m-%d").date()
    form.end_date.data = datetime.strptime(event.end_date, "%Y-%m-%d").date()
    form.title.data = event.title
    form.description.data = event.description

    return (
        render_template("events/edit_event.j2", event=event, form=form),
        HTTPStatus.OK,
    )


@blueprint.route("/delete_event/<int:event_id>.html", methods=["GET", "POST"])
def delete_event(event_id: int):
    event = Event.get_by_id(event_id)

    if not event:
        flash(f"Event with ID {event_id} does not exist.", "error")
        abort(HTTPStatus.NOT_FOUND)

    if request.method == "POST":
        event.delete()
        flash(f"{event.title} successfully deleted.", "success")
        return redirect(url_for("events.future_events"))

    form = EventForm()
    flash(f"Are you sure you want to delete {event.title}?", "warning")

    return (
        render_template("events/delete_event.j2", event=event, form=form),
        HTTPStatus.OK,
    )
