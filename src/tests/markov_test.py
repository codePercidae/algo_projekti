import unittest
from markov import choose, generate
from data_structures.trie import Trie

class TestMarkov(unittest.TestCase):
    #testaa ettei mitään ylimääräistä löydy
    #testaa että k-monikot löytyvät kaikki opetusdatasta
    #vertaa opetusdataan
    
    def setUp(self):
        '''Set up the trie, and data used for testing.'''

        self.t = Trie()
        self.data = [1,2,3,4,7,2,1,0]
        self.data_4s = [[1,2,3,4], [2,3,4,7], [3,4,7,2], [4,7,2,1], [7,2,1,0]]
        self.t.train(self.data_4s)

        print(self.t)

    def test_generate(self):
        '''Test that all k subset of the generated data can be found from original data.
        
        While using limited amounts of data, generation might come to halt as it no longer has
        possible future values. For this reason, only single bar is generated for 100 times
        to make sure that no exceptions happen, while simultaneously making strong enough case
        that all generated material exists in original data.
        '''
        def help():
            ret = generate(3, 1, self.t)
            for i in range(len(ret)-4):
                for j in range(len(self.data)-4):
                    if ret[i:i+4] == self.data[j:j+4]:
                        break
                else: return False
            return True
        for i in range(100):
            self.assertTrue(help())

    def test_choose_returns_int_from_given_list(self):
        '''Test that choose returns one of values in given list
        
        Repeat test for 50 times to make sure that no weird stuff happens
        '''
        values_weights = [(1,4), (4,4), (2,4), (9,4)]
        values = [1,4,2,9]
        for i in range(50):
            ret = choose(values_weights)
            self.assertIn(ret, values)

