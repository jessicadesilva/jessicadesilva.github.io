from . import events_blueprint
from flask import render_template


@events_blueprint.route("/events")
def events():
    return render_template("upcoming_events.html")


@events_blueprint.route("/past-events")
def past_events():
    return render_template("past-events.html")
