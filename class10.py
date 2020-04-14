# priting memory address isssue fixer to value
# by default __str__ will call while printing

class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def show(self):
        print(self.m1, self.m2)

    def add(self):
       return self.m1 + self.m2

    # this function will overwrite the printing if memory into value 
    def __str__(self):
        return f'{self.m1} {self.m2}'


s1 = Student(1,2)

# what happen if you print s1
print(s1) # now this will print tuple of m1 and m2

# what happen if i print variable it will proint value like below
a = 1
print(a)