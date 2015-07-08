#!/bin/bash

mysql -u root
CREATE USER 'api2k15'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'api2k15'@'localhost';
quit;
mysql -u api2k15
create database nba_flask_test;

