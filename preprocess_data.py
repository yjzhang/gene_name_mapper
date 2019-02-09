import pandas as pd
import sqlite3

gene_names_data = pd.read_table('homo_sapiens_gene_names.txt')
table = gene_names_data[['HGNC ID', 'Approved symbol', 'Previous symbols',
        'Synonyms', 'Accession numbers', 'RefSeq IDs', 'NCBI Gene ID',
        'Ensembl gene ID']]
table['NCBI Gene ID']
conn = sqlite3.connect('data/genes.db')
c = conn.cursor()
table.to_sql('gene_names_homo_sapiens', conn)

# TODO: create indices
c.execute('CREATE INDEX refseq_index ON gene_names_homo_sapiens("RefSeq IDs")')
c.execute('CREATE INDEX symbol_index ON gene_names_homo_sapiens("Approved symbol")')
c.execute('CREATE INDEX ensembl_index ON gene_names_homo_sapiens("Ensembl gene ID")')
