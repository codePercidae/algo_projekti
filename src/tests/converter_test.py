import unittest
import os
from converter import Converter

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.c = Converter()
        self.dir_name = os.path.dirname(__file__)

    def test_reset_sets_note_to_int_relation_back(self):
        self.c.notes_to_numbers = {}
        self.c.reset()
        self.assertDictEqual(self.c.notes_to_numbers, {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        })

    def test_apply_key_sets_correct_note_values(self):
        #Käydäänkö kaikki sävellajit läpi?
        self.c.apply_key('G')
        self.assertDictEqual(self.c.notes_to_numbers, {
            'C': 0, 'D': 2, 'E': 4, 'F': 6,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 18, 'g':19,
            'a': 21, 'b': 23
        })
        self.c.apply_key('Bb')
        self.assertDictEqual(self.c.notes_to_numbers, {
            'C': 0, 'D': 2, 'E': 3, 'F': 5,
            'G': 7, 'A': 9, 'B': 10, 'c': 12,
            'd': 14, 'e': 15, 'f': 17, 'g':19,
            'a': 21, 'b': 22
        })
    
    def test_conversion_returns_correct_ouput(self):
        ret = self.c.convert(self.dir_name + '/convert_test_data.txt')
        self.assertListEqual(ret, [11,12,14,12,14,16,
        14,12,11,9,11,12,11,9,7,6,7,9,7,9,11,12,7,9,2,11,12,
        14,19,14,11,9,7,16,16,14,12,11,12,14,16,14,12,11,12,
        11,9,2,7,6,7,9,11,9,11,12,14,16,18,19,12,11,9,7,9,
        2,6,7,7])