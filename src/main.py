from converter import Converter
from data_structures.trie import Trie
from ui.interface import Interface

class Main:
    '''Class for main application'''

    def __init__(self):
        '''Initialize the application.'''

        self.interface = Interface(Trie(), Converter())

    def launch(self):
        '''Launch the application.'''

        self.interface.mainmenu()

if __name__ == '__main__':
    app = Main()
    app.launch()
