import random
import time

from prometheus_client import Counter, start_http_server

ticks = Counter("ticks_total", "Number of ticks")

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        ticks.inc(random.randint(1, 5))
        time.sleep(0.2)
