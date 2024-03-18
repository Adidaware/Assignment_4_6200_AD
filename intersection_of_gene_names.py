""" This program is designed to find common gene symbols between two files. """
import argparse
from assignment4.io_utils import mkdir_from_infile


def get_cli_args():
    """ Defined function to parse command line arguments """
    parser = argparse.ArgumentParser(description='Provide two gene list (ignore header line), find intersection')
    parser.add_argument('-i1', '--infile1', type=str, default='chr21_genes.txt', help='Gene list 2 to open')
    parser.add_argument('-i2', '--infile2', type=str, default='HUGO_genes.txt', help='Gene list 2 to open')
    return parser.parse_args()


def main():
    """ Defining main """
    args = get_cli_args()
    chr21_genes = set()
    hugo_genes = set()
    with open(args.infile1, 'r', encoding='utf-8') as file:
        next(file)  # skip the header row
        for line in file:
            gene_symbol = line.strip().split('\t')[0]
            chr21_genes.add(gene_symbol.upper())
    with open(args.infile2, 'r', encoding='utf-8') as file:
        next(file)  # Skip the header row
        for line in file:
            gene_symbol = line.strip().split('\t')[0]
            hugo_genes.add(gene_symbol.upper())

    common_genes = chr21_genes & hugo_genes
    outfile = "OUTPUT/intersection_output.txt"
    mkdir_from_infile(file=outfile)
    with open(outfile, 'w', encoding='utf-8') as file:
        for gene_symbol in sorted(common_genes):
            file.write(f"{gene_symbol}\n")

    print(f"Number of unique gene names in chr21_genes.txt: {len(chr21_genes)}")
    print(f"Number of unique gene names in HUGO_genes.txt: {len(hugo_genes)}")
    print(f"Number of common gene symbols found: {len(common_genes)}")
    print("Output stored in OUTPUT/intersection_output.txt")


if __name__ == "__main__":
    main()
