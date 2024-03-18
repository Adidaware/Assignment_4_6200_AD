""" This program finds common categories and exports them in OUTPUT/categories.txt """
import argparse
from assignment4.io_utils import mkdir_from_infile
from assignment4.assignment4_utils import read_gene_data


def get_cli_args():
    """ Defined function to parse command line arguments """
    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', type=str, default='chr21_genes.txt',
                        help='Path to the gene description file to open')
    parser.add_argument('-i2', '--infile2', type=str, default='HUGO_gene.txt',
                        help='Path to the gene category file to open')
    return parser.parse_args()


def main():
    """ Defining main """
    args = get_cli_args()
    category_dict = {}
    description_dict = {}

    gene_data1 = read_gene_data(args.infile1)
    gene_data2 = read_gene_data(args.infile2)

    for _gene, (description, category) in gene_data1.items():
        category_dict[category] = category_dict.get(category, 0) + 1
        description_dict[category] = description

    for _gene, (description, category) in gene_data2.items():
        category_dict[category] = category_dict.get(category, 0) + 1
        description_dict[category] = description

    outfile = "OUTPUT/categories.txt"
    mkdir_from_infile(file=outfile)
    with open(outfile, 'w', encoding='utf-8') as file:
        file.write("Category\tCount\tDescription\n")
        for category, count in sorted(category_dict.items()):
            description = description_dict.get(category, "")
            file.write(f"{category}\t{count}\t{description}\n")


if __name__ == "__main__":
    main()
