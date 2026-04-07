
---

### 1. Lista interfejsów sieciowych w systemie (format: nazwa-status)
* **Źródło (polecenie):** `ip -br link`
* **Odpowiedź:**
```
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>
enp0s3           UP             08:00:27:a2:d3:b0 <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### 2. Adres MAC routera (bramy domyślnej)
* **Źródło (polecenie):** `ip route | grep default` 
* **Odpowiedź:** `default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100` 

### 3. Zmiana adresu MAC karty sieciowej Ethernet
* **Źródło (polecenie):** Trzeba najpierw wyłączyć kartę, zmienić MAC i włączyć ją z powrotem:
  1. `sudo ip link set dev eth0 down`
  2. `sudo ip link set dev eth0 address 00:11:22:33:44:55`
  3. `sudo ip link set dev eth0 up`

### 4. Ping wszystkich urządzeń jednocześnie w podsieci
* **Źródło (polecenie):**`nmap -sn 192.168.64.0/24` 
* **Odpowiedź (wynik):**
```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-04-07 20:48 UTC
Nmap done: 256 IP addresses (0 hosts up) scanned in 125.94 seconds
```


### 5. Skan całej podsieci w poszukiwaniu otwartego portu 22 (SSH)
* **Źródło (polecenie):** `nmap -p 22 --open 192.168.1.0/24`
* **Odpowiedź (wynik):**

### 6. Skan wszystkich portów na interfejsie lo (loopback)
* **Źródło (polecenie):** `nmap -p- 127.0.0.1`
* **Odpowiedź (wynik):**
```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-04-07 21:19 UTC
Nmap scan report for localhost.localdomain (127.0.0.1)
Host is up (0.000077s latency).
Not shown: 65534 closed tcp ports (conn-refused)
PORT    STATE SERVICE
631/tcp open  ipp

Nmap done: 1 IP address (1 host up) scanned in 1.28 seconds
```

### 7. Porty otwarte w systemie wraz z PID i nazwą programu
* **Źródło (polecenie):** `sudo ss -tulpn`
* **Odpowiedź (wynik):**
```
Netid      State       Recv-Q      Send-Q           Local Address:Port            Peer Address:Port     Process                                         
udp        UNCONN      0           0                   127.0.0.54:53                   0.0.0.0:*         users:(("systemd-resolve",pid=470,fd=16))      
udp        UNCONN      0           0                127.0.0.53%lo:53                   0.0.0.0:*         users:(("systemd-resolve",pid=470,fd=14))      
udp        UNCONN      0           0                      0.0.0.0:33294                0.0.0.0:*         users:(("avahi-daemon",pid=725,fd=14))         
udp        UNCONN      0           0                      0.0.0.0:5353                 0.0.0.0:*         users:(("avahi-daemon",pid=725,fd=12))         
udp        UNCONN      0           0                         [::]:50137                   [::]:*         users:(("avahi-daemon",pid=725,fd=15))         
udp        UNCONN      0           0                         [::]:5353                    [::]:*         users:(("avahi-daemon",pid=725,fd=13))         
tcp        LISTEN      0           4096                 127.0.0.1:631                  0.0.0.0:*         users:(("cupsd",pid=1152,fd=7))                
tcp        LISTEN      0           4096             127.0.0.53%lo:53                   0.0.0.0:*         users:(("systemd-resolve",pid=470,fd=15))      
tcp        LISTEN      0           4096                127.0.0.54:53                   0.0.0.0:*         users:(("systemd-resolve",pid=470,fd=17))      
tcp        LISTEN      0           4096                     [::1]:631                     [::]:*         users:(("cupsd",pid=1152,fd=6))
```
### 8. Trasa domyślna w systemie
* **Źródło (polecenie):** `ip route` 
* **Odpowiedź (wynik):**
```
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.16 metric 100 
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.16 metric 100
```

### 9. Trasa pakietów do serwera kosmatka.pl
* **Źródło (polecenie):** `traceroute kosmatka.pl`
* **Odpowiedź (wynik):**
```
traceroute to kosmatka.pl (217.28.148.190), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  1.678 ms  1.586 ms  1.523 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * _gateway (10.0.2.2)  6.565 ms  6.214 ms
  ```

### 10. Adres serwera DNS ustawiony w systemie
* **Źródło (plik/polecenie):** `cat /etc/resolv.conf | grep nameserver`
* **Odpowiedź (zawartość pliku):** `nameserver 127.0.0.53`

### 11. Lista statycznych wpisów DNS w systemie
* **Źródło (plik):** `cat /etc/hosts`
* **Odpowiedź (zawartość pliku):**
```
127.0.0.1	localhost.localdomain	localhost
::1		localhost6.localdomain6	localhost6

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
```
### 12. Rekord DNS poczty e-mail (MX) dla kosmatka.pl przez serwer 8.8.8.8
* **Źródło (polecenie):** `dig @8.8.8.8 kosmatka.pl MX +short`
* **Odpowiedź (wynik):**
```
10 mx2.privateemail.com.
10 mx1.privateemail.com.
```

### 13. Adres IPv6 hosta google.pl
* **Źródło (polecenie):** `dig +short google.pl AAAA`
* **Odpowiedź (wynik):** `2a00:1450:4025:802::5e`

### 14. Data rejestracji i opłacenia domeny kosmatka.pl
* **Źródło (polecenie):** `whois kosmatka.pl | grep -E "created|renewal"`
* **Odpowiedź (wynik):** 
```
created:                        2022.12.02 12:27:10
renewal date:                   2032.12.02 12:27:10
```
### 15. Adres strony z listą usuniętych domen .pl dzisiejszego dnia
* **Źródło (wiedza z internetu):** `https://www.dns.pl/deleted_domains.txt`
* **Odpowiedź:**
```
2026-04-07 08:10:56 MEST

0olx.pl
0x9d.pl
112.edu.pl
1trip.pl
24h-online.pl
25latkappahl.pl
272slowa.pl
31.com.pl
37.com.pl
3ddrukuj.pl
3dlogic.pl
3wkoncept.pl
40tygodni.pl
42069.pl
4rise.pl
53.com.pl
543323.pl
638.pl
67.slupsk.pl
72.com.pl
...
```
