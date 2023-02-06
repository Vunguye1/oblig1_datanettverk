from socket import *

#define which client you will connect to
server_Port = 2609 
server_Host = 'localhost'

server_Socket = socket(AF_INET, SOCK_STREAM) # create a socket
server_Socket.bind((server_Host,server_Port)) # bind the adress of connection from client to the socket
server_Socket.listen(1) #activate listening on the oscket

print("Vu-server is ready to receive ur message")

while True:
    
    connection_Socket, addr = server_Socket.accept()  # accept connections from the outside. Create a new socket for that connection on return
    # -> server can use connection_Socket to communicate with client

    request = connection_Socket.recv(1024).decode('utf-8') # receive request from client.

    request_lines = request.split("\n") # A list of request lines
    request_each_line = request_lines[0].split(' ') # Take only one like at a time for handling
    
    
    Http_method = request_each_line[0] # get the Http method

    path = request_each_line[1] # get the path as well
    

    response_from_server = 'HTTP/1.1 404 Not Found\n\n'

    if Http_method == "GET":
        try:
            read = open(path[1:], 'r')
            response_from_server = 'HTTP/1.1 200 OK\n\n' + read.read() # get the contents from HTML-file
        except FileNotFoundError:
            continue


    connection_Socket.sendall(response_from_server.encode()) # send data back from server to client over the connection
    print(response_from_server.encode())

    # close both sockets
    connection_Socket.close()
    server_Socket.close()
    