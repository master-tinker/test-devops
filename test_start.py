import unittest
from start import app
import json

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def testBaa(self):
        res = self.app.get('/baa')
        data = json.loads(res.get_data(as_text=True))

        self.assertEqual(data,{'result': 'BAA!'})

        res = self.app.get('/baamoo')
        data = json.loads(res.get_data(as_text=True))

        self.assertEqual(data, {'result': 1})

    def testMoo(self):
        res = self.app.get('/moo')
        data = json.loads(res.get_data(as_text=True))

        self.assertEqual(data, {'result': 'MOO!'})

        res = self.app.get('/baamoo')
        data = json.loads(res.get_data(as_text=True))

        self.assertEqual(data, {'result': 0})