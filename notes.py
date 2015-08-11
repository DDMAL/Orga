from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist


def local_align(seq1, seq2, matrix=None):
    if matrix is not None:
        for a in pairwise2.align.localds(seq1.upper(), seq2.upper(), matrix, -10, -.5):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.localms(seq1, seq2, 2, -1, -.5, -.1):
            print format_alignment(*a)

def global_align(seq1, seq2, matrix=None):
    if matrix is not None:
        for a in pairwise2.align.globalds(seq1.upper(), seq2.upper(), matrix, -10, -.5):
            print format_alignment(*a)
    else:
        for a in pairwise2.align.globalms(seq1, seq2, 2, -1, -.5, -.1):
            print format_alignment(*a)

# Counts the the number of characters in sequence
def count(sequence):
    return "number of notes: {}".format(len(sequence))

# Maps characters in sequence to desired character 
def convert(sequence, map):

    new_sequence = ""
    for s in sequence:
        if s not in map: 
            new_sequence += s
        else:
            new_sequence += map.get(s)

    return new_sequence

# Removes desired symbols from input sequence
def remove(sequence, symbols):
    to_remove = symbols

    new_sequence = ""
    for s in sequence:
        if s not in to_remove:
            new_sequence += s

    return new_sequence