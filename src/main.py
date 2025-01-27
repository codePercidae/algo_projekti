from converter import Converter
from data_structures.trie import Trie
from markov import choose
from utils import logger, file_operations
from ui.interface import Interface

class Main:
    '''Class for main application'''

    def __init__(self):
        '''Initialize the application and links necessary elements to it.'''

        self.converter = Converter()
        self.trie = Trie()
        self.interface = Interface(self.train, self.generate)

    def generate(self, degree: int, length: int) -> list:
        '''Generate a list of integers

        Args:
            degree: integer that specifies the degree of markov's chain
            length: integer that tells how long the output is (in 2/4 bars)
        Returns:
            list: a list of newly generated integers [int]
        '''
        return_list = []
        for i in range(10):
            generated_list = []
            for i in range(4*length):
                if i < degree:
                    generated_list.append(
                        choose(self.trie.search(self.trie.root, generated_list[0:i], degree)))
                else:
                    generated_list.append(
                        choose(self.trie.search(self.trie.root, generated_list[i:i+degree], degree)))
                return_list.append(generated_list)
            return return_list

    def train(self, dataset: str, degree: int) -> None:
        '''Train the trie with given data

        Args:
            dataset: name of a file to be read
            degree: specifies the degree of markov's chain and the depth of trie
        Returns:
            None
        '''
        res = file_operations.read(dataset)
        if res[0]:
            initial_numbers = self.converter.convert(res[1])
            seq = self.converter.chunk(initial_numbers, degree)
            for lst in seq:
                self.trie.add_notes(lst)
        else:
            logger.info(res[1])

    def launch(self):
        '''Launch the application'''
        self.interface.mainmenu()

if __name__ == '__main__':
    app = Main()
    app.launch()
