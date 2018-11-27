from threading import Thread
import threading


# Create thread by extending the Thread class (inheritance).
class myThread(Thread):
    def run(self):
        print("Egyptian Pyramid")
        print(threading.current_thread().getName())
        for x in range(0, 5):
            for j in range(0, x+1):
                print("*", end=" ")
            print("\r")


# Create and start.
obj = myThread()
obj.start()
