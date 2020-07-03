def print_formatted(num):
    width = len("{0:b}".format(num)) # Binary digits give maximum width so calculate the max_width using binary
    for i in range(1,num+1):
     print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)