[![Build Status](https://travis-ci.com/W-L/ProblematicSites_SARS-CoV2.svg?branch=master)](https://travis-ci.com/github/W-L/ProblematicSites_SARS-CoV2)

- [Human-friendly version of the vcf file](#human-friendly-version-of-the-vcf-file)
- [Description of the columns in the vcf-version](#description-of-the-columns-in-the-vcf-version)


# Human-friendly version of the vcf file

|    POS    |REF|     ALT     |FILTER |                                  EXC                                  |   GENE    |AA_POS|AA_REF|   AA_ALT    |
|-----------|---|-------------|-------|-----------------------------------------------------------------------|-----------|------|------|-------------|
|1-55       |.  |.            |mask   |seq_end                                                                |.          |.     |.     |.            |
|76         |T  |W,K,A,Y,C    |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.            |
|78         |T  |W,K,A,Y,C,G  |caution|ambiguous<br>neighbour_linked<br>narrow_src                            |.          |.     |.     |.            |
|150        |T  |Y,C          |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.            |
|153        |T  |Y,G          |mask   |homoplasic<br>single_src<br>neighbour_linked                           |.          |.     |.     |.            |
|285        |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|7     |G     |D,X,V        |
|320        |C  |A,S,Y,T,G    |caution|narrow_src<br>highly_ambiguous                                         |gene-orf1ab|19    |P     |T,X,X,S,A    |
|538        |A  |W,R,G        |caution|ambiguous                                                              |gene-orf1ab|91    |E     |X,E,E        |
|553        |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|96    |Q     |H,Q,X,H      |
|558        |G  |K,T,R        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|98    |G     |X,V,X        |
|635        |C  |Y,T          |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|124   |R     |X,C          |
|660        |G  |A,K,S        |caution|ambiguous                                                              |gene-orf1ab|132   |G     |D,X,X        |
|663        |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|133   |G     |D,X,V,X      |
|759        |A  |D,T          |caution|ambiguous<br>single_src                                                |gene-orf1ab|165   |H     |X,L          |
|856        |T  |Y,A,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|197   |P     |P,P,P        |
|1001       |G  |A,R          |caution|ambiguous<br>amended                                                   |gene-orf1ab|246   |E     |K,X          |
|1406       |G  |A,K,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|381   |E     |K,X,Z,*      |
|1707       |C  |Y,A,T        |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|481   |S     |X,Y,F        |
|1814       |A  |.            |caution|ambiguous<br>amended                                                   |gene-orf1ab|517   |K     |.            |
|1895       |G  |K,T          |mask   |ambiguous                                                              |gene-orf1ab|544   |V     |X,L          |
|1947       |T  |Y,C,G        |caution|ambiguous<br>narrow_src                                                |gene-orf1ab|561   |V     |X,A,G        |
|2087       |T  |Y            |caution|ambiguous                                                              |gene-orf1ab|608   |L     |L            |
|2091       |C  |Y,T          |mask   |highly_ambiguous<br>homoplasic<br>narrow_src                           |gene-orf1ab|609   |T     |X,I          |
|2094       |C  |Y,T          |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|610   |S     |X,L          |
|2101       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|612   |W     |X,C          |
|2198       |G  |A,R,T        |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|645   |G     |S,X,C        |
|2247       |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|661   |G     |D,X,V,X      |
|2381       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|706   |G     |X,C          |
|2604       |G  |K,T          |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-orf1ab|780   |G     |X,V          |
|3050       |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|929   |E     |K,X,*        |
|3073       |T  |Y,W,C        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|936   |C     |C,X,C        |
|3145       |G  |T            |mask   |homoplasic<br>single_src                                               |gene-orf1ab|960   |L     |F            |
|3191       |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|976   |E     |Q,K,X,*      |
|3480       |C  |Y,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1072  |A     |X,V          |
|3504       |A  |W,M,T,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1080  |N     |X,X,I,S      |
|3564       |G  |K,T          |mask   |highly_ambiguous<br>highly_homoplasic<br>single_src                    |gene-orf1ab|1100  |G     |X,V          |
|3639       |G  |A,R          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1125  |G     |D,X          |
|3778       |A  |G            |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1171  |T     |T            |
|3877       |T  |A,K,C,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1204  |A     |A,A,A,A      |
|4050       |A  |C            |mask   |homoplasic<br>single_src<br>amended                                    |gene-orf1ab|1262  |N     |T            |
|4221       |A  |W,D,T        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|1319  |K     |X,X,I        |
|4463       |T  |Y,K,C,G      |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|1400  |S     |X,X,P,A      |
|4505       |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1414  |G     |S,X,C,X      |
|4692       |C  |A,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1476  |S     |Y,F          |
|4854       |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1530  |R     |K,X,I        |
|4991       |A  |M,C,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1576  |N     |X,H,Y        |
|5011       |A  |M,C          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|1582  |Q     |X,H          |
|5130       |C  |A,T,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1622  |P     |H,L,R        |
|5196       |G  |C,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1644  |G     |A,X,V        |
|5233       |G  |A,K,R,D,T    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1656  |W     |*,X,X,X,C    |
|5257       |A  |W,M,G        |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|1664  |L     |X,X,L        |
|5322       |T  |W,K,A,Y,G    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1686  |I     |X,X,K,X,R    |
|5375       |G  |K,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1704  |A     |X,X,S        |
|5393       |T  |Y,C          |caution|ambiguous<br>amended                                                   |gene-orf1ab|1710  |F     |X,L          |
|5498       |A  |R            |caution|ambiguous<br>amended                                                   |gene-orf1ab|1745  |K     |X            |
|5657       |G  |A,K,S,T      |caution|ambiguous<br>single_src                                                |gene-orf1ab|1798  |V     |I,X,X,L      |
|5736       |C  |Y,T          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|1824  |A     |X,V          |
|5743       |G  |S,T          |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1826  |E     |X,D          |
|5744       |T  |Y            |mask   |highly_ambiguous<br>neighbour_linked<br>narrow_src                     |gene-orf1ab|1827  |Y     |X            |
|5765       |G  |K,R          |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X,X          |
|5766       |G  |S            |caution|ambiguous<br>single_src<br>neighbour_linked                            |gene-orf1ab|1834  |G     |X            |
|5847       |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1861  |G     |A,D,X,V      |
|5880       |G  |A,K,C,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|1872  |S     |N,X,T,I      |
|6167       |G  |K,R          |mask   |ambiguous<br>single_src                                                |gene-orf1ab|1968  |V     |X,X          |
|6255       |C  |T            |mask   |highly_homoplasic<br>narrow_src                                        |gene-orf1ab|1997  |A     |V            |
|6309       |G  |A,R,K,C,T    |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |N,X,X,T,I    |
|6310       |C  |A,Y,M,T,G    |caution|neighbour_linked                                                       |gene-orf1ab|2015  |S     |R,S,X,S,R    |
|6312       |C  |A,Y,M,T,G    |caution|neighbour_linked                                                       |gene-orf1ab|2016  |T     |K,X,X,I,R    |
|6483       |G  |K,T,R        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2073  |G     |X,V,X        |
|6804       |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2180  |C     |S,Y,X,F      |
|6866       |A  |W,T          |caution|ambiguous                                                              |gene-orf1ab|2201  |N     |X,Y          |
|6869       |A  |W,T          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|2202  |T     |X,S          |
|6874       |T  |Y,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2203  |V     |V,V,V        |
|6877       |G  |K,T          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2204  |K     |X,N          |
|6971       |T  |Y,W,C        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2236  |L     |L,J,L        |
|6975       |G  |R,T          |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2237  |S     |X,I          |
|6977       |G  |A,K,R        |caution|neighbour_linked<br>single_src                                         |gene-orf1ab|2238  |V     |I,X,X        |
|7017       |G  |A,K,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2251  |G     |D,X,X,V      |
|7038       |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2258  |G     |D,X,V,X      |
|7090       |T  |K,G          |caution|ambiguous<br>single_src                                                |gene-orf1ab|2275  |N     |X,K          |
|7118       |T  |A,K,Y,C,G    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2285  |S     |T,X,X,P,A    |
|7214       |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2317  |D     |N,X,Y        |
|7246       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2327  |W     |X,C          |
|7305       |T  |Y,A,K        |caution|ambiguous<br>single_src                                                |gene-orf1ab|2347  |M     |X,K,X        |
|7396       |T  |Y,W,C        |caution|ambiguous                                                              |gene-orf1ab|2377  |I     |I,I,I        |
|7805       |G  |A,R          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2514  |E     |K,X          |
|8022       |T  |K,C,G        |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-orf1ab|2586  |V     |X,A,G        |
|8026       |A  |W,T,G        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|2587  |A     |A,A,A        |
|8328       |T  |G            |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2688  |L     |R            |
|8459       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2732  |A     |X,S          |
|8550       |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2762  |G     |X,V          |
|8658       |A  |W,C,T,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2798  |K     |X,T,I,R      |
|8678       |G  |A,R,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2805  |E     |K,X,*        |
|8688       |G  |A,K,T,B      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2808  |G     |E,X,V,X      |
|8696       |G  |A,R,K,T,B    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2811  |A     |T,X,X,S,X    |
|8790       |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|2842  |G     |X,V          |
|8827       |T  |W            |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2854  |I     |I            |
|8828       |G  |A,K          |mask   |ambiguous<br>neighbour_linked                                          |gene-orf1ab|2855  |A     |T,X          |
|8886       |T  |Y,A,C,W      |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2874  |L     |X,*,S,X      |
|8887       |A  |C,R,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|2874  |L     |F,L,L        |
|8943       |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2893  |G     |D,X,V        |
|8999       |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2912  |A     |T,X,S        |
|9039       |C  |Y,M,T        |mask   |ambiguous<br>single_src                                                |gene-orf1ab|2925  |A     |X,X,V        |
|9141       |G  |A,K,R,C,T    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2959  |G     |D,X,X,A,V    |
|9249       |G  |K,C,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|2995  |G     |X,A,V        |
|9276       |G  |K,C,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3004  |W     |X,S,L,*      |
|9471       |G  |A,C,S        |caution|ambiguous<br>single_src                                                |gene-orf1ab|3069  |R     |K,T,X        |
|10046      |G  |A,R,K        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3261  |V     |I,X,X        |
|10122      |G  |K,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3286  |G     |X,X,V        |
|10129      |T  |Y,W,C        |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|3288  |T     |T,T,T        |
|10157      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3298  |V     |I,X,L        |
|10239      |C  |M,A          |mask   |homoplasic<br>single_src                                               |gene-orf1ab|3325  |S     |X,Y          |
|10266      |G  |K,R,T,A      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3334  |G     |X,X,V,D      |
|10554      |T  |A,D          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|3430  |L     |*,X          |
|10716      |A  |W,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|3484  |N     |X,T,S        |
|10764      |A  |C,T,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3500  |Y     |S,F,C        |
|10986      |G  |K,S,D,C,T    |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3574  |R     |X,X,X,T,I    |
|11048      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3595  |V     |X,F          |
|11074      |C  |Y,T          |mask   |highly_homoplasic                                                      |gene-orf1ab|3603  |F     |F,F          |
|11083      |G  |A,K,T        |mask   |highly_homoplasic                                                      |gene-orf1ab|3606  |L     |L,X,F        |
|11392      |G  |K,C,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3709  |W     |X,C,C        |
|11535      |G  |K,T          |mask   |ambiguous<br>highly_homoplasic<br>single_src                           |gene-orf1ab|3757  |G     |X,V          |
|12041      |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3926  |D     |H,N,X,Y      |
|12164      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|3967  |A     |T,X,S        |
|12413      |A  |C,R,T,G      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4050  |N     |H,B,Y,D      |
|12491      |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4076  |D     |H,N,X,Y      |
|12506      |A  |R            |caution|ambiguous<br>single_src                                                |gene-orf1ab|4081  |K     |X            |
|12685      |G  |A,K,T        |caution|narrow_src<br>highly_ambiguous                                         |gene-orf1ab|4140  |Q     |Q,X,H        |
|12698      |A  |W,C,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4145  |S     |X,R,G        |
|12751      |T  |W,A          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4162  |A     |A,A          |
|13117      |A  |M,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4284  |L     |L,L,L        |
|13161      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4299  |C     |Y,X,F        |
|13193      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4310  |V     |I,X,F        |
|13239      |C  |Y,T,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4325  |S     |X,L,W        |
|13402      |T  |K,C,G        |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4379  |Y     |X,Y,*        |
|13408      |T  |K            |mask   |homoplasic<br>narrow_src<br>amended                                    |gene-orf1ab|4381  |C     |X            |
|13476      |C  |Y,T          |mask   |highly_ambiguous<br>narrow_src                                         |gene-orf1ab|4404  |C     |X,V          |
|13512      |A  |C,T,G        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |P,L,R        |
|13513      |G  |A,K,T        |caution|neighbour_linked                                                       |gene-orf1ab|4416  |T     |Q,X,H        |
|13514      |G  |A,C,S,T      |caution|neighbour_linked                                                       |gene-orf1ab|4417  |G     |T,P,X,S      |
|13571      |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4436  |G     |X,F          |
|13599      |T  |Y,C          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4445  |C     |X,A          |
|13650      |T  |K            |caution|ambiguous<br>single_src                                                |gene-orf1ab|4462  |F     |X            |
|13686      |T  |Y,A,C        |caution|neighbour_linked                                                       |gene-orf1ab|4474  |H     |X,K,T        |
|13687      |G  |T            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4474  |H     |I            |
|13693      |A  |W,R,T        |caution|neighbour_linked                                                       |gene-orf1ab|4476  |E     |X,K,N        |
|14197      |G  |A,K,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4644  |T     |L,L,L,L      |
|14222      |T  |B,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4653  |L     |X,E          |
|14223      |A  |C,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4653  |L     |S,*          |
|14225      |C  |A,B,T,M      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|4654  |T     |K,X,*,X      |
|14277      |G  |K,T          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|4671  |R     |X,V          |
|14488      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4741  |R     |E,X,D        |
|14536      |C  |Y,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4757  |R     |D,D          |
|14548      |G  |A,R,D,K      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4761  |K     |R,R,X,X      |
|14553      |A  |C,T,G        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4763  |L     |S,F,C        |
|14851      |T  |A,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4862  |L     |*,Y,*        |
|14852      |T  |Y,C,G        |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|4863  |F     |L,L,V        |
|15075      |G  |A,K,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4937  |K     |N,X,X,I      |
|15103      |C  |T            |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4946  |A     |L            |
|15199      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4978  |T     |L,L,L        |
|15230      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|4989  |G     |I,X,F        |
|15435      |A  |R,G          |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-orf1ab|5057  |E     |X,R          |
|15513      |T  |W,C,A        |caution|single_src<br>ambiguous                                                |gene-orf1ab|5083  |N     |X,T,K        |
|15769      |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5168  |V     |*,X,C,X      |
|15771      |T  |A,K,W,D,Y,H  |caution|ambiguous<br>single_src                                                |gene-orf1ab|5169  |A     |Q,X,X,X,X,X  |
|15922      |T  |Y,C          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|5219  |V     |C,C          |
|16130      |G  |A,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5289  |G     |N,Y          |
|16132      |C  |T            |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5289  |G     |D            |
|16188      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5308  |W     |X,V          |
|16210      |A  |W,R,D        |caution|ambiguous<br>single_src                                                |gene-orf1ab|5315  |A     |L,L,L        |
|16290      |T  |K            |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|5342  |A     |X            |
|16537      |G  |A,K,T,R      |caution|ambiguous<br>single_src                                                |gene-orf1ab|5424  |S     |A,A,A,A      |
|16738      |G  |K,C,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5491  |W     |G,G,G        |
|16787      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5508  |G     |X,F          |
|16887      |C  |Y,T          |mask   |highly_homoplasic                                                      |gene-orf1ab|5541  |Y     |X,I          |
|16988      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5575  |G     |T,X,S        |
|17096      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5611  |G     |X,L          |
|17178      |T  |C,G          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5638  |V     |S,W          |
|17179      |G  |S,T          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5638  |V     |X,F          |
|17182      |G  |A            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|5639  |D     |I            |
|17479      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5738  |K     |X,S          |
|17567      |G  |A,K          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|5768  |C     |I,X          |
|17668      |G  |K,R,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5801  |K     |X,R,X,S      |
|17675      |T  |Y,C          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5804  |I     |X,P          |
|17716      |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5817  |I     |*,X,Y,*      |
|17754      |G  |K,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5830  |W     |X,X,V        |
|17848      |G  |K,T,B        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|5861  |Q     |X,S,X        |
|18297      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6011  |W     |E,X,V        |
|18445      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6060  |R     |E,X,D        |
|18465      |T  |K,G          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6067  |P     |X,R          |
|18505      |G  |R            |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6080  |K     |K            |
|18506      |G  |K,S          |caution|ambiguous<br>neighbour_linked                                          |gene-orf1ab|6081  |G     |X,X          |
|18690      |T  |K,C          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6142  |F     |X,S          |
|18716      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6151  |C     |X,F          |
|19250      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6329  |R     |K,X,*        |
|19286      |G  |C,A,R,T      |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6341  |G     |L,M,X,L      |
|19298      |A  |W,R,D,T      |mask   |highly_ambiguous<br>single_src                                         |gene-orf1ab|6345  |Y     |X,X,X,L      |
|19299      |T  |Y,G          |mask   |homoplasic<br>ambiguous<br>narrow_src                                  |gene-orf1ab|6345  |Y     |X,R          |
|19338      |A  |M,R,G        |caution|highly_ambiguous<br>narrow_src                                         |gene-orf1ab|6358  |K     |X,X,R        |
|19339      |A  |M,R,W        |caution|ambiguous<br>single_src                                                |gene-orf1ab|6358  |K     |X,K,X        |
|19344      |T  |Y,K,C,A      |caution|ambiguous<br>amended                                                   |gene-orf1ab|6360  |A     |X,X,P,H      |
|19369      |T  |Y,G          |caution|ambiguous<br>amended                                                   |gene-orf1ab|6368  |P     |H,Q          |
|19406      |G  |K,R,A        |caution|highly_ambiguous<br>single_src                                         |gene-orf1ab|6381  |G     |X,X,K        |
|19482      |T  |W,K          |caution|ambiguous<br>single_src                                                |gene-orf1ab|6406  |G     |X,X          |
|19484      |C  |Y,T          |mask   |highly_ambiguous<br>amended                                            |gene-orf1ab|6407  |A     |L,L          |
|19548      |A  |W,R,D,T,G    |mask   |ambiguous<br>single_src                                                |gene-orf1ab|6428  |S     |X,X,X,L,R    |
|19732      |G  |A,K,T,R      |caution|homoplasic<br>narrow_src                                               |gene-orf1ab|6489  |G     |V,V,V,V      |
|20056      |G  |A,K          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6597  |E     |K,X          |
|20123      |T  |Y,C          |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-orf1ab|6620  |I     |L,L          |
|20126      |G  |A,K,S,R      |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-orf1ab|6621  |G     |K,X,Z,X      |
|20128      |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6621  |G     |D,E,X,D      |
|20254      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6663  |I     |X,F          |
|20465      |A  |W,R,G        |mask   |highly_homoplasic<br>single_src                                        |gene-orf1ab|6734  |D     |X,X,V        |
|20857      |G  |C,A,K,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|6864  |R     |D,E,X,D      |
|21149      |G  |A            |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6962  |G     |K            |
|21151      |G  |D,T          |mask   |single_src<br>highly_homoplasic                                        |gene-orf1ab|6962  |G     |X,D          |
|21209      |T  |C,H          |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|6982  |M     |R,X          |
|21212      |G  |A            |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-orf1ab|6983  |G     |N            |
|21281      |G  |A,K,C,T      |caution|single_src<br>highly_ambiguous                                         |gene-orf1ab|7006  |G     |N,X,H,Y      |
|21302      |C  |A,S,T,M      |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |N,X,Y,X      |
|21304      |C  |A,S,Y,M,T    |caution|neighbour_linked                                                       |gene-orf1ab|7013  |P     |Q,X,H,X,H    |
|21305      |G  |A,R,T,K      |caution|neighbour_linked                                                       |gene-orf1ab|7014  |R     |T,X,S,X      |
|21379      |T  |Y,C          |caution|ambiguous<br>single_src                                                |gene-orf1ab|7038  |S     |L,L          |
|21550      |A  |M,C          |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7095  |N     |T,T          |
|21551      |A  |W,R,T        |mask   |ambiguous<br>homoplasic<br>narrow_src                                  |gene-orf1ab|7096  |N     |X,X,S        |
|21575      |C  |Y,T          |mask   |highly_homoplasic                                                      |gene-S     |5     |L     |X,F          |
|21609      |T  |W,K          |caution|ambiguous<br>single_src                                                |gene-S     |16    |V     |X,X          |
|21658      |C  |G,Y,M,T,H    |caution|ambiguous                                                              |gene-S     |32    |F     |L,F,X,F,X    |
|21968      |T  |C,G          |mask   |single_src<br>highly_homoplasic                                        |gene-S     |136   |C     |R,G          |
|21987      |G  |T,K,C,A      |mask   |amplicon_drop_or_primer_artefact<br>back_to_ref                        |gene-S     |142   |G     |V,X,A,D      |
|22329      |C  |Y,M,T,V      |caution|ambiguous<br>single_src                                                |gene-S     |256   |S     |X,X,L,X      |
|22335      |G  |A,K,T        |mask   |highly_ambiguous<br>amended                                            |gene-S     |258   |W     |*,X,L        |
|22389      |T  |Y,W,C,K      |caution|ambiguous<br>single_src                                                |gene-S     |276   |L     |X,X,P,X      |
|22393      |A  |W,R,G        |caution|ambiguous<br>amended                                                   |gene-S     |277   |L     |X,L,L        |
|22410      |G  |A,K,R,D,C,T  |caution|narrow_src<br>highly_ambiguous                                         |gene-S     |283   |G     |E,X,X,X,A,V  |
|22416      |T  |Y,C          |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |285   |I     |X,T          |
|22420      |A  |W,T          |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-S     |286   |T     |T,T          |
|22488      |A  |W,R,M,C,T    |caution|ambiguous<br>amended                                                   |gene-S     |309   |E     |X,X,X,A,V    |
|22500      |A  |W,R,M        |caution|ambiguous<br>single_src                                                |gene-S     |313   |Y     |X,X,X        |
|22506      |C  |Y,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |315   |T     |X,X,I        |
|22515      |T  |Y,W,K        |caution|ambiguous<br>narrow_src                                                |gene-S     |318   |F     |X,X,X        |
|22516      |T  |W,K,D,Y,C    |mask   |highly_ambiguous<br>single_src                                         |gene-S     |318   |F     |X,X,X,F,F    |
|22521      |T  |Y,K          |mask   |highly_ambiguous                                                       |gene-S     |320   |V     |X,X          |
|22651      |T  |A,C          |mask   |single_src<br>highly_homoplasic                                        |gene-S     |363   |A     |A,A          |
|22661      |G  |A,S,T        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-S     |367   |V     |I,X,F        |
|22797      |C  |Y,M,A,T      |caution|single_src<br>highly_ambiguous<br>homoplasic                           |gene-S     |412   |P     |X,X,Q,L      |
|22802      |C  |Y,M,A,T      |mask   |homoplasic<br>single_src<br>amended<br>interspecific_contamination     |gene-S     |414   |Q     |X,X,K,*      |
|22892      |A  |C,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |444   |K     |Q,*          |
|22904      |A  |W,R,G,V,M,T,H|caution|single_src<br>highly_ambiguous                                         |gene-S     |448   |N     |X,B,D,X,X,Y,X|
|23016      |G  |A,K,C,T      |caution|single_src<br>highly_ambiguous                                         |gene-S     |485   |G     |D,X,A,V      |
|23116      |A  |W,T          |caution|ambiguous<br>single_src                                                |gene-S     |518   |L     |L,L          |
|23122      |A  |W,R,H,V,M,T,G|caution|single_src<br>highly_ambiguous                                         |gene-S     |520   |A     |A,A,A,A,A,A,A|
|23144      |A  |G            |caution|ambiguous<br>amended                                                   |gene-S     |528   |K     |E            |
|23162      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |534   |V     |I,X,F        |
|23288      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |576   |V     |I,X,F        |
|23291      |C  |Y,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |577   |R     |X,C          |
|23292      |G  |K,R,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |577   |R     |X,X,L        |
|23302      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |580   |Q     |Q,X,H        |
|23343      |G  |A,K,T,R      |caution|single_src<br>highly_ambiguous                                         |gene-S     |594   |G     |D,X,V,X      |
|23519      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |653   |A     |X,S          |
|23652      |T  |Y,A,C        |caution|single_src<br>highly_ambiguous                                         |gene-S     |697   |M     |X,K,T        |
|23738      |A  |W,T,G        |caution|single_src<br>highly_ambiguous                                         |gene-S     |726   |I     |X,F,V        |
|23745      |C  |Y,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |728   |P     |X,L          |
|23763      |C  |Y,S,T,G      |caution|single_src<br>highly_ambiguous                                         |gene-S     |734   |T     |X,X,I,R      |
|23766      |C  |Y,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |735   |S     |X,X,L        |
|23775      |G  |K,S,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |738   |C     |X,X,F        |
|23855      |C  |Y,A,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |765   |R     |X,S,C        |
|24389      |A  |W,C,M        |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |X,R,X        |
|24390      |G  |C,K,S,T      |mask   |highly_homoplasic<br>highly_ambiguous<br>narrow_src<br>nanopore_adapter|gene-S     |943   |S     |T,X,X,I      |
|24410      |G  |C,A          |mask   |amplicon_drop_or_primer_artefact<br>back_to_ref                        |gene-S     |950   |D     |H,N          |
|24497      |G  |K,C,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |979   |D     |X,H,Y        |
|24557      |G  |A,K,T        |caution|single_src<br>highly_ambiguous                                         |gene-S     |999   |G     |S,X,C        |
|24622      |T  |Y            |mask   |highly_ambiguous<br>single_src                                         |gene-S     |1020  |A     |A            |
|24673      |A  |G            |caution|ambiguous<br>amended                                                   |gene-S     |1037  |S     |S            |
|24728      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-S     |1056  |A     |X,S          |
|24933      |G  |K,T          |mask   |highly_ambiguous<br>highly_homoplasic<br>narrow_src                    |gene-S     |1124  |G     |X,V          |
|24942      |A  |W,R,T        |caution|ambiguous<br>single_src                                                |gene-S     |1127  |D     |X,X,V        |
|25202      |T  |K            |mask   |highly_ambiguous                                                       |gene-S     |1214  |W     |X            |
|25381      |A  |M,C,R        |mask   |homoplasic<br>single_src                                               |gene-S     |1273  |T     |T,T,T        |
|25382      |T  |C            |mask   |single_src<br>highly_homoplasic                                        |gene-S     |1274  |T     |Q            |
|25446      |T  |W,C,G,A      |caution|single_src<br>highly_ambiguous                                         |gene-ORF3a |18    |G     |G,G,G,G      |
|25798      |A  |G            |caution|ambiguous<br>amended                                                   |gene-ORF3a |136   |K     |E            |
|25902      |T  |W,C,G,A      |caution|single_src<br>highly_ambiguous<br>neighbour_linked                     |gene-ORF3a |170   |T     |T,T,T,T      |
|25908      |T  |W,C,A        |caution|single_src<br>highly_ambiguous<br>neighbour_linked                     |gene-ORF3a |172   |G     |G,G,G        |
|25961      |C  |Y,A,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-ORF3a |190   |T     |X,N,X,I      |
|26549      |C  |Y,T          |mask   |homoplasic<br>single_src                                               |gene-M     |9     |T     |T,T          |
|26700      |G  |K,T          |caution|ambiguous<br>single_src<br>homoplasic                                  |gene-M     |60    |V     |X,L          |
|26709      |G  |A,R,T,K      |caution|ambiguous<br>amended                                                   |gene-M     |63    |A     |T,X,S,X      |
|27033      |G  |A,K,S,T      |caution|single_src<br>highly_ambiguous                                         |gene-M     |171   |A     |T,X,X,S      |
|27534      |T  |Y,W,C,G      |caution|ambiguous<br>single_src                                                |gene-ORF7a |47    |H     |H,X,H,Q      |
|27658      |A  |W,D,T,G      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-ORF7a |89    |R     |X,X,*,G      |
|27660      |A  |V,C,T,G      |mask   |single_src<br>highly_homoplasic<br>neighbour_linked                    |gene-ORF7a |89    |R     |X,S,S,R      |
|27720      |T  |W,K,C        |caution|ambiguous<br>single_src                                                |gene-ORF7a |109   |F     |X,X,F        |
|27760      |T  |Y,A,K        |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.            |
|27761      |T  |C            |mask   |homoplasic<br>neighbour_linked                                         |.          |.     |.     |.            |
|27784      |A  |W,T,G        |mask   |ambiguous<br>single_src                                                |.          |.     |.     |.            |
|27792      |T  |W,K          |caution|ambiguous<br>amended                                                   |.          |.     |.     |.            |
|28004      |T  |Y,C          |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |37    |C     |C,C          |
|28005      |C  |Y,T,G        |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |X,S,A        |
|28006      |C  |T            |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |38    |P     |L            |
|28008      |A  |G            |caution|neighbour_linked<br>single_src                                         |gene-ORF8  |39    |I     |V            |
|28184      |T  |C,H          |mask   |single_src<br>highly_homoplasic                                        |gene-ORF8  |97    |S     |S,X          |
|28253      |C  |A,S,Y,T,G    |mask   |highly_homoplasic                                                      |gene-ORF8  |120   |F     |L,X,F,F,L    |
|28517      |G  |K,S,T        |caution|ambiguous<br>single_src                                                |gene-N     |82    |D     |X,X,Y        |
|28559      |G  |K,T          |caution|single_src<br>highly_ambiguous                                         |gene-N     |96    |G     |X,C          |
|28676      |A  |M,C,R,G      |caution|ambiguous<br>single_src                                                |gene-N     |135   |T     |X,P,X,A      |
|28780      |A  |W,R,D        |caution|ambiguous<br>single_src                                                |gene-N     |169   |K     |X,K,X        |
|28881      |G  |A,R,K,M,T    |caution|neighbour_linked                                                       |gene-N     |203   |R     |K,X,X,X,M    |
|28882      |G  |A,R,S,K,C,T  |caution|neighbour_linked                                                       |gene-N     |203   |R     |R,R,X,X,S,S  |
|28883      |G  |A,C,S,R      |caution|neighbour_linked                                                       |gene-N     |204   |G     |R,R,X,X      |
|28886      |A  |W,M,C,T,G    |caution|single_src<br>highly_ambiguous                                         |gene-N     |205   |T     |X,X,P,S,A    |
|28985      |G  |A,K,R,D,T    |mask   |highly_ambiguous<br>homoplasic<br>single_src                           |gene-N     |238   |G     |S,X,X,X,C    |
|29037      |C  |Y,M,T        |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |255   |S     |X,X,F        |
|29039      |A  |W,T          |mask   |homoplasic<br>ambiguous<br>single_src                                  |gene-N     |256   |K     |X,*          |
|29049      |G  |A,R,T        |caution|single_src<br>highly_ambiguous                                         |gene-N     |259   |R     |Q,X,L        |
|29058      |G  |A,K,T        |mask   |single_src<br>highly_homoplasic                                        |gene-N     |262   |R     |H,X,L        |
|29378      |A  |W            |caution|ambiguous<br>amended                                                   |gene-N     |369   |K     |X            |
|29425      |G  |A,S,T        |mask   |ambiguous<br>homoplasic<br>single_src                                  |gene-N     |384   |Q     |Q,X,H        |
|29427      |G  |A,K,R,S,C,T  |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |K,X,X,X,T,I  |
|29428      |A  |R,C,G        |caution|ambiguous<br>neighbour_linked<br>single_src                            |gene-N     |385   |R     |R,S,R        |
|29553      |G  |A,T          |mask   |highly_homoplasic<br>single_src                                        |.          |.     |.     |.            |
|29594      |A  |C,T          |mask   |single_src<br>highly_homoplasic                                        |gene-ORF10 |13    |I     |L,L          |
|29737      |G  |A,K,S,R,C,T  |caution|ambiguous<br>single_src                                                |.          |.     |.     |.            |
|29783      |G  |C,A,K,T      |mask   |highly_homoplasic                                                      |.          |.     |.     |.            |
|29786      |G  |K,S,C        |caution|homoplasic<br>single_src                                               |.          |.     |.     |.            |
|29827      |A  |T,G          |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.            |
|29830      |G  |A,C,T        |mask   |seq_end<br>highly_homoplasic<br>single_src                             |.          |.     |.     |.            |
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
