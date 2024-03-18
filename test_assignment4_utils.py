""" This program is designed to test the functions of assignment4_utils.py """

from assignment4.assignment4_utils import read_gene_data, count_categories, find_intersection


def test_read_gene_data():
    """
    Test the read_gene_data function
    """
    gene_data = read_gene_data('chr21_genes.txt')
    assert isinstance(gene_data, dict)
    assert 'TPTE' in gene_data
    assert gene_data['TPTE'] == 'tensin, putative protein-tyrosine phosphatase, EC 3.1.3.48.'


def test_count_categories():
    """
    Test the count_categories function
    """
    category_counts = count_categories('chr21_genes.txt', 'chr21_genes_categories.txt')
    assert isinstance(category_counts, dict)


def test_find_intersection():
    """
    Test the find_intersection function
    """
    intersection = find_intersection('chr21_genes.txt', 'HUGO_genes.txt')
    assert isinstance(intersection, set)
