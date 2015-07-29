#!/usr/bin/python

''' This file contains a bunch of functions that I've been using in many of the
    Rosalind problems.
'''

def parseFasta(path):
    ''' Reads a text file containing one or more FASTA sequences and returns a
        dictionary of ids and corresponding sequences.
    '''
    fastas = {}
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                head = line[1:].strip()
                fastas[head] = ''
            else:
                fastas[head] += line.strip()

    return(fastas)


def codonTable(seq_type='dna'):
    ''' Builds a dictionary of codons and corresponding amino acids '''
    bases = ["T", "C", "A", "G"]
    if seq_type == 'rna':
        bases[0] = 'U'
    
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)


def check_nwck(file):
    from io import StringIO
    from Bio import Phylo
    import networkx

    answers = []
    
    with open(file, 'r') as f:
        lines = map(lambda l: l.strip(), f.readlines())
        lines = [line for line in lines if line]

    for i in range(int(len(lines)/2)):
        handle = StringIO(lines[2*i])
        tree = Phylo.read(handle, "newick")
        names = lines[2*i+1].split()

        t =  Phylo.to_networkx(tree)

        na = [node for node in t.nodes() if node.name == names[0]][0]
        nb = [node for node in t.nodes() if node.name == names[1]][0]

        answers.append(len(networkx.shortest_path(t, na, nb))-1)

    return(answers)
