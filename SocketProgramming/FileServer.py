import socket

host = 'localhost'
port = 8080

# Create socket using internet version 4 (socket.AF_INET),  using a TCP connection (socket.SOCK_STREAM).
# You can also pass nothing in the socket function and it will do the same thing. These are set by default.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port number.
s.bind((host, port))

# Listen for client request. We have set it so the server is only allowed to establish one connection.
s.listen(1)
print("The sever is listening for client request on port ", port)

# Allow the server to accept client requests.
connection, address = s.accept()
print("Connection has been established from ", str(address))

# === Sending a file ===
try:
    fileName = connection.recv(1024)
    # Open file and read it in bytes.
    file = open(fileName, 'rb')
    readFile = file.read()
    # Send file.
    connection.send(readFile)
    # Close once sent.
    file.close()
except:
    connection.send("Server Face couldn't find the file.".encode())

# Close connection.
connection.close()