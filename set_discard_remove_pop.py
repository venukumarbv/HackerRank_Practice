n = int(input())
s = set(map(int, input().split()))
comm_len = int(input())

for i in range(comm_len):
    com, *ele = input().split()
    if com == 'pop':
        s.pop()
    elif com == 'remove':
        s.remove(int(ele[0]))
    elif com == 'discard':
        s.discard(int(ele[0]))
print(sum(s))