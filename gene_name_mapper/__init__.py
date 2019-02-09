import os
import sqlite3

PATH = os.path.dirname(__file__)
DB_DIR = os.path.join(PATH, 'data', 'genes.db')

def get_gene_symbol(accessions):
    """
    Given a string or list of strings that are either RefSeq ID ('NM_...')
    or Ensembl ID ('ENSG...'), this returns a list of gene symbols.
    """
    conn = sqlite3.connect(DB_DIR)
    c = conn.cursor()
    if isinstance(accessions, str):
        accessions = [accessions]
    all_results = []
    for a in accessions:
        c.execute('SELECT "Approved symbol" FROM gene_names_homo_sapiens WHERE "RefSeq IDs"=? OR "Ensembl gene ID"=?', (a, a))
        results = c.fetchall()
        if len(results) == 1:
            all_results.append(results[0][0])
        elif len(results) == 0:
            print('WARNING: no results found for ' + a)
            all_results.append(None)
        else:
            print('WARNING: multiple results found for ' + a + '. Using arbitrary result.')
            all_results.append(results[0][0])
    return all_results

if __name__ == '__main__':
    print(get_gene_symbol('NM_001178126'))
    print(get_gene_symbol(['NM_001178126', 'NM_001136213']))
