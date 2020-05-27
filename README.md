- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)

# Human-friendly version of the vcf file

|    POS    |REF|  ALT  |FILTER |            EXC            |   GENE    |AAPOS|REFAA| ALTAA |
|-----------|---|-------|-------|---------------------------|-----------|-----|-----|-------|
|1-55       |.  |.      |seq_end|.                          |.          |     |     |       |
|635        |C  |Y,T    |mask   |highly_ambiguous           |gene-orf1ab|  124|R    |X,C    |
|2091       |C  |T,Y    |mask   |highly_ambiguous           |gene-orf1ab|  609|T    |I,X    |
|2094       |C  |T,Y    |mask   |highly_ambiguous           |gene-orf1ab|  610|S    |L,X    |
|3145       |G  |T      |mask   |homoplasic;single_src      |gene-orf1ab|  960|L    |F      |
|3564       |G  |T,K    |mask   |highly_ambiguous           |gene-orf1ab| 1100|G    |V,X    |
|4050       |A  |C      |mask   |homoplasic;single_src      |gene-orf1ab| 1262|N    |T      |
|5736       |C  |T,Y    |mask   |homoplasic;single_src      |gene-orf1ab| 1824|A    |V,X    |
|6309       |G  |T,A,R  |caution|neighbour_linked           |gene-orf1ab| 2015|S    |I,N,X  |
|6310       |C  |T,A,M  |caution|neighbour_linked           |gene-orf1ab| 2015|S    |S,R,X  |
|6312       |C  |A,T,G,M|caution|neighbour_linked           |gene-orf1ab| 2016|T    |K,I,R,X|
|6869       |A  |T,W,R  |mask   |highly_ambiguous           |gene-orf1ab| 2202|T    |S,X,X  |
|6971       |T  |C      |caution|neighbour_linked;single_src|gene-orf1ab| 2236|L    |L      |
|6975       |G  |T      |caution|neighbour_linked;single_src|gene-orf1ab| 2237|S    |I      |
|6977       |G  |A      |caution|neighbour_linked;single_src|gene-orf1ab| 2238|V    |I      |
|8022       |T  |K,G    |mask   |highly_ambiguous           |gene-orf1ab| 2586|V    |X,G    |
|8790       |G  |K,T    |mask   |highly_ambiguous           |gene-orf1ab| 2842|G    |X,V    |
|10129      |T  |C,Y    |mask   |highly_ambiguous           |gene-orf1ab| 3288|T    |T,T    |
|11074      |C  |Y,T    |mask   |highly_homoplasic          |gene-orf1ab| 3603|F    |F,F    |
|11083      |G  |T,K,A  |mask   |highly_homoplasic          |gene-orf1ab| 3606|L    |F,X,L  |
|11535      |G  |T,K    |mask   |homoplasic;single_src      |gene-orf1ab| 3757|G    |V,X    |
|13402      |T  |G,K    |mask   |homoplasic;single_src      |gene-orf1ab| 4379|Y    |*,X    |
|13408      |T  |C,K    |mask   |homoplasic;single_src      |gene-orf1ab| 4381|C    |C,X    |
|13476      |C  |Y,T    |mask   |highly_ambiguous           |gene-orf1ab| 4404|C    |X,V    |
|13512      |A  |T      |caution|neighbour_linked           |gene-orf1ab| 4416|T    |L      |
|13513      |G  |T      |caution|neighbour_linked           |gene-orf1ab| 4416|T    |H      |
|13514      |G  |A      |caution|neighbour_linked           |gene-orf1ab| 4417|G    |T      |
|13571      |G  |K,T    |mask   |highly_ambiguous           |gene-orf1ab| 4436|G    |X,F    |
|13686      |T  |Y,A    |caution|neighbour_linked           |gene-orf1ab| 4474|H    |X,K    |
|13687      |G  |T      |caution|neighbour_linked           |gene-orf1ab| 4474|H    |I      |
|13693      |A  |T      |caution|neighbour_linked           |gene-orf1ab| 4476|E    |N      |
|14277      |G  |T,K    |mask   |homoplasic;single_src      |gene-orf1ab| 4671|R    |V,X    |
|15922      |T  |C,Y    |mask   |highly_ambiguous           |gene-orf1ab| 5219|V    |C,C    |
|16887      |C  |T      |mask   |highly_homoplasic          |gene-orf1ab| 5541|Y    |I      |
|19484      |C  |T,Y    |mask   |highly_ambiguous           |gene-orf1ab| 6407|A    |L,L    |
|21302      |C  |T      |caution|neighbour_linked           |gene-orf1ab| 7013|P    |Y      |
|21304      |C  |Y,A,T  |caution|neighbour_linked           |gene-orf1ab| 7013|P    |H,Q,H  |
|21305      |G  |A      |caution|neighbour_linked           |gene-orf1ab| 7014|R    |T      |
|21575      |C  |T,Y    |mask   |highly_homoplasic          |gene-S     |    5|L    |F,X    |
|22335      |G  |T      |mask   |highly_ambiguous           |gene-S     |  258|W    |L      |
|24389      |A  |M,C    |mask   |homoplasic;single_src      |gene-S     |  943|S    |X,R    |
|24390      |G  |S,C,T  |mask   |homoplasic;single_src      |gene-S     |  943|S    |X,T,I  |
|24933      |G  |K,T    |mask   |highly_ambiguous           |gene-S     | 1124|G    |X,V    |
|26549      |C  |T,Y    |mask   |homoplasic;single_src      |gene-M     |    9|T    |T,T    |
|27382      |G  |C,T,K  |caution|neighbour_linked           |gene-ORF6  |   61|D    |H,Y,X  |
|27383      |A  |T      |caution|neighbour_linked           |gene-ORF6  |   61|D    |V      |
|27384      |T  |C,Y    |caution|neighbour_linked           |gene-ORF6  |   61|D    |D,D    |
|28004      |T  |C      |caution|neighbour_linked;single_src|gene-ORF8  |   37|C    |C      |
|28005      |C  |T,G    |caution|neighbour_linked;single_src|gene-ORF8  |   38|P    |S,A    |
|28006      |C  |T      |caution|neighbour_linked;single_src|gene-ORF8  |   38|P    |L      |
|28007      |T  |       |caution|neighbour_linked;single_src|gene-ORF8  |   38|P    |       |
|28008      |A  |G      |caution|neighbour_linked;single_src|gene-ORF8  |   39|I    |V      |
|28009      |T  |       |caution|neighbour_linked;single_src|gene-ORF8  |   39|I    |       |
|28881      |G  |A,R,T,K|caution|MNM                        |gene-N     |  203|R    |K,X,M,X|
|28882      |G  |A,R,T  |caution|MNM                        |gene-N     |  203|R    |R,R,S  |
|28883      |G  |C,S,A  |caution|MNM                        |gene-N     |  204|G    |R,X,R  |
|29037      |C  |T,Y    |mask   |homoplasic;single_src      |gene-N     |  255|S    |F,X    |
|29553      |G  |A      |mask   |homoplasic;single_src      |.          |.    |.    |.      |
|29804-29903|.  |.      |seq_end|.                          |.          |     |     |       |


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
|FILTER  | Masking recommendation (mask or interpret with caution) |
|INFO    | Initials of submitter |
|EXC     | List of reasons for suggested exclusion (tags described in separate table) |
|SRC     | Source laboratory of samples showing the variant |
|GENE    | Position falls into range of this gene |
|AAPOS   | Position of amino acid residue within gene |
|REFAA   | Reference amino acid residue |
|ALTAA   | List of alternative amino acid residues (IUPAC ambiguity code) |



| Tag | Description |
|------|-------------|
| seq_end |Alignment ends are affected by low coverage and high error rates (masking recommended, but might be more stringent than necessary) |
| highly_homoplasic | Positions which are highly homoplasic, and it is unclear if these variants are true frequent mutations or sequencing artefacts (masking recommended) |
| highly_ambiguous | Sites with a high proportion of ambiguous characters, often emerging from a single country or sequencing laboratory (masking recommended) |
| homoplasic | Apparent homoplasic site (masking recommended unless identified from multiple sources) |
| single_src | Only observed in samples from a single laboratory (masking recommended) |
| MNM | Apparent multinucleotide mutations (caution recommended) |
| neighbour_linked | Proximal variants displaying near perfect linkage (caution recommended) |

Suggestions, additions and issues are very gratefully received.
