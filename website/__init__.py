# -*- coding: utf-8 -*-
"""The __init__ module, containing the app factory function."""
import sqlalchemy
from click import echo
from flask import Flask, render_template

from website import events, mentor_groups, public, research
from website.extensions import ckeditor, csrf_protect, database, migrate


def create_app(config_object="website.settings"):
    # Create the Flask application using the app factory pattern.
    # http://flask.pocoo.org/docs/patterns/appfactories/.
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    # Check if the database needs to be initialized
    engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    inspector = sqlalchemy.inspect(engine)

    expected_tables = [
        "events",
        "event_status",
        "projects",
        "undergrad_status",
        "project_type",
    ]
    table_names = inspector.get_table_names()

    if not all(items in table_names for items in expected_tables):
        from website.events.models import EventStatus
        from website.research.models import ProjectType, UndergradStatus

        with app.app_context():
            database.drop_all()
            echo("Initializing the database...")
            database.create_all()

            # Data for the following tables should only be inserted once
            # during the initialization of the database.
            database.session.add_all(
                [
                    EventStatus(status="scheduled"),
                    EventStatus(status="completed"),
                    UndergradStatus(status="current"),
                    UndergradStatus(status="former"),
                    ProjectType(type="project"),
                    ProjectType(type="abstract"),
                ]
            )
            database.session.commit()
            echo("Database initialized.")
    else:
        echo("Database already initialized.")

    return app


def register_extensions(app):
    ckeditor.init_app(app)
    csrf_protect.init_app(app)
    database.init_app(app)
    migrate.init_app(app, database)
    return None


def register_blueprints(app):
    app.register_blueprint(public.routes.blueprint)
    app.register_blueprint(events.routes.blueprint)
    app.register_blueprint(mentor_groups.routes.blueprint)
    app.register_blueprint(research.routes.blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.j2"), error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
