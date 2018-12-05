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

# Message sent to client when connected. Converted into binary form using 'encode()'
connection.send("Hello my name is Servo Server Face and I am the server".encode())

# Close connection.
connection.close()