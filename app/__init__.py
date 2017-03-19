from flask import Flask
from flask import session
from flask_debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


connection = MongoClient("ds047448.mlab.com", 47448)
db = connection["theabbytapes"]
# MongoLab has user authentication
db.authenticate("dfic", "LV78}76eDDx4y7[")


from app import views


