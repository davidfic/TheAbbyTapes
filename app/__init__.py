from flask import Flask
from flask import session


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


# connection = MongoClient("ds047448.mlab.com", 47448)
# db = connection["theabbytapes"]
# # MongoLab has user authentication
# db.authenticate("dfic2", "password")


from app import views
