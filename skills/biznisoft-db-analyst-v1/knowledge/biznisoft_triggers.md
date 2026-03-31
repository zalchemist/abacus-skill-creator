# Biznisoft ERP - Trigeri

**Baza:** `opp7102025`
**Ukupno trigera:** 265
**Datum izvlačenja:** 2026-03-29

---

## Pregled trigera

| # | Triger | Tabela | Timing | Event |
|---|--------|--------|--------|-------|
| 1 | updartikli | artikli | AFTER | UPDATE |
| 2 | operdoc_del_blgpromet | blgpromet | BEFORE | DELETE |
| 3 | operdoc_upd_blgpromet | blgpromet | BEFORE | UPDATE |
| 4 | updfakture | fakture | AFTER | UPDATE |
| 5 | operdoc_del_fakture | fakture | BEFORE | DELETE |
| 6 | operdoc_ins_fakture | fakture | BEFORE | INSERT |
| 7 | operdoc_upd_fakture | fakture | BEFORE | UPDATE |
| 8 | operdoc_del_faktureos | faktureos | BEFORE | DELETE |
| 9 | operdoc_ins_faktureos | faktureos | BEFORE | INSERT |
| 10 | operdoc_upd_faktureos | faktureos | BEFORE | UPDATE |
| 11 | zak_del_finprom | finprom | BEFORE | DELETE |
| 12 | operdoc_del_finprom | finprom | BEFORE | DELETE |
| 13 | zak_ins_finprom | finprom | BEFORE | INSERT |
| 14 | operdoc_ins_finprom | finprom | BEFORE | INSERT |
| 15 | operdoc_upd_finprom | finprom | BEFORE | UPDATE |
| 16 | zak_upd_finprom | finprom | BEFORE | UPDATE |
| 17 | operdoc_del_frmgk_avans | frmgk_avans | BEFORE | DELETE |
| 18 | operdoc_upd_frmgk_avans | frmgk_avans | BEFORE | UPDATE |
| 19 | operdoc_del_frmgk_carina | frmgk_carina | BEFORE | DELETE |
| 20 | operdoc_upd_frmgk_carina | frmgk_carina | BEFORE | UPDATE |
| 21 | operdoc_del_frmgk_ed | frmgk_ed | BEFORE | DELETE |
| 22 | operdoc_upd_frmgk_ed | frmgk_ed | BEFORE | UPDATE |
| 23 | operdoc_del_frmgk_faktura | frmgk_faktura | BEFORE | DELETE |
| 24 | operdoc_upd_frmgk_faktura | frmgk_faktura | BEFORE | UPDATE |
| 25 | operdoc_del_frmgk_nefak | frmgk_nefak | BEFORE | DELETE |
| 26 | operdoc_upd_frmgk_nefak | frmgk_nefak | BEFORE | UPDATE |
| 27 | operdoc_del_frmgk_nefak_spec | frmgk_nefak_spec | BEFORE | DELETE |
| 28 | operdoc_ins_frmgk_nefak_spec | frmgk_nefak_spec | BEFORE | INSERT |
| 29 | operdoc_upd_frmgk_nefak_spec | frmgk_nefak_spec | BEFORE | UPDATE |
| 30 | operdoc_del_frmgk_osnsred | frmgk_osnsred | BEFORE | DELETE |
| 31 | operdoc_upd_frmgk_osnsred | frmgk_osnsred | BEFORE | UPDATE |
| 32 | operdoc_del_frmgk_prijemfakture | frmgk_prijemfakture | BEFORE | DELETE |
| 33 | operdoc_upd_frmgk_prijemfakture | frmgk_prijemfakture | BEFORE | UPDATE |
| 34 | operdoc_del_frmgk_troskovi | frmgk_troskovi | BEFORE | DELETE |
| 35 | operdoc_upd_frmgk_troskovi | frmgk_troskovi | BEFORE | UPDATE |
| 36 | operdoc_del_intprijem | intprijem | BEFORE | DELETE |
| 37 | operdoc_ins_intprijem | intprijem | BEFORE | INSERT |
| 38 | operdoc_upd_intprijem | intprijem | BEFORE | UPDATE |
| 39 | operdoc_del_intracun | intracun | BEFORE | DELETE |
| 40 | operdoc_ins_intracun | intracun | BEFORE | INSERT |
| 41 | operdoc_upd_intracun | intracun | BEFORE | UPDATE |
| 42 | operdoc_del_kalkulacije | kalkulacije | BEFORE | DELETE |
| 43 | operdoc_ins_kalkulacije | kalkulacije | BEFORE | INSERT |
| 44 | operdoc_upd_kalkulacije | kalkulacije | BEFORE | UPDATE |
| 45 | delkasa | kasa | AFTER | DELETE |
| 46 | inskasa | kasa | AFTER | INSERT |
| 47 | updkasa | kasa | AFTER | UPDATE |
| 48 | operdoc_del_komnivelacije | komnivelacije | BEFORE | DELETE |
| 49 | operdoc_ins_komnivelacije | komnivelacije | BEFORE | INSERT |
| 50 | operdoc_upd_komnivelacije | komnivelacije | BEFORE | UPDATE |
| 51 | operdoc_del_nabambalaze | nabambalaze | BEFORE | DELETE |
| 52 | operdoc_ins_nabambalaze | nabambalaze | BEFORE | INSERT |
| 53 | operdoc_upd_nabambalaze | nabambalaze | BEFORE | UPDATE |
| 54 | operdoc_del_nivelacije | nivelacije | BEFORE | DELETE |
| 55 | operdoc_ins_nivelacije | nivelacije | BEFORE | INSERT |
| 56 | operdoc_upd_nivelacije | nivelacije | BEFORE | UPDATE |
| 57 | operdoc_del_nivkalkulacije | nivkalkulacije | BEFORE | DELETE |
| 58 | operdoc_ins_nivkalkulacije | nivkalkulacije | BEFORE | INSERT |
| 59 | operdoc_upd_nivkalkulacije | nivkalkulacije | BEFORE | UPDATE |
| 60 | delosamvr | osamvr | AFTER | DELETE |
| 61 | insosamvr | osamvr | AFTER | INSERT |
| 62 | updosamvr | osamvr | AFTER | UPDATE |
| 63 | delosnabvr | osnabvr | AFTER | DELETE |
| 64 | insosnabvr | osnabvr | AFTER | INSERT |
| 65 | updosnabvr | osnabvr | AFTER | UPDATE |
| 66 | delosotpis | osotpis | AFTER | DELETE |
| 67 | insosotpis | osotpis | AFTER | INSERT |
| 68 | updosotpis | osotpis | AFTER | UPDATE |
| 69 | operdoc_del_pazari | pazari | BEFORE | DELETE |
| 70 | operdoc_ins_pazari | pazari | BEFORE | INSERT |
| 71 | operdoc_upd_pazari | pazari | BEFORE | UPDATE |
| 72 | zak_del_pk1 | pk1 | BEFORE | DELETE |
| 73 | zak_ins_pk1 | pk1 | BEFORE | INSERT |
| 74 | zak_upd_pk1 | pk1 | BEFORE | UPDATE |
| 75 | zak_del_popdv_promet | popdv_promet | BEFORE | DELETE |
| 76 | zak_ins_popdv_promet | popdv_promet | BEFORE | INSERT |
| 77 | zak_upd_popdv_promet | popdv_promet | BEFORE | UPDATE |
| 78 | operdoc_del_popis | popis | BEFORE | DELETE |
| 79 | operdoc_upd_popis | popis | BEFORE | UPDATE |
| 80 | operdoc_del_prodintracun | prodintracun | BEFORE | DELETE |
| 81 | operdoc_ins_prodintracun | prodintracun | BEFORE | INSERT |
| 82 | operdoc_upd_prodintracun | prodintracun | BEFORE | UPDATE |
| 83 | operdoc_del_prodkalkulacije | prodkalkulacije | BEFORE | DELETE |
| 84 | operdoc_ins_prodkalkulacije | prodkalkulacije | BEFORE | INSERT |
| 85 | operdoc_upd_prodkalkulacije | prodkalkulacije | BEFORE | UPDATE |
| 86 | operdoc_del_prodnivelacije | prodnivelacije | BEFORE | DELETE |
| 87 | operdoc_ins_prodnivelacije | prodnivelacije | BEFORE | INSERT |
| 88 | operdoc_upd_prodnivelacije | prodnivelacije | BEFORE | UPDATE |
| 89 | operdoc_del_prodpovracajdob | prodpovracajdob | BEFORE | DELETE |
| 90 | operdoc_ins_prodpovracajdob | prodpovracajdob | BEFORE | INSERT |
| 91 | operdoc_upd_prodpovracajdob | prodpovracajdob | BEFORE | UPDATE |
| 92 | operdoc_del_proveraprijema | proveraprijema | BEFORE | DELETE |
| 93 | operdoc_ins_proveraprijema | proveraprijema | BEFORE | INSERT |
| 94 | operdoc_upd_proveraprijema | proveraprijema | BEFORE | UPDATE |
| 95 | operdoc_del_putninalog | putninalog | BEFORE | DELETE |
| 96 | operdoc_upd_putninalog | putninalog | BEFORE | UPDATE |
| 97 | operdoc_del_radnal | radnal | BEFORE | DELETE |
| 98 | operdoc_upd_radnal | radnal | BEFORE | UPDATE |
| 99 | delstanje | robno | AFTER | DELETE |
| 100 | insstanje | robno | AFTER | INSERT |
| 101 | updstanje | robno | AFTER | UPDATE |
| 102 | zak_del_robno | robno | BEFORE | DELETE |
| 103 | zak_ins_robno | robno | BEFORE | INSERT |
| 104 | zak_upd_robno | robno | BEFORE | UPDATE |
| 105 | operdoc_del_sitinvpov | sitinvpov | BEFORE | DELETE |
| 106 | operdoc_ins_sitinvpov | sitinvpov | BEFORE | INSERT |
| 107 | operdoc_upd_sitinvpov | sitinvpov | BEFORE | UPDATE |
| 108 | operdoc_del_sitinvras | sitinvras | BEFORE | DELETE |
| 109 | operdoc_ins_sitinvras | sitinvras | BEFORE | INSERT |
| 110 | operdoc_upd_sitinvras | sitinvras | BEFORE | UPDATE |
| 111 | operdoc_del_sitinvzad | sitinvzad | BEFORE | DELETE |
| 112 | operdoc_ins_sitinvzad | sitinvzad | BEFORE | INSERT |
| 113 | operdoc_upd_sitinvzad | sitinvzad | BEFORE | UPDATE |
| 114 | operdoc_del_tblambintpr | tblambintpr | BEFORE | DELETE |
| 115 | operdoc_ins_tblambintpr | tblambintpr | BEFORE | INSERT |
| 116 | operdoc_upd_tblambintpr | tblambintpr | BEFORE | UPDATE |
| 117 | operdoc_del_tblamizdkup | tblamizdkup | BEFORE | DELETE |
| 118 | operdoc_ins_tblamizdkup | tblamizdkup | BEFORE | INSERT |
| 119 | operdoc_upd_tblamizdkup | tblamizdkup | BEFORE | UPDATE |
| 120 | operdoc_del_tblampovdob | tblampovdob | BEFORE | DELETE |
| 121 | operdoc_ins_tblampovdob | tblampovdob | BEFORE | INSERT |
| 122 | operdoc_upd_tblampovdob | tblampovdob | BEFORE | UPDATE |
| 123 | operdoc_del_tblampovkup | tblampovkup | BEFORE | DELETE |
| 124 | operdoc_ins_tblampovkup | tblampovkup | BEFORE | INSERT |
| 125 | operdoc_upd_tblampovkup | tblampovkup | BEFORE | UPDATE |
| 126 | operdoc_del_tblamprijdob | tblamprijdob | BEFORE | DELETE |
| 127 | operdoc_ins_tblamprijdob | tblamprijdob | BEFORE | INSERT |
| 128 | operdoc_upd_tblamprijdob | tblamprijdob | BEFORE | UPDATE |
| 129 | operdoc_del_tblfaktakcrab | tblfaktakcrab | BEFORE | DELETE |
| 130 | operdoc_ins_tblfaktakcrab | tblfaktakcrab | BEFORE | INSERT |
| 131 | operdoc_upd_tblfaktakcrab | tblfaktakcrab | BEFORE | UPDATE |
| 132 | operdoc_del_tblfaktbezobr | tblfaktbezobr | BEFORE | DELETE |
| 133 | operdoc_ins_tblfaktbezobr | tblfaktbezobr | BEFORE | INSERT |
| 134 | operdoc_upd_tblfaktbezobr | tblfaktbezobr | BEFORE | UPDATE |
| 135 | operdoc_del_tblintizdavanje | tblintizdavanje | BEFORE | DELETE |
| 136 | operdoc_ins_tblintizdavanje | tblintizdavanje | BEFORE | INSERT |
| 137 | operdoc_upd_tblintizdavanje | tblintizdavanje | BEFORE | UPDATE |
| 138 | operdoc_del_tblisplata | tblisplata | BEFORE | DELETE |
| 139 | operdoc_upd_tblisplata | tblisplata | BEFORE | UPDATE |
| 140 | operdoc_del_tblizdavanje | tblizdavanje | BEFORE | DELETE |
| 141 | operdoc_ins_tblizdavanje | tblizdavanje | BEFORE | INSERT |
| 142 | operdoc_upd_tblizdavanje | tblizdavanje | BEFORE | UPDATE |
| 143 | operdoc_del_tblizvoz | tblizvoz | BEFORE | DELETE |
| 144 | operdoc_ins_tblizvoz | tblizvoz | BEFORE | INSERT |
| 145 | operdoc_upd_tblizvoz | tblizvoz | BEFORE | UPDATE |
| 146 | operdoc_del_tblkomfakture | tblkomfakture | BEFORE | DELETE |
| 147 | operdoc_ins_tblkomfakture | tblkomfakture | BEFORE | INSERT |
| 148 | operdoc_upd_tblkomfakture | tblkomfakture | BEFORE | UPDATE |
| 149 | operdoc_del_tblkomkalk | tblkomkalk | BEFORE | DELETE |
| 150 | operdoc_ins_tblkomkalk | tblkomkalk | BEFORE | INSERT |
| 151 | operdoc_upd_tblkomkalk | tblkomkalk | BEFORE | UPDATE |
| 152 | operdoc_del_tblkomvrac | tblkomvrac | BEFORE | DELETE |
| 153 | operdoc_ins_tblkomvrac | tblkomvrac | BEFORE | INSERT |
| 154 | operdoc_upd_tblkomvrac | tblkomvrac | BEFORE | UPDATE |
| 155 | operdoc_del_tblkooizdavanje | tblkooizdavanje | BEFORE | DELETE |
| 156 | operdoc_ins_tblkooizdavanje | tblkooizdavanje | BEFORE | INSERT |
| 157 | operdoc_upd_tblkooizdavanje | tblkooizdavanje | BEFORE | UPDATE |
| 158 | operdoc_del_tblmatobrdor | tblmatobrdor | BEFORE | DELETE |
| 159 | operdoc_ins_tblmatobrdor | tblmatobrdor | BEFORE | INSERT |
| 160 | operdoc_upd_tblmatobrdor | tblmatobrdor | BEFORE | UPDATE |
| 161 | operdoc_del_tblmatobrdorprij | tblmatobrdorprij | BEFORE | DELETE |
| 162 | operdoc_ins_tblmatobrdorprij | tblmatobrdorprij | BEFORE | INSERT |
| 163 | operdoc_upd_tblmatobrdorprij | tblmatobrdorprij | BEFORE | UPDATE |
| 164 | operdoc_del_tblnabsitinv | tblnabsitinv | BEFORE | DELETE |
| 165 | operdoc_ins_tblnabsitinv | tblnabsitinv | BEFORE | INSERT |
| 166 | operdoc_upd_tblnabsitinv | tblnabsitinv | BEFORE | UPDATE |
| 167 | operdoc_del_tblnardobavljacima | tblnardobavljacima | BEFORE | DELETE |
| 168 | operdoc_ins_tblnardobavljacima | tblnardobavljacima | BEFORE | INSERT |
| 169 | operdoc_upd_tblnardobavljacima | tblnardobavljacima | BEFORE | UPDATE |
| 170 | operdoc_del_tblnarkupaca | tblnarkupaca | BEFORE | DELETE |
| 171 | operdoc_ins_tblnarkupaca | tblnarkupaca | BEFORE | INSERT |
| 172 | operdoc_upd_tblnarkupaca | tblnarkupaca | BEFORE | UPDATE |
| 173 | operdoc_del_tblodobdob | tblodobdob | BEFORE | DELETE |
| 174 | operdoc_ins_tblodobdob | tblodobdob | BEFORE | INSERT |
| 175 | operdoc_upd_tblodobdob | tblodobdob | BEFORE | UPDATE |
| 176 | operdoc_del_tblodobinodob | tblodobinodob | BEFORE | DELETE |
| 177 | operdoc_ins_tblodobinodob | tblodobinodob | BEFORE | INSERT |
| 178 | operdoc_upd_tblodobinodob | tblodobinodob | BEFORE | UPDATE |
| 179 | operdoc_del_tblodobinokup | tblodobinokup | BEFORE | DELETE |
| 180 | operdoc_ins_tblodobinokup | tblodobinokup | BEFORE | INSERT |
| 181 | operdoc_upd_tblodobinokup | tblodobinokup | BEFORE | UPDATE |
| 182 | operdoc_del_tblodobkup | tblodobkup | BEFORE | DELETE |
| 183 | operdoc_ins_tblodobkup | tblodobkup | BEFORE | INSERT |
| 184 | operdoc_upd_tblodobkup | tblodobkup | BEFORE | UPDATE |
| 185 | operdoc_del_tblotkup | tblotkup | BEFORE | DELETE |
| 186 | operdoc_ins_tblotkup | tblotkup | BEFORE | INSERT |
| 187 | operdoc_upd_tblotkup | tblotkup | BEFORE | UPDATE |
| 188 | operdoc_del_tblotkupss | tblotkupss | BEFORE | DELETE |
| 189 | operdoc_ins_tblotkupss | tblotkupss | BEFORE | INSERT |
| 190 | operdoc_upd_tblotkupss | tblotkupss | BEFORE | UPDATE |
| 191 | operdoc_del_tblotpisnz | tblotpisnz | BEFORE | DELETE |
| 192 | operdoc_ins_tblotpisnz | tblotpisnz | BEFORE | INSERT |
| 193 | operdoc_upd_tblotpisnz | tblotpisnz | BEFORE | UPDATE |
| 194 | operdoc_del_tblotpisz | tblotpisz | BEFORE | DELETE |
| 195 | operdoc_ins_tblotpisz | tblotpisz | BEFORE | INSERT |
| 196 | operdoc_upd_tblotpisz | tblotpisz | BEFORE | UPDATE |
| 197 | operdoc_del_tblpoljoprivreda | tblpoljoprivreda | BEFORE | DELETE |
| 198 | operdoc_ins_tblpoljoprivreda | tblpoljoprivreda | BEFORE | INSERT |
| 199 | operdoc_upd_tblpoljoprivreda | tblpoljoprivreda | BEFORE | UPDATE |
| 200 | operdoc_del_tblposotpremnice | tblposotpremnice | BEFORE | DELETE |
| 201 | operdoc_ins_tblposotpremnice | tblposotpremnice | BEFORE | INSERT |
| 202 | operdoc_upd_tblposotpremnice | tblposotpremnice | BEFORE | UPDATE |
| 203 | operdoc_del_tblpovracaj | tblpovracaj | BEFORE | DELETE |
| 204 | operdoc_ins_tblpovracaj | tblpovracaj | BEFORE | INSERT |
| 205 | operdoc_upd_tblpovracaj | tblpovracaj | BEFORE | UPDATE |
| 206 | operdoc_del_tblpovracajdob | tblpovracajdob | BEFORE | DELETE |
| 207 | operdoc_ins_tblpovracajdob | tblpovracajdob | BEFORE | INSERT |
| 208 | operdoc_upd_tblpovracajdob | tblpovracajdob | BEFORE | UPDATE |
| 209 | operdoc_del_tblpovracajdobnovi | tblpovracajdobnovi | BEFORE | DELETE |
| 210 | operdoc_ins_tblpovracajdobnovi | tblpovracajdobnovi | BEFORE | INSERT |
| 211 | operdoc_upd_tblpovracajdobnovi | tblpovracajdobnovi | BEFORE | UPDATE |
| 212 | operdoc_del_tblpovracajinokup | tblpovracajinokup | BEFORE | DELETE |
| 213 | operdoc_ins_tblpovracajinokup | tblpovracajinokup | BEFORE | INSERT |
| 214 | operdoc_upd_tblpovracajinokup | tblpovracajinokup | BEFORE | UPDATE |
| 215 | operdoc_del_tblprodajagp | tblprodajagp | BEFORE | DELETE |
| 216 | operdoc_ins_tblprodajagp | tblprodajagp | BEFORE | INSERT |
| 217 | operdoc_upd_tblprodajagp | tblprodajagp | BEFORE | UPDATE |
| 218 | operdoc_del_tblprodamb | tblprodamb | BEFORE | DELETE |
| 219 | operdoc_ins_tblprodamb | tblprodamb | BEFORE | INSERT |
| 220 | operdoc_upd_tblprodamb | tblprodamb | BEFORE | UPDATE |
| 221 | operdoc_del_tblprodfakture | tblprodfakture | BEFORE | DELETE |
| 222 | operdoc_ins_tblprodfakture | tblprodfakture | BEFORE | INSERT |
| 223 | operdoc_upd_tblprodfakture | tblprodfakture | BEFORE | UPDATE |
| 224 | operdoc_del_tblprodmat | tblprodmat | BEFORE | DELETE |
| 225 | operdoc_ins_tblprodmat | tblprodmat | BEFORE | INSERT |
| 226 | operdoc_upd_tblprodmat | tblprodmat | BEFORE | UPDATE |
| 227 | operdoc_del_tblproizvobrdor | tblproizvobrdor | BEFORE | DELETE |
| 228 | operdoc_ins_tblproizvobrdor | tblproizvobrdor | BEFORE | INSERT |
| 229 | operdoc_upd_tblproizvobrdor | tblproizvobrdor | BEFORE | UPDATE |
| 230 | operdoc_del_tblproizvobrdorprij | tblproizvobrdorprij | BEFORE | DELETE |
| 231 | operdoc_ins_tblproizvobrdorprij | tblproizvobrdorprij | BEFORE | INSERT |
| 232 | operdoc_upd_tblproizvobrdorprij | tblproizvobrdorprij | BEFORE | UPDATE |
| 233 | operdoc_del_tblreversizdavanje | tblreversizdavanje | BEFORE | DELETE |
| 234 | operdoc_ins_tblreversizdavanje | tblreversizdavanje | BEFORE | INSERT |
| 235 | operdoc_upd_tblreversizdavanje | tblreversizdavanje | BEFORE | UPDATE |
| 236 | operdoc_del_tblreversprijem | tblreversprijem | BEFORE | DELETE |
| 237 | operdoc_ins_tblreversprijem | tblreversprijem | BEFORE | INSERT |
| 238 | operdoc_upd_tblreversprijem | tblreversprijem | BEFORE | UPDATE |
| 239 | operdoc_del_tblrobobrdor | tblrobobrdor | BEFORE | DELETE |
| 240 | operdoc_ins_tblrobobrdor | tblrobobrdor | BEFORE | INSERT |
| 241 | operdoc_upd_tblrobobrdor | tblrobobrdor | BEFORE | UPDATE |
| 242 | operdoc_del_tblrobobrdorprij | tblrobobrdorprij | BEFORE | DELETE |
| 243 | operdoc_ins_tblrobobrdorprij | tblrobobrdorprij | BEFORE | INSERT |
| 244 | operdoc_upd_tblrobobrdorprij | tblrobobrdorprij | BEFORE | UPDATE |
| 245 | operdoc_del_tblrobtransf | tblrobtransf | BEFORE | DELETE |
| 246 | operdoc_ins_tblrobtransf | tblrobtransf | BEFORE | INSERT |
| 247 | operdoc_upd_tblrobtransf | tblrobtransf | BEFORE | UPDATE |
| 248 | operdoc_del_tblsitanizd | tblsitanizd | BEFORE | DELETE |
| 249 | operdoc_ins_tblsitanizd | tblsitanizd | BEFORE | INSERT |
| 250 | operdoc_upd_tblsitanizd | tblsitanizd | BEFORE | UPDATE |
| 251 | operdoc_del_tblsopsttros | tblsopsttros | BEFORE | DELETE |
| 252 | operdoc_ins_tblsopsttros | tblsopsttros | BEFORE | INSERT |
| 253 | operdoc_upd_tblsopsttros | tblsopsttros | BEFORE | UPDATE |
| 254 | operdoc_del_tbltrebovanje | tbltrebovanje | BEFORE | DELETE |
| 255 | operdoc_ins_tbltrebovanje | tbltrebovanje | BEFORE | INSERT |
| 256 | operdoc_upd_tbltrebovanje | tbltrebovanje | BEFORE | UPDATE |
| 257 | operdoc_del_tbluvoz | tbluvoz | BEFORE | DELETE |
| 258 | operdoc_ins_tbluvoz | tbluvoz | BEFORE | INSERT |
| 259 | operdoc_upd_tbluvoz | tbluvoz | BEFORE | UPDATE |
| 260 | zak_del_trgovacka | trgovacka | BEFORE | DELETE |
| 261 | zak_ins_trgovacka | trgovacka | BEFORE | INSERT |
| 262 | zak_upd_trgovacka | trgovacka | BEFORE | UPDATE |
| 263 | operdoc_del_tr_finprom | tr_finprom | BEFORE | DELETE |
| 264 | operdoc_ins_tr_finprom | tr_finprom | BEFORE | INSERT |
| 265 | operdoc_upd_tr_finprom | tr_finprom | BEFORE | UPDATE |

