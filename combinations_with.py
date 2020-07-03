from itertools import combinations_with_replacement

st,len = input().split()
x = [''.join(ch) for ch in combinations_with_replacement(sorted(st), int(len))]
print(*x,sep='\n')