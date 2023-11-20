import socket
import sys


def send_message(address, message, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (address, port)

    client_socket.sendto(message.encode(), server_address)
    (response,) = client_socket.recvfrom(1024)
    print(f"Received response: {response.decode()}")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            print("Usage: python client.py <message> <address> <port>")
            sys.exit(1)

        message = sys.argv[1]
        address = sys.argv[2]
        port = int(sys.argv[3])
        send_message(address, message, port)
    except Exception as e:
        print(f"Error occurred: {e}")
