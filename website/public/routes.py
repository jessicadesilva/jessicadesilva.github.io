# -*- coding: utf-8 -*-
"""Public section, including homepage, about, and student news."""
from flask import Blueprint, render_template

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/index.html")
def home():
    return render_template("public/home.j2")


@blueprint.route("/about.html")
def about():
    return render_template("public/about_me.j2")


@blueprint.route("/about/cv.html")
def cv():
    return render_template("public/desilva_cv.j2")


@blueprint.route("/news.html")
def student_news():
    return render_template("public/student_news.j2")
