import json
import cgi
from tests import TestAPI
import unittest
from io import StringIO

def makeJSON():
	
	result = {}
	suite = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
	testStream = StringIO()
	testStatus = unittest.TextTestRunner(stream=testStream, verbosity=2).run(suite)
	result['results'] = testStream.getvalue()
	result['status'] = str(testStatus)

	return json.dumps(result)
