"""
The `events` blueprint handles displaying events pages.
"""
from datetime import date

from flask import Blueprint, flash, render_template, request, redirect, abort
from pydantic import ValidationError

from website.events.schema import EventSchema, EventsListSchema
from website.events.utilities import (
    determine_event_status,
    event_is_unique,
    formatted_date,
    get_event_schema,
    load_events_data_file,
    markdown_formatted,
    update_events_data_file,
)


events_blueprint = Blueprint("events", __name__, template_folder="templates")


@events_blueprint.route("/scheduled.html")
def scheduled_events():
    try:
        event_json_data = load_events_data_file()
    except OSError as error:
        flash(error, "error")
        abort(500)
    else:
        try:
            EventsListSchema.model_validate(event_json_data)
        except ValidationError as error:
            flash(error, "error")
            abort(500)

    data = []
    for event in event_json_data["events"]:
        determine_event_status(event["end_date"])
        event_json_data["events"] = sorted(
            event_json_data["events"], key=lambda k: k["end_date"], reverse=True
        )

        try:
            update_events_data_file(event_json_data)
        except OSError as error:
            flash(error, "error")
            abort(500)

        if event["status"] == "scheduled":
            event_output = {
                "ID": event["id"],
                "Date": formatted_date(event["end_date"])
                if event["start_date"] == event["end_date"]
                else formatted_date(event["start_date"])
                + " - "
                + formatted_date(event["end_date"]),
                "Name": markdown_formatted(event["name"]),
                "Description": markdown_formatted(event["description"]),
            }
            data.append(event_output)

    return render_template(
        "scheduled_events.j2", data=data, updated=event_json_data["updated"]
    )


@events_blueprint.route("/past.html")
def past_events():
    try:
        event_json_data = load_events_data_file()
    except OSError as error:
        flash(error, "error")
        abort(500)
    else:
        try:
            EventsListSchema.model_validate(event_json_data)
        except ValidationError as error:
            flash(error, "error")
            abort(500)

    data = []
    for event in event_json_data["events"]:
        determine_event_status(event["end_date"])
        event_json_data["events"] = sorted(
            event_json_data["events"], key=lambda k: k["end_date"], reverse=True
        )
        try:
            update_events_data_file(event_json_data)
        except OSError as error:
            flash(error, "error")
            abort(500)

        if event["status"] == "completed":
            output_data = {
                "ID": event["id"],
                "Date": formatted_date(event["end_date"])
                if event["start_date"] == event["end_date"]
                else formatted_date(event["start_date"])
                + " - "
                + formatted_date(event["end_date"]),
                "Name": markdown_formatted(event["name"]),
                "Description": markdown_formatted(event["description"]),
            }
            data.append(output_data)

    return render_template(
        "past_events.j2", data=data, updated=event_json_data["updated"]
    )


# NOTE: This page is only interactive when the development server is running.
@events_blueprint.route("/add.html", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        if request.form.get("add_event"):
            if not request.form.get("start_date"):
                flash("Event start date not provided.", "error")
                return redirect(request.url)

            if not request.form.get("end_date"):
                flash("Event end date not provided.", "error")
                return redirect(request.url)

            if not request.form.get("name"):
                flash("Event name not provided.", "error")
                return redirect(request.url)

            if not request.form.get("description"):
                flash("Event description not provided.", "error")
                return redirect(request.url)

            try:
                events_json_data = load_events_data_file()
            except OSError as error:
                flash(error, "error")
                abort(500)
            else:
                try:
                    EventsListSchema.model_validate(events_json_data)
                except ValidationError as error:
                    flash(error, "error")
                    return redirect(request.url)

            event = {
                "id": len(events_json_data["events"]) + 1,
                "status": determine_event_status(request.form.get("end_date")),
                "start_date": request.form.get("start_date"),
                "end_date": request.form.get("end_date"),
                "name": request.form.get("name"),
                "description": request.form.get("description"),
            }
            try:
                EventSchema.model_validate(event)
            except ValidationError as error:
                flash(error, "error")
                return redirect(request.url)

            if not event_is_unique(events_json_data, event):
                flash("The event you are trying to add already exists.", "error")
                return redirect(request.url)

            events_json_data["events"].append(event)
            events_json_data["events"] = sorted(
                events_json_data["events"],
                key=lambda k: k["start_date"],
                reverse=True,
            )
            events_json_data["updated"] = date.today().strftime("%b %d, %Y")

            try:
                update_events_data_file(events_json_data)
            except OSError as error:
                flash(error, "error")
                abort(500)
            else:
                flash("Event successfully added.", "success")

            for key, value in event.items():
                flash(f"{key}: {value}", "info" if value != "" else "question")

    flash(
        "This is an internal page that is only live on the development server.", "info"
    )
    return render_template("add_event.j2")


@events_blueprint.route("/schema.json")
def events_schema():
    return get_event_schema()
