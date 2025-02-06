import unittest
from data_structures.node import Node

class TestNode(unittest.TestCase):
    '''Tests functioning of the node data structure'''

    def setUp(self):
        self.n = Node(0)

    def test_constructor_returns_a_node_with_given_frequency(self):
        node = Node(3)
        self.assertEqual(node.frequency, 3)
