from threading import Thread
import threading
from time import sleep

# Function that prints natural numbers from 0 - 10.
def naturalNum():
    print(threading.current_thread().getName(), " has started.")
    # Put your thread to sleep for 2 seconds.
    sleep(2)
    for x in range(10):
        print(x)

    print(threading.current_thread().getName(), " has ended.")


# Create threads.
t1 = Thread(target=naturalNum)
t2 = Thread(target=naturalNum)
t1.start()
t2.start()