---

## 1. delkasa

**Tabela:** `kasa` | **Timing:** AFTER DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `delkasa` AFTER DELETE ON `kasa` FOR EACH ROW begin
  if not (old.status=1) then
    set @w=(select sum(kolicina*kasakoef) from kasa,artikli where kasa.sifra=artikli.sifra and kasa.sifobj=OLD.sifobj and kasa.sifra=OLD.sifra and status=99 and tipracuna=0);
    if isnull(@w) then
      set @w=0;
    end if;   
    insert into trstanje set sifobj=OLD.sifobj, sifra=OLD.sifra,stanje=0,rezervacije=0,refobjst=0,neprokkasa=@w on duplicate key update neprokkasa=@w;       
    if not isnull(@refobjekat) and not (trim(@refobjekat)='') then
```

---

## 2. delosamvr

**Tabela:** `osamvr` | **Timing:** AFTER DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `delosamvr` AFTER DELETE ON `osamvr` FOR EACH ROW BEGIN
  IF old.tipam='K' then
    DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datam and brnal=CONCAT('AMSS-',date_format(OLD.datam, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbramort*100+OLD.rbr),3));
  END IF;
  
end
```

---

## 3. delosnabvr

**Tabela:** `osnabvr` | **Timing:** AFTER DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `delosnabvr` AFTER DELETE ON `osnabvr` FOR EACH ROW BEGIN
  DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datnab and brnal=CONCAT('NBSS-',date_format(OLD.datnab, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbr),3));
  
