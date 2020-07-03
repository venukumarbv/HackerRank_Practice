from collections import OrderedDict

d = OrderedDict()

for i in range(int(input())):
    *item, price = input().split()
    name = ' '.join(item)
    if name in d.keys():
        d[name] += int(price)
    else:
        d[name] = int(price)

for i,j in d.items():
    print(i,str(j))

