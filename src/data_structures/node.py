#Class node: children will be saved in form of key value pairs, where key is the note name
#and value is the corresponding node. end tells wether the noteblock ends at the current note
#or not.
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