#!/usr/bin/python
# PPER_PartialPermutations.py

'''
Given: Positive integers n and k such that 100 >= n >= 0 and 10 >= k >= 0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
'''

import operator
from itertools import permutations
from collections import Counter
from math import factorial

def numPermutations(l):
    num = factorial(len(numbers))
    mults = Counter(numbers).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    counts = (num / den) % 1000000
    return(counts)

n = 21
k = 7

numbers = [x for x in range(1, n+1)]
print(numPermutations(numbers))
