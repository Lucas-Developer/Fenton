import socket
import os

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print "Conected: ", cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        os.system(msg)
    con.close()
