from db_workaround import db_tests
from sqlalchemy.dialects.mysql import BIGINT
import flask.ext.whooshalchemy

class Player(db_tests.Model):
  '''
  Information about player
  Information includes name, picture, position, player number, weight etc.
  '''

  __searchable__ = ['id', 'name', 'picture', 'experience_years', 'draft_info', 'position', 'player_number', 'current_team', 'college', 'birth_info', 'weight', 'twitter', 'age', 'team_name']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified
  id = db_tests.Column(db_tests.Integer, primary_key=True,unique=True,index=True)
  name = db_tests.Column(db_tests.String(256))
  picture = db_tests.Column(db_tests.String(256), unique=True)
  experience_years = db_tests.Column(db_tests.String(256))
  draft_info = db_tests.Column(db_tests.String(256))
  position = db_tests.Column(db_tests.String(256))
  player_number = db_tests.Column(db_tests.String(256))
  current_team = db_tests.Column(db_tests.String(256))
  college = db_tests.Column(db_tests.String(256))
  birth_info = db_tests.Column(db_tests.String(256))
  weight = db_tests.Column(db_tests.String(256))
  twitter = db_tests.Column(db_tests.String(256))
  age = db_tests.Column(db_tests.String(256))
  youtube_link_1 = db_tests.Column(db_tests.String(256))
  youtube_link_2 = db_tests.Column(db_tests.String(256))
  youtube_link_3 = db_tests.Column(db_tests.String(256))
  career_GS = db_tests.Column(db_tests.String(256))
  career_REB = db_tests.Column(db_tests.String(256))
  career_BLK = db_tests.Column(db_tests.String(256))
  career_FT_PCT = db_tests.Column(db_tests.String(256))
  career_DR = db_tests.Column(db_tests.String(256))
  career_MIN = db_tests.Column(db_tests.String(256))
  career_FG_PCT = db_tests.Column(db_tests.String(256))
  career_3PM_A = db_tests.Column(db_tests.String(256))
  career_OR = db_tests.Column(db_tests.String(256))
  career_FGM_A = db_tests.Column(db_tests.String(256))
  career_STL = db_tests.Column(db_tests.String(256))
  career_TO = db_tests.Column(db_tests.String(256))
  career_3PM_PCT = db_tests.Column(db_tests.String(256))
  career_AST = db_tests.Column(db_tests.String(256))
  career_GP = db_tests.Column(db_tests.String(256))
  career_PF = db_tests.Column(db_tests.String(256))
  career_PTS = db_tests.Column(db_tests.String(256))
  CAREER_FTM_A = db_tests.Column(db_tests.String(256))
  season_TO = db_tests.Column(db_tests.String(256))
  season_GS = db_tests.Column(db_tests.String(256))
  season_FG_PCT = db_tests.Column(db_tests.String(256))
  season__PTS = db_tests.Column(db_tests.String(256))
  season_OR = db_tests.Column(db_tests.String(256))
  season_GP = db_tests.Column(db_tests.String(256))
  season_PF = db_tests.Column(db_tests.String(256))
  season_REB = db_tests.Column(db_tests.String(256))
  season_FTM_A = db_tests.Column(db_tests.String(256))
  season_BLK = db_tests.Column(db_tests.String(256))
  season_MIN = db_tests.Column(db_tests.String(256))
  season_STL = db_tests.Column(db_tests.String(256))
  season_AST = db_tests.Column(db_tests.String(256))
  season_FT_PCT = db_tests.Column(db_tests.String(256))
  season_FGM_A = db_tests.Column(db_tests.String(256))
  season_3P_PCT = db_tests.Column(db_tests.String(256))
  season_DR = db_tests.Column(db_tests.String(256))
  season_3PM_A = db_tests.Column(db_tests.String(256))
  citation = db_tests.Column(db_tests.String(256))
  team_name = db_tests.Column(db_tests.String(256), db_tests.ForeignKey('team.name'))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


class Team(db_tests.Model):
  '''
  Information about Team 
  Information includes name, conference, division, site_name, city, state, mascot
  '''

  __searchable__ = ['name', 'conference', 'division', 'site_name', 'city', 'state', 'mascot', 'twitter', 'google_maps']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified
  players = db_tests.relationship('Player', backref='team', lazy='dynamic')
  name = db_tests.Column(db_tests.String(256), primary_key=True,unique=True,index=True)
  conference = db_tests.Column(db_tests.String(256))
  division = db_tests.Column(db_tests.String(256))
  site_name = db_tests.Column(db_tests.String(256))
  city = db_tests.Column(db_tests.String(256))
  state = db_tests.Column(db_tests.String(256))
  mascot = db_tests.Column(db_tests.String(256))
  twitter = db_tests.Column(db_tests.String(256))
  citation = db_tests.Column(db_tests.String(256))
  google_maps = db_tests.Column(db_tests.String(256))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


