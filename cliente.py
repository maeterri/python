import socket
import sys

#creo un archivo donde voy a meter los datos del servidor
miarchivo=open("datosservidor.txt","a")
miarchivo.write("nuevos datos en el archivo /n")
# creo el socket
misocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creo una dupla con la dirección del servidor
dirservidor=('localhost',10000)
misocket.connect(dirservidor)

try:

    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    misocket.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = misocket.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    misocket.close()