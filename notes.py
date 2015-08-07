from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def local_align(seq1, seq2):
    for a in pairwise2.align.localxx(seq1, seq2):
        print format_alignment(*a)

def count(notes):
    return "number of notes: {}".format(len(notes))
