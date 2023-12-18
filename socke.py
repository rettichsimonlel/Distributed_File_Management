import socket


class socket_():

    def __init__(self, sock=None) -> None:
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        self.sock.connect((ip, port))

    def listen_(self):
        self.sock.bind(('', 80))
        self.sock.listen(10)
        address = self.sock.accept()
        return print('Connected with ', address)

    def receive_request(self):
        msg = self.sock.recv(1024)
        msg.decode("utf-8")
        return msg

    def send_request(self, msg):
        self.sock.send(msg.encode("utf-8")[:1024])
