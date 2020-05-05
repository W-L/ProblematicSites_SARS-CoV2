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

Suggestions, additions and issues are very gratefully received.


# Human readable version



|    POS    |         EXC         |  SRC   |
|-----------|---------------------|--------|
|1-55       |seq_end              |.       |
|187        |homoplasic,no_sig    |.       |
|241        |homoplasic           |.       |
|335        |homoplasic           |.       |
|1059       |homoplasic,no_sig    |.       |
|2094       |homoplasic,no_sig    |.       |
|3037       |homoplasic,no_sig    |.       |
|3130       |homoplasic,no_sig    |.       |
|3145       |homoplasic           |.       |
|4050       |homoplasic,single_src|KULeuven|
|6255       |homoplasic           |.       |
|6990       |homoplasic,no_sig    |.       |
|8022       |homoplasic,no_sig    |.       |
|8782       |homoplasic           |.       |
|9223       |homoplasic           |.       |
|10323      |homoplasic,no_sig    |.       |
|10741      |homoplasic,no_sig    |.       |
|11074      |homoplasic,no_sig    |.       |
|11083      |homoplasic           |.       |
|11704      |homoplasic           |.       |
|13402      |homoplasic,single_src|KULeuven|
|13408      |homoplasic,no_sig    |.       |
|14408      |homoplasic           |.       |
|14724      |homoplasic           |.       |
|14786      |homoplasic,no_sig    |.       |
|14805      |homoplasic           |.       |
|15324      |homoplasic           |.       |
|16887      |homoplasic           |.       |
|17247      |homoplasic           |.       |
|19684      |homoplasic,no_sig    |.       |
|20148      |homoplasic,no_sig    |.       |
|21137      |homoplasic,no_sig    |.       |
|21575      |homoplasic           |.       |
|23403      |homoplasic           |.       |
|24034      |homoplasic,no_sig    |.       |
|24378      |homoplasic,no_sig    |.       |
|24389      |homoplasic,single_src|.       |
|24390      |homoplasic,single_src|.       |
|25563      |homoplasic,no_sig    |.       |
|26144      |homoplasic,no_sig    |.       |
|26461      |homoplasic,no_sig    |.       |
|26681      |homoplasic,no_sig    |.       |
|27384      |homoplasic           |.       |
|28077      |homoplasic,no_sig    |.       |
|28826      |homoplasic,no_sig    |.       |
|28854      |homoplasic,no_sig    |.       |
|29353      |homoplasic,no_sig    |.       |
|29700      |homoplasic,no_sig    |.       |
|29736      |homoplasic           |.       |
|29774      |homoplasic,no_sig    |.       |
|29804-29903|seq_end              |.       |
