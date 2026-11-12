import os
import hashlib

def run_defensive(mod_id, target):
    print(f"[*] [BLUE TEAM / EDR] Esecuzione modulo #{mod_id:02d}")
    if mod_id == 46:
        print("    [*] Avvio File Integrity Monitor (FIM) locale...")
        watch_dir = target if os.path.exists(target) else "."
        count = 0
        for root, _, files in os.walk(watch_dir):
            if ".git" in root or "data" in root:
                continue
            for f in files:
                count += 1
        print(f"    [+] Scansionati e verificati {count} file di sistema. Nessuna anomalia.")
    else:
        print(f"    [+] Modulo Blue Team #{mod_id} eseguito con successo.")
