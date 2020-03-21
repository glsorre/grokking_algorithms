from random import randint

def recursive_sum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recursive_sum(l[1:])

l = [randint(0, 10) for x in range(10)]
assert recursive_sum(l) == sum(l)