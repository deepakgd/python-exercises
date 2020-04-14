mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append(7)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print(mylist[3]) # prints 4
print(mylist[4]) # prints 5
print(mylist[5]) # prints 6
print(mylist[6]) # prints 7

# prints out 1,2,3
for x in mylist:
    print(x)

print(mylist)

# remove item in list - remove item by value
mylist.remove(2)
print(mylist)

# remove item in list - remove item by index
del mylist[0] # delete index 0
print(mylist)

del mylist[-1] # delte last item
print(mylist)

# remove multiple items - remove index 1 and 2 (before 3 index delete data)
del mylist[1:3]
print(mylist)

# remove all items in array or make empty array
del mylist[:]
print(mylist)

# remove all items in array {option 2} - comment above code and then try Equivalent to del mylist[:].
# mylist.clear()

# remove varibale - if u try print this mylist it will throw error as mylist not defined - u can do this to other type of variable also
del mylist 
