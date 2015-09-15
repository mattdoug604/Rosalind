#!/usr/bin/python

'''
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

'''

'''
EXAMPLE INPUT:
1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391	
1221.7188991
1249.7250491
1377.8200091

EXAMPLE OUTPUT:
KEKEP
'''

from rosalind_utils import mass_to_aa

def infer_peptide(p, l):
    add_to = lambda p, x, y: True if abs(p-x-y) < 0.0001 else False

    pairs = []
    for i in range(len(l)):
        for j in range(len(l)-1, i, -1):
            if add_to(p, l[i], l[j]):
                pairs.append((l[i], l[j]))

    for p in pairs:
        print(p)
    print()
    
    for x in range(len(pairs)):
        for i in pairs[x]:
            for y in range(len(pairs)-1, x, -1):
                for j in pairs[y]:
                    aa = mass_to_aa(abs(i-j))
                    if aa != '*':
                        print(i, j, aa)
    print()


def main():
    # The first line of the input file is the parent mass, the rest are the
    # masses of the b- and y-ions (in no particular order).
    with open('problem_datasets/rosalind_test.txt', 'r') as infile:
        p = float(infile.readline().strip())
        l = list(map(float, infile.read().strip().split('\n')))

    # Print answer.
    print(infer_peptide(p, l))
        

if __name__ == '__main__':
    main()
