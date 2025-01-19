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

    def launch(self):
        '''Launches the application
        '''
        print('Hi, please give me a file address to begin!') 
        filename = input('Filename: ')
        initial_numbers = self.converter.convert(filename)
        print('File converted!')
        seq = self.converter.chunk(initial_numbers)
        print(initial_numbers)
        for lst in seq:
            self.trie.add_notes(lst)
        self.trie.depth = self.trie.find_depth(self.trie.root, 0)
        print('Maximum degree of the generation is now ', self.trie.depth)
        print('Model updated!')
        deg = int(input('Which degree of generation you wish to have? '))
        generated_list = []
        for i in range(10):
            print('index: ', generated_list[0:i])
            if i < deg:
                generated_list.append(
                self.markov.choose(
                    (self.trie.search(self.trie.root, generated_list[0:i], i))
                    ))
            else:
                generated_list.append(
                self.markov.choose(
                    (self.trie.search(self.trie.root, generated_list[i:i+deg], deg)))
                    )
        print(generated_list)
        