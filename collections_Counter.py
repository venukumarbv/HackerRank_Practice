'''
Demo to understand collections.Counter
Counter creates a dictionary of items:repetition
Output would be :

['t', 'e', 's', 't', 't', 'e', 's', 't', 'i', 'n', 'g']
t repeats 4 times
e repeats 2 times
s repeats 2 times
i repeats 1 times
n repeats 1 times
g repeats 1 times

'''
from collections import Counter

L = ['test', 'testing']
l1 = []
[l1.append(ch) for word in L for ch in word ]
print(l1)
d = Counter(l1)

for k,v in d.items():
    print('{} repeats {} times'.format(k,v))