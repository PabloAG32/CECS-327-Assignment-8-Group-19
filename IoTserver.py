#echo server

import socket
from pymongo import MongoClient
import datetime
import pyzt

connect = "mongodb+srv://RandomPerson:ic6847@singlecollection.yv6atd4.mongodb.net/?retryWrites=true&w=majority&appName=SingleCollection"

client = MongoClient(connect)
db = client["test"]
collection = db["A7Data_virtual"]
query = ["What is the average moisture inside my kitchen fridge in the past three hours?", "What is the average water consumption per cycle in my smart dishwasher?", "Which device consumed more electricity among my three IoT devices?"]

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
        #Accepty query
        data = str(temp, "utf-8")
        output = ""
        if data == query[0]:
            past = datetime.datetime.now() - datetime.timedelta(hours = 3)
            now = datetime.datetime.now()
            list = collection.find({
                "payload.parent_asset_uid": "npf-h18-n69-9r8",
                "time" : {
                    "$gte": past,
                    "$lte": now
                    }
                })
            count = 0
            sum = 0
            avg = 0
            for x in list:
                sum += float(x["payload"]["Moisture Meter - Fridge Moisture"])
                count += 1
            avg = (sum/40)/count
            time = now.astimezone(datetime.timezone(-datetime.timedelta(hours = 8)))
            output = "As of " + str(time) + ", the average moisture in the kitchen fridge in the past three hours is " + str(avg) + " RH %"
        elif data == query[1]:
            now = datetime.datetime.now()
            time = now.astimezone(datetime.timezone(-datetime.timedelta(hours = 8)))
            list = collection.find({
                "payload.parent_asset_uid": "g4s-c60-8t2-l83"
                })
            sum = 0
            avg = 0
            for x in list:
                sum += float(x["payload"]["DishwasherWater"])
            avg = sum/120
            output = "As of " + str(time) + ", the average water consumption per cycle is " + str(avg) + " gallons."
        elif data == query[2]:
            now = datetime.datetime.now()
            time = now.astimezone(datetime.timezone(-datetime.timedelta(hours = 8)))
            voltage = 120
            list1 = collection.find({
                "payload.parent_asset_uid": "npf-h18-n69-9r8"
                })
            amp1 = 0
            for x in list1:
                amp1 += float(x["payload"]["FridgeAmmeter1"])
            list2 = collection.find({
                "payload.parent_asset_uid": "g4s-c60-8t2-l83"
                })
            amp2 = 0
            for x in list2:
                amp2 += float(x["payload"]["DishAmmeter"])
            list3 = collection.find({
                "payload.parent_asset_uid": "3daf25db-8335-45a0-af89-3798b9915853"
                })
            amp3 = 0
            for x in list3:
                amp3 += float(x["payload"]["FridgeAmmeter2"])
            e1 = amp1 * voltage
            e2 = amp2 * voltage
            e3 = amp3 * voltage
            if (e1 >= e2 and e1 >= e3):
                most = "Smart Fridge 1"
                watts = e1/1000
            elif e2 >= e3:
                most = "Smart Dishwasher"
                watts = e2/1000
            else:
                most = "Smart Fridge 2"
                watts = e3/1000
            output = "The device that has consumed the most electricity is " + most + ", which consumed " + str(watts) + " kW."
        else:
            output = "Invalid query."
        #Sends message back to client
        conn.sendall(bytes(output, "utf-8"))
        
#Closes the socket once the connection is closed
s.close()
