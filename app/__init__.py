from flask import Flask
from flask import session
from flask_debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


connection = MongoClient("localhost", 8080)
db = connection["theabbytapes"]
# MongoLab has user authentication
db.authenticate("davidfic", "password")


from app import views


