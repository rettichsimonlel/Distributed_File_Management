import socket


class _socket:
    def __init__(self, sock=None) -> None:
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection = None

    def listen_(self):
        self.sock.bind(('', 80))
        self.sock.listen(10)
        self.connection, address = self.sock.accept()
        return self.connection, address

    def receive_request(self):
        if self.connection is None:
            raise ValueError("Connection is not established.")

        msg = self.connection.recv(1024)
        msg = msg.decode("utf-8")
        return msg

    def receive_file(self, filename):
        with open(filename, 'wb') as file:
            data = self.connection.recv(1024)
            while data:
                file.write(data)
                data = self.connection.recv(1024)
        print(f"File {filename} received successfully")

    def send_request(self, ip, port, msg) -> bool:
        try:
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_socket.connect((ip, port))
            send_socket.send(msg.encode("utf-8")[:1024])
            send_socket.close()
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
