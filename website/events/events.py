"""
The `events` blueprint handles displaying events pages.
"""
from website.events.utilities import (
    get_events,
    get_json_schema,
    write_events,
    update_events,
    strip_p_tags,
    check_event_status,
)
from flask import Blueprint, render_template, request
import markdown


events_blueprint = Blueprint("events", __name__, template_folder="templates")


@events_blueprint.route("/upcoming.html")
def upcoming_events():
    event_json_data = get_events()
    data = []
    for event in event_json_data:
        check_event_status(event)
        if event["event_status"] == "scheduled":
            # Create a new dictionary with the event data we want to display.
            event_output = {}
            if event["event_start_date"] == event["event_end_date"]:
                event_output["Date"] = event["event_end_date"]
            else:
                event_output["Date"] = (
                    event["event_start_date"] + " - " + event["event_end_date"]
                )
            event_output["Name"] = event["event_name"]
            event_output["Description"] = event["event_description"]

            data.append(event_output)
            data = sorted(data, key=lambda k: k["Date"])

            update_events(sorted(event_json_data, key=lambda k: k["event_start_date"]))
    return render_template("upcoming.j2", data=data)


@events_blueprint.route("/past.html")
def past_events():
    event_json_data = get_events()
    data = []
    for event in event_json_data:
        check_event_status(event)
        if event["event_status"] == "past":
            # Create a new dictionary with the event data we want to display.
            event_output = {}
            if event["event_start_date"] == event["event_end_date"]:
                event_output["Date"] = event["event_end_date"]
            else:
                event_output["Date"] = (
                    event["event_start_date"] + " - " + event["event_end_date"]
                )
            event_output["Name"] = event["event_name"]
            event_output["Description"] = event["event_description"]

            data.append(event_output)
            data = sorted(data, key=lambda k: k["Date"], reverse=True)

            update_events(
                sorted(
                    event_json_data,
                    key=lambda k: k["event_end_date"],
                    reverse=True,
                )
            )

    return render_template("past_events.j2", data=data)


@events_blueprint.route("/add.html", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        if request.form.get("add_event"):
            event = {
                "event_status": "scheduled",
                "event_start_date": request.form.get("start_date"),
                "event_end_date": request.form.get("end_date"),
                #
                # NOTE: Event name and description support markdown formating.
                # Convert to HTML and remove the <p> tags.
                #
                "event_name": "".join(
                    strip_p_tags(
                        markdown.markdown("".join(request.form.get("event_name")))
                    )
                ),
                "event_description": "".join(
                    strip_p_tags(
                        markdown.markdown(
                            "".join(request.form.get("event_description"))
                        )
                    )
                ),
            }

            if write_events(event) == "Event already exists.":
                return render_template(
                    "add_event.j2",
                    error="The event you are trying to add already exists.",
                )

    return render_template("add_event.j2")


@events_blueprint.route("/data/schema.json")
def schema():
    return get_json_schema()
