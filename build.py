# -*- coding: utf-8 -*-
"""Create a frozen instance of the application."""
from flask_frozen import Freezer

from website import create_app

app = create_app()
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["DEBUG"] = False
freezer = Freezer(app)


if __name__ == "__main__":
    freezer.freeze()
