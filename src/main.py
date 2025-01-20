from conversion.converter import Converter
from data_structures.trie import Trie
from markov import MarkovChain
from pathlib import Path

class Main:
    def __init__(self):
        '''Initializes the application and links necessary elements to it
        '''
        self.converter = Converter()
        self.trie = Trie()
        self.markov = MarkovChain()

    def generate(self, degree: int) -> list:
        if degree < 0:
            print('Invalid degree!')
        if degree > self.trie.depth:
            print('Degree too large! Give smaller degree or train model with longer melodies.')
        generated_list = []
        for i in range(10):
            if i < degree:
                generated_list.append(
                    self.markov.choose(
                        self.trie.search(self.trie.root, generated_list[0:i], degree)))
            else:
                generated_list.append(
                    self.markov.choose(
                        self.trie.search(self.trie.root, generated_list[i:i+degree], degree)))
        return generated_list
    
    def train(self, dataset: str) -> None:
        initial_numbers = self.converter.convert(dataset)
        print('File converted!')
        seq = self.converter.chunk(initial_numbers)
        for lst in seq:
            self.trie.add_notes(lst)
        self.trie.depth = self.trie.find_depth(self.trie.root, 0)

    def launch(self):
        '''Launches the application
        '''
        print('Hi, please give me a file address to begin!') 
        filename = input('Filename: ')
        self.train(filename)        
        print('Model updated!')
        print('Maximum degree of the generation is now ', self.trie.depth)
        deg = int(input('Which degree of generation you wish to have? '))
        self.generate(deg)
        