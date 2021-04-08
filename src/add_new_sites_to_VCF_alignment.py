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

from sys import argv


def main():
    # format = 
    # POS\tREF\tcsvALT
    existing_vcf_alignment = argv[1]
    
    # format=
    # csvREFPOSALT
    list_of_sites_file = argv[2]
    
    out_fi_name = argv[3]

    existing_entries = {}

    with open(existing_vcf_alignment, "r") as f:
        for line in f.readlines():
            line = line.strip().split("\t")
            existing_entries[line[0]] = [line[1], line[2].split(",")]

    with open(list_of_sites_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            for variant in line.split(","):
                ref = variant[0]
                alt = variant[-1]
                pos = variant[1:-1]

                if ref == "U":
                    ref = "T"
                if alt == "U":
                    alt = "T"

                if pos not in existing_entries.keys():
                    existing_entries[pos] = [ref, [alt]]

                assert existing_entries[pos][0] == ref

                existing_entries[pos][1].append(alt)
            
    for k, v in existing_entries.items():
        existing_entries[k] = [v[0], list(set(v[1]))]

    with open(out_fi_name, "w") as out_fi:
        for out_k in sorted([int(i) for i in existing_entries.keys()]):
            out_k = str(out_k)
            out_fi.write(out_k + "\t" + existing_entries[out_k][0] + "\t" + ",".join(existing_entries[out_k][1]) + "\n")


if __name__ == "__main__":
    main()
