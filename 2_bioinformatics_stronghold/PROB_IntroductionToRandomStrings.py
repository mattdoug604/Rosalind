#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Random Strings
URL: http://rosalind.info/problems/prob/

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
'''

import math

def main():
    with open('problem_datasets/rosalind_prob.txt', 'r') as infile:
        seq, gc = infile.read().strip().split('\n')
        gc = [float(x) for x in gc.split(' ')]

    answer = []
    for i in range(len(gc)):
        percent = 1
        probGC = gc[i]/2
        probAT = (1-gc[i])/2
        
        for j in range(len(seq)):
            nt = seq[j]
            if nt == 'C' or nt == 'G':
                percent = percent*probGC
            elif nt == 'A' or nt == 'T':
                percent = percent*probAT

        percent = math.log10(percent)
        answer.append('%.3f' % percent)

    print(' '.join(answer))

if __name__ == '__main__':
    main()
