#!/usr/bin/python

## Find a Profile-most probable k-mer in a string.
## Given: A string Text, an integer k, and a 4 * k matrix Profile.
## Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)

'''
Example Matrix Profile:
	A: .2  .2  .0  .0  .0  .0  .9  .1  .1  .1  .3  .0
Profile	C: .1  .6  .0  .0  .0  .0  .0  .4  .1  .2  .4  .6
	G: .0  .0  1.  1.  .9  .9  .1  .0  .0  .0  .0  .0
	T: .7  .2  .0  .0  .1  .1  .0  .5  .8  .7  .3  .4
Pr(ACGGGGATTACC|Profile) = .2*.6*.1*.1*.9*.9*.9*.5*.8*.1*.4*.6 = 0.000839808
'''

from collections import defaultdict

def getKmers(dna, k):
    for i in range(len(dna)-k+1):
        kmer = dna[i:i+k]
        yield(kmer)

def findProb(dna, k, profile):
    prob = defaultdict(str)
    nt = {'A':0, 'C':1, 'G':2, 'T':3}   ## Each row of the profile matrix corresponds to a specific nucleotide
    
    for mer in getKmers(dna, k):
        prob[mer] = 0
        for m in range(len(mer)):
            val = profile[nt[mer[m]]][m]
            if prob[mer] == 0:
                prob[mer] = val
            else:
                prob[mer] *= val

    maxVal = max(prob, key=prob.get)
    return(str(maxVal + ' with P(' + str(prob[maxVal]) + ')'))
        
## Read file
with open('rosalind_3c.txt', 'r') as infile:
    text = infile.read().rstrip().split('\n')
    string = text[0]
    k = int(text[1])
    profile = [[float(x) for x in p.split(' ')] for p in text[2:6]]

print(findProb(string, k, profile))
