'''Class for testing integrated parts of the application.'''

import unittest
from markov import generate
from converter import Converter
from data_structures.trie import Trie
from utils.file_operations import read
from os import path

class TestIntegration(unittest.TestCase):
    
    def test_training(self):
        t = Trie()
        c = Converter()
        dirname = path.dirname(__file__)
        file = open(self.dir_name + '/convert_test_data.txt', 'r', encoding='utf-8')
        initial_data = read(file)
        converted_file = c.convert(file)
        sequences = c.chunk(converted_file, 4)
        t.train(sequences)

        self.assertEqual(str(t), )

    def test_generation(self):
        pass
