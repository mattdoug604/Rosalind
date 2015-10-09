#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Overlap Alignment
URL: http://rosalind.info/problems/gap/

Given: Two DNA strings s and t in FASTA format, each having length at most 10 
kbp.

Return: The score of an optimal overlap alignment of s and t, followed by an 
alignment of a suffix s′ of s and a prefix t′ of t achieving this optimal 
score. Use an alignment score in which matching symbols count +1, 
substitutions count -2, and there is a linear gap penalty of 2. If multiple 
optimal alignments exist, then you may return any one.
'''

from rosalind_utils import parse_fasta

def semiglobal_align(s, t):
    # Initialize the distance and traceback matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    # Fill in the matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j] - 2,
                      d[i][j-1] - 2,
                      d[i-1][j-1] + [-2, 1][s[i-1] == t[j-1]]]
            d[i][j] = max(scores)
            traceback[i][j] = scores.index(d[i][j])
            
    # The max score can be found either along the last column or last row.
    last_row = d[-1]
    last_col = [d[i][-1] for i in range(len(d))]

    if max(last_row) >= max(last_col):
        i = len(s)
        j = last_row.index(max(last_row))
    else:
        i = last_col.index(max(last_col))
        j = len(t)
        
    max_score = d[i][j]
    
    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # Append insertions/deletions as necessary.
    for dash in range(len(s) - i):
        t_align += '-'
    for dash in range(len(t) - j):
        s_align += '-'
    
    # Traceback to the matrix edge starting at the index of the max score.
    while i>0 and j>0:
        if traceback[i][j] == 0:
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif traceback[i][j] == 1:
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else:
            i -= 1
            j -= 1
            
    print(i, s_align, j, t_align)

    # Prepend insertions/deletions as necessary.
    for dash in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return str(max_score), s_align, t_align
    
    
def main():
    s, t = parse_fasta('problem_datasets/rosalind_gap.txt')    
    
    alignment = semiglobal_align(s, t)
    
    with open('output/rosalind_gap_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    print('-'*37 + 'ANSWER' + '-'*37)
    with open('output/rosalind_gap_out.txt', 'r') as answer:
        print(answer.read())


if __name__ == '__main__':
    main()

# Answer:
# 1
# ATTAGAC-AG
# AT-AGACCAT