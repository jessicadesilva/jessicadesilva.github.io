# -*- coding: utf-8 -*-
"""Click commands."""
import os
from glob import glob
from subprocess import call

import click

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, "tests")


@click.command()
@click.option(
    "-c/-C",
    "--coverage/--no-coverage",
    default=True,
    help="Show coverage report.",
)
def test(coverage):
    """Run the tests."""
    import pytest

    args = [TEST_PATH, "--verbose"]
    if coverage:
        args.append("--cov=website")
    rv = pytest.main(args)
    exit(rv)


@click.command()
@click.option(
    "-c",
    "--check",
    default=False,
    is_flag=True,
    help="Check if the code is formatted without applying changes.",
)
def lint(check):
    """Lint and check code style with black and flake8."""
    skip = ["migrations", "requirements"]
    root_files = glob("*.py")
    root_directories = [
        name for name in next(os.walk("."))[1] if not name.startswith(".")
    ]
    files_and_directories = [
        arg for arg in root_files + root_directories if arg not in skip
    ]

    def execute_tool(description, *args):
        """Execute a checking tool with its arguments."""
        command_line = list(args) + files_and_directories
        click.echo(f"{description}: {' '.join(command_line)}")
        rv = call(command_line)
        if rv != 0:
            exit(rv)

    black_args = []
    if check:
        black_args.append("--check")
    execute_tool("Formatting files with black", "black", *black_args)
    execute_tool("Checking code style with flake8", "flake8")
