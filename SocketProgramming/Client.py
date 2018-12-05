import socket

s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))
# The message size can be at most 1024 bytes.
message = s.recv(1024)

# As long as the message is being received, keep receiving it and storing it in variable 'message' and decode it.
while message:
    print("Message: ", message.decode())
    message = s.recv(1024)

s.close()
