#!/bin/bash

export PATH=$PATH:/usr/local/mysql/bin
mysql --user="root" --execute="CREATE USER 'api2k15'@'localhost'; GRANT ALL PRIVILEGES ON *.* TO 'api2k15'@'localhost';"
mysql --user="api2k15" --execute="CREATE DATABASE nba_flask;"
mysql --user="api2k15" --execute="CREATE DATABASE nba_flask_test;"
mysql --user="root" --execute="SET @@global.innodb_large_prefix = 1;"


