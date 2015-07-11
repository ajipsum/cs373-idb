from flask.ext.sqlalchemy import SQLAlchemy
from models import Player, Team, Game

# Purposely avoiding pulling in Flask modules here
# in order to maintain some separation of concern

def player_by_name_handler(name):
    return Player.query.filter_by(name = name).all()



def players_collection_handler(a):
    """
    Eventually we need to modify this to handle 
    Tuple rangers for numerical data sets.
    """
    return Player.query.filter_by(**a).all()

def teams_collection_handler(a):
    return Team.query.filter_by(**a).all()

def team_by_name_handler(tn):
    return Team.query.filter_by(name = tn)

def team_schedule_handler(tn):
    return Game.filter(_or(home_team == tn, away_team == tn))


