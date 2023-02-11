from socket import *
import sys

server_host = "127.0.0.1"
server_port = 2609

# create an INET, STREAMing socket
client_socket = socket(AF_INET, SOCK_STREAM)

# connect to the server
try:
    client_socket.connect((server_host, server_port))
except:
    print("Can not connect")
    sys.exit()

# As long as the server is still connected
while True:
    # Ask what file the user want to access. I intentionally stop the program from sending request continuously
    fil_name = input("File name? ")
    client_socket.send(fil_name.encode())  # send request til server
    message_from_server = client_socket.recv(1024)  # get the message from server
    print("From server: ", message_from_server.decode())  # print it out
    if message_from_server == "exit":
        break
client_socket.close()  # close the socket
