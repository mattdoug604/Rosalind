#!/usr/bin/python
# -*- coding: utf-8 -*-

# For a collection of strings and a positive integer k,
# the overlap graph for the strings is a directed graph O(k) in which each string is represented by a node,
# and string s is connected to string t with a directed edge when there is a length k suffix of s that
# matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in
# the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O(3). You may return edges in any order.

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

infile = "rosalind_grph.txt"
dataset = ParseFasta(infile)

for seq in dataset:
    suf = dataset[seq][-3:]
    for seq2 in dataset:
        pre = dataset[seq2][:3]
        if seq <> seq2:
            if suf == pre:
                print seq, seq2
