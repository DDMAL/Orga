from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

def local_align(seq1, seq2, matrix=None):
	"""Pairwise Local Alignment

	Args:
		seq1 (str): query sequence
		seq2 (str): subject sequence

	Returns:
		formatted alignment result

	"""

    if matrix is not None:
        for a in pairwise2.align.localds(seq1.upper(), seq2.upper(), matrix, -10, -.5):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.localms(seq1, seq2, 2, -1, -.5, -.1):
            print format_alignment(*a)

def global_align(seq1, seq2, matrix=None):
	"""Pairwise Global Alignment

	Args:
		seq1 (str): query sequence
		seq2 (str): query sequence

	Returns:
		formatted alignment result
		
	"""
    if matrix is not None:
        for a in pairwise2.align.globalds(seq1.upper(), seq2.upper(), matrix, -10, -.5):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.globalms(seq1, seq2, 2, -1, -.5, -.1):
            print format_alignment(*a)