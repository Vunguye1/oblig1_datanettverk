from socket import *
import _thread as thread


def handle_each_request(connection):  # this function will handle each connect from client

    while True:
        request = connection.recv(1024).decode()  # receive request from client/web browser.

        # check if this is the request from web browser or our custom client
        if "GET" in request:  # request from web browser
            request_lines = request.split("\n")  # there are many lines from web server request.
            request_line = request_lines[0].split(" ")  # We only take the first line which is "GET /filename HTTP/1.1"
            path = request_line[1]  # get the path
        else:  # request from client
            path = ("/" + request)  # Path to the file in system

        try:  # If the file is found
            read = open(path[1:], 'r')
            response_from_server = 'HTTP/1.1 200 OK\n\n' + read.read()  # get the contents from HTML-file
        except FileNotFoundError:  # If the file is not found
            response_from_server = 'HTTP/1.1 404 Not Found'

        # stop connecting with server when users request "stop"
        if request == "stop":
            break
        connection.send(response_from_server.encode())  # send data back from server to client
    connection.close()  # close connection


def main():
    # define which client you will connect to
    server_Port = 2609
    server_Host = 'localhost'

    server_Socket = socket(AF_INET, SOCK_STREAM)  # create a socket
    server_Socket.bind((server_Host, server_Port))  # bind the address of connection from client to the socket
    server_Socket.listen(1)  # activate listening on the socket

    print("Vu-server is ready to receive ur message")

    while True:
        connection_Socket, addr = server_Socket.accept()  # accept connections from the outside.
        # Create a new socket for that connection on return
        # -> server can use connection_Socket to communicate with client/web browser
        print(f"Server connected by the following address: {addr}")  # Update addresses from differents clients
        thread.start_new_thread(handle_each_request, (connection_Socket,))  # threading for handling multiple clients
    # if there is no client, the server will close
    server_Socket.close()  # close the server socket when there is no one


if __name__ == '__main__':
    main()
