# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import bleach


def formatted_date(date: str) -> str:
    """Format date for display on the website."""
    return f"{date[5:]}{date[4]}{date[:4]}".replace("-", "/")


def clean_input(text, *, allow_tags=None):
    """Clean the input from client."""
    if allow_tags is None:
        allow_tags = ["a", "b", "em", "i", "strong"]
    return bleach.clean(text, tags=allow_tags, strip=True)
