import numpy as np

#SAMM
#MASA
#SAMX
#MASA

puzzle_input="""SAMMSMSXMMXXXXSSSMXMAXAMSSSSMSAXMXSSXXXSMMSMMXMASXSSSSSMSMMXMAXMSMMMASMSXSAMMXMMMSMXXSMMXSMXSXXXXMMMMXMASMMMSAMXXSSMMSMAMXMSSMXSSMMSAMSAMXMM
MASAAAMAMMAMSMMAAXMSSXMSAMAAXXMAMAMXMSMMMXSASXSMSMMAAAXMAMSAMXSMAASMXXASMSASMMSAMASXXMAMAMMAMXMMMMAASAMXAXASXSXSASAAAAXAXXMAAASXSXAMAXAMSASX
SAMXSMSMMMAMMAMSMMXAMAXMAMMMMSSSMXSAAAAAMAMXMAAAMAMMMMMXSAMXASAXSXMMAMXMASAMAXSASASXXSAMSSMASAMAASMMSASMMMSMAAXXMSXMXSMMXXMASMMAMMMSMMMXSMAM
MASAXAAASXMXXAMMAMXAMMXSAMASMXAAAASMMSSMMASAMSMMSSMAXXMXMAXXMAMMMSSXMSMSMMAMMMSAMXXMXMXMXAXAXASMXXMMSXMAAMAMMMMSXSMSAMAMMAXAXAXXMAXAXAAMXXMA
SXMASMSMSAASMSMSAMSXAXASASAMAMSMMMMAAMXXSASAMMMXXMMXMAXXSSMMSMXSAAXSXAAAXSXMXAMSMAMAAAMASXMSSMMMSMSAMASMXSASAAAMAMAMASAASXMSSSSXSXSSSXSAXMXS
SXMAMAXAMMMMAAMMAMMSSMAMXMAXMMAAASMMMSAXMASXMMXSXSAAMSAMXAAAMXMMMXSMXMMMMXAXMASXMSASMSAMAAAAMMXAAAMASAMMASXSMMMMAMMMXMMMXAAMAAMAXXAMAMMXSAMX
MAXSXXMAMXAMSMMSSMMAMMXMSSMMXSSMMMAXAMXMSXMAMSAMAMSXSAXSSSMMSAMASMMXMSASXMASMXSXMAMXAXXXMMMMMAMMXSXMMXSMXMASXMASMSSMSASXSXMMMMMMMXMMAMMAMMMM
SSMMAMSAMXMAXMMAXAMSSXMSAAASXMMASMSMMMMMXAMAMMAMAMMMMMXXAAMAXASASAXMASAMXMASXMMASMXMAMXMMSSSMXSMAXMAMXMMXSXMMSMSAAXASXMASXAAXAAAMXXSXSMMMAMA
XMAMAMSASXXSXAMXMXMASXMMMSMMASXXMAAAAAAXMXMAMSSMXSXAASXMSMMSSMMMSMXAMMSMAMASAMSAMXAMXMAMSAAAMAAMAMSAMAMMMSAMAMXMMMMXMAMXMSXMMSSSSMXMMMAXSASM
XSMMAXSAMXAXSMMSXMASXXXAAMASAMAXMMMSXSSSMMSAXAMXAMMSMXMAAXSXAASAMXMSMAAMXMASAMXXSSXMAXXSMMXMMSSMSMSASXSAAXAMASAMSXXMSMSAMXMXMAMXXMASASAMMASA
XMXXXXMSMMXMAMAMAMXXMMSMSMAMXSMSAMXXAAAXAAXMASXMXSAASMSSMSMSSMMMSMAAMSSSSMMMXSAMXMASASMXMSASMXAXMASXMASMMXAMASXSAAMXAMMXAMXSAXXMASAXXMASXMMM
XXASMXMAXAMASMMSAMAMMAXMAMAMXAXAAXAMMMMMMAXMXXASASXSSXAAXAAAMAAAMMSSXXXXXAXAAXAMXMXMAMMAXMAXASAMMASAAXMASXSMMMMMMSMSASXSXMASXMASXMASXSAMXMSX
SMMSAAMMMMAMXAMXMMSSMMMMXXMSMMAXAMXXXAXXMXMSMSAMAXMXMAMMMMMSSSMMSAAXXMXSXXMMMXSMAMSSSSSMMMMMMAMXMAXAMXXMAMXAAXMAAAASAMAMXMASAAXMAAMAAMASAAAX
XAXSXMMXAASMMMMMMAXXAXSSMSAAAXAXMXSXSXXSAMXAAMAMXMXAMXASXSAXMAMXMMMSXSAAASXXXAAMXSAAXMAXSASAXAXSMSSMMXMMMASMMXSAXMMMXMAMXMASXMAMSMMMSMMSMSSS
MSXSAMXSXMXXAAAAMMSMSMAAAMXSMSMSMAMAMASAXAMSSSXMAMMASMMAAMMSSSMXSSMSAMMXMAAAMSMMXMMSMSAMXASMSXSAAXAMMXSAMMAAAMMAXSAMXSXMASAXMASXMASXMAXXAAAX
AMASAMXMSMXSMMXXXAAAAMMMXMAMXMAAAAMAMMMMXSAMXMASAMAMXAAMXMAAMAXMAAAMXMXSSMMMMXAMMMAAAXXXMXMAXMXMMMMXMASMXXXMXXMAMSAMMSASAMXAMAAASXMASAMXMMXM
XMAMMMAAAMMSMSSSMSSXMXXXXMXSAMSMSMSXSASMXMASXSXMASXXSXMASXMSSXMASMMMXSXAAXXAXXAMAMAMAMMMMMMMMMAXAAXAMXXAASMSMMMMMXAMASMMASMXMASMMMMMMMAXSSSS
XSAMXSMXMSAMXAAAMAXAXSAMXXAMAMMAAAXAXASAASMMMMASASXAAXXMXMAMAXXMXMXSAXMMMMSXMMAMXMASAXMAAAAMXSAXMXSMSXMXMXAAASAMSSMMMSXMAMXAMMMXMAMMASMMMAAS
AMASXAAMSXMXMMSMMASXMMAMXMMSAMSSMSMXMXMXMMXAAMMMASMSMMMSAMAMSMSAMXAMMSSSSMXAMMSMMXMSASASMSMSAMASXMAAAMSMMMSMSMASAAAXXXXMASXXMAMMSSXSASAAMMMM
ASAMXMXMAASXSXMXMAXAASMMAXMXAXAMXXAXSAMXSXSSMSAMAMXMAAAMXMAXAAAASMASXAAAAMMXMAXXSAMMAMMAAAAMASAAASMMMMAAXAMXAMMMMMMMSXMAXSAMSASAAXAMASMMMSXS
MMXXSXMXMMMMXAXXMASXMMMSSSSSSSMASMSMSAMAXXXAMXMMAMMSSMSSMSSSMSMAXAAMMMMSMMSXMASASASXAXXMMMMSMMMSMMSSSSSSMSSSSSXASXSAXXAMXMAMSASXMMSMMMXMXAAA
MASMMASMXMAMSAMMMXXMAAASAAAAAXXAXXMASAMSSMMMAAMSXSXAAAMAMAAAAXXSSMXSASXMXXAXSASMSAMMMSMXMXXXAAAXXXAXXAAXAMXAMXMXSAMASMSXMMAMSXMAXMXXMMASXMMM
MAMASAMAASAMMAMXAMMSSMMMMMMMMMMSSMMMMXMMAAAXMAXMAAMSSMSAMMMMXMXAMMMSASASMMMAMASXMMMAMAMASAMSMMMSMMMMMMMMASMMMMSXMXMAMXXAMSAXXAXXMMMSAMXSAAMX
MSXXMMXSMMASXMMMXXXAAAMXSXMASXMXAXXSXMSXSSMSSMMSMMXMAASXSAASXMMSAAAMAMXMASXMSAMXMAXAXASXSAXAMSXAXAAXAAXMAXAXAAMXSAMASXSAMSMMSSMXMAASXMASXMMS
MMASXSAXXMAMXMASMXSMSSMAMASXXAXSXMMAMAAAMAMMAAAAXMXSMMMMMXXSAXAMMMSMXMMSMMMXMAXXXXSXSASASMMMMMSSSSSMMXSMAMSMMMSASASASAMMMSAAAMXAMMXXAMAXAMAS
MXAMAMASMMASMSASAMSAAXMAMMMMSMMSAAAMAMMMMAMSSMMXMSAMXMXXAMMSAMSSMXAMMSAAAAXASMMMSMAXMAMAMXSXXAAXXMAMSMSMSAMMMMMAMAMXSXXXASMMSASXSSMSSMSSMMAS
MMMSXMMMASXSAMAMXAMMMSSMMMAMMMASXMMXXXAXSMMXAAAASMMMAMXMMSAMAXAAMSMXAMSSSMMXMAAXAASAMXMMMMMMMMSSMXXMAAXAMAMAASMSMSMMXMMMXSAMMAXXAXAAXXXAAMXM
AAXSASXSAMMMMMAMMMAAAXMMASXSXMAMAXXSSMMMXAXSSMMXSAMSASASAMXSXMXSMXMASMMMAMXSSSMMSSMMMASAAXAAAXXAAASMMSMXMMMSXSAMXAASXAASAMXXMMMMXMMMSMSSMMMS
SSSXAMASXAAAXMSMXXSMSSXSAMAXMMMSSMAXMASASXMMMSSSMMMSASAMMSMMMXXMXMMMXAMSSMMXAAMAXAXXSASXSSMSSSMMMMXAAAXXXXAXAMMMMSSMSXMMAXMAMAAAAXAAAAAMASAA
MMMMSMXMMSSSMAXXSMXAAAMMMSSMMSMAMMXMAXMASAAAAASAAMXXMMMMXAAAXXXXAMXASAMAMAMMXMMSSMMMMASAXAXXMXAAMXSSMMXSAMXSMMXAAMAMXMSXSMASXSSXMSSMMMMSASMM
XAAMAAXXMAXAMXMAXAMMMSMMAAAMXAMASXSMMSMAMXSMMXXMMMSASXXSSSSMSMSSSMMMSXMXSAMMASXMMAMXAMMMMSMSAXSMSXXAASASMMASXMMMXSASXXAAXMMMAAAXXAMXXAAMAXAX
SSSXSSXMMMSXMSMMSSMMAXAMMSSMSMSMSAMSAAMAXAXMSMSSMXSAMSAAMAMAMAMXXMAXMXMASAXMAAAXSAMMXSASMMAMMMMSMXSSMMAMAXASAXXSAAXXXMMSMAAMXMSMMASXSMSSSSMM
MAMXMMXMXXXAMXAAAAAMXSXMMXMAAXMXMMXMSSXSSMMASAAXMAMAMMMMMSMAMMXMAMSAMXMMSAMMSMMMSASAXMMMAMSMAASASAMXMMSMMMASXMXMASMMASAMXSMSAMXAMAMMSAMXMAXM
MAMASAMMASXMMXMMSSMMXMAXXAMXMSMXMMAXMMAAXXMAMMMXMAMAMXMXSAMAXXSMMAMAMAXAMAMAAAXXSAMXMXASAMXSSMSAMMMSAAXAXAXMAMSSSMAXAMASXMXMASMMMMSMMXMAXMMM
SASXSAMSASAMXXXAXAMMSMMSSMSAAAMAASMSAMSMMXMAXASASMSMSAMSAMSSSMXAMAXAMMSSSMMMSSMAMXMSMSMSSSMAMAMXMAXXMMSSMSASXMAMAMSMMSAMXMASXMMXAMAMXMXSSMSS
SASXXAMSSSMMXAMMXMMMAAMAAAXMMMSSXSAMXMAXAMXXSASAMAAASAMXMXAAAAMXMAMMMAAAAAXAAAMXMAXAAAAMMMMAMXMXMXMMXMAAAXAMMMMSAMAAMMAMSMMXAAAXSXXSASXAAAAX
MAMMMSMMAXXAASXSAXASXSMSSMXMSXXMAXMMSSMXSAAXMMMXMSMMMAMXXMAXMMASMMAMXMMXXXMMSSMMXMSMSMXMASMMXMMAMASXMMSSMMMMAAXSAMMSMSMMSAMXSMMMMAASASMMMMMS
XSMSAMAMMMMMMMAXAXMSMAAAMXASAMMSSMMSXAAAXMMMSMAMXXMMSAMXMXSSSXXSAMSAMXMSXSAAAXAXAXAAAAMSASMSAAMXSAMMXAAAXAXMMSXXSMAXAMXAXAMAXAXAMMMMXXAXSAMX
MMAMMSMMXAXMXMXMXSXXMMMMXSMSASAAAAXSMMMMXXSAXMAXAXXAAXSASAAAXSMMAMAAXXAAASMMMSASMSMSMSMMASASXSMAMMSAMMSSMSXSAMXAXMXMASMXSMMXSMMMXMMMMMSMXASA
XXAMXXMASXSMAMASAAAMSMXXASASAMMSSMMMXSAXXMMSSSSMMMMMSXSASMMMMMXXAMSMMMMMXMXSXMAAMAXXMXAMXMMMSMMMSXAMMAMXAAXMXMMXMAXMAXMAMXMXXMASAXAAAAAASAMX
XSXSXMAMAAMMASASMMSMAAXMASAMXMMXAXXAAXXSSMAMMAXAAAAXAAMAMXSXMXMXSMMAXAMXMSAMXSMMSXMAXXAMXSXMMXAMXMMXSAMMSMSAMXSMAXXMXSXMMAMXXMAXMMSSSSXMAAMX
MMMMAMSAMXSAXSASXXMMSSMMASXMASXSASMMMSMMAMMSMAMMSMSSMSMAMXAAMMSAXASMMXXAXMASAXAXXAXASMSMAMAAAMSSMSXASMMAAAXXAMMAMXXAAMAMSAMXSMXMSAMXMAXMASMA
XAASMMMSXAMMMMXMASMXMMAXASAAXAAMAMMAAAXSXMXAMMSMAMMMAAXMMMXAMAMMMMMMXMSASXXMASAMSMMMXAAMMMMMMSXAASMMSMMSSMMXAAMAMSSMMSAMASXXMASAMMMAMAMMAMXM
MXMXMAMXMSAXAMXXAMAMXMMSASXMAMMMSMXMXSXMMMSMSAAXAMMMSMMSAMSMMSSMASAMAXAXMMMSAXMAAXAMMSMMSASAXAMMMMAXXAAAAAMASMMAXXAAASASAXMMSMMMMMSSSSSXAMAM
SSSXSASXAMMSMSMMSSMSXSAMXSMMXXMAXMMXSMXXSAMXMXSXMMSAMAASMXAXXAAXMXAXSSMXXXMMSSXXMMMSAXAAMAXASMAXMMAMSMMSSMSMMMXXMXSMMSXMMSXAAMAXSAMMAMXMMXAM
XAAASAXMXMAAAAAXMAXAAMSMAMAMXSMMMXAMXXAXMASXXAXASASAMMMMXXSSMSSMSMAMMAMASXSAAMMSMSXMXSMMMSSMMXMMSSMAXAAXMAAAASMXSAAXXXASAMMSSSXSMASMXMAMXSAS
MMMMMMMSAMSMSXSMSXMMXMXMXSSMMMMMAXMMMMSMSAMXSMMAMAMXMMSSSMAXXAXAXMSMXAMXXAMMXSAAXAAMAXAXXAAAXASMAAMSMMMSMSSSMSAAMMMXSMMMASAAMMMMXMMMASXXAAAX
AXAXAAAXAMXAMAAAXXSXMMXSAMAAMAMMXSAAXAAMXAXAXXMSMSMAXXAAAMMMXMMMMMMSSXMMMXMAMAXMSSXMAMMAMXSMMMAMSSMXXASXMAXXAMMMMXMXSAXSAMMXSAAXASASASAMSXSM
SMMXSSSSSMMAMMMSMMSASXAMASXMAMSAAXMMMSMMSMMMSAMXAASMMMMSMMXSMXAAAAAXXMASXMMASMSXXMAMSXXAMXMXXXSMMMASAMXXMXMMXMSXXXAASXMMXXSASXXXAMAMXSMAXAAA
MSMMXAMXAXMASXAAAXSAMMSSMMXSAAMMSMMXAXXMAAAXXMAMXMMMXSAAAXMXMMSSSMSSMSMMAMSASXMXSSMMAMSXMAXMAMXAXMAMAMSMMSMSAAXXSAMXSMSXMXMASAXMSMSAMXXAMSMS
SAMXMAMMXXXMMMSSXMMAMAAAXAXMAXXAAASMMSSSSSMXMSSXMXXAAMSSSMMAMXAMMAMXAAASMMMXSAAAMXMXAXSASMSMASMMMMMSSMAAAAASMMMAMXMAMASAMXMMMXAAAAXXMAMXXAXX
SXMMXMMMSMSXXAXMXSMMMMMAMXSXMMMMSMMAAAMMMAMXAAMMSMMMXMAMXASAMMAMMMXMSMXMAAXASMMXXAMSSXXAMXAXXSAXXXXAXSMSMMMMAXMASAAAMXMAMXMSAMMSMSMSMMSMSMSM
XSXMMSAMAAMAMSXSASASXSMSMMXAMSXAXASMMSSXSAMSMMSAAMAMXMSXSXMASXMMMSAMXMSMSSMMSXSMSXXAMXMSMSXSMSMMMSMMXXXAAXXSXMXMAXSASMSMMXXMASXAXMAMXAAXXXMA
AAMMMSASMMMMMAAMAXAMAXMAXSSMMAMASMMMAMMAMXMXAXMMSXMASAMASMSXXAAXAXMXAXMAAMAXMASMASMSSXMXAMSAMXAMAAASAMXSMMXMASXSMXXAMXAAXMXSAMXMMASMMMSXSASM
SMASASMMASAXMMSMSMXMMMMMMMAXSXXAMAAMAXXASMMMSMMAMAMAMMSAMAMMSMMMSSSSMSMMMSSMMAMMAMXAMAMMAMMMSSMMMXMMASAAMXAMXMAMXSMMMASXMSMMMSMSAAAXASAMSAMX
AXSMAMSAXXAMMMAAAMSMXMAXAMMMMSMSSSMSXSSMSASAMAMSMSMXMAMXMXMAMXAAXXAAAMASAMXMMSSMASMMSAMSMSXAAAXMMSMSAMMSMSMSMMAMXXAAAMMMAAXMXSAAMSMMMMAXMMMX
SXMMXMAMSSMSXSMSMSAMSXSMXSAAAAXMAXASXMAXSMMASXMXAXASMASMXSMMXMXXSMSMMXXSASXSAMAMASAXSAXAAXMMSSMSMAAMXSXMASAAMSMSSMSMXMAMSMMSAMXMXAASMSXMASMM
AAXXMXAXAAXSXMAMXXAMSAMAXXMMMMMMAMSMMSMMXXMAMMASAMAMXMMMAAAASMMXSAMXSXAMXMAXXSSMASXMSMXMSMXAXXAAMMXMXMMMMMXMXAMAMAAMMSSMAMMMASMXSMXMAAXSMMXA
SXMAASMMMMMMAMSMSXSAMAMXASXMSSSMSXMAAAAMAMMMSMAMAMAXMSAMXMMMAASAMXMASMSMSMMMXMAMASAAXXXSXMMSSMSMSAAMAMXSASXSSMMAMMMXXAMSMSASMMXAMXAMMMMMAMMS
XMAXMMAAAMSSMMMAMXMAMXMXMSAAAAXAXAMXXXMMAXAAAMXSXMSXXMASAXAXXXMASXMXSAAAAAASAMAMASXMMMMSAMXMMAXMMMXXASAMXSAMAXSASXSXMAXAXSMMAAMXXMXXXMAMAMAX
XAXMASXMMXMASXMAMXSSMAMAXSMMMSMMMXMASMSSSSSSMXAAMMXMAMAMXSSMSMMXMXAAMXMSMSMSASXSXXAAMMAXMMSSXAXAMAMSMMASAMAMAXSXMAASMXMAXMXMMSMSSSMSMSMSXSAM
XSMSASXSXASAMXSAMMAAMASMXSXMSAMXAXSXSAAAAAMXAMSSMXMASMMXASXASMSSXSAMXAXXXAASMMMAAXSMMMMMAAXMMMSXMAXAMSSMXSXMXXMMMMMMXMAXMASXXXAXAAAAAMMAXMAS
MMASASAXSMMMSASASAMMSAXMASMMSAMXSXMMMMMMMMMMSMAAMXMAXAAMSMMMMAAAMMMMSSSXSMXMXAMXMMXXSASAMXMXAXAASXXMXSAMXSMMMXMAXAAMXMAXMXMSAMXMSMMMSSMMMSAM
AMAMAMMMSMAMMASAMMXXMXMMMSMXMAMAMASAMSMSAMXAXMMMMAMXMMMXAASMMMMSXSAXAMMMSXAMMMSXAXXAMASMSSXMAMSMMXXSXMASASMMSAMSSSSSXSASAMXMMMMXASXXAAAAAMAS
SMAMAAXSXMAXMXMAMXMAMAXXXMASAAMXSAMXMAXMXXMXSXXXSASMSXXXSMMXAAAAXMXMAMSAMXXMASXMASMMMAMAAAMXSXMXSXMMASXMASAAMAMXAAXXAMXSMAAXAAXSASXSASMMXSAM
XSXMSSXMAMMXMXXAMAXAMXSMASASXSXXMMSMSMSMXMSMSMXMAXSAAMMMMAMSAMMSSSSMSMMASXMSMSAMAXASMXSMMSMAXASAAMMSXMASXMMMSSMSMMMMSMAMMSMSMSMMAMAMAMMXXMAS
MXMMMMMMMMSAMSSMSXSAXAAMXMXMAMMMSAAAAAAXMAXAXAASMAMAMAMAMXXAMXXMXAAAMMXMMMXAXSAMXSSMMAAMMXMXSSMXMSAAAMAMAAAXAMAMAMXMASASMAMXAXXMAMXMAMXMASAM
AMXAAMAAXASASAAXXAAAMSMMXMXMXMAXMSSSMXMSMSXAXSMSMAXMAMSASMXAASXMMMMMMAASASXMMSAMXMMXXSXAMASMMXAMXMAMSMAXSMMMMMAMAMMMAXMXMAAMMMMMSSMMASAMXXSS
SASMXMSXXASXMXMMMMMXMAASAMASMMMSMXMMXMAAAAMMMMAXMMMMAMSAMMMXMAAXXMAAMSMXASXMAXAMAAMSMMAMSASAAMXAMXMAXMMMXAXAASASMSXMSSMMSMSAMASXAAXSXMASAAAS
MMMAMXASMAMMXAMMSAMXMXXXASAXAAXAAAXAAMXMSMSXAXAXSMASXMMAMXASMSMMMSSMMAAMSMMMSMMSSSMSMAMMMASMMSMSSSMAMASAMXSSXSASAMXXAAMAMXMMSASMSMMMMXAMMMMM
SAMAMMASMAMXSASAMASMMSSSMMMSSMSSSMSSXSXXXASMSMSMASASAMSMMXSXMASAXMMMSMSMAAMAXAAXAMAMMMXXXXMXXXAAAXMASMMMSAMXXMMMAMXMSSMSXAMAMMSAAAMASMMMXMXS
MXXMXMAMXMAASXMAXSAMXAAMAXMAMXAXXAXXAMMMMMXAXAAMAMMSMMAMXXMAMXSMMMAMXXMASXMASMMMXMAMMSSMSSMXSMMMSMSMSAAXMMSSXMSSSMXMAMXMMXMASAMXSAMASAMXXSAM
SMASAMASXMMMXAMAMMMXMMSMMMMSSMXSMMMMSMAXXXASMSMSMSMSASMSMMSAMMSAMSXSSSSMXAMAMXXAMXSSXAAXAAAAMAXXMAAASMMMAAXXAMXAMAMMAMAXAMSASAMXMXMASXMMAMAS
AMASASASXSASXSMXSMMSSXXAXAXXXXMAMMAAXSXSXMAXAAXAAAASXMXMAMSASAMAMASXXAAASMMSSMMXSAASMSSMSSMMSAMXMXMMMAMSMMSMSMMAMSXSASXSSXMASMMAXXXAMASAMSAM
MMAXXMXXMSAXAXMASAAXASAMSMSMXSAMSXMMXMSMMMAMMMSMMMMMXMASXMSAMXSMMMMMASMMMAAXAXAAMMSMMXXAXAAAXASXSSSXSMMAAXSMMASMSMAMAXXAMXSAMASMXXMAMSXSXMAM
XMXSSMXMAMAMSMMAMMMSMMSXAAAAASXXMMSMXMAMAMMSMMMMSXAXAXMASXMAMAMXXMAMXMAXSXMSSMSSSXAAMXMSMMMSSSMAMAAMXMSSSMMAXAMXAMXMAMMSMMMASAAAASMSMXAMXSAM
XSAXAAAASMMMXAMSMMXXMAXXMSMMMXSXSAAAASASXXAAAXAAMXXSASMAXMMAMMXAXSAMASXMXXAMXAXAMMSMMAMAAXAAXAMAMMMMXXMAMXMAMSSSMSAMXMAAAAMMMMSMMSAAAMSMXSXS
SMMXXMMMXAAASXMXASAMMXXMAAXXMAMMMSMMAXXMAMSSMMMSSMMMMXMXSAXXXSMSXSASASASAMSSMXMAMMMAXAXSSMMSSMSSSXSMXXMAMAMSSMAAMSAMSMSSSMSXXXXAXMMMMMMAXMMS
XASMSSSXSSMXXMASAMAMSMMSXMMAMAMSAMXSMSSMSMAAXAAAAXSASAXXXMAMSAMXASXMASAMXSMAMXSAXASMXSXMXAAMAAAAMAAMSXSXMMXMAMSMMSAMXAAAAMAMXSXMXSAMAAXMMMAM
SAAAMAMXMAMXMMXMMSAMAAMAASXMMSMMXSAAXAAMAAXSMMMSSMSASMSMAXMXASXMMMAMMMXMXMXAMXAMMMSAAXXMSMMSMMMSMSAMXMMAMXSXSMMXASAMMMMSMMASMSMSASASMSMMAXXS
MMMMMAMMMSMSAMXAASASASAMXMAAAXAMXMASMSSMMXMAXXAAAAMXMASAAMXSAMXAXMAMAAAXAASMMSASAXMMMMAMXMAAXXAXMXXSAMMASASAAAXMXSSMXXXAMSAMAMAAMSXMXMASAXMA
AASASXSAAXAXMSSMMSAMAMXAAMXMAXAAXXAAAAAAXMSSSSSXSXMASXMMXSAXXXXAMXMSASMSMMSAASAMMMXMASMMMMSSSMMMSXMSASXSMASXMMMMXMMMXXSMXMXSAMSMAXAMXAMSASXM
SXXASASMSMMMXAAAXMXMAMXSASAMSSMMMMASMSSMMAXAAAAXXASXSASAMXMMSMMXSAMXXAMXMAMMMMXMASMMAXMAMXAAXXSAMXXMAMXAMXMMSAAXAAAAMMAXSAASAMXMSMSSSSXSMMAX
MAMMMMXXAAXXMAMMMMXMASAMMAXXXAMAMMXMXMAXSMMMMMMMSAMXSAMXSMAAXMAAMAMMMMMAMASASXXXXSAASMSSSMMSMMMSSMXMAMXMXMAXSASMSSMXAXMSMMMSXMXAAXXAAMXSASXM
MASXASASMSSSMSSSXMASMAXAAAXXSASMSMAXMXMMSAMXAXXASMMXMSMAMMMMSMSSSSMSAASXSASASMMSMMXMAAXAAMAAMAXAMAAMASAXMAXXXAMAXAMMXMXXXXAXMSMSMSMMMMASMMXX
SAMXXMASAAAXAAXXASASAMXMMXXASAMAAMXMMMSASAMMMSMMXAMXAAMAMAAMAAXAMXAMSXSASMMMMMAAAXSMMMMSMMXSXSXMASMSASXSASMMMMMXSMMSAAXAMMMSAAXAAXXXAMXMAMXX
MMSSMMMMMMMMMMSSXMASMXXMASMAMAMSMMAXXXMASXMAASASMSMMSMSAMSMSMMMXSMMMMXMAMXAASMSSSMXMASXMAMAXXMAXXAAMXSMMXXAAAAXXMAAXAXXMXAAMXSSMSMSMSSSMMMXM
MMAAMXSMXAXMAAXMAMAMXMXMAMMXMAMXAMSXSAMAMAMMXSAMXXXXAMMMXMAAXXSMMASAXMMSMSMMMAAAXAMSXSXSAMASAMXMAMXMMXAMMSSSSSSMSSMSSXMASMXSAXMXXAAAXAAMXSAA
MMSSMASASMMXMMMMSXAXAMAMXXXASMSMXMAASXMASXMSAMAMXMMSMSXMAMMMSAMASAMXMXXAMASXMMMSMSAMXMAXXMASAMAMXXMSSMSAAXAAMAAAAAAAAMAMAAAMMMSAMMMSMSXMASXS
AAAAMAMXMASXSXMAXMMSSSXMAMSAMMAMMMMMMSXMAXSMMMXMASAMXMAMXSXXXAXAMASMSSMMMAXXSSXXAAMSAMMSMMASAXAMMMAAAAMMMMMMMXMMMMMMSASXMAMSXAMAXXXXXXXMXSAM
MMSSMSSXSAAXMAMXXAXAAXAXAMMAMXAXAMXMMAMAMXXAASAMMMXSASAMAAXMSMMXSXMAMAASMMSMMSAMXMASASAAAMMSASXXMMSSMMMASXMASXSSXXSXMXXMMAAXMXSAMSMSMSXSXMAM
MXMAMAAAMMSXSAMMSMMXSSSMSMSAASMSMSASXMSMAXSXMXAXAXAXXSMSSSSMAAAMXXMAMMAMAMAMAMXMAXXSXMMSSMAMMMXAAAAAASXMMAMAMMAMXMAMXXSASMSMSAMMMSAAXAAXMSMM
MAMMSMMMSMMXSASMASMAMAMAAAMAMAAAASAMXXAXSXMMSSSMSMASASAAMMAXMSXSXMSASXSSSMXMASAXMAMMMXXXXMXSXAXMMMSSMMAASXMASMSMSMSAXAMAMXXAMXSAAMMMSMMMAAAA
SASAXXXAAAMXMAMMAAMMSAMSMMMSMMMMXMAMMSXMMAAMMAMAAASAAMMMMSAMXAASAMSASXMAXAXSASMSASAAMMMAMXMMMMSSXAAAMSXMMASMMMAAXAXSMMMSSMMSMMSMXSXMAAAXSMSM
SAMASMMSSSMSMSMMXSAAMXMXXSAXMXSXSSMMASMMSSMMMAMSXSMMMMXAXMXMMMSMAMMAMXAMMSMMASAMAMMASXMSMSMAMMAAMMXSMMASMXMXXSMXMXMXMXAAAAAAAXXMASMSSSMXXAAX
XAMXMXAAAXAAAAMSMMMXXMASAMXXSASXMASMXSAMAMMAXAMMMMAAMMMSSMSSSMMXAMMAMMXSAXAMAMAMMMSAMAMAAASASMMSMSMXAXAAXMMMXMAMSAMMSMMSSMMSAMSAMXAXMXMAMMMM
XAMXXMSMMMSMSMSMAAXSMSXMXMXAMMSASAMXASMMASXMSSSMASXMMAAXAAMXXAAMMMSASAAAAMSMSSXMXAMASAMMSMSXSAMXAXAMSMSMXAAAMXMASASAAXMAXMXXXAXMSMSMAAMASAMA
ASXSAAAXAAXMAXAMMMSAAMMSASAMXAMMMASMMSASAMXAAMAMMSASMMMSMMMSSMMSMASAMMSMXMXAMAXMMXSASXSXMAMXSXMMSMSMXAAXSXXSMAMMMMMXSSMMSSSMXSASAMXASXSASASM
MXAMMMMSSSSSMSAMXMMMAMASASMXMSAAMXSAXSXMMSMMSSMMMSAMAAAXAAAAAAAAAXMAMAMXXXMAMSMSAAMASMAMMASMSAMXXAMXSSXMMSMMXAXAAASXMAMXXAMAAMSSMSSXMMMMSAMX
XMAMASXMMAAAASXMAXXXAMMMXMAXAMSXSASAMMAMMXAXAAMAMXXXMMMXSMMXSMSXSMSSMMSSMSSSMAAXMXSXXAAASXSASMMAMAMXMASMAAXASMSSSSMXSXMMMMMMMSASXAMAMASXMMMS
XSAMXXAAMXMMMMASMSSXSSXXASMMXXAXMXXSASXMAMSMSSMXMAAASXSAAASXXAXXXMXXAXXAAAAASMSMSASMMSAMXXMMMMSASAMSMMXMSMSMMXAAXMXAMASXMAAAMXASMMMSMASMXAAM
XSXXXXSMMXXSSXXMXAAAMAMSASXSXMMMSMXXXXASMSXAXAXAMMAMAAMXSMXAMAMAXMSMMMSMMMSMMMAAMASAAAAXMXMXMASAMMSMAMXMAMSAMMMSMMMASXMMSMSXSMAMAXAMMAMAMMSS
MMMSSMXAMMSMMXSXMSMXMAMMMMXSAAXAAAAMAXXMSAMXMASMXAXXMXMMMMMSMAMMMMAAAAAAAXMASMMXMAMMMSSMMASAMMMMMMAMMMASAXXAMXAAAXSMMMMAAAXASMMSXMXSMMMSXAAX
XAAAAAXAMXAAMAMAMXXAMXMXAXAMMMMSSSSMSSMMSXXMAAMMASXMXAXAAXAXXXAAAAXSMSXSMSAMXXSMMXSXAXMXSAMAMAAMSSSSMSXSMSMSMSSMSMMAMAXSMSSMXAASAMASASAXMMMS
SMMSSMSSMSSSMAMSMMMXMXSXMMXXAXXAMMAXXAAXMASMMSSXXMMAXSSSSMMSSSSSSSMXAXAMAMXXAAMAMSXMASXXMMSSSMSMXAXAASMMASAXAMMSAAAAMAXMXMAASMMXAMASXMMXAAAM
MAXMMAXAAAAMMASAAAMAMAMMSAAXSXMAXSSMSSMMSMAXAXMMXMASAMAAXASAAMAMAMMMMMXSAMMMMMSAMXAMMMXMXXAMXAAMMSMMMMAMAMXMAMXMMMMMSSSMASXMMSASXMASAXSMSMSS
SXMAMMSMMMXSSMSXXMMAMXSAMXSAAMSMMXAAAXMXAMMMMSASMMAMAMXMSMMSMMAMAMAAXSMSAMSXAASASMSMASAMXMMSMSMMAMMMSSXMXXMSSMMSXSAMAMAXASASAXXAAMXMMMSAMXMX
AMSXMAXXSMMMAASAMSSMSAMASAMMMMAMMSMMMAXMMXXAXXXSAMAMAMXAXAAXMSASXSSSXMASAMMMSMSXMAXSXSASAAMSAMXMAXAAXMMMSAMAAAXAASXMASMMMSAMSSSXMASXXAMMMSMM
MAMXMMSMXMAXMMMASAAXMASXMASMXSXXXAMAMXSXAMSSXSAXXMSSSXSMSMXSASXSXXAAMMMMMXXAMAMXMAMXXMXSMSMMAMXMASMMSXAAXAMSSMMMMMASASXSMMXMMXMASAMXMXSAAMAM
XSMXXAAXSMSSXXXXMMXXMASASMMMXXAMSAMXMAMMSMMAAMMMMXXAMAMMAAXMMMAMASMXSSSSSMMSSMMAMAXMXSAXAXMMSMXMAAAAAMMSXMMXXMMMMSAMASASXMMXXSXMMSAMXASMXMAM
AAAXASMMSAMMMSMMXXAMSMSAMAASXMMMSMMSMMXAAAMMMMSAAMMAMAMMMSXMXMAMAMXXAAAXXXAAAAMSSMSAAMAMAMAAXMAMSSMMSXAXASMMMSXAAMASAMXMAXSAMXASAMXMMAMASXMM
AMMMMXXAMMMAAAASXSSMAAMXMMXMXMMAMAAXAAMMSSMSMAMMSXXMSASXXMMSASXSSSXMMMMMMMMSSMMAAAXXMMXMXMMMXSXXMAAMAMXMXMASAAXMSSXMASASXMMAXMMMASMMSSMXMAXS
SMMAXMMASXSMSSSMAAASMMMMXSASMSMASMMSSMXXAXAXMASXMMMASAMXXMAXXSAAXMAMXAMAXXAXMAMMSMMXXSXMXXAAXSMSSXMASAXMASMMMSMSAMAAAXAXMASAMSMSMMAAAXMASAMX
XASMSAMAXMXMAXAMMMMAXAXAMSASAXSAMMXMMSXAXMMMMAMAAXSAMXSSMMSSMMMMMSSMSMSMSMMSSXMAAXAXXMASMSMSMMAMMASXMAXSAMXXMAXMASXMSMSMSAMXXAAAXXMMSMSASAMA
SAMAAAMMMSAMMSXMXXXSXMMSAMXMMMMMXSASXSXMAMXAMAXMMMMXXXXAAXAAAXMAMXAAXMAMXASXMAMSSSSXXSXXAMAMAMMMMXMAMAMMAMXSMSMXAMXAMXMXMASMSMSMSXXAAXMXSAMS
XMMXSXMAASAMMAMXSMMMAMAXMMXXSASXMSASAMMXSMASMSSMMXMAMSXSMMSSSMXMASMMMSMSSXXAXXMMAMXMMSXMXMAXASMSSSMAMAMMMMAXMASMXSMMMAXMSMMAAAAASMMMSSMMSMAM
MXSAMAMMMSAMXXASAMAXAMAMASMASASAMMMMXMAAXMAMAAAXSSMMXSAAAAMXMXASAMXAMAMXXMMSMMSXMAMSAXXAMMSSMMASAMSASASAMMMMSAMXMMAMSSMMAAMSMMXSXSAAAAAAMXSX
XXMAMXMXAXMSMMSAMXSXXMMSAMMAMXSAMSXAMXMXSMAXMXMMAMAXAMSMMXSAMMMMXMSMXSSMAAAAAAXAXSXMASMSAXAAAMMMAMXXMAXAXAAAMASXASMMAMAXSSMXAMSMMMXMSXMMSAMX
MASMMMMMMSMAAMXMXMMXSAMMMMMMMAXAMSMMSASXAMMSXSAAXSAMXXMMMMMMMAAAAMXMAXAXMSSSMMSSMXAMMSAMMMSSMMXMXMSSMSMSSMSMSMMAMAAMMSSMAMMMAMAAXAAMMMSSMASX
AXASXAXAMXXMSMMXXAAAMAMAAAASMSSSMXAXSASXXAAXMAXSXSMAMSAMAAAXXSMSMSAXMSAMMXXAMAMXASAMSMXMXAMAXXXMAMXAAAAXMAXMAXSMSMMMMAXMMMXSXSSSMSXSAAXXMSMX
SSXASMSMMMXMMMMMSMMSSSMSSSMSAAAASXXMMAMMSMXSAMXXASXSXMAXSSSSMXAMASASMMXMSSXMMSSMMMSMAAAXMASXMXAXAXXMMMSMSAMXAMXASXXSMSMSAMXSMAAXAMAMMMSMXMAA
XAXMAMAAASAMMAAAXAMAXMAXAXAMMMSMXMXAMAMAXXMAMXSMAMAMMSSMAMAAAMMMAMMMMASMAAASAXXXMAAXMSMMXXAAASASXXXXMAMASXMMASMAMSMMAAAMASASMMMMSMAMASAAAMSM
MAMXASXXMMASXSMSSSMMAMXMSMXMXXMXAMXMXMSSMMXSAXAAAMSMAAXMAMSMMMSMSMXSXAXMMSMMASMSMSSSXMXXSMSSMMAXAASASAMMMAMSAMMAMXXMMMSMAMASXAXXMXXMXMMXMMAX
MAMMMSASXXXMMAAMAAXMXMAMAMMSMMMSMSASAMXMASAMXMMSXXXMMSSSSMXAMXMAMMMMMSXMAXAMAMAMMAMXAAXXXAAAXMXMMMMAMSSXMAMMASXXSXSXMAMMMMMMMMSMMMSMMMSAMXMX
SSMMAMXMAASXSMSMMMXSMMSSMXAAAAAAXMASMSASXMAMXAXXXASAMXMMMAXMASMAMAMXAMMMMSAMAMXXMMSSMMMMMMMSAAAAXAMXMAXAMAMMXSMAXASXXAXMASAAAXAAAAAAMAMASXXM
MAXMAMXMMMMAMXXAXXMXSAMXXMSSSMSSSMAMASAMXMAMXSAXAXMAMMMASXMMAXMAMAMMXSASXSMSMSMASMAAAAXAMXMAXXMSSXSAMAXXSAXXAMMSMAMXMMMSASMXXSMSMSSMMASMMMAS
MAMSSMAXMAMXMASMMXAXMXMAXXAAAAXAMXAMXMSMAMXSXMMMMASXMASAMAAXXSSMSSSMMSASAMXMAAMMMMXSSMSMMASAMXXAAMSXSMSAMXMMASAMMMMXASXMMSXSAAXAAXXMSASASXXA
MXXAAMMMXAMAMMSAMSMSMAMSMMMSMMMAMASXSAMXMMSAMXAXXXMAMXMMSSMMMMAAAXAAAMAMXMXMSMMAXXAMAMXMSXXAAMMMXMMMAMMASAMSAMMXMAMMSAAXSXAASMMMMMMMSASMSASM
SXMXMASXSMSASASAMAMAMAXAASXXXMSMMMMAMAMAXMSASXSSSMSAMXMAAMAXASMMMSSMMMAXXMSAXMSMSMMSAMAXAMMSMMXXAMAXAXSXMAAMXXMAXMMMXSMMAMSMXXXXMAAXMAMASAMS
MASASAAAAASXMAXAXASASMSSSMMXMAMSMXMAMSXXMASAMAMAMASAMAMMSSMMXXAAAXMASXSMMXSAXAAASAAXXSXSXMAXASAMSSMSSMSAMXMSMASMSMMAMAMAMAXXMXMASXSSMMMMMAMX
MMMASMMMMMMXXMMXSASXMMMXAAXAMAAASXXAMXASMMMMMMMAMMXMMSSMXAASASXMMSMMMAAAXAMXMXMXMSMSMXASMMAMAMASAAMAXAMXMAXXMAMMAXMASAMAXXMXAXXAXMAMAAXXMAMX
SXMAXASAXXXSMSAXAAXASXSSSMSXSMSASMSSSMAMAMXXAXMXMSMSAAAMMSAMXMAMSAAAMXMSMXSAMASXMMXAAAMSAMMSXSMMXMMMSSXXMXMXMAMSMMMAMAXMSMAXSMMASXSSSMSSSMSX
AXMASAMMMMMMAAMMMMMMMMAAAAXAXAMAMAAAXXAMAMAMMMAAAAAMMSMMAMSMXAAXSSSMSAXAAASMSASAMXSMSSXSMXMAXXMAMSAXAAMXMAMSMXMAASMSSSMASAMMAMSAAXXAXXXXAMXM
SXSAMMXAAAAMXMSMMAAXAMMMMAMMMXMSMMMXMMSXSMSAAMSSMMMMAXAMXXAXSSMXXAXASXSMSMSXMAXAMMAAAXXMXXSMMMMAXMAMXSAAXAXMAMSMMMAAAXMXMAXSAMMMMSMAMMMMSAMX
XAMXMASMXXXXAXAASXXSXSXAXAMXAAMXMAXMAXMAMAXMMXAAMSSMASAMSMSAAAXMMMMASXMAXXMXXMXSMAMMMSSXSASAAMMSSSSMAAXXMMMMAMMMSMMMSMSAMXMMASXSAXMXMXAAAASX
MXMXAXXMASMMMXMXMXXMAMXSSMSXSASXSAMASXMAMAMASMMMAAAMAMXMSAMXSMAMMAMASAMAMAMSMSAMASXMXXMASMSSMSMAAAXMXSMMMSASAXSASAMXMAMXMAXSXMAMAXSAMSSXMAMX
SAMXMXMMXAAASMSSSXSMAMAMAMXMXAXXMAMAMAMXMSMAMASXMSSMMXSAMXMMMMXASASXSMMXSAMXAMAMAXAMXAMXMAMXMAMMMMMMAAAMAMASXMMASAMXMSMSSMXMMSAMXMMAXAAMMSXM
MXXAMMXMXMSMSAAAAAAMAMMSSMAMMMMSSMMSSMMSMAMMSAMMMAMASASXMAMAAXMMSASMMMAASASMSMSMXSAMSSMASXMASAMMASAMSSSMASMMMSMMMMSMMMAMAMMSASASMMSMMMSXMMAM
SSSXSAASMXMXMMMSMMMSXSAAASASXAAAAAAAAMAASASMMAXAMASAMASASASMMSAXMXMAAMMMSAMXXAMAAMAMAASXSAAAMSMSASXXXAXXXMASAAAXMASAXSASAMAMMSXMXAAAAXMAASMM
XMASAMMSAXMASAMXMXXAAMMSMSSSXMSSSMMSSMSXSXSXSMMXSASMMXMMSMSXMAMXMASMMSSXMAMXMMMMMSAMSMMXSMMMSXXMASMXMXMASMMMSSSMMMSSMSAMXMXSMMMXMSSSMSSSMAMM"""

