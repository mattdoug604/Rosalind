#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Matching a Spectrum to a Protein
URL: http://rosalind.info/problems/prsm/

Given: A positive integer n followed by a collection of n protein strings s1, 
s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, 
followed by the string sk for which this maximum multiplicity occurs (you may 
output any such value if multiple solutions exist).
'''

from rosalind_utils import aa_mass

def build_peptide(n, frag_dict, peptide='', aa=0):
    ''' Given a dictionary of fragment masses, with the next highest fragment
    mass and an amino acid representing the gap between them, iterably build a
    peptide by starting with the smallest mass. 
    '''
    if aa == 0:
        aa = min(frag_dict)
    
    if len(peptide) == n:
        return peptide
    else:
        for i in frag_dict[aa]:
            return build_peptide(n, frag_dict, peptide+i[0], i[1])


def peptide_from_fragments(p, l):
    # A peptide has length n, assuming a list of 2n+2 masses are given 
    # (excluding the mass of the parent peptide).
    n = (len(l)-2)/2
    
    # Find each pair of b- and y-ions.
    pairs = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            aa = mass_to_aa(l[j]-l[i])
            if aa:
                if l[i] in pairs:
                    pairs[l[i]].append((aa, l[j]))
                else:
                    pairs[l[i]] = [(aa, l[j])]
        
    # Iterably build the peptide starting with the smallest fragment mass.
    peptide = build_peptide(n, pairs)
    
    # Return the completed peptide of length n.
    return peptide

def max_multiplicity(n, s, r):
    r = sorted(r)
    
    print(peptide_from_fragments(0, r))
    
    return '', ''


def main():
    with open('problem_datasets/rosalind_prsm.txt', 'r') as infile:
        n = int(infile.readline().strip())
        s = [infile.readline().strip() for i in range(n)]
        r = list(map(float, infile.read().strip().split('\n')))
    
    print('\n'.join(map(str, max_multiplicity(n, s, r))))
    

if __name__ == '__main__':
    main()