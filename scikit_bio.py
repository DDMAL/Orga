from skbio.alignment import local_pairwise_align_protein
from skbio.alignment import global_pairwise_align_protein
from datetime import datetime


dt = datetime.now()

def skbio_local_align(seq1, seq2, gap_open_penalty, gap_extend_penalty, outfile):
    """Local alignment using query and reference strings.

    Args:
        seq1 (str): Query sequence.
        seq2 (str): Subject sequence.
        gap_open_penalty (int): Penalty for opening a gap.
        gap_extend_penalty (int): Penalty for extending a gap.

    Returns:
        File containing local alignment result of input sequences.
    """

    r = local_pairwise_align_protein(seq1, seq2, gap_open_penalty, gap_extend_penalty)
    r.write(outfile)
    with open( outfile, "a") as fo:
        fo.write("\n" + "Score: "+ str(r.score()))
        fo.write("\n" + str(dt) + "\n")

def skbio_global_align(seq1, seq2, gap_open_penalty, gap_extend_penalty, outfile):
    """Global alignment using query and reference strings.

        Args:
            seq1 (str): Query sequence.
            seq2 (str): Subject sequence.
            gap_open_penalty (int): Penalty for opening a gap.
            gap_extend_penalty (int): Penalty for extending a gap.

        Returns:
            File containing global alignment result of input sequences.

    """
    r = global_pairwise_align_protein(seq1, seq2, gap_open_penalty, gap_extend_penalty)
    r.write(outfile)
    with open( outfile, "a") as fo:
        fo.write("\n" + "Score: "+ str(r.score()))
        fo.write("\n" + str(dt) + "\n")


