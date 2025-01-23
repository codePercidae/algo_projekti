import unittest
from data_structures.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        pass

    def test_initializing_new_trie_creates_node_with_no_children(self):
        new_trie = Trie()
        self.assertEqual(len(new_trie.root.children), 0)