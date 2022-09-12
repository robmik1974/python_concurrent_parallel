"""Program showing creation of threads that execute neverending loops"""

import os
import threading

def main():
    """Display information about resuorces befor and after creating threads"""
    show()
    print("\nStarting 12 CPU wasters")
    create_tread(number=12)
    show()

def create_tread(number):
    """Create number of threads"""
    for _ in range(number):
        threading.Thread(target=cpu_waster).start()

def show():
    """Display based information about allocated/used resurces"""
    print(os.getpid())
    print(threading.active_count())
    for thread in threading.enumerate():
        print(thread)

def cpu_waster():
    """Neverending loop doing nothing"""
    while True:
        pass

if __name__ == "__main__":
    main()
