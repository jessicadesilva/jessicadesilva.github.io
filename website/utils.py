# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from functools import wraps

import bleach
from flask import current_app


def dev_utils(func):
    """Decorator that adds addtional functionality when in debug mode."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_app.debug:
            kwargs["debug"] = True
        return func(*args, **kwargs)

    return wrapper


def formatted_date(date: str) -> str:
    """Format date for display on the website."""
    return f"{date[5:]}{date[4]}{date[:4]}".replace("-", "/")


def clean_input(text, *, allow_tags=None):
    """Clean the input from client."""
    if allow_tags is None:
        allow_tags = ["a", "b", "em", "i", "strong"]
    return bleach.clean(text, tags=allow_tags, strip=True)
