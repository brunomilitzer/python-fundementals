from threading import *


class BookMyBus:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        # self.lock = Lock()
        self.lock = Semaphore()

    def buy(self, seats_requested):
        self.lock.acquire()
        print("Total seats available: ", self.available_seats)

        if self.available_seats >= seats_requested:
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the Ticket")
            self.available_seats -= seats_requested
        else:
            print("Sorry no more seats available")

        self.lock.release()


obj = BookMyBus(10)

t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(4,))

t1.start()
t2.start()
t3.start()
