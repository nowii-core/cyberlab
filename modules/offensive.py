def run_offensive(mod_id, target):
    print(f"[*] [OFFENSIVE/AUDIT] Esecuzione modulo #{mod_id:02d} su {target}")
    if mod_id == 31:
        print("    [+] Generazione payload di test sicuri...")
        print("    [payload] python3 -c 'import socket,subprocess,os;...'")
    else:
        print(f"    [+] Modulo Offensive #{mod_id} completato.")
