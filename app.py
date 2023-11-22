from website import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()


if __name__ == "__main__":
    # Run the development server on <http://127.0.0.1:5000>
    # NOTE: We are using the development server here, which is not
    #       suitable for production. See the Flask deployment guide
    #       for information on deploying a Flask application:
    #           http://flask.pocoo.org/docs/deploying/
    # NOTE: We are not using Frozen-Flask here, so we can take advantage
    #       of the dynamic nature of Flask to run the application.
    app.run(debug=True)
