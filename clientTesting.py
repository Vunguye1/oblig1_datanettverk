from socket import *

serverName = '127.0.0.1'
serverPort = 2609  # use a nice high number (4 digits) if we are playing around

# create an INET, STREAMing socket
client_socket = socket(AF_INET, SOCK_STREAM)

# bind the socket to localhost, and a well-known port
client_socket.connect((serverName, serverPort))

# input from client
sentence = input("Write in the file you want to connect to: ")

# become a server socket
client_socket.send(sentence.encode())  # send input til server
message_from_server = client_socket.recv(1024)  # get back message from server

print("From Server:", message_from_server.decode())  # print message from server to terminal
client_socket.close()
