# Biznisoft OPP - Stored Procedures i Funkcije

**Baza:** opp (globalna/master baza sa šifarnicima i definicijama)
**Datum ekstrakcije:** 2026-03-29

---

## Stored Procedures (11)

| # | Naziv | Kreirana | Izmenjena |
|---|-------|----------|-----------|
| 1 | `AutCheckInt` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 2 | `bsnotif` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 3 | `bsnotiftoopers` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 4 | `CheckBsNotifForOper` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 5 | `CheckBsNotification` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 6 | `checkistekugorad` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 7 | `collect_ldstav_ugod` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 8 | `ExportAndDeleteProcedure` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 9 | `fetch_finprom_data_new` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 10 | `fetch_finprom_data_new_z` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |
| 11 | `popuniFirme` | 2026-03-29 15:28:09 | 2026-03-29 15:28:09 |

### Procedura: `AutCheckInt`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE i integer;\n  DECLARE s_firma varchar(50);\n  DECLARE s_operater varchar(50);\n  DECLARE s_sveporuke integer;\n  DECLARE nmybsliveid varchar(50);\n  DECLARE mybaza varchar(50);\n  DECLARE exit_loop boolean;\n  DECLARE cfirme CURSOR FOR SELECT sifrafirme FROM defautint GROUP BY sifrafirme ORDER by sifrafirme;\n  DECLARE coperateri CURSOR FOR SELECT sifrafirme, korime, sveporuke FROM defautint;\n  declare continue handler for not found set exit_loop = true;\n\n  SET nmybsliveid = '';\n  SELECT bsliveid INTO nmybsliveid from mybsliveid LIMIT 1;\n  SELECT bsliveid INTO @bsliveid from mybsliveid LIMIT 1;\n\n  DROP TEMPORARY TABLE IF EXISTS tmp_integritet1x;\n  CREATE TEMPORARY TABLE tmp_integritet1x (sifrafirme varchar(50), nalog varchar(100), tipprovere varchar(500), opis varchar(500), iznos double(15, 2), critical int(1) DEFAULT 0); \n\n  OPEN cfirme;\n  set exit_loop = false;\n  firme_loop: \n    LOOP FETCH cfirme INTO s_firma;\n    IF exit_loop THEN\n      LEAVE firme_loop;\n    END IF;\n\n    SET @qvr4=concat("select sifrakpl into @kontniplan from matpod where sifra=",s_firma);\n    PREPARE stmt14 FROM @qvr4;\n    EXECUTE stmt14;\n    deallocate PREPARE stmt14;\n\n    SET mybaza = CONCAT(nmybsliveid,"opp",s_firma,YEAR(NOW()));\n\n    SET @qvr4=concat("select konto into @r70 from ",mybaza,".tabrac where sifrakpl=@kontniplan and sifra='BSRN0070'");\n    PREPARE stmt14 FROM @qvr4;\n    EXECUTE stmt14;\n    deallocate PREPARE stmt14;\n\n    SET @qvr4=concat("select konto into @r40 from ",mybaza,".tabrac where sifrakpl=@kontniplan and sifra='BSRN0070'");\n    PREPARE stmt14 FROM @qvr4;\n    EXECUTE stmt14;\n    deallocate PREPARE stmt14;\n\n    SET @qvr4=concat("call ",mybaza,".ProveraIntegriteta(MAKEDATE(year(now()),1), date(now()),'",@r70,"','",@r40,"',YEAR(NOW()), true, true, true, true, true, false, true)");\n    PREPARE stmt14 FROM @qvr4;\n    EXECUTE stmt14;\n    deallocate PREPARE stmt14;\n\n    SET @qvr4=concat("insert into tmp_integritet1x select ",s_firma,",tmp_integritet.* from ",mybaza,".tmp_integritet");\n    PREPARE stmt14 FROM @qvr4;\n    EXECUTE stmt14;\n    deallocate PREPARE stmt14;\n\n  END LOOP firme_loop;\n  CLOSE cfirme;\n\n  OPEN coperateri;\n  set exit_loop = false;\n  operateri_loop: \n    LOOP FETCH coperateri INTO s_firma, s_operater, s_sveporuke;\n    IF exit_loop THEN\n      LEAVE operateri_loop;\n    END IF;\n\n    SET @mybssifrafirme = s_firma;\n\n    IF s_sveporuke = 1 then\n      SELECT CONCAT(GROUP_CONCAT(nalog,' ',opis,' - ',iznos SEPARATOR '\\n'), ' ...') INTO @mybsporuka1 FROM tmp_integritet1x WHERE sifrafirme=@mybssifrafirme limit 20;\n    else \n      SELECT CONCAT(GROUP_CONCAT(nalog,' ',opis,' - ',iznos SEPARATOR '\\n'), ' ...') INTO @mybsporuka1 FROM tmp_integritet1x WHERE sifrafirme=@mybssifrafirme AND critical=1 limit 20;\n    END IF;\n\n    IF not (TRIM(@mybsporuka1)='') AND NOT ISNULL(@mybsporuka1) THEN\n      CALL bsnotif(s_operater,CONCAT('Provera integriteta podataka: ','\\n',@mybsporuka1), false, 10007, s_firma);\n    END IF;\n\n  END LOOP operateri_loop;\n  CLOSE coperateri;\n\nEND
```

---

### Procedura: `bsnotif`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  SET @icountnotif := 0;\n  IF checkdate THEN\n    SET @qvr=concat('SELECT COUNT(*) INTO @icountnotif FROM bsnotif WHERE tipporuke=',mytippor,' and operater2="',myoperater,'" and DATE(vremeslanja)=DATE(NOW())');\n    PREPARE stmt1 FROM @qvr;\n    EXECUTE stmt1;\n    deallocate PREPARE stmt1;\n  END IF;\n  IF @icountnotif=0 THEN\n    SET @qvr=concat('INSERT INTO bsnotif SET operater="BizniSoft", operater2="',myoperater,'", mssg="',msg,'", vremeslanja=NOW(), sendertype=1, tipporuke=',mytippor,', zafirmu=', mysifrafirme);\n    PREPARE stmt1 FROM @qvr;\n    EXECUTE stmt1;\n    deallocate PREPARE stmt1;   \n  END IF;\nEND
```

