# ---------------------------------------------------------------------------------------
# Copyright (C) 2020 EMBL - European Bioinformatics Institute
# Contact: goldman@ebi.ac.uk, cwalker@ebi.ac.uk
#
# This program is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with this
# program. If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------------------------

#!/usr/local/bin/python

import numpy as np
from Bio import SeqIO, AlignIO
#from six.moves import urllib
from collections import Counter
from sys import argv


def main():
    # parse alignment
    multiple_alignment = argv[1]
    records = AlignIO.read(multiple_alignment, "fasta")
    seq_matrix = []
    
    # get reference sequence from alignment
    ref_align_seq = list(str(records[0].seq).upper())

    # append all seqs to sequence matrix
    for rec in records:
        seq_matrix.append(list(str(rec.seq).upper()))
    seq_matrix = np.asarray(seq_matrix)

    # store alt bases at each site
    bases_per_ref_site = []
    
    # determine all bases in each alignment column (slow, works as needed)
    for i, ref_base in enumerate(ref_align_seq):
        if ref_base == "-":
            continue
        else:
            bases_at_position = list(Counter(seq_matrix[:,i]).keys())
            if ref_base in bases_at_position:
                bases_at_position.remove(ref_base)
            if "-" in bases_at_position:
                bases_at_position.remove("-")
            if "N" in bases_at_position:
                bases_at_position.remove("N")
            bases_per_ref_site.append(",".join(bases_at_position))

    # parse MN908947.3 sequence
    ref_fasta = "data/SARS-CoV-2.fa"
    ref_seq = str(SeqIO.read(ref_fasta, "fasta").seq)

    # retrieve vcf
    #cov_vcf = urllib.request.urlopen("https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/problematic_sites_sarsCov2.vcf")
    cov_vcf = "problematic_sites_sarsCov2.vcf"

    # hold ref positions
    vcf_lines = []

    # parse vcf from github
    #vcf_contents = cov_vcf.read().decode("utf-8").split("\n")
    with open(cov_vcf, "r") as f:
        vcf_contents = [i.strip() for i in f.readlines()]

    # don't report alt variants if in genome end
    genome_ends = [i+1 for i in range(55)] + [i+1 for i in range(29803,29903)]

    # parse ref positions
    for vcf_i, vcf_line in enumerate(vcf_contents):
        print("vcf_line: ", vcf_line)
        if not vcf_line:
            continue
        if not vcf_line.startswith("#"):
            vcf_line = vcf_line.split("\t")
            ref_position = int(vcf_line[1])
            ref_base = ref_seq[ref_position-1]
            vcf_line[3] = ref_base
            if int(vcf_line[1]) in genome_ends:
                vcf_line[4] = "."
            else:
                vcf_line[4] = bases_per_ref_site[ref_position-1]
            vcf_lines.append("\t".join(vcf_line))
        else:
            vcf_lines.append(vcf_line)

    # write updated VCF
    with open("problematic_sites_sarsCov2.vcf", "w") as out_file:
        fi_content = "\n".join(vcf_lines)
        out_file.write(fi_content) 


if __name__ == "__main__":
    main()
