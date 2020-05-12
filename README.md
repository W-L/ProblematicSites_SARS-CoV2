- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)

# Human-friendly version of the vcf file

|    POS    |REF| ALT |         EXC         |   GENE    |AAPOS|REFAA|ALTAA|
|-----------|---|-----|---------------------|-----------|-----|-----|-----|
|1-55       |.  |.    |seq_end              |.          |.    |     |     |
|187        |A  |G    |homoplasic,no_sig    |.          |.    |.    |.    |
|241        |C  |T,Y  |homoplasic           |.          |.    |.    |.    |
|335        |C  |T    |homoplasic           |gene-orf1ab|24   |R    |C    |
|1059       |C  |T,Y  |homoplasic,no_sig    |gene-orf1ab|265  |T    |I,X  |
|2094       |C  |T    |homoplasic,no_sig    |gene-orf1ab|610  |S    |L    |
|3037       |C  |T,Y  |homoplasic,no_sig    |gene-orf1ab|924  |F    |F,F  |
|3130       |C  |T    |homoplasic,no_sig    |gene-orf1ab|955  |Y    |Y    |
|3145       |G  |T    |homoplasic           |gene-orf1ab|960  |L    |F    |
|4050       |A  |C    |homoplasic,single_src|gene-orf1ab|1262 |N    |T    |
|6255       |C  |T    |homoplasic           |gene-orf1ab|1997 |A    |V    |
|6990       |C  |T    |homoplasic,no_sig    |gene-orf1ab|2242 |S    |F    |
|8022       |T  |G    |homoplasic,no_sig    |gene-orf1ab|2586 |V    |G    |
|8782       |C  |T,Y  |homoplasic           |gene-orf1ab|2839 |S    |S,S  |
|9223       |C  |T,M,Y|homoplasic           |gene-orf1ab|2986 |H    |H,X,H|
|10323      |A  |G    |homoplasic,no_sig    |gene-orf1ab|3353 |K    |R    |
|10741      |C  |T    |homoplasic,no_sig    |gene-orf1ab|3492 |D    |D    |
|11074      |C  |T    |homoplasic,no_sig    |gene-orf1ab|3603 |F    |F    |
|11083      |G  |T,K  |highly_hom           |gene-orf1ab|3606 |L    |F,X  |
|11704      |C  |T    |homoplasic           |gene-orf1ab|3813 |Y    |Y    |
|13402      |T  |W,G  |homoplasic,single_src|gene-orf1ab|4379 |Y    |X,*  |
|13408      |T  |A,G,C|homoplasic,no_sig    |gene-orf1ab|4381 |C    |*,W,C|
|14408      |C  |T,Y  |homoplasic           |gene-orf1ab|4715 |P    |L,L  |
|14724      |C  |Y,T  |homoplasic           |gene-orf1ab|4820 |F    |X,F  |
|14786      |C  |T    |homoplasic,no_sig    |gene-orf1ab|4841 |A    |L    |
|14805      |C  |T,Y  |homoplasic           |gene-orf1ab|4847 |Y    |I,X  |
|15324      |C  |T,Y  |highly_hom           |gene-orf1ab|5020 |N    |I,X  |
|16887      |C  |T    |homoplasic           |gene-orf1ab|5541 |Y    |I    |
|17247      |T  |C,Y,G|homoplasic           |gene-orf1ab|5661 |R    |A,X,G|
|19684      |G  |T    |homoplasic,no_sig    |gene-orf1ab|6473 |E    |N    |
|20148      |C  |T    |homoplasic,no_sig    |gene-orf1ab|6628 |F    |L    |
|21137      |A  |G,R  |homoplasic,no_sig    |gene-orf1ab|6958 |K    |G,X  |
|21575      |C  |T,Y  |highly_hom           |gene-S     |5    |L    |F,X  |
|23403      |A  |G,R  |homoplasic           |gene-S     |614  |D    |G,X  |
|24034      |C  |T,Y  |homoplasic,no_sig    |gene-S     |824  |N    |N,N  |
|24378      |C  |T,Y  |homoplasic,no_sig    |gene-S     |939  |S    |F,X  |
|24389      |A  |C    |seq_err              |gene-S     |943  |S    |R    |
|24390      |G  |C    |seq_err              |gene-S     |943  |S    |T    |
|25563      |G  |T,K  |homoplasic,no_sig    |gene-ORF3a |57   |Q    |H,X  |
|26144      |G  |T,K  |homoplasic,no_sig    |gene-ORF3a |251  |G    |V,X  |
|26461      |C  |T    |homoplasic,no_sig    |gene-E     |73   |L    |F    |
|26681      |C  |T,Y  |homoplasic,no_sig    |gene-M     |53   |F    |F,F  |
|27384      |T  |C    |homoplasic           |gene-ORF6  |61   |D    |D    |
|28077      |G  |C,T,S|homoplasic,no_sig    |gene-ORF8  |62   |V    |L,L,X|
|28826      |C  |T    |homoplasic,no_sig    |gene-N     |185  |R    |C    |
|28854      |C  |T,Y  |homoplasic,no_sig    |gene-N     |194  |S    |L,X  |
|28881      |G  |A,R,K|MNM                  |gene-N     |203  |R    |K,X,X|
|28882      |G  |A,R  |MNM                  |gene-N     |203  |R    |R,R  |
|28883      |G  |C,S,A|MNM                  |gene-N     |204  |G    |R,X,R|
|29353      |C  |T    |homoplasic,no_sig    |gene-N     |360  |Y    |Y    |
|29700      |A  |G    |homoplasic,no_sig    |.          |.    |.    |.    |
|29736      |G  |T    |homoplasic           |.          |.    |.    |.    |
|29774      |C  |T    |homoplasic,no_sig    |.          |.    |.    |.    |
|29804-29903|.  |.    |seq_end              |.          |.    |     |     |

# Description of the columns in the vcf-version

The information presented in the table above is also [available as a .vcf formatted file](https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/problematic_sites_sarsCov2.vcf).

The adapted vcf format contains all 8 mandatory as well as several additional columns.

| Header | Description |
|--------|-------------|
|CHROM   |Name of the reference sequence |
|POS     |1-based position of the variation on the reference |
|ID      | NA |
|REF     | Reference base |
|ALT     | List of alternative alleles at the position (IUPAC ambiguity code) |
|QUAL    | NA |
|FILTER  | NA |
|INFO    | Initials of submitter |
|EXC     | List of reasons for suggested exclusion (tags described in separate table) |
|SRC     | Source laboratory of samples showing the variant |
|GENE    | Position falls into range of this gene |
|AAPOS   | Position of amino acid residue within gene |
|REFAA   | Reference amino acid residue |
|ALTAA   | List of alternative amino acid residues (IUPAC ambiguity code) |



| Tag | Description |
|------|-------------|
| homoplasic | homoplasic site (not necessarily to be masked in itself) |
| highly_hom | highly homoplasic site (recommended to be masked)
| no_sig | no phylogenetic signal as inferred by the delta statistic (recommended to be masked) |
| single_src | only observed in samples from a single laboratory (recommended to be masked) |
| seq_end | alignment ends are affected by low coverage and high error rates (recommended to be masked, but might be more stringent than necessary) |


Suggestions, additions and issues are very gratefully received.