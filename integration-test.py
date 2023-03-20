from api import app
from unittest import TestCase
import unittest
import sys

class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
    	response = self.app.get('/')
    	self.assertEqual(response.get_data().decode(sys.getdefaultencoding()), "Hello, World!")

    def test_low_number(self):
    	response = self.app.get('/1').json
    	self.assertEqual(response['value'], "low")

    def test_high_number(self):
    	response = self.app.get('/101').json
    	self.assertEqual(response['value'], "high")

    def test_equal_number(self):
    	response = self.app.get('/100').json
    	self.assertEqual(response['value'], "equal")

if __name__ == '__main__':
	unittest.main()