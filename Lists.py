if __name__ == '__main__':
    n = int(input()) # Takes the maximm number of commands
    L = [] # Initialize an empty List

    for _ in range(n): # Iterate for n commands
        com, *ele_obj = input().split() # Unpacking Commands and Elemets_object using *

        #elem = [int(x) for x in ele_obj] # Converting element and obkect into integers

        elem = list(map(int, ele_obj))
        #print(elem)

        if com.lower() == 'insert':
            L.insert(elem[0], elem[1])

        elif com.lower() == 'print':
            print(L)

        elif com.lower() == 'remove':
            L.remove(elem[0])

        elif com.lower() == 'append':
            L.append(elem[0])

        elif com.lower() == 'sort':
            L.sort()

        elif com.lower() == 'pop':
            L.pop()

        elif com.lower() == 'reverse':
            L.reverse()

