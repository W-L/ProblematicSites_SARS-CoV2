#!/usr/local/bin/python
from Bio import SeqIO
from six.moves import urllib

def main():
    # parse MN908947.3 sequence
    ref_fasta = "./SARS-CoV-2.fa"
    ref_seq = str(SeqIO.read(ref_fasta, "fasta").seq)
    # retrieve vcf
    cov_vcf = urllib.request.urlopen("https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/problematic_sites_sarsCov2.vcf")
    # hold ref positions
    vcf_lines = []
    # parse ref positions
    for vcf_line in cov_vcf.read().decode("utf-8").split("\n"):
        if not vcf_line.startswith("#"):
            vcf_line = vcf_line.split("\t")
            ref_base = ref_seq[int(vcf_line[1])-1]
            vcf_line[3] = ref_base
            vcf_lines.append("\t".join(vcf_line))
        else:
            vcf_lines.append(vcf_line)
    # write updated VCF
    with open("problematic_sites_sarsCov2_ref.vcf", "w") as out_file:
        for line in vcf_lines:
            out_file.write(line + "\n")

if __name__ == "__main__":
    main()