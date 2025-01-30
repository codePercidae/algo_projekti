import unittest
from data_structures.node import Node

class TestNode(unittest.TestCase):
    '''Tests functioning of the node data structure'''

    def setUp(self):
        self.n = Node(0)

    def test_constructor_returns_a_node_with_given_frequency(self):
        node = Node(3)
        self.assertEqual(node.frequency, 3)

    def test_visit_grows_frequency(self):
        '''Visit should grow nodes frequency by one.'''

        self.n.visit()
        self.assertEqual(self.n.frequency, 1)

    def test_add_child_adds_a_node_into_children(self):

        self.n.add_child(3)
        self.assertIn(3, self.n.children)
        self.assertIsInstance(self.n.children[3], Node)

    def test_stringify(self):
        self.n.add_child(3)
        string_n = self.n.__str__()
        self.assertEqual(string_n, 'Node(freq: 0, children: [ Node(freq: 0, children: [])])')
