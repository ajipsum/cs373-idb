from flask.ext.sqlalchemy import SQLAlchemy 
from sqlalchemy import or_, and_
from models import Player, Team, Game
import json

# Purposely avoiding pulling in Flask modules here
# in order to maintain some separation of concern

def player_by_id_handler(id):
    data = Player.query.filter_by(id = id).first().serialize
    data["schedule"] = team_schedule_handler(data["team_name"]);
    return json.dumps(data)

def players_collection_handler(a):
    """
    Eventually we need to modify this to handle 
    Tuple rangers for numerical data sets.
    """
    return json.dumps([i.serialize for i in Player.query.filter_by(**a).all()])

def teams_collection_handler(a):
    return json.dumps([i.serialize for i in Team.query.filter_by(**a).all()])

def team_by_name_handler(tn):
    return json.dumps(Team.query.filter_by(name = tn).first().serialize)

def team_schedule_handler(tn):
    return json.dumps([i.serialize for i in Game.query.filter(or_(Game.home_team == tn, Game.away_team == tn)).all()])

def team_top_starters_handler(tn):
    data = [i.serialize for i in Player.query.filter_by(current_team = tn).all()]
    data = sorted(data, key='season_GS')
    return json.dumps(set(data[:5]))

def team_wins_handler(tn):
    return json.dumps([i.serialize for i in Games.query.filter(or_(and_(Game.home_team == tn, Game.home_score > Game.away_score), \
                                 (and_(Game.away_team == tn, Game.away_score > Game.home_score)))).all()])


