from __init__ import db
from sqlalchemy.dialects.mysql import BIGINT
import flask.ext.whooshalchemy


class Player(db.Model):
  '''
  Information about player
  Information includes name, picture, position, player number, weight etc.
  '''

  __searchable__ = ['id', 'name', 'picture', 'experience_years', 'draft_info', 'position', 'player_number', 'current_team', 'college', 'birth_info', 'weight', 'twitter', 'age', 'team_name']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified

  id = db.Column(db.Integer, primary_key=True,unique=True,index=True)
  name = db.Column(db.String(256))
  picture = db.Column(db.String(256), unique=True)
  experience_years = db.Column(db.String(256))
  draft_info = db.Column(db.String(256))
  position = db.Column(db.String(256))
  player_number = db.Column(db.String(256))
  current_team = db.Column(db.String(256))
  college = db.Column(db.String(256))
  birth_info = db.Column(db.String(256))
  weight = db.Column(db.String(256))
  twitter = db.Column(db.String(256))
  age = db.Column(db.String(256))
  youtube_link_1 = db.Column(db.String(256))
  youtube_link_2 = db.Column(db.String(256))
  youtube_link_3 = db.Column(db.String(256))
  career_GS = db.Column(db.String(256))
  career_REB = db.Column(db.String(256))
  career_BLK = db.Column(db.String(256))
  career_FT_PCT = db.Column(db.String(256))
  career_DR = db.Column(db.String(256))
  career_MIN = db.Column(db.String(256))
  career_FG_PCT = db.Column(db.String(256))
  career_3PM_A = db.Column(db.String(256))
  career_OR = db.Column(db.String(256))
  career_FGM_A = db.Column(db.String(256))
  career_STL = db.Column(db.String(256))
  career_TO = db.Column(db.String(256))
  career_3PM_PCT = db.Column(db.String(256))
  career_AST = db.Column(db.String(256))
  career_GP = db.Column(db.String(256))
  career_PF = db.Column(db.String(256))
  career_PTS = db.Column(db.String(256))
  CAREER_FTM_A = db.Column(db.String(256))
  season_TO = db.Column(db.String(256))
  season_GS = db.Column(db.String(256))
  season_FG_PCT = db.Column(db.String(256))
  season__PTS = db.Column(db.String(256))
  season_OR = db.Column(db.String(256))
  season_GP = db.Column(db.String(256))
  season_PF = db.Column(db.String(256))
  season_REB = db.Column(db.String(256))
  season_FTM_A = db.Column(db.String(256))
  season_BLK = db.Column(db.String(256))
  season_MIN = db.Column(db.String(256))
  season_STL = db.Column(db.String(256))
  season_AST = db.Column(db.String(256))
  season_FT_PCT = db.Column(db.String(256))
  season_FGM_A = db.Column(db.String(256))
  season_3P_PCT = db.Column(db.String(256))
  season_DR = db.Column(db.String(256))
  season_3PM_A = db.Column(db.String(256))
  citation = db.Column(db.String(256))
  team_name = db.Column(db.String(256), db.ForeignKey('team.name'))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


  @property 
  def serialize(self) :
      return {
            "id" : self.id,  
            "name" : self.name, 
            "picture" : self.picture, 
            "experience_years" : self.experience_years, 
            "draft_info" : self.draft_info, 
            "position" : self.position, 
            "player_number" : self.player_number, 
            "current_team" : self.current_team, 
            "college" : self.college, 
            "birth_info" : self.birth_info, 
            "weight" : self.weight, 
            "twitter" : self.twitter, 
            "age" : self.age, 
            "youtube_link_1" : self.youtube_link_1, 
            "youtube_link_2" : self.youtube_link_2, 
            "youtube_link_3" : self.youtube_link_3, 
            "career_GS" : self.career_GS, 
            "career_REB" : self.career_REB, 
            "career_BLK" : self.career_BLK, 
            "career_FT_PCT" : self.career_FT_PCT, 
            "career_DR" : self.career_DR, 
            "career_MIN" : self.career_MIN, 
            "career_FG_PCT" : self.career_FG_PCT, 
            "career_3PM_A" : self.career_3PM_A, 
            "career_OR" : self.career_OR, 
            "career_FGM_A" : self.career_FGM_A, 
            "career_STL" : self.career_STL, 
            "career_TO" : self.career_TO, 
            "career_3PM_PCT" : self.career_3PM_PCT, 
            "career_AST" : self.career_AST, 
            "career_GP" : self.career_GP, 
            "career_PF" : self.career_PF, 
            "career_PTS" : self.career_PTS, 
            "CAREER_FTM_A" : self.CAREER_FTM_A, 
            "season_TO" : self.season_TO, 
            "season_GS" : self.season_GS, 
            "season_FG_PCT" : self.season_FG_PCT, 
            "season__PTS" : self.season__PTS, 
            "season_OR" : self.season_OR, 
            "season_GP" : self.season_GP, 
            "season_PF" : self.season_PF, 
            "season_REB" : self.season_REB, 
            "season_FTM_A" : self.season_FTM_A, 
            "season_BLK" : self.season_BLK, 
            "season_MIN" : self.season_MIN, 
            "season_STL" : self.season_STL, 
            "season_AST" : self.season_AST, 
            "season_FT_PCT" : self.season_FT_PCT, 
            "season_FGM_A" : self.season_FGM_A, 
            "season_3P_PCT" : self.season_3P_PCT, 
            "season_DR" : self.season_DR, 
            "season_3PM_A" : self.season_3PM_A, 
            "citation" : self.citation, 
            "team_name" : self.team_name, 
            }


