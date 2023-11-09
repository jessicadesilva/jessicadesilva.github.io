"""
The `views` file handles displaying the top-level web pages.
"""

from flask import render_template
from . import app


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.j2")


@app.route("/about")
def about():
    return render_template("about_me.j2")


@app.route("/about/cv")
def cv():
    return render_template("desilva_cv.j2")


@app.route("/news")
def student_news():
    return render_template("student_news.j2")
