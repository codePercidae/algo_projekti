class Node:
    def __init__(self, frequency: int, end: bool):
        '''Creates a new node
        Args:
            frequency: a number representing how often node is traversed through
            end: boolean signalling wether the path ends to current node
        Returns:
            Node    
        '''
        self.children = {}
        self.frequency = frequency
        self.end = end #onko tarpeellinen???

    def __str__(self):
        children = '[]'
        if self.children:
            children = '['
            for k, v in self.children.items():
                children += ' ' + str(v)
            children += ']'
        return f'Node(freq: {self.frequency}, leaf: {self.end}, children: {children})'
    
if __name__ == '__main__':
    node = Node(0, False)
    node.children = {1: Node(0, False), 2: Node(0, False), 3: Node(1, True)}
    print(node)