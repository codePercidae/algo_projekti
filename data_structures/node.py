#Class node: children will be saved in form of key value pairs, where key is the note name
#and value is the corresponding node. end tells wether the noteblock ends at the current note
#or not.
class Node:
    def __init__(self, frequency: int, end: bool):
        self.children = {}
        self.frequency = frequency
        self.end = end