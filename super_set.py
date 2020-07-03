sA = set(map(int, input().split()))
number_of_sets = int(input())
l = []

for _ in range(number_of_sets):
    s = set(map(int, input().split()))
    l.append(s.intersection(sA) == s )
print(l)
print(all(l))

