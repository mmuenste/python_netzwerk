# Eine erweiterte Variante des tcp-Clients. Erlaubt Verbindungen zum in
# tcp_server.py beschriebenen Server aufzubauen.

import socket
HOST = 'localhost'
PORT = 12346
BUFSIZ = 256
ADDR = (HOST, PORT)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)

    # Verwendet input um vom Nutzer Daten für Hostaddrese und Port
    # einzulesen. Gibt in der Eingabeaufforderung die oben definierten
    # default-Werte an. Diese werden durch das 'or' Schlüsselwort verwendet,
    # falls der Benutzer keinen Input liefert, und passen zu den default-
    # Einstellungen in tcp_server.py für den lokalen Betrieb.
    host = input("Enter hostname [%s]: " % HOST) or HOST
    port = input("Enter port [%s]: " % PORT) or PORT

    # Definiert ein socket-Tupel aus den obigen Eingaben und baut die
    # Verbindung auf. int() dient dazu den Eingabestring auf jeden Fall korrekt
    # als Zahl zu interpretieren.
    sock_addr = (host, int(port))
    client_sock.connect(sock_addr)

    payload = 'GET TIME'
    try:
        while True:
            client_sock.send(payload.encode('utf-8'))
            data = client_sock.recv(BUFSIZ)
            print(repr(data))  # repr() als Alternative zur Dekodierung.
            more = input("Want to send more data to server[y/n]:")
            if more.lower() == 'y':  # .lower() um sowohl y/Y zu akzeptieren.
                payload = input("Enter payload: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")
    client_sock.close()
