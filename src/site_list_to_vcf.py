#!/usr/local/bin/python

from os import makedirs, path
from shutil import copyfile
from datetime import datetime


def generate_vcf_header(current_date, submitters,
                        exclusions, labs):
    fixed1 = "##fileformat=VCFv4.3"
    fidate = "##fileDate={0}".format(str(current_date))
    fixed2 = '''##source=http://virological.org/t/masking-strategies-for-sars-cov-2-alignments/480
    ##reference=MN908947.3
    ##contig=<ID=MN908947.3,length=29903>
    ##FILTER=<Description="Masking recommendation"
    ##	caution = apparent homoplasic sites that should be interpreted carefully, but not necessarily masked
    ##	mask = sites we recommend to always mask
    ##INFO=<Description="Initials of submitter"
    '''.replace("\n    ", "\n")[:-1]
    subs = submitters
    fixed3 = '##EXC=<Description="List of reasons for suggested exclusion">'
    seq_end = '##	seq_end = alignment ends are affected by low coverage and high error rates (recommended to be masked, but might be more stringent than necessary)'
    exc_desc = exclusions
    fixed4 = '##SRC=<Description="Source laboratory or study of samples showing the variant">'
    exc_labs = labs
    fixed5 = '''##GENE=<Decription="Position falls into range of this gene">
    ##AAPOS=<Description="Position of amino acid residue within gene">
    ##REFAA=<Description="Reference amino acid residue">
    ##ALTAA=<Description="List of alternative amino acid residues (IUPAC ambiguity code)">
    #CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    EXC     SRC     GENE    AAPOS   REFAA   ALTAA
    '''.replace("\n    ", "\n")[:-1]
    full_header = "\n".join([fixed1,
                             fidate,
                             fixed2,
                             subs,
                             fixed3,
                             seq_end,
                             exc_desc,
                             fixed4,
                             exc_labs,
                             fixed5])
    return full_header


def generate_descriptions(vcf_header, unique_descriptions, context):
    truncated_headers = [i.split(" =")[0] for i in vcf_header]
    new_descriptions = []
    seen = []
    for desc_val in unique_descriptions or desc_val in seen:
        for desc in desc_val.split(";"):
            if desc in seen:
                continue
            seen.append(desc)
            if str(desc) == "0":
                continue
            try:
                desc_in_list = truncated_headers.index("##\t" + str(desc))
                new_descriptions.append(vcf_header[desc_in_list].strip())
            except ValueError:
                try:
                    desc_in_list = truncated_headers.index("## \t" + str(desc))
                    new_descriptions.append(vcf_header[desc_in_list].strip())
                except ValueError:
                    manual_description = input('{0} "{1}" not in header, add brief description:\n>> '.format(context, desc))
                    new_descriptions.append("##\t{0}".format(desc) + " = " + manual_description)
    return "\n".join(new_descriptions)


def main():
    # create VCF archive directory if it doesn't exist
    if not path.exists("archived_vcf"):
        makedirs("archived_vcf")
    
    # files used to create new VCF
    current_vcf = "problematic_sites_sarsCov2.vcf"
    site_csv = "data/update_sites.txt"

    # back up VCF with dated filename
    date_suffix = datetime.now().strftime("%Y-%m-%d-%H:%M")
    backup_vcf = current_vcf.split(".")[0] + "." + date_suffix + ".vcf"
    copyfile(current_vcf, "archived_vcf/" + backup_vcf)
    
    # get vcf header as list
    vcf_header = []
    with open(current_vcf, "r") as f:
        for line in f.readlines():
            if line.startswith("##"):
                vcf_header.append(line)

    # get list of sites in csv format
    with open(site_csv, "r") as csv_fi:
        update_lines = [i.strip().split(",") for i in csv_fi.readlines()[1:]]
    
    # get unique: exclusion reasons, labs, submitters
    unique_exclusion = list(set([i[2] for i in update_lines]))
    unique_labs = list(set([i[3] for i in update_lines]))
    unique_submitters = list(set([i[4] for i in update_lines]))

    all_exclusions = generate_descriptions(vcf_header, unique_exclusion,"Exclusion")
    all_labs = generate_descriptions(vcf_header, unique_labs, "Lab")
    all_submitters = generate_descriptions(vcf_header, unique_submitters, "Submitter")

    updated_header = generate_vcf_header(date_suffix, all_submitters, all_exclusions, all_labs)
    
    genome_end_lines = []

    with open("data/genome_ends.vcf", "r") as f:
        for line in f.readlines():
            genome_end_lines.append(line.strip())
    
    with open("problematic_sites_sarsCov2.vcf", "w+") as out_vcf:
        out_vcf.write(updated_header + "\n")
        for line in genome_end_lines:
            out_vcf.write(line + "\n")
        for line in update_lines:
            pos = line[0]
            mask_rec = line[1]
            exc_reason = line[2]
            if line[3] == "0":
                source = "."
            else:
                source = line[3]
            submitter = line[4]
            out_vcf.write("MN908947.3\t{0}\t.\t.\t.\t.\t{1}\t{2}\t{3}\t{4}\t.\t.\t.\t.".format(pos,mask_rec,submitter,exc_reason,source) + "\n")


    pass


if __name__ == "__main__":
    main()
