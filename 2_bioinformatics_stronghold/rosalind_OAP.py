#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Overlap Alignment
URL: http://rosalind.info/problems/oap/

Given: Two DNA strings s and t in FASTA format, each having length at most 10 
kbp.

Return: The score of an optimal overlap alignment of s and t, followed by an 
alignment of a suffix s′ of s and a prefix t′ of t achieving this optimal 
score. Use an alignment score in which matching symbols count +1, 
substitutions count -2, and there is a linear gap penalty of 2. If multiple 
optimal alignments exist, then you may return any one.
"""

from rosalind_utils import parse_fasta


def overlap_align(s, t):
    # Initialize the score and traceback matrices with zeros.
    d = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceback = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Fill in the matrices: matches = 1, mismatches/gaps = -2.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            scores = [
                d[i - 1][j] - 2,
                d[i][j - 1] - 2,
                d[i - 1][j - 1] + [-2, 1][s[i - 1] == t[j - 1]],
            ]
            d[i][j] = max(scores)
            traceback[i][j] = scores.index(d[i][j])

    # The max score can be found either along the last column or last row.
    last_row = d[-1]
    last_col = [d[i][-1] for i in range(len(d))]

    # A valid alignment can be found by starting with any occurance of the
    # maximum score (if there is more than one). However, we'll use the
    # following bit of code to find the longest alignment.
    mr = max(last_row)
    mc = max(last_col)

    row_ind, row_max = [(i, j) for i, j in enumerate(last_row) if j == mr][-1]
    col_ind, col_max = [(i, j) for i, j in enumerate(last_col) if j == mc][-1]

    if row_max > col_max:
        i = len(s)
        j = row_ind
    elif row_max < col_max:
        i = col_ind
        j = len(t)
    else:
        if row_ind > col_ind:
            i = len(s)
            j = row_ind
        else:
            i = col_ind
            j = len(t)

    max_score = d[i][j]

    # Initialize the aligned strings as the input strings up to the occurance
    # of the max score found above.
    s_align, t_align = s[:i], t[:j]

    # Traceback to the matrix edge starting at the index of the max score.
    while i * j > 0:
        if traceback[i][j] == 0:
            i -= 1
            t_align = t_align[:j] + "-" + t_align[j:]
        elif traceback[i][j] == 1:
            j -= 1
            s_align = s_align[:i] + "-" + s_align[i:]
        else:
            i -= 1
            j -= 1

    # Trim the string of the part preceeding the alignment.
    s_align = s_align[i:]

    # Return the score and alignment.
    return str(max_score), s_align, t_align


def main():
    # Read in the two strings.
    s, t = parse_fasta("problem_datasets/rosalind_oap.txt")

    # Find the alignment.
    alignment = overlap_align(s, t)

    # Output the answer.
    with open("output/rosalind_oap_out.txt", "w") as outfile:
        outfile.write("\n".join(alignment))

    # Optional: Print the max alignment score.
    print("Maximum alignment score =", alignment[0])


if __name__ == "__main__":
    main()
