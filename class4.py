class A:

    def __init__(self):
        print("init of A")


    def feature1(self):
        print("Feature 1")

class B(A):
    # if there is no init function in B class it will automatically call A init. check class5.py
    def feature2(self):
        print("Feature 2")


b = B()
b.feature1()
b.feature2()