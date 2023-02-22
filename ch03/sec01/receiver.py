import multiprocessing as mp
from pyupbit import WebSocketManager
import pprint


class Receiver:
    def __init__(self):
        self.run()

    def run(self):
        codes = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP']
        wm = WebSocketManager("ticker", codes)

        while True:
            data = wm.get()
            pprint.pprint(data)

if __name__ == "__main__":
    proc_receiver = mp.Process(target=Receiver, name="Receiver")
    proc_receiver.start()
    proc_receiver.join()