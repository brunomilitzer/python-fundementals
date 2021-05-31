from threading import *


def display_numbers():
    i = 0
    current_thread().setName("My Thread")
    print(current_thread().getName())
    while i <= 10:
        print(i)
        i += 1


print(current_thread().getName())
t = Thread(target=display_numbers)
t.start()