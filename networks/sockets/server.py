import socket

# Define the host and port to listen on
HOST = '127.0.0.1'  # The loopback IP address of the local machine
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("The server is listening on", (HOST, PORT))
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print('Connection established from', addr)
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            print('Message received from the client:', data.decode())
            # Respond to the client
            conn.sendall(b'Message received. Thank you for connecting.')
