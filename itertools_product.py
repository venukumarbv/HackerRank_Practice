from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(product(l1,l2))
print(*product(l1,l2))

