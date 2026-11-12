import hashlib
import base64

def run_crypto(mod_id, target):
    print(f"[*] [CRYPTO] Esecuzione modulo #{mod_id:02d}")
    if mod_id == 81:
        h = hashlib.sha256(target.encode()).hexdigest()
        print(f"    [+] SHA-256 Hash: {h}")
    elif mod_id == 82:
        b = base64.b64encode(target.encode()).decode()
        print(f"    [+] Base64 Encoded: {b}")
    else:
        print(f"    [+] Modulo Crypto #{mod_id} elaborato.")
