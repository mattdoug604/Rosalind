#!/usr/bin/env python3

## Find a median string.
## Given: An integer k and a collection of strings DNA.
## Return: A k-mer Pattern that minimizes d(Pattern, DNA) over all k-mers Pattern. (If multiple answers exist, you may return any one.)

import itertools

def countMedian(kmers, motifs, k):
    # compare possible k-mer to each found k-mer, nucleotide-by-nucleotide
    # and keep the minimum value for each along that particular string.s
    for old in motifs:
        temp = k    # k is the maximum possible value
        for new in kmers:
            diff = 0
            for nt in range(k):
                if new[nt] != old[nt]:
                    diff += 1

            if diff < temp:
                temp = diff
            
        motifs[old] += temp
    return motifs

def findMedianMotif(strings, k):
    ## Start with dictionary of all possible k-mers (value for each k-mer starts at 0)
    motifs = {''.join(nt) : 0 for nt in itertools.product(['A','C','T','G'], repeat=k)}

    ## Find all k-mers in each string...
    for seq in strings:
        kmers = []
        for i in range(len(seq)-k+1):
            kmers.append(seq[i:i+k])

        ## Find the min for each k-mer and return an updated dictionary of values
        motifs = countMedian(kmers, motifs, k)
    
    return motifs

## Read in file    
with open('rosalind_3b.txt', 'r') as infile:
    text = infile.read().rstrip().split('\n')
    k = int(text[0])
    strings = text[1:]

# Find minimum d(Pattern, DNA), then print out every Pattern with the minimum value
answer = findMedianMotif(strings, k)
minVal = min(answer.itervalues())
print('median = %i' % minVal)
for key, val in answer.iteritems():
    if val == minVal:
        print(key)
