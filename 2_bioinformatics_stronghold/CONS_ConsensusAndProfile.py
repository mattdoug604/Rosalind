#!/usr/bin/python
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

import re

# Read FASTA formatted lines into seperate strings
seqs = ""
dna = open("rosalind_cons.txt", "r")
for line in dna:
    if not re.search(r'^>.+$\n', line):
        seqs += line.strip()
    else:
        seqs += "\n"
dna.close()
seqs = seqs.lstrip().split('\n') # lstrip() removes leading newline, spaces, etc.

# Establish a profile matrix
matrix = [[0 for x in xrange(len(seqs[0]))] for y in xrange(len(seqs))]
x = 0
for i in seqs:
    for j in i:
        matrix[x].remove(0)
        matrix[x].append(j)
    x += 1

# Print matrix (optional)
s = [[str(e) for e in row] for row in matrix]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table), '\n'

# Count nt occurences at each position
a_count = [0 for x in xrange(len(seqs[0]))]
c_count = [0 for x in xrange(len(seqs[0]))]
g_count = [0 for x in xrange(len(seqs[0]))]
t_count = [0 for x in xrange(len(seqs[0]))]

for x in range(len(matrix)):
    for y in range(len(seqs[0])):
        if "a" in matrix[x][y].lower():
            a_count[y] += 1
        elif "c" in matrix[x][y].lower():
            c_count[y] += 1
        elif "g" in matrix[x][y].lower():
            g_count[y] += 1
        elif "t" in matrix[x][y].lower():
            t_count[y] += 1

# Determine the consensus sequence
cons = []
for i in range(len(seqs[0])):
    count = []
    count.append(a_count[i])
    count.append(c_count[i])
    count.append(g_count[i])
    count.append(t_count[i])

    if count.index(max(count)) == 0:
        cons.append("A")
    elif count.index(max(count)) == 1:
        cons.append("C")
    elif count.index(max(count)) == 2:
        cons.append("G")
    elif count.index(max(count)) == 3:
        cons.append("T")
    else:
        cons.append("?")
        
# Print results
print (''.join(map(str, cons)))
print "A:", (' '.join(map(str, a_count)))
print "C:", (' '.join(map(str, c_count)))
print "G:", (' '.join(map(str, g_count)))
print "T:", (' '.join(map(str, t_count)))
