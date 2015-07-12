from flask.ext.sqlalchemy import SQLAlchemy 
from sqlalchemy import or_, and_
from models import Player, Team, Game
import json

# Purposely avoiding pulling in Flask modules here
# in order to maintain some separation of concern

# -------------------
# Collection Handlers
# -------------------

def players_collection_handler(a):
    """
    Eventually we need to modify this to handle 
    Tuple rangers for numerical data sets.
    """
    return json.dumps([i.serialize for i in Player.query.filter_by(**a).all()])

def teams_collection_handler(a):
    return json.dumps([i.serialize for i in Team.query.filter_by(**a).all()])

def games_collection_handler(a):
    return json.sumps([i.serialize for i in Game.query.filter_by(**a).all()])

# ----------------
# Player Endpoints
# ----------------

def player_by_id_handler(id):
    data = Player.query.filter_by(id = id).first().serialize
    data["schedule"] = sorted(json.loads(team_schedule_handler(data["team_name"])), key=lambda k : k["date"])
    return json.dumps(data)

# --------------
# Team Endpoints
# --------------

def team_by_name_handler(tn):
    data = Team.query.filter_by(name = tn).first().serialize
    return json.dumps(data)

def team_schedule_handler(tn):
    return json.dumps([i.serialize for i in Game.query.filter(or_(Game.home_team == tn, Game.away_team == tn)).all()])

def team_top_starters_handler(tn):
    data = [i.serialize for i in Player.query.filter_by(team_name = tn).all()]
    data = sorted(data, key= lambda k: k['season_GS'], reverse=True)
    return json.dumps(data[:5])

def team_wins_handler(tn):
    return json.dumps([i.serialize for i in Game.query.filter(or_(and_(Game.home_team == tn, Game.home_score > Game.away_score), \
                                                                 (and_(Game.away_team == tn, Game.away_score > Game.home_score)))).all()])

def team_losses_handler(tn):
    return json.dumps([i.serialize for i in Game.query.filter(or_(and_(Game.home_team == tn, Game.home_score < Game.away_score), \
                                                                 (and_(Game.away_team == tn, Game.away_score < Game.home_score)))).all()])
# --------------
# Game Endpoints
# --------------

def game_by_id_handler(id):
    return json.dumps(Game.query.filter_by(id = id).first().serialize)

def game_by_month_handler(month_id):
    return json.dumps([])

def game_by_site_handler(site):
    site_team = Team.query.filter_by(site_name = site)
    return json.dumps([i.serialize for i in Game.query.filter_by(home_team = site_team["name"]).all()])