end
```

---

## 4. delosotpis

**Tabela:** `osotpis` | **Timing:** AFTER DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `delosotpis` AFTER DELETE ON `osotpis` FOR EACH ROW BEGIN
  DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datotp and brnal=CONCAT('OTSS-',date_format(OLD.datotp, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbr),3));
  
end
```

---

## 5. delstanje

**Tabela:** `robno` | **Timing:** AFTER DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `delstanje` AFTER DELETE ON `robno` FOR EACH ROW begin
  if (not (@NEAZURIRAJROBNO=1133)) or (isnull(@NEAZURIRAJROBNO)) then
    set @st=(select sum(ulaz-izlaz) from robno where sifobj=OLD.sifobj and sifra=OLD.sifra and stornirano=0);
  if isnull(@st) then
    set @st=0;
  end if;
  update trstanje set stanje=@st, refobjst=0 where sifobj=OLD.sifobj and sifra=OLD.sifra;
  if not isnull(@refobjekat) and not (trim(@refobjekat)='') then   
    set @mynewferobj=null;
```

---

## 6. inskasa

**Tabela:** `kasa` | **Timing:** AFTER INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `inskasa` AFTER INSERT ON `kasa` FOR EACH ROW begin
  if not (new.status=1) then
   set @w=(select sum(kolicina*kasakoef) from kasa,artikli where kasa.sifra=artikli.sifra and kasa.sifobj=NEW.sifobj and kasa.sifra=NEW.sifra and status=99 and tipracuna=0);
   if isnull(@w) then
     set @w=0;
   end if;
   insert into trstanje set sifobj=NEW.sifobj, sifra=NEW.sifra,stanje=0,rezervacije=0,refobjst=0,neprokkasa=@w on duplicate key update neprokkasa=@w;    
   if not isnull(@refobjekat) and not (trim(@refobjekat)='') then   
     set @mynewferobj=null;
     select refobj into @mynewferobj from objekti where sifra=NEW.sifobj;
     if not isnull(@mynewferobj) and not (trim(@mynewferobj)='') then    
       set @wref=(select if(isnull(stanje),0,stanje)-if(isnull(neprokkasa),0,neprokkasa)-if(isnull(rezervacije),0,rezervacije) from trstanje where sifobj=NEW.sifobj and sifra=NEW.sifra);
       if isnull(@wref) then
         set @wref = 0;
       end if;
       insert into trstanje SET sifobj=@mynewferobj, sifra=NEW.sifra, stanje=0, neprokkasa=0, rezervacije=0, refobjst=@wref*-1 on DUPLICATE KEY UPDATE refobjst=@wref*-1;
       update trstanje set refobjst=@wref where sifobj=NEW.sifobj and sifra=NEW.sifra;
     end if;
   end if;
 end if;
  
end
```

---

## 7. insosamvr

**Tabela:** `osamvr` | **Timing:** AFTER INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `insosamvr` AFTER INSERT ON `osamvr` FOR EACH ROW BEGIN
  IF NEW.tipam='K' then
    INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datam, CONCAT('AMSS-',date_format(datam, '%y%m%d'), '-', RIGHT(CONCAT('000',rbramort*100+rbr),3)), 4, 0, 0, SUM(amvr*komada), 0, 0, opis, NULL,0 FROM osamvr WHERE tipam='K' AND osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datam=NEW.datam and rbr=NEW.rbr AND rbramort=NEW.rbramort  GROUP BY osoznaka, invbroj, datam, rbramort;
  END IF;
  
end
```

---

## 8. insosnabvr

**Tabela:** `osnabvr` | **Timing:** AFTER INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `insosnabvr` AFTER INSERT ON `osnabvr` FOR EACH ROW BEGIN
  INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datnab, CONCAT('NBSS-',date_format(datnab, '%y%m%d'), '-', RIGHT(CONCAT('000',rbr),3)), IF(tipnab='0',0,IF(tipnab='1',1,IF(tipnab='2',2,IF(tipnab='3',3,4)))), IF(tipnab='2',0, komada), IF(tipnab='2',nabvr, nabvr*komada), IF(tipnab='2',amvr, amvr*komada), 0, 0, nazdob, datsadvr, (rzdvr*komada) FROM osnabvr WHERE osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datnab=NEW.datnab and rbr=NEW.rbr;
  
end
```

---

## 9. insosotpis

**Tabela:** `osotpis` | **Timing:** AFTER INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `insosotpis` AFTER INSERT ON `osotpis` FOR EACH ROW BEGIN
  INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datotp, CONCAT('OTSS-',date_format(datotp, '%y%m%d'), '-', RIGHT(CONCAT('000',rbr),3)), 5, (komada * -1), 0, 0, 0, (iznotp * komada), opis, NULL, 0 FROM osotpis WHERE osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datotp=NEW.datotp and rbr=NEW.rbr;
  
end
```

---

## 10. insstanje

**Tabela:** `robno` | **Timing:** AFTER INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `insstanje` AFTER INSERT ON `robno` FOR EACH ROW begin
 if (not (@NEAZURIRAJROBNO=1133)) or (isnull(@NEAZURIRAJROBNO)) then
  insert ignore into trstanje set sifobj=NEW.sifobj,sifra=NEW.sifra,faktcena=NEW.cena,nabcena=NEW.nabcena,vpcena=NEW.cenabezpp,mpcena=NEW.cenasapp,stanje=0,neprokkasa=0,rezervacije=0,refobjst=0;
  set @st=(select sum(ulaz-izlaz) from robno where sifobj=NEW.sifobj and sifra=NEW.sifra and stornirano=0);
  if isnull(@st) then
    set @st=0;
  end if;
  update trstanje set stanje=@st, refobjst=0 where sifobj=NEW.sifobj and sifra=NEW.sifra;
  if not isnull(@refobjekat) and not (trim(@refobjekat)='') then   
    set @mynewferobj=null;
    select refobj into @mynewferobj from objekti where sifra=NEW.sifobj;
```

---

## 11. operdoc_del_blgpromet

**Tabela:** `blgpromet` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_blgpromet` BEFORE DELETE ON `blgpromet` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 12. operdoc_del_fakture

**Tabela:** `fakture` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_fakture` BEFORE DELETE ON `fakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 13. operdoc_del_faktureos

**Tabela:** `faktureos` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_faktureos` BEFORE DELETE ON `faktureos` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 14. operdoc_del_finprom

