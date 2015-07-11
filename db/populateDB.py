#!/usr/bin/env python3
# from unittest import TestCase, main
from models import Player, Team, Game, team_game, player_game
from flask import Flask
from __init__ import app, db
import json
import sys

players = None
teams = None
nbaGames = None
nbaGameStats = None
with open("../data/nba_players_data.json") as json_file:
    players = json.load(json_file)

with open("../data/nba_teams_data.json") as json_file:
    teams = json.load(json_file)

with open("../data/nbaGames_highlights.json") as json_file:
    nbaGames = json.load(json_file)

with open("../data/nbaTeamGameStats.json") as json_file:
    nbaGameStats = json.load(json_file)

def findGameStats(game_id, team_id):
    for v in nbaGameStats:
        if v['game_id'] == game_id and v['team_id'] == team_id:
            return v

def populate():

    db.session.remove()
    db.drop_all()
    db.create_all()


    # print(len(teams))
    # sys.exit()

    for team_id in teams:
        team = teams[team_id]
        team_entry = Team(
                name = team['last_name'],
                conference = team['conference'],
                division = team['division'],
                site_name = team['site_name'],
                city = team['city'],
                state = team['state'],
                mascot = team['mascot'],
                twitter = team['twitter'],
                citation = team['citation'],
            )
        db.session.add(team_entry)
        db.session.commit()


    # i = 1
    # print(len(players))
    for player_name in players:
        player = players[player_name]
        player_career_stats = player['career_stats_avg_per_game']
        player_season_stats = player['stats_avg_per_game']
        # print(type(player_season_stats))
        # print(player_name)
        # sys.exit()
        # print(player['current_team'][player['current_team'].rfind(" ") + 1:])
        # sys.exit()
        player_current_team = player['current_team'][player['current_team'].rfind(" ") + 1:]
        if(player_current_team == 'Blazers'):
            player_current_team = 'Trail Blazers'

        player_entry = Player(
                name = player_name,
                picture = player['picture'],
                experience_years = player['experience_years'],
                draft_info = player['draft_info'],
                position = player['position'],
                player_number = player['player_number'],
                current_team = player['current_team'],
                college = player['college'],
                birth_info = player['birth_info'],
                weight = player['weight'],
                twitter = player['twitter'],
                age = player['age'],
                youtube_link_1 = player['youtube_links'][0],
                youtube_link_2 = player['youtube_links'][1],
                youtube_link_3 = player['youtube_links'][2],
                career_GS = player_career_stats['career_GS'],
                career_REB = player_career_stats['career_REB'],
                career_BLK = player_career_stats['career_BLK'],
                career_FT_PCT = player_career_stats['career_FT%'],
                career_DR = player_career_stats['career_DR'],
                career_MIN = player_career_stats['career_MIN'],
                career_FG_PCT = player_career_stats['career_FG%'],
                career_3PM_A = player_career_stats['career_3PM-A'],
                career_OR = player_career_stats['career_OR'],
                career_FGM_A = player_career_stats['career_FGM-A'],
                career_STL = player_career_stats['career_STL'],
                career_TO = player_career_stats['career_TO'],
                career_3PM_PCT = player_career_stats['career_3P%'],
                career_AST = player_career_stats['career_AST'],
                career_GP = player_career_stats['career_GP'],
                career_PF = player_career_stats['career_PF'],
                career_PTS = player_career_stats['career_PTS'],
                CAREER_FTM_A = player_career_stats['career_FTM-A'],
                season_TO = player_season_stats['TO'],
                season_GS = player_season_stats['GS'],
                season_FG_PCT = player_season_stats['FG%'],
                season__PTS = player_season_stats['PTS'],
                season_OR = player_season_stats['OR'],
                season_GP = player_season_stats['GP'],
                season_PF = player_season_stats['PF'],
                season_REB = player_season_stats['REB'],
                season_FTM_A = player_season_stats['FTM-A'],
                season_BLK = player_season_stats['BLK'],
                season_MIN = player_season_stats['MIN'],
                season_STL = player_season_stats['STL'],
                season_AST = player_season_stats['AST'],
                season_FT_PCT = player_season_stats['FT%'],
                season_FGM_A = player_season_stats['FGM-A'],
                season_3P_PCT = player_season_stats['3P%'],
                season_DR = player_season_stats['DR'],
                season_3PM_A = player_season_stats['3PM-A'],
                citation = player['citation'],
                team_name = player_current_team,
            )
        db.session.add(player_entry)
        db.session.commit()
        # print(i)
        # i += 1

    i = 1
    for game_id in nbaGames:
        game = nbaGames[game_id]
        if game['season'] == '2014':
            home_team_stats = findGameStats(game['game_id'], game['home_id'])
            # print(home_team_stats)
            # sys.exit()
            away_team_stats = findGameStats(game['game_id'], game['away_id'])
            # print(away_team_stats)
            # sys.exit()

            # print("game id: " + game_id + "   home team " + str(game['home_id']) + "  away team: " + str(game['away_id']))
            if not home_team_stats == None:
                game_entry = Game(
                        home_team = teams[str(game['home_id'])]['last_name'],
                        away_team = teams[str(game['away_id'])]['last_name'],
                        date = game['date'],
                        home_score = game['home_score'],
                        away_score = game['away_score'],
                        home_box_fgm = home_team_stats['box_fgm'],
                        home_box_fga = home_team_stats['box_fga'],
                        home_box_fg3m = home_team_stats['box_fg3m'],
                        home_box_fg3a = home_team_stats['box_fg3a'],
                        home_box_ftm = home_team_stats['box_ftm'],
                        home_box_fta = home_team_stats['box_fta'],
                        home_box_oreb = home_team_stats['box_oreb'],
                        home_box_dreb = home_team_stats['box_dreb'],
                        home_box_ast = home_team_stats['box_ast'],
                        home_box_stl = home_team_stats['box_stl'],
                        home_box_blk = home_team_stats['box_blk'],
                        home_box_to = home_team_stats['box_to'],
                        home_box_pf = home_team_stats['box_pf'],
                        home_box_pts = home_team_stats['box_pts'],
                        home_box_plus_minus = home_team_stats['box_plus_minus'],
                        away_box_fgm = away_team_stats['box_fgm'],
                        away_box_fga = away_team_stats['box_fga'],
                        away_box_fg3m = away_team_stats['box_fg3m'],
                        away_box_fg3a = away_team_stats['box_fg3a'],
                        away_box_ftm = away_team_stats['box_ftm'],
                        away_box_fta = away_team_stats['box_fta'],
                        away_box_oreb = away_team_stats['box_oreb'],
                        away_box_dreb = away_team_stats['box_dreb'],
                        away_box_ast = away_team_stats['box_ast'],
                        away_box_stl = away_team_stats['box_stl'],
                        away_box_blk = away_team_stats['box_blk'],
                        away_box_to = away_team_stats['box_to'],
                        away_box_pf = away_team_stats['box_pf'],
                        away_box_pts = away_team_stats['box_pts'],
                        away_box_plus_minus = away_team_stats['box_plus_minus'],
                        youtube_link_1 = game['youtube_links'][0],
                        youtube_link_2 = game['youtube_links'][1],
                        youtube_link_3 = game['youtube_links'][2],
                )
                db.session.add(game_entry)
                db.session.commit()
        # print(i)
        i += 1


    #game to team relationship inserting
    games = Game.query.all()
    j = 1
    for game in games:
        home_team = game.home_team
        away_team = game.away_team
        # print(game.id)
        # sys.exit()
        # id_of_game = game.id
        # print(type(id_of_game))

        db.session.execute(team_game.insert().values([(home_team, game.id)]))
        db.session.commit()
        db.session.execute(team_game.insert().values([(away_team, game.id)]))
        db.session.commit()

        print(j)
        j += 1
        # team_game_entry = team_game(
        #         team_name = home_team,
        #         game_id = 5,
        #     )

        # db.session.add(team_game_entry)
        # db.session.commit()
        # team_game_entry_1 = team_game(
        #         team_name = away_team,
        #         game_id = 5,
        #     )
        # db.session.add(team_game_entry)
        # db.session.commit()
    print("DONE WITH INSERTING TEAM AND PLAYER DATA AND GAME DATA")

    #player to team relationship inserting
    b = 1
    for game in games:
        home_team = game.home_team
        away_team = game.away_team
        players_home = Team.query.filter_by(name=home_team).first().players
        for player in players_home:
            # print("player id: " + str(player.id) + "game id: " + str(game.id))
            # print(player.name)
            # print(b)
            # sys.exit()
            db.session.execute(player_game.insert().values([(player.id, game.id)]))
            db.session.commit()
        players_away = Team.query.filter_by(name=away_team).first().players
        for player in players_away:
            db.session.execute(player_game.insert().values([(player.id, game.id)]))
            db.session.commit()
        print(b)
        b += 1



