import socket
HOST = "localhost"
PORT = 3000         # this is the port no of server we want to connect

print("Starting a Client : Client1")

# Create a New Socket Obj
client_socket = socket.socket()

# Client need to connect to server socket object
client_socket.connect((HOST, PORT))

# Sending This Message to server side
client_socket.sendall(b"Hello, I am from Client Side")

# Recieving This Message from Server Side
response_from_server = client_socket.recv(2048)     # Maximum of 2048 bytes of data can be recieved
print(response_from_server)
