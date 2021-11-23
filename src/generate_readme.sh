echo "[![Build Status](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2.svg?branch=master)](https://travis-ci.com/github/W-L/ProblematicSites_SARS-CoV2)"
echo 
echo "- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)"
echo "- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)"
echo
echo
python src/vcf2markdown.py
echo
echo
cat << EOF
# Description of the columns in the vcf-version

The information presented in the table above is also [available as a .vcf formatted file](https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/problematic_sites_sarsCov2.vcf).

The VCF files have the 8 mandatory columns outlined in the VCF v4.3 specification, some of which contain non-standard content:

| Header         | Description                    |
|----------------|--------------------------------|
|CHROM           | Name of the reference sequence |
|POS             | 1-based position of the variation on the reference |
|ID              | NA |
|REF             | Reference base |
|ALT             | List of alternative alleles at the position (IUPAC ambiguity code) |
|QUAL            | NA |
|FILTER          | Masking recommendation (mask or interpret with caution) |
|INFO            | Key=value metadata pairs |

Metadata in the INFO column current includes the following:

| INFO keys      | Description                    |
|----------------|--------------------------------|
|SUB             | Initials of submitter          |
|EXC             | List of reasons for suggested exclusion (tags described in separate table) |
|SRC_COUNTRY     | Source country/countries of samples with the variant (excluded from the human-friendly VCF) |
|SRC_LAB         | Source laboratory/laboratories of samples with the variant, ordered to match the respective values in SRC_COUNTRY (excluded from the human-friendly VCF)  |
|GENE            | Position falls into range of this gene |
|AAPOS           | Position of amino acid residue within gene |
|REFAA           | Reference amino acid residue |
|ALTAA           | List of alternative amino acid residues (IUPAC ambiguity code) |


Descriptions of reasons for mask/caution (values for EXC in the INFO column) are as follows:

| Tag                         | Description                                                      |
|-----------------------------|------------------------------------------------------------------|
| seq_end                     | Alignment ends are affected by low coverage and high error rates |
| ambiguous                   | Sites which show an excess of ambiguous basecalls relative to the number of alternative alleles, often emerging from a single country or sequencing laboratory |
| amended                     | Previous sequencing errors which now appear to have been fixed in the latest versions of the GISAID sequences, at least in sequences from some of the sequencing laboratories |
| highly_ambiguous            | Sites with a very high proportion of ambiguous characters, relative to the number of alternative alleles |
| highly_homoplasic           | Positions which are extremely homoplasic - it is sometimes not necessarily clear if these are hypermutable sites or sequencing artefacts |
| homoplasic                  | Homoplasic sites, with many mutation events needed to explain a relatively small alternative allele count |
| interspecific_contamination | Cases (so far only one instance) in which the known sequencing issue is due to contamination from genetic material that does not have SARS-CoV-2 origin |
| nanopore_adapter            | Cases in which the known sequencing issue is due to the adapter sequences in nanopore reads |
| narrow_src                  | Variants which are found in sequences from only a few sequencing labs (usually two or three), possibly as a consequence of the same artefact reproduced independently |
| neighbour_linked            | Proximal variants displaying near perfect linkage |
| single_src                  | Only observed in samples from a single laboratory |
| amplicon_drop_or_primer_artefact                  | Amplicon dropout and/or failed primer trimming |
| back_to_ref                  | The alternate allele is sometimes not called for this position due to issues with amplicon dropout and/or primer trimming. For more details, see: https://github.com/W-L/ProblematicSites_SARS-CoV2/issues/7 and https://github.com/cov-lineages/pango-designation/issues/95 |



Suggestions, additions and issues are very gratefully received.
EOF
