# multithreading - run two function parallely with some delay
# first hello then hi in this order five time
from threading import Thread
from time import sleep

# sleep is like settimeout

class Hello(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hi")


obj1 = Hello()
obj2 = Hi()

obj1.start()
sleep(0.5)
obj2.start()
# check multithreading3.py