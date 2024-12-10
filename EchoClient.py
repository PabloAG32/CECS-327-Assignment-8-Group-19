import socket

if __name__ == "__main__":
    ip = str(input("Enter the server IP address: "))
    port = input("Enter the server port number: ")

    try:
        # Create a TCP socket
        TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to server
        TCPSocket.connect((ip, int(port)))

        while True:
            message = input("Enter a message (or type 'exit' to quit): ")
            if message.lower() == "exit":
                break

            # Send the message to the server
            TCPSocket.send(message.encode("utf-8"))

            # Receive and display the server's response
            response = TCPSocket.recv(1024).decode("utf-8")
            print(f"Server response: {response}")

    # Checks if port number is an int
    except ValueError:
        print("Error: Port number must be an integer.")
    # Checks if client can connect to the server
    except (socket.gaierror, ConnectionRefusedError):
        print("Error: Could not connect to the server. Please check the IP address and port number.")
    finally:
        TCPSocket.close()
