from collections import defaultdict
d = {}
d['v1'] = 1
print(d)
#erro
#print(d['v2'])
d2 = defaultdict(lambda : 'Valor default')
d2['v1'] = 1
print(d2['v2'])
print(d2)
