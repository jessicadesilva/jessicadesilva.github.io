from flask_frozen import Freezer
from website import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()

app.config["FREEZER_RELATIVE_URLS"] = True
# Create an instance of Freezer for generating the static files from
# the Flask application routes ('/', '/about', etc.)
freezer = Freezer(app)


if __name__ == "__main__":
    # Generate the static files using Frozen-Flask
    freezer.freeze()
