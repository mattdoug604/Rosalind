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

infile = "rosalind_long_test.txt"
dataset = ParseFasta(infile).values()

def FindOverlaps(sequences):
    overlaps = []
    for frag in sequences:                              # first fragment to compare
        temp = []
        for j in range(len(frag)/2+1, len(frag)+1):     # j = overlap size
            for k in range(len(frag)-j+1):              # k = starting point
                over = frag[k:k+j]
                for frag2 in sequences:                 # compare against every other sample
                    if frag <> frag2:                   # don't compare against self
                        match = re.search(over, frag2)
                        if match:
                            start = match.span()[0]
                            end = match.span()[1]
                            if start <= 1:
                                overlaps.append(frag[:k]+frag2[start:])
                                #print frag, frag2, '->', over, '@', 'if', 'k=',k, 'j=',j, '(', start, ',', end, ')\t', frag[:k]+frag2[start:]
                            else:
                                overlaps.append(frag2[:start]+frag[k:])
                                #print frag, frag2, '->', over, '@', 'else', 'k=',k, 'j=',j, '(', start, ',', end, ')\t', frag2[:start]+frag[k:]
        #print ''
        overlaps = list(set(overlaps))
    #print '----------------'
    return overlaps

contigs = FindOverlaps(dataset)
contigs2 = FindOverlaps(contigs)
print max(contigs2, key=len)

#ATTAGACCTGCCGGAATAC
#ATTAGACCTGCCGGAATAC
