#!/bin/bash
# =============================================================================
# import_database.sh — Import SQL dump-a u MariaDB bazu
# =============================================================================
# Koristi: sudo bash import_database.sh <dump_file> <database_name>
# Primer: sudo bash import_database.sh /home/ubuntu/db_dumps/opp.sql opp
# =============================================================================

set -e

DUMP_FILE="$1"
DB_NAME="$2"

if [ -z "$DUMP_FILE" ] || [ -z "$DB_NAME" ]; then
    echo "Upotreba: $0 <dump_file> <database_name>"
    echo "Primer:   $0 /home/ubuntu/db_dumps/opp.sql opp"
    exit 1
fi

if [ ! -f "$DUMP_FILE" ]; then
    echo "[ERROR] Dump fajl ne postoji: $DUMP_FILE"
    exit 1
fi

# Provera da li MariaDB radi
if ! sudo mysqladmin ping &>/dev/null 2>&1; then
    echo "[ERROR] MariaDB nije aktivan. Pokreni setup_mariadb.sh ili restart_mariadb.sh prvo."
    exit 1
fi

DUMP_SIZE=$(du -h "$DUMP_FILE" | cut -f1)
echo "=== Import baze: $DB_NAME ==="
echo "    Dump fajl: $DUMP_FILE ($DUMP_SIZE)"

# 1. Kreiranje baze ako ne postoji
echo "[INFO] Kreiranje baze '$DB_NAME' ako ne postoji..."
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS \`$DB_NAME\` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
echo "[OK] Baza '$DB_NAME' spremna."

# 2. Import sa --force flagom (nastavlja uprkos greškama)
echo "[INFO] Import u toku... (ovo može potrajati)"
START_TIME=$(date +%s)

sudo mysql -u root "$DB_NAME" --force < "$DUMP_FILE" 2>/tmp/import_errors_${DB_NAME}.log

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# 3. Provera rezultata
TABLE_COUNT=$(sudo mysql -u root -N -e "SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_SCHEMA='$DB_NAME';")
echo ""
echo "[OK] Import završen za ${DURATION}s."
echo "     Baza: $DB_NAME"
echo "     Broj tabela: $TABLE_COUNT"

# Prikaz grešaka ako postoje
if [ -s "/tmp/import_errors_${DB_NAME}.log" ]; then
    ERROR_COUNT=$(wc -l < "/tmp/import_errors_${DB_NAME}.log")
    echo "     Upozorenja/greške: $ERROR_COUNT (detalji: /tmp/import_errors_${DB_NAME}.log)"
fi

echo ""
echo "[DONE] Import baze '$DB_NAME' završen."
