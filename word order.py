# Enter your code here. Read input from STDIN. Print output to STDOU
from collections import Counter

num_words = int(input())
l = []

for i in range(num_words):
    word = input()
    l.append(word)

x = Counter(l)
print(len(x))
print(*x.values())