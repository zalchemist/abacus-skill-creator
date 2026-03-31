#!/bin/bash
# =============================================================================
# unzip_and_detect.sh — Raspakivanje ZIP fajla i detekcija SQL dump-ova
# =============================================================================
# Koristi: bash unzip_and_detect.sh <zip_file> [output_dir]
# Primer: bash unzip_and_detect.sh /home/ubuntu/backup.zip /home/ubuntu/db_dumps/
# =============================================================================

ZIP_FILE="$1"
OUTPUT_DIR="${2:-/home/ubuntu/db_dumps}"

if [ -z "$ZIP_FILE" ]; then
    echo "Upotreba: $0 <zip_file> [output_dir]"
    echo "Primer:   $0 /home/ubuntu/backup.zip /home/ubuntu/db_dumps/"
    exit 1
fi

if [ ! -f "$ZIP_FILE" ]; then
    echo "[ERROR] ZIP fajl ne postoji: $ZIP_FILE"
    exit 1
fi

# Instalacija unzip ako nije dostupan
if ! command -v unzip &>/dev/null; then
    echo "[INFO] Instalacija unzip..."
    sudo apt-get install -y unzip -qq
fi

ZIP_SIZE=$(du -h "$ZIP_FILE" | cut -f1)
echo "=== Raspakivanje: $ZIP_FILE ($ZIP_SIZE) ==="
echo "    Destinacija: $OUTPUT_DIR"

# 1. Kreiranje output direktorijuma
mkdir -p "$OUTPUT_DIR"

# 2. Raspakivanje (overwrite bez pitanja)
unzip -o "$ZIP_FILE" -d "$OUTPUT_DIR" 2>/dev/null

# 3. Detekcija SQL dump fajlova
echo ""
echo "=== Pronađeni SQL fajlovi ==="

SQL_FILES=()
while IFS= read -r -d '' file; do
    SQL_FILES+=("$file")
done < <(find "$OUTPUT_DIR" -name "*.sql" -type f -print0 | sort -z)

if [ ${#SQL_FILES[@]} -eq 0 ]; then
    echo "[WARN] Nijedan .sql fajl nije pronađen."
    echo ""
    echo "Svi raspakivani fajlovi:"
    find "$OUTPUT_DIR" -type f -newer "$ZIP_FILE" -o -type f -name "*.sql" | sort
    exit 0
fi

for sql_file in "${SQL_FILES[@]}"; do
    FILE_SIZE=$(du -h "$sql_file" | cut -f1)
    FILE_NAME=$(basename "$sql_file" .sql)

    # Pokušaj detekcije ime baze iz dump-a
    DB_HINT=$(grep -m1 -oP '(?<=CREATE DATABASE.*`)([^`]+)' "$sql_file" 2>/dev/null || \
              grep -m1 -oP '(?<=USE `)([^`]+)' "$sql_file" 2>/dev/null || \
              echo "$FILE_NAME")

    echo "  - $sql_file ($FILE_SIZE) → moguća baza: $DB_HINT"
done

echo ""
echo "Ukupno pronađeno: ${#SQL_FILES[@]} SQL fajl(ova)"
echo ""
echo "Za import koristite:"
for sql_file in "${SQL_FILES[@]}"; do
    DB_NAME=$(basename "$sql_file" .sql)
    echo "  sudo bash import_database.sh \"$sql_file\" \"$DB_NAME\""
done

echo ""
echo "[DONE] Raspakivanje završeno."
