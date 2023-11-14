# Einfaches Clientprogramm, dass einen tcp-socket erstellt und von
# einem Webserver per http-GET eine Website anfordert.

# Importiert das Modul socket aus der Python Standard Library und
# stellt damit unter dem namen socket.* die dort vorhandenen Objekte
# und Funktionen zur Verfügung.
import socket

# Hier werden einige Variablen zur späteren Verwendung definiert
HOST = 'www.linuxcommand.org' # oder 'localhost'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)  # (,) erstellt ADDR als Tupel aus HOST+PORT

# Die if anweisung sorgt dafür, dass der Code nur verwendet wird,
# wenn die Datei direkt ausgeführt wird. (-> "python3 simple_tcp_
# client.py")
if __name__ == '__main__':
    # Verwendet den Konstruktor socket aus dem modul socket mit
    # den dort definierten Werten AF_INET und SOCK_STREAM um einen
    # ip-tcp socket zu erstellen und weisst diese Instanz dem Namen
    # client_sock zu.
    client_sock = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)
    # Verbindet den socket mit der Oben definierten Addresse.
    client_sock.connect(ADDR)

    # Loop für die Anfrage der Website. Der Loop sorgt dafür, dass die
    # Anfrage komplettiert wird auch wenn die Antwort größer ist als
    # die oben festgelegt Buffergröße.
    while True:
        # Definiere den http-GET Request.
        data = 'GET / HTTP/1.1\nHost: ' + HOST + '\nConnection: close\n\n'

        # .send(data) sendet auf dem socket client_sock die Anfrage.
        # .encode() legt fest anch welchem Schema die Buchstaben etc.in
        # in Bits umgewandetlt werden (das s.g. encoding).
        client_sock.send(data.encode('utf-8'))

        # Empfängt vom Socket die Antwort und weisst diese data zu.
        data = client_sock.recv(BUFSIZ)
        if not data:  # Abbruch wenn die Antwort komplett ist.
            break
        # Ausgabe, die die empfangenen bits Entsprechen dem utf-8 Schema
        # interpretiert um diese darzustellen.
        print(data.decode('utf-8'))
    client_sock.close()  # Schließe den socket.