class Team(db.Model):
  '''
  Information about Team 
  Information includes name, conference, division, site_name, city, state, mascot
  '''
  __searchable__ = ['name', 'conference', 'division', 'site_name', 'city', 'state', 'mascot', 'twitter', 'google_maps']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified
  players = db. relationship('Player', backref='team', lazy='dynamic')
  name = db.Column(db.String(256), primary_key=True)
  conference = db.Column(db.String(256))
  division = db.Column(db.String(256))
  site_name = db.Column(db.String(256))
  city = db.Column(db.String(256))
  state = db.Column(db.String(256))
  mascot = db.Column(db.String(256))
  twitter = db.Column(db.String(256))
  citation = db.Column(db.String(256))
  google_maps = db.Column(db.String(256))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


  @property
  def serialize(self):
      return {
            "players" : [i.serialize for i in self.players], 
            "name" : self.name, 
            "conference" : self.conference, 
            "division" : self.division, 
            "site_name" : self.site_name, 
            "city" : self.city, 
            "state" : self.state, 
            "mascot" : self.mascot, 
            "twitter" : self.twitter, 
            "citation" : self.citation, 
            "google_maps" : self.google_maps,
        }

team_game = db.Table('team_game',
  db.Column('team_name', db.String(256), db.ForeignKey('team.name')),
  db.Column('game_id', db.Integer, db.ForeignKey('game.id')), mysql_engine='InnoDB', mysql_charset='utf8', mysql_row_format='dynamic'
)

player_game = db.Table('player_game',
  db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
  db.Column('game_id', db.Integer, db.ForeignKey('game.id')), mysql_engine='InnoDB', mysql_charset='utf8', mysql_row_format='dynamic'
)

