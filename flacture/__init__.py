# -*- coding: utf-8 -*-
"""
    flacture
    ~~~~~~~~

    flacture factory module
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_json import FlaskJSON

from .config import config
from .errors import Unauthorized, ValidationError, on_not_found, \
    on_unauthorized, on_not_validated, on_not_allowed

db = SQLAlchemy()
json = FlaskJSON()


def create_app(package_name, package_path, config_override=None):
    """Factory function to return a `Flask` application instance.

        :package_name: the name of your application.
        :package_path: the path of your application.
        :config_override: the settings for you application
    """

    app = Flask(package_name)
    app.config.from_object(config['development'])
    app.config.from_object(config_override)

    db.init_app(app)
    json.init_app(app)

    app.errorhandler(404)(on_not_found)
    app.errorhandler(405)(on_not_allowed)
    app.errorhandler(Unauthorized)(on_unauthorized)
    app.errorhandler(ValidationError)(on_not_validated)

    from .helpers import register_blueprints
    register_blueprints(app, package_name, package_path)

    return app
