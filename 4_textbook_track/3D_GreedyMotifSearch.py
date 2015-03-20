#!/usr/bin/python

'''
Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running
        GreedyMotifSearch(Dna, k, t). If at any step you find more than one
        Profile-most probable k-mer in a given string, select the one occurring
        first in the string.
'''

def mostProbMotif(dna, k, profile):
    nt = {'A':0, 'C':1, 'G':2, 'T':3}
    max_prob = -1

    for i in range(len(dna)-k+1):
        mer = dna[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[j][nt[mer[j]]]

        if prob > max_prob:
            max_prob = prob
            best = dna[i:i+k]

    return(best)

def newProfile(motifs):
    ''' Takes a list of motifs and returns the dna profile '''
    positions = [''.join(nt) for nt in zip(*motifs)]
    return [[float(pos.count(nt)) / float(len(pos)) for nt in 'ACGT'] for pos in positions]

def score(motifs):
    '''Returns the score of the given list of motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return(len(motifs[0])*len(motifs) - max_count)

def greedyMotifSearch(dna, k, t):
    ## start with the max (worst) possible score
    best_score = t*k
    
    ## For every k-mer motif in the first dna string
    for i in range(len(dna[0])-k+1):
        motifs = [dna[0][i:i+k]]

        for j in range(1, t):
            profile = newProfile(motifs)
            motifs.append(mostProbMotif(dna[j], k, profile))
            
            ## check to see if the current 'motifs' score lower (better) than the previous
            new_score = score(motifs)
        if new_score < best_score:
            best_score = new_score
            best_motifs = motifs

    return(best_motifs)

'''
Read file:
    strings = a list of dna strings
    k = length of motifs to search for
    t = number of DNA strings
'''
with open('rosalind_3d.txt', 'r') as infile:
    text = infile.read().rstrip().split('\n')
    k, t = [int(x) for x in text[0].split(' ')]
    strings = text[1:]

answer = greedyMotifSearch(strings, k, t)
print('\n'.join(answer))

'''
Test input:
3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG
'''

'''
Expected output for each k-mer in the first dna string:
['GGC', 'AAG', 'AAG', 'CAC', 'CAA']
['GCG', 'AAG', 'AAG', 'ACG', 'CAA']
['CGT', 'AAG', 'AAG', 'AAT', 'AAT']
['CGT', 'AAG', 'AAG', 'AAT', 'AAT']
['CGT', 'AAG', 'AAG', 'AAT', 'AAT']
['TCA', 'TCA', 'CAA', 'TCA', 'TAA']
['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
['CAG', 'CAG', 'CAA', 'CAA', 'CAA'] <- final output
'''
