from datetime import datetime
import json
import os

import markdown


def load_events_data_file():
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "events.json"), "r"
    ) as json_file:
        return json.load(json_file)


def get_event_schema():
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "schema.json"), "r"
    ) as json_file:
        return json.load(json_file)


def update_events_data_file(event_data):
    with open(
        os.path.join(os.getcwd(), "website", "events", "data", "events.json"), "w"
    ) as json_file:
        json.dump(event_data, json_file, indent=4)


def determine_event_status(end_date: str) -> str:
    date = datetime.strptime(end_date, "%Y-%m-%d")
    if date < datetime.today():
        return "completed"
    else:
        return "scheduled"


def formatted_date(date: str) -> str:
    return f"{date[5:]}{date[4]}{date[:4]}".replace("-", "/")


def strip_p_tags(text: str) -> str:
    return text.replace("<p>", "").replace("</p>", "")


def markdown_formatted(data: str) -> str:
    return strip_p_tags(markdown.markdown(data))


def event_is_unique(events_file_data: dict, event: dict) -> bool:
    for existing_event in events_file_data["events"]:
        if (
            existing_event["start_date"] == event["start_date"]
            and existing_event["end_date"] == event["end_date"]
            and existing_event["name"] == event["name"]
            and existing_event["description"] == event["description"]
        ):
            return False
    return True