#140 characters per line
#141 lines
#19739

# Split the string into rows (giant list seperated by commas for each row)
import numpy as np

# Split the string into rows
rows = puzzle_input.split('\n')

# Make each row a list
char_lists = [list(row) for row in rows]

# Convert to a 2D NumPy array
array = np.array(char_lists)

def is_it_horizontal(array,row,col):
    horizontal_elements = ''.join(array[row,col:col+4])
    if horizontal_elements == 'XMAS' or horizontal_elements[::-1] == 'XMAS':
        return True
    return False

def is_it_vertical(array,row,col):
    vertical_elements = ''.join(array[row:row+4, col])
    if vertical_elements == 'XMAS' or vertical_elements[::-1] == 'XMAS':
        return True
    return False

def is_it_diagonal_TLBR(array, row, col):
    # Ensure we don't exceed array bounds
    if row + 4 > array.shape[0] or col + 4 > array.shape[1]:
        return False
    diagonal_elements = ''.join([array[row+i, col+i] for i in range(4)])
    return diagonal_elements == 'XMAS' or diagonal_elements[::-1] == 'XMAS'
    
def is_it_diagonal_TRBL(array, row, col):
    # Ensure we don't exceed array bounds
    if row + 4 > array.shape[0] or col - 3 < 0:
        return False
    diagonal_elements = ''.join([array[row+i, col-i] for i in range(4)])
    return diagonal_elements == 'XMAS' or diagonal_elements[::-1] == 'XMAS'

# Create a set to track unique finds
unique_finds = set()


for row in range(array.shape[0]):
    for col in range(array.shape[1]):
        # Check all directions from every starting point
        if is_it_horizontal(array, row, col):
            unique_finds.add(f'H{row},{col}')
        if is_it_vertical(array, row, col):
            unique_finds.add(f'V{row},{col}')
        if is_it_diagonal_TRBL(array, row, col):
            unique_finds.add(f'TRBL{row},{col}')
        if is_it_diagonal_TLBR(array, row, col):
            unique_finds.add(f'TLBR{row},{col}')

count=len(unique_finds)
print("Count:", count)

#2547
