import socket
import os
import hashlib

server_ip = "172.17.147.1"
server_port = 5002
separator = "<#1234>"

# Create a socket and connect to the server
s = socket.socket()
s.connect((server_ip, server_port))
print(f"Connected successfully to server ({server_ip}, {server_port})")

# Receive the file sent by the server
received = s.recv(1024).decode("utf-8")
filename, received_hash = received.split(separator)
filename = os.path.basename(filename)

# Save the file locally
with open(filename, "wb") as f:
    while True:
        bytes_read = s.recv(1024)
        if not bytes_read:
            break
        file_hash = hashlib.sha256(bytes_read).hexdigest()
        f.write(bytes_read)

os.rename(filename, "mydata_client_copy.txt")
print(f"File {filename} received successfully")

#Hash verification
print(f"Received Hash:  {received_hash}")
print(f"Generated Hash: {file_hash}")
if file_hash==received_hash:
    print("Hash Verified")
else:
    print("Incorrect Hash value")

#Close the socket
s.close()