---

### Procedura: `bsnotiftoopers`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE s_operater varchar(50);\n  DECLARE exit_loop boolean;\n  DECLARE coper CURSOR FOR SELECT korime FROM operateri WHERE notifikacije=1;\n  declare continue handler for not found set exit_loop = true;\n\n  OPEN coper;\n  set exit_loop = false;\n  oper_loop: \n    LOOP FETCH coper INTO s_operater;\n    IF exit_loop THEN\n      LEAVE oper_loop;\n    END IF;\n\n    CALL bsnotif(s_operater,msg, checkdate, mytippor, mysifrafirme);\n\n    END LOOP oper_loop;\n    CLOSE coper;\nEND
```

---

### Procedura: `CheckBsNotifForOper`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE i integer;\n\n  \n  SELECT (LENGTH(slika)<1 or ISNULL(LENGTH(slika))) INTO i FROM operateri where upper(korime)=upper(@aktivnioperater);\n  IF i>0 THEN\n    select vremeslanja into @tmpvremeslanja from bsnotif where upper(operater2)=upper(@aktivnioperater) and tipporuke=10005 and vremeslanja>date_sub(NOW(), interval 30 day);\n    if ROW_COUNT()<1 then\n      CALL bsnotif(@aktivnioperater,'Nije postavljena profilna slika. Koristite funkciju PROFIL OPERATERA na glavnoj BizniSoft formi !', true, 10005, -1);\n    end if;\n  END IF;\n\n  \n  SELECT (LENGTH(imeiprezime)<8 or ISNULL(LENGTH(imeiprezime))) INTO i FROM operateri where upper(korime)=upper(@aktivnioperater);\n  IF i>0 THEN\n    select vremeslanja into @tmpvremeslanja from bsnotif where upper(operater2)=upper(@aktivnioperater) and tipporuke=10006 and vremeslanja>date_sub(NOW(), interval 30 day);\n    if ROW_COUNT()<1 then\n      CALL bsnotif(@aktivnioperater,'Nije postavljeno ime i prezime operatera. Ovo možete podesiti u šifarniku operatera ili se obratite administratoru !', true, 10006, -1);\n    end if;\n  END IF;\nEND
```

