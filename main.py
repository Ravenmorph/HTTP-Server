import socket

def parse_request(request_data):
    lines = request_data.split('\r\n')
    start_line = lines[0] 
    method, path, version = start_line.split(' ')
    return method, path, version

# returns http response for a given path
def get_reponse(path):
    #mapping paths to their responses
    responses = {
        "/": "HTTP/1.1 200 OK\r\n\r\n",
    } 

    # default response if path not found
    default_response = "HTTP/1.1 404 Not Found\r\n\r\n"

    return responses.get(path, default_response)


def handle_request(client_socket):
    #read data from client
    client_socket.recv(1024) # reading a bit of data

    # send a 200 OK response
    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode())

def main():
    # Create a TCP/IP socket
    server_socket = socket.create_server(("localhost", 4221),)
    print("Server is running on port 4221.....")

    try:
        while True:
            # Wait for a connection
            print("waiting for a connection....")
            client_socket, addr = server_socket.accept()

            print(f"Connection from {addr} has been established")

            # Handle the client's request
            handle_request(client_socket)

            # Close the connection to the client
            client_socket.close()

    except KeyboardInterrupt:
        print("\n Server is shutting down. ")
    finally:
        #clean up the server socket
        server_socket.close()
        print("Server has been shut down.")

if __name__ == "__main__":
    main()
