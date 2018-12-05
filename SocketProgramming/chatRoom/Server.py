import socket
from threading import Thread

clients = {}
addresses = {}

host = '10.1.1.17'
port = 8080

s = socket.socket()
s.bind((host, port))


# Accept client requests to connect to the server.
def accept_client_connections():
    while True:
        client_connection, client_address = s.accept()
        print(client_address, " has connected...")
        client_connection.send("Welcome to the Servo Face chat room! Type your name to continue: ".encode("utf8"))
        addresses[client_connection] = client_address
        Thread(target=handle_client, args=(client_connection, client_address)).start()


# Send/broadcast message to all clients in dictionary.
def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8") + msg)


# handle client messages and naming.
def handle_client(connection, address):
    name = connection.recv(1024).decode("utf8")
    welcome = "Welcome " + name + ", you can type #quit to abandon Servo Face :("
    connection.send(bytes(welcome, "utf8"))

    msg = name + " has recently joined the chat room..."
    broadcast(bytes(msg, "utf8"))
    clients[connection] = name

    # As long as the client is exchanging messages in the chat room:
    while True:
        msg = connection.recv(1024)

        # If message is not a quit message, broadcast message.
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + " : ")
        else:
            connection.send(bytes("#quit", "utf8"))
            # Close connection.
            connection.close()
            # Delete client from dictionary.
            del clients[connection]
            broadcast(bytes(name + " has left the Chat Room, like a proper bastard...", "utf8"))


# Main function.
if __name__ == '__main__':
    s.listen(10)
    print("Servo Face is now online...")
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()
