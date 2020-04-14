class A:

    def __init__(self):
        print("init of A")


    def feature1(self):
        print("Feature 1")

class B(A):
    
    # we have init of b so it wont call init of b to call init of A see class6.py
    def __init__(self):
        print("init of B")

    def feature2(self):
        print("Feature 2")


b = B()
b.feature1()
b.feature2()