from Bio.Emboss.Applications import NeedleCommandline
from Bio.Emboss.Applications import WaterCommandline


def needle(seq1, seq2, gapopen, gapextend, matrix, outfile):
    """Needleman-Wunsch Global Alignment.

    Args:
        seq1 (str): Query sequence.
        seq2 (str): Subject sequence.
        gapopen (int): Score for opening a gap.
        gapextend (int): Score for extending a gap.
        matrix (str): Path to or name of file containing matrix data.
        outfile (str): Path or name of file to write output data.

    Returns:
        File containing global alignment result of input sequences.

    """
    needle_cline = NeedleCommandline()
    needle_cline.asequence = "asis:" + seq1
    needle_cline.bsequence = "asis:" + seq2
    needle_cline.gapopen = gapopen
    needle_cline.gapextend = gapextend
    needle_cline.outfile = outfile
    needle_cline.datafile = matrix
    needle_cline()

def water(seq1, seq2, gapopen, gapextend, matrix, outfile):

    """Smith-Waterman Local Alignment

    Args:
        seq1 (str): Query sequence.
        seq2 (str): Subject sequence.
        gapopen (int): Score for opening a gap.
        gapextend (int): Score for extending a gap.
        matrix (str): Path to or name of file containing matrix data.
        outfile (str): Path to or name of file to write output data.

    Returns:
       File containing local alignment result of input sequences 

    """
    water_cline = WaterCommandline()
    water_cline.asequence = "asis:" + seq1
    water_cline.bsequence = "asis:" + seq2
    water_cline.gapopen = gapopen
    water_cline.gapextend = gapextend
    water_cline.outfile = outfile
    water_cline.datafile = matrix
    water_cline()

