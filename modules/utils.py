import sqlite3
import os

def run_utils(mod_id, target):
    print(f"[*] [UTILS & SYSTEM] Esecuzione modulo #{mod_id:02d}")
    if mod_id == 89:
        db_path = "data/results.db"
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM audit_logs")
            count = cursor.fetchone()[0]
            conn.close()
            print(f"    [+] Trovati {count} record storici nel database SQLite locale.")
        else:
            print("    [!] Nessun database trovato.")
    else:
        print(f"    [+] Modulo di utilità #{mod_id} completato.")
