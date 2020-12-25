# 

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from nb.settings import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

from nb import routes

if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()