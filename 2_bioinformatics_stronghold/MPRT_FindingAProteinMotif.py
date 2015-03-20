#!/usr/bin/python
# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

# N-glycosylation motif is denoted by: "N{P}[ST]{P}"
# where "[ST]" means "either S or T" and "{P}" means "any except P"

import re

def ParseFasta(file_name):
    heads = []
    seqs = {}

    with open(file_name, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                heads.append(num)
    heads.append(sum(1 for line in open(file_name)))

    f = open(file_name, 'r')
    lines = f.readlines()
    for i in range(len(heads)-1):
        h = lines[heads[i]].replace('\n', '')
        l = lines[heads[i]+1:heads[i+1]]
        seqs[h] = ''.join(l).replace('\n', '')

    return seqs

def FindMotif(head, seq, pattern):
    results = []
    
    header = re.compile(r'\|.{,20}([A-Z]\s)')
    head = header.search(head).group()
    head = head[1:].replace('|', '_')
    
    pat = re.compile(pattern)
    for i in range(len(seq)):
        if pat.match(seq[i:i+4]):
            results.append(i+1)
    if len(results) != 0:
        out = head, ' '.join(map(str, results))
    else:
        out = head, '**no N-glycosylation motif found!'
    return out

fasta = 'rosalind_motifs.txt'
seq_dict = ParseFasta(fasta)
for seq in seq_dict:
    out = FindMotif(seq, seq_dict[seq], '^N[A-O,Q-Z](S|T)[A-O,Q-Z]')
    if not out[1].startswith('**'):
        print '\n'.join(map(str, out))
