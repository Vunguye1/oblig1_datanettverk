from socket import *
import sys


def request_to_server(host, port, fil_name):  # function with 3 arguments
    # create an INET, STREAMing socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # connect to the server
    try:
        client_socket.connect((host, port))
    except:
        print("Can not connect")
        sys.exit()

    # prepare request
    while True:
        # send request til server
        client_socket.send(fil_name.encode())
        message_from_server = client_socket.recv(1024)  # get the message from server
        print("From server: ", message_from_server.decode())  # print it out
        if message_from_server == "exit":
            break
    client_socket.close()


if __name__ == '__main__':
    """
    server_host = sys.argv[1]  # first argument
    server_port = int(sys.argv[2])  # second argument
    filename = sys.argv[3]  # third argument"""

    request_to_server("127.0.0.1", 2609, input("Write in filename: "))
