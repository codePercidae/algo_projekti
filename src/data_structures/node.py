'''Class for representing node data structure.'''

class Node:
    '''Class functions:
        __init__: create a new node
        add_child: adds a new child for node
        visit: grows nodes frequncy
        __str__: string representation for node
    '''
    def __init__(self, frequency: int):
        '''Create a new node

        Args:
            frequency: a number representing how often node is traversed through
        Returns:
            Node    
        '''
        self.children = {}
        self.frequency = frequency

    def add_child(self, child: int) -> None:
        '''Add child for node

        Args: 
            child: integer representing the child node
        Returns:
            None
        '''
        self.children[child] = Node(0)

    def visit(self):
        '''Grow nodes frequency by one.'''

        self.frequency += 1

    def __str__(self):
        '''String representation of node.'''

        children = '[]'
        if self.children:
            children = '['
            for v in self.children.values():
                children += ' ' + str(v)
            children += ']'
        return f'Node(freq: {self.frequency}, children: {children})'
