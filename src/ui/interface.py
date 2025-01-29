from utils import file_operations
from markov import generate
from data_structures.trie import Trie
from converter import Converter

class Interface:
    '''Commandline interface for melody generation app.'''

    def __init__(self, trie: Trie, converter: Converter) -> None:
        '''Link elements and init needed values.
        Args:
            trie: a trie for storing training data
            converter: a converter to turn given data into integer form and vice versa
        Returns:
            None
        '''
        self.degree = 0
        self.trained = False
        self.trie = trie
        self.converter = converter
        self.greetings = (
            'Hi! Looking to generate melodies? your are in a right place!\n'
            'For help, please enter H.\n'
            'To start training the model, please enter T.\n'
            'To generate music, please enter G.\n'
            'To exit the application, enter Q.')

    def mainmenu(self) -> None:
        '''Main menu for the application.'''

        print(self.greetings)
        while True:
            command = input()
            if command == 'H':
                print('Tähän ohjeet')
            elif command == 'T':
                self.trainmenu()
            elif command == 'G':
                self.generatemenu()
            elif command == 'Q':
                print('Bye!')
                break
            else:
                print('Unknown command!')

    def trainmenu(self) -> None:
        '''Menu when user wishes to train the model.'''

        filename = input('Please give the name of the file for training: ')
        output = file_operations.read(filename)
        converted_file = self.converter.convert(output[1])
        print('File converted')

        self.degree = int(input('Then give the degree of generation (max 6) ')) + 1
        sequences = self.converter.chunk(converted_file, self.degree)
        self.trie.train(sequences, self.degree)
        self.trained = True
        print('Model trained, to start generating music, enter G')

    def generatemenu(self):
        '''Menu when user wishes to generate music.'''

        if self.trained:
            file = input('''Please give the name for generated file.
                         If empty, will be music.txt as default. ''')
            if file == '':
                file = 'music.txt'

            length = int(input('Give the length of the melody (as 2/4 bars): '))
            generated_lists = generate(self.degree, length, self.trie)
            converted_lists = self.converter.reverse_convert(generated_lists)
            file_operations.write(file, converted_lists)
            print(f'Generated 10 melodies into file {file}.')
        else:
            print('Model is not trained yet on any data.')
