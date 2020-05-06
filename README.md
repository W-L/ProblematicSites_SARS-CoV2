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
|GENE    | Position falls into range of this gene |
|AAPOS   | Position of amino acid residue within gene |



| Tag | Description |
|------|-------------|
| homoplasic | highly homoplasic site |
| no_sig | no phylogenetic signal as inferred by the delta statistic |
| single_src | only observed in samples from a single laboratory |
| seq_end | alignment ends are affected by low coverage and high error rates |

Suggestions, additions and issues are very gratefully received.


# Problematic sites in SARS-CoV-2 sequencing data
|    POS    |REF| ALT |         EXC         |   GENE    |AAPOS|
|-----------|---|-----|---------------------|-----------|-----|
|1-55       |.  |.    |seq_end              |.          |.    |
|187        |A  |.    |homoplasic,no_sig    |.          |.    |
|241        |C  |.    |homoplasic           |.          |.    |
|335        |C  |.    |homoplasic           |gene-orf1ab|24   |
|1059       |C  |.    |homoplasic,no_sig    |gene-orf1ab|265  |
|2094       |C  |.    |homoplasic,no_sig    |gene-orf1ab|610  |
|3037       |C  |.    |homoplasic,no_sig    |gene-orf1ab|924  |
|3130       |C  |T    |homoplasic,no_sig    |gene-orf1ab|955  |
|3145       |G  |.    |homoplasic           |gene-orf1ab|960  |
|4050       |A  |C    |homoplasic,single_src|gene-orf1ab|1262 |
|6255       |C  |.    |homoplasic           |gene-orf1ab|1997 |
|6990       |C  |T    |homoplasic,no_sig    |gene-orf1ab|2242 |
|8022       |T  |G    |homoplasic,no_sig    |gene-orf1ab|2586 |
|8782       |C  |.    |homoplasic           |gene-orf1ab|2839 |
|9223       |C  |.    |homoplasic           |gene-orf1ab|2986 |
|10323      |A  |G    |homoplasic,no_sig    |gene-orf1ab|3353 |
|10741      |C  |T    |homoplasic,no_sig    |gene-orf1ab|3492 |
|11074      |C  |T,-  |homoplasic,no_sig    |gene-orf1ab|3603 |
|11083      |G  |T,-  |homoplasic           |gene-orf1ab|3606 |
|11704      |C  |.    |homoplasic           |gene-orf1ab|3813 |
|13402      |T  |G    |homoplasic,single_src|gene-orf1ab|4379 |
|13408      |T  |C,G,A|homoplasic,no_sig    |gene-orf1ab|4381 |
|14408      |C  |.    |homoplasic           |gene-orf1ab|4715 |
|14724      |C  |.    |homoplasic           |gene-orf1ab|4820 |
|14786      |C  |T    |homoplasic,no_sig    |gene-orf1ab|4841 |
|14805      |C  |.    |homoplasic           |gene-orf1ab|4847 |
|15324      |C  |T    |homoplasic           |gene-orf1ab|5020 |
|16887      |C  |T    |homoplasic           |gene-orf1ab|5541 |
|17247      |T  |.    |homoplasic           |gene-orf1ab|5661 |
|19684      |G  |.    |homoplasic,no_sig    |gene-orf1ab|6473 |
|20148      |C  |.    |homoplasic,no_sig    |gene-orf1ab|6628 |
|21137      |A  |G    |homoplasic,no_sig    |gene-orf1ab|6958 |
|21575      |C  |T    |homoplasic           |gene-S     |5    |
|23403      |A  |.    |homoplasic           |gene-S     |614  |
|24034      |C  |.    |homoplasic,no_sig    |gene-S     |824  |
|24378      |C  |.    |homoplasic,no_sig    |gene-S     |939  |
|24389      |A  |.    |homoplasic,single_src|gene-S     |943  |
|24390      |G  |.    |homoplasic,single_src|gene-S     |943  |
|25563      |G  |.    |homoplasic,no_sig    |gene-ORF3a |57   |
|26144      |G  |.    |homoplasic,no_sig    |gene-ORF3a |251  |
|26461      |C  |.    |homoplasic,no_sig    |gene-E     |73   |
|26681      |C  |.    |homoplasic,no_sig    |gene-M     |53   |
|27384      |T  |.    |homoplasic           |gene-ORF6  |61   |
|28077      |G  |.    |homoplasic,no_sig    |gene-ORF8  |62   |
|28826      |C  |.    |homoplasic,no_sig    |gene-N     |185  |
|28854      |C  |.    |homoplasic,no_sig    |gene-N     |194  |
|29353      |C  |T    |homoplasic,no_sig    |gene-N     |360  |
|29700      |A  |.    |homoplasic,no_sig    |.          |.    |
|29736      |G  |.    |homoplasic           |.          |.    |
|29774      |C  |T    |homoplasic,no_sig    |.          |.    |
|29804-29903|.  |.    |seq_end              |.          |.    |
