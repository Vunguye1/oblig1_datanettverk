from socket import *
server_Port = 5050
server_Host = 'localhost'
server_Socket = socket(AF_INET, SOCK_STREAM)
server_Socket.bind((server_Host,server_Port))
server_Socket.listen(1)
print("Vu-server is ready to receive ur message")

while True:
    # accept connections from outside
    connection_Socket, addr = server_Socket.accept()

    message = connection_Socket.recv(1024).decode() # receive message from client
    capitalized_MSG = message.upper() # make it capitalized 
    connection_Socket.send(capitalized_MSG.encode()) # send back to client as signal
    connection_Socket.close()
    print(message) # print the massage to our client