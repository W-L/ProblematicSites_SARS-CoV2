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
|REFAA   | Reference amino acid residue |
|ALTAA   | List of alternative amino acid residues |



| Tag | Description |
|------|-------------|
| homoplasic | highly homoplasic site |
| no_sig | no phylogenetic signal as inferred by the delta statistic |
| single_src | only observed in samples from a single laboratory |
| seq_end | alignment ends are affected by low coverage and high error rates |

Suggestions, additions and issues are very gratefully received.


# Problematic sites in SARS-CoV-2 sequencing data
|    POS    |REF| ALT |         EXC         |   GENE    |AAPOS|REFAA|ALTAA|
|-----------|---|-----|---------------------|-----------|-----|-----|-----|
|1-55       |.  |.    |seq_end              |.          |.    |     |     |
|187        |A  |G    |homoplasic,no_sig    |.          |.    |.    |.    |
|241        |C  |T,Y  |homoplasic           |.          |.    |.    |.    |
|335        |C  |T    |homoplasic           |gene-orf1ab|24   |R    |.    |
|1059       |C  |T,Y  |homoplasic,no_sig    |gene-orf1ab|265  |T    |.    |
|2094       |C  |T    |homoplasic,no_sig    |gene-orf1ab|610  |S    |.    |
|3037       |C  |T,Y  |homoplasic,no_sig    |gene-orf1ab|924  |F    |.    |
|3130       |C  |T    |homoplasic,no_sig    |gene-orf1ab|955  |Y    |.    |
|3145       |G  |T    |homoplasic           |gene-orf1ab|960  |L    |.    |
|4050       |A  |C    |homoplasic,single_src|gene-orf1ab|1262 |N    |.    |
|6255       |C  |T    |homoplasic           |gene-orf1ab|1997 |A    |.    |
|6990       |C  |T    |homoplasic,no_sig    |gene-orf1ab|2242 |S    |.    |
|8022       |T  |G    |homoplasic,no_sig    |gene-orf1ab|2586 |V    |.    |
|8782       |C  |T,Y  |homoplasic           |gene-orf1ab|2839 |S    |.    |
|9223       |C  |T,M,Y|homoplasic           |gene-orf1ab|2986 |H    |.    |
|10323      |A  |G    |homoplasic,no_sig    |gene-orf1ab|3353 |K    |.    |
|10741      |C  |T    |homoplasic,no_sig    |gene-orf1ab|3492 |D    |.    |
|11074      |C  |T    |homoplasic,no_sig    |gene-orf1ab|3603 |F    |.    |
|11083      |G  |T,K  |homoplasic           |gene-orf1ab|3606 |L    |.    |
|11704      |C  |T    |homoplasic           |gene-orf1ab|3813 |Y    |.    |
|13402      |T  |W,G  |homoplasic,single_src|gene-orf1ab|4379 |Y    |.    |
|13408      |T  |A,G,C|homoplasic,no_sig    |gene-orf1ab|4381 |C    |.    |
|14408      |C  |T,Y  |homoplasic           |gene-orf1ab|4715 |P    |.    |
|14724      |C  |Y,T  |homoplasic           |gene-orf1ab|4820 |F    |.    |
|14786      |C  |T    |homoplasic,no_sig    |gene-orf1ab|4841 |A    |.    |
|14805      |C  |T,Y  |homoplasic           |gene-orf1ab|4847 |Y    |.    |
|15324      |C  |T,Y  |homoplasic           |gene-orf1ab|5020 |N    |.    |
|16887      |C  |T    |homoplasic           |gene-orf1ab|5541 |Y    |.    |
|17247      |T  |C,Y,G|homoplasic           |gene-orf1ab|5661 |R    |.    |
|19684      |G  |T    |homoplasic,no_sig    |gene-orf1ab|6473 |E    |.    |
|20148      |C  |T    |homoplasic,no_sig    |gene-orf1ab|6628 |F    |.    |
|21137      |A  |G,R  |homoplasic,no_sig    |gene-orf1ab|6958 |K    |.    |
|21575      |C  |T,Y  |homoplasic           |gene-S     |5    |L    |.    |
|23403      |A  |G,R  |homoplasic           |gene-S     |614  |D    |.    |
|24034      |C  |T,Y  |homoplasic,no_sig    |gene-S     |824  |N    |.    |
|24378      |C  |T,Y  |homoplasic,no_sig    |gene-S     |939  |S    |.    |
|24389      |A  |C    |homoplasic,single_src|gene-S     |943  |S    |.    |
|24390      |G  |C    |homoplasic,single_src|gene-S     |943  |S    |.    |
|25563      |G  |T,K  |homoplasic,no_sig    |gene-ORF3a |57   |Q    |.    |
|26144      |G  |T,K  |homoplasic,no_sig    |gene-ORF3a |251  |G    |.    |
|26461      |C  |T    |homoplasic,no_sig    |gene-E     |73   |L    |.    |
|26681      |C  |T,Y  |homoplasic,no_sig    |gene-M     |53   |F    |.    |
|27384      |T  |C    |homoplasic           |gene-ORF6  |61   |D    |.    |
|28077      |G  |C,T,S|homoplasic,no_sig    |gene-ORF8  |62   |V    |.    |
|28826      |C  |T    |homoplasic,no_sig    |gene-N     |185  |R    |.    |
|28854      |C  |T,Y  |homoplasic,no_sig    |gene-N     |194  |S    |.    |
|29353      |C  |T    |homoplasic,no_sig    |gene-N     |360  |Y    |.    |
|29700      |A  |G    |homoplasic,no_sig    |.          |.    |.    |.    |
|29736      |G  |T    |homoplasic           |.          |.    |.    |.    |
|29774      |C  |T    |homoplasic,no_sig    |.          |.    |.    |.    |
|29804-29903|.  |.    |seq_end              |.          |.    |     |     |
