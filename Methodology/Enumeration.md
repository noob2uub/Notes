# Network Scanning
```
  nmap -sn 10.11.1.*
  nmap -sL 10.11.1.*
  nbtscan -r 10.11.1.0/24
  smbtree
  ```
# Individual Host Scanning
```
   NMAP -sC -sN -A -T4 
   nmap  --top-ports 20 --open -iL iplist.txt
   nmap -sS -A -sV -O -p- ipaddress
   nmap -sU ipaddres
```
# Service Scanning

### WebApp
```
      Nikto
           nikto -host 10.10.150.75 -port 8080 -id joker:hannah
           nikto -h http://10.10.241.55:1234/manager/html -id bob:bubbles
      dirb/Gobuster
            gobuster dir -u http://10.10.255.58 -w /home/noob2uub/Documents/Wordlists/common.txt
            gobuster dir -u http://10.10.86.230/island/2100 -w /home/noob2uub/Documents/Wordlists/2.3-big.txt -x .ticket
            gobuster dir -u http://10.10.150.75 -w /home/noob2uub/Documents/Wordlists/2.3-medium.txt -x php,html,txt
      wpscan
      dotdotpwn
      view source 
      davtest\cadevar
      droopscan
      joomscan
      LFI\RFI Test
```
###  Linux\Windows
```
      snmpwalk -c public -v1 ipaddress 1
      smbclient -L //ipaddress
      showmount -e ipaddress port
      rpcinfo
      Enum4Linux    
 ```
    
###  Anything Else
```    
      nmap scripts (locate *nse* | grep servicename)
      hydra
      MSF Aux Modules
      Download the software
```     
