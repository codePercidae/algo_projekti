'''Class for Trie data structure.'''
from .node import Node

class Trie:
    '''Class functions:
        __init__: constructor
        __str__: basic string representation
        help_stringify: turn Trie into list with tuples, [(x,y)]
        train: train Trie with given data
        add_notes: add given values to Trie
        search: look for possible future values from Trie
        '''

    def __init__(self) -> None:
        '''Initialize the tree, with root as "empty" note'''

        self.root = Node(0)

    def __str__(self) -> str:
        '''Return string representation of trie.'''

        return str(self.help_stringify(0, self.root))
    
    def help_stringify(self, value: int, current: Node) -> list:
        '''Turn trie into list representation via DFS.
        
        Args:
            value: integer representing the node value
            current: the current node to process
        Returns:
            a list with tuples (x,y), where x is nodes value
            and y is it's frequency'''
        ret = [(value, current.frequency)]
        if current.children: #if current node has childen, recursively process them
            for i, n in current.children.items():
                ret.extend(self.help_stringify(i, n))
        return ret

    def train(self, dataset: list) -> None:
        '''Train the trie with given data

        Args:
            dataset: contents of the file, stored into a list row by row
        Returns:
            None
        '''
        for noteblock in dataset:
            self.add_notes(noteblock)


    def add_notes(self, noteblock: list) -> None:
        '''Add a block of notes into trie structure and update each values frequency

        Args:
            noteblock: a list of integers
        Returns:
            None
        '''
        current_node = self.root #start from root
        for note in noteblock: 
            if note not in current_node.children:
                current_node.children[note] = Node(0) 
            current_node = current_node.children[note]
            current_node.frequency += 1

    def search(self, noteblock: list) -> list:
        '''Search trie for possible future values

        Args:
            noteblock: a list of integers
        Retruns:
            List of tuples (x,y) where x is the future value, and y its frequency
            if no viable future value is found, returns empty list
        '''
        returnList = []
        current_node = self.root
        #Use given notes to traverse the trie
        for note in noteblock:
            if note in current_node.children:
                current_node = current_node.children[note]
            else: 
                return returnList
        #Return final nodes children
        for note, node in current_node.children.items():
            returnList.append((note, node.frequency))
        return returnList