from .node import Node

class Trie:
    '''Data structure that holds the frequencies of different note sequences'''

    def __init__(self) -> Node:
        '''Initialize the tree, with root as "empty note'''
        self.root = Node(0, False)
        self.depth = 0 #tod näk turhake

    def __str__(self):
        '''String representation of trie'''
        return str(self.root)

    def find_depth(self, current_node: Node, depth: int) -> int: #tod näk turhake
        '''Finds the depth of the trie
        Args: 
            current_node: points to current node of the trie, starts always from root
            depth: carries the information how deep in the trie functio is, starts always as 0
        Returns:
            Integer representing the depth of the trie
        '''
        if len(current_node.children) > 0:
            for child in current_node.children.values():
                new_depth = max(self.find_depth(child, depth + 1), depth)
            return new_depth
        return depth

    def add_notes(self, noteblock: list) -> None:
        '''Application uses this to start the note insertion
        Args:
            noteblock: a list of integers
        Returns:
            None
        '''
        return self._add_note_helper(self.root, noteblock)

    def _add_note_helper(self, current_node: Node, noteblock: list, depth = 0) -> None:
        '''Adds a block of notes into trie structure and updates
        each values frequency
        Args:
            current_node: points to current node of the trie. Starts always with the root
            depth: tracks how deep in the trie function currently is
            noteblock: a list of integers
        Returns:
            None
        '''
        if depth >= len(noteblock):
            return
        if depth > 0:
            current_node.frequency += 1
        if noteblock[depth] not in current_node.children:
            current_node.children[noteblock[depth]] = Node(1, True)
        return self._add_note_helper(current_node.children[noteblock[depth]], noteblock, depth+1)

    def search(self, current_node: Node, noteblock: list, degree: int, depth = 0) -> list:
        '''Searches trie for possible future values
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
                self.search(current_node.children[noteblock[depth]], noteblock, degree, depth+1))
        return possible_notes

if __name__ == '__main__':
    trie = Trie()
    trie.add_notes([1,2,3,4])
    trie.add_notes([2,3,4,5])
    trie.add_notes([1,3,5])
    print(trie)
