import socket

# Define the host and port to connect to
HOST = '127.0.0.1'  # The loopback IP address of the local machine
PORT = 65432        # Port to connect to

# Create a TCP/IP socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    # Send data to the server
    s.sendall(b'Hello, server!')
    # Receive response from the server
    data = s.recv(1024)

print('Message received from the server:', data.decode())
