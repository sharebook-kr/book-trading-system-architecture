# collector.py
import pprint


class Collector:
    def __init__(self, qlist):
        self.queue_from_recv = qlist[0]
        self.run()

    def run(self):
        while True:
            data = self.queue_from_recv.get()
            pprint.pprint(data)
