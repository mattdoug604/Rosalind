#!/usr/bin/python
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k = 28.0 # homozygous dominant individuals
m = 28.0 # heterozygous
n = 15.0 # homozygous recessive

t = k+m+n # total population

# four different cases that would NOT result in an offspring w/ a dominant allele
c1 = k/t * (k-1)/(t-1) * 1/4
c2 = k/t * n/(t-1) * 1/2
c3 = n/t * k/(t-1) * 1/2
c4 = n/t * (n-1)/(t-1)

print 1-(c1+c2+c3+c4)

# Note: Rosalind only seems to accept answer to first 5 decimal points as correct
