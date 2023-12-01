import os
import pytest
from website import create_app


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    flask_app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    flask_app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")
    flask_app.config["ALLOWED_EXTENSIONS"] = os.environ.get("ALLOWED_EXTENSIONS")

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        yield testing_client  # this is where the testing happens!
