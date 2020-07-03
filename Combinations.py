from itertools import combinations

st, ln = input().split()
for i in range(int(ln)):
    com = [''.join(x) for x in combinations(sorted(st), i+1)]
    print(*com,sep='\n')