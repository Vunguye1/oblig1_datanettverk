from socket import *


serverName = '127.0.0.1'
serverPort = 5050 # use a nice high number (4 digits) if we r playing around

# create an INET, STREAMing socket
client_socket = socket(AF_INET, SOCK_STREAM)

# bind the socket to localhost, and a well-known port
client_socket.connect((serverName,serverPort))
        # https://stackoverflow.com/questions/7334199/getaddrinfo-failed-what-does-that-mean

# input from client
sentence = input("Input lowercase sentence: ")



# become a server socket
client_socket.send(sentence.encode()) # send input til server
modified_Sentence = client_socket.recv(1024) # get back message from server



print("From Server:", modified_Sentence.decode()) # print message from server to terminal
client_socket.close()
