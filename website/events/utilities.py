from datetime import datetime
import json
import os


def get_events():
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "events.json"), "r"
    ) as json_file:
        return json.load(json_file)


def get_json_schema():
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "schema.json"), "r"
    ) as json_file:
        return json.load(json_file)


def update_events(event_data):
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "events.json"), "w"
    ) as json_file:
        json.dump(event_data, json_file, indent=4)


def check_event_status(event):
    """Check if an event is scheduled or past."""

    event_start_date = datetime.strptime(event.get("event_start_date"), "%Y-%m-%d")
    event_end_date = datetime.strptime(event.get("event_end_date"), "%Y-%m-%d")
    today = datetime.today()

    if event_start_date > today:
        event["event_status"] = "scheduled"
    elif event_end_date < today:
        event["event_status"] = "past"

    return event


def strip_p_tags(text):
    return text.replace("<p>", "").replace("</p>", "")


def is_event_unique(event):
    events_data = get_events()
    for existing_event in events_data:
        if (
            existing_event["event_start_date"] == event["event_start_date"]
            and existing_event["event_end_date"] == event["event_end_date"]
            and existing_event["event_name"] == event["event_name"]
            and existing_event["event_description"] == event["event_description"]
        ):
            return False
    return True


def write_events(event):
    if is_event_unique(event) is False:
        return "Event already exists."

    events_data = get_events()
    events_data.append(event)

    update_events(events_data)
