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
