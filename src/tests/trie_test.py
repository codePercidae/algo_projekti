import unittest
from data_structures.trie import Trie

class TestTrie(unittest.TestCase):
    '''Tests functioning of the trie data structure'''

    def setUp(self):
        '''Init trie for tests.'''

        self.t = Trie()
        self.t.add_notes(self.t.root, [1,2,3,4])
        self.t.add_notes(self.t.root, [1,2,3,5])
        self.t.add_notes(self.t.root, [1,2,3,5])
        self.t.add_notes(self.t.root, [1,2,3,6])

    def test_initializing_new_trie_creates_node_with_no_children(self):
        '''Trie should initially have just the root node.'''

        new_trie = Trie()
        self.assertEqual(len(new_trie.root.children), 0)

    def test_search_returns_expected_values(self):
        '''Trie should return possible future values, when given a list of values.'''

        res = self.t.search([1,2,3], 4)
        self.assertEqual(res, [(4,1), (5,2), (6,1)])

    def test_search_returns_empty_list(self):
        '''When no possible succession of values is found, return empty list.'''

        res = self.t.search([2,3,4], 4)
        self.assertEqual(res, [])
