import os

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
    ███╗   ██╗ ██████╗ ██╗    ██╗██╗██╗      ██████╗███████╗ ██████╗██████╗ 
    ████╗  ██║██╔═══██╗██║    ██║██║██║     ██╔════╝██╔════╝██╔════╝██╔══██╗
    ██╔██╗ ██║██║   ██║██║ █╗ ██║██║██║     ██║     █████╗  ██║     ██████╔╝
    ██║╚██╗██║██║   ██║██║███╗██║██║██║     ██║     ██╔══╝  ██║     ██╔══██╗
    ██║ ╚████║╚██████╔╝╚███╔███╔╝██║███████╗╚██████╗███████╗╚██████╗██║  ██║
    ========================================================================
           [!] NEXT-GEN 100-MODULE UNIFIED SECURITY & DEFENSE SUITE
           [!] Architecture: Native Python | Zero-Bloat | SQLite Engine
    ========================================================================
    """
    print(banner)

def list_all_categories():
    print("  [ MACRO-AREE DISPONIBILI NELLA SUITE (1 - 100) ]")
    print("   • [01-15] Reconnaissance & OSINT (Scansioni, DNS, Whois)")
    print("   • [16-30] Perimeter & Web Auditing (Fuzzer, Header, SQLi check)")
    print("   • [31-45] Offensive & Exploit Simulation (PrivEsc, Shell, Hash)")
    print("   • [46-65] Blue Team & EDR Telemetry (FIM, Processi, Log, SQLite)")
    print("   • [66-78] Cloud & Infrastructure Security (Docker, K8s, Config)")
    print("   • [79-88] Cryptography & Data Protection (AES, RSA, Hash, Base64)")
    print("   • [89-100] System Automation & Utils (Benchmark, Backup, SQLite Shell)")
    print("-" * 72)
    print("   [!] Utilizzo: python3 main.py --mod <1-100> --target <ip/path/url>")
