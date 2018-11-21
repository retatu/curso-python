s = set()
s.clear()
s = {1,2,3}
s2 = s.copy()
s2.add(4)
s2.add(5)
print(s2.difference(s))
#Adiciona no s apenas os valores diferentes dos dois sets
s2.difference_update(s)
print(s2)
s2 = {3,4,5}
s = {1,2,3}
print(s.intersection(s2))
#Adiciona no s apenas os valores iguais dos dois sets
s.intersection_update(s2)
print(s)
 s2 = {3,4,5}
s = {1,2,3}
print(s.union(s2))
