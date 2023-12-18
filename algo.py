from datetime import datetime

from threading import Thread
from time import sleep


class Request:
    def __init__(self, origin: str, addr: str, payload: str, datetime: datetime):
        self.origin   = origin
        self.addr     = addr
        self.payload  = payload
        self.datetime = datetime


class Algo:
    def __init__(self):
        self.others: list[str]           = []
        self.request_list: list[Request] = []
        self.duing                       = False
        self.ipaddr                      = "127.0.0.1"
        self.keep_alive_thread           = Thread(target=self.multicast_keep_alive)

    def send_multicast(self, payload):
        for i in self.others:
            self.send_request(i, payload)

    def not_responding(self, other):
        self.send_multicast(self, f"{other} not responding")

    def request_ressource(self, req: Request) -> None:
        self.request_list.append(req)
        self.request_list.sort(key=lambda x: x.datetime)
        return self.return_acceptance()

    def send_request(self, other, payload):
        # other = ...
        # payload = "request_ressource"
        # Socket
        request = Request(
            origin=self.ipaddr,
            addr=other,
            payload=payload,
            datetime=datetime.now())
        ...
        return socket(request)

    def multicast_keep_alive(self):
        while True:
            for i in self.others:
                response = self.send_request(i, "keep_alive")
                if response is not True:
                    self.not_responding(i)
            sleep(10)

    def answer_keep_alive(self):
        return True

    def add_others(self, others):
        self.others += others

    def sync(self):
        # socket + file management
        ...

    def return_acceptance(self):
        return not self.duing

    def get_acceptance(self) -> bool:
        allowed = True
        for i in self.others:
            response = self.send_request(i, "return_acceptance")
            if not response:
                allowed = False
        return allowed


algo = Algo()
algo.add_others(["",])

request = Request('test', '1', 'pay', datetime.now())
