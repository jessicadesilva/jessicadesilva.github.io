# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()


requirements = [
    "Flask>=3.0.0",
    "Flask-SQLAlchemy>=3.0.0",
    "SQLAlchemy>=2.0.0",
    "Flask-Migrate>=4.0.0",
    "Flask-WTF>=1.0.0",
    "WTForms>=3.0.0",
    "flask-ckeditor>=0.5.1",
    "bleach>=6.0.0",
    "Frozen-Flask>=1.0.1",
    "pydantic>=2.5.2",
    "environs>=9.5.0",
]


setup(
    name="jessicadesilva.io",
    description="Dr. Jessica De Silva's personal website.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["website"],
    package_dir={"website": "website"},
    entry_points={"console_scripts": ["website=website.__main__:main"]},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
)
