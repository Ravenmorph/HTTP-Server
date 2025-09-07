import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)


server_socket.bind((SERVER_HOST , SERVER_PORT ))
server_socket.listen(5)
print("Listening ON PORT", SERVER_PORT)

while True:
    client_socket , client_address = server_socket.accept()
    request = client_socket.recv(1500).decode(errors="ignore")
    print(request)

    header = (request.split("\n"))
    first_header_components = header[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if path =="/":
        fin = open('index.html')
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK\n\n' + content
        client_socket.sendall(response.encode())
        client_socket.close()