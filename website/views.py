"""
The `views` file handles displaying the top-level web pages.
"""

from flask import Blueprint, render_template

core_blueprint = Blueprint("core", __name__, template_folder="templates")


@core_blueprint.route("/index.html")
def home():
    return render_template("index.j2")


@core_blueprint.route("/about.html")
def about():
    return render_template("about_me.j2")


@core_blueprint.route("/about/cv.html")
def cv():
    return render_template("desilva_cv.j2")


@core_blueprint.route("/news.html")
def student_news():
    return render_template("student_news.j2")
