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
        a2 = '%' + a + '%'
        if a.startswith('N'):
            c.execute('SELECT "Approved symbol" FROM gene_names_homo_sapiens WHERE "RefSeq IDs"=?', (a,))
        elif a.startswith('E'):
            c.execute('SELECT "Approved symbol" FROM gene_names_homo_sapiens WHERE "Ensembl gene ID"=?', (a,))
        results = c.fetchall()
        if len(results) == 1:
            all_results.append(results[0][0])
        elif len(results) == 0:
            print('WARNING: no results found for ' + a)
            all_results.append(None)
        else:
            print('WARNING: multiple results found for ' + a + '. Using arbitrary result.')
            print(results)
            all_results.append(results[0][0])
    c.close()
    conn.close()
    return all_results

def get_refseq_id(symbols):
    """
    Given a string or list of gene symbols,
    this returns a list of RefSeq IDs ('NM_...')
    """
    conn = sqlite3.connect(DB_DIR)
    c = conn.cursor()
    if isinstance(symbols, str):
        symbols = [symbols]
    all_results = []
    for a in symbols:
        a = a.upper()
        c.execute('SELECT "RefSeq IDs" FROM gene_names_homo_sapiens WHERE "Approved symbol"=?', (a,))
        results = c.fetchall()
        if len(results) == 1:
            all_results.append(results[0][0])
        elif len(results) == 0:
            print('WARNING: no results found for ' + a)
            all_results.append(None)
        else:
            print('WARNING: multiple results found for ' + a + '. Using arbitrary result.')
            all_results.append(results[0][0])
    c.close()
    conn.close()
    return all_results


if __name__ == '__main__':
    print(get_gene_symbol('NM_001178126'))
    print(get_gene_symbol(['NM_001178126', 'NM_001136213']))
