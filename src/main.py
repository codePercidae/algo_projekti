from converter import Converter
from data_structures.trie import Trie
from markov import MarkovChain
from utils import logger, file_operations

class Main:
    '''Class for main application'''
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
            logger.info(
                '''Degree too large! Give smaller degree or 
                train model with longer melodies.''')
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

    def train(self, dataset: str, degree: int) -> None:
        res = file_operations.read(dataset)
        if res[0]:
            initial_numbers = self.converter.convert(res[1])
            print('File converted!')
            seq = self.converter.chunk(initial_numbers, degree)
            print(seq)
            for lst in seq:
                self.trie.add_notes(lst)
            self.trie.depth = self.trie.find_depth(self.trie.root, 0)
            print('Model updated!')
        else:
            logger.info(res[1])

    def launch(self):
        '''Launches the application'''
        deg = int(input('Hi, please give me a degree of generation you wish to have (max 6): '))
        print('Then the file that you wish to use for training!')
        filename = input('Filename: ')
        self.train(filename, deg)
        songs = [self.generate(deg) for i in range(10)]
        abc_songs = self.converter.reverse_converter(songs)
        file_operations.write('music.txt',abc_songs)


if __name__ == '__main__':
    app = Main()
    app.launch()
