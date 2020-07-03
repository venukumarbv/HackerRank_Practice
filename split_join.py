def split_join(line):
    s = line.split(" ")
    s = '-'.join(s)
    return s


if __name__ == '__main__':
    line = input()
    print(split_join(line))
