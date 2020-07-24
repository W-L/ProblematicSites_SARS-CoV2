[![Build Status](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2.svg?branch=master)](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2)

- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)

# Human-friendly version of the vcf file

|    POS    |REF|    ALT    |FILTER |                                  EXC                                  |   GENE    |AA_POS|AA_REF|  AA_ALT   |
|-----------|---|-----------|-------|-----------------------------------------------------------------------|-----------|------|------|-----------|
|1-55       |.  |.          |mask   |seq_end                                                                |.          |.     |.     |.          |
|76         |T  |W,A,C      |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.          |
|78         |T  |Y,K,W,A,G,C|caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.          |
|150        |T  |C,Y        |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.          |
|153        |T  |G,Y        |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.          |
|538        |A  |W          |caution|ambiguous                                                              |gene-orf1ab|91    |E     |X          |
|635        |C  |Y,T        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|124   |R     |X,C        |
|660        |G  |K          |caution|ambiguous                                                              |gene-orf1ab|132   |G     |X          |
|759        |A  |T          |caution|ambiguous<br>single_src                                                |gene-orf1ab|165   |H     |L          |
|1001       |G  |A          |caution|ambiguous<br>amended                                                   |gene-orf1ab|246   |E     |K          |
|1707       |C  |Y,T,A      |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|481   |S     |X,F,Y      |
|1814       |A  |.          |caution|ambiguous<br>amended                                                   |gene-orf1ab|517   |K     |.          |
|1895       |G  |T,K        |mask   |ambiguous                                                              |gene-orf1ab|544   |V     |L,X        |
|1947       |T  |C          |caution|ambiguous<br>narrow_src                                                |gene-orf1ab|561   |V     |A          |
|2087       |T  |C,Y        |caution|ambiguous                                                              |gene-orf1ab|608   |L     |L,L        |
|2091       |C  |T,Y        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|609   |T     |I,X        |
|2094       |C  |T,Y        |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|610   |S     |L,X        |
|2198       |G  |R,A        |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|645   |G     |X,S        |
|2604       |G  |T,K        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-orf1ab|780   |G     |V,X        |
|3145       |G  |T          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|960   |L     |F          |
|3564       |G  |K,T,Y,S,R  |mask   |highly_ambiguous<br>highly_homoplasic<br>single_src                    |gene-orf1ab|1100  |G     |X,V,X,X,X  |
|3639       |G  |R,A        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1125  |G     |X,D        |
|3778       |A  |G          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1171  |T     |T          |
|4050       |A  |C          |mask   |homoplasic<br>single_src<br>amended                                    |gene-orf1ab|1262  |N     |T          |
|4463       |T  |C          |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|1400  |S     |P          |
|5011       |A  |M,C        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1582  |Q     |X,H        |
|5257       |A  |W,G        |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|1664  |L     |X,L        |
|5393       |T  |Y          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1710  |F     |X          |
|5498       |A  |.          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1745  |K     |.          |
|5657       |G  |S,K,T,A    |caution|ambiguous<br>single_src                                                |gene-orf1ab|1798  |V     |X,X,L,I    |
|5736       |C  |T,Y        |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1824  |A     |V,X        |
|5743       |G  |S,T        |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1826  |E     |X,D        |
|5744       |T  |Y          |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1827  |Y     |X          |
|5765       |G  |A,K,R      |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |S,X,X      |
|5766       |G  |C,S        |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |A,X        |
|6167       |G  |R,S,K,C    |mask   |ambiguous<br>single_src                                                |gene-orf1ab|1968  |V     |X,X,X,L    |
|6255       |C  |T,Y        |mask   |highly_homoplasic<br>narrow_src                                        |gene-orf1ab|1997  |A     |V,X        |
|6309       |G  |T,A,R      |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |I,N,X      |
|6310       |C  |A,T,M      |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |R,S,X      |
|6312       |C  |A,Y,M,T,G  |caution|neighbour_linked                                                       |gene-orf1ab|2016  |T     |K,X,X,I,R  |
|6866       |A  |W          |caution|ambiguous                                                              |gene-orf1ab|2201  |N     |X          |
|6869       |A  |T,W,R      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|2202  |T     |S,X,X      |
|6877       |G  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2204  |K     |X          |
|6971       |T  |C,K        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2236  |L     |L,X        |
|6975       |G  |T          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2237  |S     |I          |
|6977       |G  |A          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2238  |V     |I          |
|7090       |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2275  |N     |X          |
|7305       |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2347  |M     |X          |
|7396       |T  |W          |caution|ambiguous                                                              |gene-orf1ab|2377  |I     |I          |
|8022       |T  |K,G        |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-orf1ab|2586  |V     |X,G        |
|8026       |A  |W,T,G      |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|2587  |A     |A,A,A      |
|8790       |G  |T,K        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|2842  |G     |V,X        |
|8827       |T  |W,A        |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2854  |I     |I,I        |
|8828       |G  |K,T        |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2855  |A     |X,S        |
|9039       |C  |Y,M,T,A    |mask   |ambiguous<br>single_src                                                |gene-orf1ab|2925  |A     |X,X,V,D    |
|9471       |G  |S,C        |caution|ambiguous<br>single_src                                                |gene-orf1ab|3069  |R     |X,T        |
|10129      |T  |Y,C,W      |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|3288  |T     |T,T,T      |
|10239      |C  |M,A        |mask   |homoplasic<br>single_src                                               |gene-orf1ab|3325  |S     |X,Y        |
|11074      |C  |T,Y        |mask   |highly_homoplasic                                                      |gene-orf1ab|3603  |F     |F,F        |
|11083      |G  |T,K,A      |mask   |highly_homoplasic                                                      |gene-orf1ab|3606  |L     |F,X,L      |
|11535      |G  |T,K        |mask   |ambiguous<br>highly_homoplasic<br>single_src                           |gene-orf1ab|3757  |G     |V,X        |
|12506      |A  |R          |caution|ambiguous<br>single_src                                                |gene-orf1ab|4081  |K     |X          |
|13402      |T  |K,G        |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4379  |Y     |X,*        |
|13408      |T  |K,C        |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4381  |C     |X,C        |
|13476      |C  |T,Y        |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|4404  |C     |V,X        |
|13512      |A  |T          |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |L          |
|13513      |G  |T,K        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |H,X        |
|13514      |G  |A,K        |caution|neighbour_linked                                                       |gene-orf1ab|4417  |G     |T,X        |
|13571      |G  |K,T        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4436  |G     |X,F        |
|13650      |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|4462  |F     |X          |
|13686      |T  |D,A,Y      |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |X,K,X      |
|13687      |G  |T          |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |I          |
|13693      |A  |T,G        |caution|neighbour_linked                                                       |gene-orf1ab|4476  |E     |N,K        |
|14277      |G  |T,K        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4671  |R     |V,X        |
|15435      |A  |G,R        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|5057  |E     |R,X        |
|15771      |T  |Y,K,W,D,H  |caution|ambiguous<br>single_src                                                |gene-orf1ab|5169  |A     |X,X,X,X,X  |
|15922      |T  |Y,C        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|5219  |V     |C,C        |
|16210      |A  |W,D        |caution|ambiguous<br>single_src                                                |gene-orf1ab|5315  |A     |L,L        |
|16290      |T  |K,Y        |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|5342  |A     |X,X        |
|16537      |G  |R          |caution|ambiguous<br>single_src                                                |gene-orf1ab|5424  |S     |A          |
|16887      |C  |T,Y        |mask   |highly_homoplasic                                                      |gene-orf1ab|5541  |Y     |I,X        |
|18505      |G  |R          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6080  |K     |K          |
|18506      |G  |K          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6081  |G     |X          |
|18690      |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6142  |F     |X          |
|19298      |A  |R,W,D,G    |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|6345  |Y     |X,X,X,V    |
|19299      |T  |Y,G,K      |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|6345  |Y     |X,R,X      |
|19338      |A  |C,G,R,M    |caution|highly_ambiguous<br>narrow_src                                         |gene-orf1ab|6358  |K     |T,R,X,X    |
|19339      |A  |M,W,R      |caution|ambiguous<br>single_src                                                |gene-orf1ab|6358  |K     |X,X,K      |
|19344      |T  |Y,C,K      |caution|ambiguous<br>amended                                                   |gene-orf1ab|6360  |A     |X,P,X      |
|19369      |T  |C,Y        |caution|ambiguous<br>amended                                                   |gene-orf1ab|6368  |P     |H,H        |
|19406      |G  |R,K,A      |caution|highly_ambiguous<br>single_src                                         |gene-orf1ab|6381  |G     |X,X,K      |
|19482      |T  |K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6406  |G     |X          |
|19484      |C  |T,Y        |mask   |highly_ambiguous<br>amended                                            |gene-orf1ab|6407  |A     |L,L        |
|19548      |A  |R,W,G,T    |mask   |ambiguous<br>single_src                                                |gene-orf1ab|6428  |S     |X,X,R,L    |
|19732      |G  |T          |caution|homoplasic<br>narrow_src                                               |gene-orf1ab|6489  |G     |V          |
|20056      |G  |K,T,A      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6597  |E     |X,N,K      |
|20123      |T  |Y,C,W      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6620  |I     |L,L,X      |
|20126      |G  |K,A,S,R    |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|6621  |G     |X,K,Z,X    |
|20465      |A  |W,R,G      |mask   |highly_homoplasic<br>single_src                                        |gene-orf1ab|6734  |D     |X,X,V      |
|21302      |C  |M,T,S      |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |X,Y,X      |
|21304      |C  |A,M,T,Y    |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |Q,X,H,H    |
|21305      |G  |A,S,R      |caution|neighbour_linked                                                       |gene-orf1ab|7014  |R     |T,X,X      |
|21379      |T  |Y,K        |caution|ambiguous<br>single_src                                                |gene-orf1ab|7038  |S     |L,L        |
|21550      |A  |M,C        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7095  |N     |T,T        |
|21551      |A  |W,T,R      |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7096  |N     |X,S,X      |
|21575      |C  |Y,T        |mask   |highly_homoplasic                                                      |gene-S     |5     |L     |X,F        |
|21609      |T  |K,W        |caution|ambiguous<br>single_src                                                |gene-S     |16    |V     |X,X        |
|21658      |C  |M,Y,H,T,G  |caution|ambiguous                                                              |gene-S     |32    |F     |X,F,X,F,L  |
|22335      |G  |T,K,A      |mask   |highly_ambiguous<br>amended                                            |gene-S     |258   |W     |L,X,*      |
|22389      |T  |Y,C        |caution|ambiguous<br>single_src                                                |gene-S     |276   |L     |X,P        |
|22393      |A  |G          |caution|ambiguous<br>amended                                                   |gene-S     |277   |L     |L          |
|22416      |T  |Y,C        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |285   |I     |X,T        |
|22420      |A  |W,T        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |286   |T     |T,T        |
|22488      |A  |R,C        |caution|ambiguous<br>amended                                                   |gene-S     |309   |E     |X,A        |
|22500      |A  |W          |caution|ambiguous<br>single_src                                                |gene-S     |313   |Y     |X          |
|22515      |T  |K,Y        |caution|ambiguous<br>narrow_src                                                |gene-S     |318   |F     |X,X        |
|22516      |T  |W,K,D,C,Y  |mask   |highly_ambiguous<br>single_src                                         |gene-S     |318   |F     |X,X,X,F,F  |
|22521      |T  |K,G,Y      |mask   |highly_ambiguous                                                       |gene-S     |320   |V     |X,G,X      |
|22661      |G  |T,S,K,A    |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-S     |367   |V     |F,X,X,I    |
|22802      |C  |Y,M        |mask   |homoplasic<br>single_src<br>amended<br>interspecific_contamination     |gene-S     |414   |Q     |X,X        |
|23116      |A  |W,T        |caution|ambiguous<br>single_src                                                |gene-S     |518   |L     |L,L        |
|23144      |A  |.          |caution|ambiguous<br>amended                                                   |gene-S     |528   |K     |.          |
|24389      |A  |W,M,C      |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |X,X,R      |
|24390      |G  |S,T,C      |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |X,I,T      |
|24622      |T  |Y          |mask   |highly_ambiguous<br>single_src                                         |gene-S     |1020  |A     |A          |
|24673      |A  |.          |caution|ambiguous<br>amended                                                   |gene-S     |1037  |S     |.          |
|24933      |G  |T,K        |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-S     |1124  |G     |V,X        |
|24942      |A  |W,G,R      |caution|ambiguous<br>single_src                                                |gene-S     |1127  |D     |X,G,X      |
|25202      |T  |K,Y        |mask   |highly_ambiguous                                                       |gene-S     |1214  |W     |X,X        |
|25381      |A  |C,R,M      |mask   |homoplasic<br>single_src                                               |gene-S     |1273  |T     |T,T,T      |
|25798      |A  |G,M        |caution|ambiguous<br>amended                                                   |gene-ORF3a |136   |K     |E,X        |
|26549      |C  |T,Y        |mask   |homoplasic<br>single_src                                               |gene-M     |9     |T     |T,T        |
|26700      |G  |T,K        |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-M     |60    |V     |L,X        |
|26709      |G  |T,R,A      |caution|ambiguous<br>amended                                                   |gene-M     |63    |A     |S,X,T      |
|27534      |T  |W,Y        |caution|ambiguous<br>single_src                                                |gene-ORF7a |47    |H     |X,H        |
|27720      |T  |K          |caution|ambiguous<br>single_src                                                |gene-ORF7a |109   |F     |X          |
|27760      |T  |K,Y,W,A    |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.          |
|27761      |T  |C          |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.          |
|27784      |A  |W,G        |mask   |ambiguous<br>single_src                                                |.          |.     |.     |.          |
|27792      |T  |W,A,Y      |caution|ambiguous<br>amended                                                   |.          |.     |.     |.          |
|28004      |T  |C          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |37    |C     |C          |
|28005      |C  |T,G        |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |S,A        |
|28006      |C  |T          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |L          |
|28008      |A  |G          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |39    |I     |V          |
|28253      |C  |Y,T,G,S,A  |mask   |highly_homoplasic                                                      |gene-ORF8  |120   |F     |F,F,L,X,L  |
|28517      |G  |T,K,S,C    |caution|ambiguous<br>single_src                                                |gene-N     |82    |D     |Y,X,X,H    |
|28780      |A  |W,D,R      |caution|ambiguous<br>single_src                                                |gene-N     |169   |K     |X,X,K      |
|28881      |G  |A,R,T,K    |caution|neighbour_linked                                                       |gene-N     |203   |R     |K,X,M,X    |
|28882      |G  |A,R,T,K,S  |caution|neighbour_linked                                                       |gene-N     |203   |R     |R,R,S,X,X  |
|28883      |G  |C,S,R,A    |caution|neighbour_linked                                                       |gene-N     |204   |G     |R,X,X,R    |
|28985      |G  |R,S,D,T,K,A|mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-N     |238   |G     |X,X,X,C,X,S|
|29037      |C  |Y,T,M      |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |255   |S     |X,F,X      |
|29039      |A  |T,W        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |256   |K     |*,X        |
|29378      |A  |W          |caution|ambiguous<br>amended                                                   |gene-N     |369   |K     |X          |
|29425      |G  |T,S,A      |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-N     |384   |Q     |H,X,Q      |
|29427      |G  |S,R,T,K,C,A|caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |X,X,I,X,T,K|
|29428      |A  |G,R,C      |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |R,R,S      |
|29553      |G  |A          |mask   |highly_homoplasic<br>single_src                                        |.          |.     |.     |.          |
|29737      |G  |K,A,T,S,C  |caution|ambiguous<br>single_src                                                |.          |.     |.     |.          |
|29786      |G  |K,C        |caution|homoplasic<br>single_src                                               |.          |.     |.     |.          |
|29827      |A  |C,G,T      |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.          |
|29830      |G  |T,A,C,S    |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.          |
|29804-29903|.  |.          |mask   |seq_end                                                                |.          |.     |.     |.          |


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

Suggestions, additions and issues are very gratefully received.
