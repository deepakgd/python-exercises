# constructor not working in python3

class Employee:

    def __init__(self, name, age):
	self.name = name
	self.age = age

    def display(self):
	print("my name is %s and my age is %d" % (self.name, self.age))

emp1 = Employee("Ganesh", 26);
emp2 = Employee("venkatesh", 27);
emp1.display()
emp2.display()


emp3 = Employee(name="test", age=12)
emp3.display()
