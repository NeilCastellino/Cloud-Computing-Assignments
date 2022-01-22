import socket
import os

server_filename = "server_storage/mydata.txt"
separator = "<#1234>"
server_ip = socket.gethostbyname(socket.gethostname())
server_port = 5002
filesize = os.path.getsize(server_filename)

#Create a socket connection and start listening for requests
s = socket.socket()
s.bind((server_ip, server_port))
s.listen(5)
print(f"Server is up and running on ({server_ip}, {server_port})")

#Accept a request by a client
client_socket, address = s.accept()
print(f"Client: ({address[0]}) is connected.")

#Send the text file
client_socket.send(f"{server_filename}{separator}{file_size}".encode("utf-8"))
with open(server_filename, "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)

print(f"File {server_filename} sent successfully")

#Close all sockets
client_socket.close()
s.close()