# class TestAPI (TestCase) :
#     # app = Flask(__name__)

#     @classmethod
#     def setUpClass(models):
#         #database for testing
#         # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
#         # models.set_verbose(True)    
#         db.drop_all()
#         db.create_all()

#     @classmethod
#     def tearDownClass(models):
#         db.session.remove()
#         db.drop_all()

#     def test_team_create_1(self):
#         team = Team(
#             name = "Spurs",
#             conference = "West",
#             division = "Southwest",
#             site_name = "AT&T Center",
#             city = "San Antonio",
#             state = "Texas",
#             mascot = "The Coyote",
#         )
#         db.session.add(team)
#         db.session.commit()
#         t = Team.query.filter_by(name='Spurs').first()
#         self.assertEqual(t.name, "Spurs") 
#         self.assertEqual(t.conference, "West")
#         self.assertEqual(t.division, "Southwest")
#         self.assertEqual(t.site_name, "AT&T Center")
#         self.assertEqual(t.city, "San Antonio")
#         self.assertEqual(t.state, "Texas")
#         self.assertEqual(t.mascot, "The Coyote")

#     def test_team_create_2(self):
#          team = Team(
#              name = "",
#              conference = "",
#              division = "",
#              site_name = "",
#              city = "",
#              state = "",
#              mascot = "",
#          )
#          db.session.add(team)
#          db.session.commit()
#          t = Team.query.filter_by(name='').first()
#          self.assertEqual(t.name, "") 
#          self.assertEqual(t.conference, "")
#          self.assertEqual(t.division, "")
#          self.assertEqual(t.site_name, "")
#          self.assertEqual(t.city, "")
#          self.assertEqual(t.state, "")
#          self.assertEqual(t.mascot, "")

