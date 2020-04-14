x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
print("before", x)    
foo()
print("after",x)