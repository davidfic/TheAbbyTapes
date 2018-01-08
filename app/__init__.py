from flask import Flask
from flask import session


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


from app import views
