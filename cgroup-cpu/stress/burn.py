import multiprocessing as mp
import os


def burn():
    x = 0
    while True:
        x = (x + 1) % 1_000_000


if __name__ == "__main__":
    workers = int(os.environ.get("WORKERS", mp.cpu_count()))
    procs = [mp.Process(target=burn) for _ in range(workers)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
