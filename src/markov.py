from random import choices
from functools import reduce

class MarkovChain:
    def __init__(self):
        pass

    def choose(self, values: list) -> int:
        #jokin rikki
        total = reduce(lambda v, t : v + t[0], values, 0)
        weights = map(lambda v: v[1]/total, values)
        return choices(values, weights).pop()[0]
        