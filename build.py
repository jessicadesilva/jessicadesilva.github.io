# -*- coding: utf-8 -*-
"""Create a frozen instance of the application."""
from flask_frozen import Freezer

from website import create_app
from website.research.utils import poster_pages

app = create_app()
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True
app.config["FREEZER_REDIRECT_POLICY"] = "ignore"
app.config["DEBUG"] = False
freezer = Freezer(app, with_static_files=True)


@freezer.register_generator
def projects_url_generator():
    for poster in poster_pages():
        yield "research.project", {"poster": poster}


if __name__ == "__main__":
    freezer.freeze()
