#!/bin/bash

mysql -u root
CREATE USER 'api2k15'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'api2k15'@'localhost';
create database nba_flask_test;

