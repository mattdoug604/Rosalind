#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Multiple Alignment
URL: http://rosalind.info/problems/mult/

Given: A collection of four DNA strings of length at most 10 bp in FASTA 
format.

Return: A multiple alignment of the strings having maximum score, where we 
score matched symbols 0 (including matched gap symbols) and all mismatched 
symbols -1 (thus incorporating a linear gap penalty of 1).
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_mult.txt")


def alignment_score(s, t):
    # Initialize the distance and traceback matrices with zeros.
    d = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceback = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Each cell in the first row and column recieves a gap penalty (-1).
    for i in range(1, len(s) + 1):
        d[i][0] = -i
    for j in range(1, len(t) + 1):
        d[0][j] = -j

    # Fill in the distance and traceback matrices.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            scores = [
                d[i - 1][j - 1] - (s[i - 1] != t[j - 1]),  # 0 = match
                d[i - 1][j] - 1,  # 1 = insertion
                d[i][j - 1] - 1,
            ]  # 2 = deletion
            d[i][j] = max(scores)
            traceback[i][j] = scores.index(d[i][j])

    # The edit distance the last cell (bottom-right) of the distance matrix.
    score = d[-1][-1]

    # print_matrix(d, s, t)
    # print()
    # print(s, ', ', t, ' -> ', score, sep='')

    return score, traceback


def align_sequences(s, t, traceback):
    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # traceback to the edge of the matrix starting at the bottom right.
    i, j = len(s), len(t)

    while i > 0 and j > 0:
        if traceback[i][j] == 1:
            i -= 1
            t_align = t_align[:j] + "-" + t_align[j:]
        elif traceback[i][j] == 2:
            j -= 1
            s_align = s_align[:i] + "-" + s_align[i:]
        else:
            i -= 1
            j -= 1

    # Prepend insertions/deletions if necessary.
    for dash in range(i):
        t_align = t_align[:0] + "-" + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + "-" + s_align[0:]

    return s_align, t_align


def main():
    # Get the collection of sequences.
    # seqs = ['ATATCCG', 'TCCG', 'ATGTACTG', 'ATGTCTG']
    seqs = parse_fasta(INPUT_FILE)

    # Create two arrays to keep track of which sequences are already aligned.
    alignment = ["" for i in seqs]
    remaining = [i for i in range(len(seqs))]

    # Start by aligning the two most similar sequences.
    scores = {}
    for i in range(len(seqs)):
        for j in range(len(seqs) - 1, i, -1):
            scores[(i, j)] = alignment_score(seqs[i], seqs[j])

    a, b = max(scores)
    max_score, matrix = scores[(a, b)]
    alignment[a], alignment[b] = align_sequences(seqs[a], seqs[b], matrix)

    remaining.remove(a)
    remaining.remove(b)

    # Pick the sequence that aligned best to one of the already aligned
    # sequences and align it to the set; repeat until all sequences are
    # aligned.
    while len(remaining) > 0:
        scores = {}
        i = remaining[0]

        for j in range(len(alignment)):
            if alignment[j] != "":
                scores[j] = alignment_score(seqs[i], alignment[j])

        best = max(scores)
        best_score, matrix = scores[best]

        max_score += best_score
        alignment[i], alignment[j] = align_sequences(seqs[i], alignment[best], matrix)

        remaining.remove(i)

    # Calulate the maxumum score
    max_score = 0
    for i in range(len(alignment)):
        for j in range(len(alignment) - 1, i, -1):
            max_score += alignment_score(alignment[i], alignment[j])[0]

    # Output the answer.
    with open("output/rosalind_mult_out.txt", "w") as outfile:
        outfile.write(str(max_score) + "\n")
        outfile.write("\n".join(alignment))

    print("-" * 37 + "ANSWER" + "-" * 37)
    with open("output/rosalind_mult_out.txt", "r") as answer:
        print(answer.read())


if __name__ == "__main__":
    main()

"""
Input:
>Rosalind_2962
GCGGCGTAC
>Rosalind_3274
AACCCTTCT
>Rosalind_9073
ATAGCAAGGA
>Rosalind_8296
CTGGATTT


Correct Answer:
-43
GCGGCGTAC-
AACCCTTCT-
ATAGCAAGGA
CTGGATT-T-
"""
