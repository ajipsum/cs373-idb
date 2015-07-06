#!/usr/bin/env python3
from unittest import TestCase, main
from models import Player, Team, Game
from flask import Flask
from __init__ import app, db

class TestAPI (TestCase) :
    app = Flask(__name__)

    @classmethod
    def setUpClass(models):
        #database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
        # models.set_verbose(True)    
        db.drop_all()
        db.create_all()

    @classmethod
    def tearDownClass(models):
        db.session.remove()
        db.drop_all()

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
        db.session.add(team)
        db.session.commit()
        t = Team.query.filter_by(name='Spurs').first()
        assertEqual(t.name, "Spurs") 
        assertEqual(t.conference, "West")
        assertEqual(t.division, "Southwest")
        assertEqual(t.site_name, "AT&T Center")
        assertEqual(t.city, "San Antonio")
        assertEqual(t.state, "Texas")
        assertEqual(t.mascot, "The Coyote")

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
         db.session.add(team)
         db.session.commit()
         t = Team.query.filter_by(name='').first()
         assertEqual(t.name, "") 
         assertEqual(t.conference, "")
         assertEqual(t.division, "")
         assertEqual(t.site_name, "")
         assertEqual(t.city, "")
         assertEqual(t.state, "")
         assertEqual(t.mascot, "")

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
         db.session.add(team)
         db.session.commit()
         t = Team.query.filter_by(name='Heat').first()
         assertEqual(t.name, "Heat") 
         assertEqual(t.conference, "East")
         assertEqual(t.division, "Southeast")
         assertEqual(t.site_name, "AmericanAirlines Arena")
         assertEqual(t.city, "Miami")
         assertEqual(t.state, "Florida")
         assertEqual(t.mascot, "Burnie")

    def test_player_create_1(self):
         player = Player(
             name = "Dwyane Wade",
             position = "SG",
             player_number = "3",
             current_team = "Miami Heat",
             age = "33",
             weight = "220",
         )
         db.session.add(player)
         db.session.commit()
         p = Player.query.filter_by(name='Dwyane Wade').first()
         assertEqual(p.name, "Dwyane Wade") 
         assertEqual(p.position, "SG")
         assertEqual(p.player_number, "3")
         assertEqual(p.current_team, "Miami Heat")
         assertEqual(p.age, "33")
         assertEqual(p.weight, "220")

    def test_player_create_2(self):
         player = Player(
             name = "",
             position = "",
             player_number = "",
             current_team = "",
             age = "",
             weight = "",
         )
         db.session.add(player)
         db.session.commit()
         p = Player.query.filter_by(name='').first()
         assertEqual(p.name, "") 
         assertEqual(p.position, "")
         assertEqual(p.player_number, "")
         assertEqual(p.current_team, "")
         assertEqual(p.age, "")
         assertEqual(p.weight, "")

    def test_player_create_3(self):
         player = Player(
             name = "Tim Duncan",
             position = "PF",
             player_number = "21",
             current_team = "San Antonio Spurs",
             age = "39",
             weight = "250",
         )
         db.session.add(player)
         db.session.commit()
         p = Player.query.filter_by(name='Tim Duncan').first()
         assertEqual(p.name, "Tim Duncan") 
         assertEqual(p.position, "PF")
         assertEqual(p.player_number, "21")
         assertEqual(p.current_team, "San Antonio Spurs")
         assertEqual(p.age, "39")
         assertEqual(p.weight, "250")

    def test_game_create_1(self):
         game = Game(
             id = "21400102",
             home_team = "Los Angeles Clippers",
             home_score = "89",
             away_team = "San Antonio Spurs",
             away_score = "85",
             date = "November 10, 2014",
         )
         db.session.add(game)
         db.session.commit()
         g = Game.query.filter_by(id='21400102').first()
         assertEqual(g.home_team, "Los Angeles Clippers") 
         assertEqual(g.home_score, "89")
         assertEqual(g.away_team, "San Antonio Spurs")
         assertEqual(g.away_score, "85")
         assertEqual(g.date, "November 10, 2014")

    def test_game_create_2(self):
         game = Game(
             id = "",
             home_team = "",
             home_score = "",
             away_team = "",
             away_score = "",
             date = "",
         )
         db.session.add(game)
         db.session.commit()
         g = Game.query.filter_by(id='').first()
         assertEqual(g.home_team, "") 
         assertEqual(g.home_score, "")
         assertEqual(g.away_team, "")
         assertEqual(g.away_score, "")
         assertEqual(g.date, "")

    def test_game_create_3(self):
         game = Game(
             id = "21400559",
             home_team = "Los Angeles Clippers",
             home_score = "104",
             away_team = "Miami Heat",
             away_score = "90",
             date = "January 11, 2015",
         )
         db.session.add(game)
         db.session.commit()
         g = Game.query.filter_by(id='21400559').first()
         assertEqual(g.home_team, "Los Angeles Clippers") 
         assertEqual(g.home_score, "104")
         assertEqual(g.away_team, "Miami Heat")
         assertEqual(g.away_score, "90")
         assertEqual(g.date, "January 11, 2015")


if __name__ == '__main__':
    main()
