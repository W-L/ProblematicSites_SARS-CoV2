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

#!/usr/bin/env python3

import argparse


def read_fasta_keep_name(file, cli_args):
    """
    Parses an input FASTA file containing an MSA, returns headers, sequences, and
    the index of the reference sequence for later use. The reference sequence
    is determined by searching for the reference ID string in the headers,
    specified with --reference_id.
    """
    sample_headers = []
    sample_sequences = []
    line_count = 0
    line = file.readline()
    ref_index = None
    while line != "" and line != "\n":
        if line[0] == ">":
            name = line.replace("\n","").replace(">","")
            if cli_args.reference_id in name:
                ref_index = line_count
            seq = ""
            line = file.readline()
            line_count += 1
            while line != "" and line != "\n" and line[0] != ">":
                seq += line.replace("\n","")
                line = file.readline()
            sample_headers.append(name)
            #sample_sequences.append(seq.lower())
            sample_sequences.append(seq)
        else:
            print("problem with fasta format: line not recognised")
            print(line)
            exit()
    if ref_index is None:
        print("reference sequence ID not found:")
        print(cli_args.reference_id)
        exit()
    return sample_headers, sample_sequences, ref_index


def ref_coords_to_align_coords(ref_align_seq):
    """
    Generate a dictionary of reference sequence coordinates mapped to MSA
    coordinates. Used to update the VCF positions in case the reference
    sequence contains gaps.
    """
    ref_coord_dic = {}
    ref_align_seq = "".join(ref_align_seq).strip()
    for i in range(len(ref_align_seq.replace("-",""))):
        ref_coord_dic[i] = 0
    seq_count = 0
    align_count = 0
    for c in ref_align_seq:
        if c != "-":
            ref_coord_dic[seq_count] = align_count
            seq_count += 1
            align_count += 1
        else:
            align_count += 1
    return ref_coord_dic


def parse_vcf(cli_args):
    """
    Parse a VCF containing positions for masking. Assumes the VCF file is
    formatted as:
    github.com/W-L/ProblematicSites_SARS-CoV2/blob/master/problematic_sites_sarsCov2.vcf
    with a "mask" or "caution" recommendation in column 7.
    Masked sites are specified with CLI options.
    The default is to only mask sites with a "mask" recommendation.
    The options --caution or --both can be used to mask either just "caution"
    sites, or both "mask" and "caution" sites.
    """
    with open(cli_args.vcf, "r") as vcf_fi:
        vcf_lines = [i.strip() for i in vcf_fi.readlines()]
    if not cli_args.both and not cli_args.caution:
        vcf_lines = [i for (i, v) in zip(vcf_lines,["\tmask\t" in l for l in vcf_lines]) if v]
    if cli_args.caution:
        vcf_lines = [i for (i, v) in zip(vcf_lines,["\tcaution\t" in l for l in vcf_lines]) if v]
    if cli_args.both:
        vcf_lines = [i for (i, v) in zip(vcf_lines,["\tcaution\t" in l or "\tmask\t" in l for l in vcf_lines]) if v]
    return [i.split("\t")[1] for i in vcf_lines]


def main():
    # parse CLI arguments
    parser = argparse.ArgumentParser()
    # optional arguments
    parser.add_argument("-m", "--mask",
                        help="Only mask sites marked as mask (default)",
                        action="store_true")
    parser.add_argument("-c", "--caution",
                        help="Only mask sites marked as caution",
                        action="store_true")
    parser.add_argument("-b", "--both",
                        help="Mask sites marked as either mask or caution",
                        action="store_true")
    parser.add_argument("-d", "--remove_sites",
                        help="Remove sites from the alignment instead of masking",
                        action="store_true")
    parser.add_argument("-n", "--mask_character",
                        help="Masking character (default: \"N\")",
                        type=str,
                        default="N")
    parser.add_argument("-r", "--reference_id",
                        help="Reference ID (default: \"MN908947\")",
                        type=str,
                        default="MN908947")
    # required arguments
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument("-v", "--vcf",
                        required=True,
                        help="Input VCF to use for masking")
    required_args.add_argument("-i", "--input_fasta",
                        required=True,
                        help="Input FASTA file to mask")
    required_args.add_argument("-o", "--output_fasta",
                        required=True,
                        help="Name for output masked FASTA file")
    args = parser.parse_args()
    
    # parse VCF to get list of sites to mask
    iffy_sites = parse_vcf(args)
   
    # parse existing MSA FASTA file
    with open(args.input_fasta, "r") as fasta_fi:
        headers, sequences, ref_index = read_fasta_keep_name(fasta_fi, args)

    # get reference sequence
    ref_sequence = sequences[ref_index]

    # convert reference sequence coords to corresponding alignment coords
    ref_coord_dic = ref_coords_to_align_coords(ref_sequence)

    # convert list of iffy sites to corresponding alignment positions
    # using zero-based indexing
    iffy_alignment_sites = [ref_coord_dic[int(i)-1] for i in iffy_sites]

    # using list of iffy alignment sites, mask corresponding positions
    # in the input MSA
    file = open(args.output_fasta, "w")
    for i in range(len(headers)):
        seq = list(sequences[i])
        for p in iffy_alignment_sites:
            if args.remove_sites:
                seq[p] = ""
            else:
                seq[p] = args.mask_character
        seq = "".join(seq)
        file.write(">" + headers[i] + "\n" + seq + "\n")
    file.close()


if __name__ == "__main__":
    main()
