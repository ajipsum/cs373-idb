#!/usr/bin/env python3
from unittest import TestCase, main
from models_tests import Player, Team, Game, player_game, team_game
from flask import Flask
from __init__ import app, db_tests
import json
from urllib.request import urlopen

class TestAPI (TestCase) :
    # app = Flask(__name__)
    
    host = "http://127.0.0.1:5000/"

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

    def test_RESTful_team(self):
        url = urlopen(self.host + "resources/team/Heat")
        t = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))
        self.assertEqual(t["name"], "Heat") 
        self.assertEqual(t["conference"], "East")
        self.assertEqual(t["division"], "Southeast")
        self.assertEqual(t["site_name"], "AmericanAirlines Arena")
        self.assertEqual(t["city"], "Miami")
        self.assertEqual(t["state"], "Florida")
        self.assertEqual(t["mascot"], "Burnie")
        

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

    def test_RESTful_player(self):
        url = urlopen(self.host + "resources/player/341")
        p = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))
        self.assertEqual(p["name"], "Tim Duncan") 
        self.assertEqual(p["position"], "PF")
        self.assertEqual(p["player_number"], "21")
        self.assertEqual(p["current_team"], "San Antonio Spurs")
        self.assertEqual(p["age"], "39")
        self.assertEqual(p["weight"], "250")


    def test_game_create_1(self):
         game = Game(
             id = 21400102,
             home_team = "Los Angeles Clippers",
             home_score = "89",
             away_team = "San Antonio Spurs",
             away_score = "85",
             date = 1436832000,
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id='21400102').first()
         self.assertEqual(g.home_team, "Los Angeles Clippers") 
         self.assertEqual(g.home_score, "89")
         self.assertEqual(g.away_team, "San Antonio Spurs")
         self.assertEqual(g.away_score, "85")
         self.assertEqual(g.date, 1436832000)

    def test_game_create_2(self):
         game = Game(
             id = 21455555,
             home_team = "",
             home_score = "",
             away_team = "",
             away_score = "",
             date = None,
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id=21455555).first()
         self.assertEqual(g.home_team, "") 
         self.assertEqual(g.home_score, "")
         self.assertEqual(g.away_team, "")
         self.assertEqual(g.away_score, "")
         self.assertEqual(g.date, None)

    def test_game_create_3(self):
         game = Game(
             id = 21400559,
             home_team = "Los Angeles Clippers",
             home_score = "104",
             away_team = "Miami Heat",
             away_score = "90",
             date = 1420934400,
         )
         player = Player(
             name = "",
             position = "",
             player_number = "",
             current_team = "",
             age = "",
             weight = "",
         )
         db_tests.session.add(game)
         db_tests.session.commit()
         g = Game.query.filter_by(id=21400559).first()
         self.assertEqual(g.home_team, "Los Angeles Clippers") 
         self.assertEqual(g.home_score, "104")
         self.assertEqual(g.away_team, "Miami Heat")
         self.assertEqual(g.away_score, "90")
         self.assertEqual(g.date, 1420934400)

    def test_RESTful_game(self):
        url = urlopen(self.host + "resources/game/1151")
        g = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))
        self.assertEqual(g["home_team"], "Clippers") 
        self.assertEqual(g["home_score"], "104")
        self.assertEqual(g["away_team"], "Heat")
        self.assertEqual(g["away_score"], "90")
        self.assertEqual(g["date"], 1420952400000)


    def test_player_game_create_1(self):
        game = Game(
            id = 54,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        player = Player(
            id = 7979,
        )
        db_tests.session.add(player)
        db_tests.session.commit()
        db_tests.session.execute(player_game.insert().values([(7979, 54)]))
        db_tests.session.commit()
        pg = db_tests.session.query(player_game).filter_by(player_id=7979).first()
        self.assertEqual(pg.player_id, 7979) 
        self.assertEqual(pg.game_id, 54)

    def test_player_game_create_2(self):
        game = Game(
            id = 9999,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        player = Player(
            id = 88,
        )
        db_tests.session.add(player)
        db_tests.session.commit()
        db_tests.session.execute(player_game.insert().values([(88, 9999)]))
        db_tests.session.commit()
        pg = db_tests.session.query(player_game).filter_by(game_id=9999).first()
        self.assertEqual(pg.player_id, 88) 
        self.assertEqual(pg.game_id, 9999)

    def test_player_game_create_3(self):
        game = Game(
            id = 323,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        player = Player(
            id = 55,
        )
        db_tests.session.add(player)
        db_tests.session.commit()
        player = Player(
            id = 56,
        )
        db_tests.session.add(player)
        db_tests.session.commit()
        db_tests.session.execute(player_game.insert().values([(55, 323)]))
        db_tests.session.commit()
        db_tests.session.execute(player_game.insert().values([(56, 323)]))
        db_tests.session.commit()
        pg_list = db_tests.session.query(player_game).filter_by(game_id=323)
        self.assertEqual(pg_list[0].player_id, 55) 
        self.assertEqual(pg_list[0].game_id, 323)
        self.assertEqual(pg_list[1].player_id, 56) 
        self.assertEqual(pg_list[1].game_id, 323)


    def test_team_game_create_1(self):
        game = Game(
            id = 6767,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        team = Team(
            name = 'Flyers',
        )
        db_tests.session.add(team)
        db_tests.session.commit()
        db_tests.session.execute(team_game.insert().values([('Flyers', 6767)]))
        db_tests.session.commit()
        tg = db_tests.session.query(team_game).filter_by(team_name='Flyers').first()
        self.assertEqual(tg.team_name, 'Flyers') 
        self.assertEqual(tg.game_id, 6767)

    def test_team_game_create_2(self):
        game = Game(
            id = 6768,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        team = Team(
            name = 'Cinnamon Buns',
        )
        db_tests.session.add(team)
        db_tests.session.commit()
        db_tests.session.execute(team_game.insert().values([('Cinnamon Buns', 6768)]))
        db_tests.session.commit()
        tg = db_tests.session.query(team_game).filter_by(game_id=6768).first()
        self.assertEqual(tg.team_name, 'Cinnamon Buns') 
        self.assertEqual(tg.game_id, 6768)

    def test_team_game_create_3(self):
        game = Game(
            id = 7000,
        )
        db_tests.session.add(game)
        db_tests.session.commit()
        team = Team(
            name = 'Mozzarella Cheese',
        )
        db_tests.session.add(team)
        db_tests.session.commit()

        db_tests.session.add(game)
        db_tests.session.commit()
        team = Team(
            name = 'Bob',
        )
        db_tests.session.add(team)
        db_tests.session.commit()
        db_tests.session.execute(team_game.insert().values([('Mozzarella Cheese', 7000)]))
        db_tests.session.commit()
        db_tests.session.execute(team_game.insert().values([('Bob', 7000)]))
        db_tests.session.commit()
        tg_list = db_tests.session.query(team_game).filter_by(game_id=7000)
        self.assertEqual(tg_list[0].team_name, 'Mozzarella Cheese') 
        self.assertEqual(tg_list[0].game_id, 7000)
        self.assertEqual(tg_list[1].team_name, 'Bob') 
        self.assertEqual(tg_list[1].game_id, 7000)



if __name__ == '__main__':
    main()
