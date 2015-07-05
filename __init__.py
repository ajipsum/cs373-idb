#!/usr/bin/env python3

from flask import Flask, send_file, send_from_directory, safe_join
from jinja2 import TemplateNotFound
app = Flask(__name__)

# Allows for any URL to be handled by AngularJS
# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(**kwargs):
    return send_file('index.html')

# Allows us to not have to rely on Flask's default directory structure
# http://stackoverflow.com/questions/23685687/flask-html-js-css-img-reference-404-error
@app.route('/<any(static, templates):folder>/<path:filename>')
def toplevel_static(folder, filename):
    filename = safe_join(folder, filename)
    cache_timeout = app.get_send_file_max_age(filename)
    return send_file(filename)


"""
@app.route("/teams")
def teams():
    return render_template('teams/index.html')

@app.route("/players")
def players():
    return render_template('players/index.html')

@app.route("/games")
def games():
    return render_template('games/index.html')

@app.route("/LAC")
def LAC():
    return render_template('teams/LAC.html')

@app.route("/MIA")
def MIA():
    return render_template('teams/MIA.html')

@app.route("/SAS")
def SAS():
    return render_template('teams/SAS.html')

@app.route("/BG")
def BG():
    return render_template('players/BG.html')

@app.route("/DW")
def DW():
    return render_template('players/DW.html')

@app.route("/TD")
def TD():
    return render_template('players/TD.html')

@app.route("/102")
def G102():
    return render_template('games/102.html')

@app.route("/414")
def G414():
    return render_template('games/414.html')

@app.route("/559")
def G559():
    return render_template('games/559.html')

@app.route("/about")
def about():
    return render_template('about.html')
"""
if __name__ == "__main__":
    app.debug = True
    app.run(port = 5001)
