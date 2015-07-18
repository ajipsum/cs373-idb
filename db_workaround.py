from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app_tests = Flask(__name__)
app_tests.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://api2k15:@127.0.0.1:3306/nba_flask_test'
app_tests.config['WHOOSH_BASE'] = 'path/to/whoosh/base'
db_tests = SQLAlchemy(app_tests)