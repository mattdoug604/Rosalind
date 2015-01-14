#!/usr/bin/python
# -*- coding: utf-8 -*-
# Given: A positive integer n ≤ 7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

'''
A permutation of length n is an ordering of the positive integers {1,2,…,n}.
For example, π=(5,3,2,1,4) is a permutation of length 5.
'''

def all_perms(elements):
    if len(elements) <=1:
        print elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                print perm[:i] + elements[0:1] + perm[i:]

n = 3
num_list = [str(i) for i in range(1, n+1)]
all_perms(num_list)
        
