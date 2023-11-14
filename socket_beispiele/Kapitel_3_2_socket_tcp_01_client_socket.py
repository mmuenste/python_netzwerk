# Erlaubt es einen tcp-Socket für die anzugebende host/port-Kombination
# (z.B. www.python.org/80) aufzubauen.

import socket
import sys
if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Die form except x as y erlaubt es im Folgenden print statement
    # auf die Art des Fehlers hinzuweisen.
    except socket.error as err:
        print("Failed to create a socket")
        print("Reason: %s" % str(err))
        # Verwendet die Funktion exit() aus dem Modul sys, um das Programm
        # zu beenden.
        sys.exit()
    print('Socket created')
    target_host = input("Enter the target host name to connect: ")
    target_port = input("Enter the target port: ")
    try:
        sock.connect((target_host, int(target_port)))
        print("Socket Connected to %s on port: %s" % (target_host,
                                                      target_port))
        sock.shutdown(1)
    except socket.error as err:
        print("Failed to connect to %s on port %s" % (target_host,
                                                      target_port))
        print("Reason: %s" % str(err))
        sys.exit()
