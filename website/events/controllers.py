"""
The `events` blueprint handles dipsplaying events pages.
"""
from flask import Blueprint, render_template

events_blueprint = Blueprint("events", __name__, template_folder="templates")


@events_blueprint.route("/upcoming.html")
def upcoming_events():
    return render_template("upcoming_events.j2")


@events_blueprint.route("/past.html")
def past_events():
    return render_template("past_events.j2")
