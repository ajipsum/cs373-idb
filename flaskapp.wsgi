#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/www/cs373-idb/")

from __init__ import app as application
application.secret_key = 'Add your secret key'
