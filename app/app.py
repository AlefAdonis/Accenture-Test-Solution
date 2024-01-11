"""
Main Module
------------------------
Responsible to create the configuration and start the app.

Author: Álef Ádonis dos Santos Carlos
Date: 10/01/2024
"""

from flask import Flask
from flask_cors import CORS
from .extensions import db
from .routes.controller import controller
from flasgger import Swagger
from os import environ


def create_app() -> Flask:
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)

    CORS(app)

    with app.app_context():
        initiate_database(app)
        initiate_blueprints(app)

    swag = initiate_swagger(app)
    return app


def initiate_database(app: Flask):
    """
    Configures the database connection for the Flask application.

    Parameters:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = environ.get("DB_URL")
    app.config["SQLALCHEMY_POOL_SIZE"] = 20
    app.config["SQLALCHEMY_MAX_OVERFLOW"] = 0
    db.init_app(app)


def initiate_blueprints(app: Flask):
    """
    Registers the application's blueprints.

    Parameters:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    app.register_blueprint(controller)


def initiate_swagger(app: Flask):
    """
    Initializes and configures Swagger documentation for the Flask application.

    Parameters:
        app (Flask): The Flask application instance.

    Returns:
        Swagger: The configured Swagger instance.
    """
    return Swagger(app)


def create_tables(app: Flask):
    """
    Creates database tables based on defined models.

    Parameters:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app = create_app()
    create_tables(app)
