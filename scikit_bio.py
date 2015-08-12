import skbio
from skbio.alignment import local_pairwise_align_protein
from skbio.alignment import global_pairwise_align_protein
from datetime import datetime
from skbio.alignment import StripedSmithWaterman
dt = datetime.now()

# files containing sequences to be aligned are assigned
fasta_file1 = raw_input("Please input the name of  file containing the query sequence:\n")
fasta_file2 = raw_input("Please input the name of file containing the reference sequence:\n")
s1 = skbio.Sequence.read("../data/fasta_files/" + fasta_file1)
s2 = skbio.Sequence.read("../data/fasta_files/" + fasta_file2)

# Alignment parameters are set
# substitution matrix = {}
gap_open_penalty = 11
gap_extend_penalty = 1

# Does local alignment using query and reference strings
r = local_pairwise_align_protein(s1, s2, gap_open_penalty, gap_extend_penalty)
print "local_alignment using Smith-Waterman\n"
print r
r.write("../results/SCIKIT-BIO/result_local.txt")
with open( "../results/SCIKIT-BIO/result_local.txt", "a") as fo:
    fo.write("\n" + "Score: "+ str(r.score()))
    fo.write("\n" + str(dt) + "\n")

print "\n"

# Does global alignment using query and reference strings
r = global_pairwise_align_protein(s1, s2, gap_open_penalty, gap_extend_penalty)
print "global_alignment using Neeleman-Wunsch\n"
print r
r.write("../results/SCIKIT-BIO/result_global.txt")
with open( "../results/SCIKIT-BIO/result_global.txt", "a") as fo:
    fo.write("\n" + "Score: "+ str(r.score()))
    fo.write("\n" + str(dt) + "\n")

# Does optimized local alignment using query and reference string
print  'Optimized Alignment Algorithm (Striped Smith Waterman - Local Alignment)'
query = StripedSmithWaterman(str(s1))
alignment = query(str(s2))
print alignment
with open ("../results/striped.txt", "a") as fo:
    fo.write(str(alignment))
    fo.write("\n" + str(dt) + "\n")
