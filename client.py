import sys
from socket import socket, AF_INET, SOCK_DGRAM


class Client:
    def __init__(self, ip, port, size):
        self.port = port
        self.size = size
        self.host = ip

    def start(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)

    def send(self, msg):
        self.socket.sendto(bytes(msg), (self.host, self.port))


if __name__ == "__main__":
    sender = Client("127.0.0.1", 5000, 1024)
    sender.send("cool")
