import unittest
import os
from converter import Converter

class TestConverter(unittest.TestCase):
    '''Test converter functionality'''

    def setUp(self):
        '''Set up the converter and filepath for test data.'''

        self.c = Converter()
        self.dir_name = os.path.dirname(__file__)

    def test_reset_sets_note_to_int_relation_back(self):
        '''Test that note~integer relation gets reseted to original.'''

        self.c.notes_to_numbers = {}
        self.c.reset()
        self.assertDictEqual(self.c.notes_to_numbers, {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        })

    def test_apply_key_sets_correct_note_values(self):
        '''Test that when key is applied, the note~integer relations is
        manipulated accordingly.'''

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
        '''Test that converting given data returns expected list of integers.'''

        file = open(self.dir_name + '/convert_test_data.txt', 'r', encoding='utf-8')
        contents = file.readlines()
        ret = self.c.convert(contents)
        self.assertListEqual(ret, [11, 12, 14, 12, 14, 16, 14, 12, 11, 9, 11, 12, 11,
            9, 7, 6, 7, 9, 7, 9, 11, 12, 7, 9, 2, 11, 12, 14, 19, 14, 11, 9, 7, 16,
            16, 14, 12, 11, 12, 14, 16, 14, 12, 11, 12, 9, 2, 7, 6, 7, 9, 11, 9, 11,
            12, 14, 16, 18, 19, 12, 11, 9, 7, 9, 2, 6, 7, 7])

    def test_parse_row_returns_correct_output(self):
        '''Test that parsing row, returns expected list of integers.'''

        ret = self.c.parse_row('|C^deA|Bb_dg')
        self.assertEqual(ret, [0,15,16,9,11,23,13,19])

    def test_reverse_conversion_returns_correct_output(self):
        '''Test that a list of inetegers is converted to proper abc-notation.'''

        cmaj_input = [[0,2,4,5,7,9,11]]
        ret = self.c.reverse_convert(cmaj_input)
        self.assertEqual(ret, ['|CDEF|GAB\n\n'])

    def test_chunk_returns_correct_sizes_sublists(self):
        '''Test that chunk returns a list of lists that are length of given value.'''

        ret = self.c.chunk([1,1,1,1,1,1,1,1,1,1,1], 4)
        for lst in ret:
            self.assertEqual(len(lst), 4)
