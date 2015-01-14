#!/usr/bin/python
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated

from __future__ import division
import re

text = open('rosalind_gc.txt', 'r')
dna = text.read()

beg = []
end = []
nam = []
cnt = []
tot = []

for i in re.finditer('>.+\n',dna):
    beg.append(i.start())
    end.append(i.end())

for j in range(len(beg)):
    nam.append(dna[beg[j]+1:end[j]-1])

    if(j < len(beg)-1):
        z = dna[end[j]:beg[j+1]-1].replace('\n','')
    else:
        z = dna[end[j]:len(dna)].replace('\n','')
        
    cnt.append(z.count('G')+z.count('C'))
    tot.append(len(z))
    z = ''

text.close()

gc = [int(a)/int(b)*100 for a, b in zip(cnt, tot)]
max = gc.index(max(gc))
print nam[max],'\n',"%.6f" % float(gc[max])
