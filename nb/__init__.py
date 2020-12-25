#init

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from nb.settings import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

from nb import routes
