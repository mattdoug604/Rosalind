#!/usr/bin/env Rscript

getSkew <- function(fasta) {
    
    ## ----- Get header ----- ##
    header <- substring(fasta[1], 5, 12)
    
    ## ----- Process File ----- ##
    genome <- paste(fasta[2:length(fasta)], collapse="")
    
    ## Get genome length
    len <- nchar(genome)
    
    ## Split genome into characters
    nucleo = substring(fasta, 1:len, 1:len)
    
    ## ------ Get Results ------ ##
    
    ## Create data frame to hold results
    results <- vector(length=len)
    skew <- 0
    
    ## Loop through each nucleotide
    for(i in 1:len) {
        if(nucleo[i] == "C") {
              skew <- skew-1
        }
        else if(nucleo[i] == "G") {
              skew <- skew+1
        }
        
        results[i] <- skew
    }
    
    write.table(results, file=paste(header,"_skew.txt", sep=""))
}

minSkew <- function(x) {
    skew <- read.table(x)
    
    answer <- paste("Min:", min(skew), "at position", which.min(skew), ",", 
                    "Max:", max(skew), "at position", which.max(skew))
}