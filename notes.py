from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist


def local_align(seq1, seq2, matrix=None):
    if matrix is not None:
        for a in pairwise2.align.localdx(seq1.upper(), seq2.upper(), matrix):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.localxx(seq1, seq2):
            print format_alignment(*a)

def global_align(seq1, seq2, matrix):
    if matrix is not None:
        for a in pairwise2.align.globaldx(seq1, seq2, matrix):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.globalms(seq1, seq2 , 2, -1, -.5, -.1):
            print format_alignment(*a)

def count(notes):
    return "number of notes: {}".format(len(notes))
