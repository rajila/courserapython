import socket

_mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_mySocket.connect(('data.pr4e.org', 80))
_cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
_mySocket.send(_cmd)

while True:
    _data = _mySocket.recv(512) # recupera hasta 512 caracteres
    if len(_data) < 1: break # Verifico si aún hay datos en la matriz de caracteres
    print(_data.decode(), end='') # decoficar el texto
_mySocket.close()
