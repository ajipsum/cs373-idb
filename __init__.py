#!/usr/bin/env python3
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, send_file, send_from_directory, safe_join, request
from jinja2 import TemplateNotFound
app = Flask(__name__)

# Load config.py
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
db = SQLAlchemy(app)

app_tests = Flask(__name__)
app_tests.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
db_tests = SQLAlchemy(app_tests)



# Allows for any URL to be handled by AngularJS
# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(**kwargs):
    return send_file('index.html')

# Allows us to not have to rely on Flask's default directory structure
# http://stackoverflow.com/questions/23685687/flask-html-js-css-img-reference-404-error
@app.route('/<any(assets, vendors):folder>/<path:filename>')
def toplevel_static(folder, filename):
    filename = safe_join(folder, filename)
    cache_timeout = app.get_send_file_max_age(filename)
    return send_file(filename)

# The following are API calls

@app.route('/resources/players', methods=['GET','POST'])
def players_collection():
    """
    This will process the collection of players by filtering
    on the provided request arguments (within the HTTP Request
    object). Optimally we will handle this async.
    """
    if request.method == 'POST':
        return 'Not yet implemented.'

    # GET request:
    # So SQLAlchemy takes filter_by arguments for queries by dict,
    # so we can simply unpack the request params and pass them along
    # Since this isn't raw SQL we don't need to sanitize the request, 
    # it'll be handled internally.
    return flask.jsonify(db.Player.query.filter_by(**request.args))


@app.route('/resources/player/<name>')
def player_by_name(name):
    """
    This function will query the database for a given player
    by name, and optionally will further filter the data 
    based on the provided attribute request arguments (HTTP request
    object).
    """
    player_data = db.Player.query.filter_by(name = name);
    if player_data:
        return flask.jsonify(player_data)
    else:
        abort(404)


@app.route('/resources/teams', methods=['GET','POST'])
def teams_collection():
    """
    This function will query the database for all teams and 
    filter based on the provided HTTP Request arguments.
    """
    if request.method == 'POST':
        return 'Not yet implemented'

    # GET
    return flask.jsonify(db.Team.query.filter_by(**request.args))


@app.route('/resources/team/<team_name>')
def team_by_name(team_name):
    """
    This function will query the database for the team with 
    the given team_name and will further filter that request 
    based on optional parameters in the HTTP request object.
    """
    team_data = db.Team.query.filter_by(name = team_name)
    if team_data:
        return flask.jsonify(team_data)
    else:
        abort(404)

@app.route('/resources/team/<team_name>/schedule')
def team_schedule(team_name):
    """
    This function will return the schedule of games played
    by the team given by team_name.
    """
    
@app.route('/resources/team/<team_name>/top_starters')
def team_top_starters(team_name):
    """
    This function will return the top five players of given 
    team_name based on number of games started.
    """
    pass

@app.route('/resources/team/<team_name>/wins')
def team_wins(team_name):
    """
    Returns the list of games won by team_name
    """
    pass

@app.route('/resources/team/<team_name>/losses')
def team_losses(team_name):
    """
    Returns the list of games lost by team_name
    """
    pass

@app.route('/resources/games', methods=['GET','POST'])
def games_collection():
    """
    This function will return all games, filtered by the parameters
    provided in the HTTP request object.
    """
    pass

@app.route('/resources/game/<game_id>')
def game_by_id(game_id):
    """
    This function will return a game object by ID.
    """
    pass

@app.route('/resources/game/<month_id>')
def games_by_month(month_id):
    """
    This function will return all games played in a given month.
    """
    pass

@app.route('/resources/game/<site>')
def games_by_site(site):
    """
    This function will return all games played at a given arena.
    """
    pass

if __name__ == "__main__":
    app.debug = True
    app.run()
