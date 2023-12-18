from socke import _socket

from datetime import datetime
from threading import Thread
from time import sleep

class Request:
    def __init__(self, origin: str, addr: str, payload: str, datetime: datetime):
        self.origin   = origin
        self.addr     = addr
        self.payload  = payload
        self.datetime = datetime
        self.accept   = False
        self.received = False

    def __str__(self):
        return f"Request(origin={self.origin}, addr={self.addr}, payload={self.payload}, datetime={self.datetime}, accept={self.accept}, received={self.received})"

        
class Algo:
    def __init__(self):
        self.others: list[str]           = []
        self.request_list: list[Request] = []
        self.duing                       = False
        self.ipaddr                      = "127.0.0.1"
        self.ipport                      = "7450"
        self.keep_alive_thread           = Thread(target=self.multicast_keep_alive)

    async def __send_multicast(self, payload) -> list[Request]:
        requests = []
        for i in self.others:
            request = await self.send_request(i, payload)
        return requests
                
    def not_responding(self, other):
        self.__send_multicast(self, f"{other} not responding")

    def request_ressource(self, req: Request) -> None:
        self.request_list.append(req)
        self.request_list.sort(key=lambda x: x.datetime)
        return self. return_acceptance()
        
    async def send_request(self, other, payload) -> Request:
        # other = ...
        # payload = "request_ressource"
        # Socket
        request = Request(
            origin=self.ipaddr,
            addr=other,
            payload=payload,
            datetime=datetime.now())
        socke = _socket()
        request.received = socke.send_request(other, int(self.ipport), payload)
        return request
        # return socket(request)

    def multicast_keep_alive(self):
        while True:
            if self.__send_multicast("keep_alive") == False:
                ... # self.not_responding
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
        return self.__send_multicast(self, "return_acceptance")

async def main():
    algo = Algo()
    algo.add_others(["172.31.182.123"])
    request = await algo.send_request("172.31.182.123", "Weak minded")
    print(request)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
