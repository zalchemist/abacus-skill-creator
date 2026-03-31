# Biznisoft ERP - Stored Procedures

**Baza:** `opp7102025`
**Ukupno procedura:** 105
**Datum izvlačenja:** 2026-03-29

---

## Sadržaj

1. [AktuelizujCenovnik](#aktuelizujcenovnik)
2. [AutCheckMinzal](#autcheckminzal)
3. [automatskoHelper](#automatskohelper)
4. [AzurRnPartKli](#azurrnpartkli)
5. [BojiAkcije](#bojiakcije)
6. [bsnotif](#bsnotif)
7. [CheckAkcije](#checkakcije)
8. [checkdokpary](#checkdokpary)
9. [checkForeignKeys](#checkforeignkeys)
10. [CheckLDRN](#checkldrn)
11. [CheckPrometPoSifri](#checkprometposifri)
12. [CheckTabRnPog](#checktabrnpog)
13. [CheckTabRnPogAMT](#checktabrnpogamt)
14. [checkvpcenovnik](#checkvpcenovnik)
15. [create_tmp_tmp_rek](#create_tmp_tmp_rek)
16. [creeeopdvp](#creeeopdvp)
17. [creeeopdv_pz](#creeeopdv_pz)
18. [creeeppdvp](#creeeppdvp)
19. [CreTmpSerbr](#cretmpserbr)
20. [cre_pregled_eeppdv](#cre_pregled_eeppdv)
21. [cre_tmp_pojedinacna](#cre_tmp_pojedinacna)
22. [dajmidokumente](#dajmidokumente)
23. [DaLiJeUAvansuOPP](#dalijeuavansuopp)
24. [DeleteInvoiceRecords](#deleteinvoicerecords)
25. [dododatrsub](#dododatrsub)
26. [dopuni_pregled_eeppdv](#dopuni_pregled_eeppdv)
27. [DoWriteLocation](#dowritelocation)
28. [eeopdvp](#eeopdvp)
29. [eeopdvspec](#eeopdvspec)
30. [eeppdvp](#eeppdvp)
31. [eo_fix_auto_increment](#eo_fix_auto_increment)
32. [fifoPricePST](#fifopricepst)
33. [fifoPricePSTAll](#fifopricepstall)
34. [fifo_calc](#fifo_calc)
35. [fifo_calc_prerNC](#fifo_calc_prernc)
36. [formirajEEOPDVP](#formirajeeopdvp)
37. [FormirajVeznu](#formirajveznu)
38. [GetEEPAnalytics](#geteepanalytics)
39. [getEvidencijaStorno](#getevidencijastorno)
40. [GetNabCena](#getnabcena)
41. [GetNextBrNal](#getnextbrnal)
42. [ios](#ios)
43. [KnjiziTransformaciju](#knjizitransformaciju)
44. [kreirajPopis](#kreirajpopis)
45. [KreirajTabeleZaStorno](#kreirajtabelezastorno)
46. [KreirajTmpTabele](#kreirajtmptabele)
47. [labelsInsert](#labelsinsert)
48. [lastRabatI](#lastrabati)
49. [lastRabatU](#lastrabatu)
50. [myprenos1](#myprenos1)
51. [NalogPrerNc](#nalogprernc)
52. [NalogPrerNcGK](#nalogprerncgk)
53. [NalogPrerNCRobno](#nalogprerncrobno)
54. [obojiavanse](#obojiavanse)
55. [obracunPotvrdjeno](#obracunpotvrdjeno)
56. [obracunRazlikeUCeni](#obracunrazlikeuceni)
57. [OtvaranjeNoveGodine](#otvaranjenovegodine)
58. [oznakasef](#oznakasef)
59. [prenesiSveArtikle](#prenesisveartikle)
60. [PrenosSifarnika](#prenossifarnika)
61. [PrepareEEPPDVData](#prepareeeppdvdata)
62. [PrepareZaSveArtikle](#preparezasveartikle)
63. [PreracunajNC](#preracunajnc)
64. [pripremitabele](#pripremitabele)
65. [ProveraIntegriteta](#proveraintegriteta)
66. [ProveraStatusa](#proverastatusa)
67. [ProvRezervacije](#provrezervacije)
68. [pr_doeeppdv](#pr_doeeppdv)
69. [punitabelu](#punitabelu)
70. [puniTmpZbirnu](#punitmpzbirnu)
71. [punitmpzbirnusimulacija](#punitmpzbirnusimulacija)
72. [racunajKolicine](#racunajkolicine)
73. [RekapitulacijaPDV](#rekapitulacijapdv)
74. [RezNarTrb](#reznartrb)
75. [sefknjizenjanew](#sefknjizenjanew)
76. [sefknjizenjaold](#sefknjizenjaold)
77. [SpremiZaSimulaciju1](#spremizasimulaciju1)
78. [SpremiZaSimulaciju2](#spremizasimulaciju2)
79. [SpremiZaSimulaciju3](#spremizasimulaciju3)
80. [SrediAmortizaciju](#srediamortizaciju)
81. [SrediSpecSerbr](#sredispecserbr)
82. [SrediTmpFinprom](#sreditmpfinprom)
83. [SrediTmpPopdvPromet](#sreditmppopdvpromet)
84. [SrediTmpRobno](#sreditmprobno)
85. [SrediTmpTrgovacka](#sreditmptrgovacka)
86. [SrediTmp_eeopdv_pojedinacna](#sreditmp_eeopdv_pojedinacna)
87. [SrediTmp_eeopdv_zbirna](#sreditmp_eeopdv_zbirna)
88. [SrediTmp_eeppdv_promet](#sreditmp_eeppdv_promet)
89. [starostzaliha](#starostzaliha)
90. [stats4art](#stats4art)
91. [stats4artgraph](#stats4artgraph)
92. [stats4kont](#stats4kont)
93. [stats4kontgraph](#stats4kontgraph)
94. [stats4part](#stats4part)
95. [stats4partgraph](#stats4partgraph)
96. [statskart](#statskart)
97. [StornirajKnjizenja](#stornirajknjizenja)
98. [StornirajKnjizenja3](#stornirajknjizenja3)
99. [StornirajKnjizenjaNaDan](#stornirajknjizenjanadan)
100. [trigoperdoc](#trigoperdoc)
101. [trigoperdocx](#trigoperdocx)
102. [WriteLocation](#writelocation)
103. [xtrstanje](#xtrstanje)
104. [xtrstanjesql](#xtrstanjesql)
105. [ZbirnoPoDokumentu](#zbirnopodokumentu)

---

## 1. AktuelizujCenovnik

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `AktuelizujCenovnik`()
BEGIN
  
  insert into cenovnik select pricelists_detail.sifra, pricelists_detail.sifobj, pricelists_detail.mpcena, now(), 'BIZNISOFT', pricelists_detail.vpcena from pricelists_detail, pricelists 
    where pricelists_detail.plid=pricelists.plid and pricelists.status=1 and pricelists_detail.tip=1 and pricelists.stupanasnagu<now() on DUPLICATE key update cenovnik.mpcena=pricelists_detail.mpcena, cenovnik.ts=now(), operater='BIZNISOFT', cenovnik.vpcena=pricelists_detail.vpcena;
  
 insert into cenovnik select pricelists_detail.sifra, grupeobjekticenovnik.objekat, pricelists_detail.mpcena, now(), 'BIZNISOFT', pricelists_detail.vpcena from pricelists_detail, pricelists, grupeobjekticenovnik 
     where pricelists_detail.plid=pricelists.plid and pricelists.status=1 and pricelists_detail.tip=0 and pricelists_detail.sifgrpobj=grupeobjekticenovnik.grupa and pricelists.stupanasnagu<now() on DUPLICATE key update cenovnik.mpcena=pricelists_detail.mpcena, cenovnik.ts=now(), operater='BIZNISOFT', cenovnik.vpcena=pricelists_detail.vpcena;

  insert into logpotvrdi select UUID(), if(@aktivnioperater='' or isnull(@aktivnioperater), 'BIZNISOFT',@aktivnioperater), plid, now(), 2 from pricelists where status=1 and pricelists.stupanasnagu<now();

  update pricelists set status=2 where status=1 and pricelists.stupanasnagu<now();
END
```

---

## 2. AutCheckMinzal

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `AutCheckMinzal`()
BEGIN
  DECLARE s_operater varchar(50);
  DECLARE exit_loop boolean;
  DECLARE coperateri CURSOR FOR SELECT korime from minzalnotif;
  declare continue handler for not found set exit_loop = true;

  SELECT bsliveid INTO @bsliveid from mybsliveid LIMIT 1;
  SELECT sifrafirme INTO @sifrafirme from mybsliveid LIMIT 1;

  SELECT CONCAT(GROUP_CONCAT(sifra SEPARATOR ',')) INTO @mybsporuka1 FROM (select nivozaliha.*,artikli.naziv as nazivaartikla, artikli.barkod, artikli.katbr, objekti.naziv as nazivobjekta, robno.ulaz, robno.izlaz, trstanje.neprokkasa, trstanje.rezervacije,
    tblnardobavljacima.kolicina, tblnardobavljacima.realizovano, tblnardobavljacima.potvrdjeno, (sum(robno.ulaz)-sum(robno.izlaz)-neprokkasa-rezervacije+(IF(ISNULL(kolicina), 0, kolicina)-IF(ISNULL(realizovano), 0, realizovano))) as srobno
    from nivozaliha
     left join artikli on
      nivozaliha.sifra=artikli.sifra
     left join objekti on
      nivozaliha.sifobj=objekti.sifra
     left join robno on
      artikli.sifra=robno.sifra and nivozaliha.sifra=robno.sifra
     left join tblnardobavljacima on
      nivozaliha.sifra=tblnardobavljacima.sifra and nivozaliha.sifobj=tblnardobavljacima.sifobj  and tblnardobavljacima.status>1 and tblnardobavljacima.statuszat=1, trstanje
     where  
      iminzal>=0 and nivozaliha.sifobj=robno.sifobj and robno.sifobj=trstanje.sifobj and robno.sifra=trstanje.sifra and robno.sifra=artikli.sifra  and robno.datum<=DATE(NOW())
        and (IF(isnull(nivozaliha.sifobj), 1, robno.sifobj=nivozaliha.sifobj)) and ((artikli.jeambalaza=0 and artikli.jeusluga=0 and artikli.komision880=0 and artikli.jeproizvod=0
        and artikli.jesirovina=0)  or (artikli.jeproizvod=1)  or (artikli.jesirovina=1)  or (artikli.komision880=1) ) group by robno.sifra having srobno<iminzal  order by  artikli.sifra ASC, nivozaliha.sifobj) AS mss;

  IF NOT ISNULL(@mybsporuka1) THEN
    OPEN coperateri;
    set exit_loop = false;
    operateri_loop:
      LOOP FETCH coperateri INTO s_operater;
      IF exit_loop THEN
        LEAVE operateri_loop;
      END IF;
   
      IF not (TRIM(@mybsporuka1)='') AND NOT ISNULL(@mybsporuka1) THEN
        CALL bsnotif(@bsliveid,s_operater,CONCAT('Provera minimalnih zaliha: Minimalne zalihe su prekoračene za šifre: ','\n',@mybsporuka1), true, 10027, @sifrafirme);
      END IF;
 
    END LOOP operateri_loop;
    CLOSE coperateri;
  END IF;
END
```

---

## 3. automatskoHelper

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `automatskoHelper`(atributiTag int(1), sifObj int(2), SS1sifObj int(3), SS1brkalk int(6), tag int(1))
BEGIN

  IF tag = 1 THEN
    DROP TEMPORARY TABLE IF EXISTS tmp_exclude;
    CREATE TEMPORARY TABLE tmp_exclude (sifra int(6) NOT NULL PRIMARY KEY);
    IF atributiTag = 1 THEN
      INSERT INTO tmp_exclude SELECT artikli.sifra FROM trstanje, artikli, atributiartikli, myatributi_osim
      WHERE trstanje.sifra = artikli.sifra AND trstanje.sifobj = sifObj AND (mpcena <> 0 OR vpcena <> 0)
      AND atributiartikli.atribut = myatributi_osim.sifra AND atributiartikli.sifra = trstanje.sifra AND
      assigned = 1 and checked = 1 GROUP BY artikli.sifra ORDER BY artikli.sifra; 
    ELSE
      DROP TEMPORARY TABLE IF EXISTS my_atributi1_osim;
      CREATE TEMPORARY TABLE myatributi1_osim LIKE myatributi_osim;
      INSERT INTO myatributi1_osim SELECT * FROM myatributi1_osim WHERE checked = 1;
      DROP TEMPORARY TABLE IF EXISTS my_atributi2_osim;
      CREATE TEMPORARY TABLE myatributi2_osim LIKE myatributi_osim;
      INSERT INTO myatributi2_osim SELECT * FROM myatributi_osim WHERE checked = 1;
      INSERT INTO tmp_exclude SELECT artikli.sifra FROM trstanje, artikli, atributiartikli, myatributi_osim
      WHERE trstanje.sifra = artikli.sifra AND trstanje.sifobj = sifObj AND (mpcena <> 0 OR vpcena <> 0) AND
      atributiartikli.atribut = myatributi_osim.sifra AND atributiartikli.sifra = trstanje.sifra AND assigned = 1
      AND checked = 1 AND (SELECT COUNT(*) FROM atributiartikli, my_atributi1_osim WHERE atributiartikli.sifra =
      trstanje.sifra AND atributiartikli.atribut = myatributi1_osim.sifra AND myatributi11_osim.checked = 1
      AND assigned = 1) = (SELECT COUNT(*) FROM myatributi2_osim WHERE checked = 1) GROUP BY artikli.sifra
      ORDER BY artikli.sifra;             
    END IF;
  ELSEIF tag = 2 THEN
    DROP TEMPORARY TABLE IF EXISTS myAtributi1;
    CREATE TEMPORARY TABLE myatributi1 LIKE myatributi;
    INSERT INTO myatributi1 SELECT * FROM myatributi WHERE checked = 1;
    DROP TEMPORARY TABLE IF EXISTS myatributi2;
    CREATE TEMPORARY TABLE myatributi2 LIKE myatributi;
    INSERT INTO myatributi2 SELECT * FROM myatributi WHERE checked = 1;
  ELSEIF tag = 3 THEN
    ALTER TABLE tmptbltrebovanje DROP PRIMARY KEY;
    INSERT INTO tmptbltrebovanje SELECT * FROM tbltrebovanje WHERE tbltrebovanje.sifobj = SS1sifObj
    AND brkalk = SS1brkalk ORDER BY sifra, grpobj;
    DELETE FROM tbltrebovanje WHERE tbltrebovanje.sifobj = SS1sifObj AND brkalk = SS1brkalk;
    ALTER TABLE tmptbltrebovanje ORDER BY sifra, grpobj;
    ALTER TABLE tmptbltrebovanje ADD myxrbrst int(6) NOT NULL PRIMARY KEY AUTO_INCREMENT;
    UPDATE tmptbltrebovanje SET rbrst = myxrbrst;
    ALTER TABLE tmptbltrebovanje DROP myxrbrst;
    INSERT INTO tbltrebovanje SELECT * FROM tmptbltrebovanje;
    DROP TEMPORARY TABLE tmptbltrebovanje;
  END IF;
END
```

---

## 4. AzurRnPartKli

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `AzurRnPartKli`(`sifkli` integer, `sifra` integer)
BEGIN
   SET @aa=CONCAT('insert ignore into ',@bsliveid,'opp.rnpartnkli select ',sifkli,',  concat(left(conbrtekrn,3),lpad(mid(conbrtekrn,4,length(conbrtekrn)-5),13,''0''), right(conbrtekrn,2)), concat(''P-'',lpad(fgk.sifra,5,''0'')), naziv, date(now()), date(now()), @aktivnioperater ',
     'from (select kupci.sifra,naziv,mesto,racuni.brtekrn,replace(racuni.brtekrn,''-'','''') as conbrtekrn from kupci, (select * from pospracuni where (pospracuni.status=1 or pospracuni.status=9) order by pospracuni.status desc) as racuni where kupci.sifra=racuni.sifra) as fgk where sifra=', sifra);
   PREPARE stmt FROM @aa; EXECUTE stmt;
END
```

---

## 5. BojiAkcije

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `BojiAkcije`(`objekat` int)
BEGIN
  drop temporary table if exists tmp_bojiakcije;
  create temporary table tmp_bojiakcije (tipakc int(1) not null, sifra int(6) not null, ubuducnosti int(1) default 0, primary key(tipakc,sifra));
  insert ignore into tmp_bojiakcije select tipakc,artikal, 0 from akcije where (periodod<=now() or isnull(periodod)) and (perioddo>=now() or isnull(perioddo)) and aktivna=1 and tipakc<>3 and not isnull(artikal) and (sifobj=objekat or isnull(sifobj) or objekat=-1) group by tipakc,artikal;
  insert ignore into tmp_bojiakcije select tipakc,atributiartikli.sifra, 0 from akcije,atributiartikli where (periodod<=now() or isnull(periodod)) and (perioddo>=now() or isnull(perioddo)) and aktivna=1 and tipakc<>3 and not isnull(akcije.atribut) and (sifobj=objekat or isnull(sifobj) or objekat=-1)
    and akcije.atribut=atributiartikli.atribut and atributiartikli.assigned=1 group by atributiartikli.sifra, tipakc;
  insert ignore into tmp_bojiakcije select tipakc,artikal, 1 from akcije where (periodod>now()) and aktivna=1 and tipakc<>3 and not isnull(artikal) and (sifobj=objekat or isnull(sifobj) or objekat=-1) group by tipakc,artikal;
  insert ignore into tmp_bojiakcije select tipakc,atributiartikli.sifra, 1 from akcije,atributiartikli where (periodod>now()) and aktivna=1 and tipakc<>3 and not isnull(akcije.atribut) and (sifobj=objekat or isnull(sifobj) or objekat=-1)
    and akcije.atribut=atributiartikli.atribut and atributiartikli.assigned=1 group by atributiartikli.sifra, tipakc;
END
```

---

## 6. bsnotif

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `bsnotif`(bsliveid varchar(50), myoperater varchar(50), msg varchar(1000), checkdate bool, mytippor int, mysifrafirme int)
BEGIN
  SET @icountnotif := 0;
  IF checkdate THEN
    SET @qvr=concat('SELECT COUNT(*) INTO @icountnotif FROM ',bsliveid,'opp.bsnotif WHERE tipporuke=',mytippor,' and operater2="',myoperater,'" and DATE(vremeslanja)=DATE(NOW())');
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;
  END IF;
  IF @icountnotif=0 THEN
    SET @qvr=concat('INSERT INTO ',bsliveid,'opp.bsnotif SET operater="BizniSoft", operater2="',myoperater,'", mssg="',msg,'", vremeslanja=NOW(), sendertype=1, tipporuke=',mytippor,', zafirmu=', mysifrafirme);
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;   
  END IF;
END
```

---

## 7. CheckAkcije

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckAkcije`(p_sifobj INT, p_sifra INT, p_mydate DATETIME)
BEGIN
  DECLARE max_priority INT DEFAULT -1;
  DECLARE priority INT;
  DECLARE price DOUBLE;
  DECLARE name VARCHAR(255);
  DECLARE done BOOL DEFAULT FALSE;

  DECLARE c_sifobj INT;
  DECLARE c_artikal INT;
  DECLARE c_atribut INT;
  DECLARE c_bezakcije INT;
  DECLARE c_prioritet INT;
  DECLARE c_cena DOUBLE;
  DECLARE c_naziv VARCHAR(255);

  DECLARE cur CURSOR FOR
    SELECT sifobj, artikal, atribut, bezakcije, prioritet, cenasapdv, nazivakcije
      FROM akcije
     WHERE aktivna = 1
       AND tipakc = 2
       AND ((periodod <= p_mydate OR periodod IS NULL) AND (perioddo >= p_mydate OR perioddo IS NULL))
       AND ((vremeod IS NOT NULL AND vremedo IS NOT NULL
             AND (IF(vremeod < vremedo, TIME(p_mydate) BETWEEN vremeod AND vremedo, TIME(p_mydate) < vremedo OR TIME(p_mydate) > vremeod)))
             OR (vremeod IS NULL AND vremedo IS NULL))
       AND (sifobj  = p_sifobj OR sifobj  IS NULL)
       AND (artikal = p_sifra OR artikal IS NULL)
       AND IF(atribut IS NULL, 1, (SELECT sifra FROM atributiartikli WHERE assigned = 1 AND sifra = p_sifra AND atribut = akcije.atribut))
       and cenasapdv<>0 and not isnull(cenasapdv)
     ORDER BY myid DESC;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  SET @akcijskacena = 0;
  SET @nazivakcije = null;

  OPEN cur;
  read_loop: LOOP
    FETCH cur INTO
      c_sifobj,
      c_artikal,
      c_atribut,
      c_bezakcije,
      c_prioritet,
      c_cena,
      c_naziv;

    IF done THEN
      LEAVE read_loop;
    END IF;

    SET priority = -1;

    IF c_sifobj IS NOT NULL AND c_artikal IS NOT NULL THEN
      SET priority = 30;
    ELSEIF c_sifobj IS NOT NULL
          AND c_artikal IS NULL
          AND c_atribut IS NOT NULL THEN
      SET priority = 29;
    ELSEIF c_sifobj IS NULL
          AND c_artikal IS NOT NULL
          AND c_atribut IS NULL THEN
      SET priority = 28;
    ELSEIF c_sifobj IS NULL
          AND c_artikal IS NULL
          AND c_atribut IS NOT NULL THEN
      SET priority = 27;
    END IF;

    IF c_bezakcije = 1 THEN
      SET priority = 999;
    END IF;

    IF c_prioritet IS NOT NULL AND c_prioritet > 0 THEN
      SET priority = c_prioritet;
    END IF;

    IF priority >= max_priority THEN
      SET max_priority = priority;
      SET price = c_cena;
      SET name = c_naziv;
    END IF;
  END LOOP;
  CLOSE cur;

  SET @akcijskacena = price;
  SET @nazivakcije = name;
END
```

---

## 8. checkdokpary

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `checkdokpary`(tipprovere int(1), nazivtabele varchar(50), brrn int(6), brojdokumenta varchar(50), partner int(6), ulaz_tipdokfakt varchar(2))
BEGIN
  DECLARE s_tabela,s_naziv, s_tipdokfakt varchar(255);
  DECLARE exit_loop boolean;
  DECLARE s_tipkljuca, i integer;
  DECLARE uslovbrrn varchar(255);
  DECLARE nazivbroja varchar(50);
  DECLARE nazivpartnera varchar(50);
  DECLARE nazivpartnerafintrans varchar(50);
  DECLARE nazivtabelefintrans varchar(50);
  DECLARE nazivfunkcijefintrans varchar(50);
  DECLARE dokumenti CURSOR FOR SELECT tabela,naziv,tipkljuca,tipdokfakt FROM tmp_tbl_documents;
  declare continue handler for not found set exit_loop = TRUE;

  SET @provdokgreska = '';
  SET @provdokobjekat = '';
  SET @provdokbrdok = '';
  
  IF TRIM(brojdokumenta)='' THEN
    set tipprovere := 3;
  END IF;

  IF tipprovere=1 THEN
    if nazivtabele='frmgk_avans' then
      SET nazivbroja := 'brnal';
      set nazivpartnera := 'dobavljac';
      set nazivpartnerafintrans := 'dobavljac';
      set nazivtabelefintrans := 'frmgk_avans';
      SET nazivfunkcijefintrans := 'PRIJEM AVANSNOG RAČUNA';
    else
      SET nazivbroja := 'brkalk';
      set nazivpartnera := 'dobavljac';
      set nazivpartnerafintrans := 'dobavljac';
      set nazivtabelefintrans := 'frmgk_troskovi';
      SET nazivfunkcijefintrans := 'RAČUN TROŠKOVA';
    end if;
  END IF;

  IF tipprovere=2 THEN
    SET nazivbroja := 'brrn';
    set nazivpartnera := 'sifkup'; 
    set nazivpartnerafintrans := 'kupac'; 
    set nazivtabelefintrans := 'frmgk_faktura'; 
    SET nazivfunkcijefintrans := 'FIN.TRANSAKCIJE-IZLAZNA FAKTURA';
  END IF;


  DROP temporary table IF EXISTS tmp_tbl_documents;
  CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null, naziv varchar(255), tipkljuca int(2), tipdokfakt varchar(1) default null);

  
  
  SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca, tipdokfakt from ',@bsliveid,'opp.documents WHERE tipkljuca=',tipprovere,' group by tabela, tipdokfakt');
```

---

## 9. checkForeignKeys

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `checkForeignKeys`(tip int(1), sifra int(6))
BEGIN    
  DECLARE done boolean DEFAULT FALSE;
  DECLARE unknownColumn boolean DEFAULT FALSE;
  DECLARE tableName varchar(30);
  DECLARE keyType int(2);
  DECLARE queryCursor CURSOR FOR SELECT * FROM tmp_helper;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DECLARE CONTINUE HANDLER FOR 1054 SET unknownColumn = TRUE;  
  DROP TEMPORARY TABLE IF EXISTS tmp_helper;
  DROP TEMPORARY TABLE IF EXISTS tmp_foundInTable;
  CREATE TEMPORARY TABLE tmp_helper (tabela varchar(50), tipKljuca int(2));
  CREATE TEMPORARY TABLE tmp_foundInTable(tabela varchar(50));
  SET @q = CONCAT('INSERT INTO tmp_helper SELECT DISTINCT tabela, tipkljuca FROM ', @bsliveid, 'opp.documents WHERE tipkljuca IN (1, 2, 3, 4, 5, 6)');
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
  SET @q = CONCAT('INSERT INTO tmp_helper (tabela, tipkljuca) VALUES (''robno'', 0), (''pazari'', 7), (''specvirpl'', 7), (''popdv_promet'', 8)');
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
  OPEN queryCursor; 
  SET @foundInTable = 0;
  read_loop:
  LOOP FETCH queryCursor INTO tableName, keyType;
  IF done THEN
    LEAVE read_loop;
  END IF;
  SET @counter = 0;
  SET @counter1 = 0;
  IF tip = 1 THEN 
    IF keyType = 3 THEN
      SET @q = CONCAT('SELECT COUNT(sifobj), COUNT(obj2) INTO @counter, @counter1 FROM ', tableName, ' WHERE sifobj = ', sifra, ' OR obj2 = ', sifra);
      SET unknownColumn = FALSE;
      PREPARE stmt FROM @q;
      IF unknownColumn = FALSE THEN EXECUTE stmt; END IF;
      SET @counter = @counter + @counter1;
    ELSEIF KeyType = 7 THEN 
      SET @q = CONCAT('SELECT COUNT(objekat) INTO @counter FROM ', tableName, ' WHERE objekat = ', sifra);
      SET unknownColumn = FALSE;
      PREPARE stmt FROM @q;
      IF unknownColumn = FALSE THEN EXECUTE stmt; END IF;
    ELSE
      SET @q = CONCAT('SELECT COUNT(sifobj) INTO @counter FROM ', tableName, ' WHERE sifobj = ', sifra);
      SET unknownColumn = FALSE;
      PREPARE stmt FROM @q;
      IF unknownColumn = FALSE THEN EXECUTE stmt; END IF; 
    END IF;
    IF @counter > 0 THEN
      INSERT INTO tmp_foundInTable VALUES (tableName);
      SET @foundInTable = 1;
    END IF;
  END IF; 

  IF tip = 2 THEN 
    IF keyType = 1 THEN
      SET @q = CONCAT('SELECT COUNT(dobavljac) INTO @counter FROM ', tableName, ' WHERE dobavljac = ', sifra);
      PREPARE stmt FROM @q;
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
    END IF;
    IF keyType = 2 OR keyType = 7 THEN
      SET @q = CONCAT('SELECT COUNT(sifkup) INTO @counter FROM ', tableName, ' WHERE sifkup = ', sifra);
      SET unknownColumn = FALSE;
      PREPARE stmt FROM @q;
      IF unknownColumn = FALSE THEN EXECUTE stmt; END IF;
    END IF;
    IF keyType = 8 THEN
      SET @q = CONCAT('SELECT COUNT(sifpar) INTO @counter FROM ', tableName, ' WHERE sifkup = ', sifra);
      SET unknownColumn = FALSE;
      PREPARE stmt FROM @q;
      IF unknownColumn = FALSE THEN EXECUTE stmt; END IF;  
    END IF;      
    IF (@counter > 0) THEN
      INSERT INTO tmp_foundInTable VALUES (tableName);
      SET @foundInTable = 1;        
    END IF;
  END IF;

  IF tip = 3 THEN 
    SET @q = CONCAT('SELECT COUNT(sifra) INTO @counter FROM ', tableName, ' WHERE sifra = ', sifra);
    SET unknownColumn = FALSE;
    PREPARE stmt FROM @q;
    IF unknownColumn = FALSE THEN EXECUTE stmt; END IF;
    IF @counter > 0 THEN
      INSERT INTO tmp_foundInTable VALUES (tableName);
      SET @foundInTable = 1;  
    END IF;
  END IF; 
  END LOOP read_loop;
  CLOSE queryCursor; 
  
  IF tip = 2 THEN 
    SET @q = CONCAT('SELECT COUNT(brdok) INTO @counterfinprom FROM finprom WHERE brdok = ''P-', right(concat('00000',sifra),5),'''');     
    PREPARE stmt FROM @q;
    EXECUTE stmt;
  end if;  
  IF (@counterfinprom > 0) THEN
    INSERT INTO tmp_foundInTable VALUES ('finprom');
    SET @foundInTable = 1;  
  end if;
END
```

---

## 10. CheckLDRN

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckLDRN`()
BEGIN
  select osnid into @mynull from ldrngknew limit 1;
  select FOUND_ROWS() into @myrowsfound;
  if @myrowsfound < 1 then
    insert into ldrngknew values (1,'REDOVAN RAD',            '5210','5200','5211','5200','5212','5200','5200','4530','4520','4531','4521','4532','4522','4510');
    insert into ldrngknew values (2,'BOLOVANJE PREKO 30 DANA','2252','2252','2252','2252','2252','2252','2252','4560','4550','4560','4550','4560','4550','4550');
    insert into ldrngknew values (3,'PORODILJSKO BOLOVANJE',  '2251','2251','2251','2251','2251','2251','2251','4560','4550','4560','4550','4560','4550','4550');    
  end if;
END
```

---

## 11. CheckPrometPoSifri

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckPrometPoSifri`(`sifra` integer)
BEGIN
   DECLARE s_tabela,s_naziv varchar(255);
   DECLARE exit_loop boolean;
   DECLARE s_tipkljuca, i, p integer;
   DECLARE dokumenti CURSOR FOR SELECT tabela,naziv,tipkljuca FROM tmp_tbl_documents;
   declare continue handler for not found set exit_loop = true;
   SET @CheckPrometPoSifri_Result = '';

   DROP temporary table IF EXISTS tmp_tbl_documents;
   CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null primary KEY, naziv varchar(255), tipkljuca int(2));
   SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE tipkljuca<8 and sifra<>"PZ" group by tabela');
   PREPARE stmt FROM @aa; EXECUTE stmt;

   OPEN dokumenti;
   set exit_loop = false;
   dokumenti_loop: 
     LOOP FETCH dokumenti INTO s_tabela, s_naziv, s_tipkljuca;
     IF exit_loop THEN
       LEAVE dokumenti_loop;
     END IF;

     SET @aa=CONCAT('SELECT table_name FROM information_schema.tables WHERE table_name=''',s_tabela,''' and table_schema=database()');
     PREPARE stmt FROM @aa; EXECUTE stmt;

     SELECT FOUND_ROWS() INTO i;

     IF i>0 THEN
       SET @aa=CONCAT('select sifra from ',s_tabela,' where sifra=', sifra,' limit 1');
       PREPARE stmt FROM @aa; EXECUTE stmt;        
       SELECT FOUND_ROWS() INTO p;
       IF p>0 THEN
          if upper(trim(s_tabela))='ROBNO' then
            SET @CheckPrometPoSifri_Result = 'ROBNO';
          else
            SET @CheckPrometPoSifri_Result = s_naziv; 
          end if;
          SET exit_loop = TRUE;
       end IF;
     end IF;

   END LOOP dokumenti_loop;
   CLOSE dokumenti;
END
```

---

## 12. CheckTabRnPog

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckTabRnPog`(`vd` varchar(20), `tabela` varchar(20), `brnal` varchar(20), `sifobj` integer)
    MODIFIES SQL DATA
BEGIN
  DECLARE s_racun varchar(20);
  DECLARE s_analitika varchar(20);
  DECLARE s_mestotr integer;
  DECLARE s_nosioctr integer;
  DECLARE ss_mestotr varchar(20);
  DECLARE ss_nosioc varchar(20);
  DECLARE exit_loop boolean;
  DECLARE myracuni CURSOR FOR SELECT racun,analitika, mestotr, nosioctr FROM tmp_trp_racuni;
  declare continue handler FOR NOT FOUND set exit_loop = TRUE;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  SET @full_error := '';
  SET @trp_vd := vd;

  DROP temporary table IF EXISTS tmp_trp_racuni;
  CREATE TEMPORARY TABLE tmp_trp_racuni (racun varchar(20), analitika varchar(20), mestotr int(6), nosioctr int(6));
  SET @qvr=CONCAT("insert into tmp_trp_racuni select ", tabela,".racun, brdok, mestotr, nosioc from ", tabela,", tabracpog where tabracpog.vd='",vd,"' and ", tabela,".brnal='",brnal,"' and (tabracpog.sifobj=",sifobj," or tabracpog.sifobj=0) and ", tabela,".racun=tabracpog.racun group by ", tabela,".racun, brdok, mestotr, nosioc");
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;
  deallocate PREPARE stmt1;

  OPEN myracuni;
  SET exit_loop = FALSE;
  racuni_loop:
    LOOP FETCH myracuni INTO s_racun, s_analitika, s_mestotr, s_nosioctr;
    IF exit_loop THEN
      LEAVE racuni_loop;
    END IF;

    SET @trp_rac1d := '';
    SET @trp_rac1p := '';
    SET @trp_rac2d := '';
    SET @trp_rac2p := '';
    SET @trp_rac3d := '';
    SET @trp_rac3p := '';
    SET @trp_rac4d := '';
    SET @trp_rac4p := '';

    SET @trp_rac5d := '';
    SET @trp_rac5p := '';
    SET @trp_rac6d := '';
    SET @trp_rac6p := '';
    SET @trp_rac7d := '';
    SET @trp_rac7p := '';
    SET @trp_rac8d := '';
    SET @trp_rac8p := '';

    SET @trp_iznos := 0;
    SET @trp_rbrst := 0;
  
    SET @trp_racun := s_racun;

    SET @qvr=CONCAT("select analitika, mestotr, nosioc into @myanalitika, @mymestotr, @mynosioctr from kontniplan where racun='", s_racun,"' and sifrakpl=@kontniplan");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;  
  
    SET @qvr=CONCAT("select trosak, prenostros, trosak2, prenostros2, trosak3, prenostros3, trosak4, prenostros4, trosak5, prenostros5, trosak6, prenostros6, trosak7, prenostros7, trosak8, prenostros8 
       into @trp_rac1d, @trp_rac1p, @trp_rac2d, @trp_rac2p, @trp_rac3d, @trp_rac3p, @trp_rac4d, @trp_rac4p, @trp_rac5d, @trp_rac5p, @trp_rac6d, @trp_rac6p, @trp_rac7d, @trp_rac7p, @trp_rac8d, @trp_rac8p from tabracpog where vd='", vd, "' and (sifobj=", sifobj," or sifobj=0) and racun='", s_racun,"'");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;  

    SET ss_mestotr = concat(' and mestotr=',s_mestotr);
    IF ISNULL(s_mestotr) THEN
      SET ss_mestotr = ' and isnull(mestotr) ';
    END IF;

    SET ss_nosioc = concat(' and nosioc=',s_nosioctr);
    IF ISNULL(s_nosioctr) THEN
      SET ss_nosioc = ' and isnull(nosioc) ';
    END IF;

    SET @qvr=CONCAT("select if(abs(sum(izndug))>abs(sum(iznpot)), sum(izndug), sum(iznpot)) into @trp_iznos from ", tabela," where brnal='",brnal,"' and racun='", s_racun,"' and brdok='", s_analitika,"' ", ss_mestotr,ss_nosioc);
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;

    deallocate PREPARE stmt1;
    IF ISNULL(@trp_iznos) THEN
      SET @trp_iznos := 0;
    END IF;
  
    IF NOT (@trp_iznos=0) THEN
      DROP TEMPORARY TABLE IF EXISTS tmp_trp_finprom;
      SET @qvr=CONCAT("create temporary table if not exists tmp_trp_finprom like ", tabela);
      PREPARE stmt1 FROM @qvr;
      EXECUTE stmt1;
      deallocate PREPARE stmt1;
    
      DROP TEMPORARY TABLE IF EXISTS tmp_trp_finprom2;
      CREATE TEMPORARY TABLE if not EXISTS tmp_trp_finprom2 LIKE tmp_trp_finprom;
  
      SET @qvr=CONCAT("insert into tmp_trp_finprom select * from ", tabela," where brnal='", brnal,"' and racun='", s_racun,"' and brdok='", s_analitika,"' ", ss_mestotr,ss_nosioc, " limit 1");
      PREPARE stmt1 FROM @qvr;
      EXECUTE stmt1;
      deallocate PREPARE stmt1;
  
      SET @qvr=CONCAT("select max(rbrst) into @trp_rbrst from ", tabela," where brnal='", brnal,"'");
      PREPARE stmt1 FROM @qvr;
      EXECUTE stmt1;
      deallocate PREPARE stmt1;
  
      IF ISNULL(@trp_rbrst) THEN
        SET @trp_rbrst := 0;
      END IF;
  
      call CheckTabRnPogAMT(@trp_rac1d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac1p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac2d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac2p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac3d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac3p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac4d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac4p, tabela, true);                
      call CheckTabRnPogAMT(@trp_rac5d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac5p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac6d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac6p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac7d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac7p, tabela, true);  
      call CheckTabRnPogAMT(@trp_rac8d, tabela, false);  
      call CheckTabRnPogAMT(@trp_rac8p, tabela, true);                
  
      DROP TEMPORARY TABLE IF EXISTS tmp_trp_finprom;
      DROP TEMPORARY TABLE IF EXISTS tmp_trp_finprom2;
    end if;
  END LOOP racuni_loop;
  CLOSE myracuni;
END
```

---

## 13. CheckTabRnPogAMT

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckTabRnPogAMT`(`amtkonto` varchar(20), `tabela` varchar(20), potrazuje boolean)
begin
  set @mykontocheck := amtkonto;

  IF NOT (ISNULL(@mykontocheck) OR TRIM(@mykontocheck)='') THEN
    delete from tmp_trp_finprom2;
    INSERT INTO tmp_trp_finprom2 SELECT * FROM tmp_trp_finprom;
    SET @trp_rbrst := @trp_rbrst + 1;
    if potrazuje then
      UPDATE tmp_trp_finprom2 SET racun=@mykontocheck, izndug=0, iznpot=@trp_iznos, rbrst=@trp_rbrst;
    else
      UPDATE tmp_trp_finprom2 SET racun=@mykontocheck, izndug=@trp_iznos, iznpot=0, rbrst=@trp_rbrst;
    end if;
  
    select analitika, mestotr, nosioc into @myanalitika1, @mymestotr1, @mynosioctr1 from kontniplan where racun=@mykontocheck and sifrakpl=@kontniplan;
    if not (@myanalitika=@myanalitika1) then
      UPDATE tmp_trp_finprom2 SET brdok="";
    end if;
    if not (@mymestotr=@mymestotr1) then
      UPDATE tmp_trp_finprom2 SET mestotr=null;
    end if;
    if not (@mynosioctr=@mynosioctr1) then
      UPDATE tmp_trp_finprom2 SET nosioc=null;
    end if;

    SET @qvr=CONCAT("insert into ", tabela," select * from tmp_trp_finprom2");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;
  end if;
end
```

---

## 14. checkvpcenovnik

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `checkvpcenovnik`(IN bsliveid VARCHAR(50),
    IN cenpokup02 BOOLEAN,
    IN par_tipobj VARCHAR(2),
    IN par_sifobj INT,
    IN par_sifkup INT,
    IN par_posljed INT,
    IN par_datum DATE,
    IN par_sifra INT,
    IN par_cena DOUBLE,
    IN par_ostali BOOLEAN,
    IN par_cenaNula BOOLEAN,
    OUT CVPCpostojicena BOOLEAN)
BEGIN
    DECLARE imavpcenovnik BOOLEAN DEFAULT FALSE;
    DECLARE devizni BOOLEAN DEFAULT FALSE;
    DECLARE sopstvenakl BOOLEAN DEFAULT FALSE;
    DECLARE tipkl INT DEFAULT 0;
    DECLARE tipklstr VARCHAR(50) DEFAULT 'srednji';
    DECLARE sifravalute VARCHAR(3) DEFAULT '978';
    DECLARE nazivcenovnika VARCHAR(255);
    DECLARE myvpcena DOUBLE DEFAULT 0;
    DECLARE oldvpcena DOUBLE DEFAULT 0;
    DECLARE errmsg VARCHAR(255);
    DECLARE dynamic_query VARCHAR(500);
    DECLARE formatted_date VARCHAR(10);
    DECLARE done INT DEFAULT 0;
    DECLARE kupci_check_done BOOLEAN DEFAULT FALSE;
    DECLARE kupci_check BOOLEAN DEFAULT FALSE;

    SET CVPCpostojicena = FALSE;      

    IF par_cenaNula THEN
      SET @CVPCresult = 0;
    ELSE
      SET @CVPCresult = par_cena;
    END IF;

    SET formatted_date = DATE_FORMAT(par_datum, '%d.%m.%Y');
   
    IF ((par_tipobj IN ('01', '02') AND cenpokup02) OR par_tipobj IN ('08', '09', '10', '12')) THEN
        IF EXISTS (SELECT 1 FROM vpcenovnici LIMIT 1) THEN            
            WHILE done = 0 DO
                IF kupci_check_done THEN
                    SET kupci_check = FALSE;
                ELSE
                    SET kupci_check = TRUE;
                END IF;

                IF kupci_check AND EXISTS (SELECT vpcenovnik FROM kupci WHERE sifra = par_sifkup LIMIT 1) THEN
                    SELECT vpcenovnik INTO nazivcenovnika FROM kupci WHERE sifra = par_sifkup;

                    IF TRIM(nazivcenovnika) <> '' THEN
                        IF EXISTS (SELECT 1 FROM vpcenovnici WHERE naziv = nazivcenovnika LIMIT 1) THEN
                            SET imavpcenovnik = TRUE;
                        END IF;
                    ELSE
                        SELECT naziv INTO nazivcenovnika FROM vpcenovnici WHERE ostkupci = 1 LIMIT 1;
                        IF TRIM(nazivcenovnika) <> '' THEN
                            SET imavpcenovnik = TRUE;
                        END IF;
                    END IF;
                ELSE
                    SELECT naziv INTO nazivcenovnika FROM vpcenovnici WHERE ostkupci = 1 LIMIT 1;
                    IF TRIM(nazivcenovnika) <> '' THEN
                        SET imavpcenovnik = TRUE;
                    END IF;
                END IF;
               
                IF imavpcenovnik OR kupci_check_done THEN
                    SET done = 1;
                ELSE
                    SET kupci_check_done = TRUE;
                END IF;
            END WHILE;
        END IF;

        IF imavpcenovnik THEN            
            SELECT v.naziv,
                   IFNULL(v.tipkl, 0),
                   IF(v.devizni = '1', TRUE, FALSE),
                   IF(v.sopstkl = '1', TRUE, FALSE),
                   v.sifval
            INTO nazivcenovnika, tipkl, devizni, sopstvenakl, sifravalute
            FROM vpcenovnici v WHERE v.naziv = nazivcenovnika LIMIT 1;

            SELECT id, vpcena, vpcenadin
            INTO @record_id, myvpcena, oldvpcena
            FROM (
                SELECT id, vpcena, vpcenadin,
                       CASE                                  
                          WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND NOT ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 12
                          WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND NOT ISNULL(posljed) AND ISNULL(attobjekta) THEN 11                              
                          WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 10
                          WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 9                                                              
                          WHEN NOT ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 8
                          WHEN NOT ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 7                                                                
                          WHEN ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 6
                          WHEN ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 5                              
                          WHEN ISNULL(partner) AND ISNULL(sifobj) AND NOT ISNULL(posljed) AND ISNULL(attobjekta) THEN 4
                          WHEN ISNULL(partner) AND ISNULL(sifobj) AND NOT ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 3                            
                          WHEN ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 2                            
                          WHEN ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 1
                      END AS priority
                FROM vpcenovnicisifre
                WHERE naziv = nazivcenovnika
                  AND sifra = par_sifra
                  AND ((datumod <= par_datum OR ISNULL(datumod))
                  AND (datumdo >= par_datum OR ISNULL(datumdo)))
                  AND (sifobj = par_sifobj OR ISNULL(sifobj))
                  AND (partner = par_sifkup OR ISNULL(partner))
                  AND (posljed = par_posljed OR ISNULL(posljed))
                  AND (ISNULL(attobjekta) OR attobjekta IN (SELECT atribut FROM objatributiobjekti WHERE sifra = par_sifobj AND assigned = 1))                            
            ) AS subquery
            ORDER BY priority DESC, id DESC
            LIMIT 1;

            IF ISNULL(myvpcena) OR myvpcena = 0 THEN
                IF par_ostali THEN
                    SELECT naziv INTO nazivcenovnika FROM vpcenovnici WHERE ostkupci = 1 LIMIT 1;
                   
                    SELECT v.naziv,
                       IFNULL(v.tipkl, 0),
                       IF(v.devizni = '1', TRUE, FALSE),
                       IF(v.sopstkl = '1', TRUE, FALSE),
                       v.sifval
                    INTO nazivcenovnika, tipkl, devizni, sopstvenakl, sifravalute
                    FROM vpcenovnici v WHERE v.naziv = nazivcenovnika LIMIT 1;
   
                    SELECT id, vpcena, vpcenadin
                    INTO @record_id, myvpcena, oldvpcena
                    FROM (
                        SELECT id, vpcena, vpcenadin,
                               CASE                                  
                                  WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND NOT ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 12
                                  WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND NOT ISNULL(posljed) AND ISNULL(attobjekta) THEN 11                              
                                  WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 10
                                  WHEN NOT ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 9                                                              
                                  WHEN NOT ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 8
                                  WHEN NOT ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 7                                                                
                                  WHEN ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 6
                                  WHEN ISNULL(partner) AND NOT ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 5                              
                                  WHEN ISNULL(partner) AND ISNULL(sifobj) AND NOT ISNULL(posljed) AND ISNULL(attobjekta) THEN 4
                                  WHEN ISNULL(partner) AND ISNULL(sifobj) AND NOT ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 3                            
                                  WHEN ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND NOT ISNULL(attobjekta) THEN 2                            
                                  WHEN ISNULL(partner) AND ISNULL(sifobj) AND ISNULL(posljed) AND ISNULL(attobjekta) THEN 1
                              END AS priority
                        FROM vpcenovnicisifre
                        WHERE naziv = nazivcenovnika
                          AND sifra = par_sifra
                          AND ((datumod <= par_datum OR ISNULL(datumod))
                          AND (datumdo >= par_datum OR ISNULL(datumdo)))
                          AND (sifobj = par_sifobj OR ISNULL(sifobj))
                          AND (partner = par_sifkup OR ISNULL(partner))
                          AND (posljed = par_posljed OR ISNULL(posljed))
                          AND (ISNULL(attobjekta) OR attobjekta IN (SELECT atribut FROM objatributiobjekti WHERE sifra = par_sifobj AND assigned = 1))
                    ) AS subquery
                    ORDER BY priority DESC, id DESC
                    LIMIT 1;                    
                    IF (ISNULL(myvpcena) OR (myvpcena = 0)) AND NOT (par_cenaNula) THEN
                        SET imavpcenovnik = FALSE;                                                                        
                    ELSE
                        SET imavpcenovnik = TRUE;                                              
                    END IF;  
                ELSE
                  SET imavpcenovnik = FALSE;
                END IF;                                              
            ELSE
                SET imavpcenovnik = TRUE;                
            END IF;
            SET CVPCpostojicena = imavpcenovnik;

            IF imavpcenovnik THEN
                IF devizni THEN
                    IF sopstvenakl THEN
                        IF sifravalute = '840' THEN
                            SET @dynamic_query = CONCAT('SELECT usd INTO @rate FROM ', bsliveid, 'opp.zirklista WHERE datum <= "', par_datum, '" ORDER BY datum DESC LIMIT 1');
                        ELSEIF sifravalute = '756' THEN
                            SET @dynamic_query = CONCAT('SELECT chf INTO @rate FROM ', bsliveid, 'opp.zirklista WHERE datum <= "', par_datum, '" ORDER BY datum DESC LIMIT 1');
                        ELSEIF sifravalute = '978' THEN
                            SET @dynamic_query = CONCAT('SELECT eur INTO @rate FROM ', bsliveid, 'opp.zirklista WHERE datum <= "', par_datum, '" ORDER BY datum DESC LIMIT 1');
                        END IF;
                        PREPARE stmt FROM @dynamic_query;
                        EXECUTE stmt;
                        DEALLOCATE PREPARE stmt;

                        IF ISNULL(@rate) OR @rate = 0 THEN
                            SET errmsg = CONCAT('Ne postoji sopstvena kursna lista za datum ', formatted_date, ' !');
                            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errmsg;
                        END IF;
                    ELSE
                        SET tipklstr = CASE
                                        WHEN tipkl = 0 THEN 'srednji'
                                        WHEN tipkl = 1 THEN 'kup_dev'
                                        WHEN tipkl = 2 THEN 'prod_dev'
                                        WHEN tipkl = 3 THEN 'kup_efek'
                                        WHEN tipkl = 4 THEN 'prod_efek'
                                     END;

                        SET @dynamic_query = CONCAT('SELECT ', tipklstr, ' / parit INTO @rate FROM ', bsliveid, 'opp.datkl WHERE datvaz = "', par_datum, '" AND sifval = "', sifravalute, '"');
                        PREPARE stmt FROM @dynamic_query;
                        EXECUTE stmt;
                        DEALLOCATE PREPARE stmt;

                        IF ISNULL(@rate) OR @rate = 0 THEN
                            SET errmsg = CONCAT('Ne postoji kursna lista za datum ', formatted_date, ' !');
                            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errmsg;
                        END IF;
                    END IF;

                    SET myvpcena = myvpcena * @rate;
                    IF par_cenaNula THEN
                      SET @CVPCresult = myvpcena;                      
                    ELSE
                      IF myvpcena = 0 THEN SET myvpcena = oldvpcena; END IF;
                      IF myvpcena = 0 THEN SET myvpcena = 1; END IF;
                      IF myvpcena <> 0 THEN SET @CVPCresult = myvpcena; END IF;                      
                    END IF;                                                            
                ELSE  
                  IF par_cenaNula THEN
                    SET @CVPCresult = myvpcena;                    
                  ELSE            
                    IF myvpcena <> 0 THEN SET @CVPCresult = myvpcena; END IF;
                  END IF;                  
                END IF;              
            END IF;
        ELSE                                                                
            SET @CVPCresult = par_cena;                            
        END IF;              
    ELSE                            
        SET @CVPCresult = par_cena;      
    END IF;
END
```

---

## 15. create_tmp_tmp_rek

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_tmp_tmp_rek`()
begin
  drop temporary table if exists tmp_tmp_rek;
  create temporary table tmp_tmp_rek (brnal varchar(100) not null, primary key (brnal));
  insert into tmp_tmp_rek select brnal from tmp_rekapitulacijapdv group by brnal;
end
```

---

## 16. creeeopdvp

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `creeeopdvp`(zagodinu int(4), tromesecni int(1))
BEGIN
  
  
  drop temporary table if exists tmp_ez_popdv_promet;
  create temporary table tmp_ez_popdv_promet (brnal varchar(50) not null, datpdv date not null, osnovicaos double(15,2) default 0, pdvos double(15,2) default 0, osnovicaps double(15,2) default 0, pdvps double(15,2) default 0, eeopdv int(2), potvrdjeno int(1), stornirano int(1), eeopdv_tipprom int(1) not null,eeopdv_avans int(1) default 0, eeopdv_dokumentstorno int(1) default 0, primary key(brnal,eeopdv_tipprom));
  if tromesecni=1 then
    insert ignore into my_eeopdv set godina=zagodinu, period=21, mesec=3, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=21, mesec=3, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=22, mesec=6, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=22, mesec=6, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=23, mesec=9, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=23, mesec=9, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=24, mesec=12, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=24, mesec=12, tipevidencije=1, status=1;

    delete from my_eeopdv_zbirna where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=0 and status<2);
    delete from my_eeopdv_pojedinacna where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=1 and status<2);
    delete from my_eeopdv_negativni where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=0 and status<2);

    
    insert into my_eeopdv_negativni select godina, period, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps),sum(popdv_promet.pdvos+popdv_promet.pdvps-popdv_promet.bezodbitka) as ospdv,sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps+popdv_promet.pdvos+popdv_promet.pdvps-popdv_promet.bezodbitka) as osukupno
      from popdv_promet,popdv_sifarnik,my_eeopdv where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and status=1 and potvrdjeno=1 and popdv_promet.stornirano=0 and popdv_promet.popdvid=popdv_sifarnik.popdvid and ulazni=1  group by godina,period having ospdv<1;

    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(osnovicaos=0 and pdvos<>0, pdvos/(getpdv('S1',datpdv)/100) ,osnovicaos)), sum(pdvos), sum(if(osnovicaps=0 and pdvps<>0, pdvps/(getpdv('S2',datpdv)/100) ,osnovicaps)), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and left(brnal,2)='OD' and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(pdvos>0,pdvos/(getpdv('S1',datpdv)/100),0)), sum(pdvos), 0, 0, eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and not left(brnal,2)='OD' and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    update tmp_ez_popdv_promet set osnovicaos= pdvos/(getpdv('S1',datpdv)/100), osnovicaps= pdvps/(getpdv('S2',datpdv)/100) where (left(brnal,2)='OK' or left(brnal,2)='AR') and (pdvos<0 or pdvps<0) and eeopdv_avans = 1 and (osnovicaos=0 and osnovicaps=0);
    
    update my_eeopdv set smanjenje=0,uvecanje=0 where my_eeopdv.godina=zagodinu and my_eeopdv.period>20 and tipevidencije=0 and status=1;
    
    update my_eeopdv,my_eeopdv_negativni set smanjenje=0,uvecanje=my_eeopdv_negativni.pnos_pdv * -1 where my_eeopdv.godina=my_eeopdv_negativni.godina and my_eeopdv.period=my_eeopdv_negativni.period and my_eeopdv.period>20 and tipevidencije=0 and status=1;
    
   

    
    insert into my_eeopdv_zbirna select godina, period, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'PROMET SA NAKNADOM','','',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=0
          on duplicate key UPDATE pnos_osnovica=pnos_osnovica+osnovicaos, pnos_pdv=pnos_pdv+pdvos, pnos_ukupno=pnos_ukupno+osnovicaos+pdvos, pnns_osnovica=pnns_osnovica+osnovicaps, pnns_pdv=pnns_pdv+pdvps, pnns_ukupno=pnns_ukupno+osnovicaps+pdvps, sanaknadomopis='PROMET SA NAKNADOM';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, 0, 0, 0, 0, 0, 0, '','PROMET BEZ NAKNADE','',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=1
          on duplicate key UPDATE pbos_osnovica=pbos_osnovica+osnovicaos, pbos_pdv=pbos_pdv+pdvos, pbos_ukupno=pbos_ukupno+osnovicaos+pdvos, pbns_osnovica=pbns_osnovica+osnovicaps, pbns_pdv=pbns_pdv+pdvps, pbns_ukupno=pbns_ukupno+osnovicaps+pdvps, beznaknadeopis='PROMET BEZ NAKNADE';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, '','','AVANSI ZA BUDU?I PROMET',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=2
          on duplicate key UPDATE pavansos_osnovica=pavansos_osnovica+osnovicaos, pavansos_pdv=pavansos_pdv+pdvos, pavansos_ukupno=pavansos_ukupno+osnovicaos+pdvos, pavansns_osnovica=pavansns_osnovica+osnovicaps, pavansns_pdv=pavansns_pdv+pdvps, pavansns_ukupno=pavansns_ukupno+osnovicaps+pdvps, avansopis='AVANSI ZA BUDU?I PROMET';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','TURISTIČKE USLUGE',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      if(eeopdv_avans=0,osnovicaos,0), if(eeopdv_avans=0,pdvos,0), if(eeopdv_avans=1,osnovicaos,0), if(eeopdv_avans=1, pdvos, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<0) or (not pdvps<0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=3
          on duplicate key UPDATE tu_osnovicaos=if(eeopdv_avans=0,tu_osnovicaos+osnovicaos,tu_osnovicaos), tu_pdvos=if(eeopdv_avans=0,tu_pdvos+pdvos,tu_pdvos), tuav_osnovicaos=if(eeopdv_avans=1,tuav_osnovicaos+osnovicaos,tuav_osnovicaos), tuav_pdvos=if(eeopdv_avans=1,tuav_pdvos+pdvos,tuav_pdvos);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','POLOVNA DOBRA',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0,
      if(eeopdv_avans=0,osnovicaos,0), if(eeopdv_avans=0,pdvos,0), if(eeopdv_avans=0,osnovicaps,0), if(eeopdv_avans=0,pdvps,0), if(eeopdv_avans=1,osnovicaos,0), if(eeopdv_avans=1,pdvos,0), if(eeopdv_avans=1,osnovicaps,0), if(eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=4
          on duplicate key UPDATE pd_osnovicaos=if(eeopdv_avans=0,pd_osnovicaos+osnovicaos,pd_osnovicaos), pd_pdvos=if(eeopdv_avans=0,pd_pdvos+pdvos,pd_pdvos), pd_osnovicaps=if(eeopdv_avans=0,pd_osnovicaps+osnovicaps,pd_osnovicaps), 
          pd_pdvps=if(eeopdv_avans=0,pd_pdvps+pdvps,pd_pdvps), pdav_osnovicaos=if(eeopdv_avans=1,pdav_osnovicaos+osnovicaos,pdav_osnovicaos), pdav_pdvos=if(eeopdv_avans=1,pdav_pdvos+pdvos,pdav_pdvos),
          pdav_osnovicaps=if(eeopdv_avans=1,pdav_osnovicaps+osnovicaps,pdav_osnovicaps), pdav_pdvps=if(eeopdv_avans=1,pdav_pdvps+pdvps,pdav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','PROMENA OSOVICE ISPORUČILAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=5 and eeopdv_dokumentstorno=0 
          on duplicate key UPDATE poi_osnovicaos=if(osnovicaos>0,poi_osnovicaos+osnovicaos,poi_osnovicaos), poi_pdvos=if(pdvos>0,poi_pdvos+pdvos,poi_pdvos),poi_osnovicaps=if(osnovicaps>0,poi_osnovicaps+osnovicaps,poi_osnovicaps), poi_pdvps=if(pdvps>0,poi_pdvps+pdvps,poi_pdvps),
          smi_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,smi_osnovicaos+osnovicaos,smi_osnovicaos), smi_pdvos=if(pdvos<0 and eeopdv_avans=0,smi_pdvos+pdvos,smi_pdvos),smi_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,smi_osnovicaps+osnovicaps,smi_osnovicaps), smi_pdvps=if(pdvps<0 and eeopdv_avans=0,smi_pdvps+pdvps,smi_pdvps),
          smiav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,smiav_osnovicaos+osnovicaos,smiav_osnovicaos), smiav_pdvos=if(pdvos<0 and eeopdv_avans=1,smiav_pdvos+pdvos,smiav_pdvos),smiav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,smiav_osnovicaps+osnovicaps,smiav_osnovicaps), smiav_pdvps=if(pdvps<0 and eeopdv_avans=1,smiav_pdvps+pdvps,smiav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','PROMENA OSOVICE PRIMALAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=6 and eeopdv_dokumentstorno=0 
          on duplicate key UPDATE pop_osnovicaos=if(osnovicaos>0,pop_osnovicaos+osnovicaos,pop_osnovicaos), pop_pdvos=if(pdvos>0,pop_pdvos+pdvos,pop_pdvos),pop_osnovicaps=if(osnovicaps>0,pop_osnovicaps+osnovicaps,pop_osnovicaps), pop_pdvps=if(pdvps>0,pop_pdvps+pdvps,pop_pdvps),
          smp_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,smp_osnovicaos+osnovicaos,smp_osnovicaos), smp_pdvos=if(pdvos<0 and eeopdv_avans=0,smp_pdvos+pdvos,smp_pdvos),smp_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,smp_osnovicaps+osnovicaps,smp_osnovicaps), smp_pdvps=if(pdvps<0 and eeopdv_avans=0,smp_pdvps+pdvps,smp_pdvps),
          smpav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,smpav_osnovicaos+osnovicaos,smpav_osnovicaos), smpav_pdvos=if(pdvos<0 and eeopdv_avans=1,smpav_pdvos+pdvos,smpav_pdvos),smpav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,smpav_osnovicaps+osnovicaps,smpav_osnovicaps), smpav_pdvps=if(pdvps<0 and eeopdv_avans=1,smpav_pdvps+pdvps,smpav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','STORNIRANJE ISPORUČILAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=7 and eeopdv_dokumentstorno=1 
          on duplicate key UPDATE stpi_osnovicaos=if(osnovicaos>0,stpi_osnovicaos+osnovicaos,stpi_osnovicaos), stpi_pdvos=if(pdvos>0,stpi_pdvos+pdvos,stpi_pdvos),stpi_osnovicaps=if(osnovicaps>0,stpi_osnovicaps+osnovicaps,stpi_osnovicaps), stpi_pdvps=if(pdvps>0,stpi_pdvps+pdvps,stpi_pdvps),
          stsi_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,stsi_osnovicaos+osnovicaos,stsi_osnovicaos), stsi_pdvos=if(pdvos<0 and eeopdv_avans=0,stsi_pdvos+pdvos,stsi_pdvos),stsi_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,stsi_osnovicaps+osnovicaps,stsi_osnovicaps), stsi_pdvps=if(pdvps<0 and eeopdv_avans=0,stsi_pdvps+pdvps,stsi_pdvps),
          stsiav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,stsiav_osnovicaos+osnovicaos,stsiav_osnovicaos), stsiav_pdvos=if(pdvos<0 and eeopdv_avans=1,stsiav_pdvos+pdvos,stsiav_pdvos),stsiav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,stsiav_osnovicaps+osnovicaps,stsiav_osnovicaps), stsiav_pdvps=if(pdvps<0 and eeopdv_avans=1,stsiav_pdvps+pdvps,stsiav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','STORNIRANJE PRIMALAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0) 
        from tmp_ez_popdv_promet,my_eeopdv where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=8 and eeopdv_dokumentstorno=1 
          on duplicate key UPDATE stpp_osnovicaos=if(osnovicaos>0,stpp_osnovicaos+osnovicaos,stpp_osnovicaos), stpp_pdvos=if(pdvos>0,stpp_pdvos+pdvos,stpp_pdvos),stpp_osnovicaps=if(osnovicaps>0,stpp_osnovicaps+osnovicaps,stpp_osnovicaps), stpp_pdvps=if(pdvps>0,stpp_pdvps+pdvps,stpp_pdvps),
          stsp_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,stsp_osnovicaos+osnovicaos,stsp_osnovicaos), stsp_pdvos=if(pdvos<0 and eeopdv_avans=0,stsp_pdvos+pdvos,stsp_pdvos),stsp_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,stsp_osnovicaps+osnovicaps,stsp_osnovicaps), stsp_pdvps=if(pdvps<0 and eeopdv_avans=0,stsp_pdvps+pdvps,stsp_pdvps),
          stspav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,stspav_osnovicaos+osnovicaos,stspav_osnovicaos), stspav_pdvos=if(pdvos<0 and eeopdv_avans=1,stspav_pdvos+pdvos,stspav_pdvos),stspav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,stspav_osnovicaps+osnovicaps,stspav_osnovicaps), stspav_pdvps=if(pdvps<0 and eeopdv_avans=1,stspav_pdvps+pdvps,stspav_pdvps);

    
    insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), sum(osnovicaos+osnovicaps), datpdv, sum(osnovicaos) as oos , sum(osnovicaps), sum(pdvos+pdvps) as spdv, sum(ukupno), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
          eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
         from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
         where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and status=1 and potvrdjeno=1 and stornirano=0 and not (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;
  
  
  insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',REPLACE(originalbrnal,'-RZ','')), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
  eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), ABS(sum(pdvos+pdvps)) as pdvuk, datpdv, ABS(sum(osnovicaos)) as oos , ABS(sum(osnovicaps)),
  sum(ABS(osnovicaos)*(getpdv('S1',datpdv)/100) + ABS(osnovicaps)*(getpdv('S2',datpdv)/100)) as spdv, sum(ABS(osnovicaos)*(1+(getpdv('S1',datpdv)/100))+abs(osnovicaps)*(1+(getpdv('S2',datpdv)/100))), 0, 0, 0, null,
  eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(osnovicaos)*(getpdv('S1',datpdv)/100)), sum(ABS(osnovicaps)*(getpdv('S2',datpdv)/100)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
        where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=6 and status=1 and potvrdjeno=1 and stornirano=0 group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0 and pdvuk=0;

  
  insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',REPLACE(originalbrnal,'-RZ','')), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
  eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)), datpdv,
  ABS(sum(pdvos/(getpdv('S1',datpdv)/100))) as oos , ABS(sum(pdvps/(getpdv('S2',datpdv)/100))),sum(ABS(pdvos) + ABS(pdvps)) as spdv,ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)),
   0, 0, 0, null, eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(pdvos)), sum(ABS(pdvps)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
      from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra      
      where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=6 and my_eeopdv.status=1 and potvrdjeno=1 and stornirano=0
      group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;
            
  
  insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',popdv_promet.originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
  if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), sum(if(ukupno>0,ukupno,0)), datpdv, sum(if(osnovicaos>0,osnovicaos,0)), sum(if(osnovicaps>0,osnovicaps,0)),
  sum(pdvos+pdvps), sum(if(ukupno>0,ukupno,0)), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from my_eeopdv, popdv_promet 
        left join kupci on popdv_promet.sifpar=kupci.sifra            
        WHERE quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0                    
        AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and NOT (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g') group by popdv_promet.originalbrnal;    

  
  insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',popdv_promet.originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
  if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), zukupno, datpdv, zosnovicaos, zosnovicaps,
  (zpdvos+zpdvps), zukupno, 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, zpdvos, zpdvps, eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from my_eeopdv, popdv_promet 
        left join kupci on popdv_promet.sifpar=kupci.sifra 
        left join (select originalbrnal, sum(if(ukupno>0,ukupno,0)) AS zukupno, sum(if(osnovicaos>0,osnovicaos,0)) AS zosnovicaos, sum(if(osnovicaps>0,osnovicaps,0)) AS zosnovicaps, sum(pdvos) as zpdvos, sum(pdvps) as zpdvps 
        from popdv_promet where stornirano = 0 and (left(popdvid,2) = '8b' or left(popdvid,2) = '8g') group by originalbrnal) as popdv_zbir on popdv_zbir.originalbrnal = popdv_promet.originalbrnal
        WHERE quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0         
        AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g')
        group by popdv_promet.originalbrnal;  
  else
    insert ignore into my_eeopdv set godina=zagodinu, period=1, mesec=1, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=1, mesec=1, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=2, mesec=2, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=2, mesec=2, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=3, mesec=3, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=3, mesec=3, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=4, mesec=4, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=4, mesec=4, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=5, mesec=5, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=5, mesec=5, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=6, mesec=6, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=6, mesec=6, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=7, mesec=7, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=7, mesec=7, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=8, mesec=8, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=8, mesec=8, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=9, mesec=9, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=9, mesec=9, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=10, mesec=10, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=10, mesec=10, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=11, mesec=11, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=11, mesec=11, tipevidencije=1, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=12, mesec=12, tipevidencije=0, status=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=12, mesec=12, tipevidencije=1, status=1;

    delete from my_eeopdv_zbirna where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=0 and status<2);
    delete from my_eeopdv_pojedinacna where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=1 and status<2);
    delete from my_eeopdv_negativni where concat(godina,period) in (select concat(godina,period) from my_eeopdv where tipevidencije=0 and status<2);

    
    insert into my_eeopdv_negativni select godina, period, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps),sum(popdv_promet.pdvos+popdv_promet.pdvps-popdv_promet.bezodbitka) as ospdv,sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps+popdv_promet.pdvos+popdv_promet.pdvps-popdv_promet.bezodbitka) as osukupno
      from popdv_promet,popdv_sifarnik,my_eeopdv where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and year(popdv_promet.datpdv)=zagodinu and period<20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and popdv_promet.popdvid=popdv_sifarnik.popdvid and ulazni=1 group by godina,period having ospdv<1;

    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(osnovicaos=0 and pdvos<>0, pdvos/(getpdv('S1',datpdv)/100) ,osnovicaos)), sum(pdvos), sum(if(osnovicaps=0 and pdvps<>0, pdvps/(getpdv('S2',datpdv)/100) ,osnovicaps)), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(pdvos>0,pdvos/(getpdv('S1',datpdv)/100),0)), sum(pdvos), 0, 0, eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno from popdv_promet,my_eeopdv 
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    update tmp_ez_popdv_promet set osnovicaos= pdvos/(getpdv('S1',datpdv)/100), osnovicaps= pdvps/(getpdv('S2',datpdv)/100) where ((left(brnal,2)='OK' or left(brnal,2)='AR') or (left(brnal,2)='RA' and eeopdv_dokumentstorno=1)) and (pdvos<0 or pdvps<0) and eeopdv_avans = 1 and (osnovicaos=0 and osnovicaps=0);
    
    update my_eeopdv set smanjenje=0,uvecanje=0 where my_eeopdv.godina=zagodinu and my_eeopdv.period<20 and tipevidencije=0 and status=1;
    
    update my_eeopdv,my_eeopdv_negativni set smanjenje=0,uvecanje=my_eeopdv_negativni.pnos_pdv * -1 where my_eeopdv.godina=my_eeopdv_negativni.godina and my_eeopdv.period=my_eeopdv_negativni.period and my_eeopdv.period<20 and tipevidencije=0 and status=1;
    
    


    
    insert into my_eeopdv_zbirna select godina, period, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'PROMET SA NAKNADOM','','',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),     
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=0
          on duplicate key UPDATE pnos_osnovica=pnos_osnovica+osnovicaos, pnos_pdv=pnos_pdv+pdvos, pnos_ukupno=pnos_ukupno+osnovicaos+pdvos, pnns_osnovica=pnns_osnovica+osnovicaps, pnns_pdv=pnns_pdv+pdvps, pnns_ukupno=pnns_ukupno+osnovicaps+pdvps, sanaknadomopis='PROMET SA NAKNADOM';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, 0, 0, 0, 0, 0, 0, '','PROMET BEZ NAKNADE','',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0   
      from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=1
          on duplicate key UPDATE pbos_osnovica=pbos_osnovica+osnovicaos, pbos_pdv=pbos_pdv+pdvos, pbos_ukupno=pbos_ukupno+osnovicaos+pdvos, pbns_osnovica=pbns_osnovica+osnovicaps, pbns_pdv=pbns_pdv+pdvps, pbns_ukupno=pbns_ukupno+osnovicaps+pdvps, beznaknadeopis='PROMET BEZ NAKNADE';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, osnovicaos, pdvos, osnovicaos+pdvos, osnovicaps, pdvps, osnovicaps+pdvps, '','','AVANSI ZA BUDU?I PROMET',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=2
          on duplicate key UPDATE pavansos_osnovica=pavansos_osnovica+osnovicaos, pavansos_pdv=pavansos_pdv+pdvos, pavansos_ukupno=pavansos_ukupno+osnovicaos+pdvos, pavansns_osnovica=pavansns_osnovica+osnovicaps, pavansns_pdv=pavansns_pdv+pdvps, pavansns_ukupno=pavansns_ukupno+osnovicaps+pdvps, avansopis='AVANSI ZA BUDU?I PROMET';
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','TURISTIČKE USLUGE',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),
      if(eeopdv_avans=0,osnovicaos,0), if(eeopdv_avans=0,pdvos,0), if(eeopdv_avans=1,osnovicaos,0), if(eeopdv_avans=1, pdvos, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<0) or (not pdvps<0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=3
          on duplicate key UPDATE tu_osnovicaos=if(eeopdv_avans=0,tu_osnovicaos+osnovicaos,tu_osnovicaos), tu_pdvos=if(eeopdv_avans=0,tu_pdvos+pdvos,tu_pdvos), tuav_osnovicaos=if(eeopdv_avans=1,tuav_osnovicaos+osnovicaos,tuav_osnovicaos), tuav_pdvos=if(eeopdv_avans=1,tuav_pdvos+pdvos,tuav_pdvos);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','POLOVNA DOBRA',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0,
      if(eeopdv_avans=0,osnovicaos,0), if(eeopdv_avans=0,pdvos,0), if(eeopdv_avans=0,osnovicaps,0), if(eeopdv_avans=0,pdvps,0), if(eeopdv_avans=1,osnovicaos,0), if(eeopdv_avans=1,pdvos,0), if(eeopdv_avans=1,osnovicaps,0), if(eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=4
          on duplicate key UPDATE pd_osnovicaos=if(eeopdv_avans=0,pd_osnovicaos+osnovicaos,pd_osnovicaos), pd_pdvos=if(eeopdv_avans=0,pd_pdvos+pdvos,pd_pdvos), pd_osnovicaps=if(eeopdv_avans=0,pd_osnovicaps+osnovicaps,pd_osnovicaps), 
          pd_pdvps=if(eeopdv_avans=0,pd_pdvps+pdvps,pd_pdvps), pdav_osnovicaos=if(eeopdv_avans=1,pdav_osnovicaos+osnovicaos,pdav_osnovicaos), pdav_pdvos=if(eeopdv_avans=1,pdav_pdvos+pdvos,pdav_pdvos),
          pdav_osnovicaps=if(eeopdv_avans=1,pdav_osnovicaps+osnovicaps,pdav_osnovicaps), pdav_pdvps=if(eeopdv_avans=1,pdav_pdvps+pdvps,pdav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','PROMENA OSNOVICE ISPORUČILAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=5 and eeopdv_dokumentstorno=0 
          on duplicate key UPDATE poi_osnovicaos=if(osnovicaos>0,poi_osnovicaos+osnovicaos,poi_osnovicaos), poi_pdvos=if(pdvos>0,poi_pdvos+pdvos,poi_pdvos),poi_osnovicaps=if(osnovicaps>0,poi_osnovicaps+osnovicaps,poi_osnovicaps), poi_pdvps=if(pdvps>0,poi_pdvps+pdvps,poi_pdvps),
          smi_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,smi_osnovicaos+osnovicaos,smi_osnovicaos), smi_pdvos=if(pdvos<0 and eeopdv_avans=0,smi_pdvos+pdvos,smi_pdvos), smi_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,smi_osnovicaps+osnovicaps,smi_osnovicaps) , smi_pdvps=if(pdvps<0 and eeopdv_avans=0,smi_pdvps+pdvps,smi_pdvps),
          smiav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,smiav_osnovicaos+osnovicaos,smiav_osnovicaos), smiav_pdvos=if(pdvos<0 and eeopdv_avans=1,smiav_pdvos+pdvos,smiav_pdvos),smiav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,smiav_osnovicaps+osnovicaps,smiav_osnovicaps), smiav_pdvps=if(pdvps<0 and eeopdv_avans=1,smiav_pdvps+pdvps,smiav_pdvps);
    
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','PROMENA OSNOVICE PRIMALAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=6 and eeopdv_dokumentstorno=0 
          on duplicate key UPDATE pop_osnovicaos=if(osnovicaos>0,pop_osnovicaos+osnovicaos,pop_osnovicaos), pop_pdvos=if(pdvos>0,pop_pdvos+pdvos,pop_pdvos),pop_osnovicaps=if(osnovicaps>0,pop_osnovicaps+osnovicaps,pop_osnovicaps), pop_pdvps=if(pdvps>0,pop_pdvps+pdvps,pop_pdvps),
          smp_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,smp_osnovicaos+osnovicaos,smp_osnovicaos), smp_pdvos=if(pdvos<0 and eeopdv_avans=0,smp_pdvos+pdvos,smp_pdvos),smp_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,smp_osnovicaps+osnovicaps,smp_osnovicaps), smp_pdvps=if(pdvps<0 and eeopdv_avans=0,smp_pdvps+pdvps,smp_pdvps),
          smpav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,smpav_osnovicaos+osnovicaos,smpav_osnovicaos), smpav_pdvos=if(pdvos<0 and eeopdv_avans=1,smpav_pdvos+pdvos,smpav_pdvos),smpav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,smpav_osnovicaps+osnovicaps,smpav_osnovicaps), smpav_pdvps=if(pdvps<0 and eeopdv_avans=1,smpav_pdvps+pdvps,smpav_pdvps);          
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','STORNIRANJE ISPORUČILAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0        
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=7 and eeopdv_dokumentstorno=1 
        on duplicate key UPDATE stpi_osnovicaos=if(osnovicaos>0,stpi_osnovicaos+osnovicaos,stpi_osnovicaos), stpi_pdvos=if(pdvos>0,stpi_pdvos+pdvos,stpi_pdvos),stpi_osnovicaps=if(osnovicaps>0,stpi_osnovicaps+osnovicaps,stpi_osnovicaps), stpi_pdvps=if(pdvps>0,stpi_pdvps+pdvps,stpi_pdvps),
          stsi_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,stsi_osnovicaos+osnovicaos,stsi_osnovicaos), stsi_pdvos=if(pdvos<0 and eeopdv_avans=0,stsi_pdvos+pdvos,stsi_pdvos),stsi_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,stsi_osnovicaps+osnovicaps,stsi_osnovicaps), stsi_pdvps=if(pdvps<0 and eeopdv_avans=0,stsi_pdvps+pdvps,stsi_pdvps),
          stsiav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,stsiav_osnovicaos+osnovicaos,stsiav_osnovicaos), stsiav_pdvos=if(pdvos<0 and eeopdv_avans=1,stsiav_pdvos+pdvos,stsiav_pdvos),stsiav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,stsiav_osnovicaps+osnovicaps,stsiav_osnovicaps), stsiav_pdvps=if(pdvps<0 and eeopdv_avans=1,stsiav_pdvps+pdvps,stsiav_pdvps);
    
    insert into my_eeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','STORNIRANJE PRIMALAC',LAST_DAY(DATE(CONCAT_WS('-', godina, mesec, 1))),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      if(osnovicaos>0,osnovicaos,0), if(pdvos>0,pdvos,0), if(osnovicaps>0,osnovicaps,0),if(pdvps>0,pdvps,0), if(osnovicaos<0 and eeopdv_avans=0,osnovicaos,0), if(pdvos<0 and eeopdv_avans=0,pdvos,0), if(osnovicaps<0 and eeopdv_avans=0,osnovicaps,0),if(pdvps<0 and eeopdv_avans=0,pdvps,0),
       if(osnovicaos<0 and eeopdv_avans=1,osnovicaos,0), if(pdvos<0 and eeopdv_avans=1,pdvos,0), if(osnovicaps<0 and eeopdv_avans=1,osnovicaps,0),if(pdvps<0 and eeopdv_avans=1,pdvps,0) 
        from tmp_ez_popdv_promet,my_eeopdv where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=8 and eeopdv_dokumentstorno=1 
          on duplicate key UPDATE stpp_osnovicaos=if(osnovicaos>0,stpp_osnovicaos+osnovicaos,stpp_osnovicaos), stpp_pdvos=if(pdvos>0,stpp_pdvos+pdvos,stpp_pdvos),stpp_osnovicaps=if(osnovicaps>0,stpp_osnovicaps+osnovicaps,stpp_osnovicaps), stpp_pdvps=if(pdvps>0,stpp_pdvps+pdvps,stpp_pdvps),
          stsp_osnovicaos=if(osnovicaos<0 and eeopdv_avans=0,stsp_osnovicaos+osnovicaos,stsp_osnovicaos), stsp_pdvos=if(pdvos<0 and eeopdv_avans=0,stsp_pdvos+pdvos,stsp_pdvos),stsp_osnovicaps=if(osnovicaps<0 and eeopdv_avans=0,stsp_osnovicaps+osnovicaps,stsp_osnovicaps), stsp_pdvps=if(pdvps<0 and eeopdv_avans=0,stsp_pdvps+pdvps,stsp_pdvps),
          stspav_osnovicaos=if(osnovicaos<0 and eeopdv_avans=1,stspav_osnovicaos+osnovicaos,stspav_osnovicaos), stspav_pdvos=if(pdvos<0 and eeopdv_avans=1,stspav_pdvos+pdvos,stspav_pdvos),stspav_osnovicaps=if(osnovicaps<0 and eeopdv_avans=1,stspav_osnovicaps+osnovicaps,stspav_osnovicaps), stspav_pdvps=if(pdvps<0 and eeopdv_avans=1,stspav_pdvps+pdvps,stspav_pdvps);    

    
    insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), sum(osnovicaos+osnovicaps), datpdv, sum(osnovicaos) as oos , sum(osnovicaps), sum(pdvos+pdvps) as spdv, sum(ukupno), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
          eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0 and not (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5)  group by popdv_promet.originalbrnal having spdv>0;    

    
    insert into my_eeopdv_pojedinacna select year(datpdv), MONTH(popdv_promet.datpdv), concat(right(zagodinu,2),'-',REPLACE(originalbrnal,'-RZ','')), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
    eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',originalbrnal), eeopdv_opis), ABS(sum(pdvos+pdvps)) as pdvuk, datpdv, ABS(sum(osnovicaos)) as oos , ABS(sum(osnovicaps)),
    sum(ABS(osnovicaos)*(getpdv('S1',datpdv)/100) + ABS(osnovicaps)*(getpdv('S2',datpdv)/100)) as spdv, sum(ABS(osnovicaos)*(1+(getpdv('S1',datpdv)/100))+abs(osnovicaps)*(1+(getpdv('S2',datpdv)/100))), 0, 0, 0, null,
    eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(osnovicaos)*(getpdv('S1',datpdv)/100)), sum(ABS(osnovicaps)*(getpdv('S2',datpdv)/100)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
          from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
          where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=6 and potvrdjeno=1 and status=1 and stornirano=0 group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0 and pdvuk=0;
        
    
    insert into my_eeopdv_pojedinacna select year(datpdv), MONTH(popdv_promet.datpdv), concat(right(zagodinu,2),'-',REPLACE(originalbrnal,'-RZ','')), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
    eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',originalbrnal), eeopdv_opis), ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)), datpdv,
    ABS(sum(pdvos/(getpdv('S1',datpdv)/100))) as oos , ABS(sum(pdvps/(getpdv('S2',datpdv)/100))),sum(ABS(pdvos) + ABS(pdvps)) as spdv,ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)),
     0, 0, 0, null, eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(pdvos)), sum(ABS(pdvps)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
          from my_eeopdv, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
          where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=6 and potvrdjeno=1 and status=1 and stornirano=0 
          group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;  
   
   
    insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',popdv_promet.originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
    if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.originalbrnal), eeopdv_opis), sum(if(ukupno>0,ukupno,0)), datpdv, sum(if(osnovicaos>0,osnovicaos,0)), sum(if(osnovicaps>0,osnovicaps,0)),
    sum(pdvos+pdvps), sum(if(ukupno>0,ukupno,0)), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from my_eeopdv, popdv_promet 
          left join kupci on popdv_promet.sifpar=kupci.sifra            
          WHERE month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0          
          AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and NOT (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g') group by popdv_promet.originalbrnal;

  
    insert into my_eeopdv_pojedinacna select godina, period, concat(right(zagodinu,2),'-',popdv_promet.originalbrnal), eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
    if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), zukupno, datpdv, zosnovicaos, zosnovicaps,
    (zpdvos+zpdvps), zukupno, 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, zpdvos, zpdvps, eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from my_eeopdv, popdv_promet 
          left join kupci on popdv_promet.sifpar=kupci.sifra 
          left join (select originalbrnal, sum(if(ukupno>0,ukupno,0)) AS zukupno, sum(if(osnovicaos>0,osnovicaos,0)) AS zosnovicaos, sum(if(osnovicaps>0,osnovicaps,0)) AS zosnovicaps, sum(pdvos) as zpdvos, sum(pdvps) as zpdvps 
          from popdv_promet where stornirano = 0 and (left(popdvid,2) = '8b' or left(popdvid,2) = '8g') group by originalbrnal) as popdv_zbir on popdv_zbir.originalbrnal = popdv_promet.originalbrnal
          WHERE month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0 
          AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g')
          group by popdv_promet.originalbrnal;  
  end if;

  
  update my_eeopdv_zbirna set smi_osnovicaos=abs(smi_osnovicaos),smi_pdvos=abs(smi_pdvos),smi_osnovicaps=abs(smi_osnovicaps),smi_pdvps=abs(smi_pdvps),smiav_osnovicaos=abs(smiav_osnovicaos),smiav_pdvos=abs(smiav_pdvos),smiav_osnovicaps=abs(smiav_osnovicaps),smiav_pdvps=abs(smiav_pdvps),
    smp_osnovicaos=abs(smp_osnovicaos),smp_pdvos=abs(smp_pdvos),smp_osnovicaps=abs(smp_osnovicaps),smp_pdvps=abs(smp_pdvps),smpav_osnovicaos=abs(smpav_osnovicaos),smpav_pdvos=abs(smpav_pdvos),smpav_osnovicaps=abs(smpav_osnovicaps),smpav_pdvps=abs(smpav_pdvps),
    stsi_osnovicaos=abs(stsi_osnovicaos),stsi_pdvos=abs(stsi_pdvos),stsi_osnovicaps=abs(stsi_osnovicaps),stsi_pdvps=abs(stsi_pdvps),stsiav_osnovicaos=abs(stsiav_osnovicaos),stsiav_pdvos=abs(stsiav_pdvos),stsiav_osnovicaps=abs(stsiav_osnovicaps),stsiav_pdvps=abs(stsiav_pdvps),
    stsp_osnovicaos=abs(stsp_osnovicaos),stsp_pdvos=abs(stsp_pdvos),stsp_osnovicaps=abs(stsp_osnovicaps),stsp_pdvps=abs(stsp_pdvps),stspav_osnovicaos=abs(stspav_osnovicaos),stspav_pdvos=abs(stspav_pdvos),stspav_osnovicaps=abs(stspav_osnovicaps),stspav_pdvps=abs(stspav_pdvps);  
  
  
    update my_eeopdv,(select period as mymesec, sum(smi_pdvos+smi_pdvps+smiav_pdvos+smiav_pdvps+smp_pdvos+smp_pdvps+smpav_pdvos+smpav_pdvps+stsi_pdvos+stsi_pdvps+stsiav_pdvos+stsiav_pdvps+stsp_pdvos+stsp_pdvps+stspav_pdvos+stspav_pdvps) as ukupanpdvsmanjenje
    from my_eeopdv_zbirna group by period) as ukupnosmanjenje set smanjenje=smanjenje+ukupanpdvsmanjenje  
    where ukupnosmanjenje.mymesec=my_eeopdv.period and tipevidencije=0 and status=1;

    
    update my_eeopdv,(select period as mymesec, sum(poi_pdvos+poi_pdvps+pop_pdvos+pop_pdvps+stpi_pdvos+stpi_pdvps+stpp_pdvos+stpp_pdvps) as ukupanpdvpovecanje
    from my_eeopdv_zbirna group by period) as ukupnopovecanje set uvecanje=uvecanje+ukupanpdvpovecanje
    where ukupnopovecanje.mymesec=my_eeopdv.period and tipevidencije=0 and status=1;

  
  update my_eeopdv_pojedinacna left join (select originalbrnal, popdvid from popdv_promet where popdvid = '4.2.4') as mypopdv_promet on my_eeopdv_pojedinacna.biznisoftbrnal=mypopdv_promet.originalbrnal, my_eeopdv 
  set osnovicaos = pdvvs/(getpdv('S1',datprom)/100), osnovicans = pdvns/(getpdv('S2',datprom)/100) 
  where my_eeopdv_pojedinacna.period=my_eeopdv.period and my_eeopdv.status<2 and my_eeopdv.tipevidencije=1 and mypopdv_promet.popdvid = '4.2.4' and (osnovicaos=0 and osnovicans=0);

  
  update my_eeopdv_pojedinacna, my_eeopdv, 
  (select originalbrnal,eeopdv_avansi, sum(osnovicaos) as osnovicaos, sum(osnovicaps) as osnovicaps, sum(bezodbitka) as bezodbitka from popdv_promet where (left(popdvid,3)='3a.' or left(popdvid,3)='8b.' or left(popdvid,3)='8g.') and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD')  group by originalbrnal) as popdv_promet     
     set my_eeopdv_pojedinacna.osnovicaos=my_eeopdv_pojedinacna.osnovicaos+popdv_promet.osnovicaos, my_eeopdv_pojedinacna.osnovicans=my_eeopdv_pojedinacna.osnovicans+popdv_promet.osnovicaps, odbitak=if(bezodbitka=0, 2, 0)
       where my_eeopdv_pojedinacna.godina=my_eeopdv.godina and my_eeopdv_pojedinacna.period=my_eeopdv.period and my_eeopdv.status<2 and my_eeopdv.tipevidencije=1 and my_eeopdv_pojedinacna.biznisoftbrnal=popdv_promet.originalbrnal AND (tipdok=4 or tipdok=5) and (osnovodabira = 2 or tipvzdokumenta=0) and pravac=1;
  



  update my_eeopdv_pojedinacna, my_eeopdv set ukupno=osnovicaos+osnovicans+pdv, ukupnonaknada=osnovicaos+osnovicans+pdv
  where my_eeopdv_pojedinacna.godina=my_eeopdv.godina and my_eeopdv_pojedinacna.period=my_eeopdv.period and my_eeopdv.status<2 and my_eeopdv.tipevidencije=1 and pravac=1 AND (tipdok=4 or tipdok=5) and (osnovodabira = 2 or tipvzdokumenta=0);

  
  update my_eeopdv_pojedinacna set ukupnonaknada=osnovicaos+pdvvs+osnovicans+pdvns where pravac=0 AND ukupnonaknada<(osnovicaos+pdvvs+osnovicans+pdvns);

  
  delete from my_eeopdv where tipevidencije=0 and status<2 and smanjenje=0 and uvecanje=0 and (select count(*) from my_eeopdv_zbirna where my_eeopdv.godina=my_eeopdv_zbirna.godina and my_eeopdv.period=my_eeopdv_zbirna.period)=0;
  delete from my_eeopdv where tipevidencije=1 and status<2 and (select count(*) from my_eeopdv_pojedinacna where my_eeopdv.godina=my_eeopdv_pojedinacna.godina and my_eeopdv.period=my_eeopdv_pojedinacna.period)=0;

  
  update my_eeopdv_pojedinacna set brintracuna = null where not (tipdok = 4 or tipdok = 5);

  drop temporary table if exists tmp_ez_popdv_promet;
END
```

---

## 17. creeeopdv_pz

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `creeeopdv_pz`(zagodinu int(4), tromesecni int(1))
BEGIN
  if tromesecni=1 then
    insert ignore into my_eeopdv set godina=zagodinu, period=21, mesec=3, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=22, mesec=6, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=23, mesec=9, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=24, mesec=12,status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=21, mesec=3, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=22, mesec=6, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=23, mesec=9, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=24, mesec=12,status=1, tipevidencije=1;
  else
    insert ignore into my_eeopdv set godina=zagodinu, period=1, mesec=1, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=2, mesec=2, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=3, mesec=3, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=4, mesec=4, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=5, mesec=5, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=6, mesec=6, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=7, mesec=7, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=8, mesec=8, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=9, mesec=9, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=10, mesec=10, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=11, mesec=11, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=12, mesec=12, status=1, tipevidencije=0;
    insert ignore into my_eeopdv set godina=zagodinu, period=1, mesec=1, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=2, mesec=2, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=3, mesec=3, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=4, mesec=4, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=5, mesec=5, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=6, mesec=6, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=7, mesec=7, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=8, mesec=8, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=9, mesec=9, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=10, mesec=10, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=11, mesec=11, status=1, tipevidencije=1;
    insert ignore into my_eeopdv set godina=zagodinu, period=12, mesec=12, status=1, tipevidencije=1;
  end if;
END
```

---

## 18. creeeppdvp

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `creeeppdvp`(zagodinu int(4), tromesecni int(1))
BEGIN
  if tromesecni=1 then
    insert ignore into smy_eeppdv set godina=zagodinu, period=21, mesec=3, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=22, mesec=6, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=23, mesec=9, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=24, mesec=12,status=1;
  else
    insert ignore into smy_eeppdv set godina=zagodinu, period=1, mesec=1, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=2, mesec=2, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=3, mesec=3, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=4, mesec=4, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=5, mesec=5, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=6, mesec=6, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=7, mesec=7, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=8, mesec=8, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=9, mesec=9, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=10, mesec=10, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=11, mesec=11, status=1;
    insert ignore into smy_eeppdv set godina=zagodinu, period=12, mesec=12, status=1;
  end if;
END
```

---

## 19. CreTmpSerbr

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `CreTmpSerbr`(insbr varchar(50), inpartner varchar(5), inartikal varchar(6), datumod date, datumdo date, godina int(5))
BEGIN
  DECLARE s_sifra varchar(2);
  DECLARE s_tabela varchar(100);
  DECLARE whrserbr varchar(250);
  DECLARE whrartikal varchar(250);
  DECLARE whrpartner varchar(250);




  IF NOT (insbr='') THEN
    SET whrserbr:=concat(' and proveraprijema.serbr like "',insbr,'"');
  ELSE
    SET whrserbr:='';
  END IF;
  IF NOT (inpartner='') THEN
    SET whrpartner:=concat(' and proveraprijema.partner="',inpartner,'"');
  ELSE
    SET whrpartner:='';
  END IF;
  IF NOT (inartikal='') THEN
    SET whrartikal:=concat(' and proveraprijema.sifra="',inartikal,'"');
  ELSE
    SET whrartikal:='';
  END IF;

  DROP TEMPORARY TABLE IF EXISTS tmp_serbr;
  CREATE TEMPORARY TABLE tmp_serbr LIKE serbr;
  alter table tmp_serbr add godina int(5);
  alter table tmp_serbr drop primary key;
  alter table tmp_serbr add primary key(sifobj, sifra, serbr, brnal, godina);
  SET @aa=CONCAT('INSERT INTO tmp_serbr select * from (SELECT serbr.*,',godina,' FROM serbr) as proveraprijema where 1',whrserbr, whrpartner, whrartikal,' and datnal>="', datumod,'" and datnal<="', datumdo,'" and stornirano=0');
  PREPARE stmt FROM @aa; EXECUTE stmt;
 


  
  Alter table tmp_serbr add column vpcena double(15,2);
  update tmp_serbr, robno set tmp_serbr.vpcena = robno.cenabezpp where tmp_serbr.brnal=robno.brnal and tmp_serbr.sifra;

  IF NOT (inpartner='') THEN
    SET @aa=CONCAT('DELETE from tmp_serbr where partner<>"',inpartner,'"');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  END IF;

END
```

---

## 20. cre_pregled_eeppdv

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `cre_pregled_eeppdv`(zabrnal varchar(100), zagodinu integer, zaperiod integer, sufix integer)
BEGIN
  declare mywhere varchar(100);
  set mywhere='';
  
  if trim(zabrnal)='' then
    set @zabrnalxx = '%';
    set zabrnal='XXXXXXXXXX';
    set mywhere=concat(' and ', @eeppdv_promet_tabela,'.godina=',zagodinu,' and ', @eeppdv_promet_tabela,'.period=',zaperiod,' ');
  else
    set @zabrnalxx = concat(zabrnal,'/%');
    set mywhere='';
  end if;

  set @ima11=0; set @ima12=0; set @ima13=0; set @ima14=0; set @ima15=0; set @ima16=0; set @ima21=0; set @ima22=0; set @ima23=0; set @ima24=0; set @ima25=0; set @ima26=0; set @ima31=0; set @ima41=0; set @ima51=0; set @ima52=0;

  drop temporary table if exists tmp_pregled_eeppdv;
  create temporary table tmp_pregled_eeppdv (izvor varchar(100) not null primary key, izvorname varchar(1000) not null,  osnovicaos double(15,2) default 0, pdvos double(15,2) default 0, osnovicans double(15,2) default 0, pdvns double(15,2) default 0);

  set @qvr=concat('select count(*) into @hasitems from (select izvor from ', @eeppdv_promet_tabela, ' where (replace(brnal,''-RZ'','''')="',zabrnal,'" or brnal like @zabrnalxx)',mywhere,' and stornirano=0 and izvor like "1.1.%" limit 1) as tmpok1');
  PREPARE stmt1 FROM @qvr; EXECUTE stmt1; DEALLOCATE PREPARE stmt1;
```

---

## 21. cre_tmp_pojedinacna

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `cre_tmp_pojedinacna`(zagodinu int(4), zaperiod int(2))
begin
  drop temporary table if exists tmp1_eeopdv_pojedinacna;
  
  create temporary table tmp1_eeopdv_pojedinacna (primary key my_pkey(godina,period,brnal,rbrst)) as select eeopdv_pojedinacna.* from eeopdv_pojedinacna,(select getosnovnibrnal(brnal) as mybrnal,max(if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))) as mymax from eeopdv_pojedinacna where godina=zagodinu and period=zaperiod group by mybrnal) as maxrecords
    where godina=zagodinu and period=zaperiod and getosnovnibrnal(eeopdv_pojedinacna.brnal)=maxrecords.mybrnal and if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))=maxrecords.mymax 
      and eeopdv_pojedinacna.biznisoftbrnal in (select eeopdv_pojedinacna.biznisoftbrnal
        from eeopdv_pojedinacna left join veznaefakture on veznaefakture.brnal=eeopdv_pojedinacna.biznisoftbrnal and primljena=0 and eeopdv_pojedinacna.uslov=1
        where godina=zagodinu and period=zaperiod and status_evidencije=0 and 
        if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg)),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status)))
        group by godina,period,eeopdv_pojedinacna.biznisoftbrnal)  group by godina,period,getosnovnibrnal(eeopdv_pojedinacna.brnal);
  
  update tmp1_eeopdv_pojedinacna set brnal=getosnovnibrnal(brnal);
  
  update tmp1_eeopdv_pojedinacna,(select getosnovnibrnal(brnal) as mybrnal,max(individualVatId) as mymax from eeopdv_pojedinacna where godina=zagodinu and period=zaperiod group by mybrnal) as maxrecords
    set tmp1_eeopdv_pojedinacna.individualvatid=maxrecords.mymax where tmp1_eeopdv_pojedinacna.brnal=maxrecords.mybrnal;
  
  update tmp1_eeopdv_pojedinacna, (select godina, period, getosnovnibrnal(brnal) as brnal, sum(ukupnonaknada) as ukupnonaknada, sum(osnovicaos) as osnovicaos, sum(osnovicans) as osnovicans, sum(pdv) as pdv, sum(pdvvs) as pdvvs, sum(pdvns) as pdvns from eeopdv_pojedinacna where godina=zagodinu and period=zaperiod group by godina, period, getosnovnibrnal(brnal)) as mypromet
    set tmp1_eeopdv_pojedinacna.ukupnonaknada=mypromet.ukupnonaknada, tmp1_eeopdv_pojedinacna.osnovicaos=mypromet.osnovicaos, tmp1_eeopdv_pojedinacna.osnovicans=mypromet.osnovicans, tmp1_eeopdv_pojedinacna.pdv=mypromet.pdv, tmp1_eeopdv_pojedinacna.pdvvs=mypromet.pdvvs, tmp1_eeopdv_pojedinacna.pdvns=mypromet.pdvns
      where tmp1_eeopdv_pojedinacna.godina=mypromet.godina and tmp1_eeopdv_pojedinacna.period=mypromet.period AND tmp1_eeopdv_pojedinacna.brnal=mypromet.brnal;
end
```

---

## 22. dajmidokumente

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `dajmidokumente`(`tip` int, `sifra` int, `period` boolean, `periodOd` date, `periodDo` date, `operater` varchar(50))
BEGIN
  DECLARE mySifra varchar(2);
  DECLARE myNaziv varchar(150);
  DECLARE myTabela varchar(50);
  DECLARE myTipKljuca int(2);
  DECLARE myTipdokfakt varchar(1);
  DECLARE myDobavljac varchar(10);
  DECLARE myWhere varchar(255);
  DECLARE myKolone varchar(50);
  DECLARE myPolja varchar(20);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE queryCursor CURSOR FOR SELECT * FROM tmp_table;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS tmp_table;
  SET @tmptable = CONCAT('CREATE temporary table tmp_table as select sifra, naziv, tabela, tipkljuca, tipdokfakt from ', @bsliveid, 'opp.documents');
  PREPARE stmt FROM @tmptable;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
  OPEN queryCursor;
  CALL pripremitabele();
  
  SET done = FALSE;
   read_loop:
   LOOP FETCH queryCursor INTO mySifra, myNaziv, myTabela, myTipKljuca, myTipdokfakt;
   SET @ins= '';
   SET myKolone = ' 0, 0 ';
   set @mytabelanazivx = myTabela;

  IF myTipKljuca = 1 THEN
    SET myPolja = 'defpopdvid';
    IF tip = 1 THEN SET myWhere = CONCAT(' dobavljac=', sifra, ' '); END IF;
    IF NOT (mySifra = 'IP' AND tip = 1) THEN
      IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
      IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
      IF tip = 4 THEN SET myWhere = CONCAT('operater=', QUOTE(operater)); END IF;
      IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                      SET myKolone = ' sum(kolicina), cena';
                      SET myPolja = 'popdvid'; END IF;
      IF period THEN SET myWhere = CONCAT(myWhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
      SET myDobavljac = 'dobavljac';
       IF mySifra = 'IP' THEN SET myDobavljac = 'NULL'; END IF;
        IF tip = 1 THEN
          SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ' , QUOTE(myNaziv), ', sifobj, dobavljac, ',
                            'CONCAT(', QUOTE(mySifra), ', ',  ' RIGHT(CONCAT(''000'', sifobj), 3), ''-'', RIGHT(CONCAT(''00000'', brkalk), 5))',
                            ', SUM(nabvrednost), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                            ', brdok, 0, 0, NULL, 0, ',myPolja, ', brkalk, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 1 FROM ', myTabela,' WHERE ', myWhere, ' GROUP BY sifobj, brkalk;');                                                           
        ELSE
          SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ' , QUOTE(myNaziv), ', sifobj, ', myDobavljac,
                            ', CONCAT(', QUOTE(mySifra), ', ', ' RIGHT(CONCAT(''000'', sifobj), 3), ''-'', RIGHT(CONCAT(''00000'', brkalk), 5))',
                            ', SUM(vrednostsapp), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                            ', brdok, 0, 0, NULL, 0, ',myPolja, ', brkalk, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 1 FROM ', myTabela, ' WHERE ', myWhere, ' GROUP BY sifobj, brkalk;');
        END IF;
    END IF;
  END IF;

  IF myTipKljuca = 2 THEN
    SET @myPolja = 'defpopdvid';
    IF myTabela = 'tblpovracaj' THEN SET myPolja = 'knjizenourobnom'; ELSE SET myPolja = '0'; END IF;
    IF tip = 1 THEN SET mywhere = CONCAT(' sifkup=', sifra, ' '); END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                    SET myKolone = ' sum(kolicina), cena';
                    SET @myPolja = 'popdvid'; END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, sifkup, '
                      ,'CONCAT(', QUOTE(mySifra), ', ', ' RIGHT(CONCAT(''000'', sifobj), 3), RIGHT(CONCAT(''000000'', brrn), 6))',
                      ', SUM(vredkupac), status, datum, NULL, operater, prctran, IF(prctran > 0, (SELECT teren FROM posljed WHERE sifpar=',
                      myTabela, '.sifkup AND sifra=', myTabela, '.prctran), (SELECT teren FROM kupci WHERE sifra=',
                      myTabela, '.sifkup)), IF(prctran > 0, (SELECT komercijalista FROM posljed WHERE sifpar=',
                      myTabela, '.sifkup AND sifra=', myTabela, '.prctran), (SELECT komercijalista FROM kupci WHERE sifra=',
                      myTabela, '.sifkup)), dostava, IF(prctran > 0, (SELECT sortstampe FROM posljed WHERE sifpar=', myTabela,
                      '.sifkup AND sifra=', myTabela, '.prctran), (SELECT sortstampe FROM kupci WHERE sifra=',
                      myTabela, '.sifkup)),', myKolone, ', brdok, ', myPolja,', IF(LEFT(brdok, 2) = ''@@'', 1, 0), tip, akcc, ', @myPolja,', 0, potvrdjeno, stornirano, datum, datumslanja, null, null, datpdv, null, 0, 2 FROM ',
                      myTabela, ' WHERE tip=', QUOTE(myTipdokfakt),
                      ' AND', myWhere, ' GROUP BY sifobj, brrn, tip;');
  END IF;

  IF myTipKljuca = 3 THEN
  SET myKolone = ' 0, 0 ';
    IF tip = 1 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 2 THEN
      IF mySifra = 'II' THEN
        SET myWhere = CONCAT(' sifobj=', sifra, ' ');
         ELSE
        SET myWhere = CONCAT(' ((sifobj=', sifra, ')', ' OR (obj2=', sifra, ')) ');
      END IF;
    END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                    SET myKolone = ' sum(kolicina), cena'; END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, NULL, ',
                      'CONCAT(', QUOTE(mySifra), ', ', ' RIGHT(CONCAT(''000'', sifobj), 3), RIGHT(CONCAT(''000000'', brrn), 6))',
                      ', SUM(kolicina * cena), status, datum, obj2, operater, NULL, (SELECT teren FROM objekti WHERE objekti.sifra = obj2),
                      NULL, dostava, (SELECT sortstampe FROM objekti WHERE objekti.sifra = obj2),', myKolone,
                      ', brdok, 0, 0, NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, null, null, 0, 3 FROM ', myTabela, ' WHERE ', myWhere,
                      ' GROUP BY sifobj, brrn;');
  END IF;

  IF myTipKljuca = 15 THEN
  SET myKolone = ' 0, 0 ';
    IF tip = 1 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' ',mytabela,'.operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = ' 0 '; END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND if(isnull(datobracuna), datnal, datobracuna) >= ', QUOTE(periodOd), ' AND if(isnull(datobracuna), datnal, datobracuna) <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, NULL, ',
                      'biznisoftbrnal',
                      ', SUM(iznosrsd), status, if(isnull(datobracuna), datnal, datobracuna), null, putninalog.operater, NULL, null,
                      NULL, null,0,', myKolone,
                      ', null, 0, 0, NULL, 0, NULL, 0, potvrdjeno, null, null, null, null, null, null, null, 0, 3 FROM ', myTabela, ' left join putninalog_spectr on putninalog.tip=putninalog_spectr.tip and putninalog.broj=putninalog_spectr.broj WHERE ', myWhere,
                      ' and biznisoftbrnal like "',mysifra,'%"  GROUP BY biznisoftbrnal;');
  END IF;

  IF myTipKljuca = 4 THEN
    IF tip = 1 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                    SET myKolone = ' sum(kolicina), novacena'; END IF;
    IF period THEN SET myWhere = CONCAT(mywhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, NULL, '
                      'CONCAT(', QUOTE(mySifra), ', ', ' RIGHT(CONCAT(''000'', sifobj), 3), ''-'', RIGHT(CONCAT(''0000'', brnivel), 4))',
                      ', SUM((kolicina * novacena) - (kolicina * staracena)), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                      ', brdok, 0, 0, NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, null, null, 0, 4 FROM ',
                      myTabela, ' WHERE ', myWhere, ' GROUP BY sifobj, brnivel;');
  END IF;

  IF myTipKljuca = 5 THEN
    IF tip = 1 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                    SET myKolone = ' sum(kolicina), cena '; END IF;
    IF period THEN SET myWhere = CONCAT(mywhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, NULL, '
                      'CONCAT(', QUOTE(mySifra), ', ', ' RIGHT(CONCAT(''000'', sifobj), 3), ''-'', RIGHT(CONCAT(''0000'', brpop), 4))',
                      ', SUM(novakolicina * cena), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone, ', NULL, 0, 0, NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, null, null, 0, 5 FROM ',
                      myTabela, ' WHERE ', myWhere, ' GROUP BY sifobj, brpop;');
  END IF;

  IF myTipKljuca = 6 THEN
    IF tip = 1 THEN SET myWhere = CONCAT(' kupac=''P-', RIGHT(CONCAT('00000', sifra), 5), ''''); END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF tip = 5 THEN SET myWhere = CONCAT(' sifra=', sifra, ' ');
                    SET myKolone = ' sum(kolicina), cena '; END IF;
    IF period THEN SET myWhere = CONCAT(mywhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj,  RIGHT(kupac, 5),
                      CONCAT(''KA-'', brdok), SUM(vredkupac), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                      ', NULL, 0, 0, NULL, 0, NULL, 0, if(status=99,0,1), 0, null, null, null, null, null, null, 0, 6 FROM ',
                      myTabela, ' WHERE brdok <> ''MPR.RN.'' AND NOT ISNULL(brdok) AND ', myWhere, ' GROUP BY sifobj, brrn, datum, operater;');
  END IF;

  IF myTipKljuca = 8 AND NOT tip = 5 THEN
    IF tip = 1 THEN SET myWhere = CONCAT(' dt_srv_rn.sifpar=', sifra); END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' dt_srv_rnpojed.sifobj=', sifra); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' oper_primio=', QUOTE(operater)); END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datrnal >= ', QUOTE(periodOd), ' AND datrnal <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', dt_srv_rnpojed.sifobj, dt_srv_rn.sifpar,
                      CONCAT(''SN'', RIGHT(CONCAT(''000'', dt_srv_rnpojed.sifobj), 3), ''-'', RIGHT(CONCAT(''00000'', dt_srv_rnpojed.brnal), 5),
                      ''-'', RIGHT(CONCAT(''00'', dt_srv_rnpojed.rbr),2)), 0, status_rn, datrnal, NULL, oper_primio, ', REPEAT('NULL, ', 4),'0,', myKolone,
                      ', NULL, 0, 0, NULL, 0, NULL, 0, 1, 0, null, null, null, null, null, null, 0, 8 FROM
                      dt_srv_rn ,dt_srv_rnpojed WHERE dt_srv_rnpojed.brnal = dt_srv_rn.brnal AND ', myWhere,
                      ' GROUP BY dt_srv_rnpojed.sifobj, dt_srv_rnpojed.brnal, dt_srv_rnpojed.rbr;');
  END IF;

  IF myTipKljuca = 9 AND NOT tip = 5 THEN
    IF tip = 1 THEN SET myWhere = CONCAT(' analitika=''P-', RIGHT(CONCAT('00000', sifra, ''''), 5)); END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj,
                      IF(analitika LIKE ''P-%'', RIGHT(analitika, 5), NULL), CONCAT(', QUOTE(mySifra), ', RIGHT(CONCAT(''000'', sifobj), 3),
                      RIGHT(CONCAT(''000000'', brnal), 6)), SUM(uplata - isplata), status, datum,
                      NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone, ', NULL, 0, 0, NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, null, null, 0, 9 FROM ', myTabela, ' WHERE ',
                      myWhere, ' GROUP BY sifobj, brnal;');
  END IF;

  IF myTipKljuca = 10 AND NOT tip = 5 THEN
    IF mySifra = 'RD' THEN
     IF tip = 1 THEN SET myWhere = CONCAT(' (narucilac=', sifra, ' OR primalac=', sifra, ') '); END IF;
     IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
     IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
     IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
     IF period THEN SET myWhere = CONCAT(myWhere, ' AND datnal >= ', QUOTE(periodOd), ' AND datnal <= ', QUOTE(periodDo)); END IF;
     SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, NULL, gnbrnal,
                       SUM(kolicina), status, datnal, sifobjmgp, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                       ', NULL, 0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 10 FROM ', myTabela,
                       ' WHERE ', myWhere, ' GROUP BY gnbrnal;');
    END IF;
  END IF;

  IF myTipKljuca = 11 AND NOT tip = 5 THEN
    IF tip = 1 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 2 THEN SET myWhere = CONCAT(' sifobj=', sifra, ' '); END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
    SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', sifobj, sifpolj,
                      CONCAT(''PPPL'', RIGHT(CONCAT(''000'', sifobj), 3), RIGHT(CONCAT(''00000'', brkalk), 5), brpl),
                      SUM(iznos), status, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                      ', brdok, 0, 0, NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, datpdv, null, 0, 11 FROM ', myTabela, ' WHERE ',
                      myWhere, ' GROUP BY sifobj, brkalk, brpl;');
  END IF;

  IF myTipKljuca = 13 AND NOT tip = 5 THEN
  IF myTabela = 'frmgk_osnsred' OR 'frmgk_troskovi' THEN SET myPolja = 'nefakturisano'; ELSE SET myPolja = '0'; END IF;
    IF tip = 1 THEN SET myWhere = CONCAT(' dobavljac=', sifra); END IF;
    IF tip = 2 THEN SET myWhere = ' 0 '; END IF;
    IF tip = 3 THEN SET myWhere = ' 1 '; END IF;
    IF tip = 4 THEN SET myWhere = CONCAT(' operater=', QUOTE(operater)); END IF;
    IF period THEN SET myWhere = CONCAT(myWhere, ' AND datnal >= ', QUOTE(periodOd), ' AND datnal <= ', QUOTE(periodDo)); END IF;
      IF mySifra = 'TR' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''TR-'', frmgk_troskovi.brnal), SUM(IznosSaPDV), status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                        ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_troskovi,tr_finprom WHERE CONCAT(''TR-'', frmgk_troskovi.brnal) = tr_finprom.brnal AND ', myWhere,
                        ' GROUP BY frmgk_troskovi.brnal;');
      ELSEIF mySifra = 'OS' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''OS-'', frmgk_osnsred.brnal), SUM(IznosSaPDV), status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                        ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_osnsred, osnsred_spec WHERE CONCAT(''OS-'', frmgk_osnsred.brnal) = osnsred_spec.brnal AND ', myWhere,
                        ' GROUP BY frmgk_osnsred.brnal;');
      ELSEIF mySifra = 'AR' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''AR-'', frmgk_avans.brnal), SUM(IznosSaPDV), status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                        ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_avans, avans_spec WHERE CONCAT(''AR-'', frmgk_avans.brnal) = avans_spec.brnal AND ', myWhere,
                        ' GROUP BY frmgk_avans.brnal;');
      ELSEIF mySifra = 'FK' THEN
        IF tip = 1 THEN SET myWhere = CONCAT(' kupac=', sifra, ' ');
        SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, kupac,
                          CONCAT(''FK-'', frmgk_faktura.brnal), IznosSaPDV, status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                         ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, null, null, null, null, null, datpdv, 0, 99 FROM
                          frmgk_faktura WHERE ', myWhere, ' GROUP BY frmgk_faktura.brnal;');
        END IF;
      ELSEIF mySifra = 'ED' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''ED-'', frmgk_ed.brnal), IznosSaPDV, status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                       ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_ed WHERE ', myWhere, ' GROUP BY frmgk_ed.brnal;');
      ELSEIF mySifra = 'NR' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''NR-'', frmgk_nefak.brnal), IznosSaPDV, status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                        ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_nefak WHERE ', myWhere, ' GROUP BY frmgk_nefak.brnal;');
      ELSEIF mySifra = 'CR' THEN
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ', QUOTE(mySifra), ', ', QUOTE(myNaziv), ', NULL, dobavljac,
                        CONCAT(''CR-'', frmgk_carina.brnal), iznos_carine, status, datnal, NULL, operater, ', REPEAT('NULL, ', 4),'0,', myKolone,
                        ', brdok, 0, ', myPolja, ', NULL, 0, NULL, 0, potvrdjeno, stornirano, datprometa, datdok, datprih, iskazandatum, datpdv, idefakture, vrdokizvor, 13 FROM
                        frmgk_carina WHERE ', myWhere, ' GROUP BY frmgk_carina.brnal;');
      END IF;
   END IF;
   IF done THEN
           LEAVE read_loop;
        END IF;
    IF NOT @ins='' THEN
    PREPARE stmt1 FROM @ins;
    EXECUTE stmt1;
    END IF;
    END LOOP read_loop;
  CLOSE queryCursor;

  IF @AsociranjeLokacijePoDokumentima = 1 THEN 
      
      IF period THEN SET myWhere = CONCAT(' AND datnal >= ', QUOTE(periodOd), ' AND datnal <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''IZ'', ''IZVODI BANAKA'', NULL, NULL, biznisoftbrnal, SUM(izndug), status, datnal,
                        NULL, operater, posljed, NULL, komercijalista, NULL, 0, 0, 0, biznisoftbrnal, 0, 0, NULL, 0, NULL, rbrst, 0, stornirano, null, null, null, null, null, null, 0, 0 
                        FROM finprom WHERE vd = ''IZ''', mywhere, ' GROUP BY biznisoftbrnal');  
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
      
      
      IF period THEN SET myWhere = CONCAT(' AND periodod >= ', QUOTE(periodOd), ' AND perioddo <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''LD'', ''OBRAČUN ZARADA'', NULL, NULL, ', 
                        'CONCAT(''LD'', SUBSTRING(zagod, -2), ''-'', LPAD(zames, 2, ''0''), ''-'', rbzaper), ', 
                        '0, status, datval, NULL, operater, ', 
                        REPEAT('NULL, ', 4), '0, 0, 0, zames, 0, 0, NULL, 0, NULL, rbzaper, 0, 0, null, null, null, null, null, null, 0, 0  ', 
                        'FROM ld410 WHERE tipobr = 1', mywhere, ' GROUP BY tipobr, zagod, zames, rbzaper');  
  
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
      
      
      IF period THEN SET myWhere = CONCAT(' AND periodod >= ', QUOTE(periodOd), ' AND perioddo <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''LD1'', ''OBRAČUN OSTALIH LIČNIH PRIMANJA'', NULL, NULL, 
                        CONCAT(''LD1'', SUBSTRING(zagod, -2), ''-'', LPAD(zames, 2, ''0''), ''-'', rbzaper), 0, status, 
                        datval, NULL, operater, ', REPEAT('NULL, ', 4), '0, 0, 0, zames, 0, 0, NULL, 0, NULL, rbzaper, 0, 0, null, null, null, null, null, null, 0, 0  
                        FROM ld410 WHERE tipobr = 2', mywhere, ' GROUP BY tipobr, zagod, zames, rbzaper');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
    
      
      IF period THEN SET myWhere = CONCAT(' WHERE datval >= ', QUOTE(periodOd), ' AND datval <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''LDDV'', ''OBRAČUN ZA ISPLATU LICIMA VAN RADNOG ODNOSA'', NULL, NULL, 
                        CONCAT(''LDDV'', DATE_FORMAT(datval, ''%d%m''), ''-'', rbrugo),  
                        0, status, datval, NULL, operater, ', REPEAT('NULL, ', 4),'0, 0, 0, rbrobr, 0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 0  
                        FROM ldstav_ugod', mywhere, ' GROUP BY rbrugo, rbrobr');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
      
      
      IF period THEN SET myWhere = CONCAT(' WHERE datam >= ', QUOTE(periodOd), ' AND datam <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''AMSS'', ''OBRAČUN AMROTIZACIJE'', NULL, NULL, 
                        CONCAT(''AMSS-'', DATE_FORMAT(datam, ''%y%m%d''), ''-'', LPAD(rbr, 3, ''0'')),  
                        SUM(amvr * komada), 0, datcre, NULL, operater, ',   
                        REPEAT('NULL, ', 4), '0, 0, 0, rbrnab, 0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 0   
                        FROM osamvr', mywhere, ' GROUP BY osoznaka, invbroj, datam, rbramort, rbr');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
    
      
      IF period THEN SET myWhere = CONCAT(' WHERE datdok >= ', QUOTE(periodOd), ' AND datdok <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''BSKOMP'', ''KOMPENZACIJE SA PARTNERIMA'', NULL, NULL,
                        CONCAT(''BSKOMP-'', LPAD(brkomp, 5, ''0'')), iznos, 0, datdok, NULL, operater, ', 
                        REPEAT('NULL, ', 4),'0, 0, 0, rbr, 0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 0  
                        FROM tblkompenzacije', mywhere, ' GROUP BY brkomp, tip, rbr');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
    
      
      IF period THEN SET myWhere = CONCAT(' WHERE datum >= ', QUOTE(periodOd), ' AND datum <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''ADM'', ''PRODAJA ADM.ZABRANOM I KURUR.SLUŽBAMA'', NULL, NULL, biznisoftbrnal, 
                        SUM(uplata + isplata), 0, datum, NULL, operater, ', REPEAT('NULL, ', 4),'0, 0, 0, brojracuna, 0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 0  
                        FROM kredprom', mywhere, ' GROUP BY id having biznisoftbrnal<>''''');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1;
    
      
      IF period THEN SET myWhere = CONCAT(' WHERE datrefr >= ', QUOTE(periodOd), ' AND datrefr <= ', QUOTE(periodDo)); END IF;
      SET @ins = CONCAT('INSERT INTO pregltrans SELECT ''REF'', ''EVIDENCIJA ZPPPDV REFUNDACIJA'', NULL, NULL, 
                        CONCAT(''REF'', LPAD(sifobj, 3, ''0''), ''-'', LPAD(evbr, 5, ''0'')), 
                        SUM(iznosbezpdv + iznospdv), 0, datrefr, NULL, operater, ', REPEAT('NULL, ', 4),'0, 0, 0, evbr,
                        0, 0, NULL, 0, NULL, 0, 0, 0, null, null, null, null, null, null, 0, 0  FROM ref4', mywhere, ' GROUP BY sifobj, evbr');                     
      PREPARE stmt1 FROM @ins;
      EXECUTE stmt1; 
  END IF; 

  IF @PregledPoLokacijama = 1 THEN
    
    delete pregltrans.* from pregltrans left join arh_doc_locations on pregltrans.brnal=arh_doc_locations.brnal where isnull(arh_doc_locations.brnal) or trim(arh_doc_locations.brnal)='';
    
    delete pregltrans.* from pregltrans,arh_doc_locations left join tmp_ahr_t1 on arh_doc_locations.locUUID=tmp_ahr_t1.arhuuid where pregltrans.brnal=arh_doc_locations.brnal and  isnull(tmp_ahr_t1.arhuuid) or trim(tmp_ahr_t1.arhuuid)='';
  END IF; 

  IF isnull(@PregledBezAlter) then
    ALTER TABLE pregltrans ADD extdoc int(1) DEFAULT 0, ADD potpdoc int(1) DEFAULT 0, ADD potpdocnum int(4) DEFAULT 0, ADD boja varchar(50) DEFAULT 0;
    ALTER TABLE pregltrans ORDER BY datum, brnal;
  end if;
END
```

---

## 23. DaLiJeUAvansuOPP

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `DaLiJeUAvansuOPP`(parkonto varchar(50),parsifpar varchar(50), nadan date, iznos double, baza varchar(50))
BEGIN
  declare jeste,p integer;
  set jeste = 0;
  set @jesteuavansu=jeste;
  set @nadanx=nadan;
  
  SET @aa=CONCAT('select tabrac.konto into @mykonto from ',baza,'.tabrnoperative, ',baza,'.tabrac  where tabrac.sifrakpl=@kontniplan and tabrac.sifra=tabrnoperative.racun and tabrnoperative.status=1 
    and tabrac.konto not in (select tabrac.konto from tabrnavansa, tabrac where tabrac.sifrakpl=@kontniplan and tabrac.sifra=tabrnavansa.racun and tabrnavansa.status=1) group by tabrac.konto having tabrac.konto=',parkonto);
  PREPARE stmt FROM @aa; EXECUTE stmt;
  SELECT FOUND_ROWS() INTO p;
  IF p>0 THEN
    SET @aa=CONCAT('select sum(izndug-iznpot) into @mysaldo from ',baza,'.finprom where racun=@mykonto and brdok="',parsifpar,'" and datnal<=@nadanx and stornirano=0');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    if (@mysaldo+iznos)>0 then
      set jeste = 1;
    end if;
  end if;

  
  SET @aa=CONCAT('select tabrac.konto into @mykonto from tabrnoperative, tabrac  where tabrac.sifrakpl=@kontniplan and tabrac.sifra=tabrnoperative.racun and tabrnoperative.status=2 
    and tabrac.konto not in (select tabrac.konto from tabrnavansa, tabrac where tabrac.sifrakpl=@kontniplan and tabrac.sifra=tabrnavansa.racun and tabrnavansa.status=2) group by tabrac.konto having tabrac.konto=',parkonto);
  PREPARE stmt FROM @aa; EXECUTE stmt;
  SELECT FOUND_ROWS() INTO p;
  IF p>0 THEN
    SET @aa=CONCAT('select sum(iznpot-izndug) into @mysaldo from ',baza,'.finprom where racun=@mykonto and brdok="',parsifpar,'" and datnal<=@nadanx and stornirano=0');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    if (@mysaldo+iznos)>0 then
      set jeste = 1;
    end if;
  end if;
  
  set @jesteuavansu=jeste;
end
```

---

## 24. DeleteInvoiceRecords

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `DeleteInvoiceRecords`(IN BE VARCHAR(17),
    IN Filter_Objekat INT,    
    IN pObjekat INT,         
    IN DatumOD DATETIME,  
    IN DatumDO DATETIME,    
    IN Status INT)
BEGIN
  DELETE FROM my_invoice_exports_items_labels
  WHERE invoiceNumber IN (
    SELECT InvoiceNumber FROM my_invoice_exports
    WHERE InvoiceNumber LIKE CONCAT(BE, '%')
      AND DATE(SDCTime_ServerTimeZone) BETWEEN DatumOD AND DatumDO
      AND ((Filter_Objekat = 0) OR (objekat = pObjekat))
      AND ((Status = 0) OR (BizniSoftStatus = 0))
  );

  DELETE FROM my_invoice_exports_tax_items
  WHERE InvoiceNumber IN (
    SELECT InvoiceNumber FROM my_invoice_exports
    WHERE InvoiceNumber LIKE CONCAT(BE, '%')
      AND DATE(SDCTime_ServerTimeZone) BETWEEN DatumOD AND DatumDO
      AND ((Filter_Objekat = 0) OR (objekat = pObjekat))
      AND ((Status = 0) OR (BizniSoftStatus = 0))
  );

  DELETE FROM my_invoice_exports_items
  WHERE InvoiceNumber IN (
    SELECT InvoiceNumber FROM my_invoice_exports
    WHERE InvoiceNumber LIKE CONCAT(BE, '%')
      AND DATE(SDCTime_ServerTimeZone) BETWEEN DatumOD AND DatumDO
      AND ((Filter_Objekat = 0) OR (objekat = pObjekat))
      AND ((Status = 0) OR (BizniSoftStatus = 0))
  );

  DELETE FROM my_invoice_exports_payments
  WHERE invoiceNumber IN (
    SELECT InvoiceNumber FROM my_invoice_exports
    WHERE InvoiceNumber LIKE CONCAT(BE, '%')
      AND DATE(SDCTime_ServerTimeZone) BETWEEN DatumOD AND DatumDO
      AND ((Filter_Objekat = 0) OR (objekat = pObjekat))
      AND ((Status = 0) OR (BizniSoftStatus = 0))
  );

  DELETE FROM my_invoice_exports
  WHERE InvoiceNumber LIKE CONCAT(BE, '%')
    AND DATE(SDCTime_ServerTimeZone) BETWEEN DatumOD AND DatumDO
    AND ((Filter_Objekat = 0) OR (objekat = pObjekat))
    AND ((Status = 0) OR (BizniSoftStatus = 0));
END
```

---

## 25. dododatrsub

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `dododatrsub`(godina integer, psubjekat varchar(10))
BEGIN
  DECLARE imaproslagodina boolean;
  DECLARE imapretproslagodina boolean;
  DECLARE proslagodina varchar(100);
  DECLARE pretproslagodina varchar(100);
  SET imaproslagodina = FALSE;
  SET imapretproslagodina = FALSE;

  SELECT COUNT(*) INTO @dodatrcount;
  if @dodatrcount>0 then
          SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',@sifrafirme,(godina-1));
          if @mydbcounts>0 THEN
                SET imaproslagodina = TRUE;
                SET proslagodina = CONCAT(@bsliveid,'opp',@sifrafirme,(godina-1));
          END IF;

          SELECT COUNT(*) INTO @mydbcounts1 FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',@sifrafirme,(godina-2));
          if @mydbcounts1>0 THEN
                SET imapretproslagodina = TRUE;
                SET pretproslagodina = CONCAT(@bsliveid,'opp',@sifrafirme,(godina-2));
          END IF;

          if isnull(psubjekat) then
            DELETE FROM atributiartikli WHERE atribut in (SELECT atribut FROM dodatrsub);
          ELSE
            DELETE FROM atributiartikli WHERE atribut in (SELECT atribut FROM dodatrsub where subjekat = psubjekat);
          end if;

          DROP TEMPORARY TABLE if EXISTS tmp_atributiartikli;
          CREATE TEMPORARY TABLE tmp_atributiartikli (sifra int(6) NOT null, atribut int(4) not null, assigned int(1), operater varchar(50), vremeizmene datetime, condatddat varchar(50), zadnja int(1) DEFAULT 0, PRIMARY KEY (sifra, atribut));

          SELECT COUNT(*) INTO @dodatrulaz FROM dodatrsub WHERE tip=1;
          SELECT COUNT(*) INTO @dodatrizlaz FROM dodatrsub WHERE tip=2;
          SELECT COUNT(*) INTO @dodatrsve FROM dodatrsub WHERE tip=3;

          IF @dodatrulaz>0 then
            if isnull(psubjekat) then
              INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno WHERE subject in (select subjekat from dodatrsub) and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject;
            ELSE
              INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno WHERE subject = psubjekat and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat = psubjekat;
            end if;
          END IF;
          IF @dodatrizlaz>0 then
            if isnull(psubjekat) then
                INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno where subject in (select subjekat from dodatrsub) and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject;
            ELSE
              INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno where subject = psubjekat and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat = psubjekat;
            end if;
          END IF;
          IF @dodatrsve>0 then
            if isnull(psubjekat) then
                INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno WHERE subject in (select subjekat from dodatrsub) and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject;
            ELSE
              INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM robno WHERE subject = psubjekat and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat = psubjekat;
            end if;
          END IF;

          IF imaproslagodina THEN
                IF @dodatrulaz>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject in (select subjekat from dodatrsub) and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject = '",psubjekat,"' and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");                    
                  end if;
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
                IF @dodatrizlaz>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject in (select subjekat from dodatrsub) and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject = '",psubjekat,"' and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");
                  end if;                    
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
                IF @dodatrsve>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject in (select subjekat from dodatrsub) and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",proslagodina,".robno where subject = '",psubjekat,"' and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");
                  end if;
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
          END IF;

          IF imapretproslagodina THEN
                IF @dodatrulaz>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject in (select subjekat from dodatrsub) and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject = '",psubjekat,"' and ulaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=1 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");
                  end if;
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
                IF @dodatrizlaz>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject in (select subjekat from dodatrsub) and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject = '",psubjekat,"' and izlaz>0 and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=2 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");
                  end if;
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
                IF @dodatrsve>0 then
                  if isnull(psubjekat) then
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject in (select subjekat from dodatrsub) and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject");
                  else
                    SET @aa=CONCAT("INSERT IGNORE INTO tmp_atributiartikli SELECT robnox.sifra, dodatrsub.atribut, 1, 'BIZNISOFT', NOW(),robnox.condatddat,dodatrsub.zadnji FROM dodatrsub,(SELECT sifra,subject,MAX(condatddat) AS condatddat FROM ",pretproslagodina,".robno where subject = '",psubjekat,"' and stornirano = 0 group by subject,sifra) AS robnox WHERE dodatrsub.tip=3 and dodatrsub.subjekat=robnox.subject and dodatrsub.subjekat='",psubjekat,"'");
                  end if;
                  PREPARE stmt FROM @aa; EXECUTE stmt;
                END IF;
          END IF;
          DROP TEMPORARY TABLE if EXISTS tmp_atributiartikli1;
          create TEMPORARY TABLE tmp_atributiartikli1 like tmp_atributiartikli;
          INSERT INTO tmp_atributiartikli1 SELECT * FROM tmp_atributiartikli;
          DELETE from tmp_atributiartikli WHERE zadnja=1 AND CONCAT(sifra,'SFR',condatddat) NOT IN (SELECT CONCAT(sifra,'SFR', MAX(condatddat)) FROM tmp_atributiartikli1 GROUP BY sifra);
          INSERT INTO atributiartikli SELECT tmp_atributiartikli.sifra,tmp_atributiartikli.atribut, tmp_atributiartikli.assigned, tmp_atributiartikli.operater, tmp_atributiartikli.vremeizmene FROM tmp_atributiartikli, artikli where tmp_atributiartikli.sifra=artikli.sifra;
          DROP TEMPORARY TABLE if EXISTS tmp_atributiartikli;
          DROP TEMPORARY TABLE if EXISTS tmp_atributiartikli1;
  end if;
END
```

---

## 26. dopuni_pregled_eeppdv

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `dopuni_pregled_eeppdv`(myid varchar(100))
begin
  set @qvr=concat('insert ignore into tmp_pregled_eeppdv select "',myid,'", concat("',myid,'", " ", getizvoriname("',myid,'")), 0, 0, 0, 0');
  PREPARE stmt1 FROM @qvr; EXECUTE stmt1; DEALLOCATE PREPARE stmt1;
```

---

## 27. DoWriteLocation

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `DoWriteLocation`(`mylocation` varchar(40), `mybrnal` varchar(50), `mylistid` int)
BEGIN
  DECLARE MYRECCOUNT integer;
  select count(*) into MYRECCOUNT FROM arh_doc_locations WHERE brnal=mybrnal AND locuuid=mylocation; 
  IF MYRECCOUNT<1 THEN
    insert INTO arh_doc_locations SET brnal=mybrnal, locUUID=MYLOCATION, operater=@aktivnioperater, listid=mylistid ON DUPLICATE KEY UPDATE  locUUID=MYLOCATION, operater=@aktivnioperater, ts=now(), listid=mylistid;
    insert INTO arh_doc_locations_history SET myuuid=uuid(), brnal=mybrnal, locUUID=MYLOCATION, operater=@aktivnioperater, ts=now(), listid=mylistid;
  end if;
END
```

---

## 28. eeopdvp

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `eeopdvp`(zabrnal varchar(100))
BEGIN
  
  if trim(zabrnal)='' then
    set @zabrnalxx = '%';
    set zabrnal='XXXXXXXXXX';
  else
    set @zabrnalxx = concat(zabrnal,'/%');
  end if;

  
  update popdv_promet set sef=0,ts=ts where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);

  update popdv_promet,popdv_sifarnik,veznaefakture set popdv_promet.sef=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1
    and veznaefakture.primljena=0 and veznaefakture.brnal=popdv_promet.originalbrnal and popdv_promet.sef=0 and veznaefakture.SalesInvoiceId>0 and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);
  update popdv_promet,popdv_sifarnik,veznaefakture set popdv_promet.sef=0,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1
    and veznaefakture.primljena=0 and veznaefakture.brnal=popdv_promet.originalbrnal and popdv_promet.sef=1 and veznaefakture.SalesInvoiceId<1 and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);
  update popdv_promet,popdv_sifarnik,veznaefakture set popdv_promet.sef=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1
    and veznaefakture.primljena=0 and veznaefakture.brnal=popdv_promet.originalbrnal and popdv_promet.sef=0 and veznaefakture.status='eksterno' and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);

  
  update popdv_promet,(select originalbrnal, sum(popdv_promet.pdvos) as spdvos, sum(popdv_promet.pdvps) as spdvns from popdv_promet group by originalbrnal) as popdv_zbir set ts=ts,sef=0
    where popdv_promet.originalbrnal=popdv_zbir.originalbrnal and popdv_promet.eeopdv_def=0 and ((popdv_zbir.spdvos+popdv_zbir.spdvns)<0) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);

  
  update popdv_promet,(select originalbrnal, sum(popdv_promet.pdvos) as spdvos, sum(popdv_promet.pdvps) as spdvns from popdv_promet group by originalbrnal) as popdv_zbir set ts=ts,popdv_promet.eeopdv=1
    where popdv_promet.originalbrnal=popdv_zbir.originalbrnal and popdv_promet.eeopdv_def=0 and (round((popdv_zbir.spdvos+popdv_zbir.spdvns),2)=0) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);  

  
  update popdv_promet set eeopdv=null,ts=ts where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx);  

  
  
  
  update popdv_promet set ts=ts,eeopdv_tipprometa=1,eeopdv_pravac=0,eeopdv_inostrana=0,eeopdv_tipdok=0,eeopdv_tipprom=0, eeopdv_osnovodabira=0, eeopdv_brojpovdok=null, eeopdv_avansi='' where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0;

  
  update popdv_promet,popdv_sifarnik set popdv_promet.eeopdv=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.ulazni=1;  

  
  update popdv_promet,popdv_sifarnik set popdv_promet.eeopdv=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and (popdv_promet.brnal like 'KA%' or popdv_promet.brnal like 'PZ%') and popdv_promet.eeopdv_def=0;

  
  if @refundacijezbirna=1 then
    update popdv_promet,popdv_sifarnik set popdv_promet.eeopdv=3,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_sifarnik.izlazni=1 and (popdv_promet.brnal like 'KA%' or popdv_promet.brnal like 'PZ%') and (popdv_promet.popdvid='3.6') and popdv_promet.eeopdv_def=0;
    
    update popdv_sifarnik, popdv_promet left join faktureposracuni FORCE INDEX FOR JOIN (primary) on popdv_promet.originalbrnal=faktureposracuni.brnal set popdv_promet.eeopdv=5,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and not isnull(faktureposracuni.brnal) and popdv_promet.sef=0 and popdv_promet.popdvid<>'3.6';

    
    update popdv_sifarnik, popdv_promet left join faktureposracuni FORCE INDEX FOR JOIN (primary) on popdv_promet.originalbrnal=faktureposracuni.brnal set popdv_promet.eeopdv=3,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and not isnull(faktureposracuni.brnal) and popdv_promet.sef=0 and popdv_promet.popdvid='3.6';
  else
    
    update popdv_sifarnik, popdv_promet left join faktureposracuni FORCE INDEX FOR JOIN (primary) on popdv_promet.originalbrnal=faktureposracuni.brnal set popdv_promet.eeopdv=5,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and not isnull(faktureposracuni.brnal) and popdv_promet.sef=0;
  end if;

  
  
  update popdv_promet,popdv_sifarnik, (select brnal as sumbrnal, popdvid as sumpopdvid, sum(popdv_promet.pdvos) as sumos, sum(popdv_promet.pdvps) as sumps from popdv_promet where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_promet.popdvid like '3a.%' group by popdv_promet.brnal) as sumporeza  set popdv_promet.eeopdv=case when (left(brnal,2)='OD' or left(brnal,2)='ZD') then 6 else 2 end,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and
    (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and sumporeza.sumbrnal=popdv_promet.brnal and (not sumporeza.sumos<0) and (not sumporeza.sumps<0) and popdv_promet.popdvid like '3a.%';

  update popdv_promet,popdv_sifarnik, (select brnal as sumbrnal, sum(popdv_promet.pdvos) as sumos, sum(popdv_promet.pdvps) as sumps from popdv_promet where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_promet.popdvid like '3a.%' group by popdv_promet.brnal) as sumporeza  set popdv_promet.eeopdv=6,eeopdv_tipdok=5,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and
    (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_sifarnik.izlazni=1 and sumporeza.sumbrnal=popdv_promet.brnal and (sumporeza.sumos<0 or sumporeza.sumps<0) and popdv_promet.popdvid like '3a.%';

  
  update popdv_promet,(select originalbrnal, sum(popdv_promet.pdvos) as spdvos, sum(popdv_promet.pdvps) as spdvns from popdv_promet group by originalbrnal) as popdv_zbir left join veznaefakture on veznaefakture.brnal=popdv_zbir.originalbrnal and veznaefakture.primljena=0 ,popdv_sifarnik set popdv_promet.eeopdv=if(left(popdv_promet.brnal,2)='OK',6,2),ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (isnull(popdv_promet.eeopdv) or popdv_promet.eeopdv=1) and popdv_promet.eeopdv_def=0
     and popdv_sifarnik.izlazni=1 and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and (isnull(veznaefakture.status) or veznaefakture.status='neregistrujese' or popdv_promet.sef=0) and left(popdv_promet.brnal,2) in ('RN', 'DF', 'FA', 'FM', 'KF', 'KO', 'OK', 'PO', 'RA', 'RB', 'RM', 'PK', 'NP') and popdv_promet.popdvid<>'3.7'
       and popdv_promet.originalbrnal=popdv_zbir.originalbrnal and ((not popdv_zbir.spdvos<=0) or (not popdv_zbir.spdvns<=0));

  
  update popdv_promet,(select originalbrnal, sum(popdv_promet.pdvos) as spdvos, sum(popdv_promet.pdvps) as spdvns from popdv_promet group by originalbrnal) as popdv_zbir 
  left join veznaefakture on veznaefakture.brnal=popdv_zbir.originalbrnal and veznaefakture.primljena=0 ,popdv_sifarnik 
  set popdv_promet.eeopdv=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (isnull(popdv_promet.eeopdv) or popdv_promet.eeopdv=2) and popdv_promet.eeopdv_def=0
     and popdv_sifarnik.izlazni=1 and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and ((not (isnull(veznaefakture.status) or veznaefakture.status='neregistrujese')) and popdv_promet.sef=1)
     and left(popdv_promet.brnal,2) in ('RN', 'DF', 'FA', 'FM', 'KF', 'KO', 'OK', 'PO', 'RA', 'RB', 'RM', 'PK', 'NP') and not ((left(popdv_promet.brnal,2)='OK' or left(popdv_promet.brnal,2)='PK') and popdv_promet.ukupno <0)
       and popdv_promet.originalbrnal=popdv_zbir.originalbrnal;  

  
  

  update popdv_promet left join (select sifra, tip from kupci) as mykupci on popdv_promet.sifpar=mykupci.sifra
  ,popdv_sifarnik set popdv_promet.eeopdv= case when (mykupci.tip<>7 and popdv_promet.popdvid = '4.2.4') then 2 else 3 end,ts=ts 
  where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_sifarnik.izlazni=1 and (popdv_promet.popdvid='4.1.4' or popdv_promet.popdvid='4.2.4') and popdv_promet.eeopdv_def=0;  
  
  
  update popdv_promet left JOIN veznaefakture on veznaefakture.brnal= replace(popdv_promet.originalbrnal,'-RZ','') and veznaefakture.primljena=0,popdv_sifarnik set popdv_promet.eeopdv=6,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_promet.sef=0
  AND (isnull(veznaefakture.status) or veznaefakture.status='neregistrujese') and popdv_sifarnik.izlazni=1 and popdv_promet.eeopdv_def=0 AND left(popdv_promet.brnal,2) in ('OK', 'PK');  

  
  update popdv_promet left JOIN veznaefakture on veznaefakture.brnal= replace(popdv_promet.originalbrnal,'-RZ','') and veznaefakture.primljena=0,popdv_sifarnik set popdv_promet.eeopdv=3,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv)
  AND not (isnull(veznaefakture.status) or veznaefakture.status='neregistrujese') and popdv_sifarnik.izlazni=1 and popdv_promet.eeopdv_def=0 AND left(popdv_promet.brnal,2) in ('OK', 'PK');  

  
  update popdv_promet left JOIN veznaefakture on veznaefakture.brnal=popdv_promet.originalbrnal and veznaefakture.primljena = 0
  LEFT JOIN avracuni on popdv_promet.originalbrnal = avracuni.brnal , popdv_sifarnik  
  SET popdv_promet.eeopdv=2,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid AND popdv_sifarnik.izlazni=1 and (isnull(popdv_promet.eeopdv) or popdv_promet.eeopdv=1) and popdv_promet.eeopdv_def=0 AND not (isnull(avracuni.avrac) OR trim(avracuni.avrac)='') 
  AND (isnull(veznaefakture.status) or veznaefakture.status='neregistrujese');

  
  update popdv_promet,popdv_sifarnik set popdv_promet.eeopdv=3,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and isnull(popdv_promet.eeopdv) and popdv_promet.sef=0 and popdv_sifarnik.izlazni=1 and popdv_promet.eeopdv_def=0
  and not (popdv_promet.popdvid in ('3.1','3.2','3.5','3.7','3.9') and (popdv_promet.pdvos<0 or popdv_promet.pdvps<0));

  
  update popdv_promet,eeopdvizuzeci set popdv_promet.eeopdv=4,ts=ts where upper(left(popdv_promet.brnal,2))=upper(eeopdvizuzeci.vd) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.sifobj=eeopdvizuzeci.objekat and eeopdvizuzeci.tip=0 and popdv_promet.eeopdv_def=0;
  update popdv_promet,eeopdvizuzeci set popdv_promet.eeopdv=2,ts=ts where upper(left(popdv_promet.brnal,2))=upper(eeopdvizuzeci.vd) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.sifobj=eeopdvizuzeci.objekat and eeopdvizuzeci.tip=1 and popdv_promet.eeopdv_def=0;
  update popdv_promet,eeopdvizuzeci set popdv_promet.eeopdv=3,ts=ts where upper(left(popdv_promet.brnal,2))=upper(eeopdvizuzeci.vd) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.sifobj=eeopdvizuzeci.objekat and eeopdvizuzeci.tip=2 and popdv_promet.eeopdv_def=0;

  
  update popdv_promet
  left join veznaefakture on veznaefakture.brnal=popdv_promet.brnal and veznaefakture.primljena=0
  left join faktureposracuni FORCE INDEX FOR JOIN (primary) on popdv_promet.originalbrnal=faktureposracuni.brnal
  ,popdv_sifarnik set popdv_promet.eeopdv=1,ts=ts where popdv_promet.popdvid=popdv_sifarnik.popdvid
  and not ((left(popdv_promet.brnal,2)='OK' or left(popdv_promet.brnal,2)='PK') and popdv_promet.ukupno <0)
     and popdv_sifarnik.izlazni=1 and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and (popdv_promet.pdvos=0 and popdv_promet.pdvps=0) AND NOT (eeopdv=6) and isnull(faktureposracuni.brnal);

  
  update popdv_promet set eeopdv=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=1;
  update popdv_promet set eeopdv=3 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=2;
  update popdv_promet set eeopdv=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=3;

  
  update popdv_promet set eeopdv_pravac=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 or eeopdv=6) and upper(left(popdvid,3))='3A.';

  
  update popdv_promet,kupci set popdv_promet.eeopdv_inostrana=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.eeopdv_def=0 and (popdv_promet.eeopdv=2 or popdv_promet.eeopdv=6) and popdv_promet.sifpar=kupci.sifra and kupci.tip=4;

  
  update popdv_promet set eeopdv_tipdok=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 OR eeopdv=6 OR eeopdv=3) and (left(brnal,2)='OK' or left(brnal,2)='PK') and ukupno<0;

  
  update popdv_promet set eeopdv_tipdok=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 OR eeopdv=6) and (left(brnal,2)='OK' or left(brnal,2)='PK') and ukupno>0;

  
  update popdv_promet set eeopdv_tipdok=3 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and ((left(brnal,2)='RA') or (left(brnal,2)='AR')); 

  
  
  update popdv_promet set eeopdv_tipdok=4,eeopdv_osnovodabira=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and upper(left(popdvid,3))='3A.' and eeopdv_inostrana=1 and ukupno>0;

  
  update popdv_promet set eeopdv_tipdok=5,eeopdv_osnovodabira=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and upper(left(popdvid,3))='3A.' and eeopdv_inostrana=0 and ukupno>0;  
  
   
  update popdv_promet set eeopdv_tipdok=case when eeopdv_inostrana=1 then 4 else 5 end,eeopdv_osnovodabira=case when ukupno<0 then 4 else 3 end where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=6 and upper(left(popdvid,3))='3A.' and (left(brnal,2)='OD' or left(brnal,2)='ZD');  

  
  update popdv_promet set eeopdv_osnovodabira=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and (eeopdv_tipdok=4 or eeopdv_tipdok=5) and upper(popdvid)='3A.8';

  
  update popdv_promet set eeopdv_datplac=datnal where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and (eeopdv_tipdok = 3 or eeopdv_osnovodabira=2); 
  
  
  update popdv_promet set eeopdv_osnovodabira=3 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 or eeopdv=6) and (eeopdv_tipdok=4 or eeopdv_tipdok=5) and upper(popdvid)='3A.4';

  
  update popdv_promet set eeopdv_osnovodabira=4 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 or eeopdv=6) and (eeopdv_tipdok=4 or eeopdv_tipdok=5) and upper(popdvid)='3A.5';


  update popdv_promet set eeopdv_tipprometa=3 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and (upper(popdvid)='3A.1' or popdvid='3.1');


  update popdv_promet set eeopdv_tipprometa=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and (upper(popdvid)='3A.6');

  


  
  update popdv_promet, (select avracuni.brnal, group_concat(concat(right(godina,2),'-',avrac)) as povdok,datumpdv from avracuni group by brnal) as avracuni set eeopdv_brojpovdok=avracuni.povdok, eeopdv_tipvzdokumenta=case when avracuni.datumpdv<'2024-09-01' then 5 else 4 end 
  where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and eeopdv_tipdok=0 and eeopdv_pravac=0 and popdv_promet.originalbrnal=avracuni.brnal;

  
  update popdv_promet, (select avracunik.brnal, group_concat(avrac) as povdok, datumav from avracunik group by brnal) as avracuni set eeopdv_brojpovdok= avracuni.povdok, eeopdv_tipvzdokumenta=case when avracuni.datumav<'2024-09-01' then 5 else 4 end 
  where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=2 and (eeopdv_tipdok=5 or eeopdv_tipdok=4) and eeopdv_pravac=1 and popdv_promet.originalbrnal=avracuni.brnal;

  
   update popdv_promet set eeopdv_tipvzdokumenta=4 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and eeopdv=6 and (eeopdv_tipdok=5 or eeopdv_tipdok=4) and eeopdv_pravac=1 
   and left(popdv_promet.brnal,2)='AR' and (pdvos<0 or pdvps<0) and popdvid = '3a.5';

  
  update popdv_promet, faktspecpl set eeopdv_brojpovdok=spisakodobzad, eeopdv_tipvzdokumenta=tipodobzad, eeopdv_vezdokod=periododobzadod, eeopdv_vezdokdo=periododobzaddo 
  where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=2 or eeopdv=6 OR eeopdv=3) and (eeopdv_tipdok=1 or eeopdv_tipdok=2) and eeopdv_pravac=0 and REPLACE(popdv_promet.originalbrnal,'-RZ','')=faktspecpl.brnal;
  
  
  update popdv_promet set eeopdv_tipprom=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='1.6' or upper(popdvid)='2.6' or upper(popdvid)='3.7');

  
  update popdv_promet set eeopdv_tipprom=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='1.7' or upper(popdvid)='2.7'  or upper(popdvid)='3A.8' or upper(popdvid)='3.9');

  
  update popdv_promet set eeopdv_tipprom=3, eeopdv_avans=case when left(brnal,2)='RA' then 1 else 0 end where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='4.1.4');

  
  update popdv_promet set eeopdv_tipprom=4, eeopdv_avans=case when left(brnal,2)='RA' then 1 else 0 end where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='4.2.4');

  
  update popdv_promet set eeopdv_tipprom=5 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3.5' or upper(popdvid)='3.6') and eeopdv_dokumentstorno = 0;

  
  update popdv_promet set eeopdv_tipprom=6 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3A.4' or upper(popdvid)='3A.5') and eeopdv_dokumentstorno = 0;

  
  update popdv_promet set eeopdv_tipprom=7 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3.5' or upper(popdvid)='3.6') and eeopdv_dokumentstorno = 1;

  
  update popdv_promet set eeopdv_tipprom=8 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3A.4' or upper(popdvid)='3A.5' or (upper(popdvid)='3A.3' and ukupno<0)) and eeopdv_dokumentstorno = 1;

  
  update popdv_promet set eeopdv_tipkorekcije=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3A.4' or upper(popdvid)='3.5');
  
  
  update popdv_promet set eeopdv_tipkorekcije=2, eeopdv_avans=case when eeopdv_tipvzdokumenta=4 then 1 else 0 end where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3 or eeopdv=6) and (upper(popdvid)='3A.5' or upper(popdvid)='3.6');
  update popdv_promet set eeopdv_tipkorekcije=2, eeopdv_avans=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and eeopdv_def=0 and (eeopdv=3) and (upper(popdvid)='3.6') and left(brnal,2)='RA';
  
  update popdv_promet,(select brnal,eeopdv_tipprom from popdv_promet as frt where frt.eeopdv=3 and frt.eeopdv_tipprom<>2 group by frt.brnal) as xxr1 set popdv_promet.eeopdv_tipprom=xxr1.eeopdv_tipprom where popdv_promet.brnal=xxr1.brnal and not isnull(xxr1.brnal) and (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.eeopdv_def=0 and popdv_promet.eeopdv=3 and popdv_promet.eeopdv_tipprom=2;
END
```

---

## 29. eeopdvspec

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `eeopdvspec`(zagodinu int(4), zaperiod int(2), klijent int(4), periodod varchar(10), perioddo varchar(10))
BEGIN
  declare proslagodina varchar(100);  
 
  drop temporary table if exists veznaproslagodina;
  create temporary table veznaproslagodina(brnal varchar(50),status varchar(50), razbrnal varchar(100));

  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',klijent,(zagodinu-1));
  if @mydbcounts>0 THEN    
    SET proslagodina = CONCAT(@bsliveid,'opp',klijent,(zagodinu-1));

    set @aa=concat(' insert into veznaproslagodina select ',proslagodina,'.veznaefakture.brnal, ',proslagodina,'.veznaefakture.status as status, mypopdv.brnal 
    from ',proslagodina,'.veznaefakture, (select * from popdv_promet where datpdv>="',periodod,'" and datpdv<="',perioddo,'" and right(brnal,3)=''-RZ'') as mypopdv 
    where ',proslagodina,'.veznaefakture.brnal = mypopdv.originalbrnal and ',proslagodina,'.veznaefakture.datum > "',concat(zagodinu-1,'-12-31'),'" and primljena = 0 
    having status in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")');    
    prepare stmt from @aa; execute stmt;
    DEALLOCATE PREPARE stmt;
  end if;

  drop temporary table if exists tmp_eeopdvspec;
  create temporary table tmp_eeopdvspec (regf double(15,2) default 0,rego double(15,2) default 0,regz double(15,2) default 0,rega double(15,2) default 0,regkasa double(15,2) default 0,regpazari double(15,2) default 0,regzbirna double(15,2) default 0,regpojedinacna double(15,2) default 0,ukupno double(15,2) default 0,sefzbirna double(15,2) default 0,sefpojedinacna double(15,2) default 0);
  insert into tmp_eeopdvspec set regf=0;

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status, veznapg.status as status1 
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
        left join veznaproslagodina as veznapg on popdv_promet.brnal=veznapg.razbrnal 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2) in ("RN", "DF", "FA", "FM", "KF", "KO", "PO", "RB", "RM", "NP") and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and (popdv_promet.sef=1 or (popdv_promet.sef=0 and veznaefaktureizlaz.status="dokumentstorno") or (popdv_promet.sef=0 and not isnull(veznapg.brnal))) and popdv_promet.eeopdv<>2 and popdv_promet.eeopdv<>3
          group by popdv_promet.brnal,rbrst having status in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")
          or status1 in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set regf=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status, veznapg.status as status1
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0         
        left join veznaproslagodina as veznapg on popdv_promet.brnal=veznapg.razbrnal 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2) in ("OK", "PK") and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and (popdv_promet.sef=1 or (popdv_promet.sef=0 and veznaefaktureizlaz.status="dokumentstorno") or (popdv_promet.sef=0 and not isnull(veznapg.brnal))) and popdv_promet.eeopdv<>2 and popdv_promet.eeopdv<>3 and (popdv_promet.pdvos+popdv_promet.pdvps)<0
          group by popdv_promet.brnal,rbrst having status in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")
          or status1 in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set rego=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2) in ("OK", "PK") and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and (popdv_promet.sef=1 or (popdv_promet.sef=0 and veznaefaktureizlaz.status="dokumentstorno")) and popdv_promet.eeopdv<>2 and popdv_promet.eeopdv<>3 and (popdv_promet.pdvos+popdv_promet.pdvps)>0
          group by popdv_promet.brnal,rbrst having status in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set regz=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2)="RA" and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and (popdv_promet.sef=1 or (popdv_promet.sef=0 and veznaefaktureizlaz.status="dokumentstorno")) and popdv_promet.eeopdv<>2 and popdv_promet.eeopdv<>3
          group by popdv_promet.brnal,rbrst having status in ("poslato","prihvaceno","arhivirano","arhivirano","odbijeno","otkazano","storno","placeno","istekla","dokumentstorno","eskterno","vidjeno","podsecen","primljenio","ponovoobavesten","eksterno")) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set rega=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2)="KA" and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and not (popdv_promet.eeopdv=3 or popdv_promet.eeopdv=2)
          group by popdv_promet.brnal,rbrst) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set regkasa=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and popdv_promet.eeopdv=5 and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0
          group by popdv_promet.brnal,rbrst) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set regkasa=regkasa+if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  SET @aa=CONCAT('select sum(hh.pdvos+hh.pdvps) into @yy1 from (select popdv_promet.*, if((isnull(veznaefaktureizlaz.status) or trim(veznaefaktureizlaz.status)=""),sef_sales.status, veznaefaktureizlaz.status) as status
      from popdv_sifarnik,popdv_promet left join ',@bsliveid,'biznisoftbinaries.sef_sales on sef_sales.klijent=',klijent,' and sef_sales.godina=',zagodinu,' and popdv_promet.originalbrnal=sef_sales.biznisoftbrnal 
        left join veznaefakture as veznaefaktureizlaz on veznaefaktureizlaz.brnal=popdv_promet.originalbrnal and veznaefaktureizlaz.primljena=0 
          where popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.izlazni=1 and popdv_promet.datpdv>="',periodod,'" and popdv_promet.datpdv<="',perioddo,'"  
            and left(popdv_promet.brnal,2)="PZ" and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0 and not (popdv_promet.eeopdv=3 or popdv_promet.eeopdv=2) 
          group by popdv_promet.brnal,rbrst) as hh');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  update tmp_eeopdvspec set regpazari=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  select sum(pnos_pdv+pnns_pdv+pbos_pdv+pbns_pdv+pavansos_pdv+pavansns_pdv) into @yy1 from my_eeopdv_zbirna where godina=zagodinu and period=zaperiod;
  update tmp_eeopdvspec set regzbirna=if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  select sum(uvecanje-smanjenje) into @yy1 from my_eeopdv where godina=zagodinu and period=zaperiod and tipevidencije=0;
  update tmp_eeopdvspec set regzbirna=regzbirna+if(isnull(@yy1),0,@yy1);

  
  set @yy1=0;
  select sum(pdv) into @yy1 from my_eeopdv_pojedinacna where godina=zagodinu and period=zaperiod;
  update tmp_eeopdvspec set regpojedinacna=if(isnull(@yy1),0,@yy1);

  
  update tmp_eeopdvspec set ukupno=regf+rego+regz+rega+regkasa+regpazari+regzbirna+regpojedinacna;

  
  update tmp_eeopdvspec, my_eeopdv_sef set tmp_eeopdvspec.sefzbirna=my_eeopdv_sef.sefzbirna, tmp_eeopdvspec.sefpojedinacna=my_eeopdv_sef.sefpojedinacna where my_eeopdv_sef.godina=zagodinu and my_eeopdv_sef.period=zaperiod;
  drop temporary table if exists veznaproslagodina;
end
```

---

## 30. eeppdvp

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `eeppdvp`(zabrnal varchar(100))
BEGIN
  

  
  if trim(zabrnal)='' then
    set @zabrnalxx = '%';
    set zabrnal='XXXXXXXXXX';
  else
    set @zabrnalxx = concat(zabrnal,'/%');
  end if;
  
  
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=1 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '8a.%' and popdv_promet.popdvid<>'8a.2.y');
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=2 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '8b.%' or popdv_promet.popdvid like '8g.%');
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=3 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '6.4');
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=4 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '7.3' and (popdv_promet.pdvos + popdv_promet.pdvps)>0);
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=51 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '8a.2.y');
  update popdv_promet, popdv_sifarnik set eeppdv_tipprometa=52 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_tipprometa=0 and (popdv_promet.popdvid like '7.3' and (popdv_promet.pdvos + popdv_promet.pdvps)<0);
  
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=11 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.1');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=12 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and ((popdv_promet.popdvid like '8a.2%' and popdv_promet.popdvid<>'8a.2.y') or (popdv_promet.popdvid like '8a.3%'));
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=13 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.4');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=14 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.5%');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=15 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.7' and (popdv_promet.pdvos + popdv_promet.pdvps)>0);
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=16 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.7' and (popdv_promet.pdvos + popdv_promet.pdvps)<0);
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=21 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8b.1');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=22 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid='8b.2' or popdv_promet.popdvid='8b.3' or popdv_promet.popdvid='8g.1' or popdv_promet.popdvid='8g.2');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=23 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid='8b.4' or popdv_promet.popdvid='8g.3');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=24 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8b.5%' or popdv_promet.popdvid='8g.4');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=25 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and ((popdv_promet.popdvid like '8b.7' and (popdv_promet.pdvos + popdv_promet.pdvps)>0) or (popdv_promet.popdvid like '8g.6' and (popdv_promet.pdvos + popdv_promet.pdvps)>0));
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=26 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and ((popdv_promet.popdvid like '8b.7' and (popdv_promet.pdvos + popdv_promet.pdvps)<0) or (popdv_promet.popdvid like '8g.6' and (popdv_promet.pdvos + popdv_promet.pdvps)<0));
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=31 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '6.4');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=41 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '7.3' and (popdv_promet.pdvos + popdv_promet.pdvps)>0);
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=512 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '8a.2.y');
  update popdv_promet, popdv_sifarnik set eeppdv_vrstaprometa=527 where (popdv_promet.brnal=zabrnal or popdv_promet.brnal like @zabrnalxx) and popdv_promet.popdvid=popdv_sifarnik.popdvid and popdv_sifarnik.ulazni=1 and eeppdv_vrstaprometa=0 and (popdv_promet.popdvid like '7.3' and (popdv_promet.pdvos + popdv_promet.pdvps)<0);
END
```

---

## 31. eo_fix_auto_increment

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `eo_fix_auto_increment`(IN doc_type VARCHAR(20))
BEGIN
  DECLARE max_id BIGINT;
  DECLARE current_auto BIGINT;
  DECLARE new_auto BIGINT;

  SET max_id = eo_get_max_document_id(doc_type);

  IF doc_type = 'otpremnica' THEN
    SELECT AUTO_INCREMENT INTO current_auto
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'eo_otpremnice';

    IF max_id >= current_auto THEN
      SET new_auto = max_id + 1;
      SET @sql = CONCAT('ALTER TABLE eo_otpremnice AUTO_INCREMENT = ', new_auto);
      PREPARE stmt FROM @sql;
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
    END IF;

  ELSEIF doc_type = 'prijemnica' THEN
    SELECT AUTO_INCREMENT INTO current_auto
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'eo_prijemnice';

    IF max_id >= current_auto THEN
      SET new_auto = max_id + 1;
      SET @sql = CONCAT('ALTER TABLE eo_prijemnice AUTO_INCREMENT = ', new_auto);
      PREPARE stmt FROM @sql;
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
    END IF;
  END IF;
END
```

---

## 32. fifoPricePST

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `fifoPricePST`(`so` int,`sa` int, `dt` date, vrstacene varchar(3))
BEGIN
  DECLARE i INTEGER;
  DECLARE trStock, krStock, krvred, krvred1, cbp, csp DOUBLE;
  DECLARE cvrednost DOUBLE;
  SELECT round(SUM(if(ulaz<0, abs(ulaz),izlaz)),4) as outStock INTO @outStock FROM robno WHERE (izlaz <> 0 or ulaz < 0) AND sifobj = so AND sifra = sa AND datum <= dt and stornirano=0 and not (robno.brnal like 'POTVRDJENO%');
  SELECT round(SUM(ulaz-izlaz),4) as trStock INTO trStock FROM robno WHERE sifobj = so AND sifra = sa AND datum <= dt and stornirano=0 and not (robno.brnal like 'POTVRDJENO%');

  if upper(vrstacene)='NBC' then
      select sum(if((ulaz=0 and izlaz=0) or @nabcenadp,duguje-potrazuje,(ulaz*nabcena)-(izlaz*nabcena))) INTO cvrednost from robno where sifobj= so and datum<=dt and sifra=sa and stornirano=0 and not (robno.brnal like 'POTVRDJENO%');
  ELSE
      select sum((ulaz*nabcena)-(izlaz*nabcena)) INTO cvrednost from robno where sifobj=so and datum<=dt and sifra=sa and stornirano=0 and not (robno.brnal like 'POTVRDJENO%');   
  END IF;
```

---

## 33. fifoPricePSTAll

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `fifoPricePSTAll`(`so` int, `dt` date, vrstacene varchar(3))
BEGIN
  DECLARE s_artikal integer;
  DECLARE exit_loop boolean;
  DECLARE artikli CURSOR FOR SELECT robno.sifra FROM robno,artikli where robno.sifra=artikli.sifra and robno.sifobj=so and artikli.jeusluga=0 GROUP by robno.sifra;
  declare continue handler for not found set exit_loop = true;

  drop temporary table if exists memall;
  create temporary table memall (sifobj int(3) not null, sifra int(6) not null, mestotr int(6), nosioc int(6), nabcena double(15,4), faktcena double(15,2), refdate date, refddatum timestamp, ulaz double(21,4), stock double(15,4), cenabezpp double(15,2), cenasapp double(15,2), brnalpst varchar(100));
  set @greskafifo='';
  OPEN artikli;
  set exit_loop = false;
  artikli_loop: 
    LOOP FETCH artikli INTO s_artikal;
    IF exit_loop THEN
      LEAVE artikli_loop;
    END IF;
    call fifoPricePST(so, s_artikal, dt, vrstacene);
    insert into memall select * from mem;
  end loop artikli_loop;
  close artikli;
end
```

---

## 34. fifo_calc

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `fifo_calc`(IN so INT, 
    IN sa INT, 
    IN dt DATE, 
    IN qt DOUBLE,
    OUT result_price DOUBLE)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE rec_datum DATE;
    DECLARE rec_ddatum TIMESTAMP;
    DECLARE rec_brnal VARCHAR(50);
    DECLARE rec_ulaz DOUBLE;
    DECLARE rec_izlaz DOUBLE;
    DECLARE rec_nabcena DOUBLE;
    
    DECLARE last_nabcena DOUBLE DEFAULT 0;
    DECLARE requested_qty DOUBLE;
    
    DECLARE remaining_qty DOUBLE;
    DECLARE total_value DOUBLE DEFAULT 0;
    DECLARE qty_taken DOUBLE DEFAULT 0;
    DECLARE has_layer INT;
    
    DECLARE fifo_cursor CURSOR FOR
        SELECT datum, ddatum, brnal, ulaz, izlaz, if(prernc>0,prernc,nabcena) as nabcena
        FROM robno
        WHERE sifobj = so 
          AND sifra = sa 
          AND datum <= dt
          AND IFNULL(stornirano, 0) = 0
          AND brnal NOT LIKE 'POTVRDJENO%'
        ORDER BY datum ASC, (ULAZ>0) DESC, ddatum ASC, brnal ASC;
    
    DECLARE layer_cursor CURSOR FOR
        SELECT price, quantity
        FROM temp_fifo_calc
        WHERE quantity > 0
        ORDER BY row_id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    IF qt <= 0 THEN
        SET requested_qty = 1;
    ELSE
        SET requested_qty = qt;
    END IF;
    
    DROP TEMPORARY TABLE IF EXISTS temp_fifo_calc;
    
    CREATE TEMPORARY TABLE temp_fifo_calc (
        row_id INT AUTO_INCREMENT PRIMARY KEY,
        price DOUBLE,
        quantity DOUBLE
    ) ENGINE=MEMORY;
    
    OPEN fifo_cursor;
    
    build_layers: LOOP
        FETCH fifo_cursor INTO rec_datum, rec_ddatum, rec_brnal, rec_ulaz, rec_izlaz, rec_nabcena;
        
        IF done THEN
            LEAVE build_layers;
        END IF;

        IF rec_nabcena IS NOT NULL THEN
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_ulaz IS NOT NULL AND rec_ulaz > 0 THEN
            INSERT INTO temp_fifo_calc (price, quantity) VALUES (rec_nabcena, rec_ulaz);
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_izlaz IS NOT NULL AND rec_izlaz > 0 THEN
            SET remaining_qty = rec_izlaz;
            
            
            WHILE remaining_qty > 0.0001 DO
                
                SELECT COUNT(*) INTO has_layer
                FROM temp_fifo_calc
                WHERE quantity > 0;
                
                IF has_layer = 0 THEN
                    
                    INSERT INTO temp_fifo_calc (price, quantity) VALUES (last_nabcena, -remaining_qty);
                    SET remaining_qty = 0;
                ELSE
                    
                    SET @layer_id = (SELECT row_id FROM temp_fifo_calc WHERE quantity > 0 ORDER BY row_id LIMIT 1);
                    SET @layer_qty = (SELECT quantity FROM temp_fifo_calc WHERE row_id = @layer_id);
                    
                    IF @layer_qty <= remaining_qty THEN
                        
                        DELETE FROM temp_fifo_calc WHERE row_id = @layer_id;
                        SET remaining_qty = remaining_qty - @layer_qty;
                    ELSE
                        
                        UPDATE temp_fifo_calc 
                        SET quantity = quantity - remaining_qty 
                        WHERE row_id = @layer_id;
                        SET remaining_qty = 0;
                    END IF;
                END IF;
            END WHILE;
        END IF;
        
        
        IF rec_izlaz IS NOT NULL AND rec_izlaz < 0 THEN
            INSERT INTO temp_fifo_calc (price, quantity) VALUES (rec_nabcena, -rec_izlaz);
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_ulaz IS NOT NULL AND rec_ulaz < 0 THEN
            SET remaining_qty = -rec_ulaz;
            
            WHILE remaining_qty > 0.0001 DO
                SELECT COUNT(*) INTO has_layer
                FROM temp_fifo_calc
                WHERE quantity > 0;
                
                IF has_layer = 0 THEN
                    SET remaining_qty = 0;
                ELSE
                    SET @layer_id = (SELECT row_id FROM temp_fifo_calc WHERE quantity > 0 ORDER BY row_id LIMIT 1);
                    SET @layer_qty = (SELECT quantity FROM temp_fifo_calc WHERE row_id = @layer_id);
                    
                    IF @layer_qty <= remaining_qty THEN
                        DELETE FROM temp_fifo_calc WHERE row_id = @layer_id;
                        SET remaining_qty = remaining_qty - @layer_qty;
                    ELSE
                        UPDATE temp_fifo_calc 
                        SET quantity = quantity - remaining_qty 
                        WHERE row_id = @layer_id;
                        SET remaining_qty = 0;
                    END IF;
                END IF;
            END WHILE;
        END IF;
    END LOOP;
    
    CLOSE fifo_cursor;
    
    
    SET remaining_qty = requested_qty;
    SET done = 0;
    
    OPEN layer_cursor;
    
    calc_price: LOOP
        FETCH layer_cursor INTO rec_nabcena, rec_ulaz;
        
        IF done OR remaining_qty <= 0 THEN
            LEAVE calc_price;
        END IF;
        
        IF rec_ulaz >= remaining_qty THEN
            SET total_value = total_value + (remaining_qty * rec_nabcena);
            SET qty_taken = qty_taken + remaining_qty;
            SET remaining_qty = 0;
        ELSE
            SET total_value = total_value + (rec_ulaz * rec_nabcena);
            SET qty_taken = qty_taken + rec_ulaz;
            SET remaining_qty = remaining_qty - rec_ulaz;
        END IF;
    END LOOP;
    
    CLOSE layer_cursor;
    
    
    IF remaining_qty > 0 THEN
        SET total_value = total_value + (remaining_qty * last_nabcena);
        SET qty_taken = qty_taken + remaining_qty;
    END IF;
    
    DROP TEMPORARY TABLE IF EXISTS temp_fifo_calc;
    
    IF qty_taken > 0 THEN
        SET result_price = total_value / qty_taken;
    ELSE
        SET result_price = 0;
    END IF;
END
```

---

## 35. fifo_calc_prerNC

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `fifo_calc_prerNC`(IN so INT, 
    IN sa INT, 
    IN dt DATE, 
    IN qt DOUBLE,
    IN s_condatddat varchar(50),
    OUT result_price DOUBLE)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE rec_datum DATE;
    DECLARE rec_ddatum TIMESTAMP;
    DECLARE rec_brnal VARCHAR(50);
    DECLARE rec_ulaz DOUBLE;
    DECLARE rec_izlaz DOUBLE;
    DECLARE rec_nabcena DOUBLE;
    
    DECLARE last_nabcena DOUBLE DEFAULT 0;
    DECLARE requested_qty DOUBLE;
    
    DECLARE remaining_qty DOUBLE;
    DECLARE total_value DOUBLE DEFAULT 0;
    DECLARE qty_taken DOUBLE DEFAULT 0;
    DECLARE has_layer INT;
    
    DECLARE fifo_cursor CURSOR FOR
        SELECT datum, ddatum, brnal, ulaz, izlaz, nabcena
        FROM my_prernc_robno
        WHERE sifobj = so 
          AND sifra = sa 
          AND datum <= dt
          AND brnal NOT LIKE 'POTVRDJENO%'
   
        ORDER BY datum ASC, (ULAZ>0) DESC, ddatum ASC, brnal ASC;
    
    DECLARE layer_cursor CURSOR FOR
        SELECT price, quantity
        FROM temp_fifo_calc
        WHERE quantity > 0
        ORDER BY row_id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    IF qt <= 0 THEN
        SET requested_qty = 1;
    ELSE
        SET requested_qty = qt;
    END IF;
    
    DROP TEMPORARY TABLE IF EXISTS temp_fifo_calc;
    
    CREATE TEMPORARY TABLE temp_fifo_calc (
        row_id INT AUTO_INCREMENT PRIMARY KEY,
        price DOUBLE,
        quantity DOUBLE
    ) ENGINE=MEMORY;
    
    OPEN fifo_cursor;
    
    build_layers: LOOP
        FETCH fifo_cursor INTO rec_datum, rec_ddatum, rec_brnal, rec_ulaz, rec_izlaz, rec_nabcena;
        
        IF done THEN
            LEAVE build_layers;
        END IF;

        IF rec_nabcena IS NOT NULL THEN
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_ulaz IS NOT NULL AND rec_ulaz > 0 THEN
            INSERT INTO temp_fifo_calc (price, quantity) VALUES (rec_nabcena, rec_ulaz);
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_izlaz IS NOT NULL AND rec_izlaz > 0 THEN
            SET remaining_qty = rec_izlaz;
            
            
            WHILE remaining_qty > 0.0001 DO
                
                SELECT COUNT(*) INTO has_layer
                FROM temp_fifo_calc
                WHERE quantity > 0;
                
                IF has_layer = 0 THEN
                    
                    INSERT INTO temp_fifo_calc (price, quantity) VALUES (last_nabcena, -remaining_qty);
                    SET remaining_qty = 0;
                ELSE
                    
                    SET @layer_id = (SELECT row_id FROM temp_fifo_calc WHERE quantity > 0 ORDER BY row_id LIMIT 1);
                    SET @layer_qty = (SELECT quantity FROM temp_fifo_calc WHERE row_id = @layer_id);
                    
                    IF @layer_qty <= remaining_qty THEN
                        
                        DELETE FROM temp_fifo_calc WHERE row_id = @layer_id;
                        SET remaining_qty = remaining_qty - @layer_qty;
                    ELSE
                        
                        UPDATE temp_fifo_calc 
                        SET quantity = quantity - remaining_qty 
                        WHERE row_id = @layer_id;
                        SET remaining_qty = 0;
                    END IF;
                END IF;
            END WHILE;
        END IF;
        
        
        IF rec_izlaz IS NOT NULL AND rec_izlaz < 0 THEN
            INSERT INTO temp_fifo_calc (price, quantity) VALUES (rec_nabcena, -rec_izlaz);
            SET last_nabcena = rec_nabcena;
        END IF;
        
        
        IF rec_ulaz IS NOT NULL AND rec_ulaz < 0 THEN
            SET remaining_qty = -rec_ulaz;
            
            WHILE remaining_qty > 0.0001 DO
                SELECT COUNT(*) INTO has_layer
                FROM temp_fifo_calc
                WHERE quantity > 0;
                
                IF has_layer = 0 THEN
                    SET remaining_qty = 0;
                ELSE
                    SET @layer_id = (SELECT row_id FROM temp_fifo_calc WHERE quantity > 0 ORDER BY row_id LIMIT 1);
                    SET @layer_qty = (SELECT quantity FROM temp_fifo_calc WHERE row_id = @layer_id);
                    
                    IF @layer_qty <= remaining_qty THEN
                        DELETE FROM temp_fifo_calc WHERE row_id = @layer_id;
                        SET remaining_qty = remaining_qty - @layer_qty;
                    ELSE
                        UPDATE temp_fifo_calc 
                        SET quantity = quantity - remaining_qty 
                        WHERE row_id = @layer_id;
                        SET remaining_qty = 0;
                    END IF;
                END IF;
            END WHILE;
        END IF;
    END LOOP;
    
    CLOSE fifo_cursor;
    
    
    SET remaining_qty = requested_qty;
    SET done = 0;
    
    OPEN layer_cursor;
    
    calc_price: LOOP
        FETCH layer_cursor INTO rec_nabcena, rec_ulaz;
        
        IF done OR remaining_qty <= 0 THEN
            LEAVE calc_price;
        END IF;
        
        IF rec_ulaz >= remaining_qty THEN
            SET total_value = total_value + (remaining_qty * rec_nabcena);
            SET qty_taken = qty_taken + remaining_qty;
            SET remaining_qty = 0;
        ELSE
            SET total_value = total_value + (rec_ulaz * rec_nabcena);
            SET qty_taken = qty_taken + rec_ulaz;
            SET remaining_qty = remaining_qty - rec_ulaz;
        END IF;
    END LOOP;
    
    CLOSE layer_cursor;
    
    
    IF remaining_qty > 0 THEN
        SET total_value = total_value + (remaining_qty * last_nabcena);
        SET qty_taken = qty_taken + remaining_qty;
    END IF;
    
    DROP TEMPORARY TABLE IF EXISTS temp_fifo_calc;
    
    IF qty_taken > 0 THEN
        SET result_price = total_value / qty_taken;
    ELSE
        SET result_price = 0;
    END IF;
END
```

---

## 36. formirajEEOPDVP

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `formirajEEOPDVP`(zagodinu int(4), tromesecni int(1))
BEGIN
  
  
  drop temporary table if exists cobi;
  drop temporary table if exists cobi1;
  drop temporary table if exists cobi2;
  create temporary table cobi as select brnal,originalbrnal, eeopdv, eeopdv_dokumentstorno from popdv_promet where eeopdv_dokumentstorno=1 and brnal<>originalbrnal and popdvid = '3.6' and stornirano = 0 and eeopdv_tipdok=0 group by originalbrnal;
  create temporary table cobi1 as select brnal from popdv_promet where originalbrnal in (select originalbrnal from cobi);
  create temporary table cobi2 as select cobi1.*, oznakadokumenta.oznaka from cobi1 left join oznakadokumenta on cobi1.brnal=oznakadokumenta.brnal;
  update popdv_promet, cobi2 set popdv_promet.eeopdv=2 where popdv_promet.brnal=cobi2.brnal and cobi2.oznaka = 11;
  drop temporary table if exists cobi;
  drop temporary table if exists cobi1;
  drop temporary table if exists cobi2;

  drop temporary table if exists tmp_zaglavljep;
  create temporary table tmp_zaglavljep like my_eeopdv;
  drop temporary table if exists tmp_inipojedinacna;
  create temporary table tmp_inipojedinacna like my_eeopdv_pojedinacna;
  drop temporary table if exists tmp_ez_popdv_promet;
  create temporary table tmp_ez_popdv_promet (brnal varchar(50) not null, datpdv date not null, osnovicaos double(15,2) default 0, pdvos double(15,2) default 0, osnovicaps double(15,2) default 0, pdvps double(15,2) default 0, eeopdv int(2), potvrdjeno int(1),
  stornirano int(1), eeopdv_tipprom int(1) not null,eeopdv_avans int(1) default 0, eeopdv_dokumentstorno int(1) default 0, operater varchar(100), vremeizmene datetime, primary key(brnal,eeopdv_tipprom));
  drop temporary table if exists tmp_zbirnapp;
  create temporary table tmp_zbirnapp like eeopdv_zbirna;
  if tromesecni=1 then
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=21, mesec=3, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=21, mesec=3, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=22, mesec=6, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=22, mesec=6, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=23, mesec=9, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=23, mesec=9, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=24, mesec=12, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=24, mesec=12, tipevidencije=1, status=1;

    delete from tmp_inipojedinacna where concat(godina,period) in (select concat(godina,period) from tmp_zaglavljep where tipevidencije=1 and status<2);

    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(osnovicaos=0 and pdvos<>0, pdvos/(getpdv('S1',datpdv)/100) ,osnovicaos)), sum(pdvos), sum(if(osnovicaps=0 and pdvps<>0, pdvps/(getpdv('S2',datpdv)/100) ,osnovicaps)), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep  
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(pdvos>0,pdvos/(getpdv('S1',datpdv)/100),0)), sum(pdvos), 0, 0, eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep 
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep 
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD' or left(brnal,2)='KA') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 1, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.7' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 0, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.2' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 2, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.9' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 5, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.6' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    update tmp_ez_popdv_promet set osnovicaos= pdvos/(getpdv('S1',datpdv)/100), osnovicaps= pdvps/(getpdv('S2',datpdv)/100) where (left(brnal,2)='OK' or left(brnal,2)='AR') and (pdvos<0 or pdvps<0) and eeopdv_avans = 1 and (osnovicaos=0 and osnovicaps=0);
  
    
    insert into tmp_zbirnapp select godina, period, brnal,1, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=0;
    
    
    insert into tmp_zbirnapp select godina, period, brnal,2, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0    
      from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=1;

    
    insert into tmp_zbirnapp select godina, period, brnal,3, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0          
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=2;          

    
    insert into tmp_zbirnapp select godina, period, brnal,if(eeopdv_avans=0,4,5), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0                
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<0) or (not pdvps<0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=3;

    
    insert into tmp_zbirnapp select godina, period, brnal,if(eeopdv_avans=0,6,7), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0                      
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period>20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=4;    

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),8, if(eeopdv_avans=0,9,10)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=5 and eeopdv_dokumentstorno=0;

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),11, if(eeopdv_avans=0,12,13)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0             
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=6 and eeopdv_dokumentstorno=0;

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),14, if(eeopdv_avans=0,15,16)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0      
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=7 and eeopdv_dokumentstorno=1;        

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),17, if(eeopdv_avans=0,18,19)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0            
        from tmp_ez_popdv_promet,tmp_zaglavljep where quarter(tmp_ez_popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=8 and eeopdv_dokumentstorno=1;          

    
    insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), sum(osnovicaos+osnovicaps), datpdv, sum(osnovicaos) as oos , sum(osnovicaps), sum(pdvos+pdvps) as spdv, sum(ukupno), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
          eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
         from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
         where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and status=1 and potvrdjeno=1 and stornirano=0 and not (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;
  
  
  insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
  eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), ABS(sum(pdvos+pdvps)) as pdvuk, datpdv, ABS(sum(osnovicaos)) as oos , ABS(sum(osnovicaps)),
  sum(ABS(osnovicaos)*(getpdv('S1',datpdv)/100) + ABS(osnovicaps)*(getpdv('S2',datpdv)/100)) as spdv, sum(ABS(osnovicaos)*(1+(getpdv('S1',datpdv)/100))+abs(osnovicaps)*(1+(getpdv('S2',datpdv)/100))), 0, 0, 0, null,
  eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(osnovicaos)*(getpdv('S1',datpdv)/100)), sum(ABS(osnovicaps)*(getpdv('S2',datpdv)/100)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
        where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=6 and status=1 and potvrdjeno=1 and stornirano=0 group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0 and pdvuk=0;

  
  insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
  eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)), datpdv,
  ABS(sum(pdvos/(getpdv('S1',datpdv)/100))) as oos , ABS(sum(pdvps/(getpdv('S2',datpdv)/100))),sum(ABS(pdvos) + ABS(pdvps)) as spdv,ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)),
   0, 0, 0, null, eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(pdvos)), sum(ABS(pdvps)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
      from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra      
      where quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=6 and status=1 and potvrdjeno=1 and stornirano=0
      group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;
            
  
  insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
  if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), sum(if(ukupno>0,ukupno,0)), datpdv, sum(if(osnovicaos>0,osnovicaos,0)), sum(if(osnovicaps>0,osnovicaps,0)),
  sum(pdvos+pdvps), sum(if(ukupno>0,ukupno,0)), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from tmp_zaglavljep, popdv_promet 
        left join kupci on popdv_promet.sifpar=kupci.sifra            
        WHERE quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0                    
        AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and NOT (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g') group by popdv_promet.originalbrnal;    

  
  insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
  if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), zukupno, datpdv, zosnovicaos, zosnovicaps,
  (zpdvos+zpdvps), zukupno, 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, zpdvos, zpdvps, eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
  eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
        from tmp_zaglavljep, popdv_promet 
        left join kupci on popdv_promet.sifpar=kupci.sifra 
        left join (select originalbrnal, sum(if(ukupno>0,ukupno,0)) AS zukupno, sum(if(osnovicaos>0,osnovicaos,0)) AS zosnovicaos, sum(if(osnovicaps>0,osnovicaps,0)) AS zosnovicaps, sum(pdvos) as zpdvos, sum(pdvps) as zpdvps 
        from popdv_promet where stornirano = 0 and (left(popdvid,2) = '8b' or left(popdvid,2) = '8g') group by originalbrnal) as popdv_zbir on popdv_zbir.originalbrnal = popdv_promet.originalbrnal
        WHERE quarter(popdv_promet.datpdv)=quarter(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period>20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0         
        AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g')
        group by popdv_promet.originalbrnal;  
  else
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=1, mesec=1, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=1, mesec=1, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=2, mesec=2, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=2, mesec=2, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=3, mesec=3, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=3, mesec=3, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=4, mesec=4, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=4, mesec=4, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=5, mesec=5, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=5, mesec=5, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=6, mesec=6, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=6, mesec=6, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=7, mesec=7, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=7, mesec=7, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=8, mesec=8, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=8, mesec=8, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=9, mesec=9, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=9, mesec=9, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=10, mesec=10, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=10, mesec=10, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=11, mesec=11, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=11, mesec=11, tipevidencije=1, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=12, mesec=12, tipevidencije=0, status=1;
    insert ignore into tmp_zaglavljep set godina=zagodinu, period=12, mesec=12, tipevidencije=1, status=1;

    delete from tmp_inipojedinacna where concat(godina,period) in (select concat(godina,period) from tmp_zaglavljep where tipevidencije=1 and status<2);

    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(osnovicaos=0 and pdvos<>0, pdvos/(getpdv('S1',datpdv)/100) ,osnovicaos)), sum(pdvos), sum(if(osnovicaps=0 and pdvps<>0, pdvps/(getpdv('S2',datpdv)/100) ,osnovicaps)), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(if(pdvos>0,pdvos/(getpdv('S1',datpdv)/100),0)), sum(pdvos), 0, 0, eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), eeopdv, potvrdjeno, stornirano, eeopdv_tipprom, eeopdv_avans,eeopdv_dokumentstorno, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 OR eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD' or left(brnal,2)='KA') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 1, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.7' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 0, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.2' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 2, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.9' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    insert into tmp_ez_popdv_promet select brnal, datpdv, sum(osnovicaos), sum(pdvos), sum(osnovicaps), sum(pdvps), 3, potvrdjeno, stornirano, 5, 0,0, popdv_Promet.operater, popdv_promet.ts from popdv_promet,tmp_zaglavljep
    where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and status=1 and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD') and not (eeopdv_tipprom=3 or eeopdv_tipprom=4) and popdvid = '3.6' and left(brnal,2) = 'KA' group by brnal,eeopdv_tipprom;
    
    update tmp_ez_popdv_promet set osnovicaos= pdvos/(getpdv('S1',datpdv)/100), osnovicaps= pdvps/(getpdv('S2',datpdv)/100) where ((left(brnal,2)='OK' or left(brnal,2)='AR') or (left(brnal,2)='RA' and eeopdv_dokumentstorno=1)) and (pdvos<0 or pdvps<0) and eeopdv_avans = 1 and (osnovicaos=0 and osnovicaps=0);

    
    insert into tmp_zbirnapp select godina, period, brnal,1, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=0;
          
    
    insert into tmp_zbirnapp select godina, period, brnal,2, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0    
      from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=1;

    
    insert into tmp_zbirnapp select godina, period, brnal,3, osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0          
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=2;          
    
    insert into tmp_zbirnapp select godina, period, brnal,if(eeopdv_avans=0,4,5), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0                
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<0) or (not pdvps<0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=3;

    
    insert into tmp_zbirnapp select godina, period, brnal,if(eeopdv_avans=0,6,7), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0                      
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and ((not pdvos<=0) or (not pdvps<=0)) and period<20 and tipevidencije=0 and eeopdv=3 and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=4;    
   
   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),8, if(eeopdv_avans=0,9,10)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=5 and eeopdv_dokumentstorno=0;
    
   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),11, if(eeopdv_avans=0,12,13)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0             
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=6 and eeopdv_dokumentstorno=0;

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),14, if(eeopdv_avans=0,15,16)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0      
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=7 and eeopdv_dokumentstorno=1;        

   
    insert into tmp_zbirnapp select godina, period, brnal,if(((osnovicaos>0) or (osnovicaps>0)),17, if(eeopdv_avans=0,18,19)), osnovicaos, pdvos, osnovicaps, pdvps, replace(GetOsnovniBrnal(brnal),'-RZ',''),0,operater, vremeizmene,0,0,0,datpdv,null,datpdv,0,0            
        from tmp_ez_popdv_promet,tmp_zaglavljep where month(tmp_ez_popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=0 and (eeopdv=3 or eeopdv=6) and status=1 and potvrdjeno=1 and stornirano=0 and eeopdv_tipprom=8 and eeopdv_dokumentstorno=1;          

    
    insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',brnal), eeopdv_opis), sum(osnovicaos+osnovicaps), datpdv, sum(osnovicaos) as oos , sum(osnovicaps), sum(pdvos+pdvps) as spdv, sum(ukupno), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
          eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0 and not (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5)  group by popdv_promet.originalbrnal having spdv>0;    

    
    insert into tmp_inipojedinacna select year(datpdv), MONTH(popdv_promet.datpdv), popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
    eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',originalbrnal), eeopdv_opis), ABS(sum(pdvos+pdvps)) as pdvuk, datpdv, ABS(sum(osnovicaos)) as oos , ABS(sum(osnovicaps)),
    sum(ABS(osnovicaos)*(getpdv('S1',datpdv)/100) + ABS(osnovicaps)*(getpdv('S2',datpdv)/100)) as spdv, sum(ABS(osnovicaos)*(1+(getpdv('S1',datpdv)/100))+abs(osnovicaps)*(1+(getpdv('S2',datpdv)/100))), 0, 0, 0, null,
    eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(osnovicaos)*(getpdv('S1',datpdv)/100)), sum(ABS(osnovicaps)*(getpdv('S2',datpdv)/100)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
          from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
          where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=6 and potvrdjeno=1 and status=1 and stornirano=0 group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0 and pdvuk=0;
        
    
    insert into tmp_inipojedinacna select year(datpdv), MONTH(popdv_promet.datpdv), popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi,
    eeopdv_datplac, if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',originalbrnal), eeopdv_opis), ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)), datpdv,
    ABS(sum(pdvos/(getpdv('S1',datpdv)/100))) as oos , ABS(sum(pdvps/(getpdv('S2',datpdv)/100))),sum(ABS(pdvos) + ABS(pdvps)) as spdv,ABS(sum((pdvos/(getpdv('S1',datpdv)/100))+pdvos+(pdvps/(getpdv('S2',datpdv)/100))+pdvps)),
     0, 0, 0, null, eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(abs(pdvos)), sum(ABS(pdvps)), eeopdv_osnovavans, 0, originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn
          from tmp_zaglavljep, popdv_promet left join kupci on popdv_promet.sifpar=kupci.sifra 
          where month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=6 and potvrdjeno=1 and status=1 and stornirano=0 
          group by REPLACE(popdv_promet.originalbrnal,'-RZ','') having spdv>0;  
   
   
    insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
    if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.originalbrnal), eeopdv_opis), sum(if(ukupno>0,ukupno,0)), datpdv, sum(if(osnovicaos>0,osnovicaos,0)), sum(if(osnovicaps>0,osnovicaps,0)),
    sum(pdvos+pdvps), sum(if(ukupno>0,ukupno,0)), 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, sum(pdvos), sum(pdvps), eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from tmp_zaglavljep, popdv_promet 
          left join kupci on popdv_promet.sifpar=kupci.sifra            
          WHERE month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0          
          AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and NOT (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g') group by popdv_promet.originalbrnal;

  
    insert into tmp_inipojedinacna select godina, period, popdv_promet.originalbrnal, eeopdv_pravac, kupci.pib, eeopdv_inostrana, eeopdv_tipdok, eeopdv_avansi, eeopdv_datplac,
    if(isnull(eeopdv_opis) or trim(eeopdv_opis)='',concat('PROMET PO DOKUMENTU ',popdv_promet.brnal), eeopdv_opis), zukupno, datpdv, zosnovicaos, zosnovicaps,
    (zpdvos+zpdvps), zukupno, 0, 0, 0, null,eeopdv_osnovodabira,eeopdv_brojpovdok,0, zpdvos, zpdvps, eeopdv_osnovavans, 0, popdv_promet.originalbrnal, 0, @aktivnioperater,now(),
    eeopdv_tipprometa, eeopdv_tipvzdokumenta, eeopdv_vezdokod, eeopdv_vezdokdo, brrn 
          from tmp_zaglavljep, popdv_promet 
          left join kupci on popdv_promet.sifpar=kupci.sifra 
          left join (select originalbrnal, sum(if(ukupno>0,ukupno,0)) AS zukupno, sum(if(osnovicaos>0,osnovicaos,0)) AS zosnovicaos, sum(if(osnovicaps>0,osnovicaps,0)) AS zosnovicaps, sum(pdvos) as zpdvos, sum(pdvps) as zpdvps 
          from popdv_promet where stornirano = 0 and (left(popdvid,2) = '8b' or left(popdvid,2) = '8g') group by originalbrnal) as popdv_zbir on popdv_zbir.originalbrnal = popdv_promet.originalbrnal
          WHERE month(popdv_promet.datpdv)=month(str_to_date(concat(godina,'-',LPAD(mesec,2,'00'),'-01'), '%Y-%m-%d')) and period<20 and tipevidencije=1 and eeopdv=2 and potvrdjeno=1 and status=1 and stornirano=0 
          AND (eeopdv_tipvzdokumenta=4 or eeopdv_tipvzdokumenta=5) and (left(srcpopdvid,2)='8b' or left(srcpopdvid,2)='8g')
          group by popdv_promet.originalbrnal;  
  end if;

  
  update tmp_inipojedinacna left join (select originalbrnal, popdvid from popdv_promet where popdvid = '4.2.4') as mypopdv_promet on tmp_inipojedinacna.biznisoftbrnal=mypopdv_promet.originalbrnal, tmp_zaglavljep 
  set osnovicaos = pdvvs/(getpdv('S1',datprom)/100), osnovicans = pdvns/(getpdv('S2',datprom)/100) 
  where tmp_inipojedinacna.period=tmp_zaglavljep.period and tmp_zaglavljep.status<2 and tmp_zaglavljep.tipevidencije=1 and mypopdv_promet.popdvid = '4.2.4' and (osnovicaos=0 and osnovicans=0);

  
  update tmp_inipojedinacna, tmp_zaglavljep, 
  (select originalbrnal,eeopdv_avansi, sum(osnovicaos) as osnovicaos, sum(osnovicaps) as osnovicaps, sum(bezodbitka) as bezodbitka from popdv_promet where (left(popdvid,3)='3a.' or left(popdvid,3)='8b.' or left(popdvid,3)='8g.') and potvrdjeno=1 and stornirano=0 and not (left(brnal,2)='OD' or left(brnal,2)='ZD')  group by originalbrnal) as popdv_promet     
     set tmp_inipojedinacna.osnovicaos=tmp_inipojedinacna.osnovicaos+popdv_promet.osnovicaos, tmp_inipojedinacna.osnovicans=tmp_inipojedinacna.osnovicans+popdv_promet.osnovicaps, odbitak=0 
       where tmp_inipojedinacna.godina=tmp_zaglavljep.godina and tmp_inipojedinacna.period=tmp_zaglavljep.period and tmp_zaglavljep.status<2 and tmp_zaglavljep.tipevidencije=1 and tmp_inipojedinacna.biznisoftbrnal=popdv_promet.originalbrnal AND (tipdok=4 or tipdok=5) and (osnovodabira = 2 or tipvzdokumenta=0) and pravac=1;

  update tmp_inipojedinacna, tmp_zaglavljep set ukupno=osnovicaos+osnovicans+pdv, ukupnonaknada=osnovicaos+osnovicans+pdv
  where tmp_inipojedinacna.godina=tmp_zaglavljep.godina and tmp_inipojedinacna.period=tmp_zaglavljep.period and tmp_zaglavljep.status<2 and tmp_zaglavljep.tipevidencije=1 and pravac=1 AND (tipdok=4 or tipdok=5) and (osnovodabira = 2 or tipvzdokumenta=0);

  
  update tmp_inipojedinacna set ukupnonaknada=osnovicaos+pdvvs+osnovicans+pdvns where pravac=0 AND ukupnonaknada<(osnovicaos+pdvvs+osnovicans+pdvns);

  
  delete from tmp_zaglavljep where tipevidencije=1 and status<2 and (select count(*) from tmp_inipojedinacna where tmp_zaglavljep.godina=tmp_inipojedinacna.godina and tmp_zaglavljep.period=tmp_inipojedinacna.period)=0;

  
  update tmp_inipojedinacna set brintracuna = null where not (tipdok = 4 or tipdok = 5);

 update tmp_zaglavljep, my_eeopdv set tmp_zaglavljep.status = my_eeopdv.status, tmp_zaglavljep.datzak =my_eeopdv.datzak where tmp_zaglavljep.godina=my_eeopdv.godina and tmp_zaglavljep.period=my_eeopdv.period and tmp_zaglavljep.tipevidencije=my_eeopdv.tipevidencije;
 
 update tmp_zbirnapp left join tmp_zaglavljep on tmp_zbirnapp.godina=tmp_zaglavljep.godina and tmp_zbirnapp.period=tmp_zaglavljep.period and tmp_zaglavljep.tipevidencije=0 set tmp_zbirnapp.status_evidencije = 1, tmp_zbirnapp.datumevidencije=tmp_zaglavljep.datzak where tmp_zaglavljep.status = 4;
 
 update tmp_zbirnapp set uslov = 1;
 update tmp_zbirnapp set uslov = 0 where left(brnal,2) = 'KA' or vrsta in (4,5,6,7,9,10,11,12,13,14,15,16,17,18,19) or left(brnal,3) = 'REF';
 update tmp_zbirnapp set osnovicavs = abs(osnovicavs), pdvvs=abs(pdvvs), pdvns=abs(pdvns), osnovicans=abs(osnovicans);
 insert ignore into eeopdv_zbirna select * from tmp_zbirnapp;

 
 update tmp_inipojedinacna, my_eeopdv_pojedinacna set tmp_inipojedinacna.pravac = my_eeopdv_pojedinacna.pravac, tmp_inipojedinacna.pib = my_eeopdv_pojedinacna.pib, tmp_inipojedinacna.inostrana = my_eeopdv_pojedinacna.inostrana,
 tmp_inipojedinacna.tipdok = my_eeopdv_pojedinacna.tipdok, tmp_inipojedinacna.avansi = my_eeopdv_pojedinacna.avansi, tmp_inipojedinacna.datplac = my_eeopdv_pojedinacna.datplac, tmp_inipojedinacna.opis = my_eeopdv_pojedinacna.opis,
 tmp_inipojedinacna.ukupnonaknada = my_eeopdv_pojedinacna.ukupnonaknada, tmp_inipojedinacna.datprom = my_eeopdv_pojedinacna.datprom, tmp_inipojedinacna.osnovicaos = my_eeopdv_pojedinacna.osnovicaos, 
 tmp_inipojedinacna.osnovicans = my_eeopdv_pojedinacna.osnovicans, tmp_inipojedinacna.pdv = my_eeopdv_pojedinacna.pdv, tmp_inipojedinacna.ukupno = my_eeopdv_pojedinacna.ukupno,tmp_inipojedinacna.odbitak = 0,
 tmp_inipojedinacna.poslato = my_eeopdv_pojedinacna.poslato, tmp_inipojedinacna.individualvatid = my_eeopdv_pojedinacna.individualVatId, tmp_inipojedinacna.datzak = my_eeopdv_pojedinacna.datzak,tmp_inipojedinacna.osnovodabira = my_eeopdv_pojedinacna.osnovodabira,
 tmp_inipojedinacna.povezanidokumenti = my_eeopdv_pojedinacna.povezanidokumenti, tmp_inipojedinacna.otkazano = my_eeopdv_pojedinacna.otkazano, tmp_inipojedinacna.pdvvs = my_eeopdv_pojedinacna.pdvvs, tmp_inipojedinacna.pdvns = my_eeopdv_pojedinacna.pdvns,
 tmp_inipojedinacna.osnovavansa = my_eeopdv_pojedinacna.osnovavansa, tmp_inipojedinacna.eksterno = my_eeopdv_pojedinacna.eksterno, tmp_inipojedinacna.biznisoftbrnal = my_eeopdv_pojedinacna.biznisoftbrnal,tmp_inipojedinacna.tipunosa = my_eeopdv_pojedinacna.tipunosa,
 tmp_inipojedinacna.operater = my_eeopdv_pojedinacna.operater, tmp_inipojedinacna.vremeizmene = my_eeopdv_pojedinacna.vremeizmene,tmp_inipojedinacna.tip_prometa = my_eeopdv_pojedinacna.tip_prometa,tmp_inipojedinacna.tipvzdokumenta = my_eeopdv_pojedinacna.tipvzdokumenta,
 tmp_inipojedinacna.vezdokod = my_eeopdv_pojedinacna.vezdokod, tmp_inipojedinacna.vezdokdo = my_eeopdv_pojedinacna.vezdokdo, tmp_inipojedinacna.brintracuna = my_eeopdv_pojedinacna.brintracuna where 
 tmp_inipojedinacna.godina = my_eeopdv_pojedinacna.godina and tmp_inipojedinacna.brnal = right(my_eeopdv_pojedinacna.brnal,length(my_eeopdv_pojedinacna.brnal)-3) and tmp_inipojedinacna.period = my_eeopdv_pojedinacna.period;

  insert ignore into eeopdv_pojedinacna select godina, period, tmp_inipojedinacna.brnal, 1, pravac, pib, inostrana, tipdok, avansi, datplac, tmp_inipojedinacna.opis, ukupnonaknada,datprom, osnovicaos, osnovicans, pdv,
  odbitak, poslato, individualvatid,datzak, osnovodabira, povezanidokumenti, otkazano, pdvvs, pdvns, osnovavansa, eksterno,biznisoftbrnal, tipunosa, operater, vremeizmene, tip_prometa, tipvzdokumenta, vezdokod, vezdokdo,
  brintracuna,0,0,1, veznaefakture.status,poslato, datprom, 0 from tmp_inipojedinacna left join veznaefakture on tmp_inipojedinacna.biznisoftbrnal=veznaefakture.brnal and veznaefakture.primljena = 0 ;  
END
```

---

## 37. FormirajVeznu

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `FormirajVeznu`(klijent int(10), godina int(4), mybrnal varchar(15))
BEGIN
  drop temporary table if exists veznazapopdv;
  create temporary table veznazapopdv (brnal varchar(50) not null, status enum('uradu','spremno','spremnoa','neregistrujese','poslato','arhivirano','slanjeutoku','obrisano','prihvaceno','odbijeno','otkazano','storno','istekla','greska','nepoznato','placeno','dokumentstorno','vidjeno','podsecen','ponovoobavesten','primljeno','eksterno') DEFAULT NULL, primary key (brnal)) engine=memory;
  
  if trim(mybrnal)='' then

    
    insert ignore into veznazapopdv select brnal, status from veznaefakture where primljena=0 and trim(brnal)<>'' and not isnull(brnal) and idfakture>0;
    
    insert ignore into veznazapopdv select brnal, status from veznaefakture where primljena=0 and trim(brnal)<>'' and not isnull(brnal) and not (idfakture>0);
    
    SET @aa=CONCAT('insert ignore into veznazapopdv select biznisoftbrnal, status from ',@bsliveid,'biznisoftbinaries.sef_sales use index (indyy) where klijent=',klijent,' and godina=',godina);
    PREPARE stmt FROM @aa; EXECUTE stmt; 
    
    SET @aa=CONCAT('insert ignore into veznazapopdv select if((position('': '' in biznisoftbrnal)>0), right(biznisoftbrnal, length(biznisoftbrnal)- (position('': '' in biznisoftbrnal)+1)) ,biznisoftbrnal ), if(isnull(veznaefakture.status), sef_purchase.status, veznaefakture.status) as status from ',
        @bsliveid,'biznisoftbinaries.sef_purchase use index (indyy) left join veznaefakture on veznaefakture.brnal=sef_purchase.brnal and veznaefakture.primljena=1 where klijent=',klijent,' and godina=',godina,' and trim(biznisoftbrnal)<>"" and not isnull(biznisoftbrnal)');
    PREPARE stmt FROM @aa; EXECUTE stmt; 
  else
  
    insert ignore into veznazapopdv select brnal, status from veznaefakture where primljena=0 and trim(brnal)<>'' and not isnull(brnal) and idfakture>0 and brnal=mybrnal;
    
    insert ignore into veznazapopdv select brnal, status from veznaefakture where primljena=0 and trim(brnal)<>'' and not isnull(brnal) and not (idfakture>0) and brnal=mybrnal;
    
    SET @aa=CONCAT('insert ignore into veznazapopdv select biznisoftbrnal, status from ',@bsliveid,'biznisoftbinaries.sef_sales use index (indyy) where klijent=',klijent,' and godina=',godina,' and biznisoftbrnal="',mybrnal,'"');
    PREPARE stmt FROM @aa; EXECUTE stmt; 
    
    SET @aa=CONCAT('insert ignore into veznazapopdv select if((position('': '' in biznisoftbrnal)>0), right(biznisoftbrnal, length(biznisoftbrnal)- position('': '' in biznisoftbrnal)+1) ,biznisoftbrnal ), if(isnull(veznaefakture.status), sef_purchase.status, veznaefakture.status) as status from ',
        @bsliveid,'biznisoftbinaries.sef_purchase use index (indyy) left join veznaefakture on veznaefakture.brnal=sef_purchase.brnal and veznaefakture.primljena=1 where klijent=',klijent,' and godina=',godina,' and trim(biznisoftbrnal)<>"" and not isnull(biznisoftbrnal) and biznisoftbrnal="',mybrnal,'"');
    PREPARE stmt FROM @aa; EXECUTE stmt; 
  end if;
END
```

---

## 38. GetEEPAnalytics

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetEEPAnalytics`(mygodina int(4), myperiod int(2), myid varchar(10), myklijent int(10))
BEGIN
  drop temporary table if exists tmp_eep_analytics;
  CREATE TEMPORARY TABLE `tmp_eep_analytics` (
    `godina` int(6) DEFAULT NULL,
    `period` int(2) DEFAULT NULL,
    `VatPosition` varchar(10) DEFAULT NULL,
    `DocumentNumber` varchar(100) DEFAULT NULL,
    `systemid` varchar(50) DEFAULT NULL,
    `source` int(1) DEFAULT NULL,
    `status` varchar(50) DEFAULT NULL,
    `supplierid` varchar(20) DEFAULT NULL,
    `vatperiod` date NOT NULL,
    `processingdate` date DEFAULT NULL,
    `HigherRateBaseValue` double(15,2) DEFAULT NULL,
    `HigherRateVatValue` double(15,2) DEFAULT NULL,
    `LowerRateBaseValue` double(15,2) DEFAULT NULL,
    `LowerRateVatValue` double(15,2) DEFAULT NULL,
    `sifkupefakt` int(5),
    `nazkupefakt` varchar(500) DEFAULT NULL,
    `biznisoftbrnal` varchar(50) DEFAULT NULL,
    `tipdok` enum('tdfaktura','tdodobrenje','tdzaduzenje','tdavans') DEFAULT NULL,
    `datumslanja` date,
    `datumprometa` date,
    `datumprihvatanja` datetime DEFAULT NULL,
    `iskazanpdv` date DEFAULT NULL,
    `evidentirano` int(1) NOT NULL DEFAULT '0');

   alter table tmp_eep_analytics engine=memory;

  set @aa=concat('insert into tmp_eep_analytics 
    select vatAnalytics.godina, vatAnalytics.period, vatAnalytics.VatPosition, vatAnalytics.DocumentNumber,vatAnalytics.systemid,vatAnalytics.source,vatAnalytics.status,vatAnalytics.supplierid,vatAnalytics.vatperiod, 
      vatAnalytics.processingdate, vatAnalytics.HigherRateBaseValue,vatAnalytics.HigherRateVatValue, vatAnalytics.LowerRateBaseValue, vatAnalytics.LowerRateVatValue,
       kupci.sifra as sifkupefakt, kupci.naziv as nazkupefakt, sef_purchase.biznisoftbrnal, sef_purchase.tipdok, sef_purchase.datumslanja, sef_purchase.datumprometa, sef_purchase.datumprihvatanja, sef_purchase.iskazanpdv, 0 as evidentirano
  from vatAnalytics
  left join kupci on vatAnalytics.source=1 and vatAnalytics.supplierid=kupci.pib and trim(vatAnalytics.supplierid)<>"" and not isnull(vatAnalytics.supplierid)
  left join ',@bsliveid,'biznisoftbinaries.sef_purchase on sef_purchase.klijent=',myklijent,' and sef_purchase.godina=',mygodina,' and sef_purchase.idfakture=vatAnalytics.systemid and vatAnalytics.source=1 and trim(vatAnalytics.systemid)<>"" and not isnull(vatAnalytics.systemid)
    where vatAnalytics.godina=',mygodina,' and period=',myperiod,' and VatPosition="',myid,'"');
  prepare stmt from @aa;
  execute stmt;
  update tmp_eep_analytics, eeopdv_pojedinacna use index(myind1) set tmp_eep_analytics.SupplierID=eeopdv_pojedinacna.pib, tmp_eep_analytics.biznisoftbrnal=concat(eeopdv_pojedinacna.godina,': ',eeopdv_pojedinacna.biznisoftbrnal)
    where tmp_eep_analytics.systemID=eeopdv_pojedinacna.individualVatId and tmp_eep_analytics.source=2 and trim(tmp_eep_analytics.systemid)<>'' and not isnull(tmp_eep_analytics.systemid); 
  update tmp_eep_analytics, kupci set tmp_eep_analytics.sifkupefakt=kupci.sifra and tmp_eep_analytics.nazkupefakt=kupci.naziv where tmp_eep_analytics.SupplierID=kupci.pib and tmp_eep_analytics.source=2 and trim(tmp_eep_analytics.supplierid)<>'' and not isnull(tmp_eep_analytics.supplierid); 



  update tmp_eep_analytics, eeppdv_promet use index(myind1)  set tmp_eep_analytics.evidentirano=1 where tmp_eep_analytics.godina=eeppdv_promet.godina and tmp_eep_analytics.period=eeppdv_promet.period and eeppdv_promet.izvor=myid and eeppdv_promet.idefakture=tmp_eep_analytics.systemID and tmp_eep_analytics.source=1 and trim(tmp_eep_analytics.systemid)<>'' and not isnull(tmp_eep_analytics.systemid);
  
  update tmp_eep_analytics, eeppdv_promet use index(myind2) set tmp_eep_analytics.evidentirano=1 where tmp_eep_analytics.godina=eeppdv_promet.godina and tmp_eep_analytics.period=eeppdv_promet.period and eeppdv_promet.izvor=myid and tmp_eep_analytics.DocumentNumber=eeppdv_promet.brdokum and tmp_eep_analytics.SupplierID=eeppdv_promet.pib and tmp_eep_analytics.source=1 and trim(tmp_eep_analytics.SupplierID)<>'' and not isnull(tmp_eep_analytics.SupplierID);
  update tmp_eep_analytics, eeppdv_promet use index(myind3) set tmp_eep_analytics.evidentirano=1 where tmp_eep_analytics.godina=eeppdv_promet.godina and tmp_eep_analytics.period=eeppdv_promet.period and eeppdv_promet.izvor=myid and tmp_eep_analytics.DocumentNumber=concat(right(mygodina,2),'-',eeppdv_promet.biznisoftbrnal) and tmp_eep_analytics.source=2;

  update tmp_eep_analytics set datumprometa=null where datumprometa=0;
  update tmp_eep_analytics set HigherRateBaseValue=0 where isnull(HigherRateBaseValue);
  update tmp_eep_analytics set HigherRateVatValue=0 where isnull(HigherRateVatValue);
  update tmp_eep_analytics set LowerRateBaseValue=0 where isnull(LowerRateBaseValue);
  update tmp_eep_analytics set LowerRateVatValue=0 where isnull(LowerRateVatValue);
end
```

---

## 39. getEvidencijaStorno

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `getEvidencijaStorno`(firma int(4), godina int(4))
begin
  declare bazafirma varchar(50);
  declare primfakture varchar(50);
  declare poslfakture varchar(50);
  declare mytabela varchar(50);
  declare mytipkljuca int(3);
  declare mysifra varchar(10);
  declare done boolean default false;
  declare selectCursor CURSOR for select sifra, tabela, tipkljuca from pomocna1 group by sifra, tipkljuca, tabela;
  declare continue handler for not found set done = TRUE;
  set primfakture = concat(@bsliveid,'biznisoftbinaries.sef_purchase');
  set poslfakture = concat(@bsliveid,'biznisoftbinaries.sef_sales');

  truncate evidencijaStorno;

  set @q= concat('insert into evidencijaStorno select ',primfakture,'.brnal, ',primfakture,'.idfakture,0, datumslanja, datumstorno, ukupnoosnovica, ukupnopdv from ',primfakture,
  ' left join veznaefakture on ',primfakture,'.brnal=veznaefakture.brnal and veznaefakture.primljena=1 where veznaefakture.status= ''storno'' and ',
  primfakture,'.klijent=',firma,' and ',primfakture,'.godina=',godina);

  prepare stmt from @q;
  execute stmt;
  deallocate prepare stmt; 

  set @q= concat('insert into evidencijaStorno select ',poslfakture,'.brnal, ',poslfakture,'.biznisoftbrnal,1, datumslanja, datumstorno, ukupnoosnovica, ukupnopdv from ',poslfakture,
  ' left join veznaefakture on ',poslfakture,'.biznisoftbrnal=veznaefakture.brnal and veznaefakture.primljena=0 where veznaefakture.status= ''storno'' and ',
  poslfakture,'.klijent=',firma,' and ',poslfakture,'.godina=',godina);

  prepare stmt from @q;
  execute stmt;
  deallocate prepare stmt; 

  
  drop table if exists pomocna;
  create table pomocna like evidencijastorno;
  alter table pomocna add stornobrnal varchar(50);
  insert ignore into pomocna select pov_brnal, pov_brnal, 1, null, datumnaloga, (osnovicavs+osnovicans), (pdvvs+pdvns), eeopdv_zbirna.biznisoftbrnal
  from eeopdv_zbirna
  left join veze on eeopdv_zbirna.biznisoftbrnal=veze.brnal
  where vrsta in (14,15,16,17,18,19) and not (isnull(pov_brnal) or trim(pov_brnal)='');

  
  delete pomocna from pomocna left join evidencijastorno on pomocna.brojnaloga=evidencijastorno.iddokumenta where not (isnull(evidencijastorno.brojnaloga) or trim(evidencijastorno.brojnaloga) = '');
  
  drop table if exists pomocna1;
  create table pomocna1 as select pomocna.*, sifra, tabela, tipkljuca from pomocna left join opp.documents on left(brojnaloga,2)=opp.documents.sifra;

  open selectCursor;
  read_loop: loop fetch selectCursor into mysifra, mytabela, mytipkljuca;
    if done then 
      leave read_loop;
    end if;
      
      if ((mytipkljuca = 2) or (mytipkljuca = 13)) and not (mysifra='OD' or mysifra='ZD') then
        if (mytipkljuca = 13) then
          set @q = concat('update pomocna,',mytabela,' set pomocna.datumizdavanja=',mytabela,'.datnal where pomocna.brojnaloga=',mytabela,'.biznisoftbrnal');
        else          
          set @q = concat('update pomocna,',mytabela,' set pomocna.datumizdavanja=',mytabela,'.datumslanja where pomocna.brojnaloga=',mytabela,'.biznisoftbrnal');
        end if;
      else
        set @q = concat('update pomocna,',mytabela,' set pomocna.datumizdavanja=',mytabela,'.datum where pomocna.brojnaloga=',mytabela,'.biznisoftbrnal');    
      end if;      
      prepare stmt from @q;
      execute stmt;
      deallocate prepare stmt;

  end loop read_loop;
  close selectCursor;
  insert into evidencijastorno select brojnaloga, iddokumenta, pravac, datumizdavanja, datumstorniranja, osnovica, pdv from pomocna;
    
end
```

---

## 40. GetNabCena

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetNabCena`(sifraKupca int(6), sifraArtikla int(6), objekat int(3), brDok varchar(30))
BEGIN
  DECLARE tabela varchar(30);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE tmpCursor CURSOR FOR SELECT * FROM tmp_Tabele;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS tmp_Tabele;
  CREATE TEMPORARY TABLE tmp_Tabele(tabela varchar(30));
  SET @nabCena = NULL;
  SET @q = CONCAT('INSERT INTO tmp_Tabele SELECT tabela FROM ', @bsliveid,
                  'opp.documents WHERE tipkljuca = 1 ORDER BY (sifra = ''KL'') DESC, (sifra = ''DK'') DESC, sifra');
  PREPARE stmt FROM @q;
  EXECUTE stmt;
 
  
  OPEN tmpCursor;
  read_loop:
  LOOP FETCH tmpCursor INTO tabela;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET @q = CONCAT('SELECT (vrednost - rabat) / kolicina INTO @nabCena FROM ', tabela, ' WHERE dobavljac = ', sifraKupca, 
                    ' AND sifra = ', sifraArtikla, ' AND kolicina > 0 AND cena > 0 AND sifobj = ', objekat, 
                    ' AND brdok = ', QUOTE(brDok), ' ORDER BY datum DESC, brkalk DESC LIMIT 1');                
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    IF NOT ISNULL(@nabCena) THEN LEAVE read_loop; END IF;
    SET done = FALSE;
  END LOOP read_loop;
  ClOSE tmpCursor;

  
  IF ISNULL(@nabCena) THEN
    SET done = FALSE;
    OPEN tmpCursor;
    read_loop:
    LOOP FETCH tmpCursor INTO tabela;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET @q = CONCAT('SELECT (vrednost - rabat) / kolicina INTO @nabCena FROM ', tabela, ' WHERE dobavljac = ', sifraKupca, 
                    ' AND sifra = ', sifraArtikla, ' AND kolicina > 0 AND cena > 0 AND brdok = ', QUOTE(brdok), 
                    ' ORDER BY datum DESC, brkalk DESC LIMIT 1');
    PREPARE stmt FROM @q;
    EXECUTE stmt; 
    IF NOT ISNULL(@nabCena) THEN LEAVE read_loop; END IF;
    SET done = FALSE;  
    END LOOP read_loop;
    CLOSE tmpCursor;
  END IF;
    
  
  IF ISNULL(@nabCena) THEN
    SET done = FALSE;    
    OPEN tmpCursor;   
    read_loop:
    LOOP FETCH tmpCursor INTO tabela;
    IF done THEN
      LEAVE read_loop;
    END IF;  
    SET @q = CONCAT('SELECT (vrednost - rabat) / kolicina INTO @nabCena FROM ', tabela, ' WHERE dobavljac = ', sifraKupca, 
                    ' AND sifra = ', sifraArtikla, ' AND kolicina > 0 AND cena > 0 AND sifobj = ', objekat, 
                    ' ORDER BY datum DESC, brkalk DESC LIMIT 1');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    IF NOT ISNULL(@nabCena) THEN LEAVE read_loop; END IF;
    SET done = FALSE;    
    END LOOP read_loop;  
    CLOSE tmpCursor; 
  END IF;

  
  IF ISNULL(@nabCena) THEN
    SET done = FALSE;
    OPEN tmpCursor;
    read_loop:
    LOOP FETCH tmpCursor INTO tabela;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET @q = CONCAT('SELECT (vrednost - rabat) / kolicina INTO @nabCena FROM ', tabela, ' WHERE dobavljac = ', sifraKupca, 
                    ' AND sifra = ', sifraArtikla, ' AND kolicina > 0 AND cena > 0 ORDER BY datum DESC, brkalk DESC LIMIT 1');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    IF NOT ISNULL(@nabCena) THEN LEAVE read_loop; END IF;
    SET done = FALSE; 
    END LOOP read_loop;  
    CLOSE tmpCursor;
  END IF;  
END
```

---

## 41. GetNextBrNal

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetNextBrNal`(brNal varchar(50), godina int(4))
BEGIN
  DECLARE polje varchar(5);
  DECLARE sufix int(4);
  DECLARE baza varchar(20);
  Declare narednagodina varchar(150);
  DECLARE tabele varchar(150) DEFAULT 'robno,finprom,pk1,popdv_promet,eeppdv_promet,eeopdv_pojedinacna,eeopdv_zbirna,trgovacka';
  SET baza = DATABASE();
  SET sufix = 0;
  SET polje = 'brnal';
  IF godina <> 0 THEN SET baza = CONCAT(LEFT(baza, LENGTH(baza) - 4), godina); END IF;
  WHILE tabele != '' DO
    SET @tabela = SUBSTRING_INDEX(tabele, ',', 1);
    IF @tabela = 'trgovacka' THEN SET polje = 'brdok'; END IF;      
    IF (@tabela = 'eeopdv_zbirna') or (@tabela = 'eeopdv_pojedinacna') or (@tabela = 'eeppdv_promet') THEN 
      SET narednagodina = ' and ((narednagodina=0) or (isnull(narednagodina))) and not (tipunosa = 1) ';
    else
      set narednagodina='';
    END IF;
    SET @q = CONCAT('SELECT COUNT(*) INTO @count FROM (SELECT ', polje, ' FROM ', baza, '.', @tabela, ' WHERE ((', polje,' = ', QUOTE(brnal),
                    ') OR (', polje,' LIKE ', QUOTE(CONCAT(brnal, '/%')), ')) ',narednagodina,' GROUP BY ', polje,') AS alias');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    
    IF LOCATE(',', tabele) > 0 THEN SET tabele = SUBSTRING(tabele, LOCATE(',', tabele) + 1); ELSE SET tabele = ''; END IF;
    IF @count > sufix THEN SET sufix = @count; END IF;
  END WHILE;

  IF sufix = 0 THEN SET @nextBrNal = brnal; ELSE SET @nextBrNal = CONCAT(brnal, '/', sufix); END IF;
  SET tabele = 'robno,finprom,pk1,popdv_promet,eeppdv_promet,eeopdv_pojedinacna,eeopdv_zbirna,trgovacka';
  SET polje = 'brnal';

  WHILE tabele != '' DO
    SET @tabela = SUBSTRING_INDEX(tabele, ',', 1);
    IF @tabela = 'trgovacka' THEN SET polje = 'brdok'; END IF;
    IF (@tabela = 'eeopdv_zbirna') or (@tabela = 'eeopdv_pojedinacna') or (@tabela = 'eeppdv_promet') THEN 
      SET narednagodina = ' and ((narednagodina=0) or (isnull(narednagodina))) and not (tipunosa = 1) ';
    else
      set narednagodina='';
    END IF;
    SET @q = CONCAT('SELECT COUNT(', polje, ') INTO @count FROM ', baza, '.', @tabela, ' WHERE ', polje, ' = ', QUOTE(@nextBrNal), ' ',narednagodina,' LIMIT 1');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    IF @count > 0 THEN       
      SET @nextBrNal = CONCAT(brnal, '/', sufix + 1);
      SET tabele = 'robno,finprom,pk1,popdv_promet,eeppdv_promet,eeopdv_pojedinacna,eeopdv_zbirna,trgovacka';
      SET polje = 'brnal';
      WHILE tabele != '' DO
        SET @tabela = SUBSTRING_INDEX(tabele, ',', 1);
        IF @tabela = 'trgovacka' THEN SET polje = 'brdok'; END IF;
        IF (@tabela = 'eeopdv_zbirna') or (@tabela = 'eeopdv_pojedinacna') or (@tabela = 'eeppdv_promet') THEN 
          SET narednagodina = ' and ((narednagodina=0) or (isnull(narednagodina))) and not (tipunosa = 1) ';
        else
          set narednagodina='';
        END IF;
        SET @q = CONCAT('SELECT COUNT(', polje, ') INTO @count FROM ', baza, '.', @tabela, ' WHERE ', polje, ' = ', QUOTE(@nextBrNal), ' ',narednagodina,' LIMIT 1');
        PREPARE stmt FROM @q;
        EXECUTE stmt;
        IF @count > 0 THEN       
          SET @nextBrNal = CONCAT(brnal, '/', sufix + 2);
          SET tabele = 'robno,finprom,pk1,popdv_promet,eeppdv_promet,eeopdv_pojedinacna,eeopdv_zbirna,trgovacka';
          SET polje = 'brnal';
          WHILE tabele != '' DO
            SET @tabela = SUBSTRING_INDEX(tabele, ',', 1);
            IF @tabela = 'trgovacka' THEN SET polje = 'brdok'; END IF;
            IF (@tabela = 'eeopdv_zbirna') or (@tabela = 'eeopdv_pojedinacna') or (@tabela = 'eeppdv_promet') THEN 
              SET narednagodina = ' and ((narednagodina=0) or (isnull(narednagodina))) and not (tipunosa = 1) ';
            else
              set narednagodina='';
            END IF;
            SET @q = CONCAT('SELECT COUNT(', polje, ') INTO @count FROM ', baza, '.', @tabela, ' WHERE ', polje, ' = ', QUOTE(@nextBrNal), ' ',narednagodina,' LIMIT 1');
            PREPARE stmt FROM @q;
            EXECUTE stmt; 
            IF @count > 0 THEN       
              SET @nextBrNal = CONCAT(brnal, '/', sufix + 3);
              SET tabele = 'robno,finprom,pk1,popdv_promet,eeppdv_promet,eeopdv_pojedinacna,eeopdv_zbirna,trgovacka';
              SET polje = 'brnal';
              WHILE tabele != '' DO
                SET @tabela = SUBSTRING_INDEX(tabele, ',', 1);
                IF @tabela = 'trgovacka' THEN SET polje = 'brdok'; END IF;
                IF (@tabela = 'eeopdv_zbirna') or (@tabela = 'eeopdv_pojedinacna') or (@tabela = 'eeppdv_promet') THEN 
                  SET narednagodina = ' and ((narednagodina=0) or (isnull(narednagodina))) and not (tipunosa = 1) ';
                else
                  set narednagodina='';
                END IF;
                SET @q = CONCAT('SELECT COUNT(', polje, ') INTO @count FROM ', baza, '.', @tabela, ' WHERE ', polje, ' = ', QUOTE(@nextBrNal), ' ',narednagodina,' LIMIT 1');
                PREPARE stmt FROM @q;
                EXECUTE stmt;
                IF @count > 0 THEN SET @nextBrNal = 'ERROR'; END IF;         
                IF LOCATE(',', tabele) > 0 THEN SET tabele = SUBSTRING(tabele, LOCATE(',', tabele) + 1); ELSE SET tabele = ''; END IF;  
              END WHILE;
            END IF;         
            IF LOCATE(',', tabele) > 0 THEN SET tabele = SUBSTRING(tabele, LOCATE(',', tabele) + 1); ELSE SET tabele = ''; END IF;  
          END WHILE;
        END IF;
        IF LOCATE(',', tabele) > 0 THEN SET tabele = SUBSTRING(tabele, LOCATE(',', tabele) + 1); ELSE SET tabele = ''; END IF;  
      END WHILE;
    END IF;
    IF LOCATE(',', tabele) > 0 THEN SET tabele = SUBSTRING(tabele, LOCATE(',', tabele) + 1); ELSE SET tabele = ''; END IF;  
  END WHILE;
END
```

---

## 42. ios

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `ios`(IN `doClose` BOOLEAN, IN `doCloseOnDate` BOOLEAN, IN `onDate` DATE, IN `DateFieldName` CHAR(30), IN `forAccounts` BOOLEAN,  IN `forCustomers` BOOLEAN, IN `doIos` BOOLEAN, 
  IN `forceClose` BOOLEAN, IN `forceChron` BOOLEAN, IN `uValuti` BOOLEAN, IN `forceZaValutu` BOOLEAN, IN `zaValutu` integer, IN `SamoSaStanjem` boolean, ZbirnoPoDokumentu Boolean, in `poslovnajed` integer)
    MODIFIES SQL DATA
BEGIN 
  DECLARE join_accounts varchar(255);
  DECLARE join_customers varchar(255);
  DECLARE p_racun varchar(20);
  DECLARE zatvaranje int(1);
  DECLARE karakter int(1);
  DECLARE mydochron int(1);
  DECLARE p_brdok varchar(20);
  DECLARE p_brnal varchar(20);
  DECLARE p_dokumveza varchar(20);
  DECLARE mysum varchar(100);
  DECLARE myvaluta varchar(50);
  DECLARE iznfak varchar(50);
  DECLARE iznupl varchar(50);
  DECLARE iznsaldo varchar(50);
  DECLARE p_izndug double(15,2);
  DECLARE poslovnajedinica varchar(50);
  DECLARE mydone int DEFAULT 0;
  DECLARE partneri CURSOR FOR SELECT * FROM tmp_customers;
  DECLARE racuni CURSOR FOR SELECT tmp_accounts.racun, kontniplan.zatvaranje, kontniplan.karakter FROM tmp_accounts, kontniplan where kontniplan.sifrakpl=@kontniplan AND kontniplan.racun=tmp_accounts.racun;
  DECLARE potrazuje CURSOR FOR SELECT brnal,dokumveza,izndug FROM temp_stavke;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET mydone = 1;
  SET join_accounts = "";
  SET join_customers = "";

  if (poslovnajed>-1) then set poslovnajedinica = concat(" and posljed=",poslovnajed); else set poslovnajedinica=""; end if;
  IF forAccounts <> 0 OR doIos=1 THEN
```

---

## 43. KnjiziTransformaciju

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `KnjiziTransformaciju`(s_sifobj int, s_brnal varchar(50), s_mysifobj int, s_condatddat varchar(50))
BEGIN
  DECLARE nabvredmat, vpvredart, nabvrednost double;
  DECLARE exit_loop boolean;
  DECLARE m_sifra int;
  DECLARE m_receptura int;
  DECLARE m_kolicina, m_vredbezpp double;
  DECLARE m_datum date;
  DECLARE dokumenti CURSOR FOR SELECT sifra, kolicina, SUM(vredbezpp), receptura, datum FROM tblrobtransf WHERE sifobj=s_sifobj and brkalk=right(GetOsnovniBrnal(s_brnal),5) GROUP by sifra;
  DECLARE CONTINUE HANDLER FOR not FOUND SET exit_loop = TRUE;

  
  INSERT INTO my_prernc_robno_2 SELECT robno.sifobj, robno.sifra, datum, robno.brnal, avgPricePrerNC(IF((s_mysifobj=1 or s_mysifobj=2),'VPC','NBC'), robno.sifobj, robno.sifra, robno.datum, SUM(kolicina), robno.condatddat, s_mysifobj) FROM robno,transfmat WHERE GetOsnovniBrnal(robno.brnal)=GetOsnovniBrnal(transfmat.brnal) AND robno.sifra=transfmat.sifra AND robno.brnal=s_brnal and stornirano=0 and not (robno.brnal like "POTVRDJENO%") GROUP by transfmat.sifra;

  

  SELECT datum into @mytrdatum FROM tblrobtransf WHERE sifobj=s_sifobj and brkalk=right(GetOsnovniBrnal(s_brnal),5) limit 1;
  SELECT SUM(kolicina*avgPricePrerNC(IF((s_mysifobj=1 or s_mysifobj=2),'VPC','NBC'), s_sifobj, sifra, @mytrdatum, kolicina, s_condatddat, s_mysifobj)) INTO nabvredmat FROM transfmat where transfmat.brnal=GetOsnovniBrnal(s_brnal) AND receptura<>1;
  IF nabvredmat is NULL then 
    SET nabvredmat=0;
  END IF;
```

---

## 44. kreirajPopis

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `kreirajPopis`(tip int(1), myID int(6), objekat int(3), datum date, vrstaCene varchar(3),
                       tag int(1), TBposition int(2), tipObjekta varchar(2), 
                       novaKolicinaNula boolean, opis varchar(1000), brPop int(4), isaambalazom int(1), samoambalaza int(1))
BEGIN 
  DECLARE bezPocetnogStanja varchar(80);
  DECLARE uslovambalaza varchar(80);
  DECLARE uslov1 varchar(30);
  DECLARE uslov2 varchar(30);
  DECLARE uslov3 varchar(30);
  DECLARE uslov4 varchar(30);
  DECLARE sifobj int(3);
  DECLARE sifra int(3);
  DECLARE naziv varchar(1000);
  DECLARE jedmere char(3);
  DECLARE suma double;
  DECLARE pdv double(15,2);
  DECLARE nosioc int(5);
  DECLARE mestotr int(6);
  DECLARE jeProizvod int(1);
  DECLARE komision880 int(1);
  DECLARE barkod varchar(15);
  DECLARE cena double;
  DECLARE vrednost double;
  DECLARE done boolean DEFAULT FALSE;
  DECLARE myKolicina double;
  DECLARE myCena double;
  DECLARE kolicina double;
  DECLARE selectStatement text;
  DECLARE serialNo int(6);
  DECLARE selectCursor CURSOR FOR SELECT * FROM selectTable;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  SET bezPocetnogStanja = ' AND NOT (robno.brnal LIKE ''PST%'' AND robno.ulaz = 0 AND robno.izlaz = 0)';
  DROP TEMPORARY TABLE IF EXISTS selectTable;
  CREATE TEMPORARY TABLE selectTable (sifobj int(3), sifra int(6), naziv varchar(1000),
                                      jedmere char(3), suma double(15,4), pdv double(15,2),
                                      nosioc int(6), mestotr int(6) , jeProizvod int(1),
                                      komision880 int(1), barkod varchar(15));

  SET uslovambalaza = ' AND artikli.jeambalaza <> 1 ';
  if isaambalazom = 1 then
    SET uslovambalaza = ' ';
  end if;
  if samoambalaza = 1 then
    SET uslovambalaza = ' AND artikli.jeambalaza = 1 ';
  end if;
                                      
  DELETE FROM popispom;
  IF tip = 1 THEN 
   SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum),'),
                                 artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM robno, artikli
                                 WHERE robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND robno.sifobj = ', objekat,' 
                                 AND artikli.jeusluga <> 1 ', bezPocetnogStanja, uslovambalaza, ' AND artikli.grupa = ', myID,'  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") GROUP BY robno.sifra ORDER BY artikli.sifra');
  END IF;        
  IF tip = 2 THEN 
    SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum),'), 
                                  artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM robno, artikli 
                                  WHERE robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND robno.sifobj = ', objekat,'  
                                  AND artikli.jeusluga <> 1 ', bezPocetnogStanja, uslovambalaza,' AND artikli.odeljenje = ', myID,'  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") GROUP BY robno.sifra ORDER BY artikli.sifra');
  END IF;
  IF tip = 3 THEN 
    IF tag = 1 THEN
      SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum),'),
                                    artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM atributiartikli, myatributi, robno, artikli
                                    WHERE atributiartikli.atribut = myatributi.sifra AND atributiartikli.sifra = artikli.sifra AND assigned = 1 AND checked = 1 
                                    AND robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND robno.sifobj = ', objekat,' 
                                    AND artikli.jeusluga <> 1 ', bezPocetnogStanja, uslovambalaza,'  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") GROUP BY robno.sifra ORDER BY artikli.sifra');
      ELSE

      DROP TEMPORARY TABLE IF EXISTS myatributi1;
      CREATE TEMPORARY TABLE myatributi1 LIKE myatributi;
      INSERT INTO myatributi1 SELECT * FROM myatributi WHERE checked = 1;
      DROP TEMPORARY TABLE IF EXISTS myatributi2;
      CREATE TEMPORARY TABLE myatributi2 LIKE myatributi;
      INSERT INTO myatributi2 SELECT * FROM myatributi WHERE checked = 1;

      SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum),'),
                                    artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM atributiartikli, myatributi, robno, 
                                    artikli WHERE atributiartikli.atribut = myatributi.sifra AND atributiartikli.sifra = artikli.sifra AND assigned = 1 
                                    AND checked = 1 AND (SELECT COUNT(*) FROM atributiartikli, myatributi1 WHERE atributiartikli.sifra = artikli.sifra 
                                    AND atributiartikli.atribut = myatributi1.sifra AND myatributi1.checked = 1 AND assigned = 1) = (SELECT COUNT(*) 
                                    FROM myatributi2 WHERE checked = 1) AND robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' 
                                    AND robno.sifobj = ', objekat,' AND artikli.jeusluga <> 1  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ', bezPocetnogStanja,uslovambalaza,' 
                                    GROUP BY robno.sifra ORDER BY artikli.sifra');
    END IF;
  END IF;
  IF tip = 4 THEN
    SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum), '),
                                  artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM robno, artikli WHERE
                                  robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND robno.sifobj = ', objekat,' AND artikli.jeusluga <> 1  and stornirano=0  and not (robno.brnal like "POTVRDJENO%")',
                                  bezPocetnogStanja, uslovambalaza, ' GROUP BY robno.sifra ORDER BY artikli.sifra');
  END IF;
  IF tip = 5 THEN
    SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(ROUND(SUM(ulaz-izlaz),5) * ', TBposition, ' / 100) AS abc, 
                                  getpdv(artikli.porez, ', QUOTE(datum),'), artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod 
                                  FROM robno, artikli WHERE robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND 
                                  robno.sifobj = ', objekat,' AND artikli.jeusluga <> 1  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ', bezPocetnogStanja, uslovambalaza,' 
                                  GROUP BY robno.sifra HAVING abc > 0 ORDER BY artikli.sifra');
  END IF;
  IF tip = 6 THEN
    SET selectStatement = CONCAT('SELECT robno.sifobj, robno.sifra, artikli.naziv, jedmere, ROUND(SUM(ulaz-izlaz),5), getpdv(artikli.porez, ', QUOTE(datum),'),
                                  artikli.nosioc, artikli.mestotr, jeproizvod, komision880, artikli.barkod FROM robno, artikli WHERE 
                                  robno.sifra = artikli.sifra AND robno.datum <= ', QUOTE(datum),' AND robno.sifobj = ', objekat,' AND 
                                  artikli.jeusluga <> 1  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ', bezPocetnogStanja, uslovambalaza,'  GROUP BY robno.sifra ORDER BY artikli.sifra');
  END IF;
  SET @insertStatement = CONCAT('INSERT INTO selectTable ', selectStatement);
  PREPARE stmt FROM @insertStatement;
  EXECUTE stmt;
  SET serialNo = 0;
  OPEN selectCursor;
  read_loop: LOOP
    
  FETCH selectCursor INTO sifobj, sifra, naziv, jedmere, suma, pdv, nosioc, mestotr, jeProizvod, komision880, barkod;
  SET @vpcc = NULL;
  SET @mpcc = NULL;
  SET @nbcc = NULL; 
  IF done THEN
    LEAVE read_loop;
  END IF;
  SET @varStatement = CONCAT('SELECT cenabezpp, cenasapp, nabcena INTO @vpcc, @mpcc, @nbcc FROM robno WHERE sifobj = ', objekat, ' AND sifra = ',
                              QUOTE(sifra),' AND izlaz = 0 AND ulaz >= 0 AND datum <=', QUOTE(datum),'  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum) DESC LIMIT 1'); 
  PREPARE stmt FROM @varStatement;
  EXECUTE stmt;
  IF ISNULL(@vpcc) OR ISNULL(@mpcc) THEN 
    SET @varStatement = CONCAT('SELECT cenabezpp, cenasapp INTO @vpcc, @mpcc FROM robno WHERE sifobj = ', 
                                objekat, ' AND sifra = ', QUOTE(sifra),'  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum) DESC LIMIT 1');
    PREPARE stmt FROM @varStatement;
    EXECUTE stmt;
  END IF; 
  IF vrstaCene = 'mpc' AND ISNULL(@mpcc) THEN SET cena = 0;
    ELSEIF vrstaCene = 'mpc' AND NOT ISNULL(@mpcc) THEN SET cena = @mpcc;     
  END IF;
  IF vrstaCene = 'vpc' AND ISNULL(@vpcc) THEN SET cena = 0;
    ELSEIF vrstaCene = 'vpc' AND NOT ISNULL(@vpcc) THEN SET cena = @vpcc;
  END IF; 
  IF vrstaCene = 'nbc' THEN
    SET myKolicina = suma; 
      IF NOT (myKolicina > 0) THEN
       SET myKolicina = 1; 
      END IF;
    SET Cena = obrNabavke(tipObjekta, objekat, sifra, myKolicina, 0, datum, vrstaCene);
```

---

## 45. KreirajTabeleZaStorno

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `KreirajTabeleZaStorno`()
BEGIN
  drop temporary table if exists tmp_storno_robno; create temporary table tmp_storno_robno like robno; 
  drop temporary table if exists tmp_storno_trgovacka; create temporary table tmp_storno_trgovacka like trgovacka; 
  drop temporary table if exists tmp_storno_finprom; create temporary table tmp_storno_finprom like finprom; 
  drop temporary table if exists tmp_storno_pk1; create temporary table tmp_storno_pk1 like pk1; 
  drop temporary table if exists tmp_storno_popdv_promet; create temporary table tmp_storno_popdv_promet like popdv_promet; 
  drop temporary table if exists tmp_storno_eeopdv_pojedinacna; create temporary table tmp_storno_eeopdv_pojedinacna like eeopdv_pojedinacna; 
  drop temporary table if exists tmp_storno_eeopdv_zbirna; create temporary table tmp_storno_eeopdv_zbirna like eeopdv_zbirna; 
  drop temporary table if exists tmp_storno_eeppdv_promet; create temporary table tmp_storno_eeppdv_promet like eeppdv_promet; 
  drop temporary table if exists tmp_storno_serbr; create temporary table tmp_storno_serbr like serbr;
END
```

---

## 46. KreirajTmpTabele

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `KreirajTmpTabele`()
BEGIN
    drop temporary table if exists tmp_robno;
    create temporary table tmp_robno like robno;
    alter table tmp_robno engine=innodb;
    alter table tmp_robno drop primary KEY;

    drop temporary table if exists tmp_trgovacka;
    create temporary table tmp_trgovacka like trgovacka;
    alter table tmp_trgovacka engine=innodb;
    alter table tmp_trgovacka drop primary KEY;

    drop temporary table if exists tmp_popdv_promet;
    create temporary table tmp_popdv_promet like popdv_promet;
    alter table tmp_popdv_promet modify osnovicaos double(25,10),modify osnovicaps double(25,10), modify pdvos double(25,10), modify pdvps double(25,10), modify bezodbitka double(25,10);
    alter table tmp_popdv_promet engine=innodb;
    alter table tmp_popdv_promet drop primary KEY;

    drop temporary table if exists tmp_pk1;
    create temporary table tmp_pk1 like pk1;
    alter table tmp_pk1 engine=innodb;
    alter table tmp_pk1 drop primary KEY;

    drop temporary table if exists tmp_knj_finprom;
    create temporary table tmp_knj_finprom like finprom;
    alter table tmp_knj_finprom modify izndug double(25,10), modify iznpot double(25,10);
    alter table tmp_knj_finprom engine=innodb;
    alter table tmp_knj_finprom drop primary KEY;

    drop temporary table if exists tmp_eeopdv_pojedinacna;
    create temporary table tmp_eeopdv_pojedinacna like eeopdv_pojedinacna;
    alter table tmp_eeopdv_pojedinacna engine=innodb;
    alter table tmp_eeopdv_pojedinacna drop primary KEY;

    drop temporary table if exists tmp_eeopdv_zbirna;
    create temporary table tmp_eeopdv_zbirna like eeopdv_zbirna;
    alter table tmp_eeopdv_zbirna modify osnovicavs double(25,10),modify osnovicans double(25,10), modify pdvvs double(25,10), modify pdvns double(25,10);
    alter table tmp_eeopdv_zbirna engine=innodb;
    alter table tmp_eeopdv_zbirna drop primary KEY;

    drop temporary table if exists tmp_eeopdv_zbirna_kasa;
    create temporary table tmp_eeopdv_zbirna_kasa like tmp_eeopdv_zbirna;

    drop temporary table if exists tmp_eeppdv_promet;
    create temporary table tmp_eeppdv_promet like eeppdv_promet;
    alter table tmp_eeppdv_promet engine=innodb;
    alter table tmp_eeppdv_promet drop primary KEY;

    alter table tmp_trgovacka order by objekat,brdok,status, vd, opis;alter table tmp_trgovacka add index indxx(objekat,brdok,status);

    drop table if exists finprompom;
    create temporary table finprompom like finprom;

    drop temporary table if exists labele;
    create temporary table `labele` (`sifra` int(8) NOT NULL DEFAULT 0, `jedmere` char(3) DEFAULT NULL, `naziv` varchar(255) DEFAULT NULL, `porez` double(15,2) DEFAULT NULL, `cena` double(15,2) DEFAULT NULL, `operater` varchar(50) NOT NULL, `staracena` double(15,3) DEFAULT NULL);
  END
```

---

## 47. labelsInsert

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `labelsInsert`(sifra int(6), operater varchar(60))
BEGIN
  DECLARE i int(1) DEFAULT 0;
  DECLARE rbr int(6); 
  DECLARE sifra1 int(6);
  DECLARE jedmere varchar(3);
  DECLARE naziv varchar(255);
  DECLARE cena double(15, 2);
  DECLARE kolnadok int(6);
  DECLARE kolzastampu int(6);
  DECLARE staraCena double(15, 2);
  DECLARE porez double(15, 2);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE selectCursor CURSOR FOR SELECT * FROM customLabels;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS mylabele1;
  CREATE TEMPORARY TABLE mylabele1 like labele;
  ALTER TABLE mylabele1 ADD INDEX ind1 (sifra);
  OPEN selectCursor;
  read_loop: LOOP
  FETCH selectCursor INTO rbr, sifra1, jedmere, naziv, cena, porez, staraCena, kolnadok, kolzastampu;
  IF done THEN
    LEAVE read_loop;
  END IF;
  SET i = 0;
  WHILE i < ROUND(kolzastampu) DO
    SET @insert = CONCAT('INSERT INTO mylabele1 VALUES(', sifra1, ',', QUOTE(jedmere), ',', QUOTE(naziv), ',', porez, ',', cena, ',', QUOTE(operater), ',', staraCena,')');
    PREPARE stmt FROM @insert;
    EXECUTE stmt;
  SET i = i + 1;
  END WHILE;
  END LOOP read_loop;
  CLOSE selectCursor;
  ALTER TABLE mylabele1 ORDER BY mylabele1.sifra;
END
```

---

## 48. lastRabatI

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `lastRabatI`(`sa` int,`dt` date, `parsifkup` integer, `proslagodina` varchar(50), `imaproslagodina` boolean)
BEGIN
  IF dt=0 THEN
    set dt=date(now());
  END IF;

  SET @lr_date := dt;
  SET @lr_sifra := sa;
  SET @lr_sifkup := parsifkup;

  drop temporary table if exists tmpmojrabat; create temporary table tmpmojrabat (datum date, faktcena double(15,6), procenat double(15,2), iznos double(15,2));
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblprodfakture where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblfaktakcrab where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblprodmat where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from fakture where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblizvoz where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1;
  IF imaproslagodina THEN
    SET @qvr=concat("insert into tmpmojrabat select datum, cena, prcrabat, rabat from ",proslagodina,".tblprodfakture where sifra=@lr_sifra and datum<=@lr_date AND sifkup=@lr_sifkup and kolicina>0 AND tip='F' order by datum desc, brrn desc limit 1");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;
```

---

## 49. lastRabatU

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `lastRabatU`(`sa` int,`dt` date, `proslagodina` varchar(50), `imaproslagodina` boolean)
BEGIN
  IF dt=0 THEN
    set dt=date(now());
  END IF;

  SET @lr_date := dt;
  SET @lr_sifra := sa;

  drop temporary table if exists tmpmojrabat; create temporary table tmpmojrabat (datum date, faktcena double(15,6), procenat double(15,2), iznos double(15,2));
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from prodkalkulacije where sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from kalkulacije WHERE sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblpoljoprivreda where sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tblotkupss where sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1;
  insert into tmpmojrabat select datum, cena, prcrabat, rabat from tbluvoz where sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1;
  IF imaproslagodina THEN
    SET @qvr=concat("insert into tmpmojrabat select datum, cena, prcrabat, rabat from ",proslagodina,".prodkalkulacije where sifra=@lr_sifra and datum<=@lr_date and kolicina >0 order by datum desc, brkalk desc limit 1");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;
```

---

## 50. myprenos1

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `myprenos1`(so int, so2 int, ignmtnt int, stanjeicene int, vrstanc int, vrstacene varchar(3), dt date, novagodina int, obrcen10je3 int, novabaza varchar(40), mytipobj1 int, jefifo int)
begin
  update robno set cena=0 where robno.sifobj=so and isnull(cena);
  update robno set nabcena=0 where robno.sifobj=so and isnull(nabcena);
  update robno set cenabezpp=0 where robno.sifobj=so and isnull(cenabezpp);
  update robno set cenasapp=0 where robno.sifobj=so and isnull(cenasapp);
  update robno set prcruc=0 where robno.sifobj=so and isnull(prcruc);

  set @mybrnalpst='PST000';
  if stanjeicene=0 then
    set @mybrnalpst='PST0';
  end if;

  drop temporary table if exists tmprobnopren;
  create temporary table tmprobnopren like robno;
  alter table tmprobnopren drop primary key;
  alter table tmprobnopren modify rbr int(4) auto_increment primary key;
  alter table tmprobnopren add dugpot double(15,2) default 0;

  
  drop temporary table if exists tmpzadcene;
  create temporary table tmpzadcene (sifra int(6) not null primary key, cena double(15,2), nabcena double(15,4), cenabezpp double(15,4), cenasapp double(15,4), prernc double (15,4), prcruc double, condatddat varchar(50), sastanjem int(1));
  alter table tmpzadcene add index ind1 (sifra, condatddat, sastanjem);
  insert into tmpzadcene select sifra, 0, 0, 0, 0, 0, 0, max(concat(datum,ddatum)),1 from robno where robno.sifobj=so and ulaz>=0 and izlaz=0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") group by robno.sifobj,sifra;
  update tmpzadcene,robno set tmpzadcene.cena=robno.cena, tmpzadcene.nabcena=robno.nabcena,tmpzadcene.cenabezpp=robno.cenabezpp, tmpzadcene.cenasapp=robno.cenasapp, tmpzadcene.prernc=robno.prernc, tmpzadcene.prcruc=robno.prcruc where robno.sifobj=so and robno.sifra=tmpzadcene.sifra and sastanjem=1 and concat(datum,ddatum)=tmpzadcene.condatddat and ulaz>=0 and izlaz=0;
  insert ignore into tmpzadcene select sifra, 0, 0, 0, 0, 0, 0, max(concat(datum,ddatum)),0 from robno where robno.sifobj=so and stornirano=0  and not (robno.brnal like "POTVRDJENO%") group by robno.sifobj,sifra;
  update tmpzadcene,robno set tmpzadcene.cena=robno.cena, tmpzadcene.nabcena=robno.nabcena,tmpzadcene.cenabezpp=robno.cenabezpp, tmpzadcene.cenasapp=robno.cenasapp, tmpzadcene.prernc=robno.prernc, tmpzadcene.prcruc=robno.prcruc where robno.sifobj=so and robno.sifra=tmpzadcene.sifra and sastanjem=0 and concat(datum,ddatum)=tmpzadcene.condatddat;

  if jefifo=0 then
  
    if ignmtnt=1 then
      insert into tmprobnopren select so2, robno.sifra,dt, @mybrnalpst, if(stanjeicene=1,round(sum(ulaz-izlaz),3),0), 0, 0, 0, null, 0, 0, 0, 0, 0, 0, makedate(novagodina,1), 'POCETNO STANJE', null, 0, 0, '', @aktivnioperater, robno.mestotr, robno.nosioc, 0, null, null, null, null, null, null, 0, makedate(novagodina,1),@mybrnalpst, sum(duguje-potrazuje) 
         from robno,artikli where robno.sifra=artikli.sifra and artikli.jeusluga=0 and robno.sifobj=so and stornirano=0  and not (robno.brnal like "POTVRDJENO%") group by robno.sifobj, robno.sifra; 
    else
      insert into tmprobnopren select so2, robno.sifra,dt, @mybrnalpst, if(stanjeicene=1,round(sum(ulaz-izlaz),3),0), 0, 0, 0, null, 0, 0, 0, 0, 0, 0, makedate(novagodina,1), 'POCETNO STANJE', null, 0, 0, '', @aktivnioperater, robno.mestotr, robno.nosioc, 0, null, null, null, null, null , null, 0, makedate(novagodina,1),@mybrnalpst, sum(duguje-potrazuje)
         from robno,artikli where robno.sifra=artikli.sifra and artikli.jeusluga=0 and robno.sifobj=so and stornirano=0  and not (robno.brnal like "POTVRDJENO%") group by robno.sifobj, robno.sifra, robno.mestotr, robno.nosioc; 
    end if;
    if vrstanc=1 then  
      update tmprobnopren set nabcena=avgprice(vrstacene, so, sifra, dt, 0);
    end if;
    if vrstanc=2 then  
      update tmprobnopren, artikli set nabcena=planskacena where tmprobnopren.sifra=artikli.sifra;
    end if;
    if vrstanc=3 then  
      update tmprobnopren, tmpzadcene set tmprobnopren.nabcena=tmpzadcene.nabcena where tmprobnopren.sifra=tmpzadcene.sifra;
    end if;
    if vrstanc=4 then  
      update tmprobnopren, tmpzadcene set tmprobnopren.nabcena=tmpzadcene.prernc where tmprobnopren.sifra=tmpzadcene.sifra;
    end if;
  
    update tmprobnopren, tmpzadcene set tmprobnopren.cena=tmpzadcene.cena, tmprobnopren.cenabezpp=tmpzadcene.cenabezpp, tmprobnopren.cenasapp=tmpzadcene.cenasapp, tmprobnopren.prcruc=tmpzadcene.prcruc where tmprobnopren.sifra=tmpzadcene.sifra;
  
    update tmprobnopren set cena=round(cena,3), nabcena=round(nabcena,4), cenabezpp=round(cenabezpp,3), cenasapp=round(cenasapp,3), prcruc=round(prcruc,3); 
  
    update tmprobnopren,artikli set nabcena=artikli.planskacena where tmprobnopren.sifra=artikli.sifra and artikli.jeambalaza=1;
    if obrcen10je3=1 then
      update tmprobnopren,artikli set nabcena=artikli.planskacena where tmprobnopren.sifra=artikli.sifra and artikli.jesirovina=1;
    end if;
  
    if upper(vrstacene)='MPC' then
      update tmprobnopren set duguje=ulaz*cenasapp;
    end if;
    if upper(vrstacene)='NBC' then
      if ((mytipobj1=8) or (mytipobj1=10)) then
        update tmprobnopren set duguje=dugpot;
      else
        update tmprobnopren set duguje=ulaz*nabcena;
      end if;
    end if;
    if upper(vrstacene)='VPC' then
      update tmprobnopren set duguje=ulaz*cenabezpp;
    end if;
    
    drop temporary table if exists tmprobnopren1;
    create temporary table tmprobnopren1 like tmprobnopren;
    insert into tmprobnopren1 select * from tmprobnopren where ulaz<0;
    update tmprobnopren1 set ulaz=0, duguje=0, prernc=nabcena;
  
    alter table tmprobnopren1 modify rbr int(4);
    alter table tmprobnopren1 drop primary key;
    update tmprobnopren1 set rbr=0;
    alter table tmprobnopren1 modify rbr int(4) not null auto_increment primary key;
    select count(*) into @cnt from tmprobnopren;
    if isnull(@cnt) then
     set @cnt=0;
    end if;
    update tmprobnopren1 set rbr=@cnt+rbr;
    insert into tmprobnopren select * from tmprobnopren1;
    
    drop temporary table if exists tmprobnopren1;
  else
    call fifopricepstAll(so, dt, vrstacene);
    alter table memall add duguje double(15,2);
    if upper(vrstacene)='MPC' then
      update memall set duguje=stock*cenasapp;
    end if;
    if upper(vrstacene)='NBC' then
        update memall set duguje=stock*nabcena;
    end if;
    if upper(vrstacene)='VPC' then
      update memall set duguje=stock*cenabezpp;
    end if;

    insert into tmprobnopren select memall.sifobj, memall.sifra, dt, @mybrnalpst, memall.stock, 0, memall.duguje, 0, null, memall.faktcena, memall.nabcena, memall.cenabezpp, memall.cenasapp, ((cenabezpp/nabcena)-1)*100,
      refdate, concat(dt,refdate), 'POCETNO STANJE', null,0,0,'',@aktivnioperater,memall.mestotr, memall.nosioc, memall.nabcena,null,null,null,null,refdate, memall.brnalpst, 0, refdate,@mybrnalpst, 0  from memall,artikli where memall.sifra=artikli.sifra;

    drop temporary table if exists mem;
    drop temporary table if exists memall;

  end if;

  

  insert into tmprobnopren select so2, robno.sifra,dt, @mybrnalpst, 0, 0, 0, 0, null, tmpzadcene.cena, tmpzadcene.nabcena, tmpzadcene.cenabezpp, tmpzadcene.cenasapp, 0, 0, makedate(novagodina,1), 'POCETNO STANJE', null, 0, 0, '', @aktivnioperater, null, null, 0, null, null, null, null, null, null, 0, makedate(novagodina,1), @mybrnalpst,0 
     from robno, tmpzadcene, artikli where robno.sifra=tmpzadcene.sifra and robno.sifobj=so and robno.sifra=artikli.sifra and artikli.jeusluga=1 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") and concat(datum,ddatum)=tmpzadcene.condatddat group by robno.sifra;

  if jefifo=0 then
    update tmprobnopren set ddatum=makedate(novagodina,1), condatddat=concat(datum,ddatum), prernc=nabcena;
  else
    update tmprobnopren set condatddat=concat(datum,ddatum), prernc=nabcena, ddatum=ddatum;
  end if;
  alter table tmprobnopren drop dugpot;

  SET @qvr=concat("delete from ",novabaza,".serbr where (brnal='PST0' or brnal='PST000') and sifobj=",so2);
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;    

  SET @qvr=concat("delete from ",novabaza,".robno where (brnal='PST0' or brnal='PST000') and sifobj=",so2);
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;

  SET @qvr=concat("INSERT INTO ",novabaza,".robno select * from tmprobnopren");
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;

  
  SET @qvr=concat("INSERT ignore INTO ",novabaza,".artikli select * from artikli");
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;

  SET @qvr=concat("insert into ",novabaza,".serbr select ",so2,",serbr.sifra,serbr.serbr,sum(ulaz-izlaz) as stanje,0, 'PST000', 0, '",dt,"','",dt,"','POCETNO STANJE', rok,now(),@aktivnioperater,0 from serbr, artikli where serbr.sifra=artikli.sifra and artikli.serbr>0 and serbr.sifobj=",so, " and serbr.stornirano=0 group by serbr.sifobj,serbr.sifra,serbr.serbr  having stanje<>0");
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;    

 
  drop temporary table if exists tmprobnopren;
end
```

---

## 51. NalogPrerNc

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `NalogPrerNc`(nbrnalrc int(3), ndatumrc date, param10018 int(1))
begin
  set @brnalrc=nbrnalrc;
  delete from my_prerncnalog where brnalrc=@brnalrc;

  insert into my_prerncnalog select @brnalrc, ndatumrc, robno.sifobj, robno.sifra, robno.brnal, rbr, datum, objekti.sifobj, ulaz, izlaz, nabcena, prernc, (ulaz*prernc)-(ulaz*nabcena), (izlaz*prernc)-(izlaz*nabcena), (abs(ulaz-izlaz)*prernc)-(abs(ulaz-izlaz)*nabcena), 0, null, null, null, null, mestotr, nosioc, cenabezpp, cenasapp, GetOsnovniBrnal(robno.brnal), robno.subject
    from robno,objekti where robno.sifobj=objekti.sifra and not objekti.sifobj = 3  and stornirano=0  and not (robno.brnal like "POTVRDJENO%") and (objekti.sifobj=1 or objekti.sifobj=2 or objekti.sifobj=3 or objekti.sifobj=8 or objekti.sifobj=10 or objekti.sifobj=12  or objekti.sifobj=18) and (ulaz<>0 or izlaz<>0) and brnal not like 'NC%' and prernc<>nabcena
      and (round(((ulaz*prernc)-(ulaz*nabcena)),2)<>0 or round(((izlaz*prernc)-(izlaz*nabcena)),2)<>0);

  
  update my_prerncnalog set finrazlika=finrazlika*-1 where (izlaz=0 and ulaz<0) or (ulaz=0 and izlaz<0);

  
  insert into my_prerncnalog select @brnalrc, ndatumrc, robno.sifobj, robno.sifra, robno.brnal, rbr, datum, objekti.sifobj, ulaz, izlaz, nabcena, prernc, (potrazuje-duguje), 0, (potrazuje-duguje), 0, null, null, null, null, mestotr, nosioc, cenabezpp, cenasapp, GetOsnovniBrnal(robno.brnal), robno.subject
    from robno,objekti where robno.sifobj=objekti.sifra and not objekti.sifobj=3 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") and (objekti.sifobj=3 or objekti.sifobj=8 or objekti.sifobj=10 or objekti.sifobj=12) and brnal like 'NC%' and round(duguje-potrazuje,2)<>0;

  
  drop temporary table if exists tmp_fin_nalozi;
  create temporary table tmp_fin_nalozi (brnal varchar(50) not null primary key) engine=myisam;
  insert into tmp_fin_nalozi select brnal from finprom group by brnal;
  update my_prerncnalog left join tmp_fin_nalozi on my_prerncnalog.brnal=tmp_fin_nalozi.brnal set ufinansijsko=1 where not isnull(tmp_fin_nalozi.brnal);

  
  select tabrac.konto into @mykonto from tabrac where tabrac.sifra='BSRN0019' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog set my_prerncnalog.kontrastav=@mykonto where tipobj=1 and (brnal like 'IR%') and isnull(kontrastav);

  
  select tabrac.konto into @mykonto from tabrac where tabrac.sifra='BSRN0012' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog set my_prerncnalog.kontrastav=@mykonto where tipobj=2 and (brnal like 'IR%') and isnull(kontrastav);

  update my_prerncnalog set my_prerncnalog.finrazlika=my_prerncnalog.finrazlika*-1 where (brnal like 'IR%') and sifobj<>mid(brnal,3,3);

  
  update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))) where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', 'BSRN0193')))
    and (tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12) and (brnal like 'IR%') and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;

  if (param10018=1) then
    update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=tabrac.konto where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=1,'BSRN0019','BSRN0012')
    and my_prerncnalog.sifobj in (select sifra from tmp_objs) and (brnal like 'IR%') and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;
  end if;

  
  select tabrac.konto into @mykonto0 from tabrac where tabrac.sifra='BSRN0002' and tabrac.sifrakpl=@kontniplan;
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0124' and tabrac.sifrakpl=@kontniplan;
  select tabrac.konto into @mykonto3 from tabrac where tabrac.sifra='BSRN0125' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog,tabrac,intracun,artikli set finrazlika=finrazlika*-1,my_prerncnalog.konto=if(isnull(intracun.fid3) or trim(intracun.fid3)='',tabrac.konto, intracun.fid3), my_prerncnalog.kontrastav=if(not(artikli.konto='' or isnull(artikli.konto)), artikli.konto ,concat(@mykonto0,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))), my_prerncnalog.konto2=@mykonto2, kontrastav2=@mykonto3
   where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=intracun.biznisoftbrnal and my_prerncnalog.sifra=intracun.sifra and tabrac.sifra='BSRN0080'
    and intracun.tipobj2=18 and my_prerncnalog.tipobj=10 and izlaz<>0 and (brnal like 'IR%') and tabrac.sifrakpl=@kontniplan;

  
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0078' and tabrac.sifrakpl=@kontniplan;
  select tabrac.konto into @mykonto3 from tabrac where tabrac.sifra='BSRN0101' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog,tabrac,tblsopsttros,artikli set my_prerncnalog.konto=tblsopsttros.racuntroska, my_prerncnalog.kontrastav=if((tipobj=8 or tipobj=10),if(not (artikli.konto='' or isnull(artikli.konto)),artikli.konto,concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))) ,concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))), konto2=@mykonto2, kontrastav2=concat(@mykonto3,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblsopsttros.biznisoftbrnal and my_prerncnalog.sifra=tblsopsttros.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', 'BSRN0193')))
    and (tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12) and brnal like 'RT%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;

  if (param10018=1) then
    update my_prerncnalog,tabrac,tblsopsttros,artikli set my_prerncnalog.konto=tblsopsttros.racuntroska, my_prerncnalog.kontrastav=if((tipobj=8 or tipobj=10),if(not (artikli.konto='' or isnull(artikli.konto)),artikli.konto,tabrac.konto) ,tabrac.konto), konto2=@mykonto2, kontrastav2=concat(@mykonto3,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblsopsttros.biznisoftbrnal and my_prerncnalog.sifra=tblsopsttros.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=1,'BSRN0019','BSRN0012')
    and my_prerncnalog.sifobj in (select sifra from tmp_objs) and brnal like 'RT%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;
  end if;

  
  update my_prerncnalog,tabrac,tblotpisz,artikli set my_prerncnalog.konto=tblotpisz.racuntroska, my_prerncnalog.kontrastav=tblotpisz.konto
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblotpisz.biznisoftbrnal and my_prerncnalog.sifra=tblotpisz.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', 'BSRN0193')))
    and (tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12) and brnal like 'OZ%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;

  if (param10018=1) then
    update my_prerncnalog,tabrac,tblotpisz,artikli set my_prerncnalog.konto=tblotpisz.racuntroska, my_prerncnalog.kontrastav=tblotpisz.konto
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblotpisz.biznisoftbrnal and my_prerncnalog.sifra=tblotpisz.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=1,'BSRN0019','BSRN0012')
    and my_prerncnalog.sifobj in (select sifra from tmp_objs) and brnal like 'OZ%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;
  end if;

  
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0078' and tabrac.sifrakpl=@kontniplan;
  select tabrac.konto into @mykonto3 from tabrac where tabrac.sifra='BSRN0101' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog,tabrac,tblotpisnz,artikli set my_prerncnalog.konto=tblotpisnz.racuntroska, my_prerncnalog.kontrastav=tblotpisnz.konto, konto2=@mykonto2, kontrastav2=concat(@mykonto3,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblotpisnz.biznisoftbrnal and my_prerncnalog.sifra=tblotpisnz.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', 'BSRN0193')))
    and (tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12) and brnal like 'ON%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;

  if (param10018=1) then
    update my_prerncnalog,tabrac,tblotpisnz,artikli set my_prerncnalog.konto=tblotpisnz.racuntroska, my_prerncnalog.kontrastav=tblotpisnz.konto, konto2=@mykonto2, kontrastav2=concat(@mykonto3,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))
    where my_prerncnalog.sifra=artikli.sifra and my_prerncnalog.biznisoftbrnal=tblotpisnz.biznisoftbrnal and my_prerncnalog.sifra=tblotpisnz.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=1,'BSRN0019','BSRN0012')
    and my_prerncnalog.sifobj in (select sifra from tmp_objs) and brnal like 'ON%' and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan;
  end if;

  
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0138' and tabrac.sifrakpl=@kontniplan; 
  select tabrac.konto into @mykonto4 from tabrac where tabrac.sifra='BSRN0140' and tabrac.sifrakpl=@kontniplan; 
  select tabrac.konto into @mykonto5 from tabrac where tabrac.sifra='BSRN0141' and tabrac.sifrakpl=@kontniplan; 
  update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=concat(if(artikli.jesirovina=1, @mykonto5,if(artikli.jeproizvod=1,@mykonto4,@mykonto2)), if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))), 
  my_prerncnalog.kontrastav=if((tipobj=8 or tipobj=10),if(not(artikli.konto=0 or isnull(artikli.konto)),artikli.konto, if(not (tipobj=1 or tipobj=2),concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))),tabrac.konto)),if(not (tipobj=1 or tipobj=2),concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))),tabrac.konto))
    where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', if(my_prerncnalog.tipobj=1,'BSRN0019',if(my_prerncnalog.tipobj=2,'BSRN0012','BSRN0193')))))
    and (tipobj=1 or tipobj=2 or tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12)  and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan and my_prerncnalog.brnal like ('II%');

  
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0138' and tabrac.sifrakpl=@kontniplan; 
  select tabrac.konto into @mykonto4 from tabrac where tabrac.sifra='BSRN0140' and tabrac.sifrakpl=@kontniplan; 
  select tabrac.konto into @mykonto5 from tabrac where tabrac.sifra='BSRN0141' and tabrac.sifrakpl=@kontniplan; 
  update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=if((tipobj=8 or tipobj=10),if(not(artikli.konto=0 or isnull(artikli.konto)),artikli.konto, if(not (tipobj=1 or tipobj=2),concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))),tabrac.konto)),if(not (tipobj=1 or tipobj=2),concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))),tabrac.konto)), 
  my_prerncnalog.kontrastav=concat(if(artikli.jesirovina=1, @mykonto5,if(artikli.jeproizvod=1,@mykonto4,@mykonto2)), if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))
    where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', if(my_prerncnalog.tipobj=1,'BSRN0019',if(my_prerncnalog.tipobj=2,'BSRN0012','BSRN0193')))))
    and (tipobj=1 or tipobj=2 or tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12)  and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan and my_prerncnalog.brnal like ('IP%');
  
  
  select tabrac.konto into @mykonto2 from tabrac where tabrac.sifra='BSRN0078' and tabrac.sifrakpl=@kontniplan;
  update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=@mykonto2, my_prerncnalog.kontrastav=if((tipobj=8 or tipobj=10),if(not(artikli.konto=0 or isnull(artikli.konto)),artikli.konto,concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1')))),concat(tabrac.konto,if(artikli.porez='S0','0',if(artikli.porez='S2','2','1'))))
    where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=3,'BSRN0185',if(my_prerncnalog.tipobj=8,'BSRN0009', if(my_prerncnalog.tipobj=10, 'BSRN0002', 'BSRN0193')))
    and (tipobj=3 or tipobj=8 or tipobj=10 or tipobj=12)  and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan and my_prerncnalog.brnal not like ('TF%');

  if (param10018=1) then
    update my_prerncnalog,tabrac,artikli set my_prerncnalog.konto=@mykonto2, my_prerncnalog.kontrastav=if((tipobj=8 or tipobj=10),if(not(artikli.konto=0 or isnull(artikli.konto)),artikli.konto,tabrac.konto),tabrac.konto)
    where my_prerncnalog.sifra=artikli.sifra and tabrac.sifra=if(my_prerncnalog.tipobj=1,'BSRN0019','BSRN0012')
    and my_prerncnalog.sifobj in (select sifra from tmp_objs)  and isnull(my_prerncnalog.konto) and tabrac.sifrakpl=@kontniplan and my_prerncnalog.brnal not like 'TF%';
  end if;
end
```

---

## 52. NalogPrerNcGK

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `NalogPrerNcGK`(nbrnalrc int(3), ndatumrc date, iprihod int(1))
begin
  DECLARE exit_loop boolean;
  declare s_brnal varchar(50);
  declare s_su, s_si double;
  DECLARE promet CURSOR FOR SELECT brnal,sum(izndug) as sd ,sum(iznpot) as sp FROM finprom where brnal like 'RC001-%' group by brnal having sd<>sp;
  declare continue handler for not found set exit_loop = true;

  set @brnalrc=nbrnalrc;

  drop temporary table if exists my_gk_prernc;
  create temporary table my_gk_prernc (brnal varchar(50) not null, datum date, konto varchar(50) not null, analitika varchar(50) not null, mestotr int(6) not null, nosioc  int(6) not null, izndug double(15,2) default 0, iznpot double(15,2) default 0, primary key (brnal, konto, analitika, mestotr, nosioc));
  insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,konto,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, (finrazlika),0 from my_prerncnalog where not isnull(konto) and ufinansijsko=1 and not (brnal like 'II%') on duplicate key update izndug=izndug+(finrazlika);
  insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,konto,subject,mestotr, nosioc, (finrazlika),0 from my_prerncnalog where not isnull(konto) and ufinansijsko=1 and (brnal like 'II%') on duplicate key update izndug=izndug+(finrazlika);
  
   insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, 0, if(isnull(my_prerncnalog.konto),(finrazlika*-1),finrazlika) from my_prerncnalog left join (select * from tabrac where sifrakpl=@kontniplan group by konto) as mytabrac on my_prerncnalog.kontrastav=mytabrac.konto where not isnull(kontrastav) and ufinansijsko=1 and (not (mytabrac.sifra='BSRN0019' or mytabrac.sifra='BSRN0012'  or mytabrac.sifra='BSRN0010') or isnull(mytabrac.sifra)) and not (brnal like 'II%') on duplicate key update iznpot=iznpot+if(isnull(my_prerncnalog.konto),(finrazlika*-1),finrazlika);

   insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, (finrazlika*-1), 0 
   from my_prerncnalog left join (select * from tabrac where sifrakpl=@kontniplan group by konto) as mytabrac on my_prerncnalog.kontrastav=mytabrac.konto
   where not isnull(kontrastav) and ufinansijsko=1 and (not (mytabrac.sifra='BSRN0019' or mytabrac.sifra='BSRN0012') or isnull(mytabrac.sifra)) and (brnal like 'II%')
   on duplicate key update izndug=izndug+(finrazlika*-1);

   insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, if(isnull(my_prerncnalog.konto),finrazlika,(finrazlika*-1)), 0 from my_prerncnalog left join (select * from tabrac where sifrakpl=@kontniplan group by konto) as mytabrac on my_prerncnalog.kontrastav=mytabrac.konto where not isnull(kontrastav) and ufinansijsko=1 and (mytabrac.sifra='BSRN0019' or mytabrac.sifra='BSRN0012' or mytabrac.sifra='BSRN0010') and not (brnal like 'II%') on duplicate key update iznpot=iznpot+if(isnull(my_prerncnalog.konto),(finrazlika*-1),finrazlika);

   insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, 0, finrazlika 
   from my_prerncnalog left join (select * from tabrac where sifrakpl=@kontniplan group by konto) as mytabrac on my_prerncnalog.kontrastav=mytabrac.konto 
   where not isnull(kontrastav) and ufinansijsko=1 and (mytabrac.sifra='BSRN0019' or mytabrac.sifra='BSRN0012') and (brnal like 'II%')
   on duplicate key update iznpot=iznpot+finrazlika;

  
  insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,konto2,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, (finrazlika),0 from my_prerncnalog where not isnull(konto2) and konto2 like '9%' and ufinansijsko=1 on duplicate key update izndug=izndug+(finrazlika);
  insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav2,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, 0, if(isnull(konto2),(finrazlika*-1),finrazlika) from my_prerncnalog where not isnull(kontrastav2) and kontrastav2 like '9%' and ufinansijsko=1 on duplicate key update iznpot=iznpot+if(isnull(my_prerncnalog.konto2),(finrazlika*-1),finrazlika);
  if iprihod=1 then
    insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,konto2,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, (finrazlika),0 from my_prerncnalog where not isnull(konto2) and konto2 not like '9%' and ufinansijsko=1 on duplicate key update izndug=izndug+(finrazlika);
    insert into my_gk_prernc select concat('RC',LPAD(@brnalrc,3,'0'),'-',brnal),datum,kontrastav2,concat('O-',LPAD(sifobj,5,'0')),mestotr, nosioc, 0, if(isnull(konto2),(finrazlika*-1),finrazlika) from my_prerncnalog where not isnull(kontrastav2) and kontrastav2 not like '9%' and ufinansijsko=1 on duplicate key update iznpot=iznpot+if(isnull(my_prerncnalog.konto2),(finrazlika*-1),finrazlika);
  end if;

  update my_gk_prernc set izndug=izndug*-1, iznpot=iznpot*-1 where brnal like concat('RC',LPAD(@brnalrc,3,'0'),'-IR%') or brnal like concat('RC',LPAD(@brnalrc,3,'0'),'-NC%');
  update my_gk_prernc set izndug=iznpot*-1, iznpot=0 where brnal like concat('RC',LPAD(@brnalrc,3,'0'),'-NC%') and iznpot<>0;

  delete from tmp_knj_finprom;
  insert into tmp_knj_finprom select datum,brnal,datum,analitika,konto,null,izndug,iznpot,1,@aktivnioperater,0,'RC',null,if(mestotr=0,null,mestotr),if(nosioc=0,null,nosioc),'Korekcija nabavne cene',null,null,0,0,now(),null,null,null,null,null,null,datum,null,null,0,GetOsnovniBrnal(brnal) from my_gk_prernc;
  update tmp_knj_finprom,kontniplan set tmp_knj_finprom.brdok='' where kontniplan.analitika<>'objekti - RJ' and sifrakpl=@kontniplan and tmp_knj_finprom.racun=kontniplan.racun;
  update tmp_knj_finprom,kontniplan set tmp_knj_finprom.mestotr=null where kontniplan.mestotr=0 and sifrakpl=@kontniplan and tmp_knj_finprom.racun=kontniplan.racun;
  update tmp_knj_finprom,kontniplan set tmp_knj_finprom.nosioc=null where kontniplan.nosioc=0 and sifrakpl=@kontniplan and tmp_knj_finprom.racun=kontniplan.racun;

  call SrediTmpFinProm(0);
  OPEN promet;
  set exit_loop = false;
  promet_loop:
    LOOP FETCH promet INTO s_brnal, s_su, s_si;
    IF exit_loop THEN
        LEAVE promet_loop;
    END IF;
    update finprom set izndug=izndug-s_su+s_si where brnal=s_brnal and rbrst=1;
  END LOOP promet_loop;
  CLOSE promet;
  delete from finprom where brnal like 'RC001-%' and izndug=0 and iznpot=0;
  update finprom set status=2 where brnal like 'RC001-%';
end
```

---

## 53. NalogPrerNCRobno

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `NalogPrerNCRobno`(nbrnalrc int(3), ndatumrc date, iprihod int(1))
begin
  
  insert into tmp_robno select sifobj,sifra,datum,concat('RC001-',brnal),0,0,razlikanculaz,razlikancizlaz,0,nabcena,nabcena,cenabezpp,cenasapp,(1-(cenabezpp/prernc))*100,now(), concat(datum,now()),'Korekcija nabavne cene',
   null,0,0,null,@aktivnioperater,mestotr,nosioc,prernc,null,null,null,null,null,null,0,null,concat('RC001-',brnal) from my_prerncnalog where tipobj<>1 and tipobj<>2;
  call SrediTmpRobno(0);
end
```

---

## 54. obojiavanse

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `obojiavanse`()
BEGIN
  DECLARE exit_loop boolean;
  DECLARE i_godina integer;
  DECLARE s_brnal, s_popdvid varchar(200);
  DECLARE f_ukupno double;
  DECLARE ulavansi CURSOR FOR SELECT ukupno, avansiulrn.godina, avansiulrn.brnal, avansiulrn.popdvid FROM avansiulrn, kupci where avansiulrn.partner=kupci.sifra order by avansiulrn.partner, avansiulrn.datknj;
  DECLARE izavansi CURSOR FOR SELECT ukupno, avansiizrn.godina, avansiizrn.brnal, avansiizrn.popdvid FROM avansiizrn, kupci where avansiizrn.partner=kupci.sifra order by avansiizrn.partner, avansiizrn.datknj;
  declare continue handler for not found set exit_loop = TRUE;

  UPDATE avansiulrn set boja='0', preostalo = 0, ts=ts;
  OPEN ulavansi;
  set exit_loop = false;
  ulavansi_loop:
    LOOP FETCH ulavansi INTO f_ukupno, i_godina,s_brnal, s_popdvid;
    IF exit_loop THEN
      LEAVE ulavansi_loop;
    END IF;
    set @tmp_izn_av := 0;
    SET @aa=CONCAT('select sum(iznav) into @tmp_izn_av from avracunik where godina=',i_godina,' and brnal_avrac=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    IF NOT ISNULL(@tmp_izn_av) then
      IF NOT (f_ukupno>round(@tmp_izn_av,2)) THEN
        SET @aa=CONCAT('UPDATE avansiulrn set boja=''128'', ts=ts, preostalo=0 WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
      else
        SET @aa=CONCAT('UPDATE avansiulrn set preostalo=(ukupno-',@tmp_izn_av,'), ts=ts WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
      END IF;
    else
      SET @aa=CONCAT('UPDATE avansiulrn set preostalo=ukupno, ts=ts WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;
    END IF;

    END LOOP ulavansi_loop;
    CLOSE ulavansi;

  UPDATE avansiizrn set boja='0', preostalo = 0,ts=ts;
  OPEN izavansi;
  set exit_loop = false;
  izavansi_loop:
    LOOP FETCH izavansi INTO f_ukupno, i_godina,s_brnal, s_popdvid;
    IF exit_loop THEN
      LEAVE izavansi_loop;
    END IF;
    set @tmp_izn_av := 0;
    SET @aa=CONCAT('select sum(iznav) into @tmp_izn_av from avracuni where godina=',i_godina,' and avrac=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    IF NOT ISNULL(@tmp_izn_av) then
      IF NOT (f_ukupno>round(@tmp_izn_av,2)) THEN
        SET @aa=CONCAT('UPDATE avansiizrn set boja=''128'', preostalo=0, ts=ts WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
      else
        SET @aa=CONCAT('UPDATE avansiizrn set preostalo=(ukupno-',@tmp_izn_av,'), ts=ts WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
      END IF;
    else
      SET @aa=CONCAT('UPDATE avansiizrn set preostalo=ukupno, ts=ts WHERE godina=',i_godina,' and brnal=''',s_brnal,''' and popdvid=''',s_popdvid,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;
    END IF;

    END LOOP izavansi_loop;
    CLOSE izavansi;

  update avansiizrn set boja='128', preostalo=0,ts=ts where externidokument like 'DOKUMENT STORNIRAN NALOGOM%';
END
```

---

## 55. obracunPotvrdjeno

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `obracunPotvrdjeno`(objekat int(3), brnal varchar(15))
BEGIN
  DECLARE qKolicina varchar(5);  
  DECLARE kolicina varchar(100);
  DECLARE orobj2 varchar(50);
  declare subjstring varchar(100);
  declare sifkom varchar(100);
  DECLARE sifra char(2);
  DECLARE tabela varchar(50);
  DECLARE tipKljuca int(1);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE queryCursor CURSOR FOR SELECT * FROM tmp_oppHelper;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS tmp_oppHelper;
  DROP TEMPORARY TABLE IF EXISTS tmp_insertHelper;
  DROP TEMPORARY TABLE IF EXISTS tmp_azursifre;
  CREATE TEMPORARY TABLE tmp_oppHelper (sifra char(2), tabela varchar(50), tipkljuca int(1));
  CREATE TEMPORARY TABLE tmp_insertHelper (sifobj int(3) not null, sifra int(6) not null, brnal varchar(50) not null, kolicina double(15, 2),
                                           rbr int(6), cena double(15, 2), nabcena double(15, 4),
                                           cenabezpp double(15, 2), cenasapp double(15, 2), brdok varchar(100), datumpotv date not null, subject varchar(20), operater varchar(50), 
                                           komercijalista varchar(50), PRIMARY KEY (brnal, sifobj, sifra));
  CREATE TEMPORARY TABLE tmp_azursifre (sifobj int(3) not null, sifra int(6) not null, primary key (sifobj, sifra));
  SET @rbr = 0;
  SET @q = CONCAT('INSERT INTO tmp_oppHelper SELECT sifra, tabela, tipkljuca FROM ', @bsliveid, 'opp.documents, obracunPotvrdjeno WHERE (tipkljuca=1 or tipkljuca=2 or tipkljuca=3) and ',
                  @bsliveid, 'opp.documents.sifra = obracunpotvrdjeno.vd AND objekat = ', objekat);
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  SET @q = CONCAT('DELETE FROM serbr WHERE brnal like ''POTVRDJENO%'' AND sifobj = ', objekat);
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  OPEN queryCursor;
  read_loop:
    LOOP FETCH queryCursor INTO sifra, tabela, tipKljuca;
    IF done THEN
      LEAVE read_loop;
    END IF;
    set @brnal = '';
    set sifkom = ' null ';
    if tipkljuca=1 then
      set subjstring = concat('concat("P-",lpad(',tabela,'.dobavljac,5,"0"))');
    end if;
    if tipkljuca=2 then
      set subjstring = concat('concat("P-",lpad(',tabela,'.sifkup,5,"0"))');
      set sifkom = ' postkom ';
    end if;
    if tipkljuca=3 then
      set subjstring = concat('concat("O-",lpad(',tabela,'.obj2,5,"0"))');
    end if;
    set @djoka=subjstring;
    IF NOT (brnal = '') THEN SET @brnal = CONCAT(' AND NOT biznisoftbrnal = ''', brnal,''''); END IF;
    SET qKolicina = '';    
    SET orobj2 = '';
    IF tipKljuca = 1 THEN SET qKolicina = '* -1'; END IF;    
    set kolicina = concat(tabela,'.kolicina', qKolicina);
    IF (tipKljuca = 3) and (sifra='IR') THEN
      set kolicina = concat(' if(obj2=',objekat,',',tabela,'.kolicina*-1,',tabela,'.kolicina) ');
      set orobj2= concat(' or obj2=',objekat);
    END IF;
    
    SET @q = CONCAT('INSERT INTO tmp_insertHelper SELECT ', objekat, ',', tabela,'.sifra, concat("POTVRDJENO-",', tabela,'.biznisoftbrnal), ',kolicina,',1,',
    ' if(isnull(trstanje.faktcena),0,trstanje.faktcena), if(isnull(trstanje.nabcena),0,trstanje.nabcena), if(isnull(trstanje.vpcena),0,trstanje.vpcena), if(isnull(trstanje.mpcena),0,trstanje.mpcena), brdok, ', tabela,
                  '.datum, ', subjstring,', operater,',sifkom,' FROM ', tabela,
                  ' left join trstanje on ', tabela, '.sifra = trstanje.sifra AND trstanje.sifobj = ', objekat, ' where potvrdjeno = 1
                  AND status = 1 ', @brnal,' and (', tabela, '.sifobj=', objekat, ' ',orobj2,') AND stornirano = 0 AND LEFT(biznisoftbrnal, 2) = ', QUOTE(sifra),
                  ' ON DUPLICATE KEY UPDATE tmp_insertHelper.kolicina = tmp_insertHelper.kolicina + (',kolicina,')');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    SET @q = CONCAT('INSERT INTO serbr SELECT spec_serbr.sifobj, spec_serbr.sifra, spec_serbr.serbr, spec_serbr.ulaz, spec_serbr.izlaz, concat("POTVRDJENO-",spec_serbr.brnal),
                   spec_serbr.partner, spec_serbr.datnal, spec_serbr.datdok, spec_serbr.brdok, spec_serbr.rok, NULL, spec_serbr.operater, 0
                   FROM spec_serbr, ', tabela, ' WHERE spec_serbr.brnal = biznisoftbrnal AND ', tabela,'.sifra = spec_serbr.sifra AND status = 1
                   AND stornirano = 0 ',@brnal,' and potvrdjeno = 1 AND spec_serbr.sifobj=',objekat,' and LEFT(biznisoftbrnal, 2) = ', QUOTE(sifra));  
    PREPARE stmt FROM @q;
    EXECUTE stmt;
  END LOOP read_loop;
  CLOSE queryCursor;

  SET @q = CONCAT('insert ignore into tmp_azursifre select sifobj, sifra from robno WHERE brnal like ''POTVRDJENO%'' AND sifobj = ', objekat,' group by sifobj, sifra');
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  SET @q = CONCAT('insert ignore into tmp_azursifre select sifobj, sifra from tmp_insertHelper group by sifobj, sifra');
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  
  SET @q = CONCAT('DELETE FROM robno WHERE brnal like ''POTVRDJENO%'' AND sifobj = ', objekat);
  PREPARE stmt FROM @q;
  EXECUTE stmt;
  SET @q = CONCAT('INSERT ignore INTO robno SELECT tmp_insertHelper.sifobj, tmp_insertHelper.sifra, datumpotv, tmp_insertHelper.brnal, 0,
                   kolicina, 0, (CASE WHEN LOWER(', @bsliveid, 'opp.sifobj.sifcene) = ''mpc'' THEN kolicina * cenasapp WHEN
                    LOWER(',@bsliveid,'opp.sifobj.sifcene) = ''vpc'' THEN kolicina * cenabezpp WHEN LOWER(', @bsliveid,'opp.sifobj.sifcene) = ''nbc'' THEN kolicina * nabcena END), rbr, cena, nabcena, cenabezpp, cenasapp, 0,
                   null, CONCAT(DATE(NOW()), NOW()), subject, null, 0, 0, komercijalista, tmp_insertHelper.operater, null, null, nabcena, 0, 0, 0, '''', DATE(NOW()),
                  brdok, 0, DATE(NOW()), tmp_insertHelper.brnal FROM tmp_insertHelper, objekti, ', @bsliveid, 'opp.sifobj WHERE
                   objekti.sifra = tmp_insertHelper.sifobj AND ', @bsliveId, 'opp.sifobj.sifra = objekti.sifobj');
  PREPARE stmt FROM @q;  
  EXECUTE stmt;

  DROP TEMPORARY TABLE if EXISTS tmpll;
  create temporary TABLE tmpll (sifobj INT(3) NOT NULL, sifra INT(6) NOT NULL, stanjell DOUBLE(15,3) DEFAULT 0, PRIMARY KEY (sifobj,sifra));
  INSERT INTO tmpll select robno.sifobj, robno.sifra, sum(ulaz-izlaz) as ssstanje from robno, tmp_azursifre where robno.sifobj=tmp_azursifre.sifobj and robno.sifra=tmp_azursifre.sifra and stornirano=0 group by robno.sifobj, robno.sifra;
  
  insert ignore into trstanje select tmpll.sifobj, tmpll.sifra, artikli.naziv, artikli.jedmere, artikli.porez, artikli.tarbr, now(), 0, 0, 0, 0, 0, 0, 0, artikli.barkod, artikli.kasakoef, artikli.taksa, artikli.akciza, null, null, null, 0 from tmpll, artikli where tmpll.sifra=artikli.sifra;
  
  update trstanje, tmpll set trstanje.stanje=tmpll.stanjell where trstanje.sifobj=tmpll.sifobj and trstanje.sifra=tmpll.sifra;
END
```

---

## 56. obracunRazlikeUCeni

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `obracunRazlikeUCeni`(`period1Od` date, `period1Do` date, `period2Od` date, `period2Do` date)
BEGIN
  DROP TEMPORARY TABLE IF EXISTS tmp_obracunRazlikeUCeni;
  CREATE TEMPORARY TABLE tmp_obracunRazlikeUCeni (sifraObjekta int(3), nazivObjekta varchar(255),
                                                  tipObjekta int(2), racunZaliha varchar(10),
                                                  racunPoreza varchar(10),
                                                  racunRazlikeUCeni varchar(10) DEFAULT 0 NOT NULL,
                                                  ukupnoUkalkulisanaRazlikaUCeni double(15, 2) DEFAULT 0 NOT NULL,
                                                  ukupnoZaduzenje double(15, 2) DEFAULT 0 NOT NULL,
                                                  ukupnoUkalkulisanPorez double(15, 2) DEFAULT 0 NOT NULL,
                                                  ukupnoRealizacija double(15, 2) DEFAULT 0 NOT NULL,
                                                  ukupnoObracunatiPorez double(15, 2) DEFAULT 0 NOT NULL,
                                                  ukupnoZaduzenjeBezPoreza double(15, 2) DEFAULT 0 NOT NULL,
                                                  stopa double(15, 6) DEFAULT 0 NOT NULL,
                                                  realizacijaBezPoreza double(15, 2) DEFAULT 0 NOT NULL,
                                                  ostvarenaRazlikaUCeni double(15, 2) DEFAULT 0 NOT NULL);
  INSERT INTO tmp_obracunRazlikeUCeni
  SELECT sifra, naziv, sifobj, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0
  FROM objekti WHERE
  sifobj IN (1, 2, 4, 5);

  UPDATE
    tmp_obracunRazlikeUCeni
  SET
    racunZaliha = CASE tipObjekta
      WHEN 1 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('17', 4, '0')))
      WHEN 2 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('11', 4, '0')))
      WHEN 4 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('13', 4, '0')))
      WHEN 5 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('14', 4, '0')))
      ELSE ''
   END,
    racunPoreza = CASE tipObjekta
      WHEN 1 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('18', 4, '0')))
      WHEN 4 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('15', 4, '0')))
      ELSE ''
   END,
    racunRazlikeUCeni = CASE tipObjekta
      WHEN 1 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('19', 4, '0')))
      WHEN 2 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('12', 4, '0')))
      WHEN 4 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('16', 4, '0')))
      WHEN 5 THEN (SELECT konto FROM tabrac WHERE sifrakpl = @kontniplan AND sifra = CONCAT('BSRN', LPAD('16', 4, '0')))
      ELSE ''
   END,
     
    ukupnoUkalkulisanaRazlikaUCeni = (SELECT SUM(iznpot) FROM finprom WHERE status = 9 AND datnal >= period1Od AND datnal <= period1Do
                                      AND LEFT(finprom.racun, 4) = LEFT(racunRazlikeUCeni, 4) AND brdok = CONCAT('O-', LPAD(sifraObjekta, 5, '0')) and stornirano=0),
    ukupnoZaduzenje = (SELECT SUM(izndug) FROM finprom WHERE status = 9 AND datnal >= period1Od AND datnal <= period1Do
                       AND (finprom.racun = concat(racunZaliha, '0') or finprom.racun = concat(racunZaliha, '1') or finprom.racun = concat(racunZaliha, '2')) AND brdok = CONCAT('O-', LPAD(sifraObjekta, 5, '0')) and stornirano=0),
    ukupnoUkalkulisanPorez = (SELECT SUM(iznpot) FROM finprom WHERE status = 9 AND datnal >= period1Od AND datnal <= period1Do
                              AND LEFT(finprom.racun, 4) = LEFT(racunPoreza, 4) AND brdok = CONCAT('O-', LPAD(sifraObjekta, 5, '0')) and stornirano=0),
    ukupnoRealizacija = (SELECT SUM(iznpot) FROM finprom WHERE status = 9 AND datnal >= period2Od AND datnal <= period2Do
                         AND (finprom.racun = concat(racunZaliha, '0') or finprom.racun = concat(racunZaliha, '1') or finprom.racun = concat(racunZaliha, '2')) AND brdok = CONCAT('O-', LPAD(sifraObjekta, 5, '0')) and stornirano=0),
    ukupnoObracunatiPorez = (SELECT SUM(izndug) FROM finprom WHERE status = 9 AND datnal >= period2Od AND datnal <= period2Do
                             AND LEFT(finprom.racun, 4) = LEFT(racunPoreza, 4) AND brdok = CONCAT('O-', LPAD(sifraObjekta, 5, '0')) and stornirano=0),

    ukupnoZaduzenjeBezPoreza = ukupnoZaduzenje - ukupnoUkalkulisanPorez,
    stopa = (ukupnoUkalkulisanaRazlikaUCeni / ukupnoZaduzenjeBezPoreza)*100,
    realizacijaBezPoreza = ukupnoRealizacija - ukupnoObracunatiPorez,
    ostvarenaRazlikaUCeni = stopa * realizacijaBezPoreza / 100;

    delete from tmp_obracunRazlikeUCeni where realizacijaBezPoreza=0;
END
```

---

## 57. OtvaranjeNoveGodine

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `OtvaranjeNoveGodine`(`nazivBaze` varchar(20))
BEGIN
  DECLARE tables varchar(50);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE queryCursor CURSOR FOR SELECT * FROM tmp_Table;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS tmp_table;
  SET @tmpTable = 'CREATE TEMPORARY TABLE tmp_Table
                   AS SELECT table_name FROM information_schema.tables
                   AS tables WHERE table_schema = database() AND NOT table_type = ''VIEW'';';
  PREPARE stmt FROM @tmpTable;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
  OPEN queryCursor;

  SET @ins = CONCAT('CREATE DATABASE IF NOT EXISTS ', nazivBaze);
  PREPARE stmt FROM @ins;
  EXECUTE stmt; 
  SET done = FALSE;

  read_loop:
  LOOP FETCH queryCursor INTO tables;
    SET @ins = CONCAT('CREATE TABLE IF NOT EXISTS ', nazivBaze, '.', tables, ' LIKE ', tables);
    
  IF done THEN
    LEAVE read_loop;
  END IF; 
  PREPARE stmt FROM @ins;
  EXECUTE stmt;
  END LOOP read_loop;
  CLOSE queryCursor; 

  SET @ins = CONCAT('ALTER TABLE ', nazivBaze, '.kasa CONVERT TO CHARACTER SET UTF8');
  PREPARE stmt FROM @ins;
  EXECUTE stmt;
  SET @ins = CONCAT('ALTER TABLE ', nazivBaze, '.robno CONVERT TO CHARACTER SET UTF8');
  PREPARE stmt FROM @ins;
  EXECUTE stmt;  
END
```

---

## 58. oznakasef

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `oznakasef`(sifrafirme varchar(100), godina integer)
BEGIN
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  
  drop temporary table if exists oznakadokumentagodine;
  create temporary table oznakadokumentagodine like oznakadokumenta;
  insert into oznakadokumentagodine select * from oznakadokumenta where brnal like concat('%-',lpad(sifrafirme,4,'0'),'-',godina,'-%');

  IF imaproslagodina THEN
    SET @aa=CONCAT('insert ignore into oznakadokumentagodine select * from ',proslagodina,'.oznakadokumenta where brnal like concat("%-",lpad(',sifrafirme,',4,"0"),"-",',godina-1,',"-%")');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  end IF; 
END
```

---

## 59. prenesiSveArtikle

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `prenesiSveArtikle`(objekat varchar(3), IgnMTNT boolean, obrCen int(6), tipWNabCene int(2),
                                   datum date, vrstaCene varchar(3), uDruguFirmu boolean,
                                   novaGodina int(4), periodDo date, prenosStanjaICena boolean, novaBaza varchar(20))
BEGIN
  DECLARE sifra int(6);
  DECLARE done boolean DEFAULT FALSE;
  DECLARE helpDone boolean DEFAULT FALSE;
  DECLARE imaStanje boolean;
  DECLARE myStanje double (20, 3);
  DECLARE suma double;
  DECLARE origStanje double;
  DECLARE mestotr int(6);
  DECLARE nosioc int(6);
  DECLARE serialNo int(6);
  DECLARE wNabCena double(15, 2);
  DECLARE wMyCena double(15, 2);
  DECLARE wMestotr varchar(30);
  DECLARE wNosioc varchar(30);
  DECLARE myDatum varchar(15);
  DECLARE sifobj int(3);
  DECLARE sifra1 int(6);
  DECLARE serbr varchar(100);
  DECLARE stanje double(21, 4);
  DECLARE sifraCursor CURSOR FOR SELECT * FROM sifraTable;
  DECLARE resultCursor CURSOR FOR SELECT * FROM resultTable;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  DROP TEMPORARY TABLE IF EXISTS sifraTable;
  DROP TEMPORARY TABLE IF EXISTS resultTable;
  CREATE TEMPORARY TABLE sifraTable (sifra int(6));
  CREATE TEMPORARY TABLE resultTable (myStanje double(20, 3), suma double(15,2), origStanje double(15,2), mestotr int(6) DEFAULT NULL, nosioc int(6) DEFAULT NULL);
  SET @countStatement = CONCAT('SELECT COUNT(*) FROM (SELECT DISTINCT artikli.sifra FROM artikli, robno 
                                WHERE artikli.sifra = robno.sifra AND robno.sifobj = ', QUOTE(objekat), ' AND jeusluga = 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%")) AS count INTO @count');
  PREPARE stmt FROM @countStatement;
  EXECUTE stmt;
  
  IF (@count > 0) THEN
  SET @selectStatement = CONCAT('INSERT INTO sifraTable SELECT DISTINCT artikli.sifra FROM artikli, robno 
                                WHERE artikli.sifra = robno.sifra AND robno.sifobj = ', QUOTE(objekat), ' AND jeusluga = 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%")');
  PREPARE stmt FROM @selectStatement;
  EXECUTE stmt;
  OPEN sifraCursor;
  SET serialNo = 0;
  read_loop : LOOP                                             
  FETCH sifraCursor INTO sifra;
  IF done THEN
    LEAVE read_loop;
  END IF;
  SET serialNo = serialNo + 1;
    SET @countStatement = CONCAT('SELECT COUNT(*) FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                 ' AND izlaz = 0 AND ulaz >= 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1 INTO @count');                                 
    PREPARE stmt FROM @countStatement;
    EXECUTE stmt;
  IF (@count > 0) THEN
    SET @varStatement = CONCAT('SELECT cena, nabcena, cenabezpp, cenasapp, prernc, prcruc
                                INTO @cena, @nabCena, @cenaBezPP, @cenaSaPP, @prernc, @prcruc
                                FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                ' AND izlaz = 0 AND ulaz >= 0 and stornirano=0 and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1');
    PREPARE stmt FROM @varStatement;
    EXECUTE stmt;
  ELSE
    SET @varStatement = CONCAT('SELECT cena, nabcena, cenabezpp, cenasapp, prernc, prcruc
                                INTO @cena, @nabCena, @cenaBezPP, @cenaSaPP, @prernc, @prcruc
                                FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                ' and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1');
    PREPARE stmt FROM @varStatement;
    EXECUTE stmt;  
  END IF;
  delete from resultTable;
  SET imaStanje = false;
  IF IgnMTNT THEN
    SET @insertStatement = CONCAT('INSERT INTO resultTable SELECT ROUND(SUM(ulaz - izlaz), 3), SUM(duguje - potrazuje), SUM(ulaz - izlaz), NULL, NULL FROM 
                                   robno WHERE sifobj = ', QUOTE(objekat), ' and stornirano=0 and not (robno.brnal like "POTVRDJENO%") AND sifra = ', QUOTE(sifra));
    PREPARE stmt FROM @insertStatement;
    EXECUTE stmt; 
  ELSE
    SET @insertStatement = CONCAT('INSERT INTO resultTable SELECT ROUND(SUM(ulaz - izlaz), 3), SUM(duguje - potrazuje), SUM(ulaz - izlaz), mestotr, nosioc FROM  
                                   robno WHERE sifobj = ', QUOTE(objekat), ' and stornirano=0  and not (robno.brnal like "POTVRDJENO%") AND sifra = ', QUOTE(sifra), ' GROUP BY mestotr, nosioc');
    PREPARE stmt FROM @insertStatement;
    EXECUTE stmt;
  END IF;

  OPEN resultCursor;
    FETCH resultCursor INTO myStanje, suma, origStanje, mestotr, nosioc;
      SET @varStatement = CONCAT('SELECT jeproizvod, jeambalaza, jesirovina, IF(ISNULL(planskacena), 0, planskacena)
                                INTO @jeProizvod, @jeAmbalaza, @jeSirovina, @planskaCena FROM artikli WHERE sifra = ', QUOTE(sifra));
      PREPARE stmt FROM @varStatement;
      EXECUTE stmt;
      SET wNabCena = 0;
      IF (@jeAmbalaza = 1) THEN  
        SET wNabCena = @planskaCena;
      END IF; 
      IF (@jeSirovina = 1) AND (obrCen = 3) THEN 
        SET wNabCena = @planskaCena;
      END IF;
      IF (wNabCena = 0) THEN
        IF (tipWNabCene = 1) THEN SET wNabCena = (SELECT avgPrice(0, objekat, sifra, datum, 0)); END IF;
        IF (tipWNabCene = 2) THEN SET wNabCena = @planskaCena; END IF;
        IF (tipWNabCene = 3) THEN SET wNabCena = @nabCena; END IF;
        IF (tipWNabCene = 4) THEN SET wNabCena = @prernc; END IF;
      END IF;
      IF (vrstaCene = 'NBC') THEN SET wMyCena = wNabCena; END IF;
      IF (vrstaCene = 'VPC') THEN SET wMyCena = @cenaBezPP; END IF;
      IF (vrstaCene = 'MPC') THEN SET wMyCena = @cenaSaPP; END IF;
      IF (ISNULL(mestotr)) THEN SET wMestotr = 'NULL'; ELSE SET wMestotr = QUOTE(mestotr); END IF;
      IF (ISNULL(nosioc)) THEN SET wNosioc = 'NULL'; ELSE SET wNosioc = QUOTE(nosioc); END IF;
      SET myDatum = CONCAT(novaGodina, '-01-01');
      IF uDruguFirmu THEN SET myDatum = periodDo; END IF;
      IF prenosStanjaICena THEN
        IF NOT (myStanje < 0) THEN SET imaStanje = TRUE; END IF;
          SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza,'.robno SET sifobj = ', QUOTE(objekat), ', sifra = ', QUOTE(sifra), ', datum = ', QUOTE(myDatum),
                                        ', brnal = ''PST000'', ulaz = ', QUOTE(myStanje), ', izlaz = 0, duguje = ', QUOTE(myStanje), '*', QUOTE(wMyCena), ', mestotr = ',
                                        wMestotr, ', nosioc = ', wNosioc, ', potrazuje = 0, rbr = ', QUOTE(serialNo), ', cena = ', QUOTE(@Cena), ', nabcena = ',
                                        QUOTE(wNabCena), ', cenabezpp = ', QUOTE(@cenaBezPP), ', cenasapp = ', QUOTE(@cenaSaPP), ', prcruc = ', QUOTE(@prcruc),
                                        ', ddatum = ''', novaGodina, '-01-01'', subject = ''POCETNO STANJE'', condatddat = CONCAT(datum, ddatum)');
          PREPARE stmt FROM @insertStatement;
          EXECUTE stmt;
        IF (vrstaCene = 'NBC') THEN
          IF (NOT myStanje = origStanje) THEN 
            SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.robno SET sifobj = ', QUOTE(objekat), ', sifra = ', QUOTE(sifra), ', datum = ', QUOTE(myDatum),
                                          ', brnal = ''PST000'', ulaz = ', QUOTE(myStanje), ', izlaz = 0, duguje = ', QUOTE(suma), ', mestotr = ', wMestotr,
                                          ', nosioc = ', wNosioc, ', potrazuje = 0, rbr = ', QUOTE(serialNo), ', cena = ', QUOTE(@Cena), ', nabcena = ',
                                           QUOTE(WnabCena), ', prernc = ', QUOTE(wNabCena), ', cenabezpp = ', QUOTE(@cenaBezPP), ', cenasapp = ', QUOTE(@cenaSaPP),
                                          ', prcruc = ', QUOTE(@prcruc), ', ddatum = ''', novaGodina, '-01-01'', subject = ''POCETNO STANJE'',
                                          condatddat = CONCAT(datum, ddatum)'); 
            PREPARE stmt FROM @insertStatement; 
            EXECUTE stmt;
          END IF;
      END IF;
    ELSE 
      SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.robno SET sifobj = ', QUOTE(objekat), ', sifra = ', QUOTE(sifra), ', datum = ', QUOTE(myDatum),
                                    ', brnal = ''PST0'', ulaz = 0, izlaz = 0, duguje = 0, mestotr = ', wMestotr, ', nosioc = ', wNosioc, ', potrazuje = 0, 
                                    rbr = ', QUOTE(serialNo), ', cena = ', QUOTE(@Cena), ', nabcena = ', QUOTE(wNabCena), ', prernc = ', QUOTE(wNabCena), 
                                    ', cenabezpp = ', QUOTE(@cenaBezPP), ', cenasapp = ', QUOTE(@cenaSaPP), ', prcruc = ', QUOTE(@prcruc), ', ddatum = ''',
                                    novaGodina, '-01-01'', subject = ''POCETNO STANJE'', condatddat = CONCAT(datum, ddatum)');                                
      PREPARE stmt FROM @insertStatement; 
      EXECUTE stmt;
    END IF;
   CLOSE resultCursor;
  IF NOT imaStanje THEN 
    SET serialNo = serialNo + 1;
    SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.robno SET sifobj = ', QUOTE(objekat), ', sifra = ', QUOTE(sifra), ', datum = ', QUOTE(myDatum),
                                  ', brnal = ''PST0'', ulaz = 0, izlaz = 0, duguje = 0, potrazuje = 0, rbr = ', QUOTE(serialNo), ', cena = ', QUOTE(@Cena),
                                  ', nabcena = ', QUOTE(wNabCena), ', prernc = ', QUOTE(wNabCena), ', cenabezpp = ', QUOTE(@cenaBezPP), ', cenasapp = ',
                                  QUOTE(@cenaSaPP), ', prcruc = ', QUOTE(@prcruc), ', ddatum = ''', novaGodina, '-01-01'',
                                  subject = ''POCETNO STANJE'', condatddat = CONCAT(datum, ddatum)'); 
    PREPARE stmt FROM @insertStatement; 
    EXECUTE stmt;
  END IF;
 END LOOP read_loop;
 CLOSE sifraCursor;
 END IF;

  DELETE FROM sifraTable;
  SET done = FALSE;
  SET serialNo = 0;
  SET @countStatement = CONCAT('SELECT COUNT(*) FROM (SELECT DISTINCT artikli.sifra FROM artikli, robno 
                                WHERE artikli.sifra = robno.sifra AND robno.sifobj = ', QUOTE(objekat), ' AND jeusluga = 1 and stornirano=0  and not (robno.brnal like "POTVRDJENO%")) AS count INTO @count');
  PREPARE stmt FROM @countStatement;
  EXECUTE stmt;
  IF (@count > 0) THEN
    SET @selectStatement = CONCAT('INSERT INTO sifraTable SELECT DISTINCT artikli.sifra FROM artikli, robno 
                                  WHERE artikli.sifra = robno.sifra AND robno.sifobj = ', QUOTE(objekat), ' AND jeusluga = 1 and stornirano=0  and not (robno.brnal like "POTVRDJENO%")');
    PREPARE stmt FROM @selectStatement;
    EXECUTE stmt;
    
    OPEN sifraCursor;
    read_loop : LOOP
    FETCH sifraCursor INTO sifra;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET serialNo = serialNo + 1;
    
      SET @countStatement = CONCAT('SELECT COUNT(*) FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                   ' AND izlaz = 0 AND ulaz >= 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1 INTO @count');                                 
      PREPARE stmt FROM @countStatement;
      EXECUTE stmt;
      IF (@count > 0) THEN
        SET @varStatement = CONCAT('SELECT cena, nabcena, cenabezpp, cenasapp, prernc, prcruc
                                    INTO @cena, @nabCena, @cenaBezPP, @cenaSaPP, @prernc, @prcruc
                                    FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                    ' AND izlaz = 0 AND ulaz >= 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1');
        PREPARE stmt FROM @varStatement;
        EXECUTE stmt;
      ELSE
        SET @varStatement = CONCAT('SELECT cena, nabcena, cenabezpp, cenasapp, prernc, prcruc
                                    INTO @cena, @nabCena, @cenaBezPP, @cenaSaPP, @prernc, @prcruc
                                    FROM robno WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra),
                                    ' and stornirano=0 and not (robno.brnal like "POTVRDJENO%") ORDER BY CONCAT(datum, ddatum, rbr) DESC LIMIT 1');
        PREPARE stmt FROM @varStatement;
        EXECUTE stmt;  
      END IF;
      SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.robno SET sifobj = ', objekat, ', sifra = ', sifra,
                                    ', datum = ''', novagodina, '-01-01'', brnal = ''PST0'', ulaz = 0, izlaz = 0, duguje = 0, 
                                    potrazuje = 0, rbr = ', serialNo, ', cena = ', QUOTE(@cena), ', nabcena = ', QUOTE(@nabCena),
                                    ', prernc = ', QUOTE(@prernc), ', cenabezpp = ', QUOTE(@cenaBezPP), ', cenasapp = ', QUOTE(@cenaSaPP),
                                    ', prcruc = ', QUOTE(@prcruc), ', ddatum = ''', novaGodina, '-01-01'', subject = ''POCETNO STANJE'', 
                                    condatddat = CONCAT(datum, ddatum)');
      PREPARE stmt FROM @insertStatement; 
      EXECUTE stmt;
    END LOOP read_loop;
    CLOSE sifraCursor;
  END IF;
  
  SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.artikli SELECT * FROM artikli');
  PREPARE stmt FROM @insertStatement;
  EXECUTE stmt;

  DELETE FROM sifraTable;
  SET done = FALSE;
  SET serialNo = 0;
  SET @selectStatement = CONCAT('INSERT INTO sifraTable SELECT sifra FROM artikli WHERE serbr > 0');
  PREPARE stmt FROM @selectStatement;
  EXECUTE stmt;
  DROP TEMPORARY TABLE IF EXISTS resultTable;
  CREATE TEMPORARY TABLE resultTable (sifobj int(3), sifra int(8), serbr varchar(100), stanje double(21, 4));
  OPEN sifraCursor;
  read_loop : LOOP
  FETCH sifraCursor INTO Sifra;
  IF done THEN
    LEAVE read_loop;
  END IF;

    SET @insertStatement = CONCAT('INSERT INTO resultTable SELECT sifobj, sifra, serbr, SUM(ulaz - izlaz) AS stanje FROM serbr WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ',
                                   QUOTE(sifra), ' GROUP BY sifobj, sifra, serbr HAVING stanje <> 0');
    PREPARE stmt FROM @insertStatement;
    EXECUTE stmt;
    OPEN resultCursor;
      BEGIN
        DECLARE helpDone boolean DEFAULT FALSE;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET helpDone = TRUE;
        helpLoop : LOOP
        FETCH resultCursor INTO sifobj, sifra1, serbr, stanje;
        IF helpDone THEN
          LEAVE helpLoop;
        END IF;
           SET @selectStatement = CONCAT('SELECT rok INTO @myRok FROM serbr WHERE sifobj = ', QUOTE(objekat), ' AND sifra = ', QUOTE(sifra), ' AND serbr = ', QUOTE(serbr),
                                         ' AND NOT (ISNULL(rok) OR rok = 0) LIMIT 1);');

           PREPARE stmt FROM @selectStatement;
           EXECUTE stmt;
           SET @insertStatement = CONCAT('INSERT IGNORE INTO ', novaBaza, '.serbr SET sifobj = ', QUOTE(sifobj), ', sifra = ', QUOTE(sifra1), ', serbr = ', QUOTE(serbr),                                       ', ulaz = ', QUOTE(stanje), ' izlaz = 0, brnal = ''PST000'', partner = 0, datnal = ''', novaGodina, '-01-01'', datdok = ''',
                                         novaGodina, '-01-01'', brdok = ''POCETNO STANJE'', rok = ', QUOTE(@myRok));
           PREPARE stmt FROM @insertStatement;
           EXECUTE stmt;
        END LOOP helpLoop;
      END;
    CLOSE resultCursor;
  END LOOP read_loop;
END
```

---

## 60. PrenosSifarnika

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `PrenosSifarnika`(`nazivBaze` varchar(20), `godina` int(4), `novagodina` int(4))
BEGIN
  DECLARE CONTINUE HANDLER FOR 1146 SET @error = TRUE;
  SET @ins = CONCAT('SELECT COUNT(*) FROM ', nazivBaze, '.aktivnikontniplan INTO @count;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  IF (@count < 1) THEN
    SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.aktivnikontniplan SELECT * FROM aktivnikontniplan');
    PREPARE stmt FROM @ins;
    IF @error = FALSE THEN EXECUTE stmt; END IF;
  END IF;
  SET @ins = CONCAT('SELECT COUNT(*) FROM ', nazivBaze, '.build INTO @count;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  IF (@count < 1) THEN
    SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.build SELECT * FROM build');
    PREPARE stmt FROM @ins;
    IF @error = FALSE THEN EXECUTE stmt; END IF;
  END IF;  
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.poslovnagodina SET godina=',novagodina);
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kontniplan SELECT * FROM kontniplan;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabrac SELECT * FROM tabrac;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifobj SELECT * FROM sifobj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.grupart SELECT * FROM grupart;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tarife SELECT * FROM tarife;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.objekti SELECT * FROM objekti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.amstope SELECT * FROM amstope;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.artikli SELECT * FROM artikli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kupci SELECT * FROM kupci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.fizkupci SELECT * FROM fizkupci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.logo SELECT * FROM logo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.receptura SELECT * FROM receptura;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifplac SELECT * FROM sifplac;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.virmani SELECT * FROM virmani;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.stdfakture SELECT * FROM stdfakture;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ostanal SELECT * FROM ostanal;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.mestatr SELECT * FROM mestatr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.nosioci SELECT * FROM nosioci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.operacije SELECT * FROM operacije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.blgsiftrans SELECT * FROM blgsiftrans;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.blgtranssr SELECT * FROM blgtranssr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabkljuca SELECT * FROM tabkljuca;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.uslovi SELECT * FROM uslovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tereni SELECT * FROM tereni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posljed SELECT * FROM posljed;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.stdfakturedet SELECT * FROM stdfakturedet;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.napomena SELECT * FROM napomena WHERE tipdok = ''A'';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.napomena SELECT * FROM napomena WHERE tipdok = ''O'';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.anlpart SELECT * FROM anlpart;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.atributi SELECT * FROM atributi;');  
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.atributiartikli SELECT * FROM atributiartikli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.cene SELECT * FROM cene;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.cenovnik SELECT * FROM cenovnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kljucevi SELECT * FROM kljucevi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.napomena SELECT * FROM napomena WHERE tipdok = ''X'';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.poljapozelji SELECT * FROM poljapozelji where tiptabele in (0,1,2,3,4,5,6,7,8,9,31,32,35)');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.defpoljapozelji SELECT * FROM defpoljapozelji;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.prcpovracaja SELECT * FROM prcpovracaja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.propsifban SELECT * FROM propsifban;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.stdfakturedet SELECT * FROM stdfakturedet;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabrnavansa SELECT * FROM tabrnavansa;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabrnoperative SELECT * FROM tabrnoperative;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabrnpdv SELECT * FROM tabrnpdv;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.zadnjirep SELECT * FROM zadnjirep;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.brojcanici SELECT * FROM brojcanici;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.opseg SELECT * FROM opseg;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posvalute SELECT * FROM posvalute;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pos_avansi SELECT * FROM pos_avansi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pos_avansi_stavke SELECT * FROM pos_avansi_stavke;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.vezna_artikli_suf SELECT * FROM vezna_artikli_suf;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.spisakbe SELECT * FROM spisakbe;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.fiskalnizapartnera SELECT * FROM fiskalnizapartnera;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tblcennivel1 SELECT * FROM tblcennivel1;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tblcennivel2 SELECT * FROM tblcennivel2;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.vpcenovnici SELECT * FROM vpcenovnici;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.vpcenovnicisifre SELECT * FROM vpcenovnicisifre;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dostava SELECT * FROM dostava;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.obracunpotvrdjeno SELECT * FROM obracunpotvrdjeno;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_duvan_artikli SELECT * FROM dt_duvan_artikli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_duvan_sifarnik SELECT * FROM dt_duvan_sifarnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_izv_kolone SELECT * FROM dt_izv_kolone;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_izv_artikli_chk SELECT * FROM dt_izv_artikli_chk;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_napomene SELECT * FROM dt_napomene;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_srv_operacije SELECT * FROM dt_srv_operacije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_srv_modeli SELECT * FROM dt_srv_modeli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_srv_radnici SELECT * FROM dt_srv_radnici;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_kamstope SELECT * FROM dt_kamstope;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dt_duvan_artikli SELECT * FROM dt_duvan_artikli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ld110 SELECT * FROM ld110;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldugozar SELECT * FROM ldugozar;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldflugozar SELECT * FROM ldflugozar;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldugozaropj1 SELECT * FROM ldugozaropj1;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldfizlica SELECT * FROM ldfizlica;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kporacuni SELECT * FROM kporacuni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pk1racuni SELECT * FROM pk1racuni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.oslokacije SELECT * FROM oslokacije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.akcije SELECT * FROM akcije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.bodcenovnik SELECT * FROM bodcenovnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.defnabcena SELECT * FROM defnabcena;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.klasa SELECT * FROM klasa;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.klista SELECT * FROM klista;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.komercijalisti SELECT * FROM komercijalisti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.minusnisaldo SELECT * FROM minusnisaldo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.operateri SELECT * FROM operateri;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.opseg SELECT * FROM opseg;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.partatributi SELECT * FROM partatributi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.partatributipartneri SELECT * FROM partatributipartneri;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija01 SELECT * FROM posakcija01;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija02 SELECT * FROM posakcija02;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija03 SELECT * FROM posakcija03;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcije SELECT * FROM posakcije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.rokoviplacanja SELECT * FROM rokoviplacanja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifrepokupcima SELECT * FROM sifrepokupcima;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.nevlasprom SELECT * FROM nevlasprom;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dondon SELECT * FROM dondon;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.aktivnosti SELECT * FROM aktivnosti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kontakti SELECT * FROM kontakti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ld220 SELECT * FROM ld220;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldclanovikap SELECT * FROM ldclanovikap;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldradjed SELECT * FROM ldradjed;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.preporucene SELECT * FROM preporucene;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.propmarza SELECT * FROM propmarza;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.recepturamesa SELECT * FROM recepturamesa;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifodeljenja SELECT * FROM sifodeljenja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.intrnruc SELECT * FROM intrnruc;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_dmsid SELECT * FROM puk_dmsid;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_konfigpar SELECT * FROM puk_go_konfigpar;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_obracun SELECT * FROM puk_go_obracun WHERE godina = ', godina, ';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_obracun_det SELECT * FROM puk_go_obracun_det WHERE godina = ', godina, ';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_osnpar SELECT * FROM puk_go_osnpar WHERE godina = ', godina, ';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_resenja SELECT * FROM puk_go_resenja WHERE godina = ', godina, ';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_go_sifkonfigpar SELECT * FROM puk_go_sifkonfigpar;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_kot SELECT * FROM puk_kot;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_obracun_zarada SELECT * FROM puk_obracun_zarada;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_orgjed SELECT * FROM puk_orgjed;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_radnamesta SELECT * FROM puk_radnamesta;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_radnikalendar SELECT * FROM puk_radnikalendar WHERE godina = ', godina, ';');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_sistematizacija SELECT * FROM puk_sistematizacija;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_skolskasprema SELECT * FROM puk_skolskasprema;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_slozenostposla SELECT * FROM puk_slozenostposla;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_stepstrucnespreme SELECT * FROM puk_stepstrucnespreme;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_kot SELECT * FROM puk_vrste_kot;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_tipovi_orgjed SELECT * FROM puk_tipovi_orgjed;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_aneksugoradu SELECT * FROM puk_vrste_aneksugoradu;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_resenjaodsustvo SELECT * FROM puk_vrste_resenjaodsustvo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_resenjaostalo SELECT * FROM puk_vrste_resenjaostalo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_ugoradu SELECT * FROM puk_vrste_ugoradu;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_zabelezbi SELECT * FROM puk_vrste_zabelezbi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_vrste_zahteva SELECT * FROM puk_vrste_zahteva;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni SELECT * FROM puk_zaposleni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_bolesti SELECT * FROM puk_zaposleni_bolesti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_boravdozvola SELECT * FROM puk_zaposleni_boravdozvola;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_clporodice SELECT * FROM puk_zaposleni_clporodice;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_invalidnost SELECT * FROM puk_zaposleni_invalidnost;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_izvodi SELECT * FROM puk_zaposleni_izvodi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_kot_troskovi SELECT * FROM puk_zaposleni_kot_troskovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_kot_ub SELECT * FROM puk_zaposleni_kot_ub;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_kot_vb SELECT * FROM puk_zaposleni_kot_vb;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_kvalifikacije SELECT * FROM puk_zaposleni_kvalifikacije;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_lekarski SELECT * FROM puk_zaposleni_lekarski;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_lk SELECT * FROM puk_zaposleni_lk;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_ogranicenjars SELECT * FROM puk_zaposleni_ogranicenjars;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_pasos SELECT * FROM puk_zaposleni_pasos;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_povredenaradu SELECT * FROM puk_zaposleni_povredenaradu;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_prethodnoradiskustvo SELECT * FROM puk_zaposleni_prethodnoradiskustvo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_raddozvola SELECT * FROM puk_zaposleni_raddozvola;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_radnaknj SELECT * FROM puk_zaposleni_radnaknj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_sistematski SELECT * FROM puk_zaposleni_sistematski;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_skolovanje SELECT * FROM puk_zaposleni_skolovanje;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_stranijezici SELECT * FROM puk_zaposleni_stranijezici;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_ugoradu SELECT * FROM puk_zaposleni_ugoradu;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.puk_zaposleni_zdravknj SELECT * FROM puk_zaposleni_zdravknj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldveznaiz SELECT * FROM ldveznaiz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldkatalogprihoda SELECT * FROM ldkatalogprihoda;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldveznavan SELECT * FROM ldveznavan;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldsifarnikpp SELECT * FROM ldsifarnikpp;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pos_pozadina SELECT * FROM pos_pozadina;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pos_stolovi SELECT * FROM pos_stolovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posscheme SELECT * FROM posscheme;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.brzitasteri SELECT * FROM brzitasteri;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dodaci SELECT * FROM dodaci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dodaciartikli SELECT * FROM dodaciartikli;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kuppobroj SELECT * FROM kuppobroj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.nivozaliha SELECT * FROM nivozaliha;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.serbrrokovi SELECT * FROM serbrrokovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.kontrolnalista SELECT * FROM kontrolnalista;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.atributikonta SELECT * FROM atributikonta;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.atributikontplana SELECT * FROM atributikontplana;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.jp_ld110 SELECT * FROM jp_ld110;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.jp_ld220 SELECT * FROM jp_ld220;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.jp_ld220vezna SELECT * FROM jp_ld220vezna;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.grupecenovnik SELECT * FROM grupecenovnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.grupeobjekticenovnik SELECT * FROM grupeobjekticenovnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifgroblja SELECT * FROM sifgroblja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.grptrebobj SELECT * FROM grptrebobj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.koousluge SELECT * FROM koousluge;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcijabez SELECT * FROM posakcijabez;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija01 SELECT * FROM posakcija01;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija02 SELECT * FROM posakcija02;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija03 SELECT * FROM posakcija03;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.posakcija04 SELECT * FROM posakcija04;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pospracuni SELECT * FROM pospracuni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_izuzeci SELECT * FROM srps_izuzeci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_parametri SELECT * FROM srps_parametri;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_sasusenje SELECT * FROM srps_sasusenje;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_sifarnik SELECT * FROM srps_sifarnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_susenje SELECT * FROM srps_susenje;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_svodjenje SELECT * FROM srps_svodjenje;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_troskovi SELECT * FROM srps_troskovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_uslovi SELECT * FROM srps_uslovi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.standardnenapomene SELECT * FROM standardnenapomene;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_atributihms SELECT * FROM hot_atributihms;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_atributisoba SELECT * FROM hot_atributisoba;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_drzava SELECT * FROM hot_drzava;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_gosti SELECT * FROM hot_gosti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_granprelaz SELECT * FROM hot_granprelaz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_sifsoba SELECT * FROM hot_sifsoba;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_takse SELECT * FROM hot_takse;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_tipsobe SELECT * FROM hot_tipsobe;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vrstedok SELECT * FROM hot_vrstedok;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vrstesoba SELECT * FROM hot_vrstesoba;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vrsteusluga SELECT * FROM hot_vrsteusluga;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.popdv_sifarnik SELECT * FROM popdv_sifarnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldrngknew SELECT * FROM ldrngknew;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.per_ugovori SELECT * FROM per_ugovori WHERE datistek > CONCAT(', QUOTE(godina), ', ''-'', ''12'', ''-'' ,''31'');');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.per_stavke SELECT per_stavke.* FROM
   per_stavke, ', nazivBaze,'.per_ugovori WHERE per_ugovori.sifobj = per_stavke.sifobj AND per_ugovori.brugo = per_stavke.brugo;');
   SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifarnikugovora SELECT * FROM sifarnikugovora;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.specdostave SELECT * FROM specdostave;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.minzalnotif SELECT * FROM minzalnotif;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.mybsliveid SELECT * FROM mybsliveid;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.siffinpopdv SELECT * FROM siffinpopdv;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabracpog SELECT * FROM tabracpog;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tudjarobarn SELECT * FROM tudjarobarn;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.koougovorinew SELECT * FROM koougovorinew;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.barcodespec SELECT * FROM barcodespec;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.refzaposleni SELECT * FROM refzaposleni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.turisticka_ag SELECT * FROM turisticka_ag;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldprglcas1 SELECT * FROM ldprglcas1;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldprglcas2 SELECT * FROM ldprglcas2;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('DROP VIEW IF EXISTS ', nazivBaze, '.artiklibarkod;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.veze SELECT * FROM veze WHERE (brnal LIKE ''PAR-%'')
                    OR (brnal LIKE ''ZAP-%'') OR (brnal LIKE ''ART-%'') OR (brnal LIKE ''RAD-%'') OR (brnal LIKE ''OS-%-%'') OR (brnal like ''______-____-%'')');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.loksifarnik SELECT * FROM loksifarnik;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.srps_objektiizuzeci SELECT * FROM srps_objektiizuzeci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tabracpog SELECT * FROM tabracpog;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifbrnalgk SELECT * FROM sifbrnalgk;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tblpodosp SELECT * FROM tblpodosp;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.objpotpdoc SELECT * FROM objpotpdoc;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_sifoprgz SELECT * FROM hot_sifoprgz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_umanjenjetakse SELECT * FROM hot_umanjenjetakse;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vrsteisprave SELECT * FROM hot_vrsteisprave;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vize SELECT * FROM hot_vize;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_mestoulaska SELECT * FROM hot_mestoulaska;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_vrstausluga SELECT * FROM hot_vrstausluga;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_nacindolaska SELECT * FROM hot_nacindolaska;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.hot_sifoprgz SELECT * FROM hot_sifoprgz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifpdvart SELECT * FROM sifpdvart;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.partwarnings SELECT * FROM partwarnings;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.lokpromet SELECT * FROM lokpromet;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tblpodosp SELECT * FROM tblpodosp;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.katobjekta SELECT * FROM katobjekta;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifkomercakc SELECT * FROM sifkomercakc;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dodatrsub SELECT * FROM dodatrsub;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.bscomments SELECT * FROM bscomments WHERE neprenosiunovugodinu = 0;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldkatalogprihoda SELECT * FROM ldkatalogprihoda;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldveznaiz SELECT * FROM ldveznaiz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldveznavan SELECT * FROM ldveznavan;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldsifarnikpp SELECT * FROM ldsifarnikpp;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ld130 SELECT * FROM ld130;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.speckatbr SELECT * FROM speckatbr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.dogadjaji SELECT * FROM dogadjaji;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.opisspecexttr SELECT * FROM opisspecexttr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tipprethtr SELECT * FROM tipprethtr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.specprethtr SELECT * FROM specprethtr;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.defugopar SELECT * FROM defugopar;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.eeopdvizuzeci SELECT * FROM eeopdvizuzeci;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldspectrn SELECT * FROM ldspectrn;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.fiskallogo SELECT * FROM fiskallogo;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.licapreuz SELECT * FROM licapreuz;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.razlozibrisanja SELECT * FROM razlozibrisanja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.objatributi SELECT * FROM objatributi;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.objatributiobjekti SELECT * FROM objatributiobjekti;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pravilastampe SELECT * FROM pravilastampe;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.artikliprevod SELECT * FROM artikliprevod;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.arh_list SELECT * FROM arh_list;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.arh_veza SELECT * FROM arh_veza;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.arh_active SELECT * FROM arh_active;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;


  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.tblpodospnedosp SELECT * FROM tblpodospnedosp;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.povalutiplacanja SELECT * FROM povalutiplacanja;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.sifgrpobj SELECT * FROM sifgrpobj;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
 
  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.siflinijatereni SELECT * FROM siflinijatereni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.siflinija SELECT * FROM siflinijatereni;');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pricelists select plid, sifkup, stupanasnagu, opis, if(status=2,1,status), vremeizmene, operater from pricelists where year(stupanasnagu)=',novagodina);
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pricelists_detail select * from pricelists_detail where plid in (select plid from ', nazivBaze, '.pricelists)');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.operzaobj select * from operzaobj');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pn_troskovi select * from pn_troskovi');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.pn_dnevnice select * from pn_dnevnice');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.defkontopart select * from defkontopart');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.ldstimulacijamr select * from ldstimulacijamr');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;

  SET @ins = CONCAT('INSERT IGNORE INTO ', nazivBaze, '.adreseartikala select * from adreseartikala');
  SET @error = FALSE;
  PREPARE stmt FROM @ins;  
  IF @error = FALSE THEN EXECUTE stmt; END IF;
END
```

---

## 61. PrepareEEPPDVData

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `PrepareEEPPDVData`(IN p_godina INT, IN p_period INT)
BEGIN
    DROP TEMPORARY TABLE IF EXISTS tmpTable;
    CREATE TEMPORARY TABLE IF NOT EXISTS tmptable (
    
    izvori VARCHAR(255),

    
    Invoice_Base DOUBLE,
    Invoice_Vat DOUBLE,
    FiscalInvoice_Base DOUBLE,
    FiscalInvoice_Vat DOUBLE,
    OtherInvoice_Base DOUBLE,
    OtherInvoice_Vat DOUBLE,
    Total_Base DOUBLE,
    Total_Vat DOUBLE,
    Deduction_Vat DOUBLE,
    OtherReductionDocuments_Base DOUBLE,
    OtherReductionDocuments_Vat DOUBLE,
    OtherDocumentation_Base DOUBLE,
    OtherDocumentation_Vat DOUBLE,

    
    InternalInvoiceForeigner_Base DOUBLE,
    InternalInvoiceForeigner_Vat DOUBLE,
    InternalInvoiceVatPayer_Base DOUBLE,
    InternalInvoiceVatPayer_Vat DOUBLE,
    ReductionOfDeductibleVat_Vat DOUBLE,

    
    PaidVatRate20 DOUBLE,
    PaidDeductibleVatRate20 DOUBLE,
    PaidVatRate10 DOUBLE,
    PaidDeductibleVatRate10 DOUBLE,
    TotalPaidVat DOUBLE,
    TotalPaidDeductibleVat DOUBLE,

    
    TotalVatPaidToFarmer DOUBLE,
    TotalDeductibleVat DOUBLE,

    
    VatDeductionBasedOnInvoice DOUBLE,
    VatDeductionBasedOnEquipmentAndFacilities DOUBLE,
    VatDeductionBasedOnDecisionOfTaxAuthority DOUBLE,
    VatDeductionBasedOnIncreaseOfVatDeductionInLastTaxPeriod DOUBLE,
    VatDeductionBasedOnVatRecord DOUBLE,
    VatDeductionBasedOnDeletionRequestFromVatPayersRegister DOUBLE,
```

---

## 62. PrepareZaSveArtikle

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `PrepareZaSveArtikle`(novaBaza varchar(20), objekat varchar(2))
BEGIN
  UPDATE robno SET cena = 0 WHERE ISNULL(cena);
  UPDATE robno SET nabcena = 0 WHERE ISNULL(nabcena);
  UPDATE robno SET cenabezpp = 0 WHERE ISNULL(cenabezpp);
  UPDATE robno SET cenasapp = 0 WHERE ISNULL(cenasapp);
  UPDATE robno SET prcruc = 0 WHERE ISNULL(prcruc);
  
  SET @deleteStatement = CONCAT('DELETE FROM ', novaBaza, '.robno WHERE (brnal = ''PST000'' OR brnal = ''PST0'') AND sifobj = ', objekat);
  PREPARE stmt FROM @deleteStatement;
  EXECUTE stmt;
  SET @deleteStatement = CONCAT('DELETE FROM ', novaBaza, '.serbr WHERE (brnal = ''PST000'' OR brnal = ''PST0'') AND sifobj = ', objekat);
  PREPARE stmt FROM @deleteStatement;
  EXECUTE stmt;
END
```

---

## 63. PreracunajNC

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `PreracunajNC`(nadatum date)
BEGIN
  DECLARE exit_loop boolean;
  DECLARE s_subject, s_sifobj, s_sifra, s_rbr, s_mysifobj, oldprc, user_cnt, curprg integer;
  DECLARE s_datdok, s_datum date;
  DECLARE s_ddatum timestamp;
  DECLARE s_ulaz, s_izlaz, s_duguje, s_potrazuje, s_nabcena, mynabcena double;
  DECLARE s_brnal, s_condatddat varchar(50);
  DECLARE dokumenti CURSOR FOR SELECT robno.sifobj, robno.sifra, robno.datum, robno.brnal, ulaz, izlaz, duguje, potrazuje, rbr, nabcena, ddatum, objekti.sifobj as mysifobj, condatddat,right(subject,5) as subject, datumdokumenta 
       FROM robno,objekti,artikli,tmp_myartikli WHERE artikli.sifra=tmp_myartikli.sifra and robno.sifra=artikli.sifra AND artikli.jeusluga=0 and robno.stornirano=0 and not (robno.brnal like "POTVRDJENO%") and jeambalaza=0 AND jeproizvod=0 and proizvod9120=0 and komision880=0 and robno.sifobj=objekti.sifra and brnal not like 'UK%' and objekti.sifobj<>3 
       AND NOT (ulaz<>0 AND NOT (brnal like 'IR%' or brnal like 'IP%') AND brnal NOT LIKE 'TF%') AND NOT (ulaz=0 and izlaz=0 AND brnal NOT like 'IR%' AND brnal NOT LIKE 'TF%') AND NOT (izlaz<>0 AND brnal like 'OD%') AND NOT (izlaz<>0 AND brnal like 'NR%') AND robno.datum<=nadatum and stornirano=0
       ORDER BY datum ASC, sifra ASC, if(brnal like 'TF%' and ulaz>0,1,0) desc, if((brnal like 'IR%' AND MID(brnal,3,3)=robno.sifobj),izlaz<>0,ulaz<>0) DESC, CONCAT(datum,ddatum), (brnal like 'IR%' AND MID(brnal,3,3)=robno.sifobj and izlaz<>0) DESC;
  DECLARE CONTINUE HANDLER FOR not FOUND SET exit_loop = TRUE;

  DROP TABLE if EXISTS my_prernc_progress;
  CREATE TABLE my_prernc_progress (datum date NOT NULL, prc int DEFAULT 0);

  DROP TABLE if EXISTS my_prernc_robno;
  CREATE TABLE my_prernc_robno (sifobj int(3) NOT NULL, sifra int(6) NOT NULL, datum date not NULL, brnal varchar(50) NOT NULL, ulaz double, izlaz double, duguje double, potrazuje double, rbr int(4) NOT NULL, nabcena double(15,4), ddatum timestamp, condatddat varchar(50), PRIMARY KEY (brnal, sifobj, sifra, rbr)) engine=myisam;
  ALTER TABLE my_prernc_robno ADD INDEX ind1 (sifobj, datum, sifra);


  DROP TEMPORARY TABLE if EXISTS my_prernc_robno_1;
  CREATE TEMPORARY TABLE my_prernc_robno_1 LIKE my_prernc_robno;


  DROP TEMPORARY TABLE if EXISTS my_prernc_robno_2;
  CREATE TEMPORARY TABLE my_prernc_robno_2 (sifobj int(3) NOT NULL, sifra int(6) NOT NULL, datum date not NULL, brnal varchar(50) NOT NULL, nabcena double(15,4), PRIMARY KEY (brnal, sifobj, sifra));


  INSERT INTO my_prernc_robno SELECT robno.sifobj, robno.sifra, datum, brnal, ulaz, izlaz, duguje, potrazuje, rbr, nabcena, ddatum, condatddat FROM robno,objekti,artikli,tmp_myartikli WHERE artikli.sifra=tmp_myartikli.sifra and robno.sifra=artikli.sifra AND artikli.jeusluga=0 and jeambalaza=0 AND jeproizvod=0 and proizvod9120=0 and komision880=0 and robno.sifobj=objekti.sifra AND robno.datum<=nadatum
     and ulaz<>0 AND NOT (brnal like 'IR%' or brnal like 'IP%') AND brnal NOT LIKE 'TF%' and stornirano=0 and not (robno.brnal like "POTVRDJENO%");
  INSERT INTO my_prernc_robno SELECT robno.sifobj, robno.sifra, datum, brnal, ulaz, izlaz, duguje, potrazuje, rbr, nabcena, ddatum, condatddat FROM robno,objekti,artikli,tmp_myartikli WHERE artikli.sifra=tmp_myartikli.sifra and robno.sifra=artikli.sifra AND artikli.jeusluga=0 and jeambalaza=0 AND jeproizvod=0 and proizvod9120=0 and komision880=0 and robno.sifobj=objekti.sifra AND robno.datum<=nadatum
     and ulaz=0 and izlaz=0 AND NOT (brnal like 'IR%' or brnal like 'IP%') AND brnal NOT LIKE 'TF%' and stornirano=0 and not (robno.brnal like "POTVRDJENO%");
  INSERT into my_prernc_robno SELECT robno.sifobj, robno.sifra, IF(ISNULL(datorigdok),datum,datorigdok), brnal, ulaz, izlaz, duguje, potrazuje, rbr, nabcena, ddatum, condatddat FROM robno,objekti,artikli,tmp_myartikli WHERE artikli.sifra=tmp_myartikli.sifra and robno.sifra=artikli.sifra AND artikli.jeusluga=0 and jeambalaza=0 AND jeproizvod=0 and proizvod9120=0 and komision880=0 and robno.sifobj=objekti.sifra AND robno.datum<=nadatum
     and brnal like 'OD%' and not (izlaz=0 and ulaz=0) and stornirano=0 and not (robno.brnal like "POTVRDJENO%");
  INSERT into my_prernc_robno SELECT robno.sifobj, robno.sifra, IF(ISNULL(datorigdok),datum,datorigdok), brnal, ulaz, izlaz, duguje, potrazuje, rbr, nabcena, ddatum, condatddat FROM robno,objekti,artikli,tmp_myartikli WHERE artikli.sifra=tmp_myartikli.sifra and robno.sifra=artikli.sifra AND artikli.jeusluga=0 and jeambalaza=0 AND jeproizvod=0 and proizvod9120=0 and komision880=0 and robno.sifobj=objekti.sifra AND robno.datum<=nadatum
     and brnal like 'NR%' and not (izlaz=0 and ulaz=0) and stornirano=0 and not (robno.brnal like "POTVRDJENO%");

  INSERT into my_prernc_progress SET datum=nadatum, prc=0;
  SET oldprc := 0;
  SET curprg := 0;

  update robno,tmp_myartikli set robno.prernc=robno.nabcena, robno.ddatum=robno.ddatum, robno.condatddat=robno.condatddat where robno.sifra=tmp_myartikli.sifra and robno.prernc=0  and stornirano=0;

  OPEN dokumenti;
  SELECT FOUND_ROWS() into user_cnt;
  SET exit_loop = FALSE;
  dokumenti_loop:
    loop fetch dokumenti into s_sifobj, s_sifra, s_datum, s_brnal, s_ulaz, s_izlaz, s_duguje, s_potrazuje, s_rbr, s_nabcena, s_ddatum, s_mysifobj, s_condatddat, s_subject, s_datdok;
    IF exit_loop THEN
      LEAVE dokumenti_loop;
    END IF;

    SET oldprc := oldprc + 1;
    IF ROUND((oldprc/user_cnt) * 100) > curprg THEN
        SET curprg := ROUND((oldprc/user_cnt) * 100);
        UPDATE my_prernc_progress set prc=curprg;
    end IF;

    IF (s_brnal NOT LIKE 'IR%') AND (s_brnal NOT LIKE 'TF%') and (s_brnal NOT LIKE 'IP%') THEN
      INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=avgPricePrerNC(IF((s_mysifobj=1 or s_mysifobj=2),'VPC','NBC'),s_sifobj, s_sifra, s_datum, s_izlaz, s_condatddat, s_mysifobj), ddatum=s_ddatum, condatddat=s_condatddat;
    END IF;

    IF (s_brnal LIKE 'IR%') or (s_brnal LIKE 'IP%') then
      IF s_izlaz<>0 THEN
        SET mynabcena := avgPricePrerNC(IF((s_mysifobj=1 or s_mysifobj=2),'VPC','NBC'),s_sifobj, s_sifra, s_datum, s_izlaz, s_condatddat, s_mysifobj);
        INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=mynabcena, ddatum=s_ddatum, condatddat=s_condatddat;
        INSERT INTO my_prernc_robno_1 SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=mynabcena, ddatum=s_ddatum, condatddat=s_condatddat;
      ELSE       
        if (s_brnal like 'IP%') then
          SET mynabcena := avgPricePrerNC(IF((s_mysifobj=1 or s_mysifobj=2),'VPC','NBC'),s_subject, s_sifra, s_datdok, s_izlaz, s_condatddat, s_mysifobj);
          INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=mynabcena, ddatum=s_ddatum, condatddat=s_condatddat;
        else
          INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=GetNovaPrerCena(s_brnal, s_sifra, s_nabcena), ddatum=s_ddatum, condatddat=s_condatddat;
        end if;
      end IF;
    end IF;

    IF (s_brnal LIKE 'TF%') THEN
      if not (@prerncnottf=1) then
        IF NOT PrerNCPostojiTransformacija(s_brnal) THEN
          CALL KnjiziTransformaciju(s_sifobj, s_brnal, s_mysifobj, s_condatddat);
        end IF;
        INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=GetTransformacija(s_sifobj, s_sifra, s_brnal, s_nabcena), ddatum=s_ddatum, condatddat=s_condatddat;
      else  
        INSERT INTO my_prernc_robno SET sifobj=s_sifobj, sifra=s_sifra, datum=s_datum, brnal=s_brnal, ulaz=s_ulaz, izlaz=s_izlaz, duguje=s_duguje, potrazuje=s_potrazuje, rbr=s_rbr, nabcena=s_nabcena, ddatum=s_ddatum, condatddat=s_condatddat;
      end if;
    end IF;
  END LOOP dokumenti_loop;
  CLOSE dokumenti;

  UPDATE robno, my_prernc_robno SET robno.prernc=my_prernc_robno.nabcena, robno.ddatum=robno.ddatum, robno.condatddat=robno.condatddat WHERE robno.sifobj=my_prernc_robno.sifobj and robno.sifra=my_prernc_robno.sifra and robno.brnal=my_prernc_robno.brnal AND robno.rbr=my_prernc_robno.rbr and robno.brnal not like 'RC001-%';

  DROP TEMPORARY TABLE if EXISTS my_prernc_robno_1;
  DROP TEMPORARY TABLE if EXISTS my_prernc_robno_2;
  DROP TABLE if EXISTS my_prernc_robno;
END
```

---

## 64. pripremitabele

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `pripremitabele`()
BEGIN
  DROP TEMPORARY TABLE IF EXISTS tmpobjekti2;
  CREATE TEMPORARY TABLE tmpobjekti2 LIKE objekti;
  INSERT INTO tmpobjekti2 SELECT * FROM objekti;
  DROP TEMPORARY TABLE IF EXISTS pregltrans;
  CREATE TEMPORARY TABLE pregltrans (oznaka varchar(10), naziv varchar(255), sifobj int(3), partner int(5), brnal varchar(50),
                                     iznos double(15,3), status int(2), datum date, sifobj2 int(3), operater varchar(50),
                                     posljed int(4), teren int(4), komercijalista varchar(50), dostava int(2), sortstampe int(4) DEFAULT 0,
                                     kolicina double(15, 2), cena double(15, 2), brdok varchar(50) DEFAULT NULL, knjizenourobnom int(1) DEFAULT 0,
                                     nefakturisano int(1) DEFAULT 0, tip varchar(1) DEFAULT NULL, akcc int(1) DEFAULT 0, defpopdvid varchar(10)
                                     DEFAULT NULL, brkalk int(6) DEFAULT 0, potvrdjeno int(1) default 0, stornirano int(1) default 0,
                                     datprom date, datdok date, datprihv date, dutobuhvaceno date, datpdv date, idefakture int(10), vrdokizvor int(1), tipkljucax int(2));
END
```

---

## 65. ProveraIntegriteta

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `ProveraIntegriteta`(`dan1` date, `dan2` date, rn4790 varchar(20), rn2790 varchar(20), godina integer, pr1 bool, pr2 bool , pr3 bool , pr4 bool , pr5 bool , pr6 bool , pr7 bool)
BEGIN
  DECLARE tipprovere varchar(250);
  DECLARE mysifra varchar(2);
  DECLARE mytipkljuca int;
  DECLARE mytipdokfakt varchar(1);
  DECLARE mytabela varchar(50);
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE cur CURSOR FOR select * from tmp_proverastatusa where tabela<>'nema';
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  DROP TEMPORARY TABLE IF EXISTS tmp_integritet;
  CREATE TEMPORARY TABLE tmp_integritet (nalog varchar(100), tipprovere varchar(500), opis varchar(500), iznos double, critical int DEFAULT 0); 

  SET @paramdatod = dan1;
  SET @paramdatdo = dan2;
  SET @rn4790=rn4790;
  SET @rn2790=rn2790;
  SET @godina=godina;
  SET @proveraintegritetautoku=1;


  IF pr1 then
    SET @tipprovere = "1 - Analiza uravnotezenosti glavne knjige..."; 

    select sum(izndug-iznpot) AS ukupno from finprom where status=9 and datnal>=@paramdatod and datnal<= @paramdatdo INTO @P1;
    IF NOT @P1 = 0 then
    CALL punitabelu(tipprovere, "", "Dugovna strana je veća od potražne za", @P1, 1);
    END IF; 

    INSERT INTO tmp_integritet select brnal, @tipprovere, "Finansijsko knjigovodstvo - nalog nije u ravnoteži", sum(izndug-iznpot) AS sumxx, 1  from finprom where status=9 and stornirano=0 and datnal>= @paramdatod and datnal<= @paramdatdo and racun not like '9%' AND racun NOT LIKE '8%' group by brnal having abs(sumxx)>0.3;
    INSERT INTO tmp_integritet select brnal, @tipprovere, "Pogonsko knjigovodstvo - nalog nije u ravnoteži", sum(izndug-iznpot) AS sumxx, 1  from finprom where status=9 and stornirano=0 and datnal>= @paramdatod and datnal<= @paramdatdo and racun like '9%' group by brnal having abs(sumxx)>0.3;
    INSERT INTO tmp_integritet select brnal, @tipprovere, "Vanbilansna evidencija - nalog nije u ravnoteži", sum(izndug-iznpot) AS sumxx, 1  from finprom where status=9 and stornirano=0 and datnal>= @paramdatod and datnal<= @paramdatdo and racun like '8%' group by brnal having abs(sumxx)>0.3;

    INSERT INTO tmp_integritet select brnal, @tipprovere, "Godina u datumu naloga se razlikuje od aktuelne", 0, 1 from finprom where year(datnal)<> @godina and status=9 and stornirano=0 group by brnal;
    INSERT INTO tmp_integritet select brnal, @tipprovere, "Godina u datumu dokumenta se razlikuje od aktuelne", 0, 0 from finprom where year(datdok)<> @godina and status=9 and stornirano=0 group by brnal;
    INSERT INTO tmp_integritet select brnal, @tipprovere, "Godina u datumu PDV se razlikuje od aktuelne", 0, 1 from finprom where (brnal not like 'PST%') and year(datpdv)<> @godina and status=9 and stornirano=0 group by brnal;
  END IF;


  IF pr2 then
    SET @tipprovere = "2 - Provera proknjizenih konta u kontnom planu ....";
    INSERT INTO tmp_integritet SELECT racun, @tipprovere, "U kontnom planu ne postoji konto", 0, 1 from finprom where status=9 and stornirano=0 AND racun NOT in (SELECT racun FROM kontniplan where sifrakpl=@kontniplan) group by racun;  
  END IF;

  IF pr3 THEN

    SET @tipprovere = "3 - Provera PDV evidencije sa Finansijskim računima ....";


    SELECT SUM(popdv_promet.pdvos + popdv_promet.pdvps - popdv_promet.bezodbitka) AS iznpopdv from popdv_sifarnik, popdv_promet 
      where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=106 OR popdv_sifarnik.pdvospppdv=107 OR popdv_sifarnik.pdvospppdv=108 or popdv_sifarnik.pdvpspppdv=106 OR popdv_sifarnik.pdvpspppdv=107 OR popdv_sifarnik.pdvpspppdv=108 or popdv_sifarnik.pdvosprdpv2=162 or popdv_sifarnik.pdvpsprdpv2=162 or popdv_sifarnik.pdvosprdpv2=172 or popdv_sifarnik.pdvpsprdpv2=172 or popdv_sifarnik.pdvosprdpv2=182 or popdv_sifarnik.pdvpsprdpv2=182 or popdv_sifarnik.pdvosprdpv2=192 or popdv_sifarnik.pdvpsprdpv2=192) 
       AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and potvrdjeno=1 and stornirano=0 INTO @ulaznipdvpopdv;


    SELECT SUM(finprom.izndug) as iznfinprom from 
       finprom 
       WHERE finprom.status=9 and stornirano=0 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND finprom.racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=1) AND racun<>@rn2790 INTO @ulaznipdvfinprom;
  
    IF ABS(@ulaznipdvpopdv - @ulaznipdvfinprom)>1 THEN
       CALL punitabelu(@tipprovere, "", "Stanje u finanijskom i PDV evidenciji ulaznog PDV se razlikuje za",ABS(@ulaznipdvpopdv - @ulaznipdvfinprom), 1);
    END IF;




    SELECT SUM(popdv_promet.pdvos + popdv_promet.pdvps) AS iznpopdv from popdv_sifarnik, popdv_promet 
      where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=103 OR popdv_sifarnik.pdvospppdv=104 or popdv_sifarnik.pdvpspppdv=103 OR popdv_sifarnik.pdvpspppdv=104 or popdv_sifarnik.pdvosprdpv2=141 OR popdv_sifarnik.pdvosprdpv2=151 or popdv_sifarnik.pdvpsprdpv2=141 OR popdv_sifarnik.pdvpsprdpv2=151) 
       AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and potvrdjeno=1 and stornirano=0 INTO @izlaznipdvpopdv;


    SELECT SUM(finprom.iznpot) as iznfinprom from 
       finprom 
       WHERE finprom.status=9 and stornirano=0 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND finprom.racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=2) AND racun<>@rn4790 INTO @izlaznipdvfinprom;
  
    IF ABS(@izlaznipdvpopdv - @izlaznipdvfinprom)>1 THEN
       CALL punitabelu(@tipprovere, "", "Stanje u finanijskom i PDV evidenciji izlaznog PDV se razlikuje za",ABS(@izlaznipdvpopdv - @izlaznipdvfinprom), 1);
    END IF;

    INSERT INTO tmp_integritet SELECT xx.brnal, @tipprovere, "Neslaganje finansijskog i ulaznog PDV", iznpopdv-iznfinprom, 1 FROM (SELECT popdv_promet.datpdv, popdv_promet.brnal, SUM(popdv_promet.pdvos + popdv_promet.pdvps - popdv_promet.bezodbitka) AS iznpopdv, IF(ISNULL(myfinprom.izndug),0,myfinprom.izndug) as iznfinprom from popdv_sifarnik, popdv_promet left join
       (SELECT brnal,SUM(izndug) AS izndug FROM finprom WHERE status=9 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=1) AND racun<>@rn2790 GROUP BY brnal) AS myfinprom ON popdv_promet.brnal=myfinprom.brnal
      where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=106 OR popdv_sifarnik.pdvospppdv=107 OR popdv_sifarnik.pdvospppdv=108 or popdv_sifarnik.pdvpspppdv=106 OR popdv_sifarnik.pdvpspppdv=107 OR popdv_sifarnik.pdvpspppdv=108 or popdv_sifarnik.pdvosprdpv2=162 or popdv_sifarnik.pdvpsprdpv2=162 or popdv_sifarnik.pdvosprdpv2=172 or popdv_sifarnik.pdvpsprdpv2=172 or popdv_sifarnik.pdvosprdpv2=182 or popdv_sifarnik.pdvpsprdpv2=182 or popdv_sifarnik.pdvosprdpv2=192 or popdv_sifarnik.pdvpsprdpv2=192) 
       AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0
       GROUP BY popdv_promet.brnal  HAVING (ABS(iznpopdv-iznfinprom)>1) OR (ISNULL(iznpopdv) AND iznfinprom<>0) OR (ISNULL(iznfinprom) AND iznpopdv<>0) ORDER by popdv_promet.datpdv) AS xx;

   INSERT INTO tmp_integritet SELECT xx.brnal, @tipprovere, "Neslaganje finansijskog i ulaznog PDV", iznfinprom-iznpopdv, 1 FROM (SELECT finprom.datpdv, finprom.brnal, IF(isnull(mypopdv.iznpopdv),0,mypopdv.iznpopdv) AS iznpopdv,SUM(finprom.izndug) as iznfinprom from 
       finprom left JOIN (SELECT brnal,SUM(popdv_promet.pdvos + popdv_promet.pdvps - popdv_promet.bezodbitka) AS iznpopdv FROM popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=106 OR popdv_sifarnik.pdvospppdv=107 OR popdv_sifarnik.pdvospppdv=108 or popdv_sifarnik.pdvpspppdv=106 OR popdv_sifarnik.pdvpspppdv=107 OR popdv_sifarnik.pdvpspppdv=108 or popdv_sifarnik.pdvosprdpv2=162 or popdv_sifarnik.pdvpsprdpv2=162 or popdv_sifarnik.pdvosprdpv2=172 or popdv_sifarnik.pdvpsprdpv2=172 or popdv_sifarnik.pdvosprdpv2=182 or popdv_sifarnik.pdvpsprdpv2=182 or popdv_sifarnik.pdvosprdpv2=192 or popdv_sifarnik.pdvpsprdpv2=192) AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and popdv_promet.potvrdjeno=1 GROUP BY popdv_promet.brnal) AS mypopdv
       ON mypopdv.brnal=finprom.brnal
       WHERE finprom.status=9 and finprom.stornirano=0 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND finprom.racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=1) AND racun<>@rn2790
       GROUP BY finprom.brnal  HAVING (ABS(iznpopdv-iznfinprom)>1) OR (ISNULL(iznpopdv) AND iznfinprom<>0) OR (ISNULL(iznfinprom) AND iznpopdv<>0) ORDER BY finprom.datpdv) AS xx;

  INSERT INTO tmp_integritet SELECT xx.brnal, @tipprovere, "Neslaganje finansijskog i izlaznog PDV", iznpopdv-iznfinprom, 1 FROM (SELECT popdv_promet.datpdv, popdv_promet.brnal, SUM(popdv_promet.pdvos + popdv_promet.pdvps) AS iznpopdv, IF(ISNULL(myfinprom.iznpot),0,myfinprom.iznpot) as iznfinprom from popdv_sifarnik, popdv_promet left join
     (SELECT brnal,SUM(iznpot) AS iznpot FROM finprom WHERE status=9 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=2) AND racun<>@rn4790 GROUP BY brnal) AS myfinprom ON popdv_promet.brnal=myfinprom.brnal
    where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=103 OR popdv_sifarnik.pdvospppdv=104 or popdv_sifarnik.pdvpspppdv=103 OR popdv_sifarnik.pdvpspppdv=104 or popdv_sifarnik.pdvosprdpv2=141 OR popdv_sifarnik.pdvosprdpv2=151 or popdv_sifarnik.pdvpsprdpv2=141 OR popdv_sifarnik.pdvpsprdpv2=151)
     AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and popdv_promet.potvrdjeno=1 and popdv_promet.stornirano=0
     GROUP BY popdv_promet.brnal  HAVING (ABS(iznpopdv-iznfinprom)>1) OR (ISNULL(iznpopdv) AND iznfinprom<>0) OR (ISNULL(iznfinprom) AND iznpopdv<>0)  ORDER by popdv_promet.datpdv) AS xx;

    INSERT INTO tmp_integritet SELECT xx.brnal, @tipprovere, "Neslaganje finansijskog i izlaznog PDV", iznfinprom-iznpopdv, 1 FROM (SELECT finprom.datpdv, finprom.brnal, IF(isnull(mypopdv.iznpopdv),0,mypopdv.iznpopdv) AS iznpopdv,SUM(finprom.iznpot) as iznfinprom from 
       finprom left JOIN (SELECT brnal,SUM(popdv_promet.pdvos + popdv_promet.pdvps) AS iznpopdv FROM popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and (popdv_sifarnik.pdvospppdv=103 OR popdv_sifarnik.pdvospppdv=104 or popdv_sifarnik.pdvpspppdv=103 OR popdv_sifarnik.pdvpspppdv=104 or popdv_sifarnik.pdvosprdpv2=141 OR popdv_sifarnik.pdvosprdpv2=151 or popdv_sifarnik.pdvpsprdpv2=141 OR popdv_sifarnik.pdvpsprdpv2=151) AND popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and popdv_promet.potvrdjeno=1 GROUP BY popdv_promet.brnal) AS mypopdv
       ON mypopdv.brnal=finprom.brnal
       WHERE finprom.status=9 and finprom.stornirano=0 AND finprom.datpdv>=@paramdatod AND finprom.datpdv<=@paramdatdo AND finprom.racun IN (select konto from tabrnpdv,tabrac where tabrnpdv.racun=tabrac.sifra and sifrakpl=@kontniplan and status=2) AND racun<>@rn4790
       GROUP BY finprom.brnal  HAVING (ABS(iznpopdv-iznfinprom)>1) OR (ISNULL(iznpopdv) AND iznfinprom<>0) OR (ISNULL(iznfinprom) AND iznpopdv<>0) ORDER BY finprom.datpdv) AS xx;



    INSERT INTO tmp_integritet SELECT xx.brnal, @tipprovere, concat("Neslaganje po šifarniku knjiženja (",xx.popdvid,"): Finansijsko<->PDV evidencija"), ABS(xx.iznosfinprom-xx.iznospopdv), 1 FROM (select yy.brnal AS brnal, yy.sifpopdv, yy.popdvid, iznosfinprom, IF(ISNULL(mypopdv.iznos),0,mypopdv.iznos) AS iznospopdv FROM (select finprom.brnal, kontniplan.sifpopdv, siffinpopdv.popdvid, sum(if(siffinpopdv.dugpot=1, finprom.iznpot, finprom.izndug)) as iznosfinprom
     FROM siffinpopdv, kontniplan, finprom where kontniplan.sifrakpl=@kontniplan and finprom.datpdv>=@paramdatod and finprom.datpdv<=@paramdatdo and finprom.racun=kontniplan.racun and kontniplan.sifpopdv=siffinpopdv.sifra and finprom.status=9 and finprom.stornirano=0 and (finprom.vd='IZ' or finprom.vd='NN') GROUP BY finprom.brnal, siffinpopdv.popdvid) AS yy
       LEFT JOIN (select brnal, popdvid, SUM(popdv_promet.osnovicaos+popdv_promet.osnovicaps+popdv_promet.pdvos+popdv_promet.pdvps+popdv_promet.vrednost) AS iznos FROM popdv_promet WHERE popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo and popdv_promet.potvrdjeno=1 GROUP by brnal, popdvid) AS mypopdv 
          ON yy.brnal=mypopdv.brnal AND yy.popdvid=mypopdv.popdvid
     group by brnal, popdvid HAVING ABS(iznosfinprom-iznospopdv)>0) AS xx;


    INSERT INTO tmp_integritet SELECT getosnovnibrnal(popdv_promet.brnal),@tipprovere,"Dokument nije proknjižen u elektronskoj evidenciji PDV",sum(osnovicaos+osnovicaps+pdvos+pdvps),0 from popdv_promet where 
      popdv_promet.datpdv>=@paramdatod AND popdv_promet.datpdv<=@paramdatdo
      and stornirano=0 and posebnaid<>'3.9.x' and (getosnovnibrnal(brnal) not like '%-RZ') and not ((pdvos+pdvps+bezodbitka)=0) 
      and (getosnovnibrnal(brnal) not in (select biznisoftbrnal from eeppdv_promet where not isnull(biznisoftbrnal) group by biznisoftbrnal))
      and (getosnovnibrnal(brnal) not in (select biznisoftbrnal from eeopdv_pojedinacna where not isnull(biznisoftbrnal) group by biznisoftbrnal))
      and (getosnovnibrnal(brnal) not in (select biznisoftbrnal from eeopdv_zbirna where not isnull(biznisoftbrnal) group by biznisoftbrnal)) 
      group by getosnovnibrnal(popdv_promet.brnal);
  END IF;

  IF pr4 THEN

    SET @tipprovere = "4 - Provera radnih naloga ....";


    INSERT INTO tmp_integritet SELECT zz.gnbrnal, @tipprovere, "Ne postoji izdatnica repromaterijala", 0,0 FROM (SELECT gnbrnal, yy.brrn, yy.mystatus FROM radnal 
       LEFT JOIN (select intracun.brrn, intracun.brdok, intracun.status as mystatus from intracun,objekti,(select sifra,sifobj from objekti) as oo2 where intracun.sifobj=objekti.sifra and intracun.obj2=oo2.sifra and (objekti.sifobj=10 or objekti.sifobj=11) and oo2.sifobj=18 GROUP by brdok, intracun.sifobj, brrn) AS yy
         ON radnal.gnbrnal=yy.brdok
      where datnal>=@paramdatod and datnal<=@paramdatdo and status>1 GROUP BY gnbrnal having isnull(yy.brrn) ORDER by gnbrnal) AS zz;


    INSERT INTO tmp_integritet SELECT zz.gnbrnal, @tipprovere, "Izdatnica repromaterijala nije proknjižena", 0,0 FROM (SELECT gnbrnal, yy.brrn, yy.mystatus FROM radnal 
       LEFT JOIN (select intracun.brrn, intracun.brdok, intracun.status as mystatus from intracun,objekti,(select sifra,sifobj from objekti) as oo2 where intracun.sifobj=objekti.sifra and intracun.obj2=oo2.sifra and (objekti.sifobj=10 or objekti.sifobj=11) and oo2.sifobj=18 GROUP by brdok, intracun.sifobj, brrn) AS yy
         ON radnal.gnbrnal=yy.brdok
      where datnal>=@paramdatod and datnal<=@paramdatdo and status>1 GROUP BY gnbrnal having yy.mystatus=1 ORDER by gnbrnal) AS zz;



    INSERT INTO tmp_integritet SELECT zz.gnbrnal, @tipprovere, "Ne postoji prijemnica (polu)proizvoda", 0,0 FROM (SELECT gnbrnal, yy.brrn, yy.mystatus FROM radnal 
       LEFT JOIN (select intracun.brrn, intracun.brdok, intracun.status as mystatus from intracun,objekti,(select sifra,sifobj from objekti) as oo2 where intracun.sifobj=objekti.sifra and intracun.obj2=oo2.sifra and (oo2.sifobj=9 or oo2.sifobj=11) and objekti.sifobj=18 GROUP by brdok, intracun.sifobj, brrn) AS yy
         ON radnal.gnbrnal=yy.brdok
      where datnal>=@paramdatod and datnal<=@paramdatdo and status>1 GROUP BY gnbrnal having isnull(yy.brrn) ORDER by gnbrnal) AS zz;


    INSERT INTO tmp_integritet SELECT zz.gnbrnal, @tipprovere, "Izdatnica (polu)proizvoda nije proknjižena", 0,0 FROM (SELECT gnbrnal, yy.brrn, yy.mystatus FROM radnal 
       LEFT JOIN (select intracun.brrn, intracun.brdok, intracun.status as mystatus from intracun,objekti,(select sifra,sifobj from objekti) as oo2 where intracun.sifobj=objekti.sifra and intracun.obj2=oo2.sifra and (oo2.sifobj=9 or oo2.sifobj=11) and objekti.sifobj=18 GROUP by brdok, intracun.sifobj, brrn) AS yy
         ON radnal.gnbrnal=yy.brdok
      where datnal>=@paramdatod and datnal<=@paramdatdo and status>1 GROUP BY gnbrnal having yy.mystatus=1 ORDER by gnbrnal) AS zz;

  END IF;



  IF pr5 THEN 

    SET @tipprovere = "5 - Provera ispravnosti stalnih sredstava ....";
    INSERT INTO tmp_integritet SELECT zz.rn_nabvr, @tipprovere, "Različiti iznosi na računu A", zz.osiznos-zz.finiznos,0 FROM (SELECT SUM(if(osnabvr.komada=0,osnabvr.nabvr,osnabvr.nabvr*osnabvr.komada))-IF(ISNULL(xxotpisano.iznos),0,xxotpisano.iznos) AS osiznos, IF(ISNULL(yyfinansijsko.iznos),0,yyfinansijsko.iznos) as finiznos, osregos.rn_nabvr FROM osnabvr, osregos 
      LEFT JOIN (SELECT SUM(osotpis.nabvr) AS iznos, osregos.rn_nabvr FROM osregos, osotpis WHERE osregos.osoznaka=osotpis.osoznaka AND osregos.invbroj=osotpis.invbroj and osotpis.datotp>=@paramdatod and status='A' and osotpis.datotp<=@paramdatdo GROUP by rn_nabvr) AS xxotpisano
         ON osregos.rn_nabvr=xxotpisano.rn_nabvr
      LEFT JOIN (select racun,sum(izndug-iznpot) AS iznos from finprom where datnal>=@paramdatod and datnal<=@paramdatdo and status=9 GROUP by racun) AS yyfinansijsko
         ON osregos.rn_nabvr=yyfinansijsko.racun
      WHERE 
    osregos.osoznaka=osnabvr.osoznaka AND osregos.invbroj=osnabvr.invbroj and osnabvr.datsadvr<=@paramdatdo and status='A' GROUP BY osregos.rn_nabvr) AS zz where (zz.osiznos-zz.finiznos)<>0;

    INSERT INTO tmp_integritet SELECT zz.rn_amvr, @tipprovere, "Različiti iznosi na računu B", zz.osiznos-zz.finiznos,0 FROM (SELECT SUM(if(osnabvr.komada=0,osnabvr.amvr,osnabvr.amvr*osnabvr.komada))+IF(ISNULL(yyamortizovano.iznos),0,yyamortizovano.iznos)-IF(ISNULL(yyotpisano.iznos),0,yyotpisano.iznos) AS osiznos, IF(ISNULL(yyfinansijsko.iznos),0,yyfinansijsko.iznos) as finiznos, ostabrn.rn_amvr FROM osnabvr, osregos, ostabrn
      LEFT JOIN (SELECT sum(if(osamvr.komada=0,amvr,amvr * osamvr.komada)) AS iznos, ostabrn.rn_amvr FROM osregos, osamvr, ostabrn WHERE osregos.rn_nabvr=ostabrn.rn_nabvr and osregos.osoznaka=osamvr.osoznaka AND osregos.invbroj=osamvr.invbroj and osamvr.datam<=@paramdatdo and status='A' GROUP by rn_amvr) as yyamortizovano
        ON ostabrn.rn_amvr=yyamortizovano.rn_amvr 
      LEFT JOIN (SELECT SUM(osotpis.amvr) AS iznos, ostabrn.rn_amvr FROM osregos, osotpis, ostabrn WHERE osregos.rn_nabvr=ostabrn.rn_nabvr and osregos.osoznaka=osotpis.osoznaka AND osregos.invbroj=osotpis.invbroj and osotpis.datotp<=@paramdatdo and status='A'  GROUP BY rn_amvr) as yyotpisano
        ON ostabrn.rn_amvr=yyotpisano.rn_amvr
      LEFT JOIN (select racun,sum(iznpot-izndug) AS iznos from finprom where datnal>=@paramdatod and datnal<=@paramdatdo and status=9 GROUP by racun) AS yyfinansijsko
         ON ostabrn.rn_amvr=yyfinansijsko.racun
    WHERE 
      osregos.rn_nabvr=ostabrn.rn_nabvr and osregos.osoznaka=osnabvr.osoznaka AND osregos.invbroj=osnabvr.invbroj and osnabvr.datsadvr<=@paramdatdo and status='A' GROUP BY ostabrn.rn_amvr) AS zz where (zz.osiznos-zz.finiznos)<>0;
  END IF;

  IF pr6 or pr7 THEN
  
    DROP TEMPORARY TABLE IF exists tmp_proverastatusa;
    CREATE TEMPORARY TABLE tmp_proverastatusa (sifra varchar(2), tipkljuca int, tipdokfakt varchar(1), tabela varchar(50));

    SET @qvr=concat("insert into tmp_proverastatusa select sifra, tipkljuca, tipdokfakt, tabela from ", @bsliveid,"opp.documents where not (sifra = 'GN') and not (sifra = 'NA') and not (sifra = 'ND') and not (sifra = 'NK') and not (sifra = 'NO') and not (sifra = 'OA') and not (sifra = 'OT') and not (sifra = 'PC') and not (sifra = 'PL') and not (sifra = 'PS') and not (sifra = 'RD') and not (sifra = 'NI') and not (sifra = 'PF') and not (sifra = 'SN') and not (sifra = 'SP') and not (sifra = 'SU') and not (sifra = 'SZ') and not (sifra = 'TB') and not (sifra = 'ZP') order by tipkljuca");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    deallocate PREPARE stmt1;
  end if;



  IF pr6 THEN

    SET @tipprovere = "6 - Provera statusa dokumenta ....";
  
    OPEN cur;
    set done = false;
    read_loop: LOOP
        FETCH cur into mysifra, mytipkljuca, mytipdokfakt, mytabela;
        IF done THEN
           LEAVE read_loop;
        END IF;
     CALL ProveraStatusa(mysifra, mytipkljuca, mytipdokfakt, mytabela);
    END LOOP read_loop;
    CLOSE cur;

  END IF;


  IF pr7 THEN

    SET @tipprovere = '7 - Provera statusa knjiženja ....';

    drop temporary table if exists tmp_proverax_robno;
    create temporary table tmp_proverax_robno (kbrnal varchar(50) not null primary key);
    insert ignore into tmp_proverax_robno select brnal from robno where datum>=@paramdatod and datum<=@paramdatdo and stornirano=0 group by brnal;
    drop temporary table if exists tmp_proverax_finprom;
    create temporary table tmp_proverax_finprom (kbrnal varchar(50) not null primary key);
    insert ignore into tmp_proverax_finprom select brnal from finprom where datnal>=@paramdatod and datnal<=@paramdatdo and stornirano=0 group by brnal;
    drop temporary table if exists tmp_proverax_trgovacka;
    create temporary table tmp_proverax_trgovacka (kbrnal varchar(50) not null primary key);
    insert ignore into tmp_proverax_trgovacka select brdok from trgovacka where datum>=@paramdatod and datum<=@paramdatdo and stornirano=0 group by brdok;
    drop temporary table if exists tmp_proverax_popdv_promet;
    create temporary table tmp_proverax_popdv_promet (kbrnal varchar(50) not null primary key);
    insert ignore into tmp_proverax_popdv_promet select brnal from popdv_promet where datnal>=@paramdatod and datnal<=@paramdatdo and stornirano=0 group by brnal;

      OPEN cur;
      set done = false;
      read_loop: LOOP
          FETCH cur into mysifra, mytipkljuca, mytipdokfakt, mytabela;
          IF done THEN
             LEAVE read_loop;
          END IF;
        CALL ProveraStatusa(mysifra, mytipkljuca, mytipdokfakt, mytabela);
      END LOOP read_loop;
      CLOSE cur;

    drop temporary table if exists tmp_proverax_robno;
    drop temporary table if exists tmp_proverax_finprom;
    drop temporary table if exists tmp_proverax_trgovacka;
    drop temporary table if exists tmp_proverax_popdv_promet;
    drop temporary table if exists tmp_provera_tabela;
  END IF;
END
```

---

## 66. ProveraStatusa

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `ProveraStatusa`(sifra varchar(2), tipkljuca int(2), tipdokfakt varchar(1), tabela varchar(50))
BEGIN
    DECLARE mystatus,myobjekat,mytip,mywhere, mybrnal, mygroup varchar(200);

    IF @tipprovere = '6 - Provera statusa dokumenta ....' THEN SET mystatus = '=1'; END IF; IF @tipprovere = '7 - Provera statusa knjiženja ....' then SET mystatus = '>1'; END IF;
    SET myobjekat=' sifobj';
    SET mytip='';
    SET mywhere='';

      if (tipkljuca=1) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat ,"),3),'-',right(concat('00000',brkalk),5))");
        SET mygroup = ' brkalk';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=2) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat ,"),3),right(concat('000000',brrn),6))");
        SET mytip = CONCAT(" and ", tabela,".tip = '", tipdokfakt,"'");
        SET mygroup = ' brrn';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=3) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat,"),3),right(concat('000000',brrn),6))");
        SET mygroup = ' brrn';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=4) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat,"),3),'-',right(concat('0000',brnivel),4))");
        SET mygroup = ' brnivel';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=6) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat, "),3),'-',right(concat(date_format(datum, '%m%d')),4))");
        SET mygroup = ' datum';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
        IF @tipprovere = '6 - Provera statusa dokumenta ....' THEN SET mystatus = '=99'; END IF; IF @tipprovere = '7 - Provera statusa knjiženja ....' THEN SET mystatus = '<98 and status >1 and (tipracuna=0 or tipracuna=4)'; END IF;
      END if;

      if (tipkljuca=7) THEN
        SET myobjekat = ' objekat';
        SET mybrnal = CONCAT("concat ('",sifra,"', right(concat('000',", myobjekat, "),3),'-',right(concat(date_format(datum, '%m%d')),4))");
        SET mygroup = ' datum';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=9) then
        SET mybrnal = CONCAT("concat ('",sifra,"',right(concat('000',", myobjekat,"),3),right(concat('000000',brnal),6))");
        SET mygroup = ' datum';
        SET mywhere = CONCAT(" and operater<>'PRENSTBLG' and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=11) then
        SET mybrnal = ' biznisoftbrnal ';
        SET mygroup = ' sifobj,brkalk, brpl';
        SET mywhere = CONCAT(" and datum>='",@paramdatod,"' and datum<='",@paramdatdo,"'");
      END if;

      if (tipkljuca=13) THEN
        SET myobjekat = ' brnal';
        SET mybrnal = CONCAT("concat ('", sifra, "', '-', brnal )");
        SET mygroup = ' brnal';
        SET mywhere = CONCAT(" and datnal>='",@paramdatod,"' and datnal<='",@paramdatdo,"'");
      END if;

      IF @tipprovere = '6 - Provera statusa dokumenta ....' then
        SET @qvr=concat('insert into tmp_integritet select ',mybrnal,',"', @tipprovere,'","Dokument je u obradi (status 1)", 0, 0 from ', tabela,' where status ', mystatus, mytip ,mywhere, ' group by ',myobjekat,', ',mygroup);  
        PREPARE stmt1 FROM @qvr;
        EXECUTE stmt1;
        deallocate PREPARE stmt1;
      END IF;
      
      IF @tipprovere = '7 - Provera statusa knjiženja ....' THEN
          drop temporary table if exists tmp_provera_tabela;
          if (tipkljuca=6) then
            create temporary table tmp_provera_tabela (wbrnal varchar(50) not null primary key, status int(2), tipracuna int(1));
            SET @qvr=concat('insert ignore into tmp_provera_tabela select ',mybrnal,', status, tipracuna from ', tabela,' where status ', mystatus, mytip ,mywhere, ' group by ',myobjekat,', ',mygroup);
          else
            if (tipkljuca=11) then
              create temporary table tmp_provera_tabela (wbrnal varchar(50) not null primary key, status int(2));
              SET @qvr=concat('insert ignore into tmp_provera_tabela select ',mybrnal,', if(status=3 and (samoupdv=0),36,if(status=3 and (samoupdv=1),32,1))  from ', tabela,' where 1 ', mytip ,mywhere, ' group by ',myobjekat,', ',mygroup);
            else
              create temporary table tmp_provera_tabela (wbrnal varchar(50) not null primary key, status int(2));
              SET @qvr=concat('insert ignore into tmp_provera_tabela select ',mybrnal,', status from ', tabela,' where 1 ', mytip ,mywhere, ' group by ',myobjekat,', ',mygroup);
            end if;
          end if;
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;

          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument nije proknjižen u robnom a po statusu bi trebao!", 0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela left join tmp_proverax_robno as xx1 on xx1.kbrnal like concat(wbrnal,"%") where inturobnom(',tipkljuca,',status) and status ', mystatus, ' and isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument nije proknjižen u PDV evidenciji a po statusu bi trebao!",0,1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela left join tmp_proverax_popdv_promet as xx1 on xx1.kbrnal like concat(wbrnal,"%") where intupdv(',tipkljuca,',status) and status ', mystatus, ' and isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument nije proknjižen u finansijskom a po statusu bi trebao!",0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela left join tmp_proverax_finprom as xx1 on xx1.kbrnal like concat(wbrnal,"%") where intufinansijskom(',tipkljuca,',status) and status ', mystatus, ' and isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument nije proknjižen u KEP a po statusu bi trebao!", 0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela left join tmp_proverax_trgovacka as xx1 on xx1.kbrnal like concat(wbrnal,"%") where intukep(',tipkljuca,',status) and status ', mystatus, ' and isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument je proknjižen u robnom a po statusu ne bi trebao!", 0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela, tmp_proverax_robno as xx1 where xx1.kbrnal like concat(wbrnal,"%") and not inturobnom(',tipkljuca,',status) and not isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument je proknjižen u finansijskom a po statusu ne bi trebao!",0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela, tmp_proverax_finprom as xx1 where xx1.kbrnal like concat(wbrnal,"%") and not intufinansijskom(',tipkljuca,',status) and not isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument je proknjižen u KEP a po statusu ne bi trebao!", 0, 1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela, tmp_proverax_trgovacka as xx1 where xx1.kbrnal like concat(wbrnal,"%") and not intukep(',tipkljuca,',status) and not intukep(',tipkljuca,',status) and not isnull(xx1.kbrnal) group by wbrnal ) as tt2');
          PREPARE stmt1 FROM @qvr;
          EXECUTE stmt1;
          deallocate PREPARE stmt1;
          if not (upper(tabela)='BLGPROMET') then
            SET @qvr=concat('insert into tmp_integritet select wbrnal,"',@tipprovere,'","Dokument je proknjižen u PDV evidenciji a po statusu ne bi trebao!",0,1 from (select wbrnal,status, xx1.kbrnal as tbrnal from tmp_provera_tabela, tmp_proverax_popdv_promet as xx1 where xx1.kbrnal like concat(wbrnal,"%") and not intupdv(',tipkljuca,',status) and not isnull(xx1.kbrnal) group by wbrnal ) as tt2');
            PREPARE stmt1 FROM @qvr;
            EXECUTE stmt1;
            deallocate PREPARE stmt1;
          end if;
      end IF;     
 END
```

---

## 67. ProvRezervacije

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `ProvRezervacije`()
BEGIN
    set @pecav=1;
    delete from rezervacija where rezervacija.datum<date(now());
    drop temporary table if exists tmp_myreznals;
    create temporary table tmp_myreznals (brnal varchar(50) not null primary key);
    insert into tmp_myreznals select concat('PF',right(concat('000',sifobj),3),right(concat('000000',brrn),6)) from fakture where tip='P' and status=2 group by sifobj,brrn,tip;
    delete from rezervacija where brnal like 'PF%' and brnal not in (select brnal from tmp_myreznals);
    delete from tmp_myreznals;
    insert into tmp_myreznals select concat('NI',right(concat('000',sifobj),3),right(concat('000000',brrn),6)) from fakture where tip='I' and status=2 group by sifobj,brrn,tip;
    delete from rezervacija where brnal like 'NI%' and brnal not in (select brnal from tmp_myreznals);
    delete from tmp_myreznals;
    insert into tmp_myreznals select concat('NA',right(concat('000',sifobj),3),right(concat('000000',brrn),6)) from tblfaktakcrab where tip='I' and status=2 group by sifobj,brrn,tip;
    delete from rezervacija where brnal like 'NA%' and brnal not in (select brnal from tmp_myreznals);
    drop temporary table if exists tmp_myreznals;
    update fakture,objekti set status=1 WHERE fakture.sifobj=objekti.sifra AND objekti.rezervacijeisticu=1 and tip='P' and status=2 and concat('PF',right(concat('000',fakture.sifobj),3),right(concat('000000',brrn),6)) not in (select brnal from rezervacija);
    update fakture,objekti set status=1 where fakture.sifobj=objekti.sifra and objekti.rezervacijeisticu=1 and tip='I' and status=2 and concat('NI',right(concat('000',fakture.sifobj),3),right(concat('000000',brrn),6)) not in (select brnal from rezervacija);
    update tblfaktakcrab,objekti set status=1 where tblfaktakcrab.sifobj=objekti.sifra and objekti.rezervacijeisticu=1 and tip='I' and status=2 and concat('NA',right(concat('000',tblfaktakcrab.sifobj),3),right(concat('000000',brrn),6)) not in (select brnal from rezervacija);
    update fakture,objekti set status=1 where fakture.sifobj=objekti.sifra AND objekti.rezervacijeisticu=1 and tip='Y' and status=2 and concat('NA',right(concat('000',fakture.sifobj),3),right(concat('000000',brrn),6)) not in (select brnal from rezervacija);
    delete from fakture where status=1 and tip='Y';
    set @pecav=null;
END
```

---

## 68. pr_doeeppdv

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `pr_doeeppdv`(tromesecni int(1))
BEGIN
  delete from tmp_eeppdv_promet;
  if tromesecni=1 then
    insert ignore into tmp_eeppdv_promet select YEAR(datpdv), 20+(QUARTER(datpdv)), brnal, eeppdv_vrstaprometa, getizvor(eeppdv_vrstaprometa,eeppdv_vrstadokumenta), abs(sum(osnovicaos)), abs(sum(pdvos)), abs(sum(osnovicaps)), abs(sum(pdvps)), originalbrnal, 0, 0, operater, ts, 1, 0, 0, datnal, datdok, datpdv, null, null, null, null, null, null, 0, sifpar, pib, brrn,0 from popdv_promet where eeppdv_vrstaprometa>0 and stornirano=0 and potvrdjeno=1 group by brnal, eeppdv_vrstaprometa, eeppdv_vrstadokumenta;
    insert ignore into tmp_eeppdv_promet select YEAR(datpdv), 20+(QUARTER(datpdv)), brnal, eeppdv_vrstaprometa, getizvorbezodbitka(getizvor(eeppdv_vrstaprometa,eeppdv_vrstadokumenta)), 0, abs(sum(if(pdvos=bezodbitka or ((pdvos+pdvps=bezodbitka) and (pdvos<>0) and (pdvps<>0)), bezodbitka-pdvps,0))), 0, abs(sum(if(pdvps=bezodbitka or ((pdvos+pdvps=bezodbitka) and (pdvos<>0) and (pdvps<>0)), bezodbitka-pdvos,0))), originalbrnal, 0, 0, operater, ts, 1, 0, 0, datnal, datdok, datpdv, null, null, null, null, null, null, 0, sifpar, pib, brrn,0  from popdv_promet where eeppdv_vrstaprometa>0 and stornirano=0 and potvrdjeno=1 and bezodbitka<>0 group by brnal, eeppdv_vrstaprometa, eeppdv_vrstadokumenta;
  else
    insert ignore into tmp_eeppdv_promet select YEAR(datpdv), MONTH(datpdv), brnal, eeppdv_vrstaprometa, getizvor(eeppdv_vrstaprometa,eeppdv_vrstadokumenta), abs(sum(osnovicaos)), abs(sum(pdvos)), abs(sum(osnovicaps)), abs(sum(pdvps)), originalbrnal, 0, 0, operater, ts, 1, 0, 0, datnal, datdok, datpdv, null, null, null, null, null, null, 0, sifpar, pib, brrn,0  from popdv_promet where eeppdv_vrstaprometa>0 and stornirano=0 and potvrdjeno=1 group by brnal, eeppdv_vrstaprometa, eeppdv_vrstadokumenta;
    insert ignore into tmp_eeppdv_promet select YEAR(datpdv), MONTH(datpdv), brnal, eeppdv_vrstaprometa, getizvorbezodbitka(getizvor(eeppdv_vrstaprometa,eeppdv_vrstadokumenta)), 0, abs(sum(if(pdvos=bezodbitka or ((pdvos+pdvps=bezodbitka) and (pdvos<>0) and (pdvps<>0)), bezodbitka-pdvps,0))), 0, abs(sum(if(pdvps=bezodbitka or ((pdvos+pdvps=bezodbitka) and (pdvos<>0) and (pdvps<>0)), bezodbitka-pdvos,0))), originalbrnal, 0, 0, operater, ts, 1, 0, 0, datnal, datdok, datpdv, null, null, null, null, null, null, 0, sifpar, pib, brrn,0  from popdv_promet where eeppdv_vrstaprometa>0 and stornirano=0 and potvrdjeno=1 and bezodbitka<>0 group by brnal, eeppdv_vrstaprometa, eeppdv_vrstadokumenta;
  end if;
  delete from tmp_eeppdv_promet where isnull(izvor) or trim(izvor)=''; 
  call SrediTmp_eeppdv_promet(0);
END
```

---

## 69. punitabelu

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `punitabelu`(`ftipprovere` varchar(500),  `fnalog` varchar(500), `fopis` varchar(500), `fiznos` double(15, 2), critical integer)
BEGIN
    INSERT INTO tmp_integritet(tipprovere, iznos, opis, nalog, critical) VALUES (ftipprovere, fiznos, fopis, fnalog, critical);
  END
```

---

## 70. puniTmpZbirnu

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `puniTmpZbirnu`(zabrnal varchar(100), zaperiod int(2), samospremno int(1), zagodinu int(4))
BEGIN
  if trim(zabrnal)='' then
    set @zabrnalxx = '%';
    set zabrnal='XXXXXXXXXX';
  else
    set @zabrnalxx = concat(zabrnal,'/%');
  end if;

  drop temporary table if exists tmp_myeeopdv_zbirna;
  create temporary table tmp_myeeopdv_zbirna like my_eeopdv_zbirna;
  
  insert into tmp_myeeopdv_zbirna select godina, period, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and vrsta = 1
        on duplicate key UPDATE pnos_osnovica=pnos_osnovica+osnovicavs, pnos_pdv=pnos_pdv+pdvvs, pnos_ukupno=pnos_ukupno+osnovicavs+pdvvs, pnns_osnovica=pnns_osnovica+osnovicans, pnns_pdv=pnns_pdv+pdvns, pnns_ukupno=pnns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and vrsta = 2
        on duplicate key UPDATE pbos_osnovica=pbos_osnovica+osnovicavs, pbos_pdv=pbos_pdv+pdvvs, pbos_ukupno=pbos_ukupno+osnovicavs+pdvvs, pbns_osnovica=pbns_osnovica+osnovicans, pbns_pdv=pbns_pdv+pdvns, pbns_ukupno=pbns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and vrsta = 3
        on duplicate key UPDATE pavansos_osnovica=pavansos_osnovica+osnovicavs, pavansos_pdv=pavansos_pdv+pdvvs, pavansos_ukupno=pavansos_ukupno+osnovicavs+pdvvs, pavansns_osnovica=pavansns_osnovica+osnovicans, pavansns_pdv=pavansns_pdv+pdvns, pavansns_ukupno=pavansns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    if(vrsta=4,osnovicavs,0), if(vrsta=4,pdvvs,0), if(vrsta=5,osnovicavs,0), if(vrsta=5, pdvvs, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 4 or vrsta = 5)
        on duplicate key UPDATE tu_osnovicaos=if(vrsta=4,tu_osnovicaos+osnovicavs,tu_osnovicaos), tu_pdvos=if(vrsta=4,tu_pdvos+pdvvs,tu_pdvos), tuav_osnovicaos=if(vrsta=5,tuav_osnovicaos+osnovicavs,tuav_osnovicaos), tuav_pdvos=if(vrsta=5,tuav_pdvos+pdvvs,tuav_pdvos);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0,
    if(vrsta=6,osnovicavs,0), if(vrsta=6,pdvvs,0), if(vrsta=6,osnovicans,0), if(vrsta=6,pdvns,0), if(vrsta=7,osnovicavs,0), if(vrsta=7,pdvvs,0), if(vrsta=7,osnovicans,0), if(vrsta=7,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 6 or vrsta = 7)
        on duplicate key UPDATE pd_osnovicaos=if(vrsta=6,pd_osnovicaos+osnovicavs,pd_osnovicaos), pd_pdvos=if(vrsta=6,pd_pdvos+pdvvs,pd_pdvos), pd_osnovicaps=if(vrsta=6,pd_osnovicaps+osnovicans,pd_osnovicaps),
        pd_pdvps=if(vrsta=6,pd_pdvps+pdvns,pd_pdvps), pdav_osnovicaos=if(vrsta=7,pdav_osnovicaos+osnovicavs,pdav_osnovicaos), pdav_pdvos=if(vrsta=7,pdav_pdvos+pdvvs,pdav_pdvos),
        pdav_osnovicaps=if(vrsta=7,pdav_osnovicaps+osnovicans,pdav_osnovicaps), pdav_pdvps=if(vrsta=7,pdav_pdvps+pdvns,pdav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=8,osnovicavs,0), if(vrsta=8,pdvvs,0), if(vrsta=8,osnovicans,0),if(vrsta=8,pdvns,0), if(vrsta=9,osnovicavs,0), if(vrsta=9,pdvvs,0), if(vrsta=9,osnovicans,0),if(vrsta=9,pdvns,0),
     if(vrsta=10,osnovicavs,0), if(vrsta=10,pdvvs,0), if(vrsta=10,osnovicans,0),if(vrsta=10,pdvns,0),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 8 or vrsta = 9 or vrsta = 10)
        on duplicate key UPDATE poi_osnovicaos=if(vrsta=8,poi_osnovicaos+osnovicavs,poi_osnovicaos), poi_pdvos=if(vrsta=8,poi_pdvos+pdvvs,poi_pdvos),poi_osnovicaps=if(vrsta=8,poi_osnovicaps+osnovicans,poi_osnovicaps), poi_pdvps=if(vrsta=8,poi_pdvps+pdvns,poi_pdvps),
        smi_osnovicaos=if(vrsta=9,smi_osnovicaos+osnovicavs,smi_osnovicaos), smi_pdvos=if(vrsta=9,smi_pdvos+pdvvs,smi_pdvos),smi_osnovicaps=if(vrsta=9,smi_osnovicaps+osnovicans,smi_osnovicaps), smi_pdvps=if(vrsta=9,smi_pdvps+pdvns,smi_pdvps),
        smiav_osnovicaos=if(vrsta=10,smiav_osnovicaos+osnovicavs,smiav_osnovicaos), smiav_pdvos=if(vrsta=10,smiav_pdvos+pdvvs,smiav_pdvos),smiav_osnovicaps=if(vrsta=10,smiav_osnovicaps+osnovicans,smiav_osnovicaps), smiav_pdvps=if(vrsta=10,smiav_pdvps+pdvns,smiav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=11,osnovicavs,0), if(vrsta=11,pdvvs,0), if(vrsta=11,osnovicans,0),if(vrsta=11,pdvns,0), if(vrsta=12,osnovicavs,0), if(vrsta=12,pdvvs,0), if(vrsta=12,osnovicans,0),if(vrsta=12,pdvns,0),
     if(vrsta=13,osnovicavs,0), if(vrsta=13,pdvvs,0), if(vrsta=13,osnovicans,0),if(vrsta=13,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 11 or vrsta = 12 or vrsta  = 13)
        on duplicate key UPDATE pop_osnovicaos=if(vrsta=11,pop_osnovicaos+osnovicavs,pop_osnovicaos), pop_pdvos=if(vrsta=11,pop_pdvos+pdvvs,pop_pdvos),pop_osnovicaps=if(vrsta=11,pop_osnovicaps+osnovicans,pop_osnovicaps), pop_pdvps=if(vrsta=11,pop_pdvps+pdvns,pop_pdvps),
        smp_osnovicaos=if(vrsta=12,smp_osnovicaos+osnovicavs,smp_osnovicaos), smp_pdvos=if(vrsta=12,smp_pdvos+pdvvs,smp_pdvos),smp_osnovicaps=if(vrsta=12,smp_osnovicaps+osnovicans,smp_osnovicaps), smp_pdvps=if(vrsta=12,smp_pdvps+pdvns,smp_pdvps),
        smpav_osnovicaos=if(vrsta=13,smpav_osnovicaos+osnovicavs,smpav_osnovicaos), smpav_pdvos=if(vrsta=13,smpav_pdvos+pdvvs,smpav_pdvos),smpav_osnovicaps=if(vrsta=13,smpav_osnovicaps+osnovicans,smpav_osnovicaps), smpav_pdvps=if(vrsta=13,smpav_pdvps+pdvns,smpav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=14,osnovicavs,0), if(vrsta=14,pdvvs,0), if(vrsta=14,osnovicans,0),if(vrsta=14,pdvns,0), if(vrsta=15,osnovicavs,0), if(vrsta=15,pdvvs,0), if(vrsta=15,osnovicans,0),if(vrsta=15,pdvns,0),
     if(vrsta=16,osnovicavs,0), if(vrsta=16,pdvvs,0), if(vrsta=16,osnovicans,0),if(vrsta=16,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 14 or vrsta = 15 or vrsta = 16)
        on duplicate key UPDATE stpi_osnovicaos=if(vrsta=14,stpi_osnovicaos+osnovicavs,stpi_osnovicaos), stpi_pdvos=if(vrsta=14,stpi_pdvos+pdvvs,stpi_pdvos),stpi_osnovicaps=if(vrsta=14,stpi_osnovicaps+osnovicans,stpi_osnovicaps), stpi_pdvps=if(vrsta=14,stpi_pdvps+pdvns,stpi_pdvps),
        stsi_osnovicaos=if(vrsta=15,stsi_osnovicaos+osnovicavs,stsi_osnovicaos), stsi_pdvos=if(vrsta=15,stsi_pdvos+pdvvs,stsi_pdvos),stsi_osnovicaps=if(vrsta=15,stsi_osnovicaps+osnovicans,stsi_osnovicaps), stsi_pdvps=if(vrsta=15,stsi_pdvps+pdvns,stsi_pdvps),
        stsiav_osnovicaos=if(vrsta=16,stsiav_osnovicaos+osnovicavs,stsiav_osnovicaos), stsiav_pdvos=if(vrsta=16,stsiav_pdvos+pdvvs,stsiav_pdvos),stsiav_osnovicaps=if(vrsta=16,stsiav_osnovicaps+osnovicans,stsiav_osnovicaps), stsiav_pdvps=if(vrsta=16,stsiav_pdvps+pdvns,stsiav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=17,osnovicavs,0), if(vrsta=17,pdvvs,0), if(vrsta=17,osnovicans,0),if(vrsta=17,pdvns,0), if(vrsta=18,osnovicavs,0), if(vrsta=18,pdvvs,0), if(vrsta=18,osnovicans,0),if(vrsta=18,pdvns,0),
     if(vrsta=19,osnovicavs,0), if(vrsta=19,pdvvs,0), if(vrsta=19,osnovicans,0),if(vrsta=19,pdvns,0)
      from eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=eeopdv_zbirna.biznisoftbrnal and primljena=0 and eeopdv_zbirna.uslov=1 where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and if(samospremno=1, status_evidencije=0, true) and if(narednagodina=2,(statusefakturepg='neregistrujese' or statusefakturepg='uradu' or isnull(statusefakturepg) or uslov=0),(veznaefakture.status='neregistrujese' or veznaefakture.status='uradu' or isnull(veznaefakture.status) or uslov=0)) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and (vrsta = 17 or vrsta = 18 or vrsta = 19)
        on duplicate key UPDATE stpp_osnovicaos=if(vrsta=17,stpp_osnovicaos+osnovicavs,stpp_osnovicaos), stpp_pdvos=if(vrsta=17,stpp_pdvos+pdvvs,stpp_pdvos),stpp_osnovicaps=if(vrsta=17,stpp_osnovicaps+osnovicans,stpp_osnovicaps), stpp_pdvps=if(vrsta=17,stpp_pdvps+pdvns,stpp_pdvps),
        stsp_osnovicaos=if(vrsta=18,stsp_osnovicaos+osnovicavs,stsp_osnovicaos), stsp_pdvos=if(vrsta=18,stsp_pdvos+pdvvs,stsp_pdvos),stsp_osnovicaps=if(vrsta=18,stsp_osnovicaps+osnovicans,stsp_osnovicaps), stsp_pdvps=if(vrsta=18,stsp_pdvps+pdvns,stsp_pdvps),
        stspav_osnovicaos=if(vrsta=19,stspav_osnovicaos+osnovicavs,stspav_osnovicaos), stspav_pdvos=if(vrsta=19,stspav_pdvos+pdvvs,stspav_pdvos),stspav_osnovicaps=if(vrsta=19,stspav_osnovicaps+osnovicans,stspav_osnovicaps), stspav_pdvps=if(vrsta=19,stspav_pdvps+pdvns,stspav_pdvps);

  
  drop temporary table if exists tmp_x_eeopdv_zbirna;
  create temporary table tmp_x_eeopdv_zbirna like eeopdv_zbirna;
  insert into tmp_x_eeopdv_zbirna select * from eeopdv_zbirna where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and stornirano=0 and (period = zaperiod or zaperiod=0) and (godina = zagodinu or zagodinu=0) and vrsta>0 and vrsta<20
    and (status_evidencije=0 or biznisoftbrnal in (select biznisoftbrnal from eeopdv_zbirna where (eeopdv_zbirna.biznisoftbrnal=zabrnal or eeopdv_zbirna.brnal like @zabrnalxx) and stornirano=0 and (period = zaperiod or zaperiod=0) and vrsta>0 and vrsta<20 and status_evidencije=0 group by biznisoftbrnal));
END
```

---

## 71. punitmpzbirnusimulacija

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `punitmpzbirnusimulacija`(zabrnal varchar(100), zaperiod int(2), samospremno int(1))
BEGIN
  if trim(zabrnal)='' then
    set @zabrnalxx = '%';
    set zabrnal='XXXXXXXXXX';
  else
    set @zabrnalxx = concat(zabrnal,'/%');
  end if;
  
  drop temporary table if exists tmp_myeeopdv_zbirna;
  create temporary table tmp_myeeopdv_zbirna like my_eeopdv_zbirna;
  
  insert into tmp_myeeopdv_zbirna select godina, period, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  vrsta = 1
        on duplicate key UPDATE pnos_osnovica=pnos_osnovica+osnovicavs, pnos_pdv=pnos_pdv+pdvvs, pnos_ukupno=pnos_ukupno+osnovicavs+pdvvs, pnns_osnovica=pnns_osnovica+osnovicans, pnns_pdv=pnns_pdv+pdvns, pnns_ukupno=pnns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  vrsta = 2
        on duplicate key UPDATE pbos_osnovica=pbos_osnovica+osnovicavs, pbos_pdv=pbos_pdv+pdvvs, pbos_ukupno=pbos_ukupno+osnovicavs+pdvvs, pbns_osnovica=pbns_osnovica+osnovicans, pbns_pdv=pbns_pdv+pdvns, pbns_ukupno=pbns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, osnovicavs, pdvvs, osnovicavs+pdvvs, osnovicans, pdvns, osnovicans+pdvns, '','','',datumevidencije,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  vrsta = 3
        on duplicate key UPDATE pavansos_osnovica=pavansos_osnovica+osnovicavs, pavansos_pdv=pavansos_pdv+pdvvs, pavansos_ukupno=pavansos_ukupno+osnovicavs+pdvvs, pavansns_osnovica=pavansns_osnovica+osnovicans, pavansns_pdv=pavansns_pdv+pdvns, pavansns_ukupno=pavansns_ukupno+osnovicans+pdvns;
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,
    if(vrsta=4,osnovicavs,0), if(vrsta=4,pdvvs,0), if(vrsta=5,osnovicavs,0), if(vrsta=5, pdvvs, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 4 or vrsta = 5)
        on duplicate key UPDATE tu_osnovicaos=if(vrsta=4,tu_osnovicaos+osnovicavs,tu_osnovicaos), tu_pdvos=if(vrsta=4,tu_pdvos+pdvvs,tu_pdvos), tuav_osnovicaos=if(vrsta=5,tuav_osnovicaos+osnovicavs,tuav_osnovicaos), tuav_pdvos=if(vrsta=5,tuav_pdvos+pdvvs,tuav_pdvos);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0,
    if(vrsta=6,osnovicavs,0), if(vrsta=6,pdvvs,0), if(vrsta=6,osnovicans,0), if(vrsta=6,pdvns,0), if(vrsta=7,osnovicavs,0), if(vrsta=7,pdvvs,0), if(vrsta=7,osnovicans,0), if(vrsta=7,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 6 or vrsta = 7)
        on duplicate key UPDATE pd_osnovicaos=if(vrsta=6,pd_osnovicaos+osnovicavs,pd_osnovicaos), pd_pdvos=if(vrsta=6,pd_pdvos+pdvvs,pd_pdvos), pd_osnovicaps=if(vrsta=6,pd_osnovicaps+osnovicans,pd_osnovicaps), 
        pd_pdvps=if(vrsta=6,pd_pdvps+pdvns,pd_pdvps), pdav_osnovicaos=if(vrsta=7,pdav_osnovicaos+osnovicavs,pdav_osnovicaos), pdav_pdvos=if(vrsta=7,pdav_pdvos+pdvvs,pdav_pdvos),
        pdav_osnovicaps=if(vrsta=7,pdav_osnovicaps+osnovicans,pdav_osnovicaps), pdav_pdvps=if(vrsta=7,pdav_pdvps+pdvns,pdav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=8,osnovicavs,0), if(vrsta=8,pdvvs,0), if(vrsta=8,osnovicans,0),if(vrsta=8,pdvns,0), if(vrsta=9,osnovicavs,0), if(vrsta=9,pdvvs,0), if(vrsta=9,osnovicans,0),if(vrsta=9,pdvns,0),
     if(vrsta=10,osnovicavs,0), if(vrsta=10,pdvvs,0), if(vrsta=10,osnovicans,0),if(vrsta=10,pdvns,0),0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 8 or vrsta = 9 or vrsta = 10)
        on duplicate key UPDATE poi_osnovicaos=if(vrsta=8,poi_osnovicaos+osnovicavs,poi_osnovicaos), poi_pdvos=if(vrsta=8,poi_pdvos+pdvvs,poi_pdvos),poi_osnovicaps=if(vrsta=8,poi_osnovicaps+osnovicans,poi_osnovicaps), poi_pdvps=if(vrsta=8,poi_pdvps+pdvns,poi_pdvps),
        smi_osnovicaos=if(vrsta=9,smi_osnovicaos+osnovicavs,smi_osnovicaos), smi_pdvos=if(vrsta=9,smi_pdvos+pdvvs,smi_pdvos),smi_osnovicaps=if(vrsta=9,smi_osnovicaps+osnovicans,smi_osnovicaps), smi_pdvps=if(vrsta=9,smi_pdvps+pdvns,smi_pdvps),
        smiav_osnovicaos=if(vrsta=10,smiav_osnovicaos+osnovicavs,smiav_osnovicaos), smiav_pdvos=if(vrsta=10,smiav_pdvos+pdvvs,smiav_pdvos),smiav_osnovicaps=if(vrsta=10,smiav_osnovicaps+osnovicans,smiav_osnovicaps), smiav_pdvps=if(vrsta=10,smiav_pdvps+pdvns,smiav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=11,osnovicavs,0), if(vrsta=11,pdvvs,0), if(vrsta=11,osnovicans,0),if(vrsta=11,pdvns,0), if(vrsta=12,osnovicavs,0), if(vrsta=12,pdvvs,0), if(vrsta=12,osnovicans,0),if(vrsta=12,pdvns,0),
     if(vrsta=13,osnovicavs,0), if(vrsta=13,pdvvs,0), if(vrsta=13,osnovicans,0),if(vrsta=13,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 11 or vrsta = 12 or vrsta  = 13)
        on duplicate key UPDATE pop_osnovicaos=if(vrsta=11,pop_osnovicaos+osnovicavs,pop_osnovicaos), pop_pdvos=if(vrsta=11,pop_pdvos+pdvvs,pop_pdvos),pop_osnovicaps=if(vrsta=11,pop_osnovicaps+osnovicans,pop_osnovicaps), pop_pdvps=if(vrsta=11,pop_pdvps+pdvns,pop_pdvps),
        smp_osnovicaos=if(vrsta=12,smp_osnovicaos+osnovicavs,smp_osnovicaos), smp_pdvos=if(vrsta=12,smp_pdvos+pdvvs,smp_pdvos),smp_osnovicaps=if(vrsta=12,smp_osnovicaps+osnovicans,smp_osnovicaps), smp_pdvps=if(vrsta=12,smp_pdvps+pdvns,smp_pdvps),
        smpav_osnovicaos=if(vrsta=13,smpav_osnovicaos+osnovicavs,smpav_osnovicaos), smpav_pdvos=if(vrsta=13,smpav_pdvos+pdvvs,smpav_pdvos),smpav_osnovicaps=if(vrsta=13,smpav_osnovicaps+osnovicans,smpav_osnovicaps), smpav_pdvps=if(vrsta=13,smpav_pdvps+pdvns,smpav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=14,osnovicavs,0), if(vrsta=14,pdvvs,0), if(vrsta=14,osnovicans,0),if(vrsta=14,pdvns,0), if(vrsta=15,osnovicavs,0), if(vrsta=15,pdvvs,0), if(vrsta=15,osnovicans,0),if(vrsta=15,pdvns,0),
     if(vrsta=16,osnovicavs,0), if(vrsta=16,pdvvs,0), if(vrsta=16,osnovicans,0),if(vrsta=16,pdvns,0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 14 or vrsta = 15 or vrsta = 16)
        on duplicate key UPDATE stpi_osnovicaos=if(vrsta=14,stpi_osnovicaos+osnovicavs,stpi_osnovicaos), stpi_pdvos=if(vrsta=14,stpi_pdvos+pdvvs,stpi_pdvos),stpi_osnovicaps=if(vrsta=14,stpi_osnovicaps+osnovicans,stpi_osnovicaps), stpi_pdvps=if(vrsta=14,stpi_pdvps+pdvns,stpi_pdvps),
        stsi_osnovicaos=if(vrsta=15,stsi_osnovicaos+osnovicavs,stsi_osnovicaos), stsi_pdvos=if(vrsta=15,stsi_pdvos+pdvvs,stsi_pdvos),stsi_osnovicaps=if(vrsta=15,stsi_osnovicaps+osnovicans,stsi_osnovicaps), stsi_pdvps=if(vrsta=15,stsi_pdvps+pdvns,stsi_pdvps),
        stsiav_osnovicaos=if(vrsta=16,stsiav_osnovicaos+osnovicavs,stsiav_osnovicaos), stsiav_pdvos=if(vrsta=16,stsiav_pdvos+pdvvs,stsiav_pdvos),stsiav_osnovicaps=if(vrsta=16,stsiav_osnovicaps+osnovicans,stsiav_osnovicaps), stsiav_pdvps=if(vrsta=16,stsiav_pdvps+pdvns,stsiav_pdvps);
  
  insert into tmp_myeeopdv_zbirna select godina, period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '','','',datumevidencije,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    if(vrsta=17,osnovicavs,0), if(vrsta=17,pdvvs,0), if(vrsta=17,osnovicans,0),if(vrsta=17,pdvns,0), if(vrsta=18,osnovicavs,0), if(vrsta=18,pdvvs,0), if(vrsta=18,osnovicans,0),if(vrsta=18,pdvns,0),
     if(vrsta=19,osnovicavs,0), if(vrsta=19,pdvvs,0), if(vrsta=19,osnovicans,0),if(vrsta=19,pdvns,0) 
      from tmp_simulacija_eeopdv_zbirna left join veznaefakture on veznaefakture.brnal=tmp_simulacija_eeopdv_zbirna.biznisoftbrnal and primljena=0 and tmp_simulacija_eeopdv_zbirna.uslov=1 where  (vrsta = 17 or vrsta = 18 or vrsta = 19)
        on duplicate key UPDATE stpp_osnovicaos=if(vrsta=17,stpp_osnovicaos+osnovicavs,stpp_osnovicaos), stpp_pdvos=if(vrsta=17,stpp_pdvos+pdvvs,stpp_pdvos),stpp_osnovicaps=if(vrsta=17,stpp_osnovicaps+osnovicans,stpp_osnovicaps), stpp_pdvps=if(vrsta=17,stpp_pdvps+pdvns,stpp_pdvps),
        stsp_osnovicaos=if(vrsta=18,stsp_osnovicaos+osnovicavs,stsp_osnovicaos), stsp_pdvos=if(vrsta=18,stsp_pdvos+pdvvs,stsp_pdvos),stsp_osnovicaps=if(vrsta=18,stsp_osnovicaps+osnovicans,stsp_osnovicaps), stsp_pdvps=if(vrsta=18,stsp_pdvps+pdvns,stsp_pdvps),
        stspav_osnovicaos=if(vrsta=19,stspav_osnovicaos+osnovicavs,stspav_osnovicaos), stspav_pdvos=if(vrsta=19,stspav_pdvos+pdvvs,stspav_pdvos),stspav_osnovicaps=if(vrsta=19,stspav_osnovicaps+osnovicans,stspav_osnovicaps), stspav_pdvps=if(vrsta=19,stspav_pdvps+pdvns,stspav_pdvps);

  
  drop temporary table if exists tmp_simulacija_eeopdv_zbirna_2;
  create temporary table tmp_simulacija_eeopdv_zbirna_2 like tmp_simulacija_eeopdv_zbirna;
  insert into tmp_simulacija_eeopdv_zbirna_2 select * from tmp_simulacija_eeopdv_zbirna;
  drop temporary table if exists tmp_x_eeopdv_zbirna;
  create temporary table tmp_x_eeopdv_zbirna like tmp_simulacija_eeopdv_zbirna;
  insert into tmp_x_eeopdv_zbirna select * from tmp_simulacija_eeopdv_zbirna where (tmp_simulacija_eeopdv_zbirna.biznisoftbrnal=zabrnal or tmp_simulacija_eeopdv_zbirna.brnal like @zabrnalxx) and stornirano=0 and (period = zaperiod or zaperiod=0) and vrsta>0 and vrsta<20
    and (status_evidencije=0 or biznisoftbrnal in (select biznisoftbrnal from tmp_simulacija_eeopdv_zbirna_2 where (tmp_simulacija_eeopdv_zbirna_2.biznisoftbrnal=zabrnal or tmp_simulacija_eeopdv_zbirna_2.brnal like @zabrnalxx) and stornirano=0 and (period = zaperiod or zaperiod=0) and vrsta>0 and vrsta<20 and status_evidencije=0 group by biznisoftbrnal));
END
```

---

## 72. racunajKolicine

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `racunajKolicine`(refDatOd Date, refDatDo Date, godina int(4), firma int(4), SS2grpObj int(2), SS2sifra int(6),
                                   refPeriodDana int(3), relatBrDana int(3), SS1sifObj int(3), SS1brkalk int(6), brojDana int(2),
                                   SS2zalihe double(15, 3), SS2tipdob int(1), ignorisiInterne boolean, minZalihe boolean, apsolutneZalihe boolean,
                                   relBrDana boolean, otvTrebovanja boolean, autoForm boolean, samoZaObj boolean, samoZaAtribut boolean,
                                   objekatUDefinisanimAtributima boolean, AtrKol0Prod0 boolean, komercijalnoPakovanje boolean, transportnoPakovanje boolean, potvrdjeni boolean)
BEGIN
  DECLARE prethodnaGodina double(15, 4);
  DECLARE tekucaGodina double(15, 4);
  DECLARE dnevnaProdaja double(15, 4);
  DECLARE minimalneZalihe double(15, 2);
  DECLARE otvorenaTrebovanja double(15, 2);
  DECLARE stanjeNaDan double(15, 2);
  DECLARE potrebnaKolicina double(15, 2);
  DECLARE docs varchar(100);
  DECLARE docspot varchar(250);
  SET @kolicina = 0;
  SET prethodnaGodina = 0;
  SET tekucaGodina = 0;
  SET minimalneZalihe = 0;
  SET otvorenaTrebovanja = 0;
  SET stanjeNaDan = 0;
  
  SET docs = '(''DF'',''FA'',''FM'',''GP'',''KA'',''PO'',''RB'',''RN'',''RT'',''ZZ'',''IR'',''PI'')'; 
  SET docspot = '(''POTVRDJENO-DF'',''POTVRDJENO-FA'',''POTVRDJENO-FM'',''POTVRDJENO-GP'',''POTVRDJENO-KA'',''POTVRDJENO-PO'',''POTVRDJENO-RB'',''POTVRDJENO-RN'',''POTVRDJENO-RT'',''POTVRDJENO-ZZ'',''POTVRDJENO-IR'',''POTVRDJENO-PI'')'; 
  IF ignorisiInterne THEN
    SET docs = CONCAT(LEFT(docs, 50), ')'); 
  END IF;
  IF YEAR(refDatOD) < godina THEN 
    if potvrdjeni then
      SET @selectZaPrethodnu = CONCAT('SELECT SUM(izlaz) INTO @izlazZaPrethodnu FROM ', @bsliveid, 'opp', firma, godina - 1,
                                    '.robno WHERE sifobj = ', SS2grpObj, ' AND datum >= ', QUOTE(refDatOd), ' AND datum <= ', QUOTE(refDatDo),
                                    ' AND izlaz <> 0 and stornirano=0 AND sifra = ', SS2sifra, ' AND ((LEFT(brnal, 2) IN ', docs,' and not left(brnal,3)="POT") or (left(brnal,13) in ',docspot,'))');      
    else
      SET @selectZaPrethodnu = CONCAT('SELECT SUM(izlaz) INTO @izlazZaPrethodnu FROM ', @bsliveid, 'opp', firma, godina - 1,
                                    '.robno WHERE sifobj = ', SS2grpObj, ' AND datum >= ', QUOTE(refDatOd), ' AND datum <= ', QUOTE(refDatDo),
                                    ' AND izlaz <> 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") AND sifra = ', SS2sifra, ' AND LEFT(brnal, 2) IN ', docs);
      
    end if;
    PREPARE stmt FROM @selectZaPrethodnu;
    EXECUTE stmt;
    IF NOT ISNULL(@izlazZaPrethodnu) THEN
      SET prethodnaGodina = @izlazZaPrethodnu;
    ELSE
      SET prethodnaGodina = 0;
    END IF;
  END IF;
  if potvrdjeni then
    SET @selectZaTekucu = CONCAT('SELECT SUM(izlaz) INTO @izlazZaTekucu FROM robno WHERE sifobj = ', SS2grpObj, ' AND datum >= ', QUOTE(refDatOd),
                               ' AND datum <= ', QUOTE(refDatDo), ' AND izlaz <> 0 and stornirano=0 AND sifra = ', SS2sifra, ' AND ((LEFT(brnal, 2) IN ', docs,' and not left(brnal,3) = "POT") or (left(brnal,13) in ',docspot,'))');    
  else
    SET @selectZaTekucu = CONCAT('SELECT SUM(izlaz) INTO @izlazZaTekucu FROM robno WHERE sifobj = ', SS2grpObj, ' AND datum >= ', QUOTE(refDatOd),
                               ' AND datum <= ', QUOTE(refDatDo), ' AND izlaz <> 0 and stornirano=0  and not (robno.brnal like "POTVRDJENO%") AND sifra = ', SS2sifra, ' AND ((LEFT(brnal, 2) IN ', docs,') or (left(brnal,13) in ',docspot,'))');
  end if;

  PREPARE stmt FROM @selectZaTekucu;
  EXECUTE stmt;  

  IF NOT ISNULL(@izlazZaTekucu) THEN
      SET tekucaGodina = @izlazZaTekucu;
    ELSE
      SET tekucaGodina = 0;
    END IF;
  SET dnevnaProdaja = (prethodnaGodina + tekucaGodina) / refPeriodDana;
  
  IF minZalihe THEN
    IF apsolutneZalihe THEN
      set @minZalihe=null;
      SET @selectMinZaliha = CONCAT('SELECT iminzal INTO @minZalihe FROM nivozaliha WHERE sifra = ', SS2sifra, ' AND sifobj = ', SS2grpObj);
      PREPARE stmt FROM @selectMinZaliha;
      EXECUTE stmt;
      IF NOT ISNULL(@minZalihe) THEN
        SET minimalneZalihe = @minZalihe;
      END IF;
      IF NOT (minimalneZalihe > 0) THEN 
        SET @selectMinZaliha = CONCAT('SELECT iminzal INTO @minZalihe FROM nivozaliha WHERE sifra = ', SS2sifra, ' AND ISNULL(sifobj)');
        PREPARE stmt FROM @selectMinZaliha;
        EXECUTE stmt;
        IF NOT ISNULL(@minZalihe) THEN
          SET minimalneZalihe = @minZalihe;
        END IF;
        IF minimalneZalihe > 0 THEN 
          if potvrdjeni then
            SET @selectMinZaliha = CONCAT('SELECT (SUM(ulaz)-sum(izlaz)) INTO @sumZaliha FROM robno WHERE sifra = ',
                                        SS2sifra, ' AND sifobj <> ', SS2grpObj, ' and datum<=now()  and stornirano=0 '); 
          else
            SET @selectMinZaliha = CONCAT('SELECT (SUM(ulaz)-sum(izlaz)) INTO @sumZaliha FROM robno WHERE sifra = ',
                                        SS2sifra, ' AND sifobj <> ', SS2grpObj, ' and datum<=now() and not (brnal like "POTVRDJENO%")  and stornirano=0 '); 
          end if;
          PREPARE stmt FROM @selectMinZaliha;
          EXECUTE stmt;
          IF NOT ISNULL(@sumZaliha) THEN
            SET minimalneZalihe = minimalneZalihe - @sumZaliha;
          END IF;
          IF minimalneZalihe < 0 THEN
            SET minimalneZalihe = 0;
          END IF;
        END IF;
      END IF;
    END IF;
    IF relBrDana THEN
      SET minimalneZalihe = dnevnaProdaja * relatBrDana;
    END IF;
  END IF;
  
  IF otvTrebovanja THEN
    SET @otvTrebovanja = CONCAT('SELECT SUM(kolicina) INTO @otvTrebKolicina FROM tbltrebovanje WHERE sifobj = ', SS1sifObj, ' AND brkalk <> ', SS1brkalk,
                                ' AND sifra = ', SS2sifra, ' AND statuszat = 1');
    PREPARE stmt FROM @otvTrebovanja;
    EXECUTE stmt;
    IF NOT ISNULL(@otvTrebKolicina) THEN
      SET otvorenaTrebovanja = @otvTrebKolicina;
    END IF;
    SET @otvTrebovanja = CONCAT('SELECT SUM(kolicina) INTO @otvTrebKolicina FROM tblnardobavljacima WHERE sifobj = ', SS1sifObj, ' AND sifra = ',
                                SS2sifra, ' AND statuszat = 1');
    PREPARE stmt FROM @otvTrebovanja;
    EXECUTE stmt;
    IF NOT ISNULL(@otvTrebKolicina) THEN
      SET otvorenaTrebovanja = otvorenaTrebovanja + @otvTrebKolicina;
    END IF;
  END IF;
  
  if potvrdjeni then
    SET @selectNaDan = CONCAT('SELECT (SUM(ulaz)-sum(izlaz)) INTO @stanjeNaDan FROM robno WHERE sifra = ',
                            SS2sifra, ' AND sifobj = ', SS2grpObj, ' and datum<=now()  and stornirano=0 ');
  else
    SET @selectNaDan = CONCAT('SELECT (SUM(ulaz)-sum(izlaz)) INTO @stanjeNaDan FROM robno WHERE sifra = ',
                            SS2sifra, ' AND sifobj = ', SS2grpObj, ' and datum<=now() and not (brnal like "POTVRDJENO%")  and stornirano=0 ');
  end if;
  PREPARE stmt FROM @selectNaDan;
  EXECUTE stmt;
  IF NOT ISNULL(@stanjeNaDan) THEN
    SET stanjeNaDan = @stanjeNaDan;
  END IF;

  
  SET potrebnaKolicina = dnevnaProdaja * brojDana;
  
  SET potrebnaKolicina = potrebnaKolicina + minimalneZalihe;
  
  SET potrebnaKolicina = potrebnaKolicina - otvorenaTrebovanja;
  
  SET potrebnaKolicina = potrebnaKolicina - stanjeNaDan;
  
  SET potrebnaKolicina = CEILING(potrebnaKolicina);

  IF autoForm THEN
    IF samoZaObj THEN
      IF potrebnaKolicina > SS2zalihe THEN
        SET potrebnaKolicina = SS2zalihe;
      END IF;
    END IF;
  END IF;


  IF autoForm THEN 
    IF samoZaObj THEN 
      IF samoZaAtribut THEN 
        IF objekatUDefinisanimAtributima THEN 
          IF NOT stanjeNaDan > 0 THEN 
            IF potrebnaKolicina = 0 THEN 
              IF SS2zalihe > 0 THEN 
                SET potrebnaKolicina = 1;
              END IF;
            END IF;
          END IF;
        END IF;
      END IF;
    END IF;
  END IF;
  IF autoForm THEN 
    IF samoZaAtribut THEN 
      IF AtrKol0Prod0 THEN 
        IF potrebnaKolicina = 0 THEN 
          IF SS2zalihe = 0 THEN 
            SET potrebnaKolicina = 1;
          END IF;
        END IF;
      END IF;
    END IF;
  END IF;
  
  IF potrebnaKolicina > 0 AND (komercijalnoPakovanje OR transportnoPakovanje) THEN
    IF komercijalnoPakovanje THEN
      SET @selectPakovanje = CONCAT('SELECT kpkolicina INTO @pakovanje FROM artikli WHERE sifra = ', SS2sifra, ' AND kpima = 1');
    ELSEIF transportnoPakovanje THEN
      SET @selectPakovanje = CONCAT('SELECT tpkolicina INTO @pakovanje FROM artikli WHERE sifra = ', SS2sifra, ' AND tpima = 1');
    END IF;
    PREPARE stmt FROM @selectPakovanje;
    EXECUTE stmt;
    IF NOT ISNULL(@pakovanje) THEN
      IF @pakovanje > 0 THEN
        IF MOD(potrebnaKolicina, @pakovanje) > 0 THEN
          IF SS2tipdob = 2 THEN 
            SET potrebnaKolicina = FLOOR(potrebnaKolicina / @pakovanje + 1) * @pakovanje;
          END IF;
          IF SS2tipdob = 1 THEN 
            IF NOT (FLOOR(potrebnaKolicina / @pakovanje + 1) * @pakovanje) < SS2zalihe THEN
              SET potrebnaKolicina = FLOOR(SS2zalihe / @pakovanje) * @pakovanje; 
            ELSE
              SET potrebnaKolicina = FLOOR(potrebnaKolicina / @pakovanje + 1) * @pakovanje; 
            END IF;
          END IF;
        END IF;
      END IF;
    END IF;
  END IF;
  SET @kolicina = potrebnaKolicina;
END
```

---

## 73. RekapitulacijaPDV

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `RekapitulacijaPDV`(`periodOd` date, `periodDo` date, klijent int(10), godina int(4), porperiod int(1), myparam10877 int(1))
BEGIN
  DECLARE koristisef boolean;

  call dajmidokumente(3,0,True,periodOd,periodDo,'OPER');
  drop temporary table if exists tmp_rekapitulacijapdv;
  create temporary table tmp_rekapitulacijapdv (brnal varchar(100) not null, brdok varchar(100) not null, mytipdok int(1) default 0, partner int(5) not null, datprom date, datdok date, datprihv date, dutobuhvaceno date, datpdv date, datnal date, idefakture int(10), vrdokizvor int(1), 
      fn_izlazni_period int(2), fn_izlazni_pdv double(15,2) default 0, po_izlazni_period int(2), po_izlazni_popdvid varchar(100), po_izlazni_osnovica double(15,2) default 0, po_izlazni_pdv double(15,2) default 0, 
        pe_izlazni_period int(2), pe_izlazni_osnovica double(15,2) default 0, pe_izlazni_pdv double(15,2) default 0, pe_izlazni_status_evidencije int(1) default 0,
        ze_izlazni_period int(2), ze_izlazni_osnovica double(15,2) default 0, ze_izlazni_pdv double(15,2) default 0, ze_izlazni_tip int(2) default 0, ze_izlazni_status_evidencije int(1) default 0,
      fn_ulazni_period int(2), fn_ulazni_pdv double(15,2) default 0, po_ulazni_period int(2), po_ulazni_popdvid varchar(100), po_ulazni_osnovica double(15,2) default 0, po_ulazni_pdv double(15,2) default 0, po_ulazni_pdv_bezpp double(15,2) default 0, po_ulazni_pdv_sapp double(15,2) default 0, 
        ep_ulazni_period int(2), ep_ulazni_vrstaprometa int(3) default 0, ep_ulazni_osnovica double(15,2) default 0, ep_ulazni_pdv double(15,2) default 0, ep_ulazni_pdv_bezpp double(15,2) default 0, ep_ulazni_pdv_sapp double(15,2) default 0, ep_ulazni_status_evidencije int(1) default 0, statknj int(2), tipkljucan int(2),
          nasef int(1) default 0, pdvok int(1) default 0, napomena int(3) default 0, razgrbrnal varchar(100), ulaznipdvok int(1), izlaznipdvok int(1), fn_izlazni_godina int(4), fn_ulazni_godina int(4), po_ulazni_godina int(4), po_izlazni_godina int(4), pe_izlazni_godina int(4), 
           ze_izlazni_godina int(4), ep_ulazni_godina int(4), myoznnal varchar(10), pe_ignorisi int(1) default 0, pe_tipdok int(2) default 0, sef_ignorisi int(1) default 0, sef_pdv_os double(15,2) default null, sef_pdv_ns double(15,2) default null, datdokxx date, datpromxx date, datprihvxx date,
            primary key(brnal, brdok, partner), index ind1(razgrbrnal), index ind2(idefakture));

  

  insert ignore into tmp_rekapitulacijapdv select brnal, if(tipkljucax=2,brnal,brdok), 0, partner, datprom, datdok, datprihv, dutobuhvaceno, datpdv, datum, idefakture, vrdokizvor, 
     null, null, null, '', null, null,  
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, pregltrans.status, tipkljucax, 0, 0, 0, concat(brnal,'-RZ'), 0, 0, null, null, null, null, null, null, null, oznaka, 0, 0, 0, null, null, null, null, null
     from pregltrans where (tipkljucax=1 or tipkljucax=2 or tipkljucax=11 or tipkljucax=13) and oznaka not in ('TI','TO','OZ')  and ((tip<>"I" and tip<>"O" and tip<>"P") or isnull(tip));



  










  
  SET @qvr=concat('select brnal into @tmpnista from ',@bsliveid,'biznisoftbinaries.sef_sales where klijent=',klijent,' and godina=',godina, ' limit 1');
  PREPARE stmt1 FROM @qvr;
  execute stmt1;
  if found_Rows()>0 then
    set koristisef = true;
  else
    set koristisef = false;
  end if;

  
  set koristisef = true;

  
  SET @qvr=concat('insert ignore into tmp_rekapitulacijapdv select "", brnal, 2, sifraklijenta, datumprometa, datumslanja, datumprihvatanja, iskazanpdv, null, null, idfakture, null, ',
    'null, null, null, "", null, null,',
    '  null, null, null, null,',
    '  null, null, null, null, null,',
    'null, null, null, "", null, null, null, null,',
    '  null, null, null, null, null, null, null, 0, 0, 1, 0, 0, "", 0, 0, null, null, null, null, null, null, null, "PE", 0, 0, 0, null, null, null, null, null',
    ' from ',@bsliveid,'biznisoftbinaries.sef_purchase where klijent=',klijent,' and godina=',godina, ' and ((datumprometa>="',periodod,'" and datumprometa<="',perioddo,'") or (datumslanja>="',periodod,'" and datumslanja<="',perioddo,'")) and (isnull(biznisoftbrnal) or trim(biznisoftbrnal)="")');
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;

  
  call create_tmp_tmp_rek;

  
  
  drop temporary table if exists tmp_rek_ped_4;
  create temporary table tmp_rek_ped_4 (brnal varchar(100) not null primary key, dokumveza varchar(100), datnal date, datdok date, datpdv date, racun varchar(10), nista varchar(100));
  insert into tmp_rek_ped_4 select finprom.brnal, finprom.dokumveza, datnal, datdok, datpdv, finprom.racun,tmp_tmp_rek.brnal from finprom  left join tmp_tmp_rek on finprom.brnal=tmp_tmp_rek.brnal , tabrac, tabrnpdv 
        where finprom.vd<>'PS' and finprom.vd<>'ZK' and finprom.vd<>'OP' and finprom.racun=tabrac.konto and tabrnpdv.racun=tabrac.sifra and tabrac.sifrakpl=@kontniplan and finprom.status=9 and (finprom.brnal not like '%-RZ') and finprom.stornirano=0 group by GetOsnovniBrnal(finprom.brnal)  having isnull(tmp_tmp_rek.brnal);
  update tmp_rek_ped_4 set brnal=GetOsnovniBrnal(brnal);
  insert ignore into tmp_rekapitulacijapdv select tmp_rek_ped_4.brnal, dokumveza, 3, -1, datnal, datdok, null, null, datpdv, datnal, null, null, 
     null, null, null, tmp_tmp_rek.brnal, null, null, 
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, 9, 99, 0, 0, 0, concat(tmp_rek_ped_4.brnal,'-RZ'), 0, 0, null, null, null, null, null, null, null, '99', 0, 0, 0, null, null, null, null, null
     from tmp_rek_ped_4 left join tmp_tmp_rek FORCE INDEX FOR JOIN (primary) on tmp_rek_ped_4.brnal=tmp_tmp_rek.brnal where datpdv>=periodod and datpdv<=perioddo
        group by tmp_rek_ped_4.brnal having isnull(tmp_tmp_rek.brnal);

  
  call create_tmp_tmp_rek;

  
  insert ignore into tmp_rekapitulacijapdv select originalbrnal, brrn, 4, sifpar, datnal, datdok, null, null, datpdv, datnal, null, null, 
     null, null, null, tmp_tmp_rek.brnal, null, null, 
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, 9, 99, 0, 0, 0, concat(originalbrnal,'-RZ'), 0, 0, null, null, null, null, null, null, null, '99', 0, 0, 0, null, null, null, null, null
     from popdv_promet left join tmp_tmp_rek on originalbrnal=tmp_tmp_rek.brnal where (originalbrnal not like '%-RZ') and popdv_promet.stornirano=0 and datpdv>=periodod and datpdv<=perioddo
        group by originalbrnal having isnull(tmp_tmp_rek.brnal);

  call create_tmp_tmp_rek;
  
  insert ignore into tmp_rekapitulacijapdv select biznisoftbrnal, brdokum, 5, sifpar, datprom, datdok, datprih, iskazandatum, datpdv, datnal, idefakture, null, 
     null, null, null, tmp_tmp_rek.brnal, null, null, 
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, 9, 99, 0, 0, 0, biznisoftbrnal, 0, 0, null, null, null, null, null, null, null, '99', 0, 0, 0, null, null, null, null, null
     from eeppdv_promet left join tmp_tmp_rek on biznisoftbrnal=tmp_tmp_rek.brnal where datpdv>=periodod and datpdv<=perioddo
        group by biznisoftbrnal having isnull(tmp_tmp_rek.brnal);

  call create_tmp_tmp_rek;
  
  insert ignore into tmp_rekapitulacijapdv select biznisoftbrnal, eeopdv_pojedinacna.brnal, 6, -1, datumnaloga, null, null, null, datprom, datumnaloga, null, null, 
     null, null, null, tmp_tmp_rek.brnal, null, null, 
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, 9, 99, 0, 0, 0, biznisoftbrnal, 0, 0, null, null, null, null, null, null, null, '99', 0, 0, 0, null, null, null, null, null
     from eeopdv_pojedinacna left join tmp_tmp_rek on biznisoftbrnal=tmp_tmp_rek.brnal where datprom>=periodod and datprom<=perioddo 
        group by biznisoftbrnal having isnull(tmp_tmp_rek.brnal);

  call create_tmp_tmp_rek;
  
  insert ignore into tmp_rekapitulacijapdv select biznisoftbrnal, eeopdv_zbirna.brnal, 6, -1, datumnaloga, null, null, null, datpdv, datumnaloga, null, null, 
     null, null, null, tmp_tmp_rek.brnal, null, null, 
       null, null, null, null,
       null, null, null, null, null,
     null, null, null, '', null, null, null, null,
       null, null, null, null, null, null, null, 9, 99, 0, 0, 0, biznisoftbrnal, 0, 0, null, null, null, null, null, null, null, '99', 0, 0, 0, null, null, null, null, null
     from eeopdv_zbirna left join tmp_tmp_rek on biznisoftbrnal=tmp_tmp_rek.brnal where datpdv>=periodod and datpdv<=perioddo
        group by biznisoftbrnal having isnull(tmp_tmp_rek.brnal);

  
  update tmp_rekapitulacijapdv set po_izlazni_popdvid=null;

  
  drop temporary table if exists tmp_rekap_pe;
  create temporary table tmp_rekap_pe like eeopdv_pojedinacna;
  insert into tmp_rekap_pe select eeopdv_pojedinacna.* from eeopdv_pojedinacna left join veznaefakture on biznisoftbrnal=veznaefakture.brnal and primljena=0 where ((datumnaloga>=periodod and datumnaloga<=perioddo) or (datprom>=periodod and datprom<=perioddo)) and (uslov=0 or (uslov=1 and (if(narednagodina=2,statusefakturepg,veznaefakture.status)='neregistrujese' or if(narednagodina=2,statusefakturepg,veznaefakture.status)='uradu' or isnull(if(narednagodina=2,statusefakturepg,veznaefakture.status)))));

  drop temporary table if exists tmp_rekap_ze;
  create temporary table tmp_rekap_ze like eeopdv_zbirna;
  insert into tmp_rekap_ze select eeopdv_zbirna.* from eeopdv_zbirna left join veznaefakture on biznisoftbrnal=veznaefakture.brnal and primljena=0 where ((datumnaloga>=periodod and datumnaloga<=perioddo) or (datpdv>=periodod and datpdv<=perioddo)) and (uslov=0 or (uslov=1 and (if(narednagodina=2,statusefakturepg,veznaefakture.status)='neregistrujese' or if(narednagodina=2,statusefakturepg,veznaefakture.status)='uradu' or isnull(if(narednagodina=2,statusefakturepg,veznaefakture.status)))));

  


  update tmp_rekapitulacijapdv, tmp_rekap_pe set pe_tipdok=tmp_rekap_pe.tipdok, pe_izlazni_godina=tmp_rekap_pe.godina, pe_izlazni_period=tmp_rekap_pe.period, tmp_rekapitulacijapdv.pe_izlazni_status_evidencije=tmp_rekap_pe.status_evidencije where tmp_rekapitulacijapdv.brnal=tmp_rekap_pe.biznisoftbrnal; 
  update tmp_rekapitulacijapdv, tmp_rekap_ze set ze_izlazni_godina=tmp_rekap_ze.godina, ze_izlazni_period=tmp_rekap_ze.period, tmp_rekapitulacijapdv.ze_izlazni_status_evidencije=tmp_rekap_ze.status_evidencije where tmp_rekapitulacijapdv.brnal=tmp_rekap_ze.biznisoftbrnal; 
  update tmp_rekapitulacijapdv, eeppdv_promet set ep_ulazni_godina=eeppdv_promet.godina, ep_ulazni_period=eeppdv_promet.period, tmp_rekapitulacijapdv.ep_ulazni_status_evidencije=eeppdv_promet.status_evidencije where tmp_rekapitulacijapdv.brnal=eeppdv_promet.biznisoftbrnal;  

  
  update tmp_rekapitulacijapdv, (select GetOsnovniBrnal(brnal) as brnalx, sum(iznpot-izndug) as sumx, datpdv as datpdvx from finprom, (select tabrac.konto from tabrac, tabrnpdv where  tabrnpdv.racun=tabrac.sifra and tabrnpdv.status=2 and tabrac.sifrakpl=@kontniplan group by tabrac.konto) as mytabrac
    where finprom.racun=mytabrac.konto and finprom.status=9 and finprom.stornirano=0 group by GetOsnovniBrnal(brnal), datpdv having sumx<>0) as myx set tmp_rekapitulacijapdv.datpdv=myx.datpdvx, fn_izlazni_godina=year(datpdvx), fn_izlazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.fn_izlazni_pdv=myx.sumx where tmp_rekapitulacijapdv.brnal=myx.brnalx and tmp_rekapitulacijapdv.datpdv=myx.datpdvx;
  update tmp_rekapitulacijapdv, (select GetOsnovniBrnal(brnal) as brnalx, sum(iznpot-izndug) as sumx, datpdv as datpdvx from finprom, (select tabrac.konto from tabrac, tabrnpdv where  tabrnpdv.racun=tabrac.sifra and tabrnpdv.status=2 and tabrac.sifrakpl=@kontniplan group by tabrac.konto) as mytabrac
    where finprom.racun=mytabrac.konto and finprom.status=9 and finprom.stornirano=0 group by GetOsnovniBrnal(brnal), datpdv having sumx<>0) as myx set tmp_rekapitulacijapdv.datpdv=myx.datpdvx, fn_izlazni_godina=year(datpdvx), fn_izlazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.fn_izlazni_pdv=myx.sumx where tmp_rekapitulacijapdv.razgrbrnal=myx.brnalx and tmp_rekapitulacijapdv.datpdv=myx.datpdvx;

  
  update tmp_rekapitulacijapdv, (select GetOsnovniBrnal(brnal) as brnalx, sum(izndug-iznpot) as sumx, datpdv as datpdvx from finprom, (select tabrac.konto from tabrac, tabrnpdv where  tabrnpdv.racun=tabrac.sifra and tabrnpdv.status=1 and tabrac.sifrakpl=@kontniplan group by tabrac.konto) as mytabrac
    where finprom.racun=mytabrac.konto and finprom.status=9 and finprom.stornirano=0 group by GetOsnovniBrnal(brnal), datpdv having sumx<>0) as myx set tmp_rekapitulacijapdv.datpdv=myx.datpdvx, fn_ulazni_godina=year(datpdvx), fn_ulazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.fn_ulazni_pdv=myx.sumx where tmp_rekapitulacijapdv.brnal=myx.brnalx and tmp_rekapitulacijapdv.datpdv=myx.datpdvx;
  update tmp_rekapitulacijapdv, (select GetOsnovniBrnal(brnal) as brnalx, sum(izndug-iznpot) as sumx, datpdv as datpdvx from finprom, (select tabrac.konto from tabrac, tabrnpdv where  tabrnpdv.racun=tabrac.sifra and tabrnpdv.status=1 and tabrac.sifrakpl=@kontniplan group by tabrac.konto) as mytabrac
    where finprom.racun=mytabrac.konto and finprom.status=9 and finprom.stornirano=0 group by GetOsnovniBrnal(brnal), datpdv having sumx<>0) as myx set tmp_rekapitulacijapdv.datpdv=myx.datpdvx, fn_ulazni_godina=year(datpdvx), fn_ulazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.fn_ulazni_pdv=myx.sumx where tmp_rekapitulacijapdv.razgrbrnal=myx.brnalx and tmp_rekapitulacijapdv.datpdv=myx.datpdvx;

  
  update tmp_rekapitulacijapdv, (select replace(originalbrnal,'-RZ','') as brnalx, group_concat(distinct popdv_promet.popdvid) as popdvidx, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps) as osnovice, sum(popdv_promet.pdvos+popdv_promet.pdvps) as pdvx, popdv_sifarnik.ulazni, datpdv as datpdvx 
    from popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and stornirano=0 group by replace(originalbrnal,'-RZ',''),ulazni, datpdv having pdvx<>0 or osnovice<>0) as myx set tmp_rekapitulacijapdv.po_izlazni_godina=year(datpdvx), tmp_rekapitulacijapdv.po_izlazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.po_izlazni_popdvid=myx.popdvidx, tmp_rekapitulacijapdv.po_izlazni_osnovica=osnovice, tmp_rekapitulacijapdv.po_izlazni_pdv=pdvx where (tmp_rekapitulacijapdv.brnal=myx.brnalx) and tmp_rekapitulacijapdv.datpdv=myx.datpdvx and myx.ulazni=0;
  update tmp_rekapitulacijapdv, (select replace(originalbrnal,'-RZ','') as brnalx, group_concat(distinct popdv_promet.popdvid) as popdvidx, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps) as osnovice, sum(popdv_promet.pdvos+popdv_promet.pdvps) as pdvx, popdv_sifarnik.ulazni, datpdv as datpdvx 
    from popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and stornirano=0 group by replace(originalbrnal,'-RZ',''),ulazni, datpdv having pdvx<>0 or osnovice<>0) as myx set tmp_rekapitulacijapdv.po_izlazni_godina=year(datpdvx), tmp_rekapitulacijapdv.po_izlazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.po_izlazni_popdvid=myx.popdvidx, tmp_rekapitulacijapdv.po_izlazni_osnovica=osnovice, tmp_rekapitulacijapdv.po_izlazni_pdv=pdvx where (tmp_rekapitulacijapdv.razgrbrnal=myx.brnalx) and tmp_rekapitulacijapdv.datpdv=myx.datpdvx and myx.ulazni=0;

  update tmp_rekapitulacijapdv, (select replace(originalbrnal,'-RZ','') as brnalx, group_concat(distinct popdv_promet.popdvid) as popdvidx, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps) as osnovice, sum(popdv_promet.pdvos+popdv_promet.pdvps) as pdvx, sum(popdv_promet.bezodbitka) as bezx, popdv_sifarnik.ulazni, datpdv as datpdvx  
    from popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and stornirano=0 group by replace(originalbrnal,'-RZ',''),ulazni, datpdv having pdvx<>0 or osnovice<>0) as myx set tmp_rekapitulacijapdv.po_ulazni_godina=year(datpdvx), tmp_rekapitulacijapdv.po_ulazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.po_ulazni_popdvid=myx.popdvidx, tmp_rekapitulacijapdv.po_ulazni_osnovica=osnovice, tmp_rekapitulacijapdv.po_ulazni_pdv=pdvx, tmp_rekapitulacijapdv.po_ulazni_pdv_bezpp=bezx where (tmp_rekapitulacijapdv.brnal=myx.brnalx) and tmp_rekapitulacijapdv.datpdv=myx.datpdvx and myx.ulazni=1;
  update tmp_rekapitulacijapdv, (select replace(originalbrnal,'-RZ','') as brnalx, group_concat(distinct popdv_promet.popdvid) as popdvidx, sum(popdv_promet.osnovicaos+popdv_promet.osnovicaps) as osnovice, sum(popdv_promet.pdvos+popdv_promet.pdvps) as pdvx, sum(popdv_promet.bezodbitka) as bezx, popdv_sifarnik.ulazni, datpdv as datpdvx  
    from popdv_promet, popdv_sifarnik where popdv_promet.popdvid=popdv_sifarnik.popdvid and stornirano=0 group by replace(originalbrnal,'-RZ',''),ulazni, datpdv having pdvx<>0 or osnovice<>0) as myx set tmp_rekapitulacijapdv.po_ulazni_godina=year(datpdvx), tmp_rekapitulacijapdv.po_ulazni_period=GetPeriod(porperiod,datpdvx), tmp_rekapitulacijapdv.po_ulazni_popdvid=myx.popdvidx, tmp_rekapitulacijapdv.po_ulazni_osnovica=osnovice, tmp_rekapitulacijapdv.po_ulazni_pdv=pdvx, tmp_rekapitulacijapdv.po_ulazni_pdv_bezpp=bezx where (tmp_rekapitulacijapdv.razgrbrnal=myx.brnalx) and tmp_rekapitulacijapdv.datpdv=myx.datpdvx and myx.ulazni=1;

  update tmp_rekapitulacijapdv set po_ulazni_pdv_sapp=po_ulazni_pdv-po_ulazni_pdv_bezpp;

  
  update tmp_rekapitulacijapdv, (select biznisoftbrnal, if(tipdok=1,sum(osnovicaos+osnovicans)*-1,sum(osnovicaos+osnovicans)) as osnovicax, if(tipdok=1,sum(pdv)*-1,sum(pdv)) as pdvx, datprom from tmp_rekap_pe group by biznisoftbrnal, datprom) as myx set tmp_rekapitulacijapdv.pe_izlazni_osnovica=osnovicax, tmp_rekapitulacijapdv.pe_izlazni_pdv=pdvx where tmp_rekapitulacijapdv.brnal=myx.biznisoftbrnal and tmp_rekapitulacijapdv.datpdv=myx.datprom;  
  update tmp_rekapitulacijapdv, (select biznisoftbrnal, sum(if(vrsta in (9,10,12,13,15,16,18,19),(osnovicavs+osnovicans)*-1,osnovicavs+osnovicans)) as osnovicax, sum(if(vrsta in (9,10,12,13,15,16,18,19),(pdvvs+pdvns)*-1,pdvvs+pdvns)) as pdvx, datpdv from tmp_rekap_ze group by biznisoftbrnal, datpdv) as myx set tmp_rekapitulacijapdv.ze_izlazni_osnovica=osnovicax, tmp_rekapitulacijapdv.ze_izlazni_pdv=pdvx where tmp_rekapitulacijapdv.brnal=myx.biznisoftbrnal and tmp_rekapitulacijapdv.datpdv=myx.datpdv;

  
  drop temporary table if exists tmp_rek_ped_7;
  create temporary table tmp_rek_ped_7 (biznisoftbrnal varchar(50) not null, osnovicax double(15,2) default 0, pdvx double(15,2) default 0, datpdv date not null, primary key (biznisoftbrnal, datpdv));
  insert into tmp_rek_ped_7 select biznisoftbrnal, sum(if((vrstaprometa in (14,16,24,26)) or (vrstaprometa>520),(osnovicavs+osnovicans)*-1,osnovicavs+osnovicans)) as osnovicax, sum(if((vrstaprometa in (14,16,24,26)) or (vrstaprometa>520),(pdvvs+pdvns)*-1,pdvvs+pdvns)) as pdvx, datpdv from eeppdv_promet where (isnull(narednagodina) or (narednagodina=0)) and (izvor not like '%.x') group by biznisoftbrnal;
  update tmp_rekapitulacijapdv, tmp_rek_ped_7 as myx
    set tmp_rekapitulacijapdv.ep_ulazni_osnovica=myx.osnovicax, tmp_rekapitulacijapdv.ep_ulazni_pdv=myx.pdvx where tmp_rekapitulacijapdv.brnal=myx.biznisoftbrnal and tmp_rekapitulacijapdv.datpdv=myx.datpdv;
  update tmp_rekapitulacijapdv, tmp_rek_ped_7 as myx
    set tmp_rekapitulacijapdv.ep_ulazni_osnovica=myx.osnovicax, tmp_rekapitulacijapdv.ep_ulazni_pdv=myx.pdvx where tmp_rekapitulacijapdv.brnal like '%-RZ' and myx.biznisoftbrnal=concat(tmp_rekapitulacijapdv.brnal,'-RZ') and tmp_rekapitulacijapdv.datpdv=myx.datpdv;

  delete from tmp_rek_ped_7;
  insert into tmp_rek_ped_7 select biznisoftbrnal, sum(osnovicavs+osnovicans) as osnovicax, sum(pdvvs+pdvns) as pdvx, datpdv from eeppdv_promet where izvor like '%.x' group by biznisoftbrnal; 
  update tmp_rekapitulacijapdv, tmp_rek_ped_7 as myx
    set tmp_rekapitulacijapdv.ep_ulazni_pdv_bezpp=myx.pdvx where tmp_rekapitulacijapdv.brnal=myx.biznisoftbrnal;
  update tmp_rekapitulacijapdv, tmp_rek_ped_7 as myx
    set tmp_rekapitulacijapdv.ep_ulazni_pdv_bezpp=myx.pdvx where tmp_rekapitulacijapdv.brnal like '%-RZ' and myx.biznisoftbrnal=concat(tmp_rekapitulacijapdv.brnal,'-RZ');

  update tmp_rekapitulacijapdv set ep_ulazni_pdv_sapp=ep_ulazni_pdv-if(isnull(ep_ulazni_pdv_bezpp),0,ep_ulazni_pdv_bezpp);

  
  SET @qvr=concat('update tmp_rekapitulacijapdv,',@bsliveid,'biznisoftbinaries.sef_purchase set sef_pdv_os=sef_purchase.pdvos+sef_purchase.pdvps, datdokxx=sef_purchase.datumslanja, datpromxx=sef_purchase.datumprometa, datprihvxx=sef_purchase.datumprihvatanja ',
    '  where klijent=',klijent,' and godina=',godina, ' and sef_purchase.idfakture=tmp_rekapitulacijapdv.idefakture and tmp_rekapitulacijapdv.idefakture>0');
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;


  
  SET @qvr=concat('update tmp_rekapitulacijapdv, ',@bsliveid,'biznisoftbinaries.sef_sales set nasef=1 where sef_sales.klijent=',klijent,' and sef_sales.godina=',godina, ' and sef_sales.biznisoftbrnal=tmp_rekapitulacijapdv.brnal and sef_sales.sifraklijenta=tmp_rekapitulacijapdv.partner');
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;
  update tmp_rekapitulacijapdv, veznaefakture set nasef=1 where tmp_rekapitulacijapdv.brnal=veznaefakture.brnal and veznaefakture.primljena=0 and (veznaefakture.status='eksterno' or veznaefakture.status='poslato' or veznaefakture.status='prihvaceno' or veznaefakture.status='odbijeno' or veznaefakture.status='storno');

  
  update tmp_rekapitulacijapdv set izlaznipdvok=1 where fn_izlazni_pdv=po_izlazni_pdv and ((nasef=1 or not koristisef) or ((pe_izlazni_pdv<=>fn_izlazni_pdv) or (ze_izlazni_pdv<=>fn_izlazni_pdv))) and (not isnull(fn_izlazni_pdv) or not isnull(po_izlazni_pdv)) and not isnull(brnal) and not (trim(brnal)='') ;
  update tmp_rekapitulacijapdv set ulaznipdvok=1 where fn_ulazni_pdv=po_ulazni_pdv_sapp and po_ulazni_pdv_sapp=ep_ulazni_pdv_sapp  and (not isnull(fn_ulazni_pdv) or not isnull(po_ulazni_pdv_sapp)) and not isnull(brnal) and not (trim(brnal)='') ;
  
  update tmp_rekapitulacijapdv set ulaznipdvok=1 where (isnull(fn_ulazni_pdv) or (fn_ulazni_pdv=0)) and po_ulazni_pdv_bezpp=ep_ulazni_pdv_bezpp;
  
  update tmp_rekapitulacijapdv set izlaznipdvok=1 where (nasef=1 or not koristisef) and ((fn_izlazni_pdv=0) or isnull(fn_izlazni_pdv)) and ((po_izlazni_pdv=0) or isnull(po_izlazni_pdv)) and ((pe_izlazni_pdv=0) or isnull(pe_izlazni_pdv)) and ((ze_izlazni_pdv=0) or isnull(ze_izlazni_pdv));

  
  update tmp_rekapitulacijapdv set fn_ulazni_pdv=null where fn_ulazni_pdv=0;
  update tmp_rekapitulacijapdv set fn_izlazni_pdv=null where fn_izlazni_pdv=0;
  update tmp_rekapitulacijapdv set po_ulazni_pdv_sapp=null where po_ulazni_pdv_sapp=0;
  update tmp_rekapitulacijapdv set po_izlazni_pdv=null where po_izlazni_pdv=0;
  update tmp_rekapitulacijapdv set ep_ulazni_pdv_sapp=null where ep_ulazni_pdv_sapp=0;
  update tmp_rekapitulacijapdv set pe_izlazni_pdv=null where pe_izlazni_pdv=0;
  update tmp_rekapitulacijapdv set ze_izlazni_pdv=null where ze_izlazni_pdv=0;

  
  delete from tmp_rekapitulacijapdv where isnull(fn_ulazni_pdv) and isnull(fn_izlazni_pdv) and isnull(po_ulazni_pdv_sapp) and isnull(po_izlazni_pdv) and isnull(ep_ulazni_pdv_sapp) and isnull(po_ulazni_pdv_bezpp) and isnull(ep_ulazni_pdv_bezpp) and isnull(pe_izlazni_pdv) and isnull(ze_izlazni_pdv) and isnull(ze_izlazni_osnovica) and myoznnal<>'PE';

  update tmp_rekapitulacijapdv set ulaznipdvok=1  where round(fn_ulazni_pdv)<=>round(po_ulazni_pdv_sapp) and round(fn_ulazni_pdv)<=>round(ep_ulazni_pdv_sapp);
 
  update tmp_rekapitulacijapdv set izlaznipdvok=1 where round(fn_izlazni_pdv)<=>round(po_izlazni_pdv) and (nasef=1 or (isnull(fn_izlazni_pdv) and isnull(po_izlazni_pdv)) or (round(fn_izlazni_pdv)=(if(isnull(ze_izlazni_pdv),0,round(ze_izlazni_pdv)) + if(isnull(pe_izlazni_pdv) or pe_ignorisi=1,0, round(pe_izlazni_pdv)))));
  update tmp_rekapitulacijapdv set pdvok=1 where ulaznipdvok=1 and izlaznipdvok=1;
  
  update tmp_rekapitulacijapdv set pdvok=0 where brnal='' and isnull(dutobuhvaceno) and mytipdok=2;
  if koristisef then
    update tmp_rekapitulacijapdv set pdvok=0 where nasef<>1 and ((fn_izlazni_pdv<>0 and not isnull(fn_izlazni_pdv)) or (po_izlazni_pdv<>0 and not isnull(po_izlazni_pdv))) and isnull(pe_izlazni_pdv) and isnull(ze_izlazni_pdv);
  end if;

  drop temporary table if exists tmp_rekap_pe;
  drop temporary table if exists tmp_rekap_ze;
  

  if myparam10877=1 then
    delete from tmp_rekapitulacijapdv where brnal in (SELECT GetOsnovniBrnal(popdv_promet.brnal) as brnal from popdv_promet left join veznazapopdv on veznazapopdv.brnal=popdv_promet.originalbrnal where stornirano=0 AND veznazapopdv.status='storno' group BY brnal);
  end if;

  
  drop temporary table if exists tmp_r_napomene;
  create temporary table tmp_r_napomene (brnal varchar(100) not null, brdok varchar(100) not null, partner int(5) not null, myuuid varchar(255) not null, napomena varchar(700));
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), 'Ne postoji broj naloga. Na osnovu primljene eFakture nije kreiran dokument u BizniSoft-u' from tmp_rekapitulacijapdv where (isnull(brnal) or trim(brnal)='') and mytipdok=2;
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Dokument nije proknjižen u PDV evidenciji (status dokumenta: ',statknj,')') from tmp_rekapitulacijapdv where mytipdok=0 and (brnal not like 'PPPL%' and not intupdv(tipkljucan,statknj)) or (brnal like 'PPPL%' and statknj<3); 
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Dokument nije proknjižen u finansijskom knjigovodstvu (status dokumenta: ',statknj,')') from tmp_rekapitulacijapdv where mytipdok=0 and (brnal not like 'PPPL%' and not intufinansijskom(tipkljucan,statknj)) or (brnal like 'PPPL%' and (statknj=1));
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Dokument nije proknjižen u finansijskom knjigovodstvu') from tmp_rekapitulacijapdv where mytipdok=4 and isnull(fn_izlazni_pdv) and isnull(fn_ulazni_pdv);
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Razlika u poreskom periodu ulaznog PDV') from tmp_rekapitulacijapdv where not (fn_ulazni_period<=>po_ulazni_period and fn_ulazni_period<=>ep_ulazni_period) and not (isnull(fn_ulazni_period) or isnull(po_ulazni_period) or isnull(ep_ulazni_period));

  IF isnull(@BezProvereStatusa) then
    insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Pojedinačna evidencija nije evidentirana na SEF') from tmp_rekapitulacijapdv where pe_izlazni_status_evidencije=0;
    insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Stavka Zbirne evidencija nije evidentirana na SEF') from tmp_rekapitulacijapdv where ze_izlazni_status_evidencije=0;
    insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Stavka evidencije prethodnog PDV nije evidentirana na SEF') from tmp_rekapitulacijapdv where ep_ulazni_status_evidencije=0;
  end if;

  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Datum naloga nije u aktuelnoj godini') from tmp_rekapitulacijapdv where year(datnal)<>godina;
  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Dokument nije proknjižen u finansijskom knjigovodstvu') from tmp_rekapitulacijapdv where (isnull(fn_ulazni_pdv) and po_ulazni_pdv<>0 and po_ulazni_pdv<>po_ulazni_pdv_bezpp) or (isnull(fn_izlazni_pdv) and po_izlazni_pdv<>0);

  insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Iznos PDV u Elektronskoj evidenciji prethodnog PDV se ne slaže sa iznosom PDV na samoj eFakturi (',abs(abs(ep_ulazni_pdv)-abs(sef_pdv_os)),' RSD). Da li na eFakturi postoji avans?') from tmp_rekapitulacijapdv where abs(round(ep_ulazni_pdv,1))<>abs(round(sef_pdv_os,1)) and idefakture>0;

  if koristisef then
    insert into tmp_r_napomene select brnal, brdok, partner, uuid(), concat('Dokument u kome je iskazan PDV nije registrovan na SEF a ne postoje knjiženja u Pojedinačnoj i/ili Zbirnoj evidenciji') from tmp_rekapitulacijapdv where nasef<>1 and (fn_izlazni_pdv<> 0 or po_izlazni_pdv<>0) and isnull(pe_izlazni_pdv) and isnull(ze_izlazni_pdv);
  end if;

  
  update tmp_rekapitulacijapdv set pe_ignorisi=1 where not isnull(pe_izlazni_pdv) and (pe_tipdok=1 or pe_tipdok=2);

  
  update tmp_rekapitulacijapdv set sef_ignorisi=1 where nasef=1 and (fn_izlazni_pdv<0 or po_izlazni_pdv<0) and (myoznnal='OK' or myoznnal='PK');

  
  update tmp_rekapitulacijapdv,tmp_r_napomene set tmp_rekapitulacijapdv.napomena=1 where tmp_rekapitulacijapdv.brnal<=>tmp_r_napomene.brnal and tmp_rekapitulacijapdv.brdok=tmp_r_napomene.brdok and tmp_rekapitulacijapdv.partner=tmp_r_napomene.partner;

  
  drop temporary table if exists tmp_rekap_pdv;
  create temporary table tmp_rekap_pdv (godina int(4) not null, period int(2) not null, fn_ulazni double(15,2), fn_izlazni double(15,2), fn_razlika double(15,2),
    po_ulazni double(15,2), po_izlazni double(15,2), po_razlika double(15,2),
    ee_ulazni double(15,2), ee_sef_izlazni double(15,2), ee_pe_izlazni double(15,2), ee_pe_ignorisi double(15,2), ee_ze_izlazni double(15,2), ee_razlika double(15,2), ee_sef_ignorisi double(15,2) default 0,
    primary key(godina,period));

  insert into tmp_rekap_pdv select fn_ulazni_godina, fn_ulazni_period, if(isnull(sum(fn_ulazni_pdv)),0,sum(fn_ulazni_pdv)), 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0 from tmp_rekapitulacijapdv where not isnull(fn_ulazni_godina) and not isnull(fn_ulazni_period) group by fn_ulazni_godina, fn_ulazni_period;
  insert into tmp_rekap_pdv select fn_izlazni_godina, fn_izlazni_period, 0, fn_izlazni_pdv, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0 from (select fn_izlazni_godina, fn_izlazni_period, sum(fn_izlazni_pdv) as fn_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(fn_izlazni_godina) and not isnull(fn_izlazni_period) group by fn_izlazni_godina, fn_izlazni_period) as myx where not isnull(fn_izlazni_pdv) on DUPLICATE KEY update fn_izlazni=fn_izlazni+fn_izlazni_pdv;
  insert into tmp_rekap_pdv select po_ulazni_godina, po_ulazni_period, 0, 0, 0, po_ulazni_pdv_sapp, 0, 0, 0, 0, 0, 0 ,0 ,0, 0 from (select po_ulazni_godina, po_ulazni_period, sum(po_ulazni_pdv_sapp) as po_ulazni_pdv_sapp from tmp_rekapitulacijapdv where not isnull(po_ulazni_godina) and not isnull(po_ulazni_period) group by po_ulazni_godina, po_ulazni_period) as myx where not isnull(po_ulazni_pdv_sapp) on DUPLICATE KEY update po_ulazni=po_ulazni+po_ulazni_pdv_sapp;
  insert into tmp_rekap_pdv select po_izlazni_godina, po_izlazni_period, 0, 0, 0, 0, po_izlazni_pdv, 0, 0, 0, 0, 0 ,0 ,0, 0 from (select po_izlazni_godina, po_izlazni_period, sum(po_izlazni_pdv) as po_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(po_izlazni_godina) and not isnull(po_izlazni_period) group by po_izlazni_godina, po_izlazni_period) as myx where not isnull(po_izlazni_pdv) on DUPLICATE KEY update po_izlazni=po_izlazni+po_izlazni_pdv;
  insert into tmp_rekap_pdv select ep_ulazni_godina,  ep_ulazni_period, 0, 0, 0, 0, 0, 0, ep_ulazni_pdv_sapp, 0, 0, 0 ,0 ,0, 0 from (select ep_ulazni_godina, ep_ulazni_period, sum(ep_ulazni_pdv_sapp) as ep_ulazni_pdv_sapp from tmp_rekapitulacijapdv where not isnull(ep_ulazni_godina) and not isnull(ep_ulazni_period) group by ep_ulazni_godina, ep_ulazni_period) as myx where not isnull(myx.ep_ulazni_pdv_sapp) on DUPLICATE KEY update ee_ulazni=ee_ulazni+ep_ulazni_pdv_sapp;
  
  insert into tmp_rekap_pdv select po_izlazni_godina, po_izlazni_period, 0, 0, 0, 0, 0, 0, 0, po_izlazni_pdv, 0, 0 ,0 ,0, 0 from (select po_izlazni_godina, po_izlazni_period, sum(po_izlazni_pdv) as po_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(po_izlazni_godina) and not isnull(po_izlazni_period) and nasef=1 group by po_izlazni_godina, po_izlazni_period) as myx where not isnull(po_izlazni_pdv) on DUPLICATE KEY update ee_sef_izlazni=ee_sef_izlazni+po_izlazni_pdv;
  insert into tmp_rekap_pdv select pe_izlazni_godina, pe_izlazni_period, 0, 0, 0, 0, 0, 0, 0, 0, pe_izlazni_pdv, 0, 0 ,0, 0 from (select pe_izlazni_godina, pe_izlazni_period, sum(pe_izlazni_pdv) as pe_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(pe_izlazni_godina) and not isnull(pe_izlazni_period) group by pe_izlazni_godina, pe_izlazni_period) as myx where not isnull(pe_izlazni_pdv) on DUPLICATE KEY update ee_pe_izlazni=ee_pe_izlazni+pe_izlazni_pdv;
  insert into tmp_rekap_pdv select pe_izlazni_godina, pe_izlazni_period, 0, 0, 0, 0, 0, 0, 0, 0, 0, pe_izlazni_pdv, 0 ,0, 0 from (select pe_izlazni_godina, pe_izlazni_period, sum(pe_izlazni_pdv) as pe_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(pe_izlazni_godina) and not isnull(pe_izlazni_period) and pe_ignorisi=1 group by pe_izlazni_godina, pe_izlazni_period) as myx where not isnull(pe_izlazni_pdv) on DUPLICATE KEY update ee_pe_ignorisi=ee_pe_ignorisi+pe_izlazni_pdv;
  insert into tmp_rekap_pdv select ze_izlazni_godina, ze_izlazni_period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ze_izlazni_pdv ,0, 0 from (select ze_izlazni_godina, ze_izlazni_period, sum(ze_izlazni_pdv) as ze_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(ze_izlazni_godina) and not isnull(ze_izlazni_period) group by ze_izlazni_godina, ze_izlazni_period) as myx where not isnull(ze_izlazni_pdv) on DUPLICATE KEY update ee_ze_izlazni=ee_ze_izlazni+ze_izlazni_pdv;

  insert into tmp_rekap_pdv select po_izlazni_godina, po_izlazni_period, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, po_izlazni_pdv from (select po_izlazni_godina, po_izlazni_period, sum(po_izlazni_pdv) as po_izlazni_pdv from tmp_rekapitulacijapdv where not isnull(po_izlazni_godina) and not isnull(po_izlazni_period) and nasef=1 and sef_ignorisi=1 group by po_izlazni_godina, po_izlazni_period) as myx where not isnull(po_izlazni_pdv) on DUPLICATE KEY update ee_sef_ignorisi=ee_sef_ignorisi+po_izlazni_pdv;

  update tmp_rekap_pdv set fn_razlika=fn_izlazni-fn_ulazni, po_razlika=po_izlazni-po_ulazni, ee_razlika=ee_sef_izlazni-ee_sef_ignorisi+ee_pe_izlazni-ee_pe_ignorisi+ee_ze_izlazni-ee_ulazni;

  drop temporary table tmp_tmp_rek;
  drop temporary table pregltrans;
  drop temporary table tmp_rek_ped_4;
  drop temporary table tmp_rek_ped_7;
end
```

---

## 74. RezNarTrb

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `RezNarTrb`()
BEGIN
  set @pecav=1;
  DROP temporary TABLE if EXISTS tmp_zanarez;
  CREATE TEMPORARY TABLE tmp_zanarez (sifobj int(3) NOT NULL, sifra int(6) NOT NULL, kolicina double(15,3) default 0, primary key (sifobj, sifra)) ENGINE=MEMORY;
  INSERT into tmp_zanarez SELECT sifobj,sifra,SUM(kolicina) AS sk FROM fakture FORCE INDEX(ind11)  WHERE (tip='P' or tip='I' or tip='X' or tip='B' or tip='Y' or tip='E') and fakture.status=2 GROUP BY sifobj,sifra HAVING NOT ISNULL(sk);
  UPDATE trstanje set rezervacije=0;
  UPDATE trstanje,tmp_zanarez SET trstanje.rezervacije=tmp_zanarez.kolicina WHERE trstanje.sifobj=tmp_zanarez.sifobj and trstanje.sifra=tmp_zanarez.sifra;
  DROP temporary TABLE if EXISTS tmp_zanarez;
  set @pecav=null;
END
```

---

## 75. sefknjizenjanew

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `sefknjizenjanew`(godina int(4), firma int(4), primljena int(1), imaprethodna int(1), imanaredna int(1))
BEGIN
  DECLARE s_tabela varchar(255);
  DECLARE exit_loop boolean;
  declare godina2 integer;
  declare baza2 varchar(50);
  
  DECLARE dokumenti CURSOR FOR SELECT tabela FROM tmp_tbl_documents;
  declare continue handler for not found set exit_loop = true;

  set @godina1=godina;

  if primljena = 1 then
    drop temporary table if exists tmp_sef_purchase;
    create temporary table tmp_sef_purchase (idfakture int(14) not null primary key, datumslanja date not null, brnal varchar(50), sifraklijenta int(5) not null, biznisoftbrnal varchar(50), index ind1 (datumslanja, brnal, sifraklijenta));
    SET @aa=CONCAT('insert into tmp_sef_purchase select idfakture, datumslanja, brnal, sifraklijenta, null from ',@bsliveid,'biznisoftbinaries.sef_purchase where klijent=',firma,' and (sef_purchase.godina=',godina,' or sef_purchase.godina=',godina-1,' or sef_purchase.godina=',godina+1,')');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  else
    drop temporary table if exists tmp_sef_sales;
    create temporary table tmp_sef_sales (idfakture int(14) not null primary key, datumslanja date not null, brnal varchar(50), sifraklijenta int(5) not null, proknjnalog varchar(50), index ind1 (datumslanja, brnal, sifraklijenta));
    SET @aa=CONCAT('insert into tmp_sef_sales select idfakture, datumslanja, brnal, sifraklijenta, null from ',@bsliveid,'biznisoftbinaries.sef_sales where klijent=',firma,' and (sef_sales.godina=',godina,' or sef_sales.godina=',godina-1,' or sef_sales.godina=',godina+1,')');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  end if;

  drop temporary table if exists tmp_tabela;
  create temporary table tmp_tabela(godina int(4) not null, brnal varchar(50) not null, brdok varchar(50) not null default '''', sifdobpar int(5), datumslanja date not null, primary key (godina, brnal, brdok), KEY `ind1` (`brdok`), key `ind2` (`datumslanja`, `brdok`, `sifdobpar`));

  drop temporary table if exists tmp_sef_knjizenja;
  CREATE temporary TABLE `tmp_sef_knjizenja` (
    `godina` int(4) NOT NULL,
    `brnal` varchar(50) NOT NULL,
    `biznisoftbrnal` varchar(50) DEFAULT NULL,
    `operater` varchar(50) DEFAULT NULL,
    `vremeizmene` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `sifdob` int(5) NOT NULL,
    `primljena` int(1) NOT NULL DEFAULT '1',
    `datumslanja` date NOT NULL,
    `tipprovere` int(1) DEFAULT '0',
    PRIMARY KEY (`brnal`,`sifdob`,`datumslanja`,`primljena`)
  );

  DROP temporary table IF EXISTS tmp_tbl_documents;
  CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null primary KEY, naziv varchar(255), tipkljuca int(2));
  if primljena=1 then
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE (tipkljuca=1 or (sifra in ("OD","TR","OS","NR","AR","CR","ED", "PK", "RK"))) and sifra<>"ND" and sifra<>"TB" and sifra<>"TF" and sifra<>"IP" and sifra<>"MP" and sifra<>"UP" and sifra<>"VP" group by tabela');
  else
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE sifra in ("FA","RN","RA","PK","OK","OD") group by tabela');
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;

  
  OPEN dokumenti;
  set exit_loop = false;
  dokumenti_loop:
    LOOP FETCH dokumenti INTO s_tabela;
    IF exit_loop THEN
      LEAVE dokumenti_loop;
    END IF;
    if primljena = 1 then
      if (lower(s_tabela)='tblodobdob') or (lower(s_tabela)='tblpovracaj') then
         SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina,', biznisoftbrnal, brdok, sifkup, datumslanja from ',s_tabela,' group by biznisoftbrnal');
       else
         SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina,',biznisoftbrnal, brdok, dobavljac, datdok from ',s_tabela,' group by biznisoftbrnal');
      end if;
    else
      SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina,',biznisoftbrnal, brdok, sifkup, datumslanja from ',s_tabela,' group by biznisoftbrnal');
    end if;
    PREPARE stmt FROM @aa; EXECUTE stmt;
  END LOOP dokumenti_loop;
  CLOSE dokumenti;

  insert ignore into tmp_tabela select godina, brnal, brrn, if(sifdob=0 and not isnull(pdvplac),pdvplac,sifdob), datum from specexttr group by brrn;
  insert into tmp_sef_knjizenja select godina, brnal, biznisoftbrnal, operater, vremeizmene, sifdob, primljena, datumslanja, 0 from sef_knjizenja;

  
  set baza2 = 'xx';
    if imaprethodna then
      set godina2 = godina-1;
      set baza2 = concat(@bsliveid,'opp',firma,godina2);
    end if;
  set @godina2=godina2;

  if baza2<>'xx' then
    OPEN dokumenti;
    set exit_loop = false;
    dokumenti_loop:
      LOOP FETCH dokumenti INTO s_tabela;
      IF exit_loop THEN
        LEAVE dokumenti_loop;
      END IF;
      if primljena = 1 then
        if (lower(s_tabela)='tblodobdob') or (lower(s_tabela)='tblpovracaj') then
           SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina2,', biznisoftbrnal, brdok, sifkup, datumslanja from ',baza2,'.',s_tabela,' group by biznisoftbrnal');
         else
           SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina2,', biznisoftbrnal, brdok, dobavljac, datdok from ',baza2,'.',s_tabela,' group by biznisoftbrnal');
        end if;
      else
        SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina2,', biznisoftbrnal, brdok, sifkup, datumslanja from ',baza2,'.',s_tabela,' group by biznisoftbrnal');
      end if;
      PREPARE stmt FROM @aa; EXECUTE stmt;
    END LOOP dokumenti_loop;
    CLOSE dokumenti;

    SET @aa=CONCAT('insert ignore into tmp_tabela select ',godina2,', brnal, brrn, if(sifdob=0 and not isnull(pdvplac),pdvplac,sifdob), datum from ',baza2,'.specexttr group by brrn');
    PREPARE stmt FROM @aa; EXECUTE stmt;

    SET @aa=CONCAT('insert ignore into tmp_sef_knjizenja select ',godina2,', brnal, biznisoftbrnal, operater, vremeizmene, sifdob, primljena, datumslanja, 0 from ',baza2,'.sef_knjizenja');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  end if;

  
  set baza2 = 'xx';
  if imanaredna then
    set godina2 = godina+1;
    set baza2 = concat(@bsliveid,'opp',firma,godina2);
  end if;
  
  set @godina2=godina2;
```

---

## 76. sefknjizenjaold

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `sefknjizenjaold`(godina int(4), firma int(4), primljena int(1))
BEGIN
  DECLARE s_tabela varchar(255);
  DECLARE exit_loop boolean;
  DECLARE dokumenti CURSOR FOR SELECT tabela FROM tmp_tbl_documents;
  declare continue handler for not found set exit_loop = true;

  drop temporary table if exists tmp_tabela;
  create temporary table tmp_tabela(brnal varchar(50) not null primary key, brdok varchar(50) default '''', sifdobpar int(5), KEY `ind1` (`brdok`));

  DROP temporary table IF EXISTS tmp_tbl_documents;
  CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null primary KEY, naziv varchar(255), tipkljuca int(2));
  if primljena=1 then
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE (tipkljuca=1 or (sifra in ("OD","TR","OS","NR","AR","CR","ED"))) and sifra<>"ND" and sifra<>"TB" and sifra<>"TF" and sifra<>"IP" and sifra<>"MP" and sifra<>"UP" and sifra<>"VP" group by tabela');
  else
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE sifra in ("FA","RN","RA","PK","OK","OD") group by tabela');
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;

  OPEN dokumenti;
  set exit_loop = false;
  dokumenti_loop:
    LOOP FETCH dokumenti INTO s_tabela;
    IF exit_loop THEN
      LEAVE dokumenti_loop;
    END IF;
    if primljena = 1 then
      if lower(s_tabela)='tblodobdob' then
         SET @aa=CONCAT('insert ignore into tmp_tabela select biznisoftbrnal, brdok, sifkup from ',s_tabela,' group by biznisoftbrnal');
       else
         SET @aa=CONCAT('insert ignore into tmp_tabela select biznisoftbrnal, brdok, dobavljac from ',s_tabela,' group by biznisoftbrnal');
      end if;
    else
      SET @aa=CONCAT('insert ignore into tmp_tabela select biznisoftbrnal, brdok, sifkup from ',s_tabela,' group by biznisoftbrnal');
    end if;
    PREPARE stmt FROM @aa; EXECUTE stmt;
  END LOOP dokumenti_loop;
  CLOSE dokumenti;

  if primljena = 1 then
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_purchase set biznisoftbrnal='''' where sef_purchase.klijent=',firma,' and sef_purchase.godina=',godina);
  else
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_sales set proknjnalog='''' where sef_sales.klijent=',firma,' and sef_sales.godina=',godina);
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;
  if primljena = 1 then
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_purchase,tmp_tabela set sef_purchase.biznisoftbrnal=tmp_tabela.brnal where sef_purchase.klijent=',firma,' and sef_purchase.godina=',godina,' and sef_purchase.brnal=tmp_tabela.brdok and sef_purchase.sifraklijenta=tmp_tabela.sifdobpar');
  else
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_sales,tmp_tabela set sef_sales.proknjnalog=tmp_tabela.brnal where sef_sales.klijent=',firma,' and sef_sales.godina=',godina,' and sef_sales.brnal=tmp_tabela.brdok and sef_sales.sifraklijenta=tmp_tabela.sifdobpar');
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;
  if primljena = 1 then
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_purchase,sef_knjizenja set sef_purchase.biznisoftbrnal=sef_knjizenja.biznisoftbrnal where sef_purchase.klijent=',firma,' and sef_purchase.godina=',godina,' and sef_purchase.brnal=sef_knjizenja.brnal and sef_purchase.sifraklijenta=sef_knjizenja.SIFDOB and sef_knjizenja.primljena = 1');
  else
    SET @aa=CONCAT('update ',@bsliveid,'biznisoftbinaries.sef_sales,sef_knjizenja set sef_sales.proknjnalog=sef_knjizenja.biznisoftbrnal where sef_sales.klijent=',firma,' and sef_sales.godina=',godina,' and sef_sales.brnal=sef_knjizenja.brnal and sef_sales.sifraklijenta=sef_knjizenja.SIFDOB and sef_knjizenja.primljena = 0');
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;
  DROP temporary table IF EXISTS tmp_tbl_documents;
END
```

---

## 77. SpremiZaSimulaciju1

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SpremiZaSimulaciju1`()
BEGIN
  drop temporary table if exists tmp_simulacija_robno; create temporary table tmp_simulacija_robno like robno; alter table tmp_simulacija_robno engine=myisam;
  drop temporary table if exists tmp_simulacija_pk1; create temporary table tmp_simulacija_pk1 like pk1; alter table tmp_simulacija_pk1 engine=myisam;
  drop temporary table if exists tmp_simulacija_finprom; create temporary table tmp_simulacija_finprom like finprom; alter table tmp_simulacija_finprom engine=myisam;
  drop temporary table if exists tmp_simulacija_trgovacka; create temporary table tmp_simulacija_trgovacka like trgovacka; alter table tmp_simulacija_trgovacka engine=myisam;
  drop temporary table if exists tmp_simulacija_popdv_promet; create temporary table tmp_simulacija_popdv_promet like popdv_promet; alter table tmp_simulacija_popdv_promet engine=myisam;
  drop temporary table if exists tmp_simulacija_eeopdv_pojedinacna; create temporary table tmp_simulacija_eeopdv_pojedinacna like eeopdv_pojedinacna; alter table tmp_simulacija_eeopdv_pojedinacna engine=myisam;
  drop temporary table if exists tmp_simulacija_eeopdv_zbirna; create temporary table tmp_simulacija_eeopdv_zbirna like eeopdv_zbirna; alter table tmp_simulacija_eeopdv_zbirna engine=myisam;
  drop temporary table if exists tmp_simulacija_eeppdv_promet; create temporary table tmp_simulacija_eeppdv_promet like eeppdv_promet; alter table tmp_simulacija_eeppdv_promet engine=myisam;
END
```

---

## 78. SpremiZaSimulaciju2

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SpremiZaSimulaciju2`(brnalzasimulaciju varchar(50))
BEGIN
  set @brnalzasimulaciju=brnalzasimulaciju;
  insert into tmp_simulacija_robno select * from robno where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_pk1 select * from pk1 where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_finprom select * from finprom where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_trgovacka select * from trgovacka where brdok=@brnalzasimulaciju;
  insert into tmp_simulacija_popdv_promet select * from popdv_promet where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_eeopdv_pojedinacna select * from eeopdv_pojedinacna where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_eeopdv_zbirna select * from eeopdv_zbirna where brnal=@brnalzasimulaciju;
  insert into tmp_simulacija_eeppdv_promet select * from eeppdv_promet where brnal=@brnalzasimulaciju;
END
```

---

## 79. SpremiZaSimulaciju3

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SpremiZaSimulaciju3`(brnalzasimulaciju varchar(50))
BEGIN
  set @brnalzasimulaciju=brnalzasimulaciju;
  insert into tmp_simulacija_robno select * from robno where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_pk1 select * from pk1 where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_finprom select * from finprom where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_trgovacka select * from trgovacka where brdok like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_popdv_promet select * from popdv_promet where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_eeopdv_pojedinacna select * from eeopdv_pojedinacna where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_eeopdv_zbirna select * from eeopdv_zbirna where brnal like concat(@brnalzasimulaciju,'-%');
  insert into tmp_simulacija_eeppdv_promet select * from eeppdv_promet where brnal like concat(@brnalzasimulaciju,'-%');
END
```

---

## 80. SrediAmortizaciju

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediAmortizaciju`(zagodinu integer)
BEGIN
  SET @srediamzagodinu = zagodinu;
  
  UPDATE osnabvr SET datsadvra=null;
  
  UPDATE osnabvr, (SELECT osoznaka, invbroj, datumod, max(datam) AS datam from osamvr GROUP by osoznaka, invbroj, datumod) AS mymax SET datsadvra=mymax.datam
     WHERE osnabvr.osoznaka=mymax.osoznaka AND osnabvr.invbroj=mymax.invbroj and osnabvr.datsadvr=mymax.datumod AND mymax.datam>ADDDATE(datsadvr, INTERVAL -1 day) AND NOT ISNULL(mymax.datam) AND YEAR(mymax.datumod)=@srediamzagodinu;
  
  UPDATE osnabvr, (SELECT osoznaka, invbroj, max(datam) AS datam from osamvr GROUP by osoznaka, invbroj) AS mymax SET datsadvra=mymax.datam
     WHERE osnabvr.osoznaka=mymax.osoznaka AND osnabvr.invbroj=mymax.invbroj and mymax.datam>ADDDATE(datsadvr, INTERVAL -1 day) AND NOT ISNULL(mymax.datam) and isnull(osnabvr.datsadvra);
  
  UPDATE osnabvr SET datsadvra=ADDDATE(datsadvr, INTERVAL -1 day) where isnull(datsadvra);
END
```

---

## 81. SrediSpecSerbr

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediSpecSerbr`(mybrnal varchar(50), mytabela varchar(50), jesteizlaz integer, myobj2 integer, mydatum date, mydatdok date, cistbrojnaloga varchar(50))
BEGIN
  declare brnalorbsbrnal varchar(20);
  declare ulazorizlaz varchar(100);
  set @novibrnalserbr=mybrnal;
  set brnalorbsbrnal = 'biznisoftbrnal';
  set ulazorizlaz = '';
  if (mytabela = 'transfmat') then
    set brnalorbsbrnal = 'brnal';
    set ulazorizlaz = ' and not (spec_serbr.izlaz=0) ';
  end if;
  if (mytabela = 'tblrobtransf') then   
    set ulazorizlaz = ' and not (spec_serbr.ulaz=0) ';
  end if;
  mojaprocedura: 
  BEGIN
    SET @full_error := '';
    set @serbrgreska  := '';

    
    select sifra into @nebitno from spec_serbr where brnal=cistbrojnaloga limit 1;
    if found_rows()<1 then
      SET @qvr=concat("select artikli.sifra into @nebitno from ", mytabela,", artikli where ", mytabela,".",brnalorbsbrnal,"='", cistbrojnaloga,"' and ", mytabela,".sifra=artikli.sifra and artikli.serbr>0 limit 1");
      PREPARE stmt1 FROM @qvr;
      EXECUTE stmt1;
      if found_rows()<1 then
        leave mojaprocedura;   
      end if;    
    end if;   

  
    
    select spec_serbr.sifra into @greskasifraserbr from spec_serbr left join artikli on spec_serbr.sifra=artikli.sifra where spec_serbr.brnal=cistbrojnaloga and artikli.sifra is null limit 1;
    if found_rows()>0 then
      set @serbrgreska = concat('Šifra ', @greskasifraserbr, ' ne postoji u šifarniku artikla!'); 
      leave mojaprocedura;   
    end if;
    
    select spec_serbr.sifra into @greskasifraserbr from spec_serbr,artikli where spec_serbr.brnal=cistbrojnaloga and spec_serbr.sifra=artikli.sifra and artikli.serbr<1 limit 1;
    if found_rows()>0 then
      set @serbrgreska = concat('Šifra ', @greskasifraserbr, ' se ne vodi po serijskim brojevima!'); 
      leave mojaprocedura;   
    end if;
    
    SET @qvr=concat("select spec_serbr.sifra into @greskasifraserbr from spec_serbr left join ", mytabela," on ", mytabela,".",brnalorbsbrnal,"=spec_serbr.brnal and spec_serbr.sifra=", mytabela,".sifra where spec_serbr.brnal='", cistbrojnaloga,"' and ", mytabela,".sifra is null ",ulazorizlaz," limit 1");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    if found_rows()>0 then         
      set @serbrgreska = concat('Šifra ', @greskasifraserbr, ' ne postoji u dokumentu a postoji u specifikaciji serijskih brojeva!'); 
      leave mojaprocedura;   
    end if;

    
    SET @qvr=concat("select ", mytabela,".sifra into @greskasifraserbr from artikli,", mytabela," left join spec_serbr on ", mytabela,".",brnalorbsbrnal,"=spec_serbr.brnal and spec_serbr.sifra=", mytabela,".sifra where ", mytabela,".",brnalorbsbrnal,"='", cistbrojnaloga,"' and ", mytabela,".sifra=artikli.sifra and artikli.serbr>0 and spec_serbr.sifra is null limit 1");
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    if found_rows()>0 then
      set @serbrgreska = concat('Šifra ', @greskasifraserbr, ' ne postoji u specifikaciji serijskih brojeva!'); 
      leave mojaprocedura;   
    end if;

    
    if (jesteizlaz=0) and (left(mybrnal,2)='UK') then 
      SET @qvr=concat("select ", mytabela,".sifra, round(abs(sum(kolicina)),4) as sk, ss.ss1 as sui into @greskasifraserbr,@k1,@k2 from ", mytabela,", (select sifra, round(abs(sum(ulaz)),4) as ss1 from spec_serbr where spec_serbr.brnal='", cistbrojnaloga,"' group by sifra) as ss where  ", mytabela,".",brnalorbsbrnal,"='", cistbrojnaloga,"' and ss.sifra=", mytabela,".sifra group by ", mytabela,".sifra having sk<>sui limit 1");
    else
      SET @qvr=concat("select ", mytabela,".sifra, round(abs(sum(kolicina)),4) as sk, ss.ss1 as sui into @greskasifraserbr,@k1,@k2 from ", mytabela,", (select sifra, round(abs(sum(ulaz-izlaz)),4) as ss1 from spec_serbr where spec_serbr.brnal='", cistbrojnaloga,"' group by sifra) as ss where  ", mytabela,".",brnalorbsbrnal,"='", cistbrojnaloga,"' and ss.sifra=", mytabela,".sifra group by ", mytabela,".sifra having sk<>sui limit 1");
    end if;
    PREPARE stmt1 FROM @qvr;
    EXECUTE stmt1;
    if found_rows()>0 then
      set @serbrgreska = concat('Šifra ', @greskasifraserbr, ': specificirana količina serijskih brojeva nije validna! Potrebno: ',@k1, ', specificirano: ',@k2); 
      leave mojaprocedura;   
    end if;

    
    if jesteizlaz then
      SET @qvr=concat("select spec_serbr.sifra, sum(izlaz-ulaz) as suu, if(isnull(ss.ss1),0,ss.ss1) as sui, spec_serbr.serbr into @greskasifraserbr,@k1,@k2,@k3 from spec_serbr left join (select sifra,serbr,if(isnull(sum(ulaz-izlaz)),0,sum(ulaz-izlaz)) as ss1 from serbr where sifra in (select sifra from ", mytabela," where ", mytabela,".",brnalorbsbrnal,"='", cistbrojnaloga,"' group by sifra) and stornirano=0 group by sifra, serbr) as ss on spec_serbr.sifra=ss.sifra and spec_serbr.serbr=ss.serbr where spec_serbr.brnal='",cistbrojnaloga,"' group by sifra,serbr having sui<suu limit 1");
      PREPARE stmt1 FROM @qvr;
      EXECUTE stmt1;
      if found_rows()>0 then
        set @serbrgreska = concat('Šifra ', @greskasifraserbr, ', serijski broj: ',@k3, ', specificirana količina nema na zalihama! Potrebno: ',@k1,', raspoloživo: ', @k2); 
        leave mojaprocedura;   
      end if;
    end if;

    
    if (jesteizlaz=0) and ((left(mybrnal,2)='UK') or (left(mybrnal,2)='KL') or (left(mybrnal,2)='DK') or (left(mybrnal,2)='KK') or (left(mybrnal,2)='PP') or (left(mybrnal,2)='SS')) then
      select spec_serbr.sifra, spec_serbr.serbr into @greskasifraserbr, @k3 from spec_serbr where brnal=cistbrojnaloga and (not isnull(rok) or rok>0) and rok not in (select rok from serbr where serbr.sifra=spec_serbr.sifra and serbr.serbr=spec_serbr.serbr and stornirano=0) and serbr in (select serbr from serbr where serbr.sifra=spec_serbr.sifra and serbr.serbr=spec_serbr.serbr and (not isnull(rok) or rok>0) and stornirano=0) limit 1;
      if found_rows()>0 then
        set @serbrgreska = concat('Šifra ', @greskasifraserbr, ', serijski broj: ',@k3, ', već postoji serija sa različitim rokom!'); 
        leave mojaprocedura;   
      end if;
    end if;
 
    update spec_serbr set datnal=mydatum, datdok=mydatdok where brnal=cistbrojnaloga;

    if (mytabela = 'transfmat') then   
      insert into serbr select sifobj, sifra,serbr,ulaz,izlaz,@novibrnalserbr,partner,datnal,datdok,brdok,rok,now(),operater,0 from spec_serbr where brnal=cistbrojnaloga and not spec_serbr.izlaz = 0;
    elseif (mytabela = 'tblrobtransf') then   
      insert into serbr select sifobj, sifra,serbr,ulaz,izlaz,@novibrnalserbr,partner,datnal,datdok,brdok,rok,now(),operater,0 from spec_serbr where brnal=cistbrojnaloga and not spec_serbr.ulaz = 0;
    else  
      insert into serbr select sifobj, sifra,serbr,ulaz,izlaz,@novibrnalserbr,partner,datnal,datdok,brdok,rok,now(),operater,0 from spec_serbr where brnal=cistbrojnaloga;
    end if;    
    if myobj2>0 then
       insert into serbr select myobj2,sifra, serbr,izlaz,0,@novibrnalserbr,partner,datnal,datdok,brdok,rok,now(),operater,0 from spec_serbr where brnal=cistbrojnaloga and sifobj<>myobj2;
    end if;   
  END;
END
```

---

## 82. SrediTmpFinprom

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmpFinprom`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;  

  set @param10976 = 1;  
  if param10976=1 then
    set @proverabrnal=null;
    select getosnovnibrnal(brnal) into @originalbrnal from tmp_knj_finprom limit 1;       
    set @aa=concat('select brnal into @proverabrnal from finprom where biznisoftbrnal = "',@originalbrnal,'" and stornirano = 0 limit 1');
    prepare stmt from @aa;
    execute stmt;
    deallocate prepare stmt;
    if not isnull(@proverabrnal) then set @param10976 = 0; end if;
  end if;
  
  if @param10976 = 1 then  
    SET @full_error := '';
    SET @myrbrst := 0;
    SET @prev_brnal := '';
    INSERT INTO finprom SELECT datnal, brnal, datdok, brdok, racun, datval, izndug, iznpot, status, operater, rbrst, vd, dokumveza, mestotr, nosioc, opis, zatvoreno, sifval, izndugval, iznpotval, now(), kepuobj, externidokument, fid1, fid2, fid3, valutaplacanja, datpdv, posljed, komercijalista,0, GetOsnovniBrnal(brnal) FROM (SELECT datnal, brnal, datdok, brdok, racun, datval, round(sum(if(isnull(izndug),0,izndug)),2) as izndug, round(sum(if(isnull(iznpot),0,iznpot)),2) as iznpot, status, operater, vd, dokumveza, mestotr, nosioc, opis, zatvoreno, sifval, round(sum(if(isnull(izndugval),0,izndugval)),2) as izndugval, round(sum(if(isnull(iznpotval),0,iznpotval)),2) as iznpotval, now(), kepuobj, externidokument, fid1, fid2, fid3, valutaplacanja, datpdv, komercijalista, posljed, IF(@prev_brnal = brnal, @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbrst, @prev_brnal := brnal FROM (select * from tmp_knj_finprom ORDER BY brnal, racun ASC, valutaplacanja asc, iznpot asc, izndug asc) as tmp9 group by brnal, racun, brdok, sifval, mestotr, nosioc, datpdv, dokumveza, externidokument, valutaplacanja, posljed ORDER BY brnal, racun ASC, status ASC, brdok ASC) AS tmp;
  end if;
  
  delete from tmp_knj_finprom;
END
```

---

## 83. SrediTmpPopdvPromet

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmpPopdvPromet`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;
  
  set @param10976 = 1;  
  if param10976=1 then    
    set @proverabrnal=null;
    select getosnovnibrnal(brnal) into @originalbrnal from tmp_popdv_promet limit 1;       
    set @aa=concat('select brnal into @proverabrnal from popdv_promet where originalbrnal = "',@originalbrnal,'" and stornirano = 0 and not right(brnal,3)="-RZ" limit 1');
    prepare stmt from @aa;
    execute stmt;
    deallocate prepare stmt;
    if not isnull(@proverabrnal) then set @param10976 = 0; end if;
  end if;

  if @param10976 = 1 then  
    SET @full_error := '';
    SET @myrbrst := 0;
    SET @prev_brnal := '';
    SET @prev_srcpopdvid := '';    
    SET @prev_posebnaid := '';  
    INSERT INTO popdv_promet SELECT brnal, rbr, popdvid, sifpar, brrn, datnal, datdok, datpdv, ukupno, vrednost, osnovicaos, pdvos, osnovicaps, pdvps, operater, now(), 0, opis, pib, osnovica0, ostalipodaci, sifobj, bezodbitka, posebnaid, if(isnull(srcpopdvid) or trim(srcpopdvid)='',popdvid,srcpopdvid) as srcpopdvid, null, null, if(@mypdvuobradi=1,0,1), 0, originalbrnal,0,0,0,0,null,null,null,0,0,0,0,null,'',0,0,null,null,0,0,eeopdv_dokumentstorno,0,0,eeppdv_vrstadokumenta
        FROM (SELECT brnal, popdvid, sifpar, brrn, datnal, datdok, datpdv, eeppdv_vrstadokumenta, sum(ukupno) as ukupno, sum(vrednost) as vrednost, sum(osnovicaos) as osnovicaos, sum(pdvos) as pdvos, sum(osnovicaps) as osnovicaps, sum(pdvps) as pdvps, operater, opis, pib, sum(osnovica0) as osnovica0, ostalipodaci, sifobj, sum(bezodbitka) as bezodbitka, posebnaid, originalbrnal, srcpopdvid,eeopdv_dokumentstorno, IF(((@prev_brnal = brnal)), @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbr, @prev_brnal := brnal, @prev_popdvid := popdvid, @prev_sifpar := sifpar, @prev_brrn := brrn, @prev_posebnaid := posebnaid, @prev_srcpopdvid := srcpopdvid 
        FROM (select * from tmp_popdv_promet order by brnal,popdvid,sifpar,brrn,srcpopdvid,if(bezodbitka<>0,pdvos<>0,0), if(bezodbitka<>0,pdvps<>0,0)) as tmp1_popdv group by brnal,popdvid,sifpar,opis,brrn,sifobj, posebnaid,srcpopdvid, datpdv,if(bezodbitka<>0,pdvos<>0,0), if(bezodbitka<>0,pdvps<>0,0) ORDER BY brnal,popdvid,sifpar,brrn,sifobj, posebnaid,srcpopdvid, datpdv,if(bezodbitka<>0,pdvos<>0,0), if(bezodbitka<>0,pdvps<>0,0)) AS tmp;
  end if;

  delete from tmp_popdv_promet;
END
```

---

## 84. SrediTmpRobno

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmpRobno`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  set @param10976 = 1;  
  if param10976=1 then
    set @proverabrnal=null;
    select getosnovnibrnal(brnal) into @originalbrnal from tmp_robno limit 1;       
    set @aa=concat('select brnal into @proverabrnal from robno where originbrnal = "',@originalbrnal,'" and stornirano = 0 limit 1');    
    prepare stmt from @aa;
    execute stmt;
    deallocate prepare stmt;
    if not isnull(@proverabrnal) then set @param10976 = 0; end if;
  end if;

  if @param10976 = 1 then  
    SET @full_error := '';
    SET @myrbrst := 0;
    SET @prev_brnal := '';
    SET @prev_sifobj := 0;  
    SET @prev_sifra := 0;
    INSERT INTO robno SELECT sifobj, sifra, datum, brnal, ulaz, izlaz, duguje, potrazuje, rbr, cena, nabcena, cenabezpp, cenasapp, prcruc, ddatum, condatddat, subject, posljed, realizacija, rabat, komercijalista, operater, mestotr, nosioc, prernc, fid1, fid2, fid3, fid4, datorigdok, brdok, 0, datumdokumenta, getosnovnibrnal(brnal) 
       FROM (SELECT sifobj, sifra, datum, brnal, sum(ulaz) as ulaz, sum(izlaz) as izlaz, sum(duguje) as duguje, sum(potrazuje) as potrazuje, cena, nabcena, cenabezpp, cenasapp, prcruc, subject, posljed, sum(realizacija) as realizacija, sum(rabat) as rabat, komercijalista, operater, mestotr, nosioc, prernc, fid1, fid2, fid3, fid4, datorigdok, brdok, datumdokumenta, IF(((@prev_sifobj = sifobj) and (@prev_brnal = brnal) and (@prev_sifra=sifra)), @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbr, ddatum, concat(datum,ddatum) as condatddat, @prev_sifobj := sifobj, @prev_brnal := brnal, @prev_sifra := sifra 
         FROM (select * from tmp_robno order by sifobj, brnal, sifra, mestotr, nosioc) as tmp1_robno group by sifobj, brnal, sifra, subject, posljed, brdok, komercijalista, mestotr, nosioc, cena, nabcena, cenabezpp, cenasapp, operater having not (ulaz=0 and izlaz=0 and (brnal not like 'NC%') and (brnal not like 'DN%') and (brnal not like 'KN%') and (subject not like 'NIVELACIJA CENE')  and (posljed<>9998) and (subject like 'P-%')) ORDER BY sifobj ASC, brnal ASC, sifra ASC) AS tmp;
   end if;
  delete from tmp_robno;
END
```

---

## 85. SrediTmpTrgovacka

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmpTrgovacka`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  set @param10976 = 1;  
  if param10976=1 then
    set @proverabrnal=null;
    select getosnovnibrnal(brdok) into @originalbrnal from tmp_trgovacka limit 1;       
    set @aa=concat('select brdok into @proverabrnal from trgovacka where brdok like "',@originalbrnal,'%" and stornirano = 0 limit 1');    
    prepare stmt from @aa;
    execute stmt;
    deallocate prepare stmt;
    if not isnull(@proverabrnal) then set @param10976 = 0; end if;
  end if;
  
  if @param10976 = 1 then
    SET @full_error := '';
    SET @myrbrst := 0;
    SET @prev_objekat := 0;
    SET @prev_status := 0;
    SET @prev_brdok := '';
    INSERT INTO trgovacka SELECT datum, brdok, vd, posp, opis, duguje, potrazuje, datupl, iznzr, objekat, status, now(), operater, zaduzenjesapdv, razduzenjesapdv, brdokdob,   sediste, rbrst, if(@mykepuobradi=1,0,1), 0 FROM (SELECT datum, brdok, vd, posp, opis, sum(if(isnull(duguje),0,duguje)) as duguje, sum(if(isnull(potrazuje),0,potrazuje)) as potrazuje, datupl, sum(if(isnull(iznzr),0,iznzr)) as iznzr, objekat, status, ts, operater, sum(if(isnull(zaduzenjesapdv),0,zaduzenjesapdv)) as zaduzenjesapdv, sum(if(isnull(razduzenjesapdv),0,razduzenjesapdv)) as razduzenjesapdv, brdokdob, sediste, IF(((@prev_objekat = objekat) and (@prev_brdok = brdok) and (@prev_status=status)), @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbrst, @prev_objekat := objekat, @prev_brdok := brdok, @prev_status := status FROM (SELECT * FROM tmp_trgovacka ORDER BY objekat,brdok,status,brdokdob, vd, opis) AS tmporder group by objekat,brdok,brdokdob,status,vd,opis ORDER BY objekat ASC, brdok ASC, status ASC, brdokdob asc) AS tmp where duguje<>0 or potrazuje<>0;
  end if;

  delete from tmp_trgovacka;
END
```

---

## 86. SrediTmp_eeopdv_pojedinacna

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmp_eeopdv_pojedinacna`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  set @param10976 = 1;  




















  if @param10976 = 1 then  

    SET @myrbrst := 0;
    SET @prev_brnal := '';
    INSERT INTO eeopdv_pojedinacna SELECT godina, period, brnal, rbr, pravac, pib, inostrana, tipdok, avansi, datplac, opis, abs(ukupnonaknada), datprom, abs(osnovicaos), abs(osnovicans), abs(pdv), odbitak, poslato, 0, datzak, osnovodabira, povezanidokumenti, otkazano, abs(pdvvs), abs(pdvns), osnovavansa, eksterno, biznisoftbrnal, tipunosa, operater, vremeizmene, tip_prometa, tipvzdokumenta, vezdokod, vezdokdo, brintracuna, potvrdjeno, 0,uslov, status_efakture, status_evidencije,datumnaloga,zakorekciju, brdok,0, null 
       FROM (SELECT godina, period, brnal, pravac, pib, inostrana, tipdok, avansi, datplac, opis, sum(ukupnonaknada) as ukupnonaknada, datprom, sum(osnovicaos) as osnovicaos, sum(osnovicans) as osnovicans, sum(pdv) as pdv, odbitak, poslato, datzak, osnovodabira, povezanidokumenti, otkazano, sum(pdvvs) as pdvvs, sum(pdvns) as pdvns, osnovavansa, eksterno, biznisoftbrnal, tipunosa, operater, vremeizmene, tip_prometa, tipvzdokumenta, vezdokod, vezdokdo, brintracuna, IF(@prev_brnal = brnal, @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbr, @prev_brnal := brnal, potvrdjeno, uslov, status_efakture, status_evidencije,datumnaloga,zakorekciju, brdok 
         FROM (select * from tmp_eeopdv_pojedinacna order by brnal, pravac, inostrana, tipdok, odbitak, osnovodabira, eksterno, tipunosa, tip_prometa, tipvzdokumenta) as tmp1_eeopdv_pojedinacna group by brnal, pravac, inostrana, tipdok, odbitak, osnovodabira, eksterno, tipunosa, tip_prometa, tipvzdokumenta, operater ORDER BY brnal, pravac, inostrana, tipdok, odbitak, osnovodabira, eksterno, tipunosa, tip_prometa, tipvzdokumenta, operater) AS tmp;
   end if;
   delete from tmp_eeopdv_pojedinacna;
END
```

---

## 87. SrediTmp_eeopdv_zbirna

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmp_eeopdv_zbirna`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  set @param10976 = 1;  




















  if @param10976 = 1 then  

    SET @myrbrst := 0;
    SET @prev_brnal := '';
    INSERT INTO eeopdv_zbirna SELECT godina, period, brnal, vrsta, abs(osnovicavs), abs(pdvvs), abs(osnovicans), abs(pdvns), biznisoftbrnal, tipunosa, operater, vremeizmene, potvrdjeno, 0, 0,datpdv,datumevidencije, datumnaloga,zakorekciju, uslov,0, null,0  
       FROM (SELECT godina, period, brnal, vrsta, sum(osnovicavs) as osnovicavs, sum(pdvvs) as pdvvs, sum(osnovicans) as osnovicans, sum(pdvns) as pdvns, biznisoftbrnal, tipunosa, operater, potvrdjeno, vremeizmene,datpdv,datumevidencije,datumnaloga,zakorekciju, uslov, @prev_brnal := brnal
         FROM (select * from tmp_eeopdv_zbirna order by brnal, vrsta) as tmp1_eeopdv_zbirna group by brnal, vrsta,vrstaref ORDER BY brnal, vrsta) AS tmp;
  end if;
  delete from tmp_eeopdv_zbirna;
END
```

---

## 88. SrediTmp_eeppdv_promet

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `SrediTmp_eeppdv_promet`(param10976 int(1))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN 
    GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
       @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
    SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
    SELECT @full_error;
  END;

  set @param10976 = 1;  




















  if @param10976 = 1 then  

    SET @myrbrst := 0;
    SET @prev_brnal := '';
    INSERT INTO eeppdv_promet SELECT godina, period, brnal, vrstaprometa, izvor, osnovicavs, pdvvs, osnovicans, pdvns, biznisoftbrnal, tipunosa, internopravilo, operater, vremeizmene, potvrdjeno, 0, 0, datnal, datdok, datpdv, datprom, datprih, iskazandatum, datevid, opis, idefakture, zakorekciju, sifpar, pib, brdokum, rbr, 0 
       FROM (SELECT godina, period, brnal, vrstaprometa, izvor, sum(osnovicavs) as osnovicavs, sum(pdvvs) as pdvvs, sum(osnovicans) as osnovicans, sum(pdvns) as pdvns, biznisoftbrnal, tipunosa, internopravilo, operater, potvrdjeno, datnal, datdok, datpdv, datprom, datprih, iskazandatum, datevid, opis, idefakture, zakorekciju, sifpar, pib, brdokum, vremeizmene, IF(@prev_brnal = brnal, @myrbrst := @myrbrst + 1, @myrbrst := 1) AS rbr, @prev_brnal := brnal
         FROM (select * from tmp_eeppdv_promet order by brnal, vrstaprometa, izvor, pib, brdokum) as tmp1_eeppdv_promet group by brnal, vrstaprometa, izvor, pib, brdokum ORDER BY brnal, vrstaprometa, izvor, pib, brdokum) AS tmp having (osnovicavs<>0 or osnovicans<>0 or pdvvs<>0 or pdvns<>0);
   end if;
  delete from tmp_eeppdv_promet;
END
```

---

## 89. starostzaliha

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `starostzaliha`(custom3 varchar(10000))
BEGIN
  DECLARE asifobj int(6);
  DECLARE asifra int(6);
  DECLARE astanje double(15,3);
  DECLARE bsifra int(6);
  DECLARE bsifobj int(5);
  DECLARE bdatum date;
  DECLARE bbrnal varchar(20);
  DECLARE bulaz double(15,3);
  DECLARE bizlaz double(15,3);
  DECLARE bsubject varchar(10);
  DECLARE bnabcena double(15,3);
  DECLARE bcenabezpp double(15,2);
  DECLARE bcenasapp double(15,2);
  DECLARE mydone int(1) DEFAULT 0;
  declare nastanju cursor for SELECT tmp_custom1.sifobj, tmp_custom1.sifra, razlika FROM artikli, tmp_custom1 LEFT JOIN (SELECT sifobj, sifra, SUM(ulaz)-SUM(izlaz) AS razlika FROM tmp_custom3 GROUP BY sifobj, sifra) as myrob 
        ON tmp_custom1.sifobj = myrob.sifobj and tmp_custom1.sifra = myrob.sifra WHERE artikli.sifra = tmp_custom1.sifra AND artikli.jeusluga = 0
                            AND artikli.jeambalaza = 0 AND razlika > 0 GROUP BY tmp_custom1.sifobj, tmp_custom1.sifra ORDER BY tmp_custom1.sifobj, tmp_custom1.sifra;
  DECLARE puni CURSOR FOR select sifobj, datum,brnal, sifra, ulaz, subject, nabcena, izlaz, cenabezpp, cenasapp from tmp_custom2 WHERE sifobj=asifobj and sifra = asifra and (ulaz >0 or izlaz<0) order by condatddat DESC; 
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET mydone = 1;
  DROP temporary table IF EXISTS tmp_custom1;
  CREATE TEMPORARY TABLE tmp_custom1 (sifobj int(3), sifra int(6), ulaz double(15,3), izlaz double(15,3));
  INSERT INTO tmp_custom1 SELECT sifobj, sifra, ulaz, izlaz FROM tmp_custom;
  DROP TEMPORARY table IF EXISTS tmp_custom3;
  CREATE TEMPORARY TABLE tmp_custom3 (sifobj int(3), sifra int(6), ulaz double(15,3), izlaz double(15,3));
  SET @qvr = custom3;
  PREPARE stmt1 FROM @qvr;
  EXECUTE stmt1;
  DROP temporary TABLE if EXISTS tmp_custom2;
  CREATE temporary TABLE tmp_custom2 (sifobj int(3), datum date, brnal varchar(20), sifra int(6), ulaz double(15,3), subject varchar(10), nabcena double(15,3), condatddat varchar(50), izlaz double(15,3), cenabezpp double(15,2), cenasapp double(15,2));
  INSERT INTO tmp_custom2 SELECT sifobj, datum, brnal, sifra, ulaz, subject, nabcena, condatddat, izlaz, cenabezpp, cenasapp FROM tmp_custom;
  open nastanju;                          
  DROP TEMPORARY TABLE IF EXISTS tmp_starostzaliha;
  CREATE temporary TABLE tmp_starostzaliha(sifobj int(5), datum date, brnal varchar(20), sifra int(6), ulaz double(15,3), subject varchar(10), nabcena double(15,3), cenabezpp double(15,2), cenasapp double(15,2));
  LOOP1: loop                            
      fetch nastanju into asifobj, asifra, astanje;
      IF mydone=1 THEN
        LEAVE loop1; END IF;
      OPEN puni;
      loop2: LOOP
        FETCH puni INTO bsifobj,bdatum,bbrnal, bsifra,bulaz,bsubject,bnabcena, bizlaz, bcenabezpp, bcenasapp;
        IF mydone=1 THEN
        LEAVE loop2; END IF;
        IF bulaz > 0 then
          IF astanje - bulaz > 0 THEN
           INSERT INTO tmp_starostzaliha VALUES(bsifobj,bdatum,bbrnal,bsifra,bulaz,bsubject,bnabcena, bcenabezpp, bcenasapp);
           SET astanje = astanje - bulaz;
          ELSEIF astanje - bulaz < 0 THEN
           INSERT INTO tmp_starostzaliha VALUES (bsifobj,bdatum,bbrnal,bsifra,astanje,bsubject,bnabcena, bcenabezpp, bcenasapp);
           SET astanje = astanje - bulaz;
         ELSE
           INSERT INTO tmp_starostzaliha VALUES(bsifobj,bdatum,bbrnal,bsifra,bulaz,bsubject,bnabcena, bcenabezpp, bcenasapp);
          SET astanje = astanje - bulaz;
          END IF;
        ELSEIF bizlaz<0 THEN
          IF astanje - bizlaz*(-1) > 0 THEN
           INSERT INTO tmp_starostzaliha VALUES(bsifobj,bdatum,bbrnal,bsifra,bizlaz*(-1),bsubject,bnabcena, bcenabezpp, bcenasapp);
           SET astanje = astanje - bizlaz*(-1);
          ELSEIF astanje - bizlaz*(-1) < 0 THEN
           INSERT INTO tmp_starostzaliha VALUES (bsifobj,bdatum,bbrnal,bsifra,astanje,bsubject,bnabcena, bcenabezpp, bcenasapp);
           SET astanje = astanje - bizlaz*(-1);
         ELSE
           INSERT INTO tmp_starostzaliha VALUES(bsifobj,bdatum,bbrnal,bsifra,bizlaz*(-1),bsubject,bnabcena, bcenabezpp, bcenasapp);
          SET astanje = astanje - bizlaz*(-1);
          END IF;
        END IF;
         
        IF astanje <= 0 then CLOSE puni; leave loop2; END if;
      end loop loop2;
  end loop LOOP1;
  DROP table tmp_custom1;
  DROP table tmp_custom2;
  DROP table tmp_custom3;
END
```

---

## 90. stats4art

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4art`(zafirmu boolean, nadan date, sifobj integer, sifra integer, brnal varchar(50), sifrafirme varchar(100), godina integer, obj2 integer, vrstacene2 varchar(100), partner integer, param11028 boolean, param11029 boolean)
BEGIN
  DECLARE whrobj varchar(100);
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SET whrobj = '';
  SET @mydatum = nadan;
  SET @statbrnal = brnal;
  IF NOT zafirmu THEN
    SET whrobj = concat('sifobj=',sifobj,' and ');
  end IF;
  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4art;
  CREATE TEMPORARY TABLE tmp_stats4art(ukupnoulaz double(15,3) DEFAULT 0, ukupnoizlaz double(15,3) DEFAULT 0, prethned double(15,3) DEFAULT 0, pre2ned double(15,3) DEFAULT 0, pre4ned double(15,3) DEFAULT 0,
    juce double(15,3) DEFAULT 0, prekjuce double(15,3) DEFAULT 0, pre4dana double(15,3) DEFAULT 0, zadnjanabavka date DEFAULT NULL, zadnjaprodaja date DEFAULT NULL,
    fkc double(15,3) DEFAULT 0, zadnab double(15,3) DEFAULT 0, prosnab double(15,3) DEFAULT 0, vpc double(15,3) DEFAULT 0, mpc double(15,3) DEFAULT 0,
    fkc2 double(15,3) DEFAULT 0, zadnab2 double(15,3) DEFAULT 0, prosnab2 double(15,3) DEFAULT 0, vpc2 double(15,3) DEFAULT 0, mpc2 double(15,3) DEFAULT 0,
    prokkol double(15,3) DEFAULT 0, rezervisano double(15,3) DEFAULT 0, neprokkasa double(15,3) DEFAULT 0,
    refobj double(15,3) DEFAULT 0, refobjstanje double(15,3) DEFAULT 0, nazivkupca varchar(255), nazivdobavljaca varchar(255), netocenanab double(15,2) DEFAULT 0, netocenaprod double(15,2) default 0, potvrdjenakol double(15,2) default 0,
    narucenakolobj double(15,2) default 0, narucenakolfirma double(15,2) default 0, stanjeuobj2 double(15,2) default 0, zadnjanabavkakolicina double(15,2) default 0,
    ukupnatezina double(15,2) default 0, ukupnalitraza double(15,2) default 0, ukupnanabvr double(15,2) default 0);

  SET @ukupnoulaz=0;
  SET @ukupnoizlaz=0;
  SET @prethned=0;
  SET @pre2ned=0;
  SET @pre4ned=0;
  SET @juce=0;
  SET @prekjuce=0;
  SET @pre4dana=0;
  SET @fkc=NULL;
  SET @zadnab=NULL;
  SET @prosnab=NULL;
  SET @vpc=NULL;
  SET @mpc=NULL;
  SET @fkc2=NULL;
  SET @zadnab2=NULL;
  SET @prosnab2=NULL;
  SET @vpc2=NULL;
  SET @mpc2=NULL;
  SET @prokkol=0;
  SET @rezervacije=0;
  SET @neprokkasa=0;
  SET @refobjst=0;
  SET @refobjstanje=0;
  SET @zadnjanabavka=NULL;
  SET @zadnjaprodaja=NULL;
  SET @zadnazkup=NULL;
  SET @zadnazdob=NULL;
  SET @myvrstacene2=vrstacene2;
  set @netocenanab=0;
  set @netocenaprod=0;
  set @statpotvrdjeni=0;
  set @statnarucenakolobj=null;
  set @statnarucenakolfirma=null;
  set @stanjeobj2=null;
  set @zadnjanabavkakolicina=0;
  SET @ukupnatezina=0;
  SET @ukupnalitraza=0;
  SET @ukupnanabvr=0;

  IF partner > 0 THEN
    SET @aa=CONCAT('select nabcena into @netocenanab from robno where ',whrobj,' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and subject=concat("P-",lpad(',partner,',5,"0")) and ulaz>0 and stornirano=0 and not brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('select realizacija/izlaz into @netocenaprod from robno where ',whrobj,' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and subject=concat("P-",lpad(',partner,',5,"0")) and izlaz>0 and realizacija>0 and stornirano=0 and not brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  END IF;

  SET @aa=CONCAT('select sum(ulaz), sum(izlaz) into @ukupnoulaz, @ukupnoizlaz from robno where ',whrobj,' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and stornirano=0 and not brnal like "POTVRDJENO%"');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  SET @aa=CONCAT('select sum(izlaz) into @prethned from robno where ',whrobj,' sifra=',sifra,' and datum<="',@mydatum,'" and datum>=adddate("',@mydatum,'", interval -1 week) and brnal<>"',@statbrnal,'" and stornirano=0 and not brnal like "POTVRDJENO%"');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  SET @aa=CONCAT('select sum(izlaz) into @pre4ned from robno where ',whrobj,' sifra=',sifra,' and datum<="',@mydatum,'" and datum>=adddate("',@mydatum,'", interval -4 week) and brnal<>"',@statbrnal,'" and stornirano=0 and not brnal like "POTVRDJENO%"');
  PREPARE stmt FROM @aa; EXECUTE stmt;

  SET @aa=CONCAT('select datum,kupci.naziv,ulaz into @zadnjanabavka,@zadnazdob,@zadnjanabavkakolicina from robno,kupci where ',whrobj,' robno.sifra=',sifra,' and kupci.sifra=right(robno.subject,5) and datum<="',@mydatum,'" and ulaz>0 and subject like "P-%" and brnal<>"',@statbrnal,'" and stornirano=0 and not robno.brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  IF isnull(@zadnjanabavka) AND imaproslagodina THEN
    SET @aa=CONCAT('select datum, kupci.naziv,ulaz into @zadnjanabavka,@zadnazdob,@zadnjanabavkakolicina from ',proslagodina,'.robno,kupci where ',whrobj,' robno.sifra=',sifra,' and kupci.sifra=right(robno.subject,5) and datum<="',@mydatum,'" and ulaz>0 and subject like "P-%" and brnal<>"',@statbrnal,'" and stornirano=0 and not robno.brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  end IF;

  SET @aa=CONCAT('select datum,kupci.naziv into @zadnjaprodaja,@zadnazkup from robno,kupci where ',whrobj,' robno.sifra=',sifra,' and kupci.sifra=right(robno.subject,5) and datum<="',@mydatum,'" and izlaz>0 and subject like "P-%" and brnal<>"',@statbrnal,'" and stornirano=0 and not robno.brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
  PREPARE stmt FROM @aa; EXECUTE stmt;
  IF ISNULL(@zadnjanaprodaja) AND imaproslagodina THEN
    SET @aa=CONCAT('select datum,kupci.naziv into @zadnjaprodaja,@zadnazkup from ',proslagodina,'.robno,kupci where ',whrobj,' robno.sifra=',sifra,' and kupci.sifra=right(robno.subject,5) and datum<="',@mydatum,'" and izlaz>0 and subject like "P-%" and brnal<>"',@statbrnal,'" and stornirano=0 and not robno.brnal like "POTVRDJENO%" order by concat(datum,ddatum) desc limit 1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
  END IF;

  SET @aa=CONCAT('select cena, nabcena, cenabezpp, cenasapp,avgPrice(@myvrstacene,',sifobj,',',sifra,',"',@mydatum,'",1) into @fkc, @zadnab,@vpc, @mpc, @prosnab from robno where ',concat('sifobj=',sifobj,' and '),' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and ((ulaz>=0) and (izlaz=0))  and stornirano=0 and not brnal like "POTVRDJENO%" order by concat(datum, ddatum) desc limit 1');
  PREPARE stmt FROM @aa; EXECUTE stmt;

  IF obj2>0 THEN
    SET @aa=CONCAT('select cena, nabcena, cenabezpp, cenasapp,avgPrice(@myvrstacene2,',obj2,',',sifra,',"',@mydatum,'",1) into @fkc2, @zadnab2,@vpc2, @mpc2, @prosnab2 from robno where ',concat('sifobj=',obj2,' and '),' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and ((ulaz>=0) and (izlaz=0))  and stornirano=0 and not brnal like "POTVRDJENO%" order by concat(datum, ddatum) desc limit 1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('select stanje - rezervacije - neprokkasa - refobjst into @stanjeobj2 from trstanje where ',concat('sifobj=',obj2,' and '),' sifra=',sifra);
    PREPARE stmt FROM @aa; EXECUTE stmt;
  end IF;

  if not isnull(@dokbrnal) then
    SET @aa=CONCAT('select sum(ulaz-izlaz) into @prokkol from robno where ',concat('sifobj=',sifobj,' and '),' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and stornirano=0 and not brnal like "POTVRDJENO%" and brnal not in (select pov_brnal from veze where brnal=@dokbrnal and (pov_brnal like "OT%" or pov_brnal like "OA%"))');
  else
    SET @aa=CONCAT('select sum(ulaz-izlaz) into @prokkol from robno where ',concat('sifobj=',sifobj,' and '),' sifra=',sifra,' and datum<="',@mydatum,'" and brnal<>"',@statbrnal,'" and stornirano=0 and not brnal like "POTVRDJENO%"');
  end if;
  PREPARE stmt FROM @aa; EXECUTE stmt;
  set @dokbrnal=null;
  SET @aa=CONCAT('select rezervacije, neprokkasa, refobjst into @rezervacije, @neprokkasa, @refobjst from trstanje where ',concat('sifobj=',sifobj,' and '),' sifra=',sifra);
  PREPARE stmt FROM @aa; EXECUTE stmt;
 
  SET @refobjstanje=null;
  IF NOT ISNULL(@refobjekat) THEN
    set @mynewrefobjekat=null;
  
    SET @aa=CONCAT('select refobj into @mynewrefobjekat from objekti where sifra=',sifobj,' and not isnull(refobj) AND trim(refobj)<>"" AND refobj>0');
    PREPARE stmt FROM @aa; EXECUTE stmt;
```

---

## 91. stats4artgraph

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4artgraph`(zafirmu boolean, nadan date, sifobj integer, sifra integer, sifrafirme varchar(100), godina integer)
BEGIN
  DECLARE whrobj varchar(100);   
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  DECLARE i integer;
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SET whrobj = '';
  SET @mydatum = nadan;
  IF NOT zafirmu THEN
    SET whrobj = concat('sifobj=',sifobj,' and '); 
  end IF;
  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4artgraph;
  CREATE TEMPORARY TABLE tmp_stats4artgraph(mydatum date NOT NULL primary KEY, mesec varchar(30), vred1 double(15,2) DEFAULT 0, vred2 double(15,2) DEFAULT 0, vred3 double(15,2) DEFAULT 0) ENGINE=memory;
  SET i=0;
  myloop: LOOP
    SET @aa=CONCAT('INSERT INTO tmp_stats4artgraph SET mydatum=last_day(date_add(last_day("',@mydatum,'"), interval -',i,' month))');
    SET i := i + 1;
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    IF i<13 THEN
      ITERATE myloop;
    end IF;
    LEAVE myloop;
  end LOOP myloop;
  UPDATE tmp_stats4artgraph SET mesec=CONCAT(GetSrbMonth(mydatum),' ',YEAR(mydatum));

  DROP TEMPORARY TABLE if EXISTS tmp_finx;
  CREATE TEMPORARY TABLE tmp_finx(datumx date not NULL PRIMARY KEY, izndug double(15,2) DEFAULT 0, iznpot double(15,2) DEFAULT 0) ENGINE=memory;
  SET @aa=CONCAT('INSERT ignore INTO tmp_finx SELECT last_day(datum), SUM(ulaz), SUM(izlaz)  from robno where ',whrobj,' sifra=',sifra,' and brnal not like "PST%" and stornirano=0 and not (robno.brnal like "POTVRDJENO%") group by month(datum), year(datum)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  SELECT 0 into @mypocstx;
  IF imaproslagodina THEN
    SET @aa=CONCAT('INSERT ignore INTO tmp_finx SELECT last_day(datum), SUM(ulaz), SUM(izlaz)  from ',proslagodina,'.robno where ',whrobj,' sifra=',sifra,' and stornirano=0 and not (robno.brnal like "POTVRDJENO%") group by month(datum), year(datum)');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  else
    SET @aa=CONCAT('select sum(ulaz-izlaz) from robno where ',whrobj,' sifra=',sifra,' and brnal like "PST%"  and stornirano=0 and not (robno.brnal like "POTVRDJENO%") into @mypocstx');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  end IF;

  SET @aa=CONCAT('update tmp_stats4artgraph, tmp_finx set vred1=tmp_finx.izndug, vred2=tmp_finx.iznpot where mydatum=datumx');
  PREPARE stmt FROM @aa; EXECUTE stmt;  
  SET @aa=CONCAT('update tmp_stats4artgraph set vred3=(select sum(izndug-iznpot)+@mypocstx from tmp_finx where datumx<=mydatum)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  DROP TEMPORARY TABLE if EXISTS tmp_finx;

  update tmp_stats4artgraph SET vred1=0 where ISNULL(vred1);
  update tmp_stats4artgraph SET vred2=0 where ISNULL(vred2);
  update tmp_stats4artgraph SET vred3=0 where ISNULL(vred3);
end
```

---

## 92. stats4kont

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4kont`(nadan date, brnal varchar(50), konto varchar(50), analitika varchar(50))
BEGIN
  SET @mydatum = nadan;
  
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4kont;
  CREATE TEMPORARY TABLE tmp_stats4kont(pdug double(15,2) DEFAULT 0, ppot double(15,2) DEFAULT 0, ndug double(15,2) DEFAULT 0, npot double(15,2) DEFAULT 0,
    apdug double(15,2) DEFAULT 0, appot double(15,2) DEFAULT 0, andug double(15,2) DEFAULT 0, anpot double(15,2) DEFAULT 0);

  SET @pdug=0;
  SET @ppot=0;
  SET @ndug=0;
  SET @npot=0;
  SET @apdug=0;
  SET @appot=0;
  SET @andug=0;
  SET @anpot=0;
  
  SET @aa=CONCAT('select sum(izndug), sum(iznpot) into @pdug, @ppot from finprom where racun="',konto,'"  and datnal<="',@mydatum,'" and brnal<>"',brnal,'" and (status=9 or status=2) and stornirano=0');
  PREPARE stmt FROM @aa; EXECUTE stmt;  
  SET @aa=CONCAT('select sum(izndug), sum(iznpot) into @ndug, @npot from finprom where racun="',konto,'"  and brnal="',brnal,'" and stornirano=0');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  IF not (TRIM(analitika)='') then
    SET @aa=CONCAT('select sum(izndug), sum(iznpot) into @apdug, @appot from finprom where racun="',konto,'" and brdok="',analitika,'" and datnal<="',@mydatum,'" and brnal<>"',brnal,'" and (status=9 or status=2) and stornirano=0');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    SET @aa=CONCAT('select sum(izndug), sum(iznpot) into @andug, @anpot from finprom where racun="',konto,'" and brdok="',analitika,'" and brnal="',brnal,'" and stornirano=0');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  END IF;
  
  INSERT INTO tmp_stats4kont SET 
     pdug=IF(ISNULL(@pdug),0, @pdug),
     ppot=IF(ISNULL(@ppot),0, @ppot),
     ndug=IF(ISNULL(@ndug),0, @ndug),
     npot=IF(ISNULL(@npot),0, @npot),
     apdug=IF(ISNULL(@apdug),0, @apdug),
     appot=IF(ISNULL(@appot),0, @appot),
     andug=IF(ISNULL(@andug),0, @andug),
     anpot=IF(ISNULL(@anpot),0, @anpot);
END
```

---

## 93. stats4kontgraph

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4kontgraph`(nadan date, konto varchar(50), analitika varchar(50), sifrafirme varchar(100), godina integer)
sp: BEGIN
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  DECLARE i integer;
  DECLARE whranalitika varchar(50);
  DECLARE mysaldo varchar(100);   
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SET @mydatum = nadan;

  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4kontgraph;
  CREATE TEMPORARY TABLE tmp_stats4kontgraph(mydatum date not null, mesec varchar(30), vred1 double(15,2) DEFAULT 0, vred2 double(15,2) DEFAULT 0, vred3 double(15,2) DEFAULT 0) ENGINE=memory;
  SET i=0;
  myloop: LOOP
    SET @aa=CONCAT('INSERT INTO tmp_stats4kontgraph SET mydatum=last_day(date_add(last_day("',@mydatum,'"), interval -',i,' month))');
    SET i := i + 1;
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    IF i<13 THEN
      ITERATE myloop;
    end IF;
    LEAVE myloop;
  end LOOP myloop;
  UPDATE tmp_stats4kontgraph SET mesec=CONCAT(GetSrbMonth(mydatum),' ',YEAR(mydatum));

  IF TRIM(analitika)='' THEN
    SET whranalitika = '';
  ELSE
    SET whranalitika = concat(' and brdok="',analitika,'" '); 
  END IF;

  SET mysaldo = 'sum(izndug-iznpot)'; 
  SELECT karakter FROM kontniplan WHERE racun=konto AND sifrakpl=@kontniplan INTO @mykarakter;
  IF TRIM(@mykarakter)='1' THEN
    SET mysaldo = 'sum(iznpot-izndug)';
  END IF;
  
  DROP TEMPORARY TABLE if EXISTS tmp_finx;
  CREATE TEMPORARY TABLE tmp_finx(datumx date not NULL PRIMARY KEY, izndug double(15,2) DEFAULT 0, iznpot double(15,2) DEFAULT 0) ENGINE=memory;
  SET @aa=CONCAT('INSERT INTO tmp_finx SELECT last_day(datnal), SUM(izndug), SUM(iznpot)  from finprom where finprom.racun="',konto,'"',whranalitika,' and finprom.status=9 and brnal not like "ZK9999%" and brnal not like "PST%" and brnal not like "FR-2%" group by month(datnal), year(datnal)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  SELECT 0 into @mypocstx;
  IF imaproslagodina THEN
    SET @aa=CONCAT('INSERT INTO tmp_finx SELECT last_day(datnal), SUM(izndug), SUM(iznpot)  from ',proslagodina,'.finprom where finprom.racun="',konto,'"',whranalitika,' and finprom.status=9 and stornirano=0 and brnal not like "ZK9999%" and brnal not like "FR-2%" group by month(datnal), year(datnal)');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  else
    SET @aa=CONCAT('select ',mysaldo,' from finprom where finprom.racun="',konto,'"',whranalitika,' and finprom.status=9 and stornirano=0 and brnal like "PST%" into @mypocstx');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  end IF;

  SET @aa=CONCAT('update tmp_stats4kontgraph, tmp_finx set vred1=tmp_finx.izndug, vred2=tmp_finx.iznpot where mydatum=datumx');
  PREPARE stmt FROM @aa; EXECUTE stmt;  
  SET @aa=CONCAT('update tmp_stats4kontgraph set vred3=(select ',mysaldo,'+@mypocstx from tmp_finx where datumx<=mydatum)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  DROP TEMPORARY TABLE if EXISTS tmp_finx;

  update tmp_stats4kontgraph SET vred1=0 where ISNULL(vred1);
  update tmp_stats4kontgraph SET vred2=0 where ISNULL(vred2);
  update tmp_stats4kontgraph SET vred3=0 where ISNULL(vred3);
end
```

---

## 94. stats4part

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4part`(nadan date, sifra integer, potrazivanja boolean, ndana integer, brnal varchar(50))
BEGIN
  SET @mybrnal=CONCAT('"',brnal,'"');
  SET @mysifrapartnera = sifra;
  SET @ostalolimit = 0;
  SET @dugovanje = 0;
  SET @uzadnjihndana = 0;
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4part;
  CREATE TEMPORARY TABLE tmp_stats4part(ukupno double(15,2) DEFAULT 0, dospelo double(15,2) DEFAULT 0, uzadnjihndana double(15,2) DEFAULT 0, kredlimit double(15,2) DEFAULT 0, ostalolimit double(15,2) DEFAULT 0);

  DROP temporary TABLE IF EXISTS `tmp_accounts`;
  CREATE temporary TABLE `tmp_accounts` (`racun` varchar(20) NOT NULL,PRIMARY KEY (`racun`));
  IF potrazivanja then
    insert into tmp_accounts select tabrac.konto from tabrac,tabrnoperative,kontniplan where kontniplan.sifrakpl=@kontniplan and tabrac.sifrakpl=@kontniplan and tabrnoperative.racun=tabrac.sifra and tabrac.konto=kontniplan.racun and tabrnoperative.status=2 group by tabrac.konto order by tabrnoperative.status, tabrnoperative.racun;
  else
    insert into tmp_accounts select tabrac.konto from tabrac,tabrnoperative,kontniplan where kontniplan.sifrakpl=@kontniplan and tabrac.sifrakpl=@kontniplan and tabrnoperative.racun=tabrac.sifra and tabrac.konto=kontniplan.racun and tabrnoperative.status=1 group by tabrac.konto order by tabrnoperative.status, tabrnoperative.racun;
  END IF;
  
  DROP temporary TABLE IF EXISTS `tmp_customers`;
  CREATE temporary TABLE `tmp_customers` (`brdok` varchar(20) NOT NULL,PRIMARY KEY (`brdok`));
  INSERT INTO tmp_customers set brdok=CONCAT('P-',RIGHT(CONCAT('00000',sifra),5));
  
  call ios(0, 1, nadan, 'datnal', 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,-1);
  drop temporary table if exists tmp_karval;
  create temporary table tmp_karval (sifra int(5), datdok date, brnal varchar(50),brdok varchar(10),dokumveza varchar(50),operater varchar(50),datum date,izndug double(15,2),
        iznpot double(15,2),racun varchar(10),vd varchar(10),datumdokumenta date, externidokument varchar(100), osnovnidokument varchar(100),
         mid int(10) not null primary key auto_increment, index ind21 (sifra), index ind2 (datum,sifra), index ind3 (datum,brnal)) engine=memory;
  insert into tmp_karval select right(brdok,5),tempfinprom.datnal,tempfinprom.brnal,tempfinprom.brdok,tempfinprom.dokumveza,'',if(isnull(valutaplacanja) or valutaplacanja is null or valutaplacanja=0,datdok,valutaplacanja) as dtm, izndug as iznd, iznpot as iznp,
        tempfinprom.racun,'',tempfinprom.datdok, tempfinprom.externidokument,'',null from tempfinprom 
         where (zatvoreno<>'*' OR ISNULL(ZATVORENO)) order by dtm;
  IF potrazivanja THEN
    select sum(iznpot-izndug)*-1 INTO @ukupno from tmp_karval;
    select sum(iznpot-izndug)*-1 INTO @dospelo from tmp_karval WHERE datum<=nadan;
    select sum(izndug-iznpot) INTO @dugovanje from finprom, tmp_accounts, tmp_customers where finprom.status=9 AND tmp_accounts.racun=finprom.racun AND finprom.brdok=tmp_customers.brdok  and brnal<>@mybrnal;
    SELECT kredlimit INTO @kredlimit FROM kupci where kupci.sifra=@mysifrapartnera;
   IF @kredlimit > 0 THEN
      SET @ostalolimit = @kredlimit - @dugovanje;
    ELSE
      SET @ostalolimit = 0;
    END IF;  
    IF ndana > 0 THEN
      select sum(izndug) INTO @uzadnjihndana from tmp_karval where datum<=nadan and datum>=ADDDATE(nadan, INTERVAL ndana*-1 day) and ((izndug<>0) or (iznpot<0));
    end IF;
  ELSE
    select sum(iznpot-izndug) INTO @ukupno from tmp_karval;
    select sum(iznpot-izndug) INTO @dospelo from tmp_karval WHERE datum<=nadan;
  end IF;
  INSERT INTO tmp_stats4part SET ukupno=IF(ISNULL(@ukupno),0, @ukupno), dospelo=IF(ISNULL(@dospelo),0, @dospelo), uzadnjihndana=IF(ISNULL(@uzadnjihndana),0, @uzadnjihndana), kredlimit=IF(ISNULL(@kredlimit),0, @kredlimit), ostalolimit=IF(ISNULL(@ostalolimit),0, @ostalolimit);
END
```

---

## 95. stats4partgraph

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `stats4partgraph`(nadan date, sifra integer, potrazivanja boolean, sifrafirme varchar(100), godina integer)
BEGIN
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  DECLARE myukupno varchar(100);  
  DECLARE myuplate varchar(100);  
  DECLARE mysaldo varchar(100);  
  DECLARE i integer;
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SET @mydatum = nadan;
  SET @mybrdok=CONCAT('P-',RIGHT(CONCAT('00000',sifra),5));

  DROP TEMPORARY TABLE if EXISTS tmp_accounts;
  CREATE temporary TABLE `tmp_accounts` (`racun` varchar(20) NOT NULL,PRIMARY KEY (`racun`));
  IF potrazivanja THEN
    insert into tmp_accounts select tabrac.konto from tabrac,tabrnoperative,kontniplan where kontniplan.sifrakpl=@kontniplan and tabrac.sifrakpl=@kontniplan and tabrnoperative.racun=tabrac.sifra and tabrac.konto=kontniplan.racun and tabrnoperative.status=2 group by tabrac.konto order by tabrnoperative.status, tabrnoperative.racun;
    SET myukupno = 'sum(izndug)'; 
    SET myuplate = 'sum(iznpot)'; 
    SET mysaldo = 'sum(izndug-iznpot)'; 
  END IF;
  IF not potrazivanja then
    insert into tmp_accounts select tabrac.konto from tabrac,tabrnoperative,kontniplan where kontniplan.sifrakpl=@kontniplan and tabrac.sifrakpl=@kontniplan and tabrnoperative.racun=tabrac.sifra and tabrac.konto=kontniplan.racun and tabrnoperative.status=1 group by tabrac.konto order by tabrnoperative.status, tabrnoperative.racun;
    SET myukupno = 'sum(iznpot)'; 
    SET myuplate = 'sum(izndug)'; 
    SET mysaldo = 'sum(iznpot-izndug)'; 
  END IF;

  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  DROP TEMPORARY TABLE IF EXISTS tmp_stats4partgraph;
  CREATE TEMPORARY TABLE tmp_stats4partgraph(mydatum date not null, mesec varchar(30), vred1 double(15,2) DEFAULT 0, vred2 double(15,2) DEFAULT 0, vred3 double(15,2) DEFAULT 0) ENGINE=memory;
  SET i=0;
  myloop: LOOP
    SET @aa=CONCAT('INSERT INTO tmp_stats4partgraph SET mydatum=last_day(date_add(last_day("',@mydatum,'"), interval -',i,' month))');
    SET i := i + 1;
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    IF i<13 THEN
      ITERATE myloop;
    end IF;
    LEAVE myloop;
  end LOOP myloop;
  UPDATE tmp_stats4partgraph SET mesec=CONCAT(GetSrbMonth(mydatum),' ',YEAR(mydatum));

  DROP TEMPORARY TABLE if EXISTS tmp_finx;
  CREATE TEMPORARY TABLE tmp_finx(datumx date not NULL PRIMARY KEY, izndug double(15,2) DEFAULT 0, iznpot double(15,2) DEFAULT 0) ENGINE=memory;
  SET @aa=CONCAT('INSERT INTO tmp_finx SELECT last_day(datnal), ',myukupno,', ',myuplate,' from finprom,tmp_accounts where finprom.racun=tmp_accounts.racun and brdok=@mybrdok and finprom.status=9 and brnal not like "ZK9999%" and brnal not like "FR-2%" and brnal not like "PST%" and stornirano=0 and year(datnal)=',godina,' group by month(datnal), year(datnal)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  SELECT 0 into @mypocstx;
  IF imaproslagodina THEN
    SET @aa=CONCAT('INSERT INTO tmp_finx SELECT last_day(datnal), ',myukupno,', ',myuplate,' from ',proslagodina,'.finprom,tmp_accounts where finprom.racun=tmp_accounts.racun and brdok=@mybrdok and finprom.status=9 and brnal not like "ZK9999%" and brnal not like "FR-2%" and stornirano=0 and year(datnal)=',godina-1,' group by month(datnal), year(datnal)');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  else
    SET @aa=CONCAT('select ',mysaldo,' from finprom,tmp_accounts where finprom.racun=tmp_accounts.racun and brdok=@mybrdok and finprom.status=9 and stornirano=0 and brnal like "PST%" into @mypocstx');
    PREPARE stmt FROM @aa; EXECUTE stmt;  
  end IF;

  SET @aa=CONCAT('update tmp_stats4partgraph, tmp_finx set vred1=tmp_finx.izndug, vred2=tmp_finx.iznpot where mydatum=datumx');
  PREPARE stmt FROM @aa; EXECUTE stmt;  
  SET @aa=CONCAT('update tmp_stats4partgraph set vred3=(select sum(izndug-iznpot)+@mypocstx from tmp_finx where datumx<=mydatum)');
  PREPARE stmt FROM @aa; EXECUTE stmt;  

  DROP TEMPORARY TABLE if EXISTS tmp_finx;

  update tmp_stats4partgraph SET vred1=0 where ISNULL(vred1);
  update tmp_stats4partgraph SET vred2=0 where ISNULL(vred2);
  update tmp_stats4partgraph SET vred3=0 where ISNULL(vred3);
end
```

---

## 96. statskart

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `statskart`(zafirmu boolean, nadan date, sifobj integer, sifra integer, brnal varchar(50), sifrafirme varchar(100), godina integer, tip integer)
BEGIN
  DECLARE whrobj varchar(100);   
  DECLARE imaproslagodina boolean;
  DECLARE proslagodina varchar(100);
  SET proslagodina = '';
  SET imaproslagodina = FALSE;
  SET whrobj = '';
  SET @mydatum = nadan;
  SET @statbrnal = brnal;
  IF NOT zafirmu THEN
    SET whrobj = concat('sifobj=',sifobj,' and '); 
  end IF;
  SELECT COUNT(*) INTO @mydbcounts FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  if @mydbcounts>0 THEN
    SET imaproslagodina = TRUE;
    SET proslagodina = CONCAT(@bsliveid,'opp',sifrafirme,(godina-1));
  END IF;
  drop temporary table if exists tmp_nard1; 
  create temporary table tmp_nard1 (sifobj int(3), sifra int(6) not null, brnal varchar(20) not null, datum date, partner int(5), 
     kolicina double(15,2), cena double(15,2), prcrabat double(15,2), rabat double(15,2), prcruc double(15,2), iznruc double(15,2), cenabezpdv double(15,2), cenasapdv double(15,2), 
     prcakcrab double(15,2), iznakcrab double(15,2), godina int(4) not null, rbrst int(3) not null, mestotr int(6), nosioc int(6), operater varchar(100), vremeizmene datetime, primary key (godina, sifra, brnal, rbrst));
  
  
  IF tip = 1 then 
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('KL',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from kalkulacije where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('DK',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from prodkalkulacije where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('PP',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblpoljoprivreda where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('TS',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblotkupss where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;  
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('UK',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tbluvoz where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt; 
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('TO',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblotkup where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt; 
    IF imaproslagodina THEN
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('KL',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","kalkulacije where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;  
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('DK',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","prodkalkulacije where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;  
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('PP',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblpoljoprivreda where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;  
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('TS',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblotkupss where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;  
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('UK',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tbluvoz where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt; 
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('TO',lpad(sifobj,3,'0'),'-',lpad(brkalk,5,'0')), datum, dobavljac, kolicina, cena, prcrabat, rabat, prcruc, ruc, cenabezpp, cenasapp,0,0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblotkup where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and kolicina>0 and status>1 order by datum desc, brkalk desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt; 
    end IF; 
    ALTER TABLE tmp_nard1 add nazivpartnera varchar(500);
    UPDATE tmp_nard1,kupci SET tmp_nard1.nazivpartnera=kupci.naziv where tmp_nard1.partner=kupci.sifra;
  END if;

  
  IF tip = 2 then 
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('FA',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat+iznakcrab)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, prcakcrab, iznakcrab,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblfaktakcrab where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('RN',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)),cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from fakture where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('DF',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblprodfakture where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('ZZ',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from tblizvoz where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
    PREPARE stmt FROM @aa; EXECUTE stmt;
    IF imaproslagodina THEN
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('FA',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat+iznakcrab)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, prcakcrab, iznakcrab,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblfaktakcrab where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('RN',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","fakture where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('DF',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblprodfakture where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;
      SET @aa=CONCAT("insert into tmp_nard1 select sifobj,sifra,concat('ZZ',lpad(sifobj,3,'0'),lpad(brrn,6,'0')), datum, sifkup, kolicina, (vredkupac-porezprom+rabat)/kolicina, prcrabat, rabat, 0, razluceni/kolicina, cenakupac/(1+(prcporpr/100)), cenakupac, 0, 0,",godina,",rbrst,mestotr,nosioc,operater,vremeizmene from ",proslagodina,".","tblizvoz where ",whrobj," sifra=",sifra," and datum<='",@mydatum,"' and tip='F' and kolicina>0 and status>1 order by datum desc, brrn desc limit 20");
      PREPARE stmt FROM @aa; EXECUTE stmt;
    end IF;
    ALTER TABLE tmp_nard1 add nazivpartnera varchar(500);
    UPDATE tmp_nard1,kupci SET tmp_nard1.nazivpartnera=kupci.naziv where tmp_nard1.partner=kupci.sifra;
  END IF;

  SET @aa=CONCAT("DELETE FROM tmp_nard1 where brnal='",@statbrnal,"'");
  PREPARE stmt FROM @aa; EXECUTE stmt;
END
```

---

## 97. StornirajKnjizenja

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `StornirajKnjizenja`(brnalstari varchar(50), brnalnovi varchar(50))
BEGIN
  set @brnalstari=brnalstari;
  set @brnalnovi=brnalnovi;

  insert into tmp_storno_robno select * from robno where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_robno set brnal=@brnalnovi, rbr=(@myrbrst := @myrbrst + 1), stornirano=1, operater=@aktivnioperater,ddatum=now(), condatddat=concat(datum,now()), ulaz=ulaz*-1, izlaz=izlaz*-1, duguje=duguje*-1, potrazuje=potrazuje*-1, rabat=rabat*-1, realizacija=realizacija*-1;
  update robno set stornirano=1, ddatum=ddatum where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into robno select * from tmp_storno_robno;

  insert into tmp_storno_trgovacka select * from trgovacka where ((brdok=@brnalstari) or (brdok like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_trgovacka set brdok=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), stornirano=1, operater=@aktivnioperater,ts=now(), duguje=duguje*-1, potrazuje=potrazuje*-1, zaduzenjesapdv=zaduzenjesapdv*-1, razduzenjesapdv=razduzenjesapdv*-1, iznzr=iznzr*-1;
  update trgovacka set stornirano=1, ts=ts where ((brdok=@brnalstari) or (brdok like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into trgovacka select * from tmp_storno_trgovacka;

  insert into tmp_storno_finprom select * from finprom where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;update tmp_storno_finprom set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), stornirano=1, operater=@aktivnioperater,ts=now(), izndug=izndug*-1, iznpot=iznpot*-1,izndugval=izndugval*-1,iznpotval=iznpotval*-1;
  update finprom set stornirano=1, ts=ts where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into finprom select * from tmp_storno_finprom;

  insert into tmp_storno_pk1 select * from pk1 where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;update tmp_storno_pk1 set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), stornirano=1, ppspo=ppspo*-1, ppspn=ppspn*-1,ppbpdv=ppbpdv*-1,ppusp=ppusp*-1,ppubp=ppubp*-1,ppop6369=ppop6369*-1,svegapr=svegapr*-1,pdvobr=pdvobr*-1,pdvpreth=pdvpreth*-1,
    operater=@aktivnioperater,vremeizmene=now(),pdvupl=pdvupl*-1,nabvred=nabvred*-1, vredspr=vredspr*-1,razlucen=razlucen*-1, obrpdv=obrpdv*-1,prodvr=prodvr*-1,trospr=trospr*-1,doprinosi=doprinosi*-1,finrash=finrash*-1,rashodi=rashodi*-1,tekrnupl=tekrnupl*-1,tekrnisp=tekrnisp*-1;
  update pk1 set stornirano=1, vremeizmene=vremeizmene where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into pk1 select * from tmp_storno_pk1;

  insert into tmp_storno_popdv_promet select * from popdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_popdv_promet set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), stornirano=1, srcpopdvid=stornopopdvid(srcpopdvid,ukupno*-1,1), posebnaid=stornopopdvid(posebnaid,ukupno*-1,1),
       operater=@aktivnioperater,ts=now(),ukupno=ukupno*-1,vrednost=vrednost*-1,osnovicaos=osnovicaos*-1,pdvos=pdvos*-1,osnovicaps=osnovicaps*-1,pdvps=pdvps*-1,osnovica0=osnovica0*-1,bezodbitka=bezodbitka*-1;
  update popdv_promet set stornirano=1,eeopdv_dokumentstorno=1, ts=ts where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into popdv_promet select * from tmp_storno_popdv_promet;
  
  delete from eeopdv_pojedinacna where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and status_evidencije=0;
  insert into tmp_storno_eeopdv_pojedinacna select eeopdv_pojedinacna.* from eeopdv_pojedinacna, (select getosnovnibrnal(brnal) as mybrnal,max(if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))) as mymax from eeopdv_pojedinacna where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) group by mybrnal) as maxrecords 
     where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0 and getosnovnibrnal(eeopdv_pojedinacna.brnal)=maxrecords.mybrnal and if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))=maxrecords.mymax;
  update tmp_storno_eeopdv_pojedinacna set brnal=@brnalnovi, stornirano=0,zakorekciju=1,status_evidencije=0, operater=@aktivnioperater,vremeizmene=now(),ukupnonaknada=ukupnonaknada*-1,pdv=pdv*-1,osnovicaos=osnovicaos*-1,pdvvs=pdvvs*-1,osnovicans=osnovicans*-1,pdvns=pdvns*-1;
  insert into eeopdv_pojedinacna select * from tmp_storno_eeopdv_pojedinacna;

  delete from eeopdv_zbirna where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and status_evidencije=0;
  insert into tmp_storno_eeopdv_zbirna select eeopdv_zbirna.* from eeopdv_zbirna, (select getosnovnibrnal(brnal) as mybrnal,max(if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))) as mymax from eeopdv_zbirna where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) group by mybrnal) as maxrecords 
     where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0 and getosnovnibrnal(eeopdv_zbirna.brnal)=maxrecords.mybrnal and if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))=maxrecords.mymax;
  update tmp_storno_eeopdv_zbirna set brnal=@brnalnovi, stornirano=0,zakorekciju=1, status_evidencije=0, operater=@aktivnioperater,vremeizmene=now(), osnovicavs=osnovicavs*-1,pdvvs=pdvvs*-1,osnovicans=osnovicans*-1,pdvns=pdvns*-1;
  insert into eeopdv_zbirna select * from tmp_storno_eeopdv_zbirna;

  delete from eeppdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and status_evidencije=0;
  insert into tmp_storno_eeppdv_promet select eeppdv_promet.* from eeppdv_promet, (select getosnovnibrnal(brnal) as mybrnal,max(if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))) as mymax from eeppdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) group by mybrnal) as maxrecords 
     where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0 and getosnovnibrnal(eeppdv_promet.brnal)=maxrecords.mybrnal and if(locate('/',brnal)>0,concat(left(brnal,locate('/',brnal)-1),'/',lpad(right(brnal,length(brnal)-locate('/',brnal)),5,'0')),concat(brnal,'/00000'))=maxrecords.mymax;
  update tmp_storno_eeppdv_promet set brnal=@brnalnovi, stornirano=0, zakorekciju=1, status_evidencije=0, operater=@aktivnioperater,vremeizmene=now(), osnovicavs=osnovicavs*-1,pdvvs=pdvvs*-1,osnovicans=osnovicans*-1,pdvns=pdvns*-1;
  insert into eeppdv_promet select * from tmp_storno_eeppdv_promet;

  
  insert into tmp_storno_serbr select * from serbr where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  update tmp_storno_serbr set brnal=@brnalnovi, stornirano=1, operater=@aktivnioperater, ulaz=ulaz*-1, izlaz=izlaz*-1;
  update serbr set stornirano=1, vremeizmene=vremeizmene where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  insert into serbr select * from tmp_storno_serbr;
END
```

---

## 98. StornirajKnjizenja3

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `StornirajKnjizenja3`(brnalstari varchar(50), brnalnovi varchar(50), datprom date, datpdv date, datizd date)
BEGIN
  
  set @brnalstari=brnalstari;
  set @brnalnovi=brnalnovi;
  set @storno3datprom=datprom;
  set @storno3datpdv=datpdv;
  set @storno3datizd=datizd;

  insert into tmp_storno_robno select * from robno where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_robno set brnal=@brnalnovi, rbr=(@myrbrst := @myrbrst + 1), operater=@aktivnioperater, ddatum=now(), datum=@storno3datprom, datumdokumenta=@storno3datizd, condatddat=concat(datum,now()), ulaz=ulaz*-1, izlaz=izlaz*-1, duguje=duguje*-1, potrazuje=potrazuje*-1, rabat=rabat*-1, realizacija=realizacija*-1;
  insert into robno select * from tmp_storno_robno;

  insert into tmp_storno_trgovacka select * from trgovacka where ((brdok=@brnalstari) or (brdok like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_trgovacka set brdok=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), operater=@aktivnioperater, ts=now(), datum=@storno3datprom, duguje=duguje*-1, potrazuje=potrazuje*-1, zaduzenjesapdv=zaduzenjesapdv*-1, razduzenjesapdv=razduzenjesapdv*-1, iznzr=iznzr*-1;
  insert into trgovacka select * from tmp_storno_trgovacka;

  insert into tmp_storno_finprom select * from finprom where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;update tmp_storno_finprom set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), operater=@aktivnioperater, ts=now(), datnal=@storno3datprom, datdok=@storno3datizd, datpdv=@storno3datpdv, izndug=izndug*-1, iznpot=iznpot*-1,izndugval=izndugval*-1,iznpotval=iznpotval*-1;
  insert into finprom select * from tmp_storno_finprom;

  insert into tmp_storno_pk1 select * from pk1 where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;update tmp_storno_pk1 set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), datknj=@storno3datprom, datdok=@storno3datizd, ppspo=ppspo*-1, ppspn=ppspn*-1,ppbpdv=ppbpdv*-1,ppusp=ppusp*-1,ppubp=ppubp*-1,ppop6369=ppop6369*-1,svegapr=svegapr*-1,pdvobr=pdvobr*-1,pdvpreth=pdvpreth*-1,
    operater=@aktivnioperater,vremeizmene=now(),pdvupl=pdvupl*-1,nabvred=nabvred*-1, vredspr=vredspr*-1,razlucen=razlucen*-1, obrpdv=obrpdv*-1,prodvr=prodvr*-1,trospr=trospr*-1,doprinosi=doprinosi*-1,finrash=finrash*-1,rashodi=rashodi*-1,tekrnupl=tekrnupl*-1,tekrnisp=tekrnisp*-1;
  insert into pk1 select * from tmp_storno_pk1;

  insert into tmp_storno_popdv_promet select * from popdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0 and not (popdvid='3.9' and posebnaid='3.9.x');
  set @myrbrst=0; update tmp_storno_popdv_promet set brnal=@brnalnovi, rbrst=(@myrbrst := @myrbrst + 1), datnal=@storno3datprom, datdok=@storno3datizd, datpdv=@storno3datpdv, popdvid=stornopopdvid(popdvid,ukupno*-1,0), srcpopdvid=stornopopdvid(srcpopdvid,ukupno*-1,1), posebnaid=stornopopdvid(posebnaid,ukupno*-1,1),
       operater=@aktivnioperater,ts=now(),ukupno=ukupno*-1,vrednost=vrednost*-1,osnovicaos=osnovicaos*-1,pdvos=pdvos*-1,osnovicaps=osnovicaps*-1,pdvps=pdvps*-1,osnovica0=osnovica0*-1,bezodbitka=bezodbitka*-1,eeopdv_def=2,eeopdv_tipprom=7, eeopdv_dokumentstorno=1;
  insert into popdv_promet select * from tmp_storno_popdv_promet;  
  update popdv_promet set stornirano = 1 where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and (popdvid='3.9' and posebnaid='3.9.x');
  update popdv_promet set Ukupno=pdvos+pdvps, osnovicaos=0, osnovicaps=0 where (brnal=@brnalnovi) and left(brnal,2)='RA';
  









  insert into tmp_storno_eeppdv_promet select * from eeppdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  update tmp_storno_eeppdv_promet set brnal=@brnalnovi, operater=@aktivnioperater,vremeizmene=now(), osnovicavs=osnovicavs*-1,pdvvs=pdvvs*-1,osnovicans=osnovicans*-1,pdvns=pdvns*-1;
  insert into eeppdv_promet select * from tmp_storno_eeppdv_promet;  

  
  insert into tmp_storno_serbr select * from serbr where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  update tmp_storno_serbr set brnal=@brnalnovi, operater=@aktivnioperater, datnal=@storno3datprom, datdok=@storno3datizd, ulaz=ulaz*-1, izlaz=izlaz*-1;
  insert into serbr select * from tmp_storno_serbr;
END
```

---

## 99. StornirajKnjizenjaNaDan

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `StornirajKnjizenjaNaDan`(brnalstari varchar(50), brnalnovi varchar(50), nadan Date, nadanpdv Date, datdok Date)
BEGIN
  set @brnalstari=brnalstari;
  set @brnalnovi=brnalnovi;
  set @nadan=nadan;
  set @nadanpdv=nadanpdv;
  set @datdok=datdok;

  insert into tmp_storno_robno select * from robno where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;
  if isnull(@datdok) then
    update tmp_storno_robno set brnal=@brnalnovi, datum=@nadan, rbr=(@myrbrst := @myrbrst + 1), stornirano=0, operater=@aktivnioperater,ddatum=now(), condatddat=concat(datum,now()), ulaz=ulaz*-1, izlaz=izlaz*-1, duguje=duguje*-1, potrazuje=potrazuje*-1, rabat=rabat*-1, realizacija=realizacija*-1;
  else
    update tmp_storno_robno set brnal=@brnalnovi, datum=@nadan, rbr=(@myrbrst := @myrbrst + 1), stornirano=0, operater=@aktivnioperater,ddatum=now(), datumdokumenta=@datdok, condatddat=concat(datum,now()), ulaz=ulaz*-1, izlaz=izlaz*-1, duguje=duguje*-1, potrazuje=potrazuje*-1, rabat=rabat*-1, realizacija=realizacija*-1;
  end if;
  insert into robno select * from tmp_storno_robno;

  insert into tmp_storno_trgovacka select * from trgovacka where ((brdok=@brnalstari) or (brdok like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0; update tmp_storno_trgovacka set brdok=@brnalnovi, datum=@nadan, rbrst=(@myrbrst := @myrbrst + 1), stornirano=0, operater=@aktivnioperater,ts=now(), duguje=duguje*-1, potrazuje=potrazuje*-1, zaduzenjesapdv=zaduzenjesapdv*-1, razduzenjesapdv=razduzenjesapdv*-1, iznzr=iznzr*-1;
  insert into trgovacka select * from tmp_storno_trgovacka;

  insert into tmp_storno_finprom select * from finprom where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;
  if isnull(@datdok) then    
    update tmp_storno_finprom set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, rbrst=(@myrbrst := @myrbrst + 1), stornirano=0, operater=@aktivnioperater,ts=now(), izndug=izndug*-1, iznpot=iznpot*-1,izndugval=izndugval*-1,iznpotval=iznpotval*-1;
  else    
    update tmp_storno_finprom set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, rbrst=(@myrbrst := @myrbrst + 1), stornirano=0, datdok=@datdok, operater=@aktivnioperater,ts=now(), izndug=izndug*-1, iznpot=iznpot*-1,izndugval=izndugval*-1,iznpotval=iznpotval*-1;    
  end if;
  insert into finprom select * from tmp_storno_finprom;

  
  insert into tmp_storno_pk1 select * from pk1 where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  update tmp_storno_pk1 set brnal=@brnalnovi, datknj=@nadan, stornirano=0, ppspo=ppspo*-1, ppspn=ppspn*-1,ppbpdv=ppbpdv*-1,ppusp=ppusp*-1,ppubp=ppubp*-1,ppop6369=ppop6369*-1,svegapr=svegapr*-1,pdvobr=pdvobr*-1,pdvpreth=pdvpreth*-1,
    operater=@aktivnioperater,vremeizmene=now(),pdvupl=pdvupl*-1,nabvred=nabvred*-1, vredspr=vredspr*-1,razlucen=razlucen*-1, obrpdv=obrpdv*-1,prodvr=prodvr*-1,trospr=trospr*-1,doprinosi=doprinosi*-1,finrash=finrash*-1,rashodi=rashodi*-1,tekrnupl=tekrnupl*-1,tekrnisp=tekrnisp*-1;
  insert into pk1 select * from tmp_storno_pk1;

  insert into tmp_storno_popdv_promet select * from popdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  set @myrbrst=0;
  if isnull(@datdok) then
    update tmp_storno_popdv_promet set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, rbrst=(@myrbrst := @myrbrst + 1),eeopdv_dokumentstorno=1, stornirano=0, popdvid=stornopopdvid(popdvid,ukupno*-1,0), srcpopdvid=stornopopdvid(srcpopdvid,ukupno*-1,1), posebnaid=stornopopdvid(posebnaid,ukupno*-1,1),
         operater=@aktivnioperater,ts=now(),ukupno=ukupno*-1,vrednost=vrednost*-1,osnovicaos=osnovicaos*-1,pdvos=pdvos*-1,osnovicaps=osnovicaps*-1,pdvps=pdvps*-1,osnovica0=osnovica0*-1,bezodbitka=bezodbitka*-1, originalbrnal=@brnalnovi;
  else
    update tmp_storno_popdv_promet set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, rbrst=(@myrbrst := @myrbrst + 1),eeopdv_dokumentstorno=1, stornirano=0, datdok=@datdok, popdvid=stornopopdvid(popdvid,ukupno*-1,0), srcpopdvid=stornopopdvid(srcpopdvid,ukupno*-1,1), posebnaid=stornopopdvid(posebnaid,ukupno*-1,1),
         operater=@aktivnioperater,ts=now(),ukupno=ukupno*-1,vrednost=vrednost*-1,osnovicaos=osnovicaos*-1,pdvos=pdvos*-1,osnovicaps=osnovicaps*-1,pdvps=pdvps*-1,osnovica0=osnovica0*-1,bezodbitka=bezodbitka*-1, originalbrnal=@brnalnovi;
  end if;
  insert into popdv_promet select * from tmp_storno_popdv_promet;

  insert into tmp_storno_eeppdv_promet select * from eeppdv_promet where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%')));
  update tmp_storno_eeppdv_promet set stornirano=0;
  update tmp_storno_eeppdv_promet set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, godina=YEAR(@nadanpdv), period=if(@tromesecnipdv=1,QUARTER(@nadanpdv)+20,MONTH(@nadanpdv)), stornirano=1, operater=@aktivnioperater,vremeizmene=now(), vrstaprometa=525, izvor='5.2.5', osnovicavs=0, osnovicans=0, pdvns=abs(pdvns), pdvvs=abs(pdvvs) where stornirano=0 and vrstaprometa in (11,11,12,13,15,21,22,23,25,31,41,511,512,513,514,515,516);
  update tmp_storno_eeppdv_promet set brnal=@brnalnovi, datnal=@nadan, datpdv=@nadanpdv, godina=YEAR(@nadanpdv), period=if(@tromesecnipdv=1,QUARTER(@nadanpdv)+20,MONTH(@nadanpdv)), stornirano=1, operater=@aktivnioperater,vremeizmene=now(), vrstaprometa=516, izvor='5.1.6', osnovicavs=0, osnovicans=0, pdvns=abs(pdvns), pdvvs=abs(pdvvs) where stornirano=0 and vrstaprometa in (14,16,24,26,521,522,523,524,525,526,527);
  delete from tmp_storno_eeppdv_promet where stornirano=0;
  update tmp_storno_eeppdv_promet set stornirano=0;
  insert into eeppdv_promet select * from tmp_storno_eeppdv_promet;

  
  insert into tmp_storno_serbr select * from serbr where ((brnal=@brnalstari) or (brnal like concat(@brnalstari,'/%'))) and stornirano=0;
  update tmp_storno_serbr set brnal=@brnalnovi, stornirano=0, operater=@aktivnioperater, ulaz=ulaz*-1, izlaz=izlaz*-1;
  insert into serbr select * from tmp_storno_serbr;
END
```

---

## 100. trigoperdoc

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `trigoperdoc`()
BEGIN
    DECLARE s_tabela,s_naziv varchar(255);
    DECLARE exit_loop boolean;
    DECLARE s_tipkljuca, i integer;
    DECLARE dokumenti CURSOR FOR SELECT tabela,naziv,tipkljuca FROM tmp_tbl_documents;
    declare continue handler for not found set exit_loop = true;

    SET @trebatriggeri = '';

    DROP temporary table IF EXISTS tmp_tbl_documents;
    CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null primary KEY, naziv varchar(255), tipkljuca int(2));
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE (tipkljuca NOT IN (6,7,8,11,14)) or (tabela="pazari") group by tabela');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''tr_finprom'', naziv=''TROSKOVI'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''frmgk_nefak_spec'', naziv=''FNEFAK'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''proveraprijema'', naziv=''KONTROLNALISTA'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''finprom'', naziv=''FINANSIJSKO'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;

    OPEN dokumenti;
    set exit_loop = false;
    dokumenti_loop: 
      LOOP FETCH dokumenti INTO s_tabela, s_naziv, s_tipkljuca;
      IF exit_loop THEN
        LEAVE dokumenti_loop;
      END IF;
      SET @aa=CONCAT('show triggers where `Trigger`=''operdoc_upd_',s_tabela,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;

      SELECT FOUND_ROWS() INTO i;

      IF i<1 THEN
        SET exit_loop = true;
        SET @trebatriggeri = s_tabela;
        LEAVE dokumenti_loop;
      END IF;

      SET @aa=CONCAT('show triggers where `Trigger`=''operdoc_del_',s_tabela,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;

      SELECT FOUND_ROWS() INTO i;

      IF i<1 THEN
        SET exit_loop = true;
        SET @trebatriggeri = s_tabela;
        LEAVE dokumenti_loop;
      END IF;

      IF s_tipkljuca<5 THEN
        SET @aa=CONCAT('show triggers where `Trigger`=''operdoc_ins_',s_tabela,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
  
        SELECT FOUND_ROWS() INTO i;
  
        IF i<1 THEN
          SET exit_loop = true;
          SET @trebatriggeri = s_tabela;
          LEAVE dokumenti_loop;
        END IF;
      end IF;

    END LOOP dokumenti_loop;
    CLOSE dokumenti;

  END
```

---

## 101. trigoperdocx

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `trigoperdocx`()
BEGIN
    DECLARE s_tabela,s_naziv varchar(255);
    DECLARE exit_loop boolean;
    DECLARE s_tipkljuca, i integer;
    DECLARE dokumenti CURSOR FOR SELECT tabela,naziv,tipkljuca FROM tmp_tbl_documents;
    declare continue handler for not found set exit_loop = true;

    SET @trebatriggeri = '';

    DROP temporary table IF EXISTS tmp_tbl_documents;
    CREATE TEMPORARY TABLE tmp_tbl_documents (tabela varchar(50) not null primary KEY, naziv varchar(255), tipkljuca int(2));
    SET @aa=CONCAT('insert into tmp_tbl_documents select tabela, naziv, tipkljuca from ',@bsliveid,'opp.documents WHERE (tipkljuca NOT IN (6,7,8,11,14)) or (tabela="pazari") group by tabela');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''tr_finprom'', naziv=''TROSKOVI'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''frmgk_nefak_spec'', naziv=''FNEFAK'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''proveraprijema'', naziv=''KONTROLNALISTA'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;
    SET @aa=CONCAT('insert into tmp_tbl_documents set tabela=''finprom'', naziv=''FINANSIJSKO'', tipkljuca=1');
    PREPARE stmt FROM @aa; EXECUTE stmt;

    OPEN dokumenti;
    set exit_loop = false;
    dokumenti_loop: 
      LOOP FETCH dokumenti INTO s_tabela, s_naziv, s_tipkljuca;
      IF exit_loop THEN
        LEAVE dokumenti_loop;
      END IF;
      SET @aa=CONCAT('select n_triger from tmp_trigeri_tabela where n_triger=''operdoc_upd_',s_tabela,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;

      SELECT FOUND_ROWS() INTO i;

      IF i<1 THEN
        SET exit_loop = true;
        SET @trebatriggeri = s_tabela;
        LEAVE dokumenti_loop;
      END IF;

      SET @aa=CONCAT('select n_triger from tmp_trigeri_tabela where n_triger=''operdoc_del_',s_tabela,'''');
      PREPARE stmt FROM @aa; EXECUTE stmt;

      SELECT FOUND_ROWS() INTO i;

      IF i<1 THEN
        SET exit_loop = true;
        SET @trebatriggeri = s_tabela;
        LEAVE dokumenti_loop;
      END IF;

      IF s_tipkljuca<5 THEN
        SET @aa=CONCAT('select n_triger from tmp_trigeri_tabela where n_triger=''operdoc_ins_',s_tabela,'''');
        PREPARE stmt FROM @aa; EXECUTE stmt;
  
        SELECT FOUND_ROWS() INTO i;
  
        IF i<1 THEN
          SET exit_loop = true;
          SET @trebatriggeri = s_tabela;
          LEAVE dokumenti_loop;
        END IF;
      end IF;

    END LOOP dokumenti_loop;
    CLOSE dokumenti;

  END
```

---

## 102. WriteLocation

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `WriteLocation`(`myoznnal` varchar(10), `mybrnal` varchar(50), `myobj` int, `mylistid` int)
BEGIN
  DECLARE MYLOCATION varchar(50);
  DECLARE MYRECCOUNT integer;
  set MYLOCATION := '';
  SET MYRECCOUNT := 0;
  select count(*) into MYRECCOUNT FROM arh_doc_locations WHERE brnal=mybrnal;
  IF MYRECCOUNT<1 THEN
    select locUUID INTO MYLOCATION from arh_active WHERE sifra=myoznnal AND sifobj=myobj;
    IF MYLOCATION='' THEN
      select locUUID INTO MYLOCATION from arh_active WHERE sifra=myoznnal and sifobj=0;
    end if;
    IF MYLOCATION='' THEN
      select arh_list.locUUID INTO MYLOCATION from arh_list,arh_veza WHERE not isnull(arh_veza.listid) and arh_veza.listid=arh_list.listid and not isnull(arh_list.locuuid) and not trim(arh_list.locuuid)='' and arh_veza.sifra=myoznnal;
    end if;
    IF NOT (trim(MYLOCATION)='') THEN
      CALL DoWriteLocation(MYLOCATION, mybrnal, mylistid);
    end if;
  end if;
END
```

---

## 103. xtrstanje

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `xtrstanje`(`so` int,`sa` int,`dt` date)
BEGIN
  DECLARE nc, vc, mc, st, nabcpros DOUBLE;
        DROP TEMPORARY TABLE IF EXISTS tmp_x_trstanje;
  create temporary table tmp_x_trstanje (sifobj int(3) not null, sifra int(6) not null, nabcena double(15,2), vpcena double(15,2), mpcena double(15,2), stanje double(15,3), neprokkasa double(15,3), rezervacije double(15,3), refobjst double(15,3), prosnabcena double(15,2), primary key (sifobj,sifra)) ENGINE=MEMORY;
  IF dt<date(NOW()) or not isnull(@dokbrnal) or not isnull(@ignorisiotpremnice) THEN
    select robno.nabcena, robno.cenabezpp, robno.cenasapp into nc,vc,mc from robno where sifobj=so and robno.sifra=sa and robno.datum<=dt and izlaz=0 and ulaz>=0 and stornirano=0 order by concat(datum,ddatum) desc limit 1;
    if isnull(@ignorisiotpremnice) then
      if not isnull(@dokbrnal) THEN       
        select sum(ulaz-izlaz), avgPrice(@myvrstacene,so,sa,dt,1) INTO st,nabcpros from robno where sifobj=so and robno.sifra=sa and robno.datum<=dt and stornirano=0 and originbrnal not in (SELECT pov_brnal from veze where brnal=@dokbrnal and (pov_brnal like 'OT%' or pov_brnal like 'OA%'));
      ELSE        
        select sum(ulaz-izlaz), avgPrice(@myvrstacene,so,sa,dt,1) INTO st,nabcpros from robno where sifobj=so and robno.sifra=sa and robno.datum<=dt and stornirano=0;
      end if;
    ELSE        
      select sum(ulaz-izlaz), avgPrice(@myvrstacene,so,sa,dt,1) INTO st,nabcpros from robno where sifobj=so and robno.sifra=sa and robno.datum<=dt and stornirano=0 and originbrnal not in (select brnal from tmp_ignotp);
    end if;
    if nc IS NULL THEN SET nc=0; END IF;
    if vc IS NULL THEN SET vc=0; END IF;
    if mc IS NULL THEN SET mc=0; END IF;
    if st IS NULL THEN SET st=0; END IF;
    if nabcpros IS NULL THEN SET nabcpros=0; END IF;
    if nc<0 THEN SET nc=0; END IF;
    if nabcpros<0 THEN SET nabcpros=0; END IF;
    INSERT INTO tmp_x_trstanje SELECT so, sa, nc, vc, mc, st, neprokkasa, rezervacije, refobjst, nabcpros  FROM trstanje where sifobj=so and sifra=sa;
  ELSE
    INSERT INTO tmp_x_trstanje SELECT sifobj, sifra, nabcena, vpcena, mpcena, stanje, neprokkasa, rezervacije, refobjst, avgPrice(@myvrstacene,so,sa,dt,1) FROM trstanje where sifobj=so and sifra=sa;
  END IF;
  set @dokbrnal=null;
END
```

---

## 104. xtrstanjesql

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `xtrstanjesql`(`so` int, `sqltxt` text, `dt` date)
BEGIN
  DECLARE nc, vc, mc, st DOUBLE;
```

---

## 105. ZbirnoPoDokumentu

```sql
CREATE DEFINER=`root`@`localhost` PROCEDURE `ZbirnoPoDokumentu`()
begin

  DROP TEMPORARY TABLE IF EXISTS tmp_dokumveza;
  CREATE TEMPORARY TABLE tmp_dokumveza (racun VARCHAR(20) NOT NULL, brdok VARCHAR(10) NOT NULL, 
                         mestotr INT(6) NOT NULL, nosioc INT(6) NOT NULL, dokumveza VARCHAR(255) NOT NULL, datnal date, datdok date, externidokument varchar(100), valutaplacanja date, posljed int(4), 
                         komercijalista varchar(50), datval date, datpdv date, operater varchar(50), opis varchar(50),
                         brnal VARCHAR(50), PRIMARY KEY (racun, brdok, mestotr, nosioc, dokumveza));
  INSERT INTO tmp_dokumveza SELECT racun, brdok, IF(ISNULL(mestotr), -1, mestotr), IF(ISNULL(nosioc), -1, nosioc), dokumveza, datnal, datdok, externidokument, valutaplacanja, posljed, komercijalista, datval, datpdv, operater, opis, NULL
                            FROM tempfinprom WHERE LENGTH(dokumveza) > 0 GROUP BY racun, brdok, mestotr, nosioc, dokumveza;

  UPDATE tmp_dokumveza, tempfinprom, kontniplan SET tmp_dokumveza.brnal = tempfinprom.brnal, tmp_dokumveza.datnal=tempfinprom.datnal, tmp_dokumveza.datdok=tempfinprom.datdok, tmp_dokumveza.externidokument=tempfinprom.externidokument,
         tmp_dokumveza.valutaplacanja=tempfinprom.valutaplacanja, tmp_dokumveza.posljed=tempfinprom.posljed, tmp_dokumveza.komercijalista=tempfinprom.komercijalista, tmp_dokumveza.datval=tempfinprom.datval, tmp_dokumveza.datpdv=tempfinprom.datpdv,
         tmp_dokumveza.operater=tempfinprom.operater, tmp_dokumveza.opis=tempfinprom.opis
           WHERE tmp_dokumveza.racun = tempfinprom.racun AND 
           tmp_dokumveza.brdok = tempfinprom.brdok AND tmp_dokumveza.mestotr = IF(ISNULL(tempfinprom.mestotr), -1, tempfinprom.mestotr) AND 
           tmp_dokumveza.nosioc = IF(ISNULL(tempfinprom.nosioc), -1, tempfinprom.nosioc) AND tmp_dokumveza.dokumveza = tempfinprom.dokumveza AND 
           tempfinprom.izndug > 0 AND tempfinprom.iznpot = 0 and kontniplan.sifrakpl=@kontniplan and tempfinprom.racun=kontniplan.racun and kontniplan.karakter=0;
  UPDATE tmp_dokumveza, tempfinprom, kontniplan SET tmp_dokumveza.brnal = tempfinprom.brnal, tmp_dokumveza.datnal=tempfinprom.datnal, tmp_dokumveza.datdok=tempfinprom.datdok, tmp_dokumveza.externidokument=tempfinprom.externidokument,
         tmp_dokumveza.valutaplacanja=tempfinprom.valutaplacanja, tmp_dokumveza.posljed=tempfinprom.posljed, tmp_dokumveza.komercijalista=tempfinprom.komercijalista, tmp_dokumveza.datval=tempfinprom.datval, tmp_dokumveza.datpdv=tempfinprom.datpdv,
         tmp_dokumveza.operater=tempfinprom.operater, tmp_dokumveza.opis=tempfinprom.opis
           WHERE tmp_dokumveza.racun = tempfinprom.racun AND 
           tmp_dokumveza.brdok = tempfinprom.brdok AND tmp_dokumveza.mestotr = IF(ISNULL(tempfinprom.mestotr), -1, tempfinprom.mestotr) AND 
           tmp_dokumveza.nosioc = IF(ISNULL(tempfinprom.nosioc), -1, tempfinprom.nosioc) AND tmp_dokumveza.dokumveza = tempfinprom.dokumveza AND 
           tempfinprom.iznpot > 0 AND tempfinprom.izndug = 0 and kontniplan.sifrakpl=@kontniplan and tempfinprom.racun=kontniplan.racun and kontniplan.karakter=1;

  UPDATE tempfinprom, tmp_dokumveza SET tempfinprom.brnal = tmp_dokumveza.brnal, tempfinprom.datnal=tmp_dokumveza.datnal, tempfinprom.datdok=tmp_dokumveza.datdok, tempfinprom.externidokument=tmp_dokumveza.externidokument,
         tempfinprom.posljed=tmp_dokumveza.posljed, tempfinprom.komercijalista=tmp_dokumveza.komercijalista, tempfinprom.datval=tmp_dokumveza.datval, tempfinprom.datpdv=tmp_dokumveza.datpdv,
         tempfinprom.operater=tmp_dokumveza.operater, tempfinprom.opis=tmp_dokumveza.opis
         WHERE tmp_dokumveza.dokumveza = tempfinprom.dokumveza AND
         NOT ISNULL(tmp_dokumveza.brnal) AND LENGTH(tmp_dokumveza.brnal) > 0 AND tmp_dokumveza.racun = tempfinprom.racun AND 
         tmp_dokumveza.brdok = tempfinprom.brdok AND tmp_dokumveza.mestotr = IF(ISNULL(tempfinprom.mestotr), -1, tempfinprom.mestotr) AND 
         tmp_dokumveza.nosioc = IF(ISNULL(tempfinprom.nosioc), -1, tempfinprom.nosioc);

  UPDATE tempfinprom, tmp_dokumveza SET tempfinprom.valutaplacanja = tmp_dokumveza.valutaplacanja
         WHERE tmp_dokumveza.dokumveza = tempfinprom.dokumveza AND
         NOT ISNULL(tmp_dokumveza.brnal) AND LENGTH(tmp_dokumveza.brnal) > 0 AND tmp_dokumveza.racun = tempfinprom.racun AND 
         tmp_dokumveza.brdok = tempfinprom.brdok AND tmp_dokumveza.mestotr = IF(ISNULL(tempfinprom.mestotr), -1, tempfinprom.mestotr) AND 
         tmp_dokumveza.nosioc = IF(ISNULL(tempfinprom.nosioc), -1, tempfinprom.nosioc) and (isnull(tempfinprom.valutaplacanja) or tempfinprom.valutaplacanja=0 or tempfinprom.valutaplacanja<'2000-01-01');
  UPDATE tempfinprom SET valutaplacanja=datdok WHERE isnull(valutaplacanja) or valutaplacanja=0 or valutaplacanja<'2000-01-01';  

  DROP TEMPORARY TABLE IF EXISTS tempfinprom1;
  CREATE TEMPORARY TABLE tempfinprom1 LIKE tempfinprom;
  INSERT INTO tempfinprom1 SELECT tempfinprom.datnal, tempfinprom.brnal, tempfinprom.datdok, tempfinprom.brdok, tempfinprom.racun, 
              tempfinprom.vd, SUM(izndug), SUM(iznpot), tempfinprom.dokumveza, tempfinprom.mestotr, tempfinprom.nosioc, 
              tempfinprom.zatvoreno, tempfinprom.sifval, sum(izndugval), sum(iznpotval), tempfinprom.externidokument,
              tempfinprom.valutaplacanja, tempfinprom.posljed, tempfinprom.komercijalista, tempfinprom.status, tempfinprom.rbrst, 
              tempfinprom.datval, tempfinprom.datval, tempfinprom.operater, tempfinprom.opis, tempfinprom.ts      
              FROM tempfinprom, kontniplan where kontniplan.sifrakpl=@kontniplan and tempfinprom.racun=kontniplan.racun and kontniplan.karakter=0
              GROUP BY tempfinprom.brnal, tempfinprom.racun, tempfinprom.brdok, tempfinprom.mestotr, tempfinprom.nosioc, tempfinprom.dokumveza,valutaplacanja; 
  INSERT INTO tempfinprom1 SELECT tempfinprom.datnal, tempfinprom.brnal, tempfinprom.datdok, tempfinprom.brdok, tempfinprom.racun, 
              tempfinprom.vd, SUM(izndug), SUM(iznpot), tempfinprom.dokumveza, tempfinprom.mestotr, tempfinprom.nosioc, 
              tempfinprom.zatvoreno, tempfinprom.sifval, sum(izndugval), sum(iznpotval), tempfinprom.externidokument,
              tempfinprom.valutaplacanja, tempfinprom.posljed, tempfinprom.komercijalista, tempfinprom.status, tempfinprom.rbrst, 
              tempfinprom.datval, tempfinprom.datval, tempfinprom.operater, tempfinprom.opis, tempfinprom.ts      
              FROM tempfinprom, kontniplan where kontniplan.sifrakpl=@kontniplan and tempfinprom.racun=kontniplan.racun and kontniplan.karakter=1
              GROUP BY tempfinprom.brnal, tempfinprom.racun, tempfinprom.brdok, tempfinprom.mestotr, tempfinprom.nosioc, tempfinprom.dokumveza,valutaplacanja; 
 
  DROP TEMPORARY TABLE IF EXISTS tempfinprom; 
  CREATE TEMPORARY TABLE tempfinprom LIKE tempfinprom1;
  INSERT INTO tempfinprom SELECT * FROM tempfinprom1; 

  DROP TEMPORARY TABLE tempfinprom1;
  DROP TEMPORARY TABLE tmp_dokumveza;
 
end
```

---

