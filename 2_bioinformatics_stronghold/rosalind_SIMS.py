#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Finding a Motif with Modifications
URL: http://rosalind.info/problems/sims/

Given: Two DNA strings s and t, where s has length at most 10 kbp and t 
represents a motif of length at most 1 kbp.

Return: An optimal fitting alignment score with respect to the mismatch score 
(a match = +1, any mismatched symbol = -1), followed by an optimal fitting 
alignment of a substring of s against t. If multiple such alignments exist, 
then you may output any one.
'''

from rosalind_utils import parse_fasta

def fitting_alignment(s, t):
    # Initialize the score and traceback matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    # Fill in the matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j] - 1,
                      d[i][j-1] - 1,
                      d[i-1][j-1] + (1 if s[i-1] == t[j-1] else -1),
                      0]
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
        
    score = d[i][j]
    
    # Initialize the aligned strings.
    s_align, t_align = s[:i], t
    
    # Traceback from the max score at one edge of the matrix.
    while i*j > 0:
        if traceback[i][j] == 0:
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif traceback[i][j] == 1:
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else:
            i -= 1
            j -= 1
    
    # Trim the beginning of the string, up to where the alignment starts.
    s_align = s_align[i:]
    
    # Calculate the alignment score of two equal length sequences.
    score = sum([[-1, 1][s_align[i]==t_align[i]] for i in range(len(s_align))])        
    
    # Return the score and alignment.
    return str(score), s_align, t_align

    
def main():
    # Read in the two sequences.
    s, t = parse_fasta('problem_datasets/rosalind_sims.txt')
    
    # Get the alignment.
    alignment = fitting_alignment(s, t)

    # Save the answer.
    with open('output/rosalind_sims_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    # Optional: Print the alignment score.
    print('Optimal fitting alignment score =', alignment[0])
        
   
if __name__ == '__main__':
    main()