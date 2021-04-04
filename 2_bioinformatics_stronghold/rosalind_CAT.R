#!/usr/bin/env Rscript

readFasta <- function(f) {
    # Parse a text file containing a single FASTA formatted sequence and return it as a character vector
    input <- read.csv(f)
    
    seq <- ""
    for(i in 1:nrow(input)) {
        seq <- paste(seq, input[[1]][i], sep="")
    }
    
    return(strsplit(seq, split="")[[1]])
}

countMatchings <- function(i, j) {
    # No need to redo any calculation we've done before...
    if(pairs[i, j] != -1) {
        return(pairs[i, j])
    }
    
    result <- 0
    if(i > j) {
        result <- 1
    }
    else if(j == 2 && bases[seq[i]] == bases[seq[j]]) {
        result <- 1
    }
    else {
        for(k in seq(i+1, j+1, by=2)) {
            if(seq[k] == bases[seq[i]]) {
                result <- result + countMatchings(i+1, k-1) * countMatchings(k+1, j)
            }
        }
    }
    
    pairs[i, j] <<- result %% 1000000
    return(result)
}

# Set the list of base pair matches
bases <- c("U", "A", "G", "C")
names(bases) <- c("A", "U", "C", "G")

# Read in the sequence
seq <- readFasta("problem_datasets/rosalind_cat.txt")

# Declare a score matrix of size x^2, where x = length of the sequence + 1
pairs <- matrix(-1, nrow=length(seq)+1, ncol=length(seq)+1)

# Calculate the number of base pair modulo 1,000,000
matches <- countMatchings(1, length(seq))
print(matches %% 1000000)
