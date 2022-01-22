import socket
import os
import hashlib

server_ip = socket.gethostbyname('ipc_server_dns_name')
server_port = 5002
separator = "<#1234>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
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
        file_hash = hashlib.sha256(bytes_read).hexdigest()
print(f"File {filename} received successfully")

with open(filename, 'r') as f:
    contents = f.read()
    print(contents)

print(f"Generated Hash: {file_hash}")
#Close the socket
s.close()
