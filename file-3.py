#!/usr/bin/python3

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10) # remove 10 to read full file
print ("Read String is : ", str)



# Close opened file
fo.close()
