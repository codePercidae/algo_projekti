from .node import Node

class Trie:
    def __init__(self) -> Node:
        '''Initialize the tree, with root as "empty note'''
        self.root = Node(0, False)
        self.depth = 0

    def find_depth(self, current_node: Node, depth: int) -> int:
        if len(current_node.children) > 0:
            for freq, child in current_node.children.items():
                new_depth = max(self.find_depth(child, depth + 1), depth)
            return new_depth
        return depth

    def add_notes(self, noteblock: list) -> None:
        '''Application uses this to start the note insertion
        Args:
            noteblock: a list of a 4 integers
        Returns:
            None
        '''
        return self._add_note_helper(self.root, 0, noteblock)

    def _add_note_helper(self, current_node: Node, depth: int, noteblock: list) -> None:
        '''Adds a block of notes into trie structure and updates
        each values frequency
        Args:
            current_node: points to current node of the trie. Starts always with the root
            depth: tracks how deep in the trie function currently is
            noteblock: a list of integers
        Returns:
            None'''
        if depth >= len(noteblock):
            return
        if depth > 0:
            current_node.frequency += 1
        if noteblock[depth] in current_node.children:
            return self._add_note_helper(current_node.children[noteblock[depth]], depth + 1, noteblock)
        else:
            current_node.children[noteblock[depth]] = Node(1, True)
            #Tämä ehkä väärin??
            return self._add_note_helper(current_node.children[noteblock[depth]], depth + 1, noteblock)
    
    def search(self, current_node: Node, noteblock: list, degree: int, depth = 0) -> list:
        '''Searches trie for possible future values
        Args:  current_node: points to current node of the trie. Starts always with the root
            noteblock: noteblock: a list of integers
            depth: tracks how deep in the trie function currently is
        Retruns:
            List of tuples (x,y) where x is the future value, and y its frequency
            if no viable future value is found, returns empty list
        '''
        possible_notes = []
        print('funktio' ,noteblock)
        if depth == degree:
            for note, child in current_node.children.items():
                possible_notes.append((note, child.frequency))
            return possible_notes
        if noteblock[depth] in current_node.children:
            return possible_notes.extend(self.search(current_node.children[noteblock[depth]], noteblock, degree, depth+1))
        else: return possible_notes
                

            


