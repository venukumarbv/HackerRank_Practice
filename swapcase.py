def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    #ss = ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in s)
    #print(ss)
    print(swap_case(s))