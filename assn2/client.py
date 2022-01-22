import socket
import os
import sys

server_ip = sys.argv[0]#"172.17.147.1"
server_port = 5002
separator = "<#1234>"

# Create a socket and connect to the server
s = socket.socket()
s.connect((server_ip, server_port))
print(f"Connected successfully to server ({server_ip}, {server_port})")

# Receive the file sent by the server
received = s.recv(1024).decode("utf-8")
filename, file_size = received.split(separator)
filename = os.path.basename(filename)

# Save the file locally
with open(filename, "wb") as f:
    while True:
        bytes_read = s.recv(1024)
        if not bytes_read:
            break
        f.write(bytes_read)

print(f"File {filename} received successfully")

#Close the socket
s.close()
