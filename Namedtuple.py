from collections import namedtuple

n = int(input())
header = input().split()
Student = namedtuple('Student', header)
l = []

for i in range(n):
    det = input().split()
    info = Student(det[0],det[1],det[2],det[3])
    l.append(int(info.MARKS))

print((sum(l))/len(l))

