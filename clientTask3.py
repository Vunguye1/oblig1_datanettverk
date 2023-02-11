from socket import *
import sys

server_host = "127.0.0.1"  # first argument
server_port = 2609  # second argument
# create an INET, STREAMing socket
client_socket = socket(AF_INET, SOCK_STREAM)

# connect to the server
try:
    client_socket.connect((server_host, server_port))
except:
    print("Can not connect")
    sys.exit()

# prepare request
while True:
    # send request til server
    fil_name = input("File name? ")
    client_socket.send(fil_name.encode())
    message_from_server = client_socket.recv(1024)  # get the message from server
    print("From server: ", message_from_server.decode())  # print it out
    if message_from_server == "exit":
        break
client_socket.close()
