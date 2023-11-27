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


def update_events_file(event_data):
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "events.json"), "w"
    ) as json_file:
        json.dump(event_data, json_file, indent=4)


def determine_event_status(end_date):
    date = datetime.strptime(end_date, "%Y-%m-%d")
    if date < datetime.today():
        return "completed"
    else:
        return "scheduled"


def format_date_string(date):
    return f"{date[5:]}{date[4]}{date[:4]}".replace("-", "/")


def strip_p_tags(text):
    return text.replace("<p>", "").replace("</p>", "")


def event_is_unique(events_data_file, event):
    for existing_event in events_data_file["events"]:
        if (
            existing_event["start_date"] == event["start_date"]
            and existing_event["end_date"] == event["end_date"]
            and existing_event["name"] == event["name"]
            and existing_event["description"] == event["description"]
        ):
            return False
    return True
