dat = open("problem_datasets/rosalind_eval.txt").read().split('\n')

n = int(dat[0])
string = dat[1]
B = [float(x) for x in dat[2].split(" ")]

## probability that we find a substring of length 'n' in string
num_GC = sum( [x == "C" or x == "G" for x in string] )
num_AG = len(string) - num_GC

for gc_content in B:
    prob = gc_content ** num_GC * (1-gc_content) ** num_AG
    print( num_GC * prob + num_AG * (1-prob) )
