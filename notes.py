from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

MATRIX = matlist.blosum62

def local_align(seq1, seq2):
    for a in pairwise2.align.localdx(seq1.upper(), seq2.upper(), MATRIX):
        print format_alignment(*a)

def global_align(seq1, seq2):
    for a in pairwise2.align.localms(seq1.upper(), seq2.upper() , 2, -1, -.5, -.1):
        print format_alignment(*a)

def count(notes):
    return "number of notes: {}".format(len(notes))
