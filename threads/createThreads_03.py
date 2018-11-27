from threading import Thread
import threading


# Create Threads without extending the Thread class (no inheritance).
class MyThread():
    def naturalNum(self):
        if threading.current_thread().getName() == "Thread-1":
            for x in range(10):
                print(x)
        else:
            print("Hey this is not Thread-1")


myObj = MyThread()
# Make this function a apart of this Thread class.
t = Thread(target=myObj.naturalNum)
t.start()
