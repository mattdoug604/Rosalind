#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Overlap Graphs
URL: http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
'''

def parseFasta(path):
    headers = []
    seqs = {}

    with open(path, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                headers.append(num)
    headers.append(sum(1 for line in open(path)))

    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(len(headers)-1):
            h = lines[headers[i]][1:].replace('\n', '')
            l = lines[headers[i]+1:headers[i+1]]
            seqs[h] = ''.join(l).replace('\n', '')

    return(seqs)

def overlapSeqs(sequences):
    for head1, seq1 in sequences.iteritems():
        suffix = seq1[-3:]
        for head2, seq2 in sequences.iteritems():
            prefix = seq2[:3]
            if seq1 <> seq2:
                if suffix == prefix:
                    yield(' '.join([head1, head2]))

def main():
    dataset = parseFasta("problem_datasets/rosalind_grph.txt")
    
    with open('output/rosalind_grph_out.txt', 'w') as outfile:
        for line in overlapSeqs(dataset):
            outfile.write(line + '\n')

if __name__ == '__main__':
    main()
