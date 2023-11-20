import socket
import sys


def create_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", port))
    print(f"Server is running on port {port}...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received message '{data.decode()}' from {client_address}")

        response = data
        server_socket.sendto(response, client_address)


if __name__ == "__main__":
    try:
        port = int(sys.argv[1]) if len(sys.argv) > 1 else 80
        create_server(port)
    except Exception as e:
        print(f"Error occurred: {e}")
