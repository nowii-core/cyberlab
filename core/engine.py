import sqlite3
import os
from datetime import datetime
from modules.recon import run_recon
from modules.offensive import run_offensive
from modules.defensive import run_defensive
from modules.cloud import run_cloud
from modules.crypto import run_crypto
from modules.utils import run_utils

class MegaEngine:
    def __init__(self):
        self.db_path = "data/results.db"
        self._init_db()

    def _init_db(self):
        os.makedirs("data", exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER,
                category TEXT,
                target TEXT,
                timestamp TEXT,
                status TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_action(self, mod_id, category, target):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO audit_logs (module_id, category, target, timestamp, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (mod_id, category, target, datetime.now().isoformat(), "SUCCESS"))
        conn.commit()
        conn.close()

    def dispatch(self, mod_id, target):
        if 1 <= mod_id <= 15:
            cat = "Recon"
            run_recon(mod_id, target)
        elif 16 <= mod_id <= 45:
            cat = "Offensive/Audit"
            run_offensive(mod_id, target)
        elif 46 <= mod_id <= 65:
            cat = "Defensive/EDR"
            run_defensive(mod_id, target)
        elif 66 <= mod_id <= 78:
            cat = "Cloud"
            run_cloud(mod_id, target)
        elif 79 <= mod_id <= 88:
            cat = "Crypto"
            run_crypto(mod_id, target)
        elif 89 <= mod_id <= 100:
            cat = "Utils"
            run_utils(mod_id, target)
        else:
            print("[!] Errore: ID modulo non valido (scegli tra 1 e 100).")
            return

        self.log_action(mod_id, cat, target)
        print("[✓] Log salvato con successo nel database SQLite locale.")
