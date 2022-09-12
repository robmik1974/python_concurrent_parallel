"""Execution of two threads counting at the same time"""

import threading
import time

counting = True

def main():
    """Create threads and start threads running for n_seconds"""
    n_seconds = 2
    threading.Thread(target=count, name="Counter_1").start()
    threading.Thread(target=count, name="Counter_2").start()
    time.sleep(n_seconds)
    global counting
    counting = False

def count():
    """Counting function runs by each thread"""
    name = threading.current_thread().getName()
    counter = 0
    while counting:
        counter += 1
        print(f"{name} added 1 !")
    print(f"{name} counted to {counter} in 2 seconds")

if __name__ == "__main__":
    main()