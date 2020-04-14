class A:

    def __init__(self):
        print("init of A")


    def feature1(self):
        print("Feature 1")

class B(A):
    
    def __init__(self):
        super().__init__()
        print("init of B")

    def feature2(self):
        print("Feature 2")


b = B()
b.feature1()
b.feature2()