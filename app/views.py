from flask import flash, redirect,render_template, send_file, request,session,g, url_for
from functools import wraps
from app import app
# import db as db
from . import db as db
# from flask_login import login_user, logout_user, current_user, login_required

videos = ['UCHO47KZgvg','0Un96jc_7sM','Ef6uFle-QqY','i6SUIajY-3I','YPr2UZfS4Vg','caDcaexxxmo','vhwo-U8PfpE']

client = db.create_client('kubernetes-testing-186304')

players = db.list_players(client)


player_list = []
player_dict = {}

# [player_list.append(player) for player in players]

# for player in players:
#     players_dict = dict(player)



# @login_required
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", players=players, player_dict=player_dict)#, places=db.get_places())

# @login_required
@app.route('/download')
def get_full_video():
   return render_template("download.html")#, data=db.get_downloads())

# @login_required  
@app.route('/player-<name>')
def player_page(name):
  return render_template("player.html", name=name)

# @login_required
@app.route('/pics-<location>')
def pics(location):
  return render_template("pics.html", location=location)

# @login_required
@app.route('/south_africa')
def south_africa():
    return render_template("south_africa.html")

# @login_required
@app.route('/video-gll')
def gll():
    return render_template("gll.html")

# @login_required
@app.route('/video-munncabin')
def munn():
    return render_template("munn.html")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         print "password info: ",  request.form['password']
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)

# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return "You are Logged out. Bye"

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function


# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html', error)

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'),404

