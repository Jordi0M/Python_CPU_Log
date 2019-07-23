import socket

def guardar_temperatura(msg_cliente):
    f = open("temperaturas.txt","a")
    f.write(msg_cliente+"\n")
    f.close() 

HOST = '127.0.0.1'
PORT = 65432

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    msg_cliente = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        msg_cliente = data
        print(msg_cliente.decode())
        guardar_temperatura(msg_cliente.decode())

    conn.close()
    print ("sensor desconectado")