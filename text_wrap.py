import textwrap

def wrap(string, width):
    res = textwrap.fill(string,width) # Returns words is of length - width mentioned
    #res = textwrap.wrap(string, width) # Returns a list where each element is of length width
    return res

if __name__ == '__main__':
    string, width = input(), int(input())
    result = wrap(string, width)
    print(result)