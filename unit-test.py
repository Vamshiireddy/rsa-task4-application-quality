import unittest
from api import app
import api

class TestApp(unittest.TestCase):

	def setUp(self):
		self.app_context = app.app_context()
		self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def test_hello(self):
		self.assertEqual(api.hello_world(), "Hello, World!")

	def test_low_num(self):
		json_response = api.low_or_high("1").json
		self.assertEqual(json_response['value'], "low")

	def test_high_num(self):
		json_response = api.low_or_high("101").json
		self.assertEqual(json_response['value'], "high")

	def test_equal_num(self):
		json_response = api.low_or_high("100").json
		self.assertEqual(json_response['value'], "equal")

if __name__ == '__main__':
	unittest.main()