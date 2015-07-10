#!/usr/bin/env python3
# from unittest import TestCase, main
from models import Player, Team, Game, team_game, player_game
from flask import Flask
from __init__ import app, db
import json
import sys

def populate():

    db.session.remove()
    db.drop_all()
    db.create_all()


    players = None
    teams = None
    with open("../data/nba_players_data.json") as json_file:
        players = json.load(json_file)

    with open("../data/nbaTeams.json") as json_file:
        teams = json.load(json_file)

        



    i = 1
    # print(len(players))
    for player_name in players:
        player = players[player_name]
        player_career_stats = player['career_stats_avg_per_game']
        player_season_stats = player['stats_avg_per_game']
        # print(player['current_team'][player['current_team'].rfind(" ") + 1:])
        # sys.exit()
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
                team_name = player['current_team'][player['current_team'].rfind(" ") + 1:],
            )
        db.session.add(player_entry)
        db.session.commit()
        print(i)
        i += 1

    print("DONE WITH INSERTING PLAYER DATA")


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
