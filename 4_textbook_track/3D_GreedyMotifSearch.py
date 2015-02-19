#!/usr/bin/python

## Given: Integers k and t, followed by a collection of strings Dna.
## Return: A collection of strings BestMotifs resulting from running
##      GreedyMotifSearch(Dna, k, t). If at any step you find more than one
##      Profile-most probable k-mer in a given string, select the one occurring
##      first in the string.

from collections import defaultdict

def greedyMotifSearch(dna, k , t):
    nt = {'A':0, 'C':1, 'G':2, 'T':3}
    length = len(dna[0])-k+1
    
    for string in dna:
    
        counts= [[float(0) for i in range(k)] for j in range(4)]
        kmers = []
        prob = defaultdict(str)

        ## Establish profile matrix
        for i in range(length):
            mer = string[i:i+k]
            kmers.append(mer)

            for j in range(k):
                counts[nt[mer[j]]][j] += 1
        
        profile = [[x/length for x in y] for y in counts]
        print(profile)

        ## Find best matrix
        for mer in kmers:
            prob[mer] = 0
            for m in range(k):
                val = profile[nt[mer[m]]][m]
                if prob[mer] == 0:
                    prob[mer] = val
                else:
                    prob[mer] *= val

        maxVal = max(prob, key=prob.get)
        print(str(maxVal + ' with P(' + str(prob[maxVal]) + ')'))

## Read file
with open('rosalind_3d.txt', 'r') as infile:
    text = infile.read().rstrip().split('\n')
    k, t = [int(x) for x in text[0].split(' ')]
    strings = text[1:]

greedyMotifSearch(strings, k, t)
