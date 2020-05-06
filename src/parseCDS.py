#!/usr/local/bin/python

from BCBio import GFF
from Bio import SeqIO

def readGFF(gff):

    with open(gff, 'r') as gff_file:
        for rec in GFF.parse(gff_file, limit_info=dict(gff_type = ["gene"])):
            genes = rec.features
    return genes


def readFA(fa):
    proteins = dict()
    record_dict = SeqIO.to_dict(SeqIO.parse(fa, "fasta"))
    for id, vals in record_dict.items():
        name = record_dict[id].description.split(' ')[1][1:-1].replace('=', '-')
        proteins[name] = vals.seq
    return proteins


def main():
    # parse gff
    gff = "data/MN908947_3.gff3"
    vcf = "problematic_sites_sarsCov2.vcf"
    prot = "data/MN908947_3.prot.fa"
    genes = readGFF(gff)
    proteins = readFA(prot)


    vcf_rebuild = []
    with open(vcf, 'r') as vcf_file:
        for line in vcf_file:
            if not line.startswith('#'):
                vcf_line = line.rstrip('\n').split('\t')
                pos = int(vcf_line[1])

                ingene = False
                for gene in genes:
                    if gene.location.nofuzzy_start <= pos <= gene.location.nofuzzy_end:
                        vcf_aa = str(int((pos - gene.location.nofuzzy_start + 2) / 3))
                        vcf_line[10] = gene.id                                  # gene name
                        vcf_line[11] = vcf_aa                                   # aa position
                        vcf_line[12] = proteins[gene.id][int(vcf_aa) - 1]       # reference aa
                        vcf_line[13] = '.'                                      # alternative aa
                        ingene = True
                        break

                if not ingene:
                    vcf_line[10] = '.'  # gene name
                    vcf_line[11] = '.'  # aa position
                    vcf_line[12] = '.'  # reference aa
                    vcf_line[13] = '.'  # alternative aa

                vcf_rebuild.append("\t".join(vcf_line))

            else:
                vcf_rebuild.append(line.rstrip('\n'))

    # write updated VCF
    with open("problematic_sites_sarsCov2_genes.vcf", "w") as out_file:
        for line in vcf_rebuild:
            out_file.write(line + "\n")
            # pass


if __name__ == "__main__":
    main()