from random import randint

def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        bigger = [n for n in l[1:] if n >= pivot]
        smaller = [n for n in l[1:] if n < pivot]
        return [*quick_sort(smaller), pivot, *quick_sort(bigger)]

l = [randint(0, 10) for x in range(10)]
assert quick_sort(l) == sorted(l)