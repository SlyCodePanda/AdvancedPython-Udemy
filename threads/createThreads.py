from threading import Thread
import threading

# Function that prints even numbers up to 20.
def evenNumber():
    for x in range(20):
        if x % 2 == 0:
            print(x)

    # change the name of the current thread then print.
    threading.current_thread().name = "New thread"
    a = threading.current_thread().getName()
    print(a)


# Create an instance of the thread class.
# Now the above function is a part of this thread, It no longer resides in the main thread.
# It is a subset of the main thread.
t = Thread(target=evenNumber)

# Start the thread.
t.start()

