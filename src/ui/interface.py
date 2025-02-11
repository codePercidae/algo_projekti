'''Commandline interface for melody generation app.'''
from utils import file_operations
from markov import generate
from data_structures.trie import Trie
from converter import Converter

class Interface:
    '''Class functions:
        __init__: constructor
        mainmenu: the main menu, obviously
        trainmenu: used when user wishes to train the model
        generatemenu: used when user wishes to generate new melodies
        '''

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
        self.help = (
            'To train the model, you should place a text file into data directory. \n'
            'This file should be in abc-format. Notice that any other format might \n'
            'result into app crashing. \n\n'
            'While generating new music, there is a slight instability in the program \n'
            'which can occur if there is not enough training data, or training data is \n'
            'not diverse enough. \n'
            'If you have very little data at your disposal, avoid using large degrees of generation. \n'
            'The generated file will always appear into data directory. If name of the file is not \n'
            'specified, it will by default be music.txt' 
        )

    def mainmenu(self) -> None:
        '''Main menu for the application.'''

        print(self.greetings)
        while True:
            command = input()
            if command == 'H':
                print(self.help)
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
        if not output[0]:
            print(output[1])
            print('Make sure the file name is correct and that file exists in data directory.')
            return
        converted_file = self.converter.convert(output[1])
        print('File converted')

        self.degree = int(input('Then give the degree of generation (max 6) '))
        if self.degree > 6:
            print('Degree too large!')
            return
        sequences = self.converter.chunk(converted_file, self.degree+1)
        self.trie.train(sequences)
        self.trained = True
        print('Model trained, to start generating music, enter G')

    def generatemenu(self):
        '''Menu when user wishes to generate music.'''

        if self.trained:
            file = input('Give name for the file to be generated: ')
            if file == '':
                file = 'music.txt'

            length = int(input('Give the length of the melody (as 2/4 bars): '))
            amount = int(input('How many melodies you wish to generate? '))
            generated_lists = [generate(self.degree, length, self.trie) for i in range(amount)]
            converted_lists = self.converter.reverse_convert(generated_lists)
            file_operations.write(file, converted_lists)
            print(f'Generated {amount} melodies into file {file}.')
        else:
            print('Model is not trained yet on any data.')
