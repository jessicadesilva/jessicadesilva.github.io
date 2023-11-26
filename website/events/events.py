"""
The `events` blueprint handles displaying events pages.
"""
from datetime import date

from flask import Blueprint, flash, render_template, request, redirect, url_for
from markdown import markdown

from website.events.utilities import (
    determine_event_status,
    event_is_unique,
    get_events,
    get_json_schema,
    strip_p_tags,
    update_events_file,
)


events_blueprint = Blueprint("events", __name__, template_folder="templates")


@events_blueprint.route("/upcoming.html")
def upcoming_events():
    event_json_data = get_events()
    data = []
    for event in event_json_data["events"]:
        determine_event_status(event["end_date"])

        if event["status"] == "scheduled":
            event_output = {}
            if event["start_date"] == event["end_date"]:
                event_output["Date"] = event["end_date"]
            else:
                event_output["Date"] = event["start_date"] + " - " + event["end_date"]
            #
            # NOTE: Event name and description support markdown formating.
            # Convert to HTML and remove the <p> tags.
            #
            event_output["Name"] = "".join(
                strip_p_tags(markdown("".join(event["name"])))
            )
            event_output["Description"] = "".join(
                strip_p_tags(markdown("".join(event["description"])))
            )

            data.append(event_output)
            data = sorted(data, key=lambda k: k["Date"])

    event_json_data["events"] = sorted(
        event_json_data["events"], key=lambda k: k["start_date"], reverse=True
    )
    update_events_file(event_json_data)

    return render_template(
        "upcoming_events.j2", data=data, updated=event_json_data["updated"]
    )


@events_blueprint.route("/past.html")
def past_events():
    event_json_data = get_events()
    data = []
    for event in event_json_data["events"]:
        determine_event_status(event["end_date"])

        if event["status"] == "completed":
            event_output = {}
            if event["start_date"] == event["end_date"]:
                event_output["Date"] = event["end_date"]
            else:
                event_output["Date"] = event["start_date"] + " - " + event["end_date"]
            #
            # NOTE: Event name and description support markdown formating.
            # Convert to HTML and remove the <p> tags.
            #
            event_output["Name"] = "".join(
                strip_p_tags(markdown("".join(event["name"])))
            )
            event_output["Description"] = "".join(
                strip_p_tags(markdown("".join(event["description"])))
            )

            data.append(event_output)
            data = sorted(data, key=lambda k: k["Date"], reverse=True)

    event_json_data["events"] = sorted(
        event_json_data["events"], key=lambda k: k["start_date"], reverse=True
    )
    update_events_file(event_json_data)

    return render_template(
        "past_events.j2", data=data, updated=event_json_data["updated"]
    )


@events_blueprint.route("/add.html", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event_json_data = get_events()
        if request.form.get("add_event"):
            event = {
                "id": len(event_json_data["events"]) + 1,
                "status": determine_event_status(request.form.get("end_date")),
                "start_date": request.form.get("start_date"),
                "end_date": request.form.get("end_date"),
                "name": "".join(request.form.get("name")),
                "description": "".join(request.form.get("description")),
            }

            if not event_is_unique(event_json_data, event):
                flash("The event you are trying to add already exists.", "error")
                return redirect(url_for("events.add_event"))

            event_json_data["events"].append(event)
            event_json_data["events"] = sorted(
                event_json_data["events"],
                key=lambda k: k["start_date"],
                reverse=True,
            )
            event_json_data["updated"] = date.today().strftime("%b %d, %Y")
            update_events_file(event_json_data)
            flash("Event added successfully.", "success")

    return render_template("add_event.j2")


@events_blueprint.route("/schema.json")
def events_schema():
    return get_json_schema()
