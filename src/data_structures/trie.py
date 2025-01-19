from .node import Node

class Trie:
    def __init__(self) -> Node:
        '''Initialize the tree, with root as "empty note'''
        self.root = Node(0, False)

    def add_notes(self, noteblock) -> None:
        '''Application uses this to start the note insertion
        Args:
            noteblock: a list of a 4 integers
        Returns:
            None
        '''
        return self._add_note_helper(self.root, 0, noteblock)

    def _add_note_helper(self, current_node: Node, depth: int, noteblock) -> None:
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
    
    def search(self, current_node: Node, noteblock, depth = 0) -> list:
        '''Searches trie for possible future values
        Args:  current_node: points to current node of the trie. Starts always with the root
            noteblock: noteblock: a list of a 3 integers
            depth: tracks how deep in the trie function currently is
        Retruns:
            List of tuples (x,y) where x is the future value, and y its frequency
            if no viable future value is found, returns empty list
        '''
        possible_notes = []
        if depth == 3:
            for note, child in current_node.children:
                possible_notes.append((note, child.frequency))
            return possible_notes
        if current_node.children[noteblock[depth]]:
            return possible_notes + self.search(current_node[noteblock[depth]], depth + 1, noteblock)
        else: return possible_notes
                

            