class Game(db.Model):
  '''
  Information about Game
  Information include home_team, away_team, data, home_score, away_score, etc.
  '''

  __searchable__ = ['id', 'home_team', 'away_team', 'date_string', 'home_score', 'away_score']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified
  id = db.Column(db.Integer, primary_key=True,unique=True,index=True)
  home_team = db.Column(db.String(256))
  away_team = db.Column(db.String(256))
  date = db.Column(BIGINT(unsigned=True))
  date_string = db.Column(db.String(256))
  home_score = db.Column(db.String(256))
  away_score = db.Column(db.String(256))
  home_box_fgm = db.Column(db.String(256))
  home_box_fga = db.Column(db.String(256))
  home_box_fg3m = db.Column(db.String(256))
  home_box_fg3a = db.Column(db.String(256))
  home_box_ftm = db.Column(db.String(256))
  home_box_fta = db.Column(db.String(256))
  home_box_oreb = db.Column(db.String(256))
  home_box_dreb = db.Column(db.String(256))
  home_box_ast = db.Column(db.String(256))
  home_box_stl = db.Column(db.String(256))
  home_box_blk = db.Column(db.String(256))
  home_box_to = db.Column(db.String(256))
  home_box_pf = db.Column(db.String(256))
  home_box_pts = db.Column(db.String(256))
  home_box_plus_minus = db.Column(db.String(256))
  away_box_fgm = db.Column(db.String(256))
  away_box_fga = db.Column(db.String(256))
  away_box_fg3m = db.Column(db.String(256))
  away_box_fg3a = db.Column(db.String(256))
  away_box_ftm = db.Column(db.String(256))
  away_box_fta = db.Column(db.String(256))
  away_box_oreb = db.Column(db.String(256))
  away_box_dreb = db.Column(db.String(256))
  away_box_ast = db.Column(db.String(256))
  away_box_stl = db.Column(db.String(256))
  away_box_blk = db.Column(db.String(256))
  away_box_to = db.Column(db.String(256))
  away_box_pf = db.Column(db.String(256))
  away_box_pts = db.Column(db.String(256))
  away_box_plus_minus = db.Column(db.String(256))
  youtube_link_1 = db.Column(db.String(256))
  youtube_link_2 = db.Column(db.String(256))
  youtube_link_3 = db.Column(db.String(256))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


  @property
  def serialize(self):
      return {

        "id" : self.id, 
        "home_team" : self.home_team, 
        "away_team" : self.away_team, 
        "date" : self.date, 
        "home_score" : self.home_score, 
        "away_score" : self.away_score, 
        "home_box_fgm" : self.home_box_fgm, 
        "home_box_fga" : self.home_box_fga, 
        "home_box_fg3m" : self.home_box_fg3m, 
        "home_box_fg3a" : self.home_box_fg3a, 
        "home_box_ftm" : self.home_box_ftm, 
        "home_box_fta" : self.home_box_fta, 
        "home_box_oreb" : self.home_box_oreb, 
        "home_box_dreb" : self.home_box_dreb, 
        "home_box_ast" : self.home_box_ast, 
        "home_box_stl" : self.home_box_stl, 
        "home_box_blk" : self.home_box_blk, 
        "home_box_to" : self.home_box_to, 
        "home_box_pf" : self.home_box_pf, 
        "home_box_pts" : self.home_box_pts, 
        "home_box_plus_minus" : self.home_box_plus_minus, 
        "away_box_fgm" : self.away_box_fgm, 
        "away_box_fga" : self.away_box_fga, 
        "away_box_fg3m" : self.away_box_fg3m, 
        "away_box_fg3a" : self.away_box_fg3a, 
        "away_box_ftm" : self.away_box_ftm, 
        "away_box_fta" : self.away_box_fta, 
        "away_box_oreb" : self.away_box_oreb, 
        "away_box_dreb" : self.away_box_dreb, 
        "away_box_ast" : self.away_box_ast, 
        "away_box_stl" : self.away_box_stl, 
        "away_box_blk" : self.away_box_blk, 
        "away_box_to" : self.away_box_to, 
        "away_box_pf" : self.away_box_pf, 
        "away_box_pts" : self.away_box_pts, 
        "away_box_plus_minus" : self.away_box_plus_minus, 
        "youtube_link_1" : self.youtube_link_1, 
        "youtube_link_2" : self.youtube_link_2, 
        "youtube_link_3" : self.youtube_link_3, 
        }
  #many to many team game relationship
  team_game = db.relationship('Team', secondary=team_game,
    backref=db.backref('games', lazy='dynamic'))

  #many to many player game relationship
  player_game = db.relationship('Player', secondary=player_game,
    backref=db.backref('games', lazy='dynamic'))
