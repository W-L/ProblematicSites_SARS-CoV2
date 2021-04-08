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

# path to alignment as first argument
#alignment_path=$1;
v="v"$1;


# path variables
subset_caution=subset_vcf/problematic_sites_sarsCov2.caution.vcf;
subset_mask=subset_vcf/problematic_sites_sarsCov2.mask.vcf;
compressed_caution=compressed_vcf/problematic_sites_sarsCov2."$v".caution.vcf.gz;
compressed_mask=compressed_vcf/problematic_sites_sarsCov2."$v".mask.vcf.gz;


# generate new vcf
python src/site_list_to_vcf.py ../update_problematic_sites/problematic_sites.tsv
#python src/parse_reference_to_vcf.py "$alignment_path"
python src/add_new_sites_to_VCF_alignment.py ../update_alignments/gisaid_alignment_v"$(($1-1))".vcf ../update_new_variants/new_sites_"$v".csv ../update_alignments/gisaid_alignment_"$v".vcf
python src/fill_alt_positions_from_vcf.py problematic_sites_sarsCov2.vcf ../update_alignments/gisaid_alignment_"$v".vcf
python src/parseCDS.py

# sort vcf, put into if statement to prevent accidental deletion
if [ -f problematic_sites_sarsCov2_genes.vcf ]; then
    header_lines=$(grep "#" problematic_sites_sarsCov2_genes.vcf | wc -l);
    body_lines=$((header_lines+1))
    (head -n "$header_lines" problematic_sites_sarsCov2_genes.vcf && tail -n +"$body_lines" problematic_sites_sarsCov2_genes.vcf | sort -k2 -n) > problematic_sites_sarsCov2.vcf
    rm problematic_sites_sarsCov2_genes.vcf
fi

# subset vcfs
egrep -h "#|caution" problematic_sites_sarsCov2.vcf > $subset_caution
egrep -h "#|mask" problematic_sites_sarsCov2.vcf > $subset_mask
cp problematic_sites_sarsCov2.vcf test/
# compress vcfs
bgzip -c problematic_sites_sarsCov2.vcf > compressed_vcf/problematic_sites_sarsCov2."$v".vcf.gz
bgzip -c $subset_caution > $compressed_caution
bgzip -c $subset_mask > $compressed_mask

# tabix index vcfs
tabix -f compressed_vcf/problematic_sites_sarsCov2."$v".vcf.gz
tabix -f --csi compressed_vcf/problematic_sites_sarsCov2."$v".vcf.gz

tabix -f $compressed_caution
tabix -f --csi $compressed_caution

tabix -f $compressed_mask
tabix -f --csi $compressed_mask
