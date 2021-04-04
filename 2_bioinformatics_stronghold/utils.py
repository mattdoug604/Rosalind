#!/usr/bin/env python3
"""
This file contains a collection of functions that I've been using frequently
in the Rosalind problems.
"""
from os.path import dirname, join

BLOSUM62_PATH = join(dirname(__file__), "data", "BLOSUM62.txt")
DNAFULL_PATH = join(dirname(__file__), "data", "DNAfull.txt")
PAM250_PATH = join(dirname(__file__), "data", "PAM250.txt")

#####################################
### ---------- FILE I/O --------- ###
#####################################


def parse_fasta(path, no_id=True):
    """Read in a Fasta file. If no_id is set to False, return a dictonary of
    sequences with associated headers; otherwise return a list of
    sequences only.
    """
    ids = []
    seqs = []

    with open(path, "r") as f:
        for line in f.readlines():
            if line.startswith(">"):
                ids.append(line[1:].strip())
                seqs.append("")
            else:
                seqs[-1] += line.strip()

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))


def print_matrix(matrix, ylab="", xlab="", outdir=None):
    """Print out the given 2D matrix with axis labels. Matrix rows must be
    the same length.
    """
    # Hold the output for later.
    output = []

    # If the axis won't cover the entire axis, prepend blank spaces. If it is
    # longer than the matrix, strip the extra characters.
    if len(ylab) < len(matrix):
        ylab = " " * (len(matrix) - len(ylab)) + ylab
    elif len(ylab) > len(matrix):
        ylab = ylab[: len(matrix)]

    if len(xlab) < len(matrix[0]):
        xlab = " " * (len(matrix[0]) - len(xlab)) + xlab
    elif len(xlab) > len(matrix[0]):
        xlab = xlab[: len(matrix[0])]

    # Determine the spacing between columns.
    spacing = [0 for i in range(len(matrix[0]) + 1)]
    for i in range(len(matrix[0])):
        max_l = 0
        for j in range(len(matrix)):
            l = len(str(matrix[j][i]))
            if l > max_l:
                max_l = l
                spacing[i + 1] = max_l

    # Print the x-axis.
    spacing[0] = len(max(ylab, key=len))
    x_axis = " " * spacing[0]
    for i, ch in enumerate(xlab):
        x_axis += " " * spacing[i + 1] + ch

    output.append(x_axis)

    # Print each row of the matrix with y-label.
    for i in range(len(matrix)):
        line = ylab[i]
        for j in range(len(matrix[i])):
            line += " " * (spacing[j + 1] - len(str(matrix[i][j])) + 1) + str(matrix[i][j])

        output.append(line)

    # Output each line.
    if outdir != None:
        location = outdir.strip("/") + "/matrix.txt"
        with open(location, "w") as outfile:
            outfile.write("\n".join(output))
    else:
        print("\n".join(output))


#####################################
### --------- MASS SPEC --------- ###
#####################################


def aa_mass(aa):
    """Returns the monoisotopic mass of a given amino acid(s)."""
    mass_table = {
        "A": 71.03711,
        "C": 103.00919,
        "D": 115.02694,
        "E": 129.04259,
        "F": 147.06841,
        "G": 57.02146,
        "H": 137.05891,
        "I": 113.08406,
        "K": 128.09496,
        "L": 113.08406,
        "M": 131.04049,
        "N": 114.04293,
        "P": 97.05276,
        "Q": 128.05858,
        "R": 156.10111,
        "S": 87.03203,
        "T": 101.04768,
        "U": 150.95363,
        "V": 99.06841,
        "W": 186.07931,
        "Y": 163.06333,
    }

    aa = aa.upper()

    # Check for cases of ambiguous amino acids.
    if "B" in aa:
        print("Ambiguity: B can be either Asparagine (N) or Aspartic acid (D)!")
        return None
    if "Z" in aa:
        print("Ambiguity: Z can be either  Glutamine (Q) or Glutamic acid (E)!")
        return None

    mass = 0
    for i in aa:
        try:
            mass += mass_table[i]
        except KeyError:
            print(f"Error: Could not find a mass for an amino acid {i}.")
            return None

    # Return the sum of the monoisotopic masses.
    return mass


def mass_to_aa(val, tolerance=0.0001):
    """Returns the amino acid corresponding to a given mass."""
    # The monoisotopic masses of each
    aa_table = {
        71.03711: "A",
        103.00919: "C",
        115.02694: "D",
        129.04259: "E",
        147.06841: "F",
        57.02146: "G",
        137.05891: "H",
        113.08406: "I",
        128.09496: "K",
        113.08406: "L",
        131.04049: "M",
        114.04293: "N",
        97.05276: "P",
        128.05858: "Q",
        156.10111: "R",
        87.03203: "S",
        101.04768: "T",
        150.95363: "U",
        99.06841: "V",
        186.07931: "W",
        163.06333: "Y",
    }

    # Keep track of the closest match to the given mass. Admittedly this is
    # only useful in certain circumstances...
    closest = ["", 999]

    for mass, aa in aa_table.items():
        diff = abs(val - mass)
        if diff < closest[1]:
            closest = [aa, diff]

        # Return if a match is found.
        if diff < tolerance:
            return aa

    # Print a warning message if no match is found.
    print(f"Note: Could not find an amino acid with monoisotopic mass {val:.5f}.")
    print(" " * 6 + f"Closest match is {closest[0]} (mass difference {closest[1]:.5f}).")


#####################################
### -------- TRANSLATION -------- ###
#####################################


def codon_table(seq_type="rna"):
    """Return a dictionary of codons and corresponding amino acids"""
    bases = ["U", "C", "A", "G"] if seq_type == "rna" else ["T", "C", "A", "G"]

    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return codon_table


#####################################
### --- SEQUENCE MANIPULATION --- ###
#####################################


def reverse_complement(seq):
    """Return the reverse complement of a given DNA or RNA string."""
    if "U" in seq:
        seq_dict = {"A": "U", "U": "A", "G": "C", "C": "G"}
    else:
        seq_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}

    return "".join([seq_dict[base] for base in reversed(seq)])


#####################################
### ----- SEQUENCE ALIGNMENT ---- ###
#####################################


def BLOSUM62():
    return scoring_matrix(BLOSUM62_PATH)


def PAM250():
    return scoring_matrix(PAM250_PATH)


def scoring_matrix(path):
    """Read a text file of a scoring matrix and return a list of scores. The
    first element in the list is the amino acids.
    """
    with open(path, "r") as f:
        lines = f.read().strip().split("\n")

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return scores


def match_score(scoring_matrix, a, b):
    """Return the score from the scoring matrix."""
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x + 1][y])

    return cost
