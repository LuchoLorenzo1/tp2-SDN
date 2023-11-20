import socket
import sys


def send_message(address, message, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))

    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Received response:\n{response}")

    client_socket.close()


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
