# multithreading - run two function parallely with some delay
# first hello then hi in this order five time
# what happen if i add print("i am main thread") at last which will execute
# this is like javascript it wont wait for delay main thread will execute
# how to tell wait untill above task complete and then run like async await or promise then in javascript
# see that in multithreading4.py
from threading import Thread
from time import sleep

# sleep is like settimeout

print("invoked")

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

# this will wait for parallel excution of obj1 and obj2 complete
obj1.join()
obj2.join()

# after complete main thread remaining code will run
print("I am main thread")

