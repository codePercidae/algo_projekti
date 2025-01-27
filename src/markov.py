from random import choices
from functools import reduce


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
        