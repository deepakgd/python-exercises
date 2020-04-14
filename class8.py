# multiple inheritance init call analysis
class A:

    def __init__(self):
        print("init of A")


    def feature1(self):
        print("Feature 1-A")


    def featurea(self):
        print("Feature A")

class B:
    
    def __init__(self):
        print("init of B")

    def feature1(self):
        print("Feature 1-B")

    def featureb(self):
        print("Feature B")

class C(A, B):

    def __init__(self):
        super().__init__() # this will call A class init because Left to right order
        # super().__init__() # even if you call again this will call A only
        print("init of C")

    def feature1(self):
        print("Feature 1-C")

    def featureb(self):
        print("Feature C") 


c = C()