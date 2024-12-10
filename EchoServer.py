import socket
#serverSocket
if __name__ == "__main__":
    ip = str(input("Enter an IP: "))
    port = int(input("Enter a port number: "))

    # Create a TCP socket
    TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding a TCP socket
    TCPSocket.bind((ip, port))
    # Listening for 1 client only
    TCPSocket.listen(1)

    print(f"Server listening on {ip}:{port}")

    client, client_address = TCPSocket.accept()
    print(f"Connection Established: {client_address[0]}:{client_address[1]}")

    while True:
        # Receive the message from the client
        message = client.recv(1024)
        if not message:
            break

        # Print the received message on the server's screen
        decoded_message = message.decode("utf-8")
        print(f"Received from client: {decoded_message}")

        # Send the uppercase message back to the client
        client.send(decoded_message.upper().encode("utf-8"))

    print("Connection closed")
    client.close()
    TCPSocket.close()
