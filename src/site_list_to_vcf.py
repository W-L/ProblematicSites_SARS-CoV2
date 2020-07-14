#!/usr/bin/env python3

from os import makedirs, path
from shutil import copyfile
from datetime import datetime


def generate_vcf_header(current_date, submitters,
                        exclusions, labs):
    """
    Generate the VCF header.
    """
    fixed1 = "##fileformat=VCFv4.3"
    fidate = "##fileDate={0}".format(str(current_date))
    fixed2 = '''##source=http://virological.org/t/masking-strategies-for-sars-cov-2-alignments/480
    ##reference=MN908947.3
    ##contig=<ID=MN908947.3,length=29903>
    ##FILTER=<Description="Masking recommendation"
    ##\tcaution = Sites that should be interpreted carefully, but not necessarily masked
    ##\tmask = Sites we recommend to always mask
    ##INFO=<Description="Initials of submitter"
    '''.replace("\n    ", "\n")[:-1]
    fixed3 = '##EXC=<Description="List of reasons for suggested exclusion">'
    seq_end_p1 = '##\tseq_end = Alignment ends are affected by low coverage and high error rates '
    seq_end_p2 = '(masking recommended, but might be more stringent than necessary)'
    # exclusion reasons
    fixed4 = '##SRC_COUNTRY=<Description="Source country/countries of samples with the variant">'
    # fixed_countries
    fixed5 = '##SRC_LAB=<Description="Source laboratory/laboratories of samples with the variant (ordered to match the respective values in SRC_COUNTRY)">'
    # fixed_labs
    fixed6 = '''##GENE=<Decription="Position falls into range of this gene">
    ##AAPOS=<Description="Position of amino acid residue within gene">
    ##REFAA=<Description="Reference amino acid residue">
    ##ALTAA=<Description="List of alternative amino acid residues (IUPAC ambiguity code)">
    #CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tEXC\tSRC_COUNTRY\tSRC_LAB\tGENE\tAAPOS\tREFAA\tALTAA
    '''.replace("\n    ", "\n")[:-1]
    full_header = "\n".join([fixed1,
                             fidate,
                             fixed2,
                             submitters,
                             fixed3,
                             seq_end_p1 + seq_end_p2,
                             exclusions,
                             fixed4,
                             fixed5,
                             labs,
                             fixed6])
    return full_header


def generate_descriptions(vcf_header, unique_descriptions, context):
    """
    Check all unique input exclusion reasons and request user adds
    a desription for each if not already in the VCF header.
    """
    truncated_headers = [i.split(" =")[0] for i in vcf_header]
    new_descriptions = []
    seen = []
    for desc_val in unique_descriptions or desc_val in seen:
        for desc in desc_val.split(","):
            if desc in seen or desc == ".":
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
    return "\n".join(sorted(new_descriptions))


def main():
    # create VCF archive directory if it doesn't exist
    if not path.exists("archived_vcf"):
        makedirs("archived_vcf")

    # files used to create new VCF
    current_vcf = "problematic_sites_sarsCov2.vcf"
    #site_tsv = "data/update_sites.txt"
    site_tsv = "data/problematic_sites.tsv"


    # back up VCF with dated filename
    date_suffix = datetime.now().strftime("%Y-%m-%d-%H:%M")
    backup_vcf = current_vcf.split(".")[0] + "." + date_suffix + ".vcf"
    copyfile(current_vcf, "archived_vcf/" + backup_vcf)

    # get vcf header as list
    vcf_header = []
    with open(current_vcf, "r") as vcf_fi:
        for line in vcf_fi.readlines():
            if line.startswith("##"):
                vcf_header.append(line)

    # get list of sites in csv format
    with open(site_tsv, "r") as csv_fi:
        tmp_update_lines = [i.strip().split("\t") for i in csv_fi.readlines()[1:]]

    # store lines to add
    update_lines = []
    # split coord ranges into individual entries
    for site_line in tmp_update_lines:
        line_coord = site_line[0]
        # handle MNM ranges
        if "-" in line_coord:
            range_split = [int(i) for i in line_coord.split("-")]
            start_pos, end_pos = range_split[0], range_split[1]
            line_content = site_line[1:]
            for i in range(start_pos, end_pos+1):
                update_lines.append([str(i)] + line_content)
        # handle MNM coord lists
        elif ";" in line_coord:
            range_split = [int(i) for i in line_coord.split(";")]
            line_content = site_line[1:]
            for i in range_split:
                update_lines.append([str(i)] + line_content)
        else:
            update_lines.append(site_line)
    del tmp_update_lines

    # get unique: exclusion reasons, labs, submitters
    unique_exclusion = list(set([i[2] for i in update_lines]))
    #unique_countries = list(set([i[3] for i in update_lines]))
    unique_labs = list(set([i[4] for i in update_lines]))
    unique_submitters = list(set([i[5] for i in update_lines]))

    all_exclusions = generate_descriptions(vcf_header, unique_exclusion, "Exclusion")
    #all_countries = generate_descriptions(vcf_header, unique_countries, "Country")
    all_labs = generate_descriptions(vcf_header, unique_labs, "Lab")
    all_submitters = generate_descriptions(vcf_header, unique_submitters, "Submitter")

    updated_header = generate_vcf_header(date_suffix,
                                         all_submitters,
                                         all_exclusions,
                                         all_labs)

    genome_end_lines = []

    with open("data/genome_ends.vcf", "r") as vcf_fi:
        for line in vcf_fi.readlines():
            genome_end_lines.append(line.strip())

    with open("problematic_sites_sarsCov2.vcf", "w+") as out_vcf:
        out_vcf.write(updated_header + "\n")
        for line in genome_end_lines:
            out_vcf.write(line + "\n")
        for line in update_lines:
            pos = line[0]
            mask_rec = line[1]
            exc_reason = line[2]
            src_country = line[3]
            src_lab = line[4]
            submitter = line[5]
            out_vcf.write("MN908947.3\t{0}\t.\t.\t.\t.\t{1}\t{2}\t{3}\t{4}\t{5}\t.\t.\t.\t.".format(pos, mask_rec, submitter, exc_reason, src_country, src_lab) + "\n")


if __name__ == "__main__":
    main()
