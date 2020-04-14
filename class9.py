# operator overloading

class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def show(self):
        print(self.m1, self.m2)

    def add(self):
       return self.m1 + self.m2

s1 = Student(1,2)
s1.show()
print(s1.add())
s2 = Student(2,2)
s2.show()
print(s2.add())

# what happen if you print s1
print(s1) # this is printing address of memery

# what happen if i print variable it will proint value like below
a = 1
print(a)
# to show value of object check class10.py