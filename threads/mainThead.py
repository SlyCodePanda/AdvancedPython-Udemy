# How to access the main thread.
import threading

# Setting the name of a main thread.
threading.current_thread().name = "Hello"
print(threading.current_thread().getName())