#!/bin/bash
# =============================================================================
# check_status.sh — Provera statusa MariaDB servera
# =============================================================================
# Koristi: bash check_status.sh
# =============================================================================

echo "=== MariaDB Status ==="

# 1. Da li server radi?
if sudo mysqladmin ping &>/dev/null 2>&1; then
    echo "Status: ✅ AKTIVAN"
    echo ""

    # Verzija
    VERSION=$(sudo mysql -u root -N -e "SELECT VERSION();" 2>/dev/null)
    echo "Verzija: $VERSION"

    # Uptime
    UPTIME=$(sudo mysql -u root -N -e "SHOW STATUS LIKE 'Uptime';" 2>/dev/null | awk '{print $2}')
    if [ -n "$UPTIME" ]; then
        DAYS=$((UPTIME / 86400))
        HOURS=$(( (UPTIME % 86400) / 3600 ))
        MINS=$(( (UPTIME % 3600) / 60 ))
        echo "Uptime: ${DAYS}d ${HOURS}h ${MINS}m"
    fi

    # Aktivne konekcije
    THREADS=$(sudo mysql -u root -N -e "SHOW STATUS LIKE 'Threads_connected';" 2>/dev/null | awk '{print $2}')
    echo "Aktivne konekcije: $THREADS"

    # Lista baza
    echo ""
    echo "=== Baze podataka ==="
    sudo mysql -u root -e "
        SELECT
            s.SCHEMA_NAME AS baza,
            COUNT(t.TABLE_NAME) AS br_tabela,
            IFNULL(ROUND(SUM(t.DATA_LENGTH + t.INDEX_LENGTH) / 1024 / 1024, 1), 0) AS velicina_MB
        FROM information_schema.SCHEMATA s
        LEFT JOIN information_schema.TABLES t ON s.SCHEMA_NAME = t.TABLE_SCHEMA
        WHERE s.SCHEMA_NAME NOT IN ('information_schema', 'performance_schema', 'mysql', 'sys')
        GROUP BY s.SCHEMA_NAME
        ORDER BY s.SCHEMA_NAME;
    " 2>/dev/null

    # BizniSoft specifična provera
    echo ""
    echo "=== BizniSoft baze (opp*) ==="
    OPP_DBS=$(sudo mysql -u root -N -e "SHOW DATABASES LIKE 'opp%';" 2>/dev/null)
    if [ -z "$OPP_DBS" ]; then
        echo "  Nijedna BizniSoft baza nije pronađena."
    else
        while IFS= read -r db; do
            TC=$(sudo mysql -u root -N -e "SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_SCHEMA='$db';" 2>/dev/null)
            echo "  $db: $TC tabela"
        done <<< "$OPP_DBS"
    fi

else
    echo "Status: ❌ NEAKTIVAN"
    echo ""
    echo "Za pokretanje koristite:"
    echo "  sudo bash setup_mariadb.sh    # Puna instalacija i pokretanje"
    echo "  sudo bash restart_mariadb.sh  # Brzi restart"
fi

echo ""
echo "[DONE]"
