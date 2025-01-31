'''Provide tools for computing and generating list of integers'''

from random import choices
from functools import reduce
from data_structures.trie import Trie

def choose(values: list) -> int:
    '''Return one of given values, based on their weights

    Args:
        values: a list with tuples t where t[0] is value and t[1] is weight
    Returns:
        int: one of the given values
    '''
    total = reduce(lambda v, t : v + t[0], values, 0)
    weights = map(lambda v: v[1]/total, values)
    return choices(values, weights).pop()[0]

def generate(degree: int, length: int, trie: Trie) -> list:
    '''Generate a list of integers

    Args:
        degree: integer that specifies the degree of markov's chain
        length: integer that tells how long the output is (in 2/4 bars)
    Returns:
        list: a list of newly generated integers [[int]]
    '''
    return_list = []
    for i in range(10):
        generated_list = []
        for j in range(4*length):
            if j < degree:
                generated_list.append(
                    choose(trie.search(generated_list[0:j], j)))
            else:
                generated_list.append(
                    choose(trie.search(generated_list[j:j+degree], degree)))
        return_list.append(generated_list)
    return return_list
