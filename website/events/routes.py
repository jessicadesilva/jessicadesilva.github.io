from . import events_blueprint
from flask import render_template


@events_blueprint.route("/events")
def events():
    # This is a placeholder for the events page
    pass


@events_blueprint.route("/events/upcoming")
def upcoming_events():
    return render_template("upcoming_events.html")


@events_blueprint.route("/events/past")
def past_events():
    return render_template("past_events.html")
