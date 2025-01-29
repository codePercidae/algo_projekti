class Node:
    '''Data structure for representing nodes in trie'''
    def __init__(self, frequency: int):
        '''Creates a new node
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
        children = '[]'
        if self.children:
            children = '['
            for v in self.children.values():
                children += ' ' + str(v)
            children += ']'
        return f'Node(freq: {self.frequency}, children: {children})'

if __name__ == '__main__':
    node = Node(0)
    node.children = {1: Node(0), 2: Node(0), 3: Node(1)}
    print(node)
