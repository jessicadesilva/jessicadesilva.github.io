"""
The `general` blueprint handles the top-level pages of the website.
"""

from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__, template_folder="templates")


# NOTE: The routes below are relative to the "main" blueprint, so they are
#       prefixed with "/". This means that the url_for() function must include
#       the blueprint name when generating a URL for these routes, e.g.
#       url_for("main.home").
#
#
# NOTE: This project uses Frozen-Flask to generate a static version of the
#       website. Frozen-Flask requires that all routes end with ".html" so that
#       it can generate the appropriate files. Please keep this in mind when adding
#       new routes to this blueprint.


@main_blueprint.route("/index.html")
def home():
    return render_template("index.j2")


@main_blueprint.route("/about.html")
def about():
    return render_template("about_me.j2")


@main_blueprint.route("/about/cv.html")
def cv():
    return render_template("desilva_cv.j2")


@main_blueprint.route("/news.html")
def student_news():
    return render_template("student_news.j2")
