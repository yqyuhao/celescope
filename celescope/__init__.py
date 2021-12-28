import os

__VERSION__ = "1.7.0b0"
__version__ = __VERSION__

ASSAY_DICT = {
    "rna": "Single-cell rna",
    "rna_virus": "Single Cell RNA-Seq Virus",
    'capture_virus': "Single Cell Capture Virus",
    'fusion': "Single Cell Fusion Gene",
    'vdj': "Single-cell vdj",
    'hla': 'Single Cell HLA',
    'capture_rna': 'Single Cell Capture RNA',
    'snp': 'Single-cell variant',
    'tag': 'Single-cell tag',
    'citeseq': 'Single Cell CITE-Seq',
    'tcr_fl': 'Single Cell full length TCR',
    'dynaseq': 'Single-cell dynaseq'
}

ROOT_PATH = os.path.dirname(__file__)

RELEASED_ASSAYS = ['rna', 'vdj', 'tag', 'dynaseq', 'snp', 'capture_virus']

HELP_DICT = {
    'match_dir': 'Match celescope scRNA-Seq directory.',
    'gene_list': 'Required. Gene list file, one gene symbol per line. Only results of these genes are reported.',
    'genomeDir': 'Required. Genome directory after running `celescope rna mkref`.',
    'thread': 'Thread to use.',
    'debug': 'If this argument is used, celescope may output addtional file for debugging.',
    'fasta': 'Required. Genome fasta file. Use absolute path or relative path to `genomeDir`.',
    'outdir': 'Output directory.',
    'matrix_dir': 'Match celescope scRNA-Seq matrix directory.',
    'panel': 'The prefix of bed file in `celescope/data/snp/panel/`, such as `lung_1`.',
    'virus_genomeDir': 'Required. Virus genome directory after running `celescope capture_virus mkref`.'
}

HELP_INFO_DICT = {
    'matched_barcode_number': {
        'display': 'Number of Matched Cells',
        'info': 'cell barcode number of matched scRNA-Seq sample',
    }
}
