from copy import copy
from random import randint

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    while left:
        result.append(left[0])
        del left[0]
    while right:
        result.append(right[0])
        del right[0]
    return result

def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        half = len(l) // 2
        left = merge_sort(l[:half])
        right = merge_sort(l[half:])
        return merge(left, right)

l = [randint(0, 10) for x in range(10)]
assert merge_sort(l) == sorted(l)