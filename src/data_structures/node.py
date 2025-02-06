'''Class for representing node data structure.'''

class Node:
    '''Class functions:
        __init__: create a new node'''

    def __init__(self, frequency: int):
        '''Constructor for node.

        Args:
            frequency: a number representing how often node is traversed through
        Returns:
            None    
        '''
        self.children = {}
        self.frequency = frequency
