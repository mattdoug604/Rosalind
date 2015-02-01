#!/usr/bin/python

# Find substrings of a genome encoding a given amino acid sequence.
# Given: A DNA string Text and an amino acid string Peptide.
# Return: All substrings of Text encoding Peptide (if any such substrings exist).

def getCodonTable():
    '''
    Generates an RNA codon table in dictionary form.
    Note: STOP codons denoted with an asterisk (*)
    '''
    aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    bases = ['T','C','A','G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, aa))

    return codon_table

def getRevComp(seq):
    ntDict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    revSeq = seq[::-1]
    revComp = ''
    for nt in revSeq:
        revComp += ntDict[nt]

    return revComp

def getEncodeSeq(seq, pep, codons):
    encodes = []
    
    for i in range(2):
        translation = ''
        encodeSeq = ''
        
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            
            if len(codon) < 3 or codons[codon] == '*':
                break
            else:
                translation += codons[codon]
                encodeSeq += codon

        if pep in translation:
            encodes.append(encodeSeq)

    return(encodes)
            

with open('rosalind_2b.txt', 'r') as infile:
    text = infile.read().split('\n')
    sequence = text[0]
    peptide = text[1]

revSequence = getRevComp(sequence)
codons = getCodonTable()

answer = getEncodeSeq(sequence, peptide, codons)
for a in answer: print(a)
