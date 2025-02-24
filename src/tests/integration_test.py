'''Class for testing integrated parts of the application.'''

import unittest
from markov import generate
from converter import Converter
from data_structures.trie import Trie
from utils.file_operations import read, write
import os

PATH = os.path.abspath(os.getcwd()) + '/data/'

class TestIntegration(unittest.TestCase):

    def tearDown(self):
        os.remove(PATH + 'test_output.txt')

    def test_integrated_system(self):
        '''Test works in two parts: 
            First check that trained trie is as expected.
            Secondly make sure that generation works.
        '''

        t = Trie()
        c = Converter()
        file = 'integration_test_data.txt'
        print(file)
        initial_data = read(file)
        if not initial_data[0]:
            raise AssertionError('Failure to read test data')
        converted_file = c.convert(initial_data[1])
        sequences = c.chunk(converted_file, 4)
        t.train(sequences)
        expected = str([(0, 0), (12, 2), (12, 1), (28, 1), (16, 1), (28, 1),            
            (16, 1), (19, 1), (28, 1), (16, 1), (19, 1), (19, 1), (16, 3),
            (19, 1), (19, 1), (16, 1), (17, 1), (17, 1), (16, 1), (16, 1),
            (14, 1), (14, 1), (19, 2), (19, 1), (16, 1), (17, 1), (16, 1),
            (17, 1), (17, 1), (17, 2), (17, 1), (16, 1), (16, 1), (16, 1),
            (16, 1), (14, 1)])

        # Training sequence completed
        self.assertEqual(str(t), expected)

        output = [generate(4, 1, t)]
        rev_converted = c.reverse_convert(output)
        write('test_output.txt', rev_converted)
        filename = PATH + 'test_output.txt'
        with open(filename) as f:
            data = f.readlines()
            #generation sequence completed
            self.assertEqual(len(data), 2)
            self.assertGreater(len(data[0]), 5)
