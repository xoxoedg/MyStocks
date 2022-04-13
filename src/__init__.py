import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

app.config.from_object(os.environ['PROFILE'] if os.environ.get('PROFILE') is not None else {})
app.config['SQLALCHEMY_ECHO'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
testing = app.config['TESTING']
db = SQLAlchemy(app)

from src.administration.lookup.lookup_controller import administration_page

app.register_blueprint(administration_page)
