from conversion.converter import Converter
from data_structures.trie import Trie
from pathlib import Path

class Main:
    def __init__(self):
        '''Initializes the application and links necessary elements to it
        '''
        self.converter = Converter()
        self.trie = Trie()
        #lisäksi markov-laskuri?

    def launch(self):
        '''Launches the application
        '''
        print('Hi, please give me a file address to begin!') 
        filename = input('Filename: ')
        initial_numbers = self.converter.convert(filename)
        print('File converted!')
        seq = self.converter.chunk(initial_numbers)
        for lst in seq:
            self.trie.add_notes(lst)
        print('Model updated!')