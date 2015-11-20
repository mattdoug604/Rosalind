#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Creating a Character Table
URL: http://rosalind.info/problems/ctbl/

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The 
columns of the character table should encode the taxa ordered 
lexicographically; the rows of the character table may be given in any order. 
Also, for any given character, the particular subset of taxa to which 1s are 
assigned is arbitrary.
'''

import re

def parse_taxa(t):
    # Parse the Newick tree to get an alphabetical list of all the taxa. 
    return sorted(re.sub('[^0-9a-zA-Z_]+', ' ', t).strip().split(' '))
    

def char_table_from_newick(t):
    # Initialize the character table.
    char = []
    
    # Dictionary of each taxa's index in the character table.
    taxa = parse_taxa(t)
    taxa_dict = {i:taxa.index(i) for i in taxa}
    
    # Keep track of the subtrees.
    level = 0
    pos = []
    subtrees = []
    
    # Sort the tree into levels.
    for i in range(len(t)):
        if t[i] == '(':
            level += 1
            pos.append(i)
        elif t[i] == ')':
            sub = t[pos[-1]+1:i]
            del pos[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(sub)
            level -= 1
    
    # Fill in the character table.
    for i in range(1, len(subtrees)):
        for j in subtrees[i]:
            char.append([0 for i in range(len(taxa_dict))])
            
            for k in parse_taxa(j):
                char[-1][taxa_dict[k]] = 1
    
    # Return the character table.
    return char
    
    
def main():
    with open('problem_datasets/rosalind_ctbl.txt', 'r') as infile:
        tree = infile.read().strip()
    
    answer = char_table_from_newick(tree)
    
    with open('output/rosalind_ctbl_out.txt', 'w') as outfile:
        outfile.write('\n'.join([''.join(map(str, answer[i])) for i in range(len(answer))]))


if __name__ == '__main__':
    main()