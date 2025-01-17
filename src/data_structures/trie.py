from node import Node

class Trie:
    #Initialize the tree, with root as "empty note"
    def __init__(self) -> Node:
        self.root = Node(0, False)

    #Add note checks if next note exists in current node's children. If not,
    #creates a new children node. Algorithm continues until the depth of 3 is
    #achieved and returns None
    def add_notes(self, noteblock):
        return self._add_note_helper(self.root, 0, noteblock)

    def _add_note_helper(self, current_node: Node, depth: int, noteblock) -> None:
        if depth > 0:
            current_node.frequency += 1
        if current_node.children[noteblock[depth-1]]:
            return self.add_note(current_node.children[noteblock[depth-1]], depth + 1, noteblock)
        else:
            current_node.children[noteblock[depth-1]] = Node(1, True)
            #Tämä ehkä väärin??
            if depth == 3:
                return
            else:
                return self.add_note(current_node.children[noteblock[depth-1]], depth + 1, noteblock)
    
    #search checks for possible future notes, their frequency, and returns them in list,
    #filled with tuples. Eg. [(1, 5), (6, 2)]
    #If no viable future note is found, empty list is returned
    def search(self, current_node: Node, noteblock, depth = 0) -> list:
        possible_notes = []
        if depth == 3:
            for note, child in current_node.children:
                possible_notes.append((note, child.frequency))
            return possible_notes
        if current_node.children[noteblock[depth-1]]:
            return possible_notes + self.search(current_node[noteblock[depth-1]], depth + 1, noteblock)
        else: return possible_notes
                

            


