#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Transitions and Transversions
URL: http://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
'''

def parseTwoFastas(fasta):
    lines = []
    headers = []
    s1, s2 =('', '')
    
    for i, line in enumerate(fasta.readlines()):
        lines.append(line.strip())
        if line.startswith('>'):
            headers.append(i)

    for j in range(len(lines)):
        if j > headers[0] and j < headers[1]:
            s1 += lines[j]
        elif j > headers[1]:
            s2 += lines[j]
        
    return(s1, s2)

def pointMutations(s1, s2):
    transitions, transversions = (0.0, 0.0)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == 'A' and s2[i] == 'G':
                transitions += 1
            elif s1[i] == 'G' and s2[i] == 'A':
                transitions += 1
            elif s1[i] == 'C' and s2[i] == 'T':
                transitions += 1
            elif s1[i] == 'T' and s2[i] == 'C':
                transitions += 1
            else:
                transversions += 1
    
    if transversions != 0:
        return(transitions/transversions)

def main():
    with open('problem_datasets/rosalind_tran.txt', 'r') as infile:
        s1, s2 = parseTwoFastas(infile)

    answer = pointMutations(s1, s2)
    print(answer)

if __name__ == '__main__':
    main()
