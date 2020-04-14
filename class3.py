class Car:

    # class  variable or namespace
    wheels = 4

    def __init__(self):
        # instance variable or instance namespace
        self.mileage = 60
        self.cc = 100

    def printer(self):
        print(self.mileage, self.cc, self.wheels)

    @classmethod # this is Decorator
    def printclassinstance(cls):
        print(cls.wheels)


c1 = Car()
c2 = Car()
c1.printer()
c2.printer()
c1.printclassinstance()
c2.printclassinstance()
Car.wheels = 2
c1.printer()
c2.printer()
c1.printclassinstance()
c2.printclassinstance()
c1.wheels = 3
c1.printer()
c2.printer()
c1.printclassinstance()
c2.printclassinstance()
