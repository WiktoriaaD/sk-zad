import socket

#Konfiguracja adresu i portu
IP = '0.0.0.0'
PORT = 50005 

#gniazdo sieciowe
serwer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


serwer.bind((IP, PORT))

users = {}

print(f"Serweru uruchomiony i słucha na porcie {PORT}")

#petla by serwer ciagle dzialal
while True:
    data, adres = serwer.recvfrom(1024)

    if not data:
        if adres in users:
            stary_nick = users[adres]
            del users[adres] 
            print(f"-- Użytkownik {stary_nick} ({adres}) rozłączył się.")
        continue 

    type_message = data[0:1]  
    tresc_bajty = data[1:]     

    if type_message == b'\0':
        nick = tresc_bajty.decode('utf-8')
        
        users[adres] = nick
        print(f"++ Zarejestrowano użytkownika: {nick} z adresu {adres}")

    elif type_message == b'\1':
        if adres not in users:
            print(f"!! Ignoruję wiadomość od nieznanego adresu: {adres}")
            continue

        nadawca_nick = users[adres]
        wiadomosc_tekst = tresc_bajty.decode('utf-8')
        print(f"[{nadawca_nick}]: {wiadomosc_tekst}")

        box_to_send = b'\1' + f"{nadawca_nick}: {message_text}".encode('utf-8')

        for odbiorca_adres in users.keys():
            if odbiorca_adres != adres:
                serwer.sendto(paczka_do_wyslania, odbiorca_adres)
