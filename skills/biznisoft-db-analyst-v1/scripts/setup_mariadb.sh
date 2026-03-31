#!/bin/bash
# =============================================================================
# setup_mariadb.sh — Instalacija i pokretanje MariaDB servera
# =============================================================================
# Koristi: sudo bash setup_mariadb.sh
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$SKILL_DIR/config/mariadb_performance.cnf"

echo "=== BizniSoft MariaDB Setup ==="

# 1. Provera da li je MariaDB već instaliran
if command -v mariadbd &>/dev/null || command -v mysqld &>/dev/null; then
    echo "[OK] MariaDB je već instaliran."
    MARIADB_VERSION=$(mariadbd --version 2>/dev/null || mysqld --version 2>/dev/null)
    echo "     Verzija: $MARIADB_VERSION"
else
    echo "[INFO] MariaDB nije pronađen. Instalacija u toku..."
    sudo apt-get update -qq
    sudo apt-get install -y mariadb-server mariadb-client
    echo "[OK] MariaDB instaliran."
fi

# 2. Primena performance konfiguracije
if [ -f "$CONFIG_FILE" ]; then
    echo "[INFO] Primena performance konfiguracije..."
    sudo cp "$CONFIG_FILE" /etc/mysql/mariadb.conf.d/99-biznisoft-performance.cnf
    echo "[OK] Konfiguracija primenjena: /etc/mysql/mariadb.conf.d/99-biznisoft-performance.cnf"
else
    echo "[WARN] Konfiguracija nije pronađena: $CONFIG_FILE"
fi

# 3. Kreiranje log direktorijuma
sudo mkdir -p /var/log/mysql
sudo chown mysql:mysql /var/log/mysql 2>/dev/null || true

# 4. Pokretanje MariaDB servera
echo "[INFO] Pokretanje MariaDB servera..."

# Proba systemctl prvo, pa mysqld_safe kao fallback (non-systemd okruženje)
if command -v systemctl &>/dev/null && systemctl is-system-running &>/dev/null 2>&1; then
    sudo systemctl start mariadb
    sudo systemctl enable mariadb
    echo "[OK] MariaDB pokrenut preko systemctl."
else
    # Non-systemd okruženje (Docker, WSL, itd.)
    if sudo mysqladmin ping &>/dev/null 2>&1; then
        echo "[OK] MariaDB je već aktivan."
    else
        echo "[INFO] Non-systemd okruženje — koristim mysqld_safe..."
        sudo mysqld_safe --defaults-extra-file=/etc/mysql/mariadb.conf.d/99-biznisoft-performance.cnf &
        sleep 3

        # Čekaj da server bude spreman (max 30 sekundi)
        for i in $(seq 1 30); do
            if sudo mysqladmin ping &>/dev/null 2>&1; then
                echo "[OK] MariaDB je aktivan nakon ${i}s."
                break
            fi
            sleep 1
        done

        if ! sudo mysqladmin ping &>/dev/null 2>&1; then
            echo "[ERROR] MariaDB se nije pokrenuo u roku od 30 sekundi."
            exit 1
        fi
    fi
fi

# 5. Verifikacija
echo ""
echo "=== Verifikacija ==="
sudo mysql -u root -e "SELECT VERSION() AS verzija, @@datadir AS datadir;" 2>/dev/null
sudo mysql -u root -e "SHOW DATABASES;" 2>/dev/null
echo ""
echo "[DONE] MariaDB setup završen."
