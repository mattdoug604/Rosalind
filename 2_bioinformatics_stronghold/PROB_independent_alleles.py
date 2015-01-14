#!/usr/bin/python
# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
# Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

'''
The probability that a sequence will match a given GC-content value is the 
probability that each nucleotide is either (C or G) or (A or T) independently.
*Think: tree-diagram.
'''

import math

s = 'TAGGCGACTCGGCTTGCCGACAACAATGTGGCGACCACGCCGAGCAGACAGGCATCGTCTAAGAAGACGTATGCTAATAGGTATCGTATGTAAGGGGAAA'
gc = '0.095 0.152 0.205 0.261 0.268 0.350 0.407 0.453 0.498 0.548 0.588 0.657 0.704 0.777 0.808 0.886 0.939'
gc = [float(n) for n in gc.split()]
answer = []

for i in range(len(gc)): # for each given GC-value...
    percent = 1
    probGC = gc[i]/2 # divide by 2 because its 50:50 wether it can be C or G
    probAT = (1-gc[i])/2 # probability of A or T is 1 minus the prob. of C or G
    for j in range(len(s)): # for each nucleotide in the given sequence...
        nt = s[j]
        if nt == 'C' or nt == 'G': # if the nucleotide is C or G...
            percent = percent*probGC # ...percent is multiplied by (half) the given GC-value
        elif nt == 'A' or nt == 'T': # ...same with A or T
            percent = percent*probAT

    percent = math.log10(percent) # The final answer is the Log10 of the probability
    answer.append('%.3f' % percent)

print ' '.join(answer)
