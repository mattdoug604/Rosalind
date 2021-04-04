#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Armory
Problem: New Motif Discovery
URL: http://rosalind.info/problems/meme/

The novel-motif finding tool MEME can be found here:
http://meme-suite.org/tools/meme

Given: A set of protein strings in FASTA format that share some motif with
minimum length 20.
Return: Regular expression for the best-scoring motif.
"""


def main():
    regex = ""

    # Read the plain text file output by the MEME tool.
    with open("output/meme.output.txt", "r") as f:
        for line in f:
            if "regular expression" in line:
                next(f)
                while True:
                    line = f.readline()
                    if "-" not in line:
                        regex += line.rstrip()
                    else:
                        break

    # Output the answer.
    with open("output/rosalind_meme_out.txt", "w") as outfile:
        outfile.write(regex)

    # Optional: Print the answer.
    print("Regular expression =", regex)


if __name__ == "__main__":
    main()
