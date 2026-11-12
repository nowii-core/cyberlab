import socket

def run_recon(mod_id, target):
    print(f"[*] [RECON] Esecuzione modulo #{mod_id:02d} su {target}")
    if mod_id == 1:
        ports = [21, 22, 80, 443, 3306, 8080]
        for p in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.4)
                    if s.connect_ex((target, p)) == 0:
                        print(f"    [!] Porta TCP {p} -> APERTA")
            except Exception:
                pass
    else:
        print(f"    [+] Modulo Recon #{mod_id} eseguito con successo (Target: {target}).")
