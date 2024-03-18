""" This functions defined in this module are later imported in the assignment 4 """


def read_gene_data(infile):
    """ Reads gene data from a file and returns a dictionary mapping gene symbols to descriptions. """
    gene_data = {}
    with open(infile, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 3:  # Ensure there are at least two parts before unpacking
                gene_symbol, description = parts[:2]
                gene_data[gene_symbol.upper()] = description
    return gene_data


def count_categories(file1, file2):
    """ Counts how many genes are in each category based on data from two files. """
    category_counts = {}
    with open(file1, 'r', encoding="utf-8") as f1_h, open(file2, 'r', encoding="utf-8") as f2_h:
        for line in f1_h:
            category = line.strip().split('\t')[0]
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
        for line in f2_h:
            category = line.strip().split('\t')[0]
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
    return category_counts


def find_intersection(infile1, infile2):
    """ Finds all gene symbols that appear both in the first and second file. """
    gene_data1 = set(read_gene_data(infile1).keys())
    gene_data2 = set(read_gene_data(infile2).keys())
    return gene_data1.intersection(gene_data2)
