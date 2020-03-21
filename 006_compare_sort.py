from random import randint
from timeit import timeit
from collections import deque

selection_sort = __import__('002_selection_sort')
quick_sort = __import__('004_quick_sort')
merge_sort = __import__('005_merge_sort')

l_lenght = 1000
l = [randint(0,l_lenght) for x in range(1,l_lenght)]

def selection_sort_test():
    selection_sort.selection_sort(l)

def quick_sort_test():
    quick_sort.quick_sort(l)

def merge_sort_test():
    merge_sort.merge_sort(l)

def std_sort_test():
    sorted(l)

number = 100

print(timeit(selection_sort_test, number=number))
print(timeit(quick_sort_test, number=number))
print(timeit(merge_sort_test, number=number))
print(timeit(std_sort_test, number=number))