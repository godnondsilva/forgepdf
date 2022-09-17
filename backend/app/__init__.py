from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.debug = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/forgepdf"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = 'forge-secret-pdf'
app.config['WEATHER_API_KEY'] = '344ee811972a07fd02ae47ca448f0700'

# configuration of database
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from app import routes