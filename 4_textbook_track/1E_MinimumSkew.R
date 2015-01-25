findSkew <- function(path) {
      ## ----- Process File ----- ##
      
      ## Read in file
      genome <- readLines(path)
      
      ## Get genome length
      len <- nchar(genome)
      
      ## Split genome into characters
      nucleo = substring(genome, 1:len, 1:len)

      ## ------ Get Results ------ ##
      
      ## Create data frame to hold results
      results <- vector(length=len)
      skew <- 0
      
      for(i in 1:len) {
            if(nucleo[i] == "C") {
                  skew <- skew-1
            }
            else if(nucleo[i] == "G") {
                  skew <- skew+1
            }
            
            results[i] <- skew
      }
      
      answer <- paste("Min:", min(results), "at position", which.min(results), ",", 
                      "Max:", max(results), "at position", which.max(results))
      
      lines(results, type="l", xlab="Position", ylab="Skew")
      return(answer)
}