#!/usr/local/bin/python

from BCBio import GFF



def readGFF(gff):

    with open(gff, 'r') as gff_file:
        for rec in GFF.parse(gff_file, limit_info=dict(gff_type = ["gene"])):
            genes = rec.features

    return genes


def main():
    # parse gff
    gff = "MN908947_3.gff3"
    vcf = "problematic_sites_sarsCov2.vcf"
    genes = readGFF(gff)


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
                        vcf_line.append(gene.id)
                        vcf_line.append(vcf_aa)
                        ingene = True
                        break

                if not ingene:
                    vcf_line.append('.')
                    vcf_line.append('.')

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