""" This program is designed to find the gene name based on the user input"""
import argparse


def get_cli_args():
    """ Defined function to parse command line arguments """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and ask user for a gene name')
    parser.add_argument('-i', '--infile', type=str, default='chr21_genes.txt', help='Path to the fh_in to open')
    return parser.parse_args()


def main():
    """ Defining main """
    args = get_cli_args()
    gene_dict = {}
    with open(args.infile, 'r', encoding='utf-8') as file:
        for line in file:
            gene_symbol, description = line.strip().split('\t')[:2]
            gene_dict[gene_symbol.lower()] = description

    while True:
        gene_symbol = input("Enter gene name of interest. Type quit to exit: ").lower()
        if gene_symbol in ['quit', 'exit']:
            print("Thanks for querying the data.")
            break
        if gene_symbol in gene_dict:
            print(f"{gene_symbol.upper()} found! Here is the description:\n{gene_dict[gene_symbol]}")
        else:
            print("Not a valid gene name.")


if __name__ == "__main__":
    main()
