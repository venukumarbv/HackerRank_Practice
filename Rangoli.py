def print_rangoli(size):
    n = size
    L = list(map(chr,range(97,123))) # Creates a list of alphabets
    #print(L)
    x = '-'.join(L[n-1::-1] + L[1:n])
    m = len(x)
    #print(m)
    for i in range(1, n):
        print('-'.join(L[n-1:n-i:-1] + L[n-i:n]).center(m,'-'))
    for i in range(n, 0, -1):
        print('-'.join(L[n - 1:n - i:-1] + L[n - i:n]).center(m, '-'))

if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)