#     def test_team_create_3(self):
#          team = Team(
#              name = "Heat",
#              conference = "East",
#              division = "Southeast",
#              site_name = "AmericanAirlines Arena",
#              city = "Miami",
#              state = "Florida",
#              mascot = "Burnie",
#          )
#          db.session.add(team)
#          db.session.commit()
#          t = Team.query.filter_by(name='Heat').first()
#          self.assertEqual(t.name, "Heat") 
#          self.assertEqual(t.conference, "East")
#          self.assertEqual(t.division, "Southeast")
#          self.assertEqual(t.site_name, "AmericanAirlines Arena")
#          self.assertEqual(t.city, "Miami")
#          self.assertEqual(t.state, "Florida")
#          self.assertEqual(t.mascot, "Burnie")

#     def test_player_create_1(self):
#          player = Player(
#              name = "Dwyane Wade",
#              position = "SG",
#              player_number = "3",
#              current_team = "Miami Heat",
#              age = "33",
#              weight = "220",
#          )
#          db.session.add(player)
#          db.session.commit()
#          p = Player.query.filter_by(name='Dwyane Wade').first()
#          self.assertEqual(p.name, "Dwyane Wade") 
#          self.assertEqual(p.position, "SG")
#          self.assertEqual(p.player_number, "3")
#          self.assertEqual(p.current_team, "Miami Heat")
#          self.assertEqual(p.age, "33")
#          self.assertEqual(p.weight, "220")

#     def test_player_create_2(self):
#          player = Player(
#              name = "",
#              position = "",
#              player_number = "",
#              current_team = "",
#              age = "",
#              weight = "",
#          )
#          db.session.add(player)
#          db.session.commit()
#          p = Player.query.filter_by(name='').first()
#          self.assertEqual(p.name, "") 
#          self.assertEqual(p.position, "")
#          self.assertEqual(p.player_number, "")
#          self.assertEqual(p.current_team, "")
#          self.assertEqual(p.age, "")
#          self.assertEqual(p.weight, "")


#     def test_player_create_3(self):
#          player = Player(
#              name = "Tim Duncan",
#              position = "PF",
#              player_number = "21",
#              current_team = "San Antonio Spurs",
#              age = "39",
#              weight = "250",
#          )
#          db.session.add(player)
#          db.session.commit()
#          p = Player.query.filter_by(name='Tim Duncan').first()
#          self.assertEqual(p.name, "Tim Duncan") 
#          self.assertEqual(p.position, "PF")
#          self.assertEqual(p.player_number, "21")
#          self.assertEqual(p.current_team, "San Antonio Spurs")
#          self.assertEqual(p.age, "39")
#          self.assertEqual(p.weight, "250")


#     def test_game_create_1(self):
#          game = Game(
#              id = 21400102,
#              home_team = "Los Angeles Clippers",
#              home_score = "89",
#              away_team = "San Antonio Spurs",
#              away_score = "85",
#              date = "November 10, 2014",
#          )
#          db.session.add(game)
#          db.session.commit()
#          g = Game.query.filter_by(id='21400102').first()
#          self.assertEqual(g.home_team, "Los Angeles Clippers") 
#          self.assertEqual(g.home_score, "89")
#          self.assertEqual(g.away_team, "San Antonio Spurs")
#          self.assertEqual(g.away_score, "85")
#          self.assertEqual(g.date, "November 10, 2014")

#     def test_game_create_2(self):
#          game = Game(
#              id = 21455555,
#              home_team = "",
#              home_score = "",
#              away_team = "",
#              away_score = "",
#              date = "",
#          )
#          db.session.add(game)
#          db.session.commit()
#          g = Game.query.filter_by(id=21455555).first()
#          self.assertEqual(g.home_team, "") 
#          self.assertEqual(g.home_score, "")
#          self.assertEqual(g.away_team, "")
#          self.assertEqual(g.away_score, "")
#          self.assertEqual(g.date, "")

#     def test_game_create_3(self):
#          game = Game(
#              id = 21400559,
#              home_team = "Los Angeles Clippers",
#              home_score = "104",
#              away_team = "Miami Heat",
#              away_score = "90",
#              date = "January 11, 2015",
#          )
#          db.session.add(game)
#          db.session.commit()
#          g = Game.query.filter_by(id=21400559).first()
#          self.assertEqual(g.home_team, "Los Angeles Clippers") 
#          self.assertEqual(g.home_score, "104")
#          self.assertEqual(g.away_team, "Miami Heat")
#          self.assertEqual(g.away_score, "90")
#          self.assertEqual(g.date, "January 11, 2015")


if __name__ == '__main__':
    populate()
