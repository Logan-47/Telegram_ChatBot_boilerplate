from flask import Flask

flask_app = Flask(__name__)

from app.api import api
import app.routes


flask_app.register_blueprint(api)