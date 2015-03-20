#!/usr/bin/python

from rosalind_functions import parseFasta

def longestMotif(seq_list):
    ''' Finds the longest common substring (motif) from all the sequences.
        Note: the script only returns the *first* motif it finds '''
    first_seq = min(seq_list, key=len)
    k = len(first_seq)
    
    for i in range(k, 1, -1):
        for j in range(k-i+1):
            motif = first_seq[j:j+i]
            found = 1
            
            for seq in seq_list:
                s = seq.find(motif)
                if s == -1:
                    found = 0
                    break

            if found == 1:
                return(motif)

    return('no common substring found')
            

def main():
    ''' Read a collection of DNA strings in FASTA format '''
    sequences = list(parseFasta('rosalind_lcsm.txt').values())

    answer = longestMotif(sequences)
    print(answer)

if __name__ == '__main__':
    main()
