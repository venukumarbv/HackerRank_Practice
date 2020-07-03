def reverse_words(input_string):
    # Write your code here
    ls = input_string.split()
    print(ls)
    res = []
    n = len(ls)

    for word in ls:
        if word.istitle():
            res.append(word[::-1].title())
        else:
            res.append(word[::-1])
    op = ' '.join(res)
    print(op)

reverse_words(input())