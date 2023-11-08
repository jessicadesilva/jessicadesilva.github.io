from . import core_blueprint
from flask import render_template


@core_blueprint.route("/")
def home():
    return render_template("index.html")


@core_blueprint.route("/about")
def about():
    return render_template("about_me.html")


@core_blueprint.route("/student-news")
def student_news():
    return render_template("student_news.html")
