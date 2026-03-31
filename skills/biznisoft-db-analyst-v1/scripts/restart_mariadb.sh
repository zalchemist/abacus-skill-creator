#!/bin/bash
# =============================================================================
# restart_mariadb.sh — Brzi restart MariaDB servera
# =============================================================================
# Koristi: sudo bash restart_mariadb.sh
# =============================================================================

echo "=== MariaDB Restart ==="

# 1. Provera trenutnog statusa
if sudo mysqladmin ping &>/dev/null 2>&1; then
    echo "[INFO] MariaDB je aktivan. Restartujem..."
    # Pokušaj graceful shutdown
    sudo mysqladmin -u root shutdown 2>/dev/null || true
    sleep 2
else
    echo "[INFO] MariaDB nije aktivan. Pokretanje..."
fi

# 2. Ubij zaostale procese ako postoje
if pgrep -x mysqld &>/dev/null || pgrep -x mariadbd &>/dev/null; then
    echo "[INFO] Zaustavljam zaostale procese..."
    sudo pkill -9 mysqld 2>/dev/null || true
    sudo pkill -9 mariadbd 2>/dev/null || true
    sleep 2
fi

# 3. Pokretanje
if command -v systemctl &>/dev/null && systemctl is-system-running &>/dev/null 2>&1; then
    sudo systemctl restart mariadb
else
    sudo mysqld_safe &
    sleep 3
fi

# 4. Čekanje da bude spreman
for i in $(seq 1 30); do
    if sudo mysqladmin ping &>/dev/null 2>&1; then
        echo "[OK] MariaDB je aktivan nakon ${i}s."
        echo ""
        sudo mysql -u root -e "SHOW DATABASES;" 2>/dev/null
        echo ""
        echo "[DONE] Restart završen."
        exit 0
    fi
    sleep 1
done

echo "[ERROR] MariaDB se nije pokrenuo u roku od 30 sekundi."
exit 1
