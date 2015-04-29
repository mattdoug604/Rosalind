#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Computing GC Content
URL: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

from __future__ import division
import re

def parseFasta(path):
    headers = []
    seqs = {}

    with open(path, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                headers.append(num)
    headers.append(sum(1 for line in open(path)))

    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(len(headers)-1):
            h = lines[headers[i]][1:].replace('\n', '')
            l = lines[headers[i]+1:headers[i+1]]
            seqs[h] = ''.join(l).replace('\n', '')

    return(seqs)

def computeGC(fastas):
    max_gc = ['n/a', 0]
    
    for header, seq in fastas.iteritems():
        gc = '%.6f' % float(((seq.count('G') + seq.count('C')) / len(seq) * 100))
        if gc > max_gc[1]:
            max_gc[0] = header
            max_gc[1] = gc

    return(max_gc)

def main():
    fastas = parseFasta('problem_datasets/rosalind_gc.txt')
    max_gc = computeGC(fastas)
    print('\n'.join(map(str, max_gc)))

if __name__ == '__main__':
    main()
