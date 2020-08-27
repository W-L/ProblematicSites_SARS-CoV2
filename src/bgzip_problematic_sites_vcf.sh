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

## Sort the file on column 2 at non-header lines only
## standard tools e.g. "bcftools sort" not used as a couple of the lines
## have non-standard formatting that throw errors. Can be changed easily
## at the cost of human readability at any point if needed.

# get number of header lines in VCF file
header_lines=$(grep "#" ../problematic_sites_sarsCov2.vcf | wc -l);
body_lines=$((header_lines+1))

(head -n "$header_lines" ../problematic_sites_sarsCov2.vcf && tail -n +"$body_lines" ../problematic_sites_sarsCov2.vcf | sort -k2 -n) | bgzip -c > ../compressed_vcf/problematic_sites_sarsCov2.vcf.gz
tabix -p vcf ../compressed_vcf/problematic_sites_sarsCov2.vcf.gz
tabix --csi ../compressed_vcf/problematic_sites_sarsCov2.vcf.gz
