# -*- coding: utf-8 -*-
"""Events module, including scheduled and past events."""
from datetime import datetime

from flask import (
    Blueprint,
    abort,
    flash,
    render_template,
    request,
    redirect,
    url_for,
)

from website.extensions import database
from website.utils import clean_input, formatted_date, dev_utils
from website.events.forms import EventForm
from website.events.models import Event, EventStatus
from website.events.utils import determine_event_status


blueprint = Blueprint(
    "events", __name__, url_prefix="/events", static_folder="../static"
)


@blueprint.route("/future.html")
@dev_utils
def future_events(*args, **kwargs):
    """Display future events."""

    data = []

    for event in database.session.execute(database.select(Event)).scalars().all():
        # Update the status of the event if it has changed
        # This is necessary because the status of an event is determined by its end date
        if determine_event_status(event.end_date) == "completed":
            event.update(
                commit=True, status_id=EventStatus.return_status_id("completed")
            )

        if event.event_status_rel.status == "scheduled":
            output_data = {
                "ID": event.id,
                "Date": formatted_date(event.end_date)
                if event.start_date == event.end_date
                else formatted_date(event.start_date)
                + " - "
                + formatted_date(event.end_date),
                "Name": event.name,
                "Description": event.description,
            }
            data.append(output_data)

    return render_template("events/future_events.j2", data=data, *args, **kwargs)


@blueprint.route("/past.html")
@dev_utils
def past_events(*args, **kwargs):
    """Display past events."""

    data = []

    for event in database.session.execute(database.select(Event)).scalars().all():
        # Update the status of the event if it has changed
        # This is necessary because the status of an event is determined by its end date
        if determine_event_status(event.end_date) == "completed":
            event.update(
                commit=True, status_id=EventStatus.return_status_id("completed")
            )

        if event.event_status_rel.status == "completed":
            output_data = {
                "ID": event.id,
                "Date": formatted_date(event.end_date)
                if event.start_date == event.end_date
                else formatted_date(event.start_date)
                + " - "
                + formatted_date(event.end_date),
                "Name": event.name,
                "Description": event.description,
            }
            data.append(output_data)

    return render_template("events/past_events.j2", data=data, *args, **kwargs)


@blueprint.route("/add_event.html", methods=["GET", "POST"])
def add_event():
    """Add an event."""

    form = EventForm()

    if request.method == "POST":
        if form.validate_on_submit():
            Event.create(
                status_id=EventStatus.return_status_id(
                    determine_event_status(form.end_date.data)
                ),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                name=clean_input(form.name.data),
                description=clean_input(form.description.data),
            )
            flash(f"{clean_input(form.name.data)} successfully added.", "success")
            return redirect(request.url)

    return render_template("events/add_event.j2", form=form)


@blueprint.route("/edit_event/<int:event_id>.html", methods=["GET", "POST"])
def edit_event(event_id: int):
    """Edit an event."""

    form = EventForm()
    event = Event.get_by_id(event_id)

    if not event:
        flash(f"Event with ID {event_id} does not exist.", "error")
        abort(404)

    if request.method == "POST":
        if form.validate_on_submit():
            event.update(
                commit=True,
                id=event_id,
                status_id=EventStatus.return_status_id(
                    determine_event_status(form.end_date.data)
                ),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                name=clean_input(form.name.data),
                description=clean_input(form.description.data),
            )
            flash(
                f"{clean_input(form.name.data)} successfully updated.",
                "success",
            )
            return redirect(url_for("events.edit_event", event_id=event_id))

    form.start_date.data = datetime.strptime(event.start_date, "%Y-%m-%d").date()
    form.end_date.data = datetime.strptime(event.end_date, "%Y-%m-%d").date()
    form.name.data = event.name
    form.description.data = event.description

    return render_template("events/edit_event.j2", event=event, form=form)


@blueprint.route("/delete_event/<int:event_id>.html", methods=["GET", "POST"])
def delete_event(event_id: int):
    """Delete an event."""

    event = Event.get_by_id(event_id)

    if not event:
        flash(f"Event with ID {event_id} does not exist.", "error")
        abort(404)

    if request.method == "POST":
        event.delete()
        flash(f"{event.name} successfully deleted.", "success")
        return redirect(url_for("events.future_events"))

    form = EventForm()
    flash(f"Are you sure you want to delete {event.name}?", "warning")

    return render_template("events/delete_event.j2", event=event, form=form)
