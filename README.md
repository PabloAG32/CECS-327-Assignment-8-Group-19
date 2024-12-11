# CECS-327-Assignment-8-Group-19
This is going to be our repo for our code for assignment 8 for CECS 327 Fall 2024 Group 19

Instructions for running client, server, and database:
1. Ensure your devices are sending data to the database
2. Connect your database to the IoTserver.py by setting the variable "connection" to your MongoDB link
3. Replace the database and collection names with the corresponding names in your MongoDB cluster
4. Run IoTserver.py in the command terminal
5. Enter the server's IP address and preferred port
6. Run IoTclient.py in the command terminal
7. Enter the server's IP address and port that you used previously
8. Enter one of the three queries:
   - "What is the average moisture inside my kitchen fridge in the past three hours?"
   - "What is the average water consumption per cycle in my smart dishwasher?"
   - "Which device consumed more electricity among my three IoT devices?"
9. After receiving the output, enter "y" if you wish to query again or "n" if you wish to stop
10. If you enter "y", repeat from step 8
