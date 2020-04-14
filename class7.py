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

    # what happen if there is no init in sub class. it will call super call init but here we have
    # two super class. it will call A because it is in first. Left to right order
    # check class8.py 

    def feature1(self):
        print("Feature 1-C")

    def featureb(self):
        print("Feature C") 


c = C()