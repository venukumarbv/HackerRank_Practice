def mutable_string(st, pos, ch):
    ms = list(st) # Converting a string into a list so that we can alter the List
    ms[pos] = ch # Changing "pos" value to "ch"
    ms = ''.join(ms) # Converting a list to a string
    return ms

if __name__ == '__main__':
    s = input()
    pos, char = input().split()
    print(mutable_string(s,int(pos),char))
