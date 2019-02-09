import sqlite3

def get_gene_symbol(accession):
    """
    Given a string that is either a RefSeq ID ('NM_...') or an
    Ensembl ID ('ENSG...'), this returns the standard gene symbol.
    """