**Tabela:** `finprom` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_finprom` BEFORE DELETE ON `finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and ((old.status>2) or (old.stornirano>0)) then
    set msg = "##ODP##DOKUMENT/STAVKA JE PROKNJIEN ILI STORNIRAN!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 15. operdoc_del_frmgk_avans

**Tabela:** `frmgk_avans` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_avans` BEFORE DELETE ON `frmgk_avans` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 16. operdoc_del_frmgk_carina

**Tabela:** `frmgk_carina` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_carina` BEFORE DELETE ON `frmgk_carina` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 17. operdoc_del_frmgk_ed

**Tabela:** `frmgk_ed` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_ed` BEFORE DELETE ON `frmgk_ed` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 18. operdoc_del_frmgk_faktura

**Tabela:** `frmgk_faktura` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_faktura` BEFORE DELETE ON `frmgk_faktura` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 19. operdoc_del_frmgk_nefak

**Tabela:** `frmgk_nefak` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_nefak` BEFORE DELETE ON `frmgk_nefak` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 20. operdoc_del_frmgk_nefak_spec

**Tabela:** `frmgk_nefak_spec` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_nefak_spec` BEFORE DELETE ON `frmgk_nefak_spec` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_nefak where brnal=replace(old.brnal,'NR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_nefak where brnal=replace(old.brnal,'NR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 21. operdoc_del_frmgk_osnsred

**Tabela:** `frmgk_osnsred` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_osnsred` BEFORE DELETE ON `frmgk_osnsred` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 22. operdoc_del_frmgk_prijemfakture

**Tabela:** `frmgk_prijemfakture` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_prijemfakture` BEFORE DELETE ON `frmgk_prijemfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 23. operdoc_del_frmgk_troskovi

**Tabela:** `frmgk_troskovi` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_frmgk_troskovi` BEFORE DELETE ON `frmgk_troskovi` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 24. operdoc_del_intprijem

**Tabela:** `intprijem` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_intprijem` BEFORE DELETE ON `intprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 25. operdoc_del_intracun

**Tabela:** `intracun` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_intracun` BEFORE DELETE ON `intracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 26. operdoc_del_kalkulacije

**Tabela:** `kalkulacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_kalkulacije` BEFORE DELETE ON `kalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 27. operdoc_del_komnivelacije

**Tabela:** `komnivelacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_komnivelacije` BEFORE DELETE ON `komnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 28. operdoc_del_nabambalaze

**Tabela:** `nabambalaze` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_nabambalaze` BEFORE DELETE ON `nabambalaze` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 29. operdoc_del_nivelacije

**Tabela:** `nivelacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_nivelacije` BEFORE DELETE ON `nivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 30. operdoc_del_nivkalkulacije

**Tabela:** `nivkalkulacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_nivkalkulacije` BEFORE DELETE ON `nivkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 31. operdoc_del_pazari

**Tabela:** `pazari` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_pazari` BEFORE DELETE ON `pazari` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 32. operdoc_del_popis

**Tabela:** `popis` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_popis` BEFORE DELETE ON `popis` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 33. operdoc_del_prodintracun

**Tabela:** `prodintracun` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_prodintracun` BEFORE DELETE ON `prodintracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 34. operdoc_del_prodkalkulacije

**Tabela:** `prodkalkulacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_prodkalkulacije` BEFORE DELETE ON `prodkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 35. operdoc_del_prodnivelacije

**Tabela:** `prodnivelacije` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_prodnivelacije` BEFORE DELETE ON `prodnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 36. operdoc_del_prodpovracajdob

**Tabela:** `prodpovracajdob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_prodpovracajdob` BEFORE DELETE ON `prodpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 37. operdoc_del_proveraprijema

**Tabela:** `proveraprijema` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_proveraprijema` BEFORE DELETE ON `proveraprijema` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 38. operdoc_del_putninalog

**Tabela:** `putninalog` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_putninalog` BEFORE DELETE ON `putninalog` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 39. operdoc_del_radnal

**Tabela:** `radnal` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_radnal` BEFORE DELETE ON `radnal` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 40. operdoc_del_sitinvpov

**Tabela:** `sitinvpov` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_sitinvpov` BEFORE DELETE ON `sitinvpov` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 41. operdoc_del_sitinvras

**Tabela:** `sitinvras` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_sitinvras` BEFORE DELETE ON `sitinvras` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 42. operdoc_del_sitinvzad

**Tabela:** `sitinvzad` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_sitinvzad` BEFORE DELETE ON `sitinvzad` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 43. operdoc_del_tblambintpr

**Tabela:** `tblambintpr` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblambintpr` BEFORE DELETE ON `tblambintpr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 44. operdoc_del_tblamizdkup

**Tabela:** `tblamizdkup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblamizdkup` BEFORE DELETE ON `tblamizdkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 45. operdoc_del_tblampovdob

**Tabela:** `tblampovdob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblampovdob` BEFORE DELETE ON `tblampovdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 46. operdoc_del_tblampovkup

**Tabela:** `tblampovkup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblampovkup` BEFORE DELETE ON `tblampovkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 47. operdoc_del_tblamprijdob

**Tabela:** `tblamprijdob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblamprijdob` BEFORE DELETE ON `tblamprijdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 48. operdoc_del_tblfaktakcrab

**Tabela:** `tblfaktakcrab` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblfaktakcrab` BEFORE DELETE ON `tblfaktakcrab` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 49. operdoc_del_tblfaktbezobr

**Tabela:** `tblfaktbezobr` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblfaktbezobr` BEFORE DELETE ON `tblfaktbezobr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 50. operdoc_del_tblintizdavanje

**Tabela:** `tblintizdavanje` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblintizdavanje` BEFORE DELETE ON `tblintizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 51. operdoc_del_tblisplata

**Tabela:** `tblisplata` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblisplata` BEFORE DELETE ON `tblisplata` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 52. operdoc_del_tblizdavanje

**Tabela:** `tblizdavanje` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblizdavanje` BEFORE DELETE ON `tblizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 53. operdoc_del_tblizvoz

**Tabela:** `tblizvoz` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblizvoz` BEFORE DELETE ON `tblizvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 54. operdoc_del_tblkomfakture

**Tabela:** `tblkomfakture` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblkomfakture` BEFORE DELETE ON `tblkomfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 55. operdoc_del_tblkomkalk

**Tabela:** `tblkomkalk` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblkomkalk` BEFORE DELETE ON `tblkomkalk` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 56. operdoc_del_tblkomvrac

**Tabela:** `tblkomvrac` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblkomvrac` BEFORE DELETE ON `tblkomvrac` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 57. operdoc_del_tblkooizdavanje

**Tabela:** `tblkooizdavanje` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblkooizdavanje` BEFORE DELETE ON `tblkooizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 58. operdoc_del_tblmatobrdor

**Tabela:** `tblmatobrdor` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblmatobrdor` BEFORE DELETE ON `tblmatobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 59. operdoc_del_tblmatobrdorprij

**Tabela:** `tblmatobrdorprij` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblmatobrdorprij` BEFORE DELETE ON `tblmatobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 60. operdoc_del_tblnabsitinv

**Tabela:** `tblnabsitinv` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblnabsitinv` BEFORE DELETE ON `tblnabsitinv` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 61. operdoc_del_tblnardobavljacima

**Tabela:** `tblnardobavljacima` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblnardobavljacima` BEFORE DELETE ON `tblnardobavljacima` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 62. operdoc_del_tblnarkupaca

**Tabela:** `tblnarkupaca` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblnarkupaca` BEFORE DELETE ON `tblnarkupaca` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 63. operdoc_del_tblodobdob

**Tabela:** `tblodobdob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblodobdob` BEFORE DELETE ON `tblodobdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 64. operdoc_del_tblodobinodob

**Tabela:** `tblodobinodob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblodobinodob` BEFORE DELETE ON `tblodobinodob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 65. operdoc_del_tblodobinokup

**Tabela:** `tblodobinokup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblodobinokup` BEFORE DELETE ON `tblodobinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 66. operdoc_del_tblodobkup

**Tabela:** `tblodobkup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblodobkup` BEFORE DELETE ON `tblodobkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 67. operdoc_del_tblotkup

**Tabela:** `tblotkup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblotkup` BEFORE DELETE ON `tblotkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 68. operdoc_del_tblotkupss

**Tabela:** `tblotkupss` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblotkupss` BEFORE DELETE ON `tblotkupss` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 69. operdoc_del_tblotpisnz

**Tabela:** `tblotpisnz` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblotpisnz` BEFORE DELETE ON `tblotpisnz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 70. operdoc_del_tblotpisz

**Tabela:** `tblotpisz` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblotpisz` BEFORE DELETE ON `tblotpisz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 71. operdoc_del_tblpoljoprivreda

**Tabela:** `tblpoljoprivreda` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblpoljoprivreda` BEFORE DELETE ON `tblpoljoprivreda` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 72. operdoc_del_tblposotpremnice

**Tabela:** `tblposotpremnice` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblposotpremnice` BEFORE DELETE ON `tblposotpremnice` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 73. operdoc_del_tblpovracaj

**Tabela:** `tblpovracaj` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblpovracaj` BEFORE DELETE ON `tblpovracaj` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 74. operdoc_del_tblpovracajdob

**Tabela:** `tblpovracajdob` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblpovracajdob` BEFORE DELETE ON `tblpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 75. operdoc_del_tblpovracajdobnovi

**Tabela:** `tblpovracajdobnovi` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblpovracajdobnovi` BEFORE DELETE ON `tblpovracajdobnovi` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 76. operdoc_del_tblpovracajinokup

**Tabela:** `tblpovracajinokup` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblpovracajinokup` BEFORE DELETE ON `tblpovracajinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 77. operdoc_del_tblprodajagp

**Tabela:** `tblprodajagp` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblprodajagp` BEFORE DELETE ON `tblprodajagp` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 78. operdoc_del_tblprodamb

**Tabela:** `tblprodamb` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblprodamb` BEFORE DELETE ON `tblprodamb` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 79. operdoc_del_tblprodfakture

**Tabela:** `tblprodfakture` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblprodfakture` BEFORE DELETE ON `tblprodfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 80. operdoc_del_tblprodmat

**Tabela:** `tblprodmat` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblprodmat` BEFORE DELETE ON `tblprodmat` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 81. operdoc_del_tblproizvobrdor

**Tabela:** `tblproizvobrdor` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblproizvobrdor` BEFORE DELETE ON `tblproizvobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 82. operdoc_del_tblproizvobrdorprij

**Tabela:** `tblproizvobrdorprij` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblproizvobrdorprij` BEFORE DELETE ON `tblproizvobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 83. operdoc_del_tblreversizdavanje

**Tabela:** `tblreversizdavanje` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblreversizdavanje` BEFORE DELETE ON `tblreversizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 84. operdoc_del_tblreversprijem

**Tabela:** `tblreversprijem` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblreversprijem` BEFORE DELETE ON `tblreversprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 85. operdoc_del_tblrobobrdor

**Tabela:** `tblrobobrdor` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblrobobrdor` BEFORE DELETE ON `tblrobobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 86. operdoc_del_tblrobobrdorprij

**Tabela:** `tblrobobrdorprij` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblrobobrdorprij` BEFORE DELETE ON `tblrobobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 87. operdoc_del_tblrobtransf

**Tabela:** `tblrobtransf` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblrobtransf` BEFORE DELETE ON `tblrobtransf` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 88. operdoc_del_tblsitanizd

**Tabela:** `tblsitanizd` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblsitanizd` BEFORE DELETE ON `tblsitanizd` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 89. operdoc_del_tblsopsttros

**Tabela:** `tblsopsttros` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tblsopsttros` BEFORE DELETE ON `tblsopsttros` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 90. operdoc_del_tbltrebovanje

**Tabela:** `tbltrebovanje` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tbltrebovanje` BEFORE DELETE ON `tbltrebovanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 91. operdoc_del_tbluvoz

**Tabela:** `tbluvoz` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tbluvoz` BEFORE DELETE ON `tbluvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 92. operdoc_del_tr_finprom

**Tabela:** `tr_finprom` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_del_tr_finprom` BEFORE DELETE ON `tr_finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_troskovi where brnal=replace(old.brnal,'TR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_troskovi where brnal=replace(old.brnal,'TR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 93. operdoc_ins_fakture

**Tabela:** `fakture` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_fakture` BEFORE INSERT ON `fakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from fakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from fakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 94. operdoc_ins_faktureos

**Tabela:** `faktureos` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_faktureos` BEFORE INSERT ON `faktureos` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from faktureos where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from faktureos where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 95. operdoc_ins_finprom

**Tabela:** `finprom` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_finprom` BEFORE INSERT ON `finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from finprom where brnal=new.brnal and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from finprom where brnal=new.brnal and status>2 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 96. operdoc_ins_frmgk_nefak_spec

**Tabela:** `frmgk_nefak_spec` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_frmgk_nefak_spec` BEFORE INSERT ON `frmgk_nefak_spec` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_nefak where brnal=replace(new.brnal,'NR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_nefak where brnal=replace(new.brnal,'NR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 97. operdoc_ins_intprijem

**Tabela:** `intprijem` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_intprijem` BEFORE INSERT ON `intprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from intprijem where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from intprijem where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 98. operdoc_ins_intracun

**Tabela:** `intracun` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_intracun` BEFORE INSERT ON `intracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from intracun where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from intracun where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 99. operdoc_ins_kalkulacije

**Tabela:** `kalkulacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_kalkulacije` BEFORE INSERT ON `kalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from kalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from kalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 100. operdoc_ins_komnivelacije

**Tabela:** `komnivelacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_komnivelacije` BEFORE INSERT ON `komnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from komnivelacije where sifobj=new.sifobj and brnivel=new.brnivel and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from komnivelacije where sifobj=new.sifobj and brnivel=new.brnivel and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 101. operdoc_ins_nabambalaze

**Tabela:** `nabambalaze` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_nabambalaze` BEFORE INSERT ON `nabambalaze` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from nabambalaze where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from nabambalaze where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 102. operdoc_ins_nivelacije

**Tabela:** `nivelacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_nivelacije` BEFORE INSERT ON `nivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from nivelacije where sifobj=new.sifobj and brnivel=new.brnivel and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from nivelacije where sifobj=new.sifobj and brnivel=new.brnivel and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 103. operdoc_ins_nivkalkulacije

**Tabela:** `nivkalkulacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_nivkalkulacije` BEFORE INSERT ON `nivkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from nivkalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from nivkalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 104. operdoc_ins_pazari

**Tabela:** `pazari` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_pazari` BEFORE INSERT ON `pazari` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from pazari where objekat=new.objekat and datum=new.datum and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from pazari where objekat=new.objekat and datum=new.datum and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 105. operdoc_ins_prodintracun

**Tabela:** `prodintracun` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_prodintracun` BEFORE INSERT ON `prodintracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from prodintracun where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from prodintracun where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 106. operdoc_ins_prodkalkulacije

**Tabela:** `prodkalkulacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_prodkalkulacije` BEFORE INSERT ON `prodkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from prodkalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from prodkalkulacije where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 107. operdoc_ins_prodnivelacije

**Tabela:** `prodnivelacije` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_prodnivelacije` BEFORE INSERT ON `prodnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from prodnivelacije where sifobj=new.sifobj and brnivel=new.brnivel and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from prodnivelacije where sifobj=new.sifobj and brnivel=new.brnivel and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 108. operdoc_ins_prodpovracajdob

**Tabela:** `prodpovracajdob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_prodpovracajdob` BEFORE INSERT ON `prodpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from prodpovracajdob where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from prodpovracajdob where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 109. operdoc_ins_proveraprijema

**Tabela:** `proveraprijema` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_proveraprijema` BEFORE INSERT ON `proveraprijema` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from proveraprijema where brkl=new.brkl and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from proveraprijema where brkl=new.brkl and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 110. operdoc_ins_sitinvpov

**Tabela:** `sitinvpov` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_sitinvpov` BEFORE INSERT ON `sitinvpov` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from sitinvpov where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from sitinvpov where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 111. operdoc_ins_sitinvras

**Tabela:** `sitinvras` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_sitinvras` BEFORE INSERT ON `sitinvras` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from sitinvras where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from sitinvras where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 112. operdoc_ins_sitinvzad

**Tabela:** `sitinvzad` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_sitinvzad` BEFORE INSERT ON `sitinvzad` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from sitinvzad where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from sitinvzad where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 113. operdoc_ins_tblambintpr

**Tabela:** `tblambintpr` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblambintpr` BEFORE INSERT ON `tblambintpr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblambintpr where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblambintpr where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 114. operdoc_ins_tblamizdkup

**Tabela:** `tblamizdkup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblamizdkup` BEFORE INSERT ON `tblamizdkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblamizdkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblamizdkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 115. operdoc_ins_tblampovdob

**Tabela:** `tblampovdob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblampovdob` BEFORE INSERT ON `tblampovdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblampovdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblampovdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 116. operdoc_ins_tblampovkup

**Tabela:** `tblampovkup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblampovkup` BEFORE INSERT ON `tblampovkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblampovkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblampovkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 117. operdoc_ins_tblamprijdob

**Tabela:** `tblamprijdob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblamprijdob` BEFORE INSERT ON `tblamprijdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblamprijdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblamprijdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 118. operdoc_ins_tblfaktakcrab

**Tabela:** `tblfaktakcrab` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblfaktakcrab` BEFORE INSERT ON `tblfaktakcrab` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblfaktakcrab where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblfaktakcrab where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 119. operdoc_ins_tblfaktbezobr

**Tabela:** `tblfaktbezobr` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblfaktbezobr` BEFORE INSERT ON `tblfaktbezobr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblfaktbezobr where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblfaktbezobr where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 120. operdoc_ins_tblintizdavanje

**Tabela:** `tblintizdavanje` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblintizdavanje` BEFORE INSERT ON `tblintizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblintizdavanje where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblintizdavanje where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 121. operdoc_ins_tblizdavanje

**Tabela:** `tblizdavanje` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblizdavanje` BEFORE INSERT ON `tblizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 122. operdoc_ins_tblizvoz

**Tabela:** `tblizvoz` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblizvoz` BEFORE INSERT ON `tblizvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblizvoz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblizvoz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 123. operdoc_ins_tblkomfakture

**Tabela:** `tblkomfakture` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblkomfakture` BEFORE INSERT ON `tblkomfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblkomfakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblkomfakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 124. operdoc_ins_tblkomkalk

**Tabela:** `tblkomkalk` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblkomkalk` BEFORE INSERT ON `tblkomkalk` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblkomkalk where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblkomkalk where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 125. operdoc_ins_tblkomvrac

**Tabela:** `tblkomvrac` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblkomvrac` BEFORE INSERT ON `tblkomvrac` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblkomvrac where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblkomvrac where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 126. operdoc_ins_tblkooizdavanje

**Tabela:** `tblkooizdavanje` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblkooizdavanje` BEFORE INSERT ON `tblkooizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblkooizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblkooizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 127. operdoc_ins_tblmatobrdor

**Tabela:** `tblmatobrdor` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblmatobrdor` BEFORE INSERT ON `tblmatobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblmatobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblmatobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 128. operdoc_ins_tblmatobrdorprij

**Tabela:** `tblmatobrdorprij` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblmatobrdorprij` BEFORE INSERT ON `tblmatobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblmatobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblmatobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 129. operdoc_ins_tblnabsitinv

**Tabela:** `tblnabsitinv` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblnabsitinv` BEFORE INSERT ON `tblnabsitinv` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblnabsitinv where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblnabsitinv where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 130. operdoc_ins_tblnardobavljacima

**Tabela:** `tblnardobavljacima` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblnardobavljacima` BEFORE INSERT ON `tblnardobavljacima` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblnardobavljacima where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblnardobavljacima where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 131. operdoc_ins_tblnarkupaca

**Tabela:** `tblnarkupaca` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblnarkupaca` BEFORE INSERT ON `tblnarkupaca` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblnarkupaca where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblnarkupaca where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 132. operdoc_ins_tblodobdob

**Tabela:** `tblodobdob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblodobdob` BEFORE INSERT ON `tblodobdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblodobdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblodobdob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 133. operdoc_ins_tblodobinodob

**Tabela:** `tblodobinodob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblodobinodob` BEFORE INSERT ON `tblodobinodob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblodobinodob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblodobinodob where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 134. operdoc_ins_tblodobinokup

**Tabela:** `tblodobinokup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblodobinokup` BEFORE INSERT ON `tblodobinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblodobinokup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblodobinokup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 135. operdoc_ins_tblodobkup

**Tabela:** `tblodobkup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblodobkup` BEFORE INSERT ON `tblodobkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblodobkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblodobkup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 136. operdoc_ins_tblotkup

**Tabela:** `tblotkup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblotkup` BEFORE INSERT ON `tblotkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblotkup where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblotkup where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 137. operdoc_ins_tblotkupss

**Tabela:** `tblotkupss` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblotkupss` BEFORE INSERT ON `tblotkupss` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblotkupss where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblotkupss where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 138. operdoc_ins_tblotpisnz

**Tabela:** `tblotpisnz` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblotpisnz` BEFORE INSERT ON `tblotpisnz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblotpisnz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblotpisnz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 139. operdoc_ins_tblotpisz

**Tabela:** `tblotpisz` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblotpisz` BEFORE INSERT ON `tblotpisz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblotpisz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblotpisz where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 140. operdoc_ins_tblpoljoprivreda

**Tabela:** `tblpoljoprivreda` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblpoljoprivreda` BEFORE INSERT ON `tblpoljoprivreda` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblpoljoprivreda where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblpoljoprivreda where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 141. operdoc_ins_tblposotpremnice

**Tabela:** `tblposotpremnice` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblposotpremnice` BEFORE INSERT ON `tblposotpremnice` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblposotpremnice where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblposotpremnice where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 142. operdoc_ins_tblpovracaj

**Tabela:** `tblpovracaj` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblpovracaj` BEFORE INSERT ON `tblpovracaj` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblpovracaj where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblpovracaj where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 143. operdoc_ins_tblpovracajdob

**Tabela:** `tblpovracajdob` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblpovracajdob` BEFORE INSERT ON `tblpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblpovracajdob where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblpovracajdob where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 144. operdoc_ins_tblpovracajdobnovi

**Tabela:** `tblpovracajdobnovi` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblpovracajdobnovi` BEFORE INSERT ON `tblpovracajdobnovi` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblpovracajdobnovi where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblpovracajdobnovi where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 145. operdoc_ins_tblpovracajinokup

**Tabela:** `tblpovracajinokup` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblpovracajinokup` BEFORE INSERT ON `tblpovracajinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblpovracajinokup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblpovracajinokup where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 146. operdoc_ins_tblprodajagp

**Tabela:** `tblprodajagp` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblprodajagp` BEFORE INSERT ON `tblprodajagp` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblprodajagp where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblprodajagp where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 147. operdoc_ins_tblprodamb

**Tabela:** `tblprodamb` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblprodamb` BEFORE INSERT ON `tblprodamb` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblprodamb where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblprodamb where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 148. operdoc_ins_tblprodfakture

**Tabela:** `tblprodfakture` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblprodfakture` BEFORE INSERT ON `tblprodfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblprodfakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblprodfakture where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 149. operdoc_ins_tblprodmat

**Tabela:** `tblprodmat` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblprodmat` BEFORE INSERT ON `tblprodmat` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblprodmat where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblprodmat where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 150. operdoc_ins_tblproizvobrdor

**Tabela:** `tblproizvobrdor` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblproizvobrdor` BEFORE INSERT ON `tblproizvobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblproizvobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblproizvobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 151. operdoc_ins_tblproizvobrdorprij

**Tabela:** `tblproizvobrdorprij` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblproizvobrdorprij` BEFORE INSERT ON `tblproizvobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblproizvobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblproizvobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 152. operdoc_ins_tblreversizdavanje

**Tabela:** `tblreversizdavanje` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblreversizdavanje` BEFORE INSERT ON `tblreversizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblreversizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblreversizdavanje where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 153. operdoc_ins_tblreversprijem

**Tabela:** `tblreversprijem` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblreversprijem` BEFORE INSERT ON `tblreversprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblreversprijem where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblreversprijem where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 154. operdoc_ins_tblrobobrdor

**Tabela:** `tblrobobrdor` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblrobobrdor` BEFORE INSERT ON `tblrobobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblrobobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblrobobrdor where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 155. operdoc_ins_tblrobobrdorprij

**Tabela:** `tblrobobrdorprij` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblrobobrdorprij` BEFORE INSERT ON `tblrobobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblrobobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblrobobrdorprij where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 156. operdoc_ins_tblrobtransf

**Tabela:** `tblrobtransf` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblrobtransf` BEFORE INSERT ON `tblrobtransf` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblrobtransf where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblrobtransf where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 157. operdoc_ins_tblsitanizd

**Tabela:** `tblsitanizd` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblsitanizd` BEFORE INSERT ON `tblsitanizd` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tblsitanizd where sifobj=new.sifobj and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tblsitanizd where sifobj=new.sifobj and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 158. operdoc_ins_tblsopsttros

**Tabela:** `tblsopsttros` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tblsopsttros` BEFORE INSERT ON `tblsopsttros` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT operater from tblsopsttros where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 and (new.tip not in ('X','B','Y','W','E')) then
    SET @w=(SELECT status from tblsopsttros where sifobj=new.sifobj AND tip=new.tip and brrn=new.brrn and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 159. operdoc_ins_tbltrebovanje

**Tabela:** `tbltrebovanje` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tbltrebovanje` BEFORE INSERT ON `tbltrebovanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tbltrebovanje where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tbltrebovanje where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 160. operdoc_ins_tbluvoz

**Tabela:** `tbluvoz` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tbluvoz` BEFORE INSERT ON `tbluvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT operater from tbluvoz where sifobj=new.sifobj and brkalk=new.brkalk and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and new.rbrst>1 then
    SET @w=(SELECT status from tbluvoz where sifobj=new.sifobj and brkalk=new.brkalk and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 161. operdoc_ins_tr_finprom

**Tabela:** `tr_finprom` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_ins_tr_finprom` BEFORE INSERT ON `tr_finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_troskovi where brnal=replace(new.brnal,'TR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_troskovi where brnal=replace(new.brnal,'TR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 162. operdoc_upd_blgpromet

**Tabela:** `blgpromet` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_blgpromet` BEFORE UPDATE ON `blgpromet` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 163. operdoc_upd_fakture

**Tabela:** `fakture` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_fakture` BEFORE UPDATE ON `fakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1))  and (not ((old.tip='P') and (old.status=2))) and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='W')  and (old.status=2)))  and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='Y') and (old.status=2))) and (not ((old.tip='X') and (old.status=2))) and (not ((old.tip='B') and (old.status=2))) and (not ((old.tip='E') and (old.status=2))) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 164. operdoc_upd_faktureos

**Tabela:** `faktureos` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_faktureos` BEFORE UPDATE ON `faktureos` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 165. operdoc_upd_finprom

**Tabela:** `finprom` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_finprom` BEFORE UPDATE ON `finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and ((old.status>2) or ((old.stornirano>0) and isnull(@ignorisistorno))) then
    set msg = "##ODP##DOKUMENT/STAVKA JE PROKNJIEN ILI STORNIRAN!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 166. operdoc_upd_frmgk_avans

**Tabela:** `frmgk_avans` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_avans` BEFORE UPDATE ON `frmgk_avans` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 167. operdoc_upd_frmgk_carina

**Tabela:** `frmgk_carina` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_carina` BEFORE UPDATE ON `frmgk_carina` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 168. operdoc_upd_frmgk_ed

**Tabela:** `frmgk_ed` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_ed` BEFORE UPDATE ON `frmgk_ed` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 169. operdoc_upd_frmgk_faktura

**Tabela:** `frmgk_faktura` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_faktura` BEFORE UPDATE ON `frmgk_faktura` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 170. operdoc_upd_frmgk_nefak

**Tabela:** `frmgk_nefak` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_nefak` BEFORE UPDATE ON `frmgk_nefak` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 171. operdoc_upd_frmgk_nefak_spec

**Tabela:** `frmgk_nefak_spec` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_nefak_spec` BEFORE UPDATE ON `frmgk_nefak_spec` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_nefak where brnal=replace(new.brnal,'NR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_nefak where brnal=replace(new.brnal,'NR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 172. operdoc_upd_frmgk_osnsred

**Tabela:** `frmgk_osnsred` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_osnsred` BEFORE UPDATE ON `frmgk_osnsred` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 173. operdoc_upd_frmgk_prijemfakture

**Tabela:** `frmgk_prijemfakture` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_prijemfakture` BEFORE UPDATE ON `frmgk_prijemfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 174. operdoc_upd_frmgk_troskovi

**Tabela:** `frmgk_troskovi` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_frmgk_troskovi` BEFORE UPDATE ON `frmgk_troskovi` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 175. operdoc_upd_intprijem

**Tabela:** `intprijem` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_intprijem` BEFORE UPDATE ON `intprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 176. operdoc_upd_intracun

**Tabela:** `intracun` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_intracun` BEFORE UPDATE ON `intracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 177. operdoc_upd_kalkulacije

**Tabela:** `kalkulacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_kalkulacije` BEFORE UPDATE ON `kalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 178. operdoc_upd_komnivelacije

**Tabela:** `komnivelacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_komnivelacije` BEFORE UPDATE ON `komnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 179. operdoc_upd_nabambalaze

**Tabela:** `nabambalaze` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_nabambalaze` BEFORE UPDATE ON `nabambalaze` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 180. operdoc_upd_nivelacije

**Tabela:** `nivelacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_nivelacije` BEFORE UPDATE ON `nivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 181. operdoc_upd_nivkalkulacije

**Tabela:** `nivkalkulacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_nivkalkulacije` BEFORE UPDATE ON `nivkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 182. operdoc_upd_pazari

**Tabela:** `pazari` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_pazari` BEFORE UPDATE ON `pazari` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 183. operdoc_upd_popis

**Tabela:** `popis` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_popis` BEFORE UPDATE ON `popis` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 184. operdoc_upd_prodintracun

**Tabela:** `prodintracun` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_prodintracun` BEFORE UPDATE ON `prodintracun` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 185. operdoc_upd_prodkalkulacije

**Tabela:** `prodkalkulacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_prodkalkulacije` BEFORE UPDATE ON `prodkalkulacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 186. operdoc_upd_prodnivelacije

**Tabela:** `prodnivelacije` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_prodnivelacije` BEFORE UPDATE ON `prodnivelacije` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 187. operdoc_upd_prodpovracajdob

**Tabela:** `prodpovracajdob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_prodpovracajdob` BEFORE UPDATE ON `prodpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 188. operdoc_upd_proveraprijema

**Tabela:** `proveraprijema` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_proveraprijema` BEFORE UPDATE ON `proveraprijema` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 189. operdoc_upd_putninalog

**Tabela:** `putninalog` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_putninalog` BEFORE UPDATE ON `putninalog` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 190. operdoc_upd_radnal

**Tabela:** `radnal` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_radnal` BEFORE UPDATE ON `radnal` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 191. operdoc_upd_sitinvpov

**Tabela:** `sitinvpov` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_sitinvpov` BEFORE UPDATE ON `sitinvpov` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 192. operdoc_upd_sitinvras

**Tabela:** `sitinvras` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_sitinvras` BEFORE UPDATE ON `sitinvras` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 193. operdoc_upd_sitinvzad

**Tabela:** `sitinvzad` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_sitinvzad` BEFORE UPDATE ON `sitinvzad` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 194. operdoc_upd_tblambintpr

**Tabela:** `tblambintpr` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblambintpr` BEFORE UPDATE ON `tblambintpr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 195. operdoc_upd_tblamizdkup

**Tabela:** `tblamizdkup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblamizdkup` BEFORE UPDATE ON `tblamizdkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 196. operdoc_upd_tblampovdob

**Tabela:** `tblampovdob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblampovdob` BEFORE UPDATE ON `tblampovdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 197. operdoc_upd_tblampovkup

**Tabela:** `tblampovkup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblampovkup` BEFORE UPDATE ON `tblampovkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 198. operdoc_upd_tblamprijdob

**Tabela:** `tblamprijdob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblamprijdob` BEFORE UPDATE ON `tblamprijdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 199. operdoc_upd_tblfaktakcrab

**Tabela:** `tblfaktakcrab` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblfaktakcrab` BEFORE UPDATE ON `tblfaktakcrab` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1))  and (not ((old.tip='P') and (old.status=2))) and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='W')  and (old.status=2)))  and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='Y') and (old.status=2))) and (not ((old.tip='X') and (old.status=2))) and (not ((old.tip='B') and (old.status=2))) and (not ((old.tip='E') and (old.status=2))) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 200. operdoc_upd_tblfaktbezobr

