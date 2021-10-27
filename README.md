[![Build Status](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2.svg?branch=master)](https://travis-ci.com/github/W-L/ProblematicSites_SARS-CoV2)

- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)


# Human-friendly version of the vcf file
|    POS    |REF|     ALT     |FILTER |                                  EXC                                  |   GENE    |AA_POS|AA_REF|   AA_ALT    |
|-----------|---|-------------|-------|-----------------------------------------------------------------------|-----------|------|------|-------------|
|1-55       |.  |.            |mask   |seq_end                                                                |.          |.     |.     |.            |
|76         |T  |K,Y,W,C,A    |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.            |
|78         |T  |K,Y,A,C,W,G  |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.            |
|150        |T  |C,Y          |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.            |
|153        |T  |Y,G          |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.            |
|285        |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|7     |G     |X,V,D        |
|320        |C  |Y,S,T,A,G    |caution|narrow_src<br>highly_ambiguous                                         |gene-orf1ab|19    |P     |X,X,S,T,A    |
|538        |A  |R,W,G        |caution|ambiguous                                                              |gene-orf1ab|91    |E     |E,X,E        |
|553        |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|96    |Q     |H,X,H,Q      |
|558        |G  |R,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|98    |G     |X,X,V        |
|635        |C  |T,Y          |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|124   |R     |C,X          |
|660        |G  |K,S,A        |caution|ambiguous                                                              |gene-orf1ab|132   |G     |X,X,D        |
|663        |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|133   |G     |X,X,V,D      |
|759        |A  |D,T          |caution|ambiguous<br>single_src                                                |gene-orf1ab|165   |H     |X,L          |
|856        |T  |C,A,Y        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|197   |P     |P,P,P        |
|1001       |G  |R,A          |caution|ambiguous<br>amended                                                   |gene-orf1ab|246   |E     |X,K          |
|1406       |G  |K,T,A,S      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|381   |E     |X,*,K,Z      |
|1707       |C  |T,A,Y        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|481   |S     |F,Y,X        |
|1814       |A  |.            |caution|ambiguous<br>amended                                                   |gene-orf1ab|517   |K     |.            |
|1895       |G  |K,T          |mask   |ambiguous                                                              |gene-orf1ab|544   |V     |X,L          |
|1947       |T  |C,Y,G        |caution|ambiguous<br>narrow_src                                                |gene-orf1ab|561   |V     |A,X,G        |
|2087       |T  |Y            |caution|ambiguous                                                              |gene-orf1ab|608   |L     |L            |
|2091       |C  |T,Y          |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|609   |T     |I,X          |
|2094       |C  |T,Y          |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|610   |S     |L,X          |
|2101       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|612   |W     |X,C          |
|2198       |G  |R,T,A        |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|645   |G     |X,C,S        |
|2247       |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|661   |G     |X,X,V,D      |
|2381       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|706   |G     |X,C          |
|2604       |G  |K,T          |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-orf1ab|780   |G     |X,V          |
|3050       |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|929   |E     |X,*,K        |
|3073       |T  |C,W,Y        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|936   |C     |C,X,C        |
|3145       |G  |T            |mask   |homoplasic<br>single_src                                               |gene-orf1ab|960   |L     |F            |
|3191       |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|976   |E     |*,X,Q,K      |
|3480       |C  |T,Y          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1072  |A     |V,X          |
|3504       |A  |T,W,M,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1080  |N     |I,X,X,S      |
|3564       |G  |K,T          |mask   |highly_ambiguous<br>highly_homoplasic<br>single_src                    |gene-orf1ab|1100  |G     |X,V          |
|3639       |G  |R,A          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1125  |G     |X,D          |
|3778       |A  |G            |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1171  |T     |T            |
|3877       |T  |K,C,A,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1204  |A     |A,A,A,A      |
|4050       |A  |C            |mask   |homoplasic<br>single_src<br>amended                                    |gene-orf1ab|1262  |N     |T            |
|4221       |A  |D,T,W        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|1319  |K     |X,I,X        |
|4463       |T  |K,C,Y,G      |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|1400  |S     |X,P,X,A      |
|4505       |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1414  |G     |X,X,C,S      |
|4692       |C  |T,A          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1476  |S     |F,Y          |
|4854       |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1530  |R     |X,I,K        |
|4991       |A  |T,C,M        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1576  |N     |Y,H,X        |
|5011       |A  |C,M          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1582  |Q     |H,X          |
|5130       |C  |T,A,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1622  |P     |L,H,R        |
|5196       |G  |T,K,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1644  |G     |V,X,A        |
|5233       |G  |D,K,R,T,A    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1656  |W     |X,X,X,C,*    |
|5257       |A  |M,W,G        |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|1664  |L     |X,X,L        |
|5322       |T  |K,Y,W,A,G    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1686  |I     |X,X,X,K,R    |
|5375       |G  |K,T,S        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1704  |A     |X,S,X        |
|5393       |T  |C,Y          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1710  |F     |L,X          |
|5498       |A  |R            |caution|ambiguous<br>amended                                                   |gene-orf1ab|1745  |K     |X            |
|5657       |G  |K,T,A,S      |caution|ambiguous<br>single_src                                                |gene-orf1ab|1798  |V     |X,L,I,X      |
|5736       |C  |T,Y          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1824  |A     |V,X          |
|5743       |G  |T,S          |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1826  |E     |D,X          |
|5744       |T  |Y            |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1827  |Y     |X            |
|5765       |G  |R,K          |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X,X          |
|5766       |G  |S            |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X            |
|5847       |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1861  |G     |V,X,A,D      |
|5880       |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1872  |S     |I,X,T,N      |
|6167       |G  |R,K          |mask   |ambiguous<br>single_src                                                |gene-orf1ab|1968  |V     |X,X          |
|6255       |C  |T            |mask   |highly_homoplasic<br>narrow_src                                        |gene-orf1ab|1997  |A     |V            |
|6309       |G  |K,R,T,C,A    |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |X,X,I,T,N    |
|6310       |C  |Y,M,T,A,G    |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |S,X,S,R,R    |
|6312       |C  |Y,M,T,A,G    |caution|neighbour_linked                                                       |gene-orf1ab|2016  |T     |X,X,I,K,R    |
|6483       |G  |R,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2073  |G     |X,X,V        |
|6804       |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2180  |C     |F,X,S,Y      |
|6866       |A  |T,W          |caution|ambiguous                                                              |gene-orf1ab|2201  |N     |Y,X          |
|6869       |A  |T,W          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|2202  |T     |S,X          |
|6874       |T  |C,Y,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2203  |V     |V,V,V        |
|6877       |G  |K,T          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2204  |K     |X,N          |
|6971       |T  |C,W,Y        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2236  |L     |L,J,L        |
|6975       |G  |R,T          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2237  |S     |X,I          |
|6977       |G  |R,K,A        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2238  |V     |X,X,I        |
|7017       |G  |K,T,A,S      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2251  |G     |X,V,D,X      |
|7038       |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2258  |G     |X,X,V,D      |
|7090       |T  |K,G          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2275  |N     |X,K          |
|7118       |T  |K,Y,C,A,G    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2285  |S     |X,X,P,T,A    |
|7214       |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2317  |D     |X,Y,N        |
|7246       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2327  |W     |X,C          |
|7305       |T  |K,A,Y        |caution|ambiguous<br>single_src                                                |gene-orf1ab|2347  |M     |X,K,X        |
|7396       |T  |C,W,Y        |caution|ambiguous                                                              |gene-orf1ab|2377  |I     |I,I,I        |
|7805       |G  |R,A          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2514  |E     |X,K          |
|8022       |T  |K,C,G        |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-orf1ab|2586  |V     |X,A,G        |
|8026       |A  |T,W,G        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|2587  |A     |A,A,A        |
|8328       |T  |G            |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2688  |L     |R            |
|8459       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2732  |A     |X,S          |
|8550       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2762  |G     |X,V          |
|8658       |A  |T,C,W,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2798  |K     |I,T,X,R      |
|8678       |G  |R,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2805  |E     |X,*,K        |
|8688       |G  |K,T,A,B      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2808  |G     |X,V,E,X      |
|8696       |G  |K,R,B,T,A    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2811  |A     |X,X,X,S,T    |
|8790       |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|2842  |G     |X,V          |
|8827       |T  |W            |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2854  |I     |I            |
|8828       |G  |K,A          |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2855  |A     |X,T          |
|8835       |T  |C            |mask   |amplicon_drop_or_primer_artefact                                       |gene-orf1ab|2857  |V     |A            |
|8886       |T  |A,C,W,Y      |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2874  |L     |*,S,X,X      |
|8887       |A  |R,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2874  |L     |L,F,L        |
|8943       |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2893  |G     |X,V,D        |
|8999       |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2912  |A     |X,S,T        |
|9039       |C  |T,M,Y        |mask   |ambiguous<br>single_src                                                |gene-orf1ab|2925  |A     |V,X,X        |
|9141       |G  |K,R,T,C,A    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2959  |G     |X,X,V,A,D    |
|9249       |G  |T,K,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2995  |G     |V,X,A        |
|9276       |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3004  |W     |L,X,S,*      |
|9471       |G  |C,A,S        |caution|ambiguous<br>single_src                                                |gene-orf1ab|3069  |R     |T,K,X        |
|10046      |G  |R,K,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3261  |V     |X,X,I        |
|10122      |G  |K,T,S        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3286  |G     |X,V,X        |
|10129      |T  |C,W,Y        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|3288  |T     |T,T,T        |
|10157      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3298  |V     |X,L,I        |
|10239      |C  |M,A          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|3325  |S     |X,Y          |
|10266      |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3334  |G     |X,X,V,D      |
|10554      |T  |D,A          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|3430  |L     |X,*          |
|10716      |A  |C,W,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|3484  |N     |T,X,S        |
|10764      |A  |T,C,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3500  |Y     |F,S,C        |
|10986      |G  |D,K,C,S,T    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3574  |R     |X,X,T,X,I    |
|11048      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3595  |V     |X,F          |
|11074      |C  |T,Y          |mask   |highly_homoplasic                                                      |gene-orf1ab|3603  |F     |F,F          |
|11083      |G  |K,T,A        |mask   |highly_homoplasic                                                      |gene-orf1ab|3606  |L     |X,F,L        |
|11392      |G  |T,K,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3709  |W     |C,X,C        |
|11535      |G  |K,T          |mask   |ambiguous<br>highly_homoplasic<br>single_src                           |gene-orf1ab|3757  |G     |X,V          |
|12041      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3926  |D     |Y,X,H,N      |
|12164      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3967  |A     |X,S,T        |
|12413      |A  |R,T,C,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4050  |N     |B,Y,H,D      |
|12491      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4076  |D     |Y,X,H,N      |
|12506      |A  |R            |caution|ambiguous<br>single_src                                                |gene-orf1ab|4081  |K     |X            |
|12685      |G  |K,T,A        |caution|narrow_src<br>highly_ambiguous                                         |gene-orf1ab|4140  |Q     |X,H,Q        |
|12698      |A  |C,W,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4145  |S     |R,X,G        |
|12751      |T  |A,W          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4162  |A     |A,A          |
|13117      |A  |C,M,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4284  |L     |L,L,L        |
|13161      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4299  |C     |X,F,Y        |
|13193      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4310  |V     |X,F,I        |
|13239      |C  |T,Y,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4325  |S     |L,X,W        |
|13402      |T  |K,C,G        |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4379  |Y     |X,Y,*        |
|13408      |T  |K            |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4381  |C     |X            |
|13476      |C  |T,Y          |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|4404  |C     |V,X          |
|13512      |A  |T,C,G        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |L,P,R        |
|13513      |G  |K,T,A        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |X,H,Q        |
|13514      |G  |T,C,A,S      |caution|neighbour_linked                                                       |gene-orf1ab|4417  |G     |S,P,T,X      |
|13571      |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4436  |G     |X,F          |
|13599      |T  |C,Y          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4445  |C     |A,X          |
|13650      |T  |K            |caution|ambiguous<br>single_src                                                |gene-orf1ab|4462  |F     |X            |
|13686      |T  |C,A,Y        |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |T,K,X        |
|13687      |G  |T            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4474  |H     |I            |
|13693      |A  |R,T,W        |caution|neighbour_linked                                                       |gene-orf1ab|4476  |E     |K,N,X        |
|14197      |G  |K,T,A,S      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4644  |T     |L,L,L,L      |
|14222      |T  |B,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4653  |L     |X,E          |
|14223      |A  |C,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4653  |L     |S,*          |
|14225      |C  |M,T,A,B      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4654  |T     |X,*,K,X      |
|14277      |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4671  |R     |X,V          |
|14488      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4741  |R     |X,D,E        |
|14536      |C  |T,Y          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4757  |R     |D,D          |
|14548      |G  |D,R,K,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4761  |K     |X,R,X,R      |
|14553      |A  |T,C,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4763  |L     |F,S,C        |
|14851      |T  |C,A,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4862  |L     |Y,*,*        |
|14852      |T  |C,Y,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4863  |F     |L,L,V        |
|15075      |G  |K,T,A,S      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4937  |K     |X,I,N,X      |
|15103      |C  |T            |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4946  |A     |L            |
|15199      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4978  |T     |L,L,L        |
|15230      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4989  |G     |X,F,I        |
|15435      |A  |R,G          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|5057  |E     |X,R          |
|15513      |T  |A,C,W        |caution|single_src<br>ambiguous                                                |gene-orf1ab|5083  |N     |K,T,X        |
|15521      |T  |A            |mask   |amplicon_drop_or_primer_artefact                                       |gene-orf1ab|5086  |F     |Y            |
|15769      |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5168  |V     |X,X,C,*      |
|15771      |T  |K,D,Y,H,W,A  |caution|ambiguous<br>single_src                                                |gene-orf1ab|5169  |A     |X,X,X,X,X,Q  |
|15922      |T  |C,Y          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|5219  |V     |C,C          |
|16130      |G  |T,A          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5289  |G     |Y,N          |
|16132      |C  |T            |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5289  |G     |D            |
|16188      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5308  |W     |X,V          |
|16210      |A  |R,D,W        |caution|ambiguous<br>single_src                                                |gene-orf1ab|5315  |A     |L,L,L        |
|16290      |T  |K            |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|5342  |A     |X            |
|16537      |G  |R,K,T,A      |caution|ambiguous<br>single_src                                                |gene-orf1ab|5424  |S     |A,A,A,A      |
|16738      |G  |T,K,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5491  |W     |G,G,G        |
|16787      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5508  |G     |X,F          |
|16887      |C  |T,Y          |mask   |highly_homoplasic                                                      |gene-orf1ab|5541  |Y     |I,X          |
|16988      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5575  |G     |X,S,T        |
|17096      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5611  |G     |X,L          |
|17178      |T  |C,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5638  |V     |S,W          |
|17179      |G  |T,S          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5638  |V     |F,X          |
|17182      |G  |A            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5639  |D     |I            |
|17479      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5738  |K     |X,S          |
|17567      |G  |K,A          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|5768  |C     |X,I          |
|17668      |G  |R,K,T,S      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5801  |K     |R,X,S,X      |
|17675      |T  |C,Y          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5804  |I     |P,X          |
|17716      |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5817  |I     |*,X,Y,*      |
|17754      |G  |K,T,S        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5830  |W     |X,V,X        |
|17848      |G  |K,T,B        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5861  |Q     |X,S,X        |
|18297      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6011  |W     |X,V,E        |
|18445      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6060  |R     |X,D,E        |
|18465      |T  |K,G          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6067  |P     |X,R          |
|18505      |G  |R            |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6080  |K     |K            |
|18506      |G  |K,S          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6081  |G     |X,X          |
|18690      |T  |K,C          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6142  |F     |X,S          |
|18716      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6151  |C     |X,F          |
|19250      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6329  |R     |X,*,K        |
|19286      |G  |R,T,C,A      |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6341  |G     |X,L,L,M      |
|19298      |A  |R,D,T,W      |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|6345  |Y     |X,X,L,X      |
|19299      |T  |Y,G          |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|6345  |Y     |X,R          |
|19338      |A  |R,M,G        |caution|highly_ambiguous<br>narrow_src                                         |gene-orf1ab|6358  |K     |X,X,R        |
|19339      |A  |R,M,W        |caution|ambiguous<br>single_src                                                |gene-orf1ab|6358  |K     |K,X,X        |
|19344      |T  |K,C,A,Y      |caution|ambiguous<br>amended                                                   |gene-orf1ab|6360  |A     |X,P,H,X      |
|19369      |T  |Y,G          |caution|ambiguous<br>amended                                                   |gene-orf1ab|6368  |P     |H,Q          |
|19406      |G  |R,K,A        |caution|highly_ambiguous<br>single_src                                         |gene-orf1ab|6381  |G     |X,X,K        |
|19482      |T  |K,W          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6406  |G     |X,X          |
|19484      |C  |T,Y          |mask   |highly_ambiguous<br>amended                                            |gene-orf1ab|6407  |A     |L,L          |
|19548      |A  |D,R,T,W,G    |mask   |ambiguous<br>single_src                                                |gene-orf1ab|6428  |S     |X,X,L,X,R    |
|19732      |G  |R,K,T,A      |caution|homoplasic<br>narrow_src                                               |gene-orf1ab|6489  |G     |V,V,V,V      |
|20056      |G  |K,A          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6597  |E     |X,K          |
|20123      |T  |C,Y          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6620  |I     |L,L          |
|20126      |G  |R,K,S,A      |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|6621  |G     |X,X,Z,K      |
|20128      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6621  |G     |D,X,D,E      |
|20254      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6663  |I     |X,F          |
|20465      |A  |R,W,G        |mask   |highly_homoplasic<br>single_src                                        |gene-orf1ab|6734  |D     |X,X,V        |
|20857      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6864  |R     |D,X,D,E      |
|21149      |G  |A            |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6962  |G     |K            |
|21151      |G  |D,T          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6962  |G     |X,D          |
|21209      |T  |C,H          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|6982  |M     |R,X          |
|21212      |G  |A            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|6983  |G     |N            |
|21281      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|7006  |G     |Y,X,H,N      |
|21302      |C  |M,T,A,S      |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |X,Y,N,X      |
|21304      |C  |Y,S,M,T,A    |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |H,X,X,H,Q    |
|21305      |G  |R,K,T,A      |caution|neighbour_linked                                                       |gene-orf1ab|7014  |R     |X,X,S,T      |
|21379      |T  |C,Y          |caution|ambiguous<br>single_src                                                |gene-orf1ab|7038  |S     |L,L          |
|21550      |A  |C,M          |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7095  |N     |T,T          |
|21551      |A  |R,T,W        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7096  |N     |X,S,X        |
|21575      |C  |T,Y          |mask   |highly_homoplasic                                                      |gene-S     |5     |L     |F,X          |
|21609      |T  |K,W          |caution|ambiguous<br>single_src                                                |gene-S     |16    |V     |X,X          |
|21658      |C  |Y,M,T,H,G    |caution|ambiguous                                                              |gene-S     |32    |F     |F,X,F,X,L    |
|21968      |T  |C,G          |mask   |single_src<br>highly_homoplasic                                        |gene-S     |136   |C     |R,G          |
|21987      |G  |T,K,C,A      |mask   |amplicon_drop_or_primer_artefact<br>back_to_ref                        |gene-S     |142   |G     |V,X,A,D      |
|22329      |C  |V,T,M,Y      |caution|ambiguous<br>single_src                                                |gene-S     |256   |S     |X,L,X,X      |
|22335      |G  |K,T,A        |mask   |highly_ambiguous<br>amended                                            |gene-S     |258   |W     |X,L,*        |
|22389      |T  |K,C,W,Y      |caution|ambiguous<br>single_src                                                |gene-S     |276   |L     |X,P,X,X      |
|22393      |A  |R,W,G        |caution|ambiguous<br>amended                                                   |gene-S     |277   |L     |L,X,L        |
|22410      |G  |K,D,R,T,C,A  |caution|narrow_src<br>highly_ambiguous                                         |gene-S     |283   |G     |X,X,X,V,A,E  |
|22416      |T  |C,Y          |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |285   |I     |T,X          |
|22420      |A  |T,W          |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |286   |T     |T,T          |
|22488      |A  |R,C,M,T,W    |caution|ambiguous<br>amended                                                   |gene-S     |309   |E     |X,A,X,V,X    |
|22500      |A  |R,M,W        |caution|ambiguous<br>single_src                                                |gene-S     |313   |Y     |X,X,X        |
|22506      |C  |T,Y,S        |caution|single_src<br>highly_ambiguous                                         |gene-S     |315   |T     |I,X,X        |
|22515      |T  |K,W,Y        |caution|ambiguous<br>narrow_src                                                |gene-S     |318   |F     |X,X,X        |
|22516      |T  |D,K,Y,C,W    |mask   |highly_ambiguous<br>single_src                                         |gene-S     |318   |F     |X,X,F,F,X    |
|22521      |T  |K,Y          |mask   |highly_ambiguous                                                       |gene-S     |320   |V     |X,X          |
|22651      |T  |C,A          |mask   |single_src<br>highly_homoplasic                                        |gene-S     |363   |A     |A,A          |
|22661      |G  |T,A,S        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-S     |367   |V     |F,I,X        |
|22797      |C  |A,T,M,Y      |caution|single_src<br>highly_ambiguous<br>homoplasic                           |gene-S     |412   |P     |Q,L,X,X      |
|22802      |C  |A,T,M,Y      |mask   |homoplasic<br>single_src<br>amended<br>interspecific_contamination     |gene-S     |414   |Q     |K,*,X,X      |
|22892      |A  |T,C          |caution|single_src<br>highly_ambiguous                                         |gene-S     |444   |K     |*,Q          |
|22904      |A  |R,V,H,M,T,W,G|caution|single_src<br>highly_ambiguous                                         |gene-S     |448   |N     |B,X,X,X,Y,X,D|
|23016      |G  |T,K,C,A      |caution|single_src<br>highly_ambiguous                                         |gene-S     |485   |G     |V,X,A,D      |
|23116      |A  |T,W          |caution|ambiguous<br>single_src                                                |gene-S     |518   |L     |L,L          |
|23122      |A  |R,V,H,M,T,W,G|caution|single_src<br>highly_ambiguous                                         |gene-S     |520   |A     |A,A,A,A,A,A,A|
|23144      |A  |G            |caution|ambiguous<br>amended                                                   |gene-S     |528   |K     |E            |
|23162      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-S     |534   |V     |X,F,I        |
|23288      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-S     |576   |V     |X,F,I        |
|23291      |C  |T,Y          |caution|single_src<br>highly_ambiguous                                         |gene-S     |577   |R     |C,X          |
|23292      |G  |R,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |577   |R     |X,X,L        |
|23302      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-S     |580   |Q     |X,H,Q        |
|23343      |G  |R,K,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-S     |594   |G     |X,X,V,D      |
|23519      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |653   |A     |X,S          |
|23652      |T  |C,A,Y        |caution|single_src<br>highly_ambiguous                                         |gene-S     |697   |M     |T,K,X        |
|23738      |A  |T,W,G        |caution|single_src<br>highly_ambiguous                                         |gene-S     |726   |I     |F,X,V        |
|23745      |C  |T,Y          |caution|single_src<br>highly_ambiguous                                         |gene-S     |728   |P     |L,X          |
|23763      |C  |S,T,Y,G      |caution|single_src<br>highly_ambiguous                                         |gene-S     |734   |T     |X,I,X,R      |
|23766      |C  |T,Y,S        |caution|single_src<br>highly_ambiguous                                         |gene-S     |735   |S     |L,X,X        |
|23775      |G  |K,T,S        |caution|single_src<br>highly_ambiguous                                         |gene-S     |738   |C     |X,F,X        |
|23855      |C  |T,A,Y        |caution|single_src<br>highly_ambiguous                                         |gene-S     |765   |R     |C,S,X        |
|24389      |A  |M,C,W        |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |X,R,X        |
|24390      |G  |T,K,C,S      |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |I,X,T,X      |
|24410      |G  |C,A          |mask   |amplicon_drop_or_primer_artefact<br>back_to_ref                        |gene-S     |950   |D     |H,N          |
|24497      |G  |T,K,C        |caution|single_src<br>highly_ambiguous                                         |gene-S     |979   |D     |Y,X,H        |
|24557      |G  |K,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-S     |999   |G     |X,C,S        |
|24622      |T  |Y            |mask   |highly_ambiguous<br>single_src                                         |gene-S     |1020  |A     |A            |
|24673      |A  |G            |caution|ambiguous<br>amended                                                   |gene-S     |1037  |S     |S            |
|24728      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |1056  |A     |X,S          |
|24933      |G  |K,T          |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-S     |1124  |G     |X,V          |
|24942      |A  |R,T,W        |caution|ambiguous<br>single_src                                                |gene-S     |1127  |D     |X,V,X        |
|25202      |T  |K            |mask   |highly_ambiguous                                                       |gene-S     |1214  |W     |X            |
|25381      |A  |R,C,M        |mask   |homoplasic<br>single_src                                               |gene-S     |1273  |T     |T,T,T        |
|25382      |T  |C            |mask   |single_src<br>highly_homoplasic                                        |gene-S     |1274  |T     |Q            |
|25446      |T  |A,C,W,G      |caution|single_src<br>highly_ambiguous                                         |gene-ORF3a |18    |G     |G,G,G,G      |
|25798      |A  |G            |caution|ambiguous<br>amended                                                   |gene-ORF3a |136   |K     |E            |
|25902      |T  |A,C,W,G      |caution|single_src<br>highly_ambiguous<br>neighbour_linked                     |gene-ORF3a |170   |T     |T,T,T,T      |
|25908      |T  |A,C,W        |caution|single_src<br>highly_ambiguous<br>neighbour_linked                     |gene-ORF3a |172   |G     |G,G,G        |
|25961      |C  |T,A,Y,S      |caution|single_src<br>highly_ambiguous                                         |gene-ORF3a |190   |T     |I,N,X,X      |
|26549      |C  |T,Y          |mask   |homoplasic<br>single_src                                               |gene-M     |9     |T     |T,T          |
|26700      |G  |K,T          |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-M     |60    |V     |X,L          |
|26709      |G  |R,K,T,A      |caution|ambiguous<br>amended                                                   |gene-M     |63    |A     |X,X,S,T      |
|27033      |G  |K,T,A,S      |caution|single_src<br>highly_ambiguous                                         |gene-M     |171   |A     |X,S,T,X      |
|27534      |T  |C,W,Y,G      |caution|ambiguous<br>single_src                                                |gene-ORF7a |47    |H     |H,X,H,Q      |
|27658      |A  |D,T,W,G      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-ORF7a |89    |R     |X,*,X,G      |
|27660      |A  |T,C,V,G      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-ORF7a |89    |R     |S,S,X,R      |
|27720      |T  |K,C,W        |caution|ambiguous<br>single_src                                                |gene-ORF7a |109   |F     |X,F,X        |
|27760      |T  |K,A,Y        |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.            |
|27761      |T  |C            |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.            |
|27784      |A  |T,W,G        |mask   |ambiguous<br>single_src                                                |.          |.     |.     |.            |
|27792      |T  |K,W          |caution|ambiguous<br>amended                                                   |.          |.     |.     |.            |
|28004      |T  |C,Y          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |37    |C     |C,C          |
|28005      |C  |T,Y,G        |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |S,X,A        |
|28006      |C  |T            |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |L            |
|28008      |A  |G            |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |39    |I     |V            |
|28184      |T  |C,H          |mask   |single_src<br>highly_homoplasic                                        |gene-ORF8  |97    |S     |S,X          |
|28253      |C  |Y,S,T,A,G    |mask   |highly_homoplasic                                                      |gene-ORF8  |120   |F     |F,X,F,L,L    |
|28517      |G  |K,T,S        |caution|ambiguous<br>single_src                                                |gene-N     |82    |D     |X,Y,X        |
|28559      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-N     |96    |G     |X,C          |
|28676      |A  |R,C,M,G      |caution|ambiguous<br>single_src                                                |gene-N     |135   |T     |X,P,X,A      |
|28780      |A  |R,D,W        |caution|ambiguous<br>single_src                                                |gene-N     |169   |K     |K,X,X        |
|28881      |G  |K,R,M,T,A    |caution|neighbour_linked                                                       |gene-N     |203   |R     |X,X,X,M,K    |
|28882      |G  |K,R,T,S,C,A  |caution|neighbour_linked                                                       |gene-N     |203   |R     |X,R,S,X,S,R  |
|28883      |G  |R,C,A,S      |caution|neighbour_linked                                                       |gene-N     |204   |G     |X,R,R,X      |
|28886      |A  |C,M,T,W,G    |caution|single_src<br>highly_ambiguous                                         |gene-N     |205   |T     |P,X,S,X,A    |
|28985      |G  |D,K,R,T,A    |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-N     |238   |G     |X,X,X,C,S    |
|29037      |C  |T,M,Y        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |255   |S     |F,X,X        |
|29039      |A  |T,W          |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |256   |K     |*,X          |
|29049      |G  |R,T,A        |caution|single_src<br>highly_ambiguous                                         |gene-N     |259   |R     |X,L,Q        |
|29058      |G  |K,T,A        |mask   |single_src<br>highly_homoplasic                                        |gene-N     |262   |R     |X,L,H        |
|29378      |A  |W            |caution|ambiguous<br>amended                                                   |gene-N     |369   |K     |X            |
|29425      |G  |T,A,S        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-N     |384   |Q     |H,Q,X        |
|29427      |G  |K,R,T,S,C,A  |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |X,X,I,X,T,K  |
|29428      |A  |R,C,G        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |R,S,R        |
|29553      |G  |T,A          |mask   |highly_homoplasic<br>single_src                                        |.          |.     |.     |.            |
|29594      |A  |T,C          |mask   |single_src<br>highly_homoplasic                                        |gene-ORF10 |13    |I     |L,L          |
|29737      |G  |K,R,T,S,C,A  |caution|ambiguous<br>single_src                                                |.          |.     |.     |.            |
|29783      |G  |T,K,C,A      |mask   |highly_homoplasic                                                      |.          |.     |.     |.            |
|29786      |G  |K,C,S        |caution|homoplasic<br>single_src                                               |.          |.     |.     |.            |
|29827      |A  |T,G          |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.            |
|29830      |G  |T,C,A        |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.            |
|29804-29903|.  |.            |mask   |seq_end                                                                |.          |.     |.     |.            |


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
