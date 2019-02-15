import unittest

class GeneNameMapperTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_gene_symbol(self):
        import gene_name_mapper
        gene_symbols = gene_name_mapper.get_gene_symbol(['NM_001320', 'NM_001178126', 'NM_001136213'])
        print(gene_symbols)
        self.assertEqual(gene_symbols, ['CSNK2B', 'IGLL5', 'POTEH'])

if __name__ == '__main__':
    unittest.main()

