import multiprocessing as mp


class Receiver:
    def __init__(self, *args):
        print("__init__", args, type(args), mp.current_process().name)
        self.run()

    def run(self):
        print("run")


if __name__ == "__main__":
    proc_receiver = mp.Process(target=Receiver, name="Receiver", args=("data1",  "data2"))
    proc_receiver.start()
    proc_receiver.join()
