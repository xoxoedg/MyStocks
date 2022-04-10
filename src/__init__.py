from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/stocks'
app.config['SQLALCHEMY_ECHO'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

from src.administration.lookup.lookup_controller import administration_page

app.register_blueprint(administration_page)