**Tabela:** `tblfaktbezobr` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblfaktbezobr` BEFORE UPDATE ON `tblfaktbezobr` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 201. operdoc_upd_tblintizdavanje

**Tabela:** `tblintizdavanje` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblintizdavanje` BEFORE UPDATE ON `tblintizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 202. operdoc_upd_tblisplata

**Tabela:** `tblisplata` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblisplata` BEFORE UPDATE ON `tblisplata` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 203. operdoc_upd_tblizdavanje

**Tabela:** `tblizdavanje` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblizdavanje` BEFORE UPDATE ON `tblizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 204. operdoc_upd_tblizvoz

**Tabela:** `tblizvoz` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblizvoz` BEFORE UPDATE ON `tblizvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1))  and (not ((old.tip='P') and (old.status=2))) and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='W')  and (old.status=2)))  and (not ((old.tip='I') and (old.status=2))) and (not ((old.tip='Y') and (old.status=2))) and (not ((old.tip='X') and (old.status=2))) and (not ((old.tip='B') and (old.status=2))) and (not ((old.tip='E') and (old.status=2))) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 205. operdoc_upd_tblkomfakture

**Tabela:** `tblkomfakture` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblkomfakture` BEFORE UPDATE ON `tblkomfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 206. operdoc_upd_tblkomkalk

