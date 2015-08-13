from Bio.Emboss.Applications import NeedleCommandline

needle_cline = NeedleCommandline(r"../apps/needle", asequence="../data/fasta_files/alpha.faa",
                                 bsequence="../data/fasta_files/beta.faa", gapopen=10, gapextend=0.5,
                                 outfile="needle.txt", datafile="EBLOSUM50")

needle_cline()
#stdout, stderr = needle_cline()
#print(stderr + stderr)
