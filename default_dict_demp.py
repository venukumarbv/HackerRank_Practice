from collections import defaultdict

d = defaultdict(list)
d['python'].append('awesome')
d['c'].append('good')
d['python'].append('I love it')

print(d.values())