---

### Procedura: `CheckBsNotification`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE i integer;\n\n  \n  SELECT * FROM INFORMATION_SCHEMA.ENGINES WHERE ENGINE='PERFORMANCE_SCHEMA';\n  SELECT FOUND_ROWS() INTO i;\n  IF i<1 THEN\n    CALL bsnotiftoopers('Sistem za ONLINE analizu parametra baze onemogućen. Uradite dopunu baze prilikom instalacije programa na serveru !', true, 10004, -1);\n  END IF;\nEND
```

---

### Procedura: `checkistekugorad`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE s_operater1 varchar(50);\n  DECLARE s_operater2 varchar(50);\n  DECLARE s_nazivfirme varchar(50);\n  DECLARE s_sifrafirme int;\n  DECLARE s_sif110 varchar(50);\n  DECLARE s_imeiprezime varchar(50);\n  DECLARE s_datumisteka date;\n  DECLARE s_vanro int(1);\n  DECLARE exit_loop boolean;\n  DECLARE coper CURSOR FOR SELECT vanro, sifrafirme, sif110, replace(replace(nazivfirme,"'",' '),'"',' ') as nazivfirme, datumisteka, imeiprezime, operater1, operater2 FROM istekugorad WHERE (DATE(lastchecked)<DATE(NOW()) OR ISNULL(lastchecked)) AND (datediff(DATE(datumisteka),DATE(NOW()))<=@gg_daniisteka AND datediff(DATE(datumisteka),DATE(NOW()))>0);\n  declare continue handler for not found set exit_loop = true;\n\n  SET @gg_daniisteka=brdana;\n\n  OPEN coper;\n  set exit_loop = false;\n  oper_loop: \n    LOOP FETCH coper INTO s_vanro,s_sifrafirme, s_sif110, s_nazivfirme, s_datumisteka, s_imeiprezime, s_operater1, s_operater2;\n    IF exit_loop THEN\n      LEAVE oper_loop;\n    END IF;\n    \n    IF TRIM(s_operater1)<>'' then\n      if s_vanro=1 then\n        CALL bsnotif(s_operater1,CONCAT('Ugovor za lice van RO ', s_sif110, ' - ', s_imeiprezime,' u firmi ', s_sifrafirme, ' - ', s_nazivfirme, ' ističe ', DATE_FORMAT(s_datumisteka, '%d.%m.%Y'),'!'), false, 10010, s_sifrafirme);\n      else\n        CALL bsnotif(s_operater1,CONCAT('Ugovor za radnika ', s_sif110, ' - ', s_imeiprezime,' u firmi ', s_sifrafirme, ' - ', s_nazivfirme, ' ističe ', DATE_FORMAT(s_datumisteka, '%d.%m.%Y'),'!'), false, 10010, s_sifrafirme);\n      end if;      \n    END IF;\n    IF TRIM(s_operater2)<>'' then\n      if s_vanro=1 then\n        CALL bsnotif(s_operater2,CONCAT('Ugovor za lice van RO ', s_sif110, ' - ', s_imeiprezime,' u firmi ', s_sifrafirme, ' - ', s_nazivfirme, ' ističe ', DATE_FORMAT(s_datumisteka, '%d.%m.%Y'),'!'), false, 10010, s_sifrafirme);\n      else\n        CALL bsnotif(s_operater2,CONCAT('Ugovor za radnika ', s_sif110, ' - ', s_imeiprezime,' u firmi ', s_sifrafirme, ' - ', s_nazivfirme, ' ističe ', DATE_FORMAT(s_datumisteka, '%d.%m.%Y'),'!'), false, 10010, s_sifrafirme);\n      end if;      \n    END IF;\n\n\n  END LOOP oper_loop;\n  CLOSE coper;\n  UPDATE istekugorad SET lastchecked=NOW();\nEND
```

