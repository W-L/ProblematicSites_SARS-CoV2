# List of sites with issues in SARS-CoV-2 sequencing data

A collection of sites described in the virological post [Issues with SARS-CoV-2 sequencing data](http://virological.org/t/issues-with-sars-cov-2-sequencing-data/473).
The information presented here is also [available as a .vcf formatted file](https://github.com/W-L/ProblematicSites_SARS-CoV2/blob/master/problematic_sites_sarsCov2.vcf).

The adapted vcf format contains all 8 mandatory as well as two additional columns.

| Header | Description |
|--------|-------------|
|CHROM   |Name of the reference sequence |
|POS     |1-based position of the variation on the reference |
|ID      | NA |
|REF     | Reference base |
|ALT     | List of alternative alleles at the position |
|QUAL    | NA |
|FILTER  | NA |
|INFO    | Initials of submitter |
|EXC     | List of reasons for suggested exclusion (tags described in separate table) |
|SRC     | Source laboratory of samples showing the variant |


| Tag | Description |
|------|-------------|
| homoplasic | highly homoplasic site |
| no_sig | no phylogenetic signal as inferred by the delta statistic |
| single_src | only observed in samples from a single laboratory |
| seq_end | alignment ends are affected by low coverage and high error rates |

Suggestions, additions and issues are very greatfully received.


# Problematic sites in SARS-CoV-2 sequencing data

|    POS    |REF| ALT |         EXC         |
|-----------|---|-----|---------------------|
|1-55       |.  |.    |seq_end              |
|187        |A  |.    |homoplasic,no_sig    |
|241        |C  |.    |homoplasic           |
|335        |C  |.    |homoplasic           |
|1059       |C  |.    |homoplasic,no_sig    |
|2094       |C  |.    |homoplasic,no_sig    |
|3037       |C  |.    |homoplasic,no_sig    |
|3130       |C  |T    |homoplasic,no_sig    |
|3145       |G  |.    |homoplasic           |
|4050       |A  |C    |homoplasic,single_src|
|6255       |C  |.    |homoplasic           |
|6990       |C  |T    |homoplasic,no_sig    |
|8022       |T  |G    |homoplasic,no_sig    |
|8782       |C  |.    |homoplasic           |
|9223       |C  |.    |homoplasic           |
|10323      |A  |G    |homoplasic,no_sig    |
|10741      |C  |T    |homoplasic,no_sig    |
|11074      |C  |T,-  |homoplasic,no_sig    |
|11083      |G  |T,-  |homoplasic           |
|11704      |C  |.    |homoplasic           |
|13402      |T  |G    |homoplasic,single_src|
|13408      |T  |C,G,A|homoplasic,no_sig    |
|14408      |C  |.    |homoplasic           |
|14724      |C  |.    |homoplasic           |
|14786      |C  |T    |homoplasic,no_sig    |
|14805      |C  |.    |homoplasic           |
|15324      |C  |T    |homoplasic           |
|16887      |C  |T    |homoplasic           |
|17247      |T  |.    |homoplasic           |
|19684      |G  |.    |homoplasic,no_sig    |
|20148      |C  |.    |homoplasic,no_sig    |
|21137      |A  |G    |homoplasic,no_sig    |
|21575      |C  |T    |homoplasic           |
|23403      |A  |.    |homoplasic           |
|24034      |C  |.    |homoplasic,no_sig    |
|24378      |C  |.    |homoplasic,no_sig    |
|24389      |A  |.    |homoplasic,single_src|
|24390      |G  |.    |homoplasic,single_src|
|25563      |G  |.    |homoplasic,no_sig    |
|26144      |G  |.    |homoplasic,no_sig    |
|26461      |C  |.    |homoplasic,no_sig    |
|26681      |C  |.    |homoplasic,no_sig    |
|27384      |T  |.    |homoplasic           |
|28077      |G  |.    |homoplasic,no_sig    |
|28826      |C  |.    |homoplasic,no_sig    |
|28854      |C  |.    |homoplasic,no_sig    |
|29353      |C  |T    |homoplasic,no_sig    |
|29700      |A  |.    |homoplasic,no_sig    |
|29736      |G  |.    |homoplasic           |
|29774      |C  |T    |homoplasic,no_sig    |
|29804-29903|.  |.    |seq_end              |
