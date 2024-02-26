import socket
import threading
HOST = "localhost"
PORT = 3000     # This is PORT No for server

# Function Of connection_for_client
def connection_for_client(conn, args):
    print("New Client Has Been Connected")

    # Recieving Some Data From Client
    data = conn.recv(2048)                  # Maximum of 2048 bytes of data can be recieved
    print("Data Recieved From Client is:", data)

    # Sending Some Confirmation Data To Client
    conn.sendall(b"Server has recieved your data")

# Create a New Socket Obj
server_socket = socket.socket()

# Bind the Socket Obj to (HOST & PORT)
server_socket.bind((HOST, PORT))

# Start listening for New Connection
server_socket.listen()
print("Server is Listening on This", HOST, "with", PORT, "No.")

# Setup For Accepting the connection
while True:
    conn, addr = server_socket.accept()             # it is accepting a new connection
    t = threading.Thread(target = connection_for_client, args = (conn, addr))       # it is preparing the thread
    t.start()                                       # it start running the thread
