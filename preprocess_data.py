import pandas as pd
import sqlite3

gene_names_data = pd.read_table('homo_sapiens_gene_names.txt')
table = gene_names_data[['HGNC ID', 'Approved symbol', 'Previous symbols',
        'Synonyms', 'Accession numbers', 'RefSeq IDs', 'NCBI Gene ID',
        'Ensembl gene ID']]
conn = sqlite3.connect('data/genes.db')
c = conn.cursor()
table.to_sql('gene_names_homo_sapiens', conn)
# TODO: what if  RefSeq IDs is a list?
for i, row in table.iterrows():
    ids = row['RefSeq IDs']
    if isinstance(ids, str) and ',' in ids:
        print(row)

# create indices
c.execute('CREATE INDEX refseq_index ON gene_names_homo_sapiens("RefSeq IDs")')
c.execute('CREATE INDEX symbol_index ON gene_names_homo_sapiens("Approved symbol")')
c.execute('CREATE INDEX ensembl_index ON gene_names_homo_sapiens("Ensembl gene ID")')

c.commit()
c.close()
conn.close()
