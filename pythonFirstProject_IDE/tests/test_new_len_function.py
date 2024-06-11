import unittest

from src import new_len_function


class test_new_len_function(unittest.TestCase):

    def test_new_len_function(self):
        self.assertEqual(2, new_len_function("go"));

    def test_new_len_function(self):
        self.assertEqual(4, new_len_function("good"));

    def test_new_len_function(self):
        self.assertEqual(8, new_len_function("gambling"));

    def test_new_len_function(self):
        self.assertEqual(13, new_len_function("recalibration"));  #


