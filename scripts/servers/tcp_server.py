import socket
import sys


def create_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server is running on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        request_data = client_socket.recv(1024).decode()
        print(f"Received request:\n{request_data}")

        response = request_data
        client_socket.sendall(response.encode())

        client_socket.close()


if __name__ == "__main__":
    try:
        port = int(sys.argv[1]) if len(sys.argv) > 1 else 80
        create_server(port)
    except Exception as e:
        print(f"Error occurred: {e}")
