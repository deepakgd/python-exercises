class Computer:
    def __init__(self):
        print("invoked")

    def config(self):
        print("hello config")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()