**Tabela:** `tblkomkalk` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblkomkalk` BEFORE UPDATE ON `tblkomkalk` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 207. operdoc_upd_tblkomvrac

**Tabela:** `tblkomvrac` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblkomvrac` BEFORE UPDATE ON `tblkomvrac` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 208. operdoc_upd_tblkooizdavanje

**Tabela:** `tblkooizdavanje` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblkooizdavanje` BEFORE UPDATE ON `tblkooizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 209. operdoc_upd_tblmatobrdor

**Tabela:** `tblmatobrdor` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblmatobrdor` BEFORE UPDATE ON `tblmatobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 210. operdoc_upd_tblmatobrdorprij

**Tabela:** `tblmatobrdorprij` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblmatobrdorprij` BEFORE UPDATE ON `tblmatobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 211. operdoc_upd_tblnabsitinv

**Tabela:** `tblnabsitinv` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblnabsitinv` BEFORE UPDATE ON `tblnabsitinv` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 212. operdoc_upd_tblnardobavljacima

**Tabela:** `tblnardobavljacima` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblnardobavljacima` BEFORE UPDATE ON `tblnardobavljacima` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 213. operdoc_upd_tblnarkupaca

**Tabela:** `tblnarkupaca` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblnarkupaca` BEFORE UPDATE ON `tblnarkupaca` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 214. operdoc_upd_tblodobdob

**Tabela:** `tblodobdob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblodobdob` BEFORE UPDATE ON `tblodobdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 215. operdoc_upd_tblodobinodob

