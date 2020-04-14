# multithreading - run two function parallely
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")

obj1 = Hello()
obj2 = Hi()

# we will call function by obj1.run() but here we have to call like obj1.start() because threading internal will call
# run function 
obj1.start()
obj2.start()

# now two function run parallely sometime u can see collition like HelloHi 
#check multithreading2.py
        