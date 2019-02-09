Gene Name Mapper: an utility to match gene names with various IDs/accession codes
================

Data source: https://www.genenames.org/download/custom/

Goal:

`gene_names = get_gene_name(['NM_...', 'NM_...'], species='human')`
`refseq_ids = get_refseq_ids(['gene1', 'gene2',...])`
`ensembl_ids = get_ensembl_ids([...])`

how to implement this? load a static file into memory? sqlite database?

Sure, sqlite...
