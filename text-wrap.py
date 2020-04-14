import textwrap

# https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    words = wrapper.wrap(text=string)
    for element in words:
        print(element)
    return 

#     return newstr

# def getresult(string, max_width):
#     global count
#     newstr = string[count:count+max_width]
#     count = count+max_width
#     return newstr


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)