---

### Procedura: `collect_ldstav_ugod`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n    DECLARE done INT DEFAULT 0;\n    DECLARE dbName VARCHAR(64);\n    DECLARE table_count INT DEFAULT 0;\n    DECLARE row_count INT DEFAULT 0;\n    DECLARE tempTableCreated TINYINT DEFAULT 0;\n\n    \n    DECLARE dbCursor CURSOR FOR\n        SELECT 'opp6272023' UNION ALL SELECT 'opp6272024'\n        UNION ALL SELECT 'opp6282023' UNION ALL SELECT 'opp6282024'\n        UNION ALL SELECT 'opp6292023' UNION ALL SELECT 'opp6292024'\n        UNION ALL SELECT 'opp6302023' UNION ALL SELECT 'opp6302024'\n        UNION ALL SELECT 'opp6312023' UNION ALL SELECT 'opp6312024'\n        UNION ALL SELECT 'opp6322023' UNION ALL SELECT 'opp6322024'\n        UNION ALL SELECT 'opp6332023' UNION ALL SELECT 'opp6332024'\n        UNION ALL SELECT 'opp6342023' UNION ALL SELECT 'opp6342024'\n        UNION ALL SELECT 'opp6352023' UNION ALL SELECT 'opp6352024'\n        UNION ALL SELECT 'opp6362023' UNION ALL SELECT 'opp6362024'\n        UNION ALL SELECT 'opp6372023' UNION ALL SELECT 'opp6372024'\n        UNION ALL SELECT 'opp6382023' UNION ALL SELECT 'opp6382024'\n        UNION ALL SELECT 'opp6392023' UNION ALL SELECT 'opp6392024'\n        UNION ALL SELECT 'opp6402023' UNION ALL SELECT 'opp6402024'\n        UNION ALL SELECT 'opp6412023' UNION ALL SELECT 'opp6412024'\n        UNION ALL SELECT 'opp6422023' UNION ALL SELECT 'opp6422024'\n        UNION ALL SELECT 'opp6442023' UNION ALL SELECT 'opp6442024'\n        UNION ALL SELECT 'opp6452023' UNION ALL SELECT 'opp6452024'\n        UNION ALL SELECT 'opp6462023' UNION ALL SELECT 'opp6462024'\n        UNION ALL SELECT 'opp6472023' UNION ALL SELECT 'opp6472024'\n        UNION ALL SELECT 'opp6482023' UNION ALL SELECT 'opp6482024'\n        UNION ALL SELECT 'opp6492023' UNION ALL SELECT 'opp6492024'\n        UNION ALL SELECT 'opp6502023' UNION ALL SELECT 'opp6502024'\n        UNION ALL SELECT 'opp6512023' UNION ALL SELECT 'opp6512024'\n        UNION ALL SELECT 'opp6522023' UNION ALL SELECT 'opp6522024'\n        UNION ALL SELECT 'opp6682023' UNION ALL SELECT 'opp6682024'\n        UNION ALL SELECT 'opp6732023' UNION ALL SELECT 'opp6732024'\n        UNION ALL SELECT 'opp6762023' UNION ALL SELECT 'opp6762024'\n        UNION ALL SELECT 'opp6792023' UNION ALL SELECT 'opp6792024'\n        UNION ALL SELECT 'opp6802023' UNION ALL SELECT 'opp6802024'\n        UNION ALL SELECT 'opp6812023' UNION ALL SELECT 'opp6812024'\n        UNION ALL SELECT 'opp6822023' UNION ALL SELECT 'opp6822024'\n        UNION ALL SELECT 'opp6832023' UNION ALL SELECT 'opp6832024'\n        UNION ALL SELECT 'opp6842023' UNION ALL SELECT 'opp6842024'\n        UNION ALL SELECT 'opp6852023' UNION ALL SELECT 'opp6852024'\n        UNION ALL SELECT 'opp6862023' UNION ALL SELECT 'opp6862024'\n        UNION ALL SELECT 'opp6872023' UNION ALL SELECT 'opp6872024'\n        UNION ALL SELECT 'opp6882023' UNION ALL SELECT 'opp6882024'\n        UNION ALL SELECT 'opp6892023' UNION ALL SELECT 'opp6892024'\n        UNION ALL SELECT 'opp6902023' UNION ALL SELECT 'opp6902024'\n        UNION ALL SELECT 'opp6952023' UNION ALL SELECT 'opp6952024'\n        UNION ALL SELECT 'opp6962023' UNION ALL SELECT 'opp6962024'\n        UNION ALL SELECT 'opp7022023' UNION ALL SELECT 'opp7022024'\n        UNION ALL SELECT 'opp7132023' UNION ALL SELECT 'opp7132024'\n        UNION ALL SELECT 'opp7172023' UNION ALL SELECT 'opp7172024';\n\n    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;\n\n    \n    OPEN dbCursor;\n\n    read_loop: LOOP\n        FETCH dbCursor INTO dbName;\n        IF done = 1 THEN\n            LEAVE read_loop;\n        END IF;\n\n        \n        SET @sql = CONCAT(\n            'SET @table_count = (',\n            '  SELECT COUNT(*) FROM information_schema.tables ',\n            '  WHERE table_schema = ''', dbName, ''' ',\n            '    AND table_name = ''ldstav_ugod''',\n            ')'\n        );\n        PREPARE stmt FROM @sql;\n        EXECUTE stmt;\n        DEALLOCATE PREPARE stmt;\n\n        SET table_count = @table_count;\n\n        \n        IF table_count > 0 THEN\n            SET @sql = CONCAT(\n                'SET @row_count = (',\n                '  SELECT COUNT(*) FROM ', dbName, '.ldstav_ugod',\n                ')'\n            );\n            PREPARE stmt FROM @sql;\n            EXECUTE stmt;\n            DEALLOCATE PREPARE stmt;\n\n            SET row_count = @row_count;\n\n            IF row_count > 0 THEN\n                \n                IF tempTableCreated = 0 THEN\n                    DROP TEMPORARY TABLE IF EXISTS temp_result;\n\n                    SET @create_sql = CONCAT(\n                        'CREATE TEMPORARY TABLE temp_result LIKE ', dbName, '.ldstav_ugod'\n                    );\n                    PREPARE stmt FROM @create_sql;\n                    EXECUTE stmt;\n                    DEALLOCATE PREPARE stmt;\n\n                    ALTER TABLE temp_result DROP PRIMARY KEY;\n\n                    ALTER TABLE temp_result\n                        ADD COLUMN izvor_baza VARCHAR(64),\n                        ADD COLUMN naziv_klijenta VARCHAR(255);\n\n                    SET tempTableCreated = 1;\n                END IF;\n\n                \n                SET @sql = CONCAT(\n                    'INSERT INTO temp_result ',\n                    'SELECT t.*,\\n                           ''', dbName, ''' AS izvor_baza,\\n                           ( SELECT naziv FROM opp.matpod ',\n                    '     WHERE sifra = SUBSTRING(''', dbName, ''', 4, LENGTH(''', dbName, ''') - 7) ',\n                    '     LIMIT 1 ',\n                    ') AS naziv_klijenta ',\n                    'FROM ', dbName, '.ldstav_ugod t'\n                );\n                PREPARE stmt FROM @sql;\n                EXECUTE stmt;\n                DEALLOCATE PREPARE stmt;\n            END IF;  \n        END IF;      \n    END LOOP;\n\n    CLOSE dbCursor;\n\n    \n    IF tempTableCreated = 1 THEN\n        SELECT * FROM temp_result;\n    ELSE\n        SELECT 'Nema podataka ni u jednoj bazi.' AS poruka;\n    END IF;\n\nEND
```

---

### Procedura: `ExportAndDeleteProcedure`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n    \n    DECLARE done INT DEFAULT 0;\n    DECLARE db_name VARCHAR(255);\n    DECLARE db_cursor CURSOR FOR SELECT schema_name FROM information_schema.schemata WHERE schema_name IN (\n        'opp5792022', 'opp5792023', 'opp5792024',\n        'opp4742020', 'opp4742021', 'opp4742022', 'opp4742023', 'opp4742024',\n        'opp2592018', 'opp2592019', 'opp2592020', 'opp2592021', 'opp2592022', 'opp2592023',\n        'opp4002018', 'opp4002019', 'opp4002020', 'opp4002021', 'opp4002022', 'opp4002023', 'opp4002024',\n        'opp3722019', 'opp3722020', 'opp3722021', 'opp3722022', 'opp3722023', 'opp3722024',\n        'opp252011', 'opp252012', 'opp252013', 'opp252014', 'opp252015', 'opp252016', 'opp252018', 'opp252019', 'opp252020', 'opp252021', 'opp252022', 'opp252023', 'opp252024',\n        'opp6722013', 'opp6722014', 'opp6722015', 'opp6722017', 'opp6722018', 'opp6722019', 'opp6722020', 'opp6722021', 'opp6722022', 'opp6722023', 'opp6722024',\n        'opp1372015', 'opp1372017', 'opp1372018', 'opp1372019', 'opp1372020', 'opp1372021', 'opp1372022', 'opp1372023', 'opp1372024'\n    );\n    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;\n\n    OPEN db_cursor;\n\n    read_loop: LOOP\n        FETCH db_cursor INTO db_name;\n        IF done THEN\n            LEAVE read_loop;\n        END IF;\n\n        \n        SET @query = CONCAT(\n            'USE ', db_name, '; ', \n            'SELECT * FROM finprom ',\n            'INTO OUTFILE \\''C:/Users/Administrator/Desktop/Exp_imp/finprom/', db_name, '_finprom.csv\\'' ',\n            'FIELDS TERMINATED BY '','' ENCLOSED BY ''"'' LINES TERMINATED BY ''\\n'';'\n        );\n\n        PREPARE stmt FROM @query;\n        EXECUTE stmt;\n        DEALLOCATE PREPARE stmt;\n    END LOOP;\n\n    CLOSE db_cursor;\n\n    \n    SET @drop_query = 'DROP PROCEDURE IF EXISTS ExportAndDeleteProcedure';\n    PREPARE drop_stmt FROM @drop_query;\n    EXECUTE drop_stmt;\n    DEALLOCATE PREPARE drop_stmt;\nEND
```

