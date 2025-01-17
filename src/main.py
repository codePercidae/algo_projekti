from conversion.converter import Converter
from data_structures.trie import Trie
from pathlib import Path

class Main:
    def __init__(self):
        self.converter = Converter()
        self.trie = Trie()
        #lisäksi markov-laskuri?

    def launch(self):
        print('Hi, please give me a file address to begin!') 
        filename = input('Filename: ')
        inital_numbers = self.converter.convert(filename)
        print('File converted!')
        print(inital_numbers)
        for i in range(len(inital_numbers)):
            self.trie.add_notes(inital_numbers[i:i+4])
        print('Model updated!')