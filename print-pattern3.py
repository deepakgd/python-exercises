# method 1
# n = 4
# for i in range(5):
#     for j in range(n):
#         print("#", end=" ")
#     n -= 1
#     print()

# method 2

for i in range(5):
    for j in range(4-i):
        print("#", end=" ")

    print()