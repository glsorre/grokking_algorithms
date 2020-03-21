from math import ceil, floor, log2

def binary_search(l, item):
    low = 0
    high = len(l) - 1

    log = log2(len(l))

    if item < l[low] or item > l[high]:
        return None

    previous = 2147483647
    counter = 0

    while low < high:
        counter += 1
        assert ceil(log) + 1 >= counter

        mid = (low + high) / 2
        guess = l[floor(mid)] if floor(mid) == floor(previous) else l[ceil(mid)]
        previous = mid

        if guess == item:
            return guess
        elif item > guess:
            low = mid
        else:
            high = mid

l = range(1, 102)
assert binary_search(l, 13) == 13
assert binary_search(l, 1) == 1
assert binary_search(l, 50) == 50
assert binary_search(l, 51) == 51
assert binary_search(l, 101) == 101
assert binary_search(l, 105) == None
assert binary_search(l, -3) == None
