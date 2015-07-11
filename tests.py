#!/usr/bin/env python3
from unittest import TestCase, main
from models_tests import Player, Team, Game, player_game, team_game
from flask import Flask
from __init__ import app, db_tests

class TestAPI (TestCase) :
    # app = Flask(__name__)

    @classmethod
    def setUpClass(models):
        #database for testing
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
        # models.set_verbose(True)    
        db_tests.drop_all()
        db_tests.create_all()

    @classmethod
    def tearDownClass(models):
        db_tests.session.remove()
        db_tests.drop_all()

    def test_team_create_1(self):
        team = Team(
            name = "Spurs",
            conference = "West",
            division = "Southwest",
            site_name = "AT&T Center",
            city = "San Antonio",
            state = "Texas",
            mascot = "The Coyote",
        )
        db_tests.session.add(team)
        db_tests.session.commit()
        t = Team.query.filter_by(name='Spurs').first()
        self.assertEqual(t.name, "Spurs") 
        self.assertEqual(t.conference, "West")
        self.assertEqual(t.division, "Southwest")
        self.assertEqual(t.site_name, "AT&T Center")
        self.assertEqual(t.city, "San Antonio")
        self.assertEqual(t.state, "Texas")
        self.assertEqual(t.mascot, "The Coyote")

    def test_team_create_2(self):
         team = Team(
             name = "",
             conference = "",
             division = "",
             site_name = "",
             city = "",
             state = "",
             mascot = "",
         )
         db_tests.session.add(team)
         db_tests.session.commit()
         t = Team.query.filter_by(name='').first()
         self.assertEqual(t.name, "") 
         self.assertEqual(t.conference, "")
         self.assertEqual(t.division, "")
         self.assertEqual(t.site_name, "")
         self.assertEqual(t.city, "")
         self.assertEqual(t.state, "")
         self.assertEqual(t.mascot, "")

    def test_team_create_3(self):
         team = Team(
             name = "Heat",
             conference = "East",
             division = "Southeast",
             site_name = "AmericanAirlines Arena",
             city = "Miami",
             state = "Florida",
             mascot = "Burnie",
         )
         db_tests.session.add(team)
         db_tests.session.commit()
         t = Team.query.filter_by(name='Heat').first()
         self.assertEqual(t.name, "Heat") 
         self.assertEqual(t.conference, "East")
         self.assertEqual(t.division, "Southeast")
         self.assertEqual(t.site_name, "AmericanAirlines Arena")
         self.assertEqual(t.city, "Miami")
         self.assertEqual(t.state, "Florida")
         self.assertEqual(t.mascot, "Burnie")

    def test_player_create_1(self):
         player = Player(
             name = "Dwyane Wade",
             position = "SG",
             player_number = "3",
             current_team = "Miami Heat",
             age = "33",
             weight = "220",
         )
         db_tests.session.add(player)
         db_tests.session.commit()
         p = Player.query.filter_by(name='Dwyane Wade').first()
         self.assertEqual(p.name, "Dwyane Wade") 
         self.assertEqual(p.position, "SG")
         self.assertEqual(p.player_number, "3")
         self.assertEqual(p.current_team, "Miami Heat")
         self.assertEqual(p.age, "33")
         self.assertEqual(p.weight, "220")

    def test_player_create_2(self):
         player = Player(
             name = "",
             position = "",
             player_number = "",
             current_team = "",
             age = "",
             weight = "",
         )
         db_tests.session.add(player)
         db_tests.session.commit()
         p = Player.query.filter_by(name='').first()
         self.assertEqual(p.name, "") 
         self.assertEqual(p.position, "")
         self.assertEqual(p.player_number, "")
         self.assertEqual(p.current_team, "")
         self.assertEqual(p.age, "")
         self.assertEqual(p.weight, "")


    def test_player_create_3(self):
         player = Player(
             name = "Tim Duncan",
             position = "PF",
             player_number = "21",
             current_team = "San Antonio Spurs",
             age = "39",
             weight = "250",
         )
         db_tests.session.add(player)
         db_tests.session.commit()
         p = Player.query.filter_by(name='Tim Duncan').first()
         self.assertEqual(p.name, "Tim Duncan") 
         self.assertEqual(p.position, "PF")
         self.assertEqual(p.player_number, "21")
         self.assertEqual(p.current_team, "San Antonio Spurs")
         self.assertEqual(p.age, "39")
         self.assertEqual(p.weight, "250")


    def test_game_create_1(self):
         game = Game(
             id = 21400102,
             home_team = "Los Angeles Clippers",
             home_score = "89",
             away_team = "San Antonio Spurs",
             away_score = "85",
             date = "November 10, 2014",
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id='21400102').first()
         self.assertEqual(g.home_team, "Los Angeles Clippers") 
         self.assertEqual(g.home_score, "89")
         self.assertEqual(g.away_team, "San Antonio Spurs")
         self.assertEqual(g.away_score, "85")
         self.assertEqual(g.date, "November 10, 2014")

    def test_game_create_2(self):
         game = Game(
             id = 21455555,
             home_team = "",
             home_score = "",
             away_team = "",
             away_score = "",
             date = "",
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id=21455555).first()
         self.assertEqual(g.home_team, "") 
         self.assertEqual(g.home_score, "")
         self.assertEqual(g.away_team, "")
         self.assertEqual(g.away_score, "")
         self.assertEqual(g.date, "")

    def test_game_create_3(self):
         game = Game(
             id = 21400559,
             home_team = "Los Angeles Clippers",
             home_score = "104",
             away_team = "Miami Heat",
             away_score = "90",
             date = "January 11, 2015",
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id=21400559).first()
         self.assertEqual(g.home_team, "Los Angeles Clippers") 
         self.assertEqual(g.home_score, "104")
         self.assertEqual(g.away_team, "Miami Heat")
         self.assertEqual(g.away_score, "90")
         self.assertEqual(g.date, "January 11, 2015")

      def test_player_game_create_1(self):
         p_g = player_game(
             player_id = "",
             game_id = ""
         )
         db_tests.session.add(p_g)
         db_tests.session.commit()
         pg = player_game.query.filter_by(player_id='').first()
         self.assertEqual(pg.player_id, "") 
         self.assertEqual(pg.game_id "")

      def test_player_game_create_2(self):
         p_g = player_game(
             player_id = "45",
             game_id = "33"
         )
         db_tests.session.add(p_g)
         db_tests.session.commit()
         pg = player_game.query.filter_by(player_id='33').first()
         self.assertEqual(pg.player_id, "45") 
         self.assertEqual(pg.game_id "33")

      def test_player_game_create_3(self):
         p_g = player_game(
             player_id = "455",
             game_id = "331"
         )
         db_tests.session.add(p_g)
         db_tests.session.commit()
         p_g = player_game(
             player_id = "341",
             game_id = "331"
         )
         db_tests.session.add(p_g)
         db_tests.session.commit()
         pgs = player_game.query.filter_by(game_id='331')
         self.assertEqual(len(pgs) == 2)
         first_pg = pgs[0]
         self.assertEqual(first_pg.player_id, "455") 
         self.assertEqual(first_pg.game_id "331")
         second_pg = pgs[1]
         self.assertEqual(first_pg.player_id, "341") 
         self.assertEqual(first_pg.game_id "331")

     #  def test_team_game_create_1(self):
     #     player = Player(
     #         name = "Dwyane Wade",
     #         position = "SG",
     #         player_number = "3",
     #         current_team = "Miami Heat",
     #         age = "33",
     #         weight = "220",
     #     )
     #     db_tests.session.add(player)
     #     db_tests.session.commit()
     #     p = Player.query.filter_by(name='Dwyane Wade').first()
     #     self.assertEqual(p.name, "Dwyane Wade") 
     #     self.assertEqual(p.position, "SG")
     #     self.assertEqual(p.player_number, "3")
     #     self.assertEqual(p.current_team, "Miami Heat")
     #     self.assertEqual(p.age, "33")
     #     self.assertEqual(p.weight, "220")

     # def test_team_game_create_2(self):
     #     player = Player(
     #         name = "Dwyane Wade",
     #         position = "SG",
     #         player_number = "3",
     #         current_team = "Miami Heat",
     #         age = "33",
     #         weight = "220",
     #     )
     #     db_tests.session.add(player)
     #     db_tests.session.commit()
     #     p = Player.query.filter_by(name='Dwyane Wade').first()
     #     self.assertEqual(p.name, "Dwyane Wade") 
     #     self.assertEqual(p.position, "SG")
     #     self.assertEqual(p.player_number, "3")
     #     self.assertEqual(p.current_team, "Miami Heat")
     #     self.assertEqual(p.age, "33")
     #     self.assertEqual(p.weight, "220")

     # def test_team_game_create_3(self):
     #     player = Player(
     #         name = "Dwyane Wade",
     #         position = "SG",
     #         player_number = "3",
     #         current_team = "Miami Heat",
     #         age = "33",
     #         weight = "220",
     #     )
     #     db_tests.session.add(player)
     #     db_tests.session.commit()
     #     p = Player.query.filter_by(name='Dwyane Wade').first()
     #     self.assertEqual(p.name, "Dwyane Wade") 
     #     self.assertEqual(p.position, "SG")
     #     self.assertEqual(p.player_number, "3")
     #     self.assertEqual(p.current_team, "Miami Heat")
     #     self.assertEqual(p.age, "33")
     #     self.assertEqual(p.weight, "220")

if __name__ == '__main__':
    main()
