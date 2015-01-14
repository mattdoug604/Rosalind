#!/usr/bin/python
# Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format
#   (which represent reads deriving from the same strand of a single linear chromosome).
# The dataset is guaranteed to satisfy the following condition:
#   there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

import re

def ParseFasta(file_name):
    heads = []
    seqs = {}

    with open(file_name, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                heads.append(num)
    heads.append(sum(1 for line in open(file_name)))

    f = open(file_name, 'r')
    lines = f.readlines()
    for i in range(len(heads)-1):
        h = lines[heads[i]].replace('\n', '')
        l = lines[heads[i]+1:heads[i+1]]
        seqs[h[1:]] = ''.join(l).replace('\n', '')

    return seqs

# Found at: https://github.com/mtarbit/Rosalind-Problems/blob/master/e025-long.py

def find_overlaps(arr, acc=''):
    #print 'arr=',arr, '\n', 'acc=',acc
    if len(arr) == 0:
        return acc
    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)
    else:
        for i in range(len(arr)):
            a = arr[i]
            l = len(a)
            for p in range(l / 2):
                q = l - p
                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)
                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])

sequences = ParseFasta('rosalind_long.txt').values()
contig = open('rosalind_long_answ.txt', 'w')
contig.write(find_overlaps(sequences))
