




from __init__ import db
from db_workaround import db_tests
import models, models_tests

# create db schema based on model
db.create_all()
db_tests.create_all()
print('Database schema created\n')