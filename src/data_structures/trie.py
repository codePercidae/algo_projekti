from .node import Node

class Trie:
    '''Data structure that holds the frequencies of different note sequences'''

    def __init__(self) -> None:
        '''Initialize the tree, with root as "empty note'''

        self.root = Node(0)

    def __str__(self) -> str:
        '''String representation of trie'''

        return str(self.root)

    def train(self, dataset: list) -> None:
        '''Train the trie with given data

        Args:
            dataset: name of a file to be read
        Returns:
            None
        '''
        for noteblock in dataset:
            self.add_notes(self.root, noteblock)


    def add_notes(self, current_node: Node, noteblock: list, depth = 0) -> None:
        '''Add a block of notes into trie structure and update each values frequency

        Args:
            current_node: points to current node of the trie. Starts always with the root
            noteblock: a list of integers
            depth: tracks how deep in the trie function currently is
        Returns:
            None
        '''
        if depth > 0:
            current_node.visit()
        if depth >= len(noteblock):
            return
        if noteblock[depth] not in current_node.children:
            current_node.add_child(noteblock[depth])
        self.add_notes(current_node.children[noteblock[depth]], noteblock, depth+1)

    def search(self, noteblock: list, degree: int):
            '''Start _search function. This is just to keep code clean and neat.'''
            return self._search(self.root, noteblock, degree, 0)

    def _search(self, current_node: Node, noteblock: list, degree: int, depth: int) -> list:
        '''Search trie for possible future values

        Args:  
            current_node: points to current node of the trie. Starts always with the root
            noteblock: a list of integers
            depth: tracks how deep in the trie function currently is
        Retruns:
            List of tuples (x,y) where x is the future value, and y its frequency
            if no viable future value is found, returns empty list
        '''
        possible_notes = []
        if depth == degree or depth >= len(noteblock):
            for note, child in current_node.children.items():
                possible_notes.append((note, child.frequency))
        elif noteblock[depth] in current_node.children:
            possible_notes.extend(
                self._search(current_node.children[noteblock[depth]], noteblock, degree, depth+1))
        return possible_notes
