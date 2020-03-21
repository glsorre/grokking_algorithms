from copy import copy
from random import randint

def selection_sort(l):
    l = copy(l)
    sorted_l = []
    while len(l) > 0:
        smaller = 2147483647
        for n in l:
            if n < smaller:
                smaller = n
        sorted_l.append(smaller)
        l.remove(smaller)
    return sorted_l


l = [randint(0, 10) for x in range(10)]
assert selection_sort(l) == sorted(l)