from socket import *

server_Port = 2609
server_Host = 'localhost'
server_Socket = socket(AF_INET, SOCK_STREAM)
server_Socket.bind((server_Host,server_Port))
server_Socket.listen(1)

print("Vu-server is ready to receive ur message")

while True:
    # accept connections from outside
    connection_Socket, addr = server_Socket.accept()
    request = connection_Socket.recv(1024).decode('utf-8') # receive request from client.

    request_lines = request.split("\n") # A list of request lines
    request_each_line = request_lines[0].split(' ') # Take only one like at a time for handling
    
    
    Http_method = request_each_line[0] # get the Http method

    path = request_each_line[1] # get the path as well
    

    response_from_server = 'HTTP/1.1 404 Not Found\n\n'

    if Http_method == "GET":
        try:
            with open(path[1:], 'r') as f:
                response_from_server = 'HTTP/1.1 200 OK\n\n' + f.read() # get the contents from HTML-file
        except FileNotFoundError:
            continue


    connection_Socket.sendall(response_from_server.encode())
    print(response_from_server.encode())
    connection_Socket.close()
    