team_game = db_tests.Table('team_game',
  db_tests.Column('team_name', db_tests.String(256), db_tests.ForeignKey('team.name')),
  db_tests.Column('game_id', db_tests.Integer, db_tests.ForeignKey('game.id')), mysql_engine='InnoDB', mysql_charset='utf8', mysql_row_format='dynamic'
)

player_game = db_tests.Table('player_game',
  db_tests.Column('player_id', db_tests.Integer, db_tests.ForeignKey('player.id')),
  db_tests.Column('game_id', db_tests.Integer, db_tests.ForeignKey('game.id')), mysql_engine='InnoDB', mysql_charset='utf8', mysql_row_format='dynamic'
)

class Game(db_tests.Model):
  '''
  Information about Game
  Information include home_team, away_team, data, home_score, away_score, etc.
  '''

  __searchable__ = ['id', 'home_team', 'away_team', 'home_score', 'away_score']  # these fields will be indexed by whoosh
  # __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified
  id = db_tests.Column(db_tests.Integer, primary_key=True)
  home_team = db_tests.Column(db_tests.String(256))
  away_team = db_tests.Column(db_tests.String(256))
  date = db_tests.Column(BIGINT(unsigned=True))
  home_score = db_tests.Column(db_tests.String(256))
  away_score = db_tests.Column(db_tests.String(256))
  home_box_fgm = db_tests.Column(db_tests.String(256))
  home_box_fga = db_tests.Column(db_tests.String(256))
  home_box_fg3m = db_tests.Column(db_tests.String(256))
  home_box_fg3a = db_tests.Column(db_tests.String(256))
  home_box_ftm = db_tests.Column(db_tests.String(256))
  home_box_fta = db_tests.Column(db_tests.String(256))
  home_box_oreb = db_tests.Column(db_tests.String(256))
  home_box_dreb = db_tests.Column(db_tests.String(256))
  home_box_ast = db_tests.Column(db_tests.String(256))
  home_box_stl = db_tests.Column(db_tests.String(256))
  home_box_blk = db_tests.Column(db_tests.String(256))
  home_box_to = db_tests.Column(db_tests.String(256))
  home_box_pf = db_tests.Column(db_tests.String(256))
  home_box_pts = db_tests.Column(db_tests.String(256))
  home_box_plus_minus = db_tests.Column(db_tests.String(256))
  away_box_fgm = db_tests.Column(db_tests.String(256))
  away_box_fga = db_tests.Column(db_tests.String(256))
  away_box_fg3m = db_tests.Column(db_tests.String(256))
  away_box_fg3a = db_tests.Column(db_tests.String(256))
  away_box_ftm = db_tests.Column(db_tests.String(256))
  away_box_fta = db_tests.Column(db_tests.String(256))
  away_box_oreb = db_tests.Column(db_tests.String(256))
  away_box_dreb = db_tests.Column(db_tests.String(256))
  away_box_ast = db_tests.Column(db_tests.String(256))
  away_box_stl = db_tests.Column(db_tests.String(256))
  away_box_blk = db_tests.Column(db_tests.String(256))
  away_box_to = db_tests.Column(db_tests.String(256))
  away_box_pf = db_tests.Column(db_tests.String(256))
  away_box_pts = db_tests.Column(db_tests.String(256))
  away_box_plus_minus = db_tests.Column(db_tests.String(256))
  youtube_link_1 = db_tests.Column(db_tests.String(256))
  youtube_link_2 = db_tests.Column(db_tests.String(256))
  youtube_link_3 = db_tests.Column(db_tests.String(256))
  __table_args__ = {'mysql_engine':'InnoDB', 'mysql_charset':'utf8', 'mysql_row_format':'dynamic'}


  #many to many team game relationship
  team_game = db_tests.relationship('Team', secondary=team_game,
    backref=db_tests.backref('games', lazy='dynamic'))

  #many to many player game relationship
  player_game = db_tests.relationship('Player', secondary=player_game,
    backref=db_tests.backref('games', lazy='dynamic'))
