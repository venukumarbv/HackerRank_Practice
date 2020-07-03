test_cases = int(input())

for i in range(test_cases):
    nA = int(input())
    sA = set(map(int, input().split()))
    nB = int(input())
    sB = set(map(int, input().split()))
    common = sA.intersection(sB)
    if common == sA:
        print('True')
    else:
        print('False')
