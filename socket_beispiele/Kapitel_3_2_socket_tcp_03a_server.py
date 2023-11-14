# Einfacher tcp-Server der auf Anfragen wartet und die lokale Zeit als
# Antwort liefert. Beachten Sie bitte auch die Kommentare in den tcp-
# Client files.

import socket
import sys

# Importiert aus dem modul time der Standard-library nur die Funktion
# ctime. Beachten Sie, dass durch diese Art des Imports die Funktion
# später direkt über ihren Name angesprochen werden kann ohne den Um-
# weg über den Modulnamen nehmen zu müsse (time.ctime).
from time import ctime

HOST = 'localhost'
PORT = 12346
BUFSIZ = 1024
ADDR = (HOST, PORT)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
    # Bindet für den Server die oben def. IP/Port-Kombination
    # fest an den socket
    server_socket.bind(ADDR)

    # Wartet auf auf Anfragen. Durch die zusätzliche Option lässt
    # sich angeben wie viele Verbindungsanfragen nicht akzeptiert
    # werden können, bevor neue Anfragen abgelehnt werden.
    server_socket.listen(5)

    # Legt weitere Optionen für den Socket fest. Im wesentlichen
    # wird hier die Wiederverwendung der lokalen Addresse erlaubt.
    # Detaillierte Informationen zu den dort möglichen Optionen
    # und der genauen Sytax lassen sich auf den Unix-man-pages
    # ermitteln, die hier vom modul socket übernommen werden.
    server_socket.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)
    while True:
        print('Server waiting for connection...')
        # Akzeptiert eine Anfrage und weisst den enstprechenden socket
        # und die ip des Clients dem Paar (client_sock, addr) zu.
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)

        # Loop zur Kommunikation mit den Client.
        while True:
            data = client_sock.recv(BUFSIZ)

            # Abbruch der Schleife, wenn alle Bits empfangen sind oder
            # explizit der String 'END' vom client gesendet werden.
            # if not data or data.decode('utf-8') == 'END':
            if not data:
                break
            if data.decode('utf-8') == 'END':
                print("hier:", repr(data))
                sys.exit()
            # Lokale formatierte Textausgabe. ctime liefert einen String
            # mit der aktuellen Serverzeit in einem lesbaren Format.
            print("Received from client: %s" % data.decode('utf-8'))
            print("Sending the server time to client: %s"
                    %ctime())

            # bytes() encodiert den String der von ctime geliefert wird ent-
            # sprechend dem Schema utf-8 und sendet die Daten über den socket
            # der dem Client zugeordnet ist.
            # Try und except dienen dazu, hier eine Abbruchmöglichkeit durch
            # das Steurkommando STR-C zu ermöglichen, falls beim Versand der
            # Daten ein Problem auftreten sollte.
            try:
                client_sock.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")
        client_sock.close() # Schließt die Verbindung zum Client.
    server_socket.close()   # Gibt den Serversocket wieder frei.