---

### Procedura: `fetch_finprom_data_new`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE done INT DEFAULT 0;\n  DECLARE db_name CHAR(255);\n  DECLARE db_num INT;\n  DECLARE matpod_naziv VARCHAR(255);\n\n  \n  DECLARE cur CURSOR FOR \n    SELECT schema_name \n    FROM information_schema.schemata \n    WHERE schema_name LIKE '%2022' OR schema_name LIKE '%2023';\n  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;\n\n  \n  \n  DROP TABLE IF EXISTS combined_finprom_data;\n  CREATE TABLE combined_finprom_data (matpod_naziv VARCHAR(255));\n\n  OPEN cur;\n  \n  read_loop: LOOP\n    FETCH cur INTO db_name;\n    \n    IF done THEN\n      LEAVE read_loop;\n    END IF;\n\n    \n    SET db_num = SUBSTRING(db_name, 4, LENGTH(db_name) - 6);\n    \n    \n    SET @s = CONCAT('SELECT naziv INTO @matpod_naziv FROM opp.matpod WHERE SIFRA = ', db_num);\n    PREPARE stmt FROM @s;\n    EXECUTE stmt;\n    DEALLOCATE PREPARE stmt;\n    \n    \n    SET @s = CONCAT('SELECT GROUP_CONCAT(CONCAT('' '',column_name,'' VARCHAR(255) DEFAULT NULL'')) INTO @col_names FROM information_schema.columns WHERE table_schema = ''', db_name, ''' AND table_name = ''finprom''');\n    PREPARE stmt FROM @s;\n    EXECUTE stmt;\n    DEALLOCATE PREPARE stmt;\n\n    \n    SET @s = CONCAT('ALTER TABLE combined_finprom_data ', @col_names);\n    PREPARE stmt FROM @s;\n    EXECUTE stmt;\n    DEALLOCATE PREPARE stmt;\n    \n    \n    SET @s = CONCAT('INSERT INTO combined_finprom_data SELECT "', @matpod_naziv, '", * FROM ', db_name, '.finprom');\n    PREPARE stmt FROM @s;\n    EXECUTE stmt;\n    DEALLOCATE PREPARE stmt;\n  END LOOP;\n  \n  CLOSE cur;\nEND
```

---

### Procedura: `fetch_finprom_data_new_z`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n\tDECLARE\n\t\tdone INT DEFAULT 0;\n\tDECLARE\n\t\tdb_name CHAR ( 255 );\n\tDECLARE\n\t\tdb_num INT;\n\tDECLARE\n\t\tmatpod_naziv VARCHAR ( 255 );\n\tDECLARE\n\t\tcur CURSOR FOR SELECT\n\t\tschema_name \n\tFROM\n\t\tinformation_schema.schemata \n\tWHERE\n\t\tschema_name LIKE '%2023' \n\t\tOR schema_name LIKE '%2024';\n\tDECLARE\n\t\tCONTINUE HANDLER FOR NOT FOUND \n\t\tSET done = 1;\n\n\tDROP TABLE\n\tIF\n\t\tEXISTS combined_finprom_data;\n\tCREATE TABLE combined_finprom_data (\n\tmatpod_naziv VARCHAR ( 255 ));\n\tOPEN cur;\n\tread_loop :\n\tLOOP\n\t\t\tFETCH cur INTO db_name;\n\t\tIF\n\t\t\tdone THEN\n\t\t\t\tLEAVE read_loop;\n\t\t\t\n\t\tEND IF;\n\t\t\n\t\tSET db_num = SUBSTRING( db_name, 4, LENGTH( db_name ) - 6 );\n\t\t\n\t\tSET @s = CONCAT( 'SELECT naziv INTO @matpod_naziv FROM opp.matpod WHERE SIFRA = ', db_num );\n\t\tPREPARE stmt \n\t\tFROM\n\t\t\t@s;\n\t\tEXECUTE stmt;\n\t\tDEALLOCATE PREPARE stmt;\n\t\t\n\t\tSET @s = CONCAT( 'SELECT GROUP_CONCAT(CONCAT('' '',column_name,'' VARCHAR(255) DEFAULT NULL'')) INTO @col_names FROM information_schema.columns WHERE table_schema = ''', db_name, ''' AND table_name = ''finprom''' );\n\t\tPREPARE stmt \n\t\tFROM\n\t\t\t@s;\n\t\tEXECUTE stmt;\n\t\tDEALLOCATE PREPARE stmt;\n\t\t\n\t\tSET @s = CONCAT( 'ALTER TABLE combined_finprom_data ', @col_names );\n\t\tPREPARE stmt \n\t\tFROM\n\t\t\t@s;\n\t\tEXECUTE stmt;\n\t\tDEALLOCATE PREPARE stmt;\n\t\t\n\t\tSET @s = CONCAT( 'INSERT INTO combined_finprom_data SELECT "', @matpod_naziv, '", * FROM ', db_name, '.finprom' );\n\t\tPREPARE stmt \n\t\tFROM\n\t\t\t@s;\n\t\tEXECUTE stmt;\n\t\tDEALLOCATE PREPARE stmt;\n\t\t\n\tEND LOOP;\n\tCLOSE cur;\n\nEND
```

