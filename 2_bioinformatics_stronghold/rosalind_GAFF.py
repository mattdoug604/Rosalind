#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Scoring Matrix and Affine Gap Penalty
URL: http://rosalind.info/problems/gaff/

Given: Two protein strings s and t in FASTA format (each of length at most 100
aa).
Return: The maximum alignment score between s and t, followed by two augmented
strings s′ and t′ representing an optimal alignment of s and t. Use:
    - The BLOSUM62 scoring matrix.
    - Gap opening penalty equal to 11.
    - Gap extension penalty equal to 1.

EXAMPLE INPUT:
>Rosalind_49
PRTEINS
>Rosalind_47
PRTWPSEIN

EXAMPLE OUTPUT:
8
PRT---EINS
PRTWPSEIN-
"""

from utils import BLOSUM62, match_score, parse_fasta


def global_align_with_affine(s, t, scores, gap, gap_e):
    """Returns two matrices of the edit distance and edit alignment between
    strings s and t.
    """
    # Initialize the three score matrices...
    M = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]  # a (mis)match
    X = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]  # a gap in X
    Y = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]  # a gap in Y

    # ...and the traceback matrices.
    traceM = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceX = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceY = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Initialize the edges of the X and Y matrices with an arbitrarily
    # large number (closer to negative infinity, the better) so it doesn't
    # affect calculations.
    for i in range(1, len(s) + 1):
        M[i][0] = gap + gap_e * (i - 1)
        X[i][0] = -9999
        Y[i][0] = -9999
    for j in range(1, len(t) + 1):
        M[0][j] = gap + gap_e * (j - 1)
        X[0][j] = -9999
        Y[0][j] = -9999

    # Fill in the matrices.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            costX = [M[i - 1][j] + gap, X[i - 1][j] + gap_e]
            X[i][j] = max(costX)
            traceX[i][j] = costX.index(X[i][j])

            costY = [M[i][j - 1] + gap, Y[i][j - 1] + gap_e]
            Y[i][j] = max(costY)
            traceY[i][j] = costY.index(Y[i][j])

            costM = [M[i - 1][j - 1] + match_score(scores, s[i - 1], t[j - 1]), X[i][j], Y[i][j]]
            M[i][j] = max(costM)
            traceM[i][j] = costM.index(M[i][j])

    # The max possible score is found at the bottom-right of the match matrix
    max_score = M[-1][-1]

    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # Get the traceback starting position, i.e. the greatest value.
    scores = [X[i][j], Y[i][j], M[i][j]]
    max_score = max(scores)
    traceback = scores.index(max_score)

    # Initialize the values of i,j
    i, j = len(s), len(t)

    # Traceback to build alignment.
    while i > 0 and j > 0:
        if traceback == 0:
            if traceX[i][j] == 0:
                traceback = 2
            i -= 1
            t_align = t_align[:j] + "-" + t_align[j:]

        elif traceback == 1:
            if traceY[i][j] == 0:
                traceback = 2
            j -= 1
            s_align = s_align[:i] + "-" + s_align[i:]

        elif traceback == 2:
            if traceM[i][j] == 1:
                traceback = 0
            elif traceM[i][j] == 2:
                traceback = 1
            else:
                i -= 1
                j -= 1

    # Fill in any leading gaps.
    for remaining in range(i):
        t_align = t_align[:0] + "-" + t_align[0:]
    for remaining in range(j):
        s_align = s_align[:0] + "-" + s_align[0:]

    return str(max_score), s_align, t_align


def main():
    s, t = parse_fasta("problem_datasets/rosalind_gaff.txt")
    alignment = global_align_with_affine(s, t, BLOSUM62(), -11, -1)

    with open("output/rosalind_gaff_out.txt", "w") as f:
        f.write("\n".join(alignment))

    print("Maximum alignment score =", alignment[0])


if __name__ == "__main__":
    main()
