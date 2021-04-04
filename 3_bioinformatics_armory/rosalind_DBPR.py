#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Armory
Problem: Introduction to Protein Databases
URL: http://rosalind.info/problems/dbpr/

Given: The UniProt ID of a protein.
Return: A list of biological processes in which the protein is involved
(biological processes are found in a subsection of the protein's "Gene Ontology"
(GO) section).
"""

from Bio import ExPASy, SwissProt


def main():
    # Read the UniProt ID for a txt file.
    with open("problem_datasets/rosalind_dbpr.txt", "r") as infile:
        uni_id = infile.read().strip()

    # Retrieve the data from UniProt (separated IDs by commas).
    raw_data = ExPASy.get_sprot_raw(uni_id)
    record = SwissProt.read(raw_data)  # use SwissProt.parse for multiple proteins

    # Collect the relevant information.
    go = []
    for i in record.cross_references:
        if i[2].startswith("P:"):
            go.append(i[2][2:])

    # Output answer.
    with open("output/rosalind_dbpr_out.txt", "w") as outfile:
        outfile.write("\n".join(go))

    # Optional: Print answer and gene ID/name
    name = record.gene_name.split(" ")[0][5:]
    print(
        "Gene:\n",
        name,
        " (UniProt ID = ",
        uni_id,
        ")\n\nBiological Processes:\n",
        "\n".join(go),
        sep="",
    )


if __name__ == "__main__":
    main()