**Tabela:** `tblodobinodob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblodobinodob` BEFORE UPDATE ON `tblodobinodob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 216. operdoc_upd_tblodobinokup

**Tabela:** `tblodobinokup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblodobinokup` BEFORE UPDATE ON `tblodobinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 217. operdoc_upd_tblodobkup

**Tabela:** `tblodobkup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblodobkup` BEFORE UPDATE ON `tblodobkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 218. operdoc_upd_tblotkup

**Tabela:** `tblotkup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblotkup` BEFORE UPDATE ON `tblotkup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 219. operdoc_upd_tblotkupss

**Tabela:** `tblotkupss` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblotkupss` BEFORE UPDATE ON `tblotkupss` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 220. operdoc_upd_tblotpisnz

**Tabela:** `tblotpisnz` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblotpisnz` BEFORE UPDATE ON `tblotpisnz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 221. operdoc_upd_tblotpisz

**Tabela:** `tblotpisz` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblotpisz` BEFORE UPDATE ON `tblotpisz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 222. operdoc_upd_tblpoljoprivreda

**Tabela:** `tblpoljoprivreda` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblpoljoprivreda` BEFORE UPDATE ON `tblpoljoprivreda` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 223. operdoc_upd_tblposotpremnice

**Tabela:** `tblposotpremnice` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblposotpremnice` BEFORE UPDATE ON `tblposotpremnice` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 224. operdoc_upd_tblpovracaj

**Tabela:** `tblpovracaj` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblpovracaj` BEFORE UPDATE ON `tblpovracaj` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 225. operdoc_upd_tblpovracajdob

**Tabela:** `tblpovracajdob` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblpovracajdob` BEFORE UPDATE ON `tblpovracajdob` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 226. operdoc_upd_tblpovracajdobnovi

**Tabela:** `tblpovracajdobnovi` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblpovracajdobnovi` BEFORE UPDATE ON `tblpovracajdobnovi` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 227. operdoc_upd_tblpovracajinokup

**Tabela:** `tblpovracajinokup` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblpovracajinokup` BEFORE UPDATE ON `tblpovracajinokup` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 228. operdoc_upd_tblprodajagp

**Tabela:** `tblprodajagp` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblprodajagp` BEFORE UPDATE ON `tblprodajagp` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 229. operdoc_upd_tblprodamb

**Tabela:** `tblprodamb` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblprodamb` BEFORE UPDATE ON `tblprodamb` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 230. operdoc_upd_tblprodfakture

**Tabela:** `tblprodfakture` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblprodfakture` BEFORE UPDATE ON `tblprodfakture` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 231. operdoc_upd_tblprodmat

**Tabela:** `tblprodmat` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblprodmat` BEFORE UPDATE ON `tblprodmat` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 232. operdoc_upd_tblproizvobrdor

**Tabela:** `tblproizvobrdor` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblproizvobrdor` BEFORE UPDATE ON `tblproizvobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 233. operdoc_upd_tblproizvobrdorprij

**Tabela:** `tblproizvobrdorprij` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblproizvobrdorprij` BEFORE UPDATE ON `tblproizvobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 234. operdoc_upd_tblreversizdavanje

**Tabela:** `tblreversizdavanje` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblreversizdavanje` BEFORE UPDATE ON `tblreversizdavanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 235. operdoc_upd_tblreversprijem

**Tabela:** `tblreversprijem` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblreversprijem` BEFORE UPDATE ON `tblreversprijem` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 236. operdoc_upd_tblrobobrdor

**Tabela:** `tblrobobrdor` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblrobobrdor` BEFORE UPDATE ON `tblrobobrdor` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 237. operdoc_upd_tblrobobrdorprij

**Tabela:** `tblrobobrdorprij` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblrobobrdorprij` BEFORE UPDATE ON `tblrobobrdorprij` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 238. operdoc_upd_tblrobtransf

**Tabela:** `tblrobtransf` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblrobtransf` BEFORE UPDATE ON `tblrobtransf` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 239. operdoc_upd_tblsitanizd

**Tabela:** `tblsitanizd` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblsitanizd` BEFORE UPDATE ON `tblsitanizd` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 240. operdoc_upd_tblsopsttros

**Tabela:** `tblsopsttros` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tblsopsttros` BEFORE UPDATE ON `tblsopsttros` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 241. operdoc_upd_tbltrebovanje

**Tabela:** `tbltrebovanje` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tbltrebovanje` BEFORE UPDATE ON `tbltrebovanje` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 242. operdoc_upd_tbluvoz

**Tabela:** `tbluvoz` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tbluvoz` BEFORE UPDATE ON `tbluvoz` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (@aktivnioperater=old.operater)) then
    set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) and (not (old.status=1)) then
    set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
  END IF;
end
```

---

## 243. operdoc_upd_tr_finprom

**Tabela:** `tr_finprom` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `operdoc_upd_tr_finprom` BEFORE UPDATE ON `tr_finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT operater from frmgk_troskovi where brnal=replace(new.brnal,'TR-','') and NOT (operater=@aktivnioperater) LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT PRIPADA DRUGOM OPERATERU. PREUZMITE DOKUMENT FUNKCIJOM 'PREUZMI DOKUMENT' U ZAGLAVLJU!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
  IF isnull(@knjizenjeutoku) and isnull(@pecav) then
    SET @w=(SELECT status from frmgk_troskovi where brnal=replace(new.brnal,'TR-','') and status>1 LIMIT 1);
    if not isnull(@w) then
      set msg = "##ODP##DOKUMENT JE U MEĐUVREMENU PROKNJIEN OD STRANE DRUGOG OPERATERA!";
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
    END IF;
  END IF;
end
```

---

## 244. updartikli

**Tabela:** `artikli` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updartikli` AFTER UPDATE ON `artikli` FOR EACH ROW begin
  update trstanje set trstanje.naziv=NEW.naziv,trstanje.jedmere=NEW.jedmere,trstanje.porez=NEW.porez,trstanje.tarbr=NEW.tarbr,trstanje.barkod=NEW.barkod,trstanje.kasakoef=NEW.kasakoef,trstanje.taksa=NEW.taksa,trstanje.akciza=NEW.akciza where trstanje.sifra=NEW.sifra;
  
end
```

---

## 245. updfakture

**Tabela:** `fakture` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updfakture` AFTER UPDATE ON `fakture` FOR EACH ROW begin
  set @s=(select sum(kolicina) from fakture force index (ind11) where sifobj=NEW.sifobj and sifra=NEW.sifra and (tip='P' or tip='I' or tip='X' or tip='B' or tip='Y' or tip='E') and status=2); 
  if isnull(@s) then 
    set @s=0;
  end if;  
  insert into trstanje set sifobj=NEW.sifobj, sifra=NEW.sifra,stanje=0,neprokkasa=0,refobjst=0,rezervacije=@s on duplicate key update rezervacije=@s; 
  if not isnull(@refobjekat) and not (trim(@refobjekat)='') then   
      set @mynewferobj=null;
      select refobj into @mynewferobj from objekti where sifra=NEW.sifobj;
      if not isnull(@mynewferobj) and not (trim(@mynewferobj)='') then   
        set @wref=(select if(isnull(stanje),0,stanje)-if(isnull(neprokkasa),0,neprokkasa)-if(isnull(rezervacije),0,rezervacije) from trstanje where sifobj=NEW.sifobj and sifra=NEW.sifra);
        if isnull(@wref) then
          set @wref = 0;
        end if;
        insert into trstanje SET sifobj=@mynewferobj, sifra=NEW.sifra,  stanje=0, neprokkasa=0, rezervacije=0, refobjst=@wref*-1 on DUPLICATE KEY UPDATE refobjst=@wref*-1;
        update trstanje set refobjst=@wref where sifobj=NEW.sifobj and sifra=NEW.sifra;
```

---

## 246. updkasa

**Tabela:** `kasa` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updkasa` AFTER UPDATE ON `kasa` FOR EACH ROW begin
   set @w=(select sum(kolicina*kasakoef) from kasa,artikli where kasa.sifra=artikli.sifra and kasa.sifobj=NEW.sifobj and kasa.sifra=NEW.sifra and status=99 and tipracuna=0);
   if isnull(@w) then
     set @w=0;
   end if;   
   insert into trstanje set sifobj=NEW.sifobj, sifra=NEW.sifra,stanje=0,rezervacije=0,refobjst=0,neprokkasa=@w on duplicate key update neprokkasa=@w;       
   if not isnull(@refobjekat) and not (trim(@refobjekat)='') then    
     set @mynewferobj=null;
```

---

## 247. updosamvr

**Tabela:** `osamvr` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updosamvr` AFTER UPDATE ON `osamvr` FOR EACH ROW BEGIN
  IF old.tipam='K' then
    DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datam and brnal=CONCAT('AMSS-',date_format(OLD.datam, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbramort*100+OLD.rbr),3));
  END IF;
  IF NEW.tipam='K' then
    INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datam, CONCAT('AMSS-',date_format(datam, '%y%m%d'), '-', RIGHT(CONCAT('000',rbramort*100+OLD.rbr),3)), 4, 0, 0, (amvr*komada), 0, 0, opis, null, 0 FROM osamvr WHERE tipam='K' AND osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datam=NEW.datam and rbr=NEW.rbr AND rbramort=NEW.rbramort AND rbr=OLD.rbr;
  END IF;
  
end
```

---

## 248. updosnabvr

