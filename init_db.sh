#!/bin/bash

mysql --user="root" --execute="CREATE USER 'api2k15'@'localhost'; GRANT ALL PRIVILEGES ON *.* TO 'api2k15'@'localhost';"
mysql --user="api2k15" --execute="CREATE DATABASE nba_flask_test;"


