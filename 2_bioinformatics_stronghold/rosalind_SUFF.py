#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Encoding Suffix Trees
URL: http://rosalind.info/problems/suff/

Given: A DNA string s of length at most 1kbp.
Return: The substrings of s∗ encoding the edges of the suffix tree for s.
You may list these substrings in any order.
'''

# - build 'implicit' suffix tree Ti for each prefix s[1..i]
# - first, build T1 using 1st character, then T2 using 2nd character...
# - suffix tree Ti+1 built upon Ti
# - true suffix tree built from Tm (m = len(s)) by adding $

def make_suffix_tree(s):
    tree = []

    # for each letter in s...
    for i in range(len(s)):

        # for s[1...i]...
        for j in range(i):
            suffix = s[j:i]

            # Find the end of the path from the root labelled S[j..i] in the
            # current tree.
            

            # Extend that path by adding character S[i+l] if it is not there
            # already.
            
    
    return tree
    
def main():
    with open('problem_datasets/rosalind_suff.txt', 'r') as infile:
        s = infile.readline().strip()
    
    print('\n'.join(make_suffix_tree(s)))
    
    
if __name__ == '__main__':
    main()
