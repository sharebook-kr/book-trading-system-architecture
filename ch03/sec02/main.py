# main.py
import multiprocessing as mp
from collector import Collector
from receiver import Receiver


def main():
    queue_recv_to_coll = mp.Queue()
    queue_list = [queue_recv_to_coll]

    # Receiver
    proc_recv = mp.Process(target=Receiver, name="Receiver", args=(queue_list,))
    proc_recv.start()

    # Collector
    proc_coll = mp.Process(target=Collector, name="Collector", args=(queue_list,))
    proc_coll.start()

    proc_recv.join()
    proc_coll.join()


if __name__ == "__main__":
    main()
