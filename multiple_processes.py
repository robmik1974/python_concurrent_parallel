"""Program showing creation of processes that execute neverending loops"""

import multiprocessing as mp
import threading
import os


def main():
    """Display information about resuorces befor and after creating processes"""
    display_based_info()
    create_process(number=12)
    display_based_info()

def create_process(number):
    """Create number of processes"""
    for _ in range(number):
        mp.Process(target=waster).start()

def display_based_info():
    """Display based information about allocated/used resurces"""
    print(os.getpid())
    print(threading.active_count())
    for thread in threading.enumerate():
        print(thread)

def waster():
    """Neverending loop doing nothing"""
    while True:
        pass

if __name__ == "__main__":
    main()
    