#!/usr/bin/env python3
"""
Generate the theoretical spectrum of a cyclic peptide.
Given: An amino acid string Peptide.
Return: Cyclospectrum(Peptide).
"""


def calcMass(frag):
    mass_table = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    mass = 0
    for aa in frag:
        mass += mass_table[aa]
    spectrum.append(mass)


# Note: in this problem, peptides are cyclic
peptide = "SAEDDYCVAGFVT"
spectrum = [0]

for i in range(1, len(peptide)):  # fragment length

    for j in range(len(peptide)):  # starting position
        frag = peptide[j : j + i]

        if len(frag) < i:
            frag = peptide[j : j + len(frag)] + peptide[: i - len(frag)]

        calcMass(frag)

calcMass(peptide)  # calculate the mass of the intact peptide
spectrum = sorted(spectrum, key=int)  # print the spectrum sorted lowest -> highest mass
for val in spectrum:
    print(val)
