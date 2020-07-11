#!/usr/bin/env python3

from sys import argv


def main():
    pos_info = {}

    with open(argv[2], "r") as alt_vcf_fi:
        for line in alt_vcf_fi.readlines():
            line = line.strip().split("\t")
            pos = line[0]
            ref = line[1]
            alt = line[2].split(",")
            if "N" in alt:
                alt.remove("N")
            alt = ",".join(alt)
            pos_info[int(pos)] = (ref, alt)

    genome_ends = [i+1 for i in range(55)] + [i+1 for i in range(29803,29903)]
    with open(argv[1], "r") as vcf_fi:
        vcf_contents = [i.strip() for i in vcf_fi.readlines()]

    vcf_lines = []
    for vcf_line in vcf_contents:
        #print("vcf_line: ", vcf_line)
        if not vcf_line:
            continue
        if not vcf_line.startswith("#"):
            vcf_line = vcf_line.split("\t")
            pos = int(vcf_line[1])
            if int(vcf_line[1]) in genome_ends:
                vcf_line[4] = "."
            else:
                try:
                    ref_base, alt_base = pos_info[pos][0], pos_info[pos][1]
                    vcf_line[3] = ref_base
                    vcf_line[4] = alt_base
                except KeyError:
                    print(pos)
            vcf_lines.append("\t".join(vcf_line))
        else:
            vcf_lines.append(vcf_line)

    print(vcf_lines)



if __name__ == "__main__":
    main()
