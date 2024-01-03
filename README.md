# Dr. Jessica De Silva's Website
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-jessicadesilva.github.io-informational?logo=github)](https://jessicadesilva.github.io/)
[![Maintainability](https://api.codeclimate.com/v1/badges/d6e4c8b1388dfda34fa0/maintainability)](https://codeclimate.com/github/4N0NYM0U5MY7H/jessicadesilva.github.io/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d6e4c8b1388dfda34fa0/test_coverage)](https://codeclimate.com/github/4N0NYM0U5MY7H/jessicadesilva.github.io/test_coverage)


## Installation
### Prerequisites
- [Python 3.10](https://www.python.org/downloads/release/python-3109/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [pipenv](https://pypi.org/project/pipenv/)
- [git](https://git-scm.com/downloads)
- [GitHub CLI](https://cli.github.com/) (optional)
- [Visual Studio Code](https://code.visualstudio.com/) (optional)
- [DB Browser for SQLite](https://sqlitebrowser.org/) (optional)

### Clone the repository
```sh
git clone https://github.com/jessicadesilva/jessicadesilva.github.io.git
```
#### Change directory to the project root
```sh
cd jessicadesilva.github.io
```
### Running locally
Run the following commands to boostrap your environment and run the development server locally.
### Pipenv (preferred installation method)
```sh
pipenv install --dev
pipenv shell
```
### Virtualenv (alternative method)
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Initialize the environment variables
```sh
python init_env.py
```
### Run the development server
```sh
flask run --debug
```
Navigate to `http://127.0.0.1:5000/` in your browser to view the website!

## Deployment
Starting the development server with `flask run` will not generate the static files required for deployment.
### Generate a local preview
```sh
python build.py
```
### Deploy to GitHub Pages
Commmiting changes to `main` or accepting a pull request on the `main` branch will trigger the [GitHub Actions Build and Deploy workflow](.github/workflows/main.yml). Automation takes care of the rest!

## Running Tests/Linter
### Run all tests
```sh
pytest
# or
python -m pytest
```

## Built With
[![Python 3.10](https://img.shields.io/badge/Python-3.10-informational?logo=python&logoColor=fff)](https://www.python.org/downloads/release/python-3109/)
[![Flask 3.0](https://img.shields.io/badge/Flask-3.0-informational?logo=flask)](https://flask.palletsprojects.com/en/3.0.x/)
[![Jinja2 3.1](https://img.shields.io/badge/Jinja2-3.1-informational?logo=jinja)](https://jinja.palletsprojects.com/en/3.1.x/)
[![Frozen Flask 1.0](https://img.shields.io/badge/Frozen_Flask-1.0-informational?logo=flask)](https://frozen-flask.readthedocs.io/en/latest/)
[![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0-informational?logo=sqlalchemy)](https://docs.sqlalchemy.org/en/20/)
[![Pydantic 2.5](https://img.shields.io/badge/Pydantic-2.5-informational?logo=pydantic)](https://docs.pydantic.dev/2.5/)
[![WTForms 3.0](https://img.shields.io/badge/%23%3F%21_WTForms-3.0-informational)](https://wtforms.readthedocs.io/en/3.0.x/)
[![CKEditor 4](https://img.shields.io/badge/CKEditor-4-informational?logo=ckeditor4&logoColor=fff)](https://ckeditor.com/docs/ckeditor4/latest/index.html)
[![HTML5 UP](https://img.shields.io/badge/HTML5_UP-Editorial-informational?logo=html5&logoColor=fff)](https://html5up.net/editorial)

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
