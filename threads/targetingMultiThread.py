from threading import Thread
import threading

def evenOdd():
    evenNum()
    # Print thread.
    #print(threading.current_thread().getName())
    oddNum()

def evenNum():
    print("Even numbers are: ")
    for x in range(10):
        if x % 2 == 0:
            print(x)

    print(threading.current_thread().getName())

def oddNum():
    print("Odd numbers are: ")
    for x in range(10):
        if x % 2 != 0:
            print(x)

# Make thread to target above function.
# The evenNum and oddNum functions are apart of the evenOdd thread too as they are in the evenOdd function that is
# being targeted in the below thread we created.
t = Thread(target=evenOdd, name="evenOdd Thread")
t.start()
