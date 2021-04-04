#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given all pairwise distances between points on a line segment, reconstruct the positions of those points.
# Given: A collection of integers L.
# Return: A set A such that ∆A = L.

from math import sqrt

'''
with open('rosalind_2i.txt', 'r') as infile:
    a = infile.read()'''

a = '1 2 2 2 3 3 3 4 5 5 5 6 7 8 10'
a = map(int, a.split(' '))

'''
def getDiff(line):
    diff = []
    for i in range(len(line)):
        for j in range(len(line)):
            diff.append(line[i]-line[j])

    return sorted(diff)
'''

def getLine(diff):
    l = int(sqrt(len(diff)))
    pos = [i if i>1 else 0 for i in range(1, l+1)] # [2, 3, 4, 5]
    for j in range(1, l):
        pos[j] = pos[j] + pos[j-1]

    line = [diff[len(diff)-1-x] for x in pos]
    return sorted(line)
    
answer = getLine(a)
print(' '.join(str(x) for x in answer))
