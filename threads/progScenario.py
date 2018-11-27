from threading import *


class flightReservation:
    # create a lock.
    l = Lock()

    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    # Lock becomes acquired by the first thread.
    # So the second thread will wait until the first thread releases the lock.
    # l.acquire()
    # OR can be done using Semaphores.
    l = Semaphore()

    def buy(self, ticketRequested):
        # the number of tickets requested should be less than or equal to the number of tickets left.
        if self.ticket_left >= ticketRequested:
            print("Your ticket is confirmed.")
            print("Please make a payment and take your ticket.")
            print("---------------------------------------------")
            self.ticket_left -= ticketRequested
        else:
            print("There is not enough tickets remaining.")
            print("---------------------------------------------")

    # First thread will then release the thread so the second thread can use the function.
    l.release()


# We have 10 tickets left.
myObj = flightReservation(10)

# Create threads.
# Makes request for 3 tickets.
t1 = Thread(target=myObj.buy, args=[3])
# Makes request for 4 tickets.
t2 = Thread(target=myObj.buy, args=[4])
# Makes request for 3 tickets.
t3 = Thread(target=myObj.buy, args=[3])

t1.start()
t2.start()
t3.start()
