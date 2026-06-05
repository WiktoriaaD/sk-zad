import socket
import sys
import select

#konfiguracja serwera - localhost
SERWER_IP = '127.0.0.1'
SERWER_PORT = 50005

#socket dla klienta
klient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


nick = input("Podaj swój nick: ")

paczka_startowa = b'\x00' + nick.encode('utf-8')
klient.sendto(paczka_startowa, (SERWER_IP, SERWER_PORT))

print(f"Połączono z serwerem jako {nick}. Możesz pisać wiadomości. Wpisz 'exit' aby wyjść.")


while True:
    odczyt, _, _ = select.select([sys.stdin, klient], [], [])
    
    for source in odczyt:
        if source == sys.stdin:
            text = sys.stdin.readline().strip()
            
            if text.lower() == 'exit':
                klient.sendto(b'', (SERWER_IP, SERWER_PORT))
                print("Rozłączono.")
                sys.exit()
                
            if text:
                full_message = b'\x01' + text.encode('utf-8')
                klient.sendto(full_message, (SERWER_IP, SERWER_PORT))
        
        
        elif source == klient:
            data, adres = klient.recvfrom(1024)
            if data:
                typ_wiadomosci = data[0:1]
                text_bajty = data[1:]
                
                if typ_wiadomosci == b'\x01':
                    print(text_bajty.decode('utf-8'))