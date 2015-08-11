import skbio
from skbio.alignment import local_pairwise_align_protein
from skbio.alignment import global_pairwise_align_protein

fasta_file1 = raw_input("Please input the name of  file containing the query sequence")
fasta_file2 = raw_input("Please input the name of file containing the reference sequence")
s1 = skbio.Sequence.read("../data/fasta_files/" + fasta_file1)
s2 = skbio.Sequence.read("../data/fasta_files/" + fasta_file2)

gap_open_penalty = 11
gap_extend_penalty = 1

r = local_pairwise_align_protein(s1, s2, gap_open_penalty, gap_extend_penalty)
print r
r.write("../results/SCIKIT-BIO/result_local.txt")
print "\n"
r = global_pairwise_align_protein(s1, s2, gap_open_penalty, gap_extend_penalty)
print r
r.write("../results/SCIKIT-BIO/result_global.txt")

