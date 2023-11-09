from . import events_blueprint
from flask import render_template


@events_blueprint.route("/upcoming")
def upcoming_events():
    return render_template("upcoming_events.j2")


@events_blueprint.route("/past")
def past_events():
    return render_template("past_events.j2")
