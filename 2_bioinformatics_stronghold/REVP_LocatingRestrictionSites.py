#!/usr/bin/python
# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

def dsDNA(seq):
    seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    return ''.join([seq_dict[base] for base in reversed(seq)])

infile = open('rosalind_revp.txt', 'r')

s = ''
while True:
    line = infile.readline().strip()
    if line == '':
        break
    if not line.startswith('>'):
        line.replace('\n', '')
        s += line

t = dsDNA(s)
for i in range(4, 13, 2):
    for j in range(len(s)):
        fwd = s[j:j+i]
        rev = t[len(t)-j-i:len(t)-j]
        if fwd == rev:
            print j+1, i
