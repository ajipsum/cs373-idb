





#!/bin/bash

export PATH=$PATH:/usr/local/mysql/bin
mysql --user="root" --execute="CREATE USER 'api2k15'@'localhost'; GRANT ALL PRIVILEGES ON *.* TO 'api2k15'@'localhost';"
mysql --user="api2k15" --execute="set global innodb_file_per_table = ON;"
mysql --user="api2k15" --execute="set global innodb_file_format = BARRACUDA;"
mysql --user="api2k15" --execute="set GLOBAL innodb_large_prefix=ON;"
mysql --user="api2k15" --execute="CREATE DATABASE nba_flask;"
mysql --user="api2k15" --execute="CREATE DATABASE nba_flask_test;"


