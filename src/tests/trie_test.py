import unittest
from data_structures.trie import Trie

class TestTrie(unittest.TestCase):
    '''Tests functioning of the trie data structure'''
    def setUp(self):
        self.t = Trie()

    def test_initializing_new_trie_creates_node_with_no_children(self):
        new_trie = Trie()
        self.assertEqual(len(new_trie.root.children), 0)

    def test_search_returns_expected_values(self):
        self.t.add_notes(self.t.root, [1,2,3,4])
        self.t.add_notes(self.t.root, [1,2,3,5])
        self.t.add_notes(self.t.root, [1,2,3,5])
        res = self.t.search(self.t.root, [1,2,3], 4)
        self.assertEqual(res, [(4,1), (5,2)])
