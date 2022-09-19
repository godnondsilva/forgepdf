from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.debug = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = 'forge-secret-pdf'
app.config['WEATHER_API_KEY'] = os.getenv('WEATHER_API_KEY')

# configuration of database
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from app import routes