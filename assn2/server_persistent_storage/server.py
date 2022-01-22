import socket
import os

server_filename = "mydata.txt"
separator = "<#1234>"
server_ip = socket.gethostbyname('ipc_server_dns_name')
server_port = 5002
filesize = os.path.getsize(server_filename)

#Create a socket connection and start listening for requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, server_port))
s.listen()
conn, addr = s.accept()

print('Connected by', addr)
while True:
    conn.send(f"{server_filename}{separator}{filesize}".encode("utf-8"))
    with open(server_filename, "rb") as f:
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            conn.sendall(bytes_read)

#Close all sockets
client_socket.close()
s.close()
