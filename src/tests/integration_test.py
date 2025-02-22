'''Class for testing integrated parts of the application.'''

import unittest
from markov import generate
from converter import Converter
from data_structures.trie import Trie
from utils.file_operations import read, write

class TestIntegration(unittest.TestCase):
    
    def test_training(self):
        '''Test that from reading a file, to training trie, all works.'''

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
        self.assertEqual(str(t), expected)

    def test_generation(self):
        pass
