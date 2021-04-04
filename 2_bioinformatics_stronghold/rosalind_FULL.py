#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Inferring Peptide from Full Spectrum
URL: http://rosalind.info/problems/full/

Given: A list L containing 2n+3 positive real numbers (n≤100). The first number 
in L is the parent mass of a peptide P, and all other numbers represent the 
masses of some b-ions and y-ions of P (in no particular order). You may assume 
that if the mass of a b-ion is present, then so is that of its complementary 
y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real 
numbers w1 and w2 such that for every prefix p and suffix s of t, each of 
w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists 
a protein string whose t-prefix and t-suffix weights correspond to the 
non-parent mass values of L.) If multiple solutions exist, you may output any 
one.
"""

from rosalind_utils import mass_to_aa


def build_peptide(n, frag_dict, peptide="", aa=0):
    """Given a dictionary of fragment masses, with the next highest fragment
    mass and an amino acid representing the gap between them, iterably build a
    peptide by starting with the smallest mass.
    """
    if aa == 0:
        aa = min(frag_dict)

    if len(peptide) == n:
        return peptide
    else:
        for i in frag_dict[aa]:
            return build_peptide(n, frag_dict, peptide + i[0], i[1])


def peptide_from_fragments(p, l):
    # A peptide has length n, assuming a list of 2n+2 masses are given
    # (excluding the mass of the parent peptide).
    n = (len(l) - 2) / 2

    # Find each pair of b- and y-ions.
    pairs = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            aa = mass_to_aa(l[j] - l[i])
            if aa:
                if l[i] in pairs:
                    pairs[l[i]].append((aa, l[j]))
                else:
                    pairs[l[i]] = [(aa, l[j])]

    # Iterably build the peptide starting with the smallest fragment mass.
    peptide = build_peptide(n, pairs)

    # Return the completed peptide of length n.
    return peptide


def main():
    with open("problem_datasets/rosalind_full.txt", "r") as infile:
        p = float(infile.readline().strip())
        frags = list(map(float, infile.readlines()))

    print(peptide_from_fragments(p, frags))


if __name__ == "__main__":
    main()
