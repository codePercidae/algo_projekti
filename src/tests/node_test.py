import unittest
from data_structures.node import Node

class TestNode(unittest.TestCase):
    '''Tests functioning of the node data structure'''
    def test_constructor_returns_a_node_with_given_frequency(self):
        node = Node(3, False)
        self.assertEqual(node.frequency, 3)
