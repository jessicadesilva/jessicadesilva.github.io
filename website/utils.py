# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""


def formatted_date(date: str) -> str:
    """Format date for display on the website."""
    return f"{date[5:]}{date[4]}{date[:4]}".replace("-", "/")


def strip_p_tags(text: str) -> str:
    """Remove <p> tags from text."""
    return text.replace("<p>", "").replace("</p>", "")
