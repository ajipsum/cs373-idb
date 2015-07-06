#!/usr/bin/env python3
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, send_file, send_from_directory, safe_join
from jinja2 import TemplateNotFound
app = Flask(__name__)

# Load config.py
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
db = SQLAlchemy(app)

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

if __name__ == "__main__":
    app.debug = True
    app.run(port = 5001)
