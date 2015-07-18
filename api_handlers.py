from flask.ext.sqlalchemy import SQLAlchemy 
from sqlalchemy import or_, and_
from models import Player, Team, Game
import json
import datetime

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
    return json.dumps([i.serialize for i in Game.query.filter_by(**a).all()])

# ----------------
# Player Endpoints
# ----------------

def player_view_by_id_handler(id):
    data = Player.query.filter_by(id = id).first().serialize
    data["schedule"] = sorted(json.loads(team_schedule_handler(data["team_name"])), key=lambda k : k["date"], reverse=True)
    data["google_maps"] = Team.query.filter_by(name = data["team_name"]).first().google_maps
    return json.dumps(data)
    
def player_by_id_handler(id):
    return json.dumps(Player.query.filter_by(id = id).first().serialize)

# --------------
# Team Endpoints
# --------------

def team_view_by_name_handler(tn):
    data = Team.query.filter_by(name = tn).first().serialize
    data["schedule"] = sorted(json.loads(team_schedule_handler(tn)), key=lambda k : k["date"], reverse=True)
    data["players"] = sorted(data["players"], key=lambda k : k["name"])
    return json.dumps(data)

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

def game_view_by_id_handler(id):
    data = Game.query.filter_by(id = id).first().serialize
    home_team_obj = Team.query.filter_by(name = data["home_team"]).first()
    away_team_obj = Team.query.filter_by(name = data["away_team"]).first()
    data["citation"] = { "home" : home_team_obj.citation, "away" : away_team_obj.citation}
    data["roster"] = { "home" : sorted([i.serialize for i in home_team_obj.players], key= lambda k: k['name']), "away" : sorted([i.serialize for i in away_team_obj.players], key= lambda k: k['name'])}
    data["google_maps"] = home_team_obj.google_maps
    return json.dumps(data)

def game_by_id_handler(id):
    return json.dumps(Game.query.filter_by(id = id).first().serialize)

def game_by_month_handler(month_id):
    # This is probably a bad way to do this, I'm loading up ALL
    # games and then searching through because I have to reformat the 
    # date with the datetime object before I can compare against the 
    # month ID. Unfortunately I don't think there is a way to refine 
    # the query with this comparison since processing is needed on 
    # each object before the predicate can be evaluated, hence 
    # each object must be pulled from the database.
    games = Game.query
    games = filter(lambda g, m = month_id: datetime.datetime.fromtimestamp(int(g.date)).month == int(m), games)
    games = sorted(games, key=lambda g: g.date)
    return json.dumps([i.serialize for i in games])


def game_by_site_handler(site):
    site_team = Team.query.filter_by(site_name = site).first()
    return json.dumps([i.serialize for i in Game.query.filter_by(home_team = site_team.name).all()])

# --------------
# Search Handler
# --------------

def search_by_query(query):
    print("Hitting Search Query: " + query)
    teams_result   = Team.query.whoosh_search(query)
    games_result   = Game.query.whoosh_search(query)
    players_result = Player.query.whoosh_search(query)
    print("Team count: " + str(teams_result.count()))

    data = { 'results': {
                'teams'   : [i.serialize for i in teams_result],
                'games'   : [i.serialize for i in games_result],
                'players' : [i.serialize for i in players_result]
                }
            }

    return json.dumps(data);

