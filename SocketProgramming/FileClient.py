import socket

s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))

# === Request file from server ===
# Request file
fileName = 'testFile.txt'
# Send file name
s.send(fileName.encode())

# If file found, receive and print it.
readFile = s.recv(1024)
print(readFile.decode())

s.close()