
m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
# perform union operation on the differences
l = sorted(list((s1-s2).union(s2-s1)))
print(*l,sep='\n')