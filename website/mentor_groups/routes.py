# -*- coding: utf-8 -*-
"""Mentor groups section, including math and stan."""
from flask import Blueprint, render_template

blueprint = Blueprint(
    "mentor_groups", __name__, url_prefix="/mentor_groups", static_folder="../static"
)


@blueprint.route("/math.html")
def math():
    """Mentor groups page for Math."""
    return render_template("mentor_groups/math.j2")


@blueprint.route("/stan.html")
def stan():
    """Mentor groups page for Stan State."""
    return render_template("mentor_groups/stan.j2")
