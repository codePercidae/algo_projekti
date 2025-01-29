'''Main module for melody generating application.'''

from converter import Converter
from data_structures.trie import Trie
from ui.interface import Interface

def main():
    '''Launch the application.'''
    app = Interface(Trie(), Converter())
    app.mainmenu()

if __name__ == '__main__':
    main()
