from socket import *

# define which client you will connect to
server_Port = 2609
server_Host = 'localhost'

server_Socket = socket(AF_INET, SOCK_STREAM)  # create a socket
server_Socket.bind((server_Host, server_Port))  # bind the adress of connection from client to the socket
server_Socket.listen(1)  # activate listening on the oscket

print("Vu-server is ready to receive ur message")

connection_Socket, addr = server_Socket.accept()  # accept connections from the outside. Create a new socket for that connection on return
# -> server can use connection_Socket to communicate with client

request = connection_Socket.recv(1024).decode('utf-8')  # receive request from client.
path = ("/" + request)  # Path to the file in system

response_from_server = ''
try:  # If the file is found
    read = open(path[1:], 'r')
    response_from_server = 'HTTP/1.1 200 OK\n\n' + read.read()  # get the contents from HTML-file
except FileNotFoundError:  # If the file is not found
    response_from_server = 'HTTP/1.1 404 Not Found'

connection_Socket.send(response_from_server.encode())  # send data back from server to client over the connection

# close both sockets
connection_Socket.close()
server_Socket.close()
