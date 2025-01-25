from converter import Converter
from data_structures.trie import Trie
from markov import choose
from utils import logger, file_operations

class Main:
    '''Class for main application'''
    def __init__(self):
        '''Initializes the application and links necessary elements to it
        '''
        self.converter = Converter()
        self.trie = Trie()

    def generate(self, degree: int, length: int) -> list:
        '''Generates a list of integers
        Args:
            degree: integer that specifies the degree of markov's chain
            length: integer that tells how long the output is (in 2/4 bars)
        Returns:
            list: a list of newly generated integers [int]
        '''
        generated_list = []
        for i in range(4*length):
            if i < degree:
                generated_list.append(
                    choose(self.trie.search(self.trie.root, generated_list[0:i], degree)))
            else:
                generated_list.append(
                    choose(self.trie.search(self.trie.root, generated_list[i:i+degree], degree)))
        return generated_list

    def train(self, dataset: str, degree: int) -> None:
        '''Trains the trie with given data
        Args:
            dataset: name of a file to be read
            degree: specifies the degree of markov's chain and the depth of trie
        Returns:
            None
        '''
        res = file_operations.read(dataset)
        if res[0]:
            initial_numbers = self.converter.convert(res[1])
            logger.info('File converted!')
            seq = self.converter.chunk(initial_numbers, degree)
            for lst in seq:
                self.trie.add_notes(lst)
            logger.info('Model updated!')
        else:
            logger.info(res[1])

    def launch(self):
        '''Launches the application'''
        deg = int(input('Hi, please give me a degree of generation you wish to have (max 6): '))
        logger.info('Then the file that you wish to use for training!')
        filename = input('Filename: ')
        length = int(input('How long melody you wish to have? (in 2/4 bars) '))
        self.train(filename, deg)
        songs = [self.generate(deg, length) for i in range(10)]
        abc_songs = self.converter.reverse_converter(songs)
        file_operations.write('music.txt', abc_songs)


if __name__ == '__main__':
    app = Main()
    app.launch()
