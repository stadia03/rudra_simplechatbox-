from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys


class Server:
    def __init__(self, port, size):
        self.port = port
        self.size = size
        self.host = gethostbyname("0.0.0.0")

    def start(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        print("Sending server started on port {self.port}")

    def recv(self):
        (data, addr) = self.socket.recvfrom(self.size)
        return data

    def close(self):
        self.socket.close()


if __name__ == "__main__":
    srv = Server(5000, 1024)
    srv.start()
    while True:
        print(srv.recv())
