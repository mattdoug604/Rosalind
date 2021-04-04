#!/usr/bin/env python3
"""
Find substrings of a genome encoding a given amino acid sequence.
Given: A DNA string Text and an amino acid string Peptide.
Return: All substrings of Text encoding Peptide (if any such substrings exist).
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_2b.txt")


def getCodonTable():
    """
    Generates an RNA codon table in dictionary form.
    Note: STOP codons denoted with an asterisk (*)
    """
    aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    bases = ["T", "C", "A", "G"]
    codons = [a + b + c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, aa))

    return codon_table


def getRevComp(dna):
    ntDict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    revSeq = dna[::-1]
    revComp = ""
    for nt in revSeq:
        revComp += ntDict[nt]

    return revComp


def getEncodeSeq(dna, match, codons):
    rcDna = getRevComp(dna)
    peptides = []
    encodes = []

    # Translate forward and reverse strands
    for seq in [dna, rcDna]:

        for i in range(3):
            translation = ""

            for j in range(i, len(seq), 3):
                codon = seq[j : j + 3]

                # if len(codon) < 3 or codons[codon] == '*':
                if len(codon) < 3:
                    break
                else:
                    translation += codons[codon]

            peptides.append(translation)

    # Look matching sequences in each strand
    for x in range(3):
        fPep = peptides[x]
        rPep = peptides[x + 3]

        for ind1, aa1 in enumerate(fPep):
            if fPep[ind1 : ind1 + len(match)] == match:
                y = (ind1 * 3) + x
                frag = dna[y : y + len(match) * 3]
                encodes.append(frag)

        for ind2, aa2 in enumerate(rPep):
            if rPep[ind2 : ind2 + len(match)] == match:
                y = len(dna) - (ind2 * 3 + len(match) * 3 - 1 + x + 1)
                frag = dna[y : y + len(match) * 3]
                encodes.append(frag)

    return encodes


with open(INPUT_FILE, "r") as infile:
    text = infile.read().split("\n")
    sequence = text[0]
    peptide = text[1]

codons = getCodonTable()
answer = getEncodeSeq(sequence, peptide, codons)
for a in answer:
    print(a)
