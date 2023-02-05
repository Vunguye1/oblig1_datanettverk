from socket import *


def request_to_server(server_host, server_port, path):
        

        # create an INET, STREAMing socket
        client_socket = socket(AF_INET, SOCK_STREAM)

        # bind the socket to localhost, and a well-known port
        client_socket.connect((server_host,server_port))
                # https://stackoverflow.com/questions/7334199/getaddrinfo-failed-what-does-that-mean

        # prepare request
        request = f"GET {path} HTTP/1.1\n\n"

        # send request til server
        client_socket.send(request.encode()) 
        response = ''

        while True:
                message_from_server = client_socket.recv(1024) # get back message from server
                if not message_from_server:
                        break
                response += message_from_server

        print("From Server: " + response) # print the response from server to terminal
        client_socket.close()
