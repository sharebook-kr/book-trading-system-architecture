# receiver.py
import multiprocessing as mp
from pyupbit import WebSocketManager


class Receiver:
    def __init__(self, qlist):
        self.queue_to_coll = qlist[0]
        self.run()

    def run(self):
        codes = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP']
        wm = WebSocketManager("ticker", codes)

        while True:
            data = wm.get()
            self.queue_to_coll.put(data)

