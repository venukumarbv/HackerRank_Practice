if __name__ == '__main__':
    s = input()
    # True if "any" one of the iterable is True i.e., satisfying the condition c.isalnum() etc.,
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.lower() for c in s))
    print(any(c.isupper() for c in s))