**Tabela:** `osnabvr` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updosnabvr` AFTER UPDATE ON `osnabvr` FOR EACH ROW BEGIN
  DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datnab and brnal=CONCAT('NBSS-',date_format(OLD.datnab, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbr),3));
  INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datnab, CONCAT('NBSS-',date_format(datnab, '%y%m%d'), '-', RIGHT(CONCAT('000',rbr),3)), IF(tipnab='0',0,IF(tipnab='1',1,IF(tipnab='2',2,IF(tipnab='3',3,4)))), IF(tipnab='2',0, komada), IF(tipnab='2',nabvr, nabvr*komada), IF(tipnab='2',amvr, amvr*komada), 0, 0, nazdob, datsadvr, (rzdvr*komada) FROM osnabvr WHERE osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datnab=NEW.datnab and rbr=NEW.rbr;
  
end
```

---

## 249. updosotpis

**Tabela:** `osotpis` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updosotpis` AFTER UPDATE ON `osotpis` FOR EACH ROW BEGIN
  DELETE from oskaros WHERE osoznaka=old.osoznaka AND invbroj=old.invbroj and datum=old.datotp and brnal=CONCAT('OTSS-',date_format(OLD.datotp, '%y%m%d'), '-', RIGHT(CONCAT('000',OLD.rbr),3));
  INSERT IGNORE into oskaros SELECT osoznaka, invbroj, datotp, CONCAT('OTSS-',date_format(datotp, '%y%m%d'), '-', RIGHT(CONCAT('000',rbr),3)), 5, (komada * -1), 0, 0, 0, (iznotp * komada), opis, NULL, 0 FROM osotpis WHERE osoznaka=NEW.osoznaka AND invbroj=NEW.invbroj and datotp=NEW.datotp and rbr=NEW.rbr;
  
end
```

---

## 250. updstanje

**Tabela:** `robno` | **Timing:** AFTER UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `updstanje` AFTER UPDATE ON `robno` FOR EACH ROW begin
 if (not (@NEAZURIRAJROBNO=1133)) or (isnull(@NEAZURIRAJROBNO)) then
  insert ignore into trstanje set sifobj=NEW.sifobj,sifra=NEW.sifra,faktcena=NEW.cena,nabcena=NEW.nabcena,vpcena=NEW.cenabezpp,mpcena=NEW.cenasapp,stanje=0,neprokkasa=0,rezervacije=0,refobjst=0;
  update trstanje,artikli set trstanje.naziv=artikli.naziv,trstanje.jedmere=artikli.jedmere,trstanje.porez=artikli.porez,trstanje.tarbr=artikli.tarbr,trstanje.barkod=artikli.barkod,trstanje.kasakoef=artikli.kasakoef,trstanje.taksa=artikli.taksa,trstanje.akciza=artikli.akciza where trstanje.sifra=artikli.sifra and trstanje.sifra=NEW.sifra  and trstanje.sifobj=NEW.sifobj;
  set @st=(select sum(ulaz-izlaz) from robno where sifobj=NEW.sifobj and sifra=NEW.sifra and stornirano=0);
  if isnull(@st) then
    set @st=0;
  end if;
  update trstanje set stanje=@st, refobjst=0 where sifobj=NEW.sifobj and sifra=NEW.sifra;
  if not isnull(@refobjekat) and not (trim(@refobjekat)='') then   
    set @mynewferobj=null;
    select refobj into @mynewferobj from objekti where sifra=NEW.sifobj;
    if not isnull(@mynewferobj) and not (trim(@mynewferobj)='') then   
      set @wref=(select if(isnull(stanje),0,stanje)-if(isnull(neprokkasa),0,neprokkasa)-if(isnull(rezervacije),0,rezervacije) from trstanje where sifobj=NEW.sifobj and sifra=NEW.sifra);
      if isnull(@wref) then
        set @wref = 0;
      end if;
      insert into trstanje SET sifobj=@mynewferobj, sifra=NEW.sifra,  stanje=0, neprokkasa=0, rezervacije=0, refobjst=@wref*-1 on DUPLICATE KEY UPDATE refobjst=@wref*-1;
      update trstanje set refobjst=@wref where sifobj=NEW.sifobj and sifra=NEW.sifra;
```

---

## 251. zak_del_finprom

**Tabela:** `finprom` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_del_finprom` BEFORE DELETE ON `finprom` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKFINDAT=(select finansijsko from zakljucano limit 1); 
    IF not (ISNULL(@BSZKFINDAT)) THEN
      IF not (@BSZKFINDAT<old.datnal) then
        set msg = "##ZAK##FINANSIJSKO POSLOVANJE: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 252. zak_del_pk1

**Tabela:** `pk1` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_del_pk1` BEFORE DELETE ON `pk1` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKPK1DAT=(select pk1 from zakljucano limit 1);  
    IF not (ISNULL(@BSZKPK1DAT)) THEN
      IF not (@BSZKPK1DAT<old.datknj) then
        set msg = "##ZAK##PK1 KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 253. zak_del_popdv_promet

**Tabela:** `popdv_promet` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_del_popdv_promet` BEFORE DELETE ON `popdv_promet` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKPDVDAT=(select kir from zakljucano limit 1);  
    IF not (ISNULL(@BSZKPDVDAT)) THEN
      IF not (@BSZKPDVDAT<old.datpdv) then
        set msg = "##ZAK##PORESKA EVIDENCIJA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 254. zak_del_robno

**Tabela:** `robno` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_del_robno` BEFORE DELETE ON `robno` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  if not (@NEAZURIRAJROBNO=1133) then
    set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta);  
    IF not (ISNULL(@BSZKROBDAT)) THEN
      IF not (@BSZKROBDAT<old.datum) then
        set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;

    if @sifraobjekta2>-1 then
      set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKROBDAT)) THEN
        IF not (@BSZKROBDAT<old.datum) then
          set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
  end if;
end
```

---

## 255. zak_del_trgovacka

**Tabela:** `trgovacka` | **Timing:** BEFORE DELETE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_del_trgovacka` BEFORE DELETE ON `trgovacka` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta);  
    IF not (ISNULL(@BSZKKEPDAT)) THEN
      IF not (@BSZKKEPDAT<old.datum) then
        set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;

    if @sifraobjekta2>-1 then
      set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKKEPDAT)) THEN
        IF not (@BSZKKEPDAT<old.datum) then
          set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
end
```

---

## 256. zak_ins_finprom

**Tabela:** `finprom` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_ins_finprom` BEFORE INSERT ON `finprom` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKFINDAT=(select finansijsko from zakljucano limit 1);  
    IF not (ISNULL(@BSZKFINDAT)) THEN
      IF not (@BSZKFINDAT<new.datnal) then
        set msg = "##ZAK##FINANSIJSKO POSLOVANJE: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 257. zak_ins_pk1

**Tabela:** `pk1` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_ins_pk1` BEFORE INSERT ON `pk1` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKPK1DAT=(select pk1 from zakljucano limit 1);  
    IF not (ISNULL(@BSZKPK1DAT)) THEN
      IF not (@BSZKPK1DAT<new.datknj) then
        set msg = "##ZAK##PK1 KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 258. zak_ins_popdv_promet

**Tabela:** `popdv_promet` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_ins_popdv_promet` BEFORE INSERT ON `popdv_promet` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKPDVDAT=(select kir from zakljucano limit 1);  
    IF not (ISNULL(@BSZKPDVDAT)) THEN
      IF not (@BSZKPDVDAT<new.datpdv) then
        set msg = "##ZAK##PORESKA EVIDENCIJA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 259. zak_ins_robno

**Tabela:** `robno` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_ins_robno` BEFORE INSERT ON `robno` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  if not (@NEAZURIRAJROBNO=1133) then
    set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta);  
    IF not (ISNULL(@BSZKROBDAT)) THEN
      IF not (@BSZKROBDAT<new.datum) then
        set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;

    if @sifraobjekta2>-1 then
      set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKROBDAT)) THEN
        IF not (@BSZKROBDAT<new.datum) then
          set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
  end if;
end
```

---

## 260. zak_ins_trgovacka

**Tabela:** `trgovacka` | **Timing:** BEFORE INSERT

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_ins_trgovacka` BEFORE INSERT ON `trgovacka` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta);  
    IF not (ISNULL(@BSZKKEPDAT)) THEN
      IF not (@BSZKKEPDAT<new.datum) then
        set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;

    if @sifraobjekta2>-1 then
      set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKKEPDAT)) THEN
        IF not (@BSZKKEPDAT<new.datum) then
          set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
end
```

---

## 261. zak_upd_finprom

**Tabela:** `finprom` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_upd_finprom` BEFORE UPDATE ON `finprom` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  if isnull(@neprovzakfin) then
    set @BSZKFINDAT=(select finansijsko from zakljucano limit 1); 
    IF not (ISNULL(@BSZKFINDAT)) THEN
      IF not (@BSZKFINDAT<old.datnal) then
        set msg = "##ZAK##FINANSIJSKO POSLOVANJE: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
  END IF;
end
```

---

## 262. zak_upd_pk1

**Tabela:** `pk1` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_upd_pk1` BEFORE UPDATE ON `pk1` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKPK1DAT=(select pk1 from zakljucano limit 1);  
    IF not (ISNULL(@BSZKPK1DAT)) THEN
      IF not (@BSZKPK1DAT<old.datknj) then
        set msg = "##ZAK##PK1 KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;
end
```

---

## 263. zak_upd_popdv_promet

**Tabela:** `popdv_promet` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_upd_popdv_promet` BEFORE UPDATE ON `popdv_promet` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    if not (@ignorisizakljucano=1) then
      set @BSZKPDVDAT=(select kir from zakljucano limit 1);  
      IF not (ISNULL(@BSZKPDVDAT)) THEN
        IF not (@BSZKPDVDAT<old.datpdv) then
          set msg = "##ZAK##PORESKA EVIDENCIJA: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
end
```

---

## 264. zak_upd_robno

**Tabela:** `robno` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_upd_robno` BEFORE UPDATE ON `robno` FOR EACH ROW begin
  DECLARE msg VARCHAR(255);
  if not (@NEAZURIRAJROBNO=1133) then
    if isnull(@NEAZURIRAJROBNO) then
      set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta);  
      IF not (ISNULL(@BSZKROBDAT)) THEN
        IF not (@BSZKROBDAT<old.datum) then
          set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;

    if @sifraobjekta2>-1 then
      set @BSZKROBDAT=(select datzakrobno from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKROBDAT)) THEN
        IF not (@BSZKROBDAT<old.datum) then
          set msg = "##ZAK##ROBNO KNJIGOVODSTVO: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
  end if;
end
```

---

## 265. zak_upd_trgovacka

**Tabela:** `trgovacka` | **Timing:** BEFORE UPDATE

```sql
CREATE DEFINER=`root`@`localhost` TRIGGER `zak_upd_trgovacka` BEFORE UPDATE ON `trgovacka` FOR EACH ROW begin
    DECLARE msg VARCHAR(255);
    set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta);  
    IF not (ISNULL(@BSZKKEPDAT)) THEN
      IF not (@BSZKKEPDAT<old.datum) then
        set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
      END IF;
    END IF;

    if @sifraobjekta2>-1 then
      set @BSZKKEPDAT=(select datzaktrgk from objekti where sifra=@sifraobjekta2);  
      IF not (ISNULL(@BSZKKEPDAT)) THEN
        IF not (@BSZKKEPDAT<old.datum) then
          set msg = "##ZAK##KEPU KNJIGA: Period knjiženja je zaključan!";
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = msg;
        END IF;
      END IF;
    end if;
end
```

---

