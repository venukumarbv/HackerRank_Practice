from collections import deque

d =deque()
n = int(input())
for i in range(n):
    com, *ele = input().split()
    if com == 'append':
        d.append(int(ele[0]))
    elif com == 'appendleft':
        d.appendleft(int(ele[0]))
    elif com == 'pop':
        d.pop()
    elif com == 'popleft':
        d.popleft()
print(*d)

