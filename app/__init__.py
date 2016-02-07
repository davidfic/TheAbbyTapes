from flask import Flask
from flask import session
from flask.ext.debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


connection = MongoClient("<<hostname>>", <<port>>)
db = connection["theabbytapes"]
# MongoLab has user authentication
db.authenticate("<<username>>", "<<password>>")


from app import views


