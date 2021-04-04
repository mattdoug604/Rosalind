#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Local Alignment with Scoring Matrix
URL: http://rosalind.info/problems/loca/

Given: Two protein strings s and t in FASTA format (each having length at most
1000 aa).
Return: A maximum alignment score along with substrings r and u of s and t,
respectively, which produce this maximum alignment score (multiple solutions may
exist, in which case you may output any one). Use:
    - The PAM250 scoring matrix.
    - Linear gap penalty equal to 5.
 
EXAMPLE INPUT:
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

EXAMPLE OUTPUT:
(note: this is correct, but different than Rosalind sample output):
23
MEANLYPRTEINSTRIN
LEASANTLYEINSTEIN
"""

from rosalind_utils import PAM250, match_score, parse_fasta


def alignment_score(s, t, scores, gap):
    """Returns two matrices of the edit distance and edit alignment between
    strings s and t.
    """

    # Initialize the similarity and traceback matrices.
    S = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceback = [[3 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    best = 0
    best_pos = (0, 0)

    # Fill in the matrices.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            cost = [
                S[i - 1][j - 1] + match_score(scores, s[i - 1], t[j - 1]),
                S[i - 1][j] + gap,
                S[i][j - 1] + gap,
                0,
            ]
            S[i][j] = max(cost)
            traceback[i][j] = cost.index(S[i][j])

            if S[i][j] >= best:
                best = S[i][j]
                best_pos = (i, j)

    # Initialize the values of i,j as the index of the highest score.
    i, j = best_pos

    # Initialize the aligned strings as the prefix of the best position.
    r, u = s[:i], t[:j]

    # Trace back to the edge of the matrix starting at the best position.
    while traceback[i][j] != 3 and i * j != 0:
        if traceback[i][j] == 0:  # a match
            i -= 1
            j -= 1
        elif traceback[i][j] == 1:  # an insertion
            i -= 1
        elif traceback[i][j] == 2:  # a deletion
            j -= 1

    # The optimal alignment is then the suffix of the end of the traceback.
    r = r[i:]
    u = u[j:]

    return str(best), r, u


def main():
    s, t = parse_fasta("problem_datasets/rosalind_loca.txt")
    alignment = alignment_score(s, t, PAM250(), -5)

    with open("output/rosalind_loca_out.txt", "w") as outfile:
        outfile.write("\n".join(alignment))

    print("Maximum alignment score =", alignment[0])


if __name__ == "__main__":
    main()
