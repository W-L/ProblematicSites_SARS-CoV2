# path to alignment as first argument
alignment_path=$1;

# generate new vcf
python src/site_list_to_vcf.py
python src/parse_reference_to_vcf.py $alignment_path
python src/parseCDS.py

# sort vcf, put into if statement to prevent accidental deletion
if [ -f problematic_sites_sarsCov2_genes.vcf ]; then
    header_lines=$(grep "#" problematic_sites_sarsCov2_genes.vcf | wc -l);
    body_lines=$((header_lines+1))
    (head -n "$header_lines" problematic_sites_sarsCov2_genes.vcf && tail -n +"$body_lines" problematic_sites_sarsCov2_genes.vcf | sort -k2 -n) > problematic_sites_sarsCov2.vcf
    rm problematic_sites_sarsCov2_genes.vcf
fi

bgzip -c problematic_sites_sarsCov2.vcf > problematic_sites_sarsCov2.vcf.gz
tabix problematic_sites_sarsCov2.vcf.gz
tabix --csi problematic_sites_sarsCov2.vcf.gz
