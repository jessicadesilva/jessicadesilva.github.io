from datetime import datetime, timedelta

import pytest

from website.events.utilities import (
    determine_event_status,
    event_is_unique,
    formatted_date,
    get_event_schema,
    load_events_data_file,
    markdown_formatted,
    strip_p_tags,
    update_events_data_file,
)

from website.events.schema import EventSchema, EventsListSchema


@pytest.mark.utility
def test_determine_event_status_completed():
    """
    GIVEN an event end date in a string with the format YYYY-MM-DD,
    WHEN the event end date is less than today,
    THEN the event status is completed.
    """
    past_date = str((datetime.today() - timedelta(days=1)).date())

    assert determine_event_status(past_date) == "completed"


@pytest.mark.utility
def test_determine_event_status_scheduled():
    """
    GIVEN an event end date in a string with the format YYYY-MM-DD,
    WHEN the event end date is greater than or equal to today,
    THEN the event status is scheduled.
    """
    future_date = str((datetime.today() + timedelta(days=1)).date())
    current_date = str(datetime.today().date())

    assert determine_event_status(future_date) == "scheduled"
    assert determine_event_status(current_date) == "scheduled"


@pytest.mark.utility
def test_formatted_date():
    """
    GIVEN a date string in the format YYYY-MM-DD,
    WHEN the date is passed to the function,
    THEN the date is returned in the format DD/MM/YYYY.
    """
    date_strings = [
        "2021-01-01",
        "2021-01-31",
        "2021-12-01",
        "2021-12-31",
    ]
    expected_dates = [
        "01/01/2021",
        "01/31/2021",
        "12/01/2021",
        "12/31/2021",
    ]

    for date in date_strings:
        assert formatted_date(date) == expected_dates[date_strings.index(date)]


@pytest.mark.utility
def test_strip_p_tags():
    """
    GIVEN a string containing HTML paragraph tags,
    WHEN the string is passed to the function,
    THEN the string is returned with the paragraph tags removed.
    NOTE: This is a helper function for the markdown_formatted function to allow
            for the markdown output to be nested within other markdown elements.
    """
    p_tag_string = "<p>This is a test string.</p>"
    multi_p_tag_string = (
        "<p>This is a test string.</p><p>This is another test string.</p>"
    )
    nested_p_tag_string = "<p>This is a <p>test</p> string.</p>"

    assert strip_p_tags(p_tag_string) == "This is a test string."
    assert (
        strip_p_tags(multi_p_tag_string)
        == "This is a test string.This is another test string."
    )
    assert strip_p_tags(nested_p_tag_string) == "This is a test string."


@pytest.mark.utility
def test_markdown_formatted():
    """
    GIVEN a string containing markdown,
    WHEN the string is passed to the function,
    THEN the string is returned with the markdown converted to HTML.
    NOTE: The HTML paragraph tags are removed by the strip_p_tags function to allow
            for the markdown output to be nested within other markdown elements.
    """
    paragraph_string = "This is a test string."
    bold_string = "This is a **test** string."
    italic_string = "This is a *test* string."
    link_string = "This is a [test](https://www.example.com) string."
    code_string = "This is a `test` string."
    code_block_string = """```
    This is
    a
    test string.
    ```"""
    image_string = "This is a ![test](https://www.example.com) string."

    assert markdown_formatted(paragraph_string) == "This is a test string."
    assert markdown_formatted(bold_string) == "This is a <strong>test</strong> string."
    assert markdown_formatted(italic_string) == "This is a <em>test</em> string."
    assert (
        markdown_formatted(link_string)
        == 'This is a <a href="https://www.example.com">test</a> string.'
    )
    assert markdown_formatted(code_string) == "This is a <code>test</code> string."
    assert (
        markdown_formatted(code_block_string)
        == "<code>This is\n    a\n    test string.</code>"
    )
    assert (
        markdown_formatted(image_string)
        == 'This is a <img alt="test" src="https://www.example.com" /> string.'
    )


@pytest.mark.utility
def test_markdown_formatted_heading():
    """
    GIVEN a string containing markdown heading,
    WHEN the string is passed to the function,
    THEN the string is returned with the markdown heading converted to HTML.
    """
    heading_1_string = "# This is a test string."
    heading_2_string = "## This is a test string."
    heading_3_string = "### This is a test string."
    heading_4_string = "#### This is a test string."
    heading_5_string = "##### This is a test string."
    heading_6_string = "###### This is a test string."

    assert markdown_formatted(heading_1_string) == "<h1>This is a test string.</h1>"
    assert markdown_formatted(heading_2_string) == "<h2>This is a test string.</h2>"
    assert markdown_formatted(heading_3_string) == "<h3>This is a test string.</h3>"
    assert markdown_formatted(heading_4_string) == "<h4>This is a test string.</h4>"
    assert markdown_formatted(heading_5_string) == "<h5>This is a test string.</h5>"
    assert markdown_formatted(heading_6_string) == "<h6>This is a test string.</h6>"


@pytest.mark.utility
def test_markdown_formatted_list():
    """
    GIVEN a string containing markdown list,
    WHEN the string is passed to the function,
    THEN the string is returned with the markdown list converted to HTML.
    """
    unordered_list_string = "- This is a test string."
    assert (
        markdown_formatted(unordered_list_string)
        == "<ul>\n<li>This is a test string.</li>\n</ul>"
    )
    ordered_list_string = "1. This is a test string."
    assert (
        markdown_formatted(ordered_list_string)
        == "<ol>\n<li>This is a test string.</li>\n</ol>"
    )


@pytest.mark.utility
def test_markdown_formatted_blockquote():
    """
    GIVEN a string containing markdown blockquote,
    WHEN the string is passed to the function,
    THEN the string is returned with the markdown blockquote converted to HTML.
    """
    blockquote_string = "> This is a test string."
    assert (
        markdown_formatted(blockquote_string)
        == "<blockquote>\nThis is a test string.\n</blockquote>"
    )


@pytest.mark.utility
def test_markdown_formatted_horizontal_rule():
    """
    GIVEN a string containing markdown horizontal rule,
    WHEN the string is passed to the function,
    THEN the string is returned with the markdown horizontal rule converted to HTML.
    """
    horizontal_rule_string = "---"
    assert markdown_formatted(horizontal_rule_string) == "<hr />"
