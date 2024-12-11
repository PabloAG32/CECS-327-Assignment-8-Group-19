#echo client

import socket

while True:
    #Requests IP address, port number, and message to be sent
    host = str(input("Enter the server IP address: "))
    port = int(input("Enter the port number: "))

    #Opens socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        #Attempts to connect to socket at given server and port
        s.connect((host, port))
    except:
        print("Invalid IP address or port number")
        continue
    break

#Loops as long as user wants to send messages
while True:
    #Loops until user enters valid query
    while True:
        mess = str(input("Enter the message to be sent: "))
        if mess in ["What is the average moisture inside my kitchen fridge in the past three hours?", "What is the average water consumption per cycle in my smart dishwasher?", "Which device consumed more electricity among my three IoT devices?"]:
            break
        else:
            print("Sorry, this query cannot be processed.  Please try one of the following:")
            print("1. What is the average moisture inside my kitchen fridge in the past three hours?")
            print("2. What is the average water consumption per cycle in my smart dishwasher?")
            print("3. Which device consumed more electricity among my three IoT devices?")
    #Sends message inputted above
    s.sendall(bytes(mess, "utf-8"))
            
    #Receives data returned from server
    data = s.recv(1024)
            
    print(f"Received {data}")
    
    #Asks user if they want to continue
    while True:
        print("Would you like to send another message? (Y/N)")
        cont = input().upper()
        if cont not in ('Y', 'N'):
            print("Invalid input")
        else:
            break
    if cont == "N":
        break
    else:
        pass
    
#Closes socket
s.close()
