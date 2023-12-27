# -*- coding: utf-8 -*-
"""Unit tests for the utils module."""
from website.utils import format_display_date, clean_input


class TestUtils:
    def test_function_format_display_date_returns_expected_with_valid_date_string(self):
        assert format_display_date("2020-01-01") == "01/01/2020"

    def test_function_clean_input_removes_unallowed_tags(self):
        # NOTE: Default allowed tags ["a", "b", "em", "i", "strong"]
        test_strings = [
            "<blockquote>Test</blockquote>",
            "<code>Test</code>",
            "<h1>Test</h1>",
            "<h2>Test</h2>",
            "<h3>Test</h3>",
            "<h4>Test</h4>",
            "<h5>Test</h5>",
            "<h6>Test</h6>",
            "<img>Test</img>",
            "<p>Test</p>",
            "<pre>Test</pre>",
            "<script>Test</script>",
            "<style>Test</style>",
            "<table>Test</table>",
        ]

        for test_string in test_strings:
            assert clean_input(test_string) == "Test"
