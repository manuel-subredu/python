"""
Given a sorted array of integers, found all numbers that add up to a certain value

Implementation: start from left
"""

from asd.generators import *
from asd.search_algos import *

if __name__ == '__main__':
    "generate an array of 100 items. All numbers are even"
    v = gen_vector_even(100)
    k=100
    
    for i in range(1, len(v)):
        item = binary_search(v, k-v[i], i+1, len(v)-1)
        if item is not False:
            print(f'Found {v[i], v[item]}')