---

### Procedura: `popuniFirme`

- **Kreirana:** 2026-03-29 15:28:09
- **Izmenjena:** 2026-03-29 15:28:09

```sql
BEGIN\n  DECLARE dbname varchar(30);\n  DECLARE godina varchar(4);\n  DECLARE sifra varchar(10);\n  DECLARE done boolean;\n  DECLARE dbCursor CURSOR FOR SELECT * FROM tmp_databases;\n  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;\n  DROP TEMPORARY TABLE IF EXISTS tmp_databases;\n  CREATE TEMPORARY TABLE tmp_databases(dbname varchar(30));\n  set @bsliveidxx=replace(@bsliveid ,'''','');\n  SET @db_bsBinaries = CONCAT('INSERT IGNORE INTO arh_config SET db_name = (SELECT schema_name FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = ''',\n                         @bsliveidxx, 'biznisoftbinaries''), sifra = 0, godina = 1000, kasa = 0, backup = 0, cloud = 0, compress = 0, putanja =', QUOTE(backupDirectory));\n  PREPARE stmt FROM @db_bsBinaries;\n  EXECUTE stmt;\n\n  SET @db_bsBinaries = CONCAT('INSERT IGNORE INTO arh_config SET db_name = (SELECT schema_name FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = ''',\n                         @bsliveidxx, 'bsmails''), sifra = 0, godina = 1002, kasa = 0, backup = 0, cloud = 0, compress = 0, putanja =', QUOTE(backupDirectory));\n  PREPARE stmt FROM @db_bsBinaries;\n  EXECUTE stmt;\n\n  SET @tmpInsert = CONCAT('INSERT INTO tmp_databases SELECT schema_name FROM information_schema.SCHEMATA WHERE (SCHEMA_NAME LIKE ''', @bsliveidxx, 'opp_____%'') or (SCHEMA_NAME LIKE ''', @bsliveidxx, 'opp'') ');\n  PREPARE stmt FROM @tmpInsert;\n  EXECUTE stmt;\n\n  OPEN dbCursor;\n  read_loop : LOOP\n  FETCH dbCursor INTO dbname;\n  IF done THEN\n    LEAVE read_loop;\n  END IF;\n  \n  IF dbname = 'OPP' THEN\n    SET sifra = '0';\n    SET godina = '1001';\n  ELSEIF dbname = 'BSMAILS' THEN\n    SET sifra = '0';\n    SET godina = '1002';\n  ELSE\n    SET sifra = (SELECT TRIM(LEADING 'opp' FROM SUBSTRING(dbname, length(@bsliveidxx)+1, LENGTH(dbname) - length(@bsliveidxx) -4)));\n    SET godina = RIGHT(dbname, 4);\n  END IF;\n\n  SET @dataBases = CONCAT('INSERT IGNORE INTO arh_config SET db_name = ', QUOTE(dbname), ', sifra = ', QUOTE(sifra) , ', godina = ', QUOTE(godina),\n                          ', kasa = 0, backup = 0, cloud = 0, putanja = ', QUOTE(backupDirectory));\n  PREPARE stmt FROM @dataBases;\n  EXECUTE stmt;\n\n  END LOOP read_loop;  \n  CLOSE dbCursor;\nEND
```

---

## Funkcije (1)

### Funkcija: `mod_97_10_check`

- **Return type:** `char(2)`

```sql
return lpad(98 - cast(s as decimal(60)) % 97, 2, '0')
```

---
