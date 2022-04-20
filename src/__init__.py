import os

from flask import Flask, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

testing = None


def create_app(config_file=None):
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config.from_object(os.environ['PROFILE'] if os.environ.get('PROFILE') is not None else {})
    db.init_app(app)
    app.config['SQLALCHEMY_ECHO'] = True
    global testing
    testing = app.config["TESTING"]

    from src.administration.lookup.lookup_controller import administration_page

    app.register_blueprint(administration_page)

    return app


db = SQLAlchemy()
SQLALCHEMY_TRACK_MODIFICATIONS = True

