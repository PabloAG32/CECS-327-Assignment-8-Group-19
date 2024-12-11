#echo server

import socket

#Requests IP address and port number
host = str(input("Enter the server IP address: "))
port = int(input("Enter the port number: "))

#Opens socket and automatically closes
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds socket to port
s.bind((host, port))
#Listens for and accepts incoming messages
s.listen()
#Waits for a connection
conn, addr = s.accept()
    

#Receives data
with conn:
    print(f"Connected by {addr}")
    while True:
        temp = conn.recv(1024)
        if not temp:
            break
        print(f"Received message: {temp}")
        #Changes message to upper case
        string = str(temp, "utf-8")
        data = string.upper()
        #Sends message back to client
        conn.sendall(bytes(data, "utf-8"))
        
#Closes the socket once the connection is closed
s.close()