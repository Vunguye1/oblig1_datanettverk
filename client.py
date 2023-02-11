from socket import *


def request_to_server(server_host, server_port, path):
    # create an INET, STREAMing socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # connect to the server
    client_socket.connect((server_host, server_port))

    # prepare request
    request = f"GET {path} HTTP/1.1\n\n"

    # send request til server
    client_socket.send(request.encode())
    response = ''

    while True:
        message_from_server = client_socket.recv(1024)  # get back and read data from server
        if not message_from_server:
            break
        response += message_from_server  # add data from server to our message-variable

    print("From Server: " + response)  # print the response from server to terminal

    # close the socket
    client_socket.close()

# viet funksjon kall på The following is an input command format to run the client.
# client.py